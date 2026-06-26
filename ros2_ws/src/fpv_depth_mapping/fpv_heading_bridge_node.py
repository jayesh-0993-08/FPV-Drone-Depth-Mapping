import math

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import ReliabilityPolicy
from rclpy.qos import HistoryPolicy
from rclpy.qos import DurabilityPolicy

from std_msgs.msg import String

from px4_msgs.msg import OffboardControlMode
from px4_msgs.msg import TrajectorySetpoint
from px4_msgs.msg import VehicleCommand
from px4_msgs.msg import VehicleLocalPosition


class FPVHeadingBridgeNode(Node):

    def __init__(self):

        super().__init__('fpv_heading_bridge_node')

        px4_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.heading = 0.0
        
        self.yaw_setpoint = 0.0
        self.first_heading_received = False
        self.pitch_input = 0
        self.roll_input = 0
        self.yaw_input = 0
        self.vertical_input = 0

        self.subscription = self.create_subscription(
            String,
            '/fpv_cmd',
            self.command_callback,
            10
        )

        self.position_sub = self.create_subscription(
            VehicleLocalPosition,
            '/fmu/out/vehicle_local_position_v1',
            self.position_callback,
            px4_qos
        )

        self.offboard_pub = self.create_publisher(
            OffboardControlMode,
            '/fmu/in/offboard_control_mode',
            10
        )

        self.trajectory_pub = self.create_publisher(
            TrajectorySetpoint,
            '/fmu/in/trajectory_setpoint',
            10
        )

        self.vehicle_command_pub = self.create_publisher(
            VehicleCommand,
            '/fmu/in/vehicle_command',
            10
        )

        self.timer = self.create_timer(
            0.05,
            self.publish_setpoint
        )

        self.get_logger().info(
            "FPV Heading Bridge Started"
        )

    def timestamp_us(self):

        return int(
            self.get_clock().now().nanoseconds / 1000
        )

    def position_callback(self, msg):

        self.heading = msg.heading

        if not self.first_heading_received:
            self.yaw_setpoint = self.heading
            self.first_heading_received = True
    def send_vehicle_command(
        self,
        command,
        param1=0.0,
        param2=0.0
    ):

        msg = VehicleCommand()

        msg.timestamp = self.timestamp_us()

        msg.command = command

        msg.param1 = param1
        msg.param2 = param2

        msg.target_system = 1
        msg.target_component = 1

        msg.source_system = 1
        msg.source_component = 1

        msg.from_external = True

        self.vehicle_command_pub.publish(msg)

    def command_callback(self, msg):

        if msg.data == "ARM":

            self.send_vehicle_command(
                VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM,
                1.0
            )
            return

        elif msg.data == "OFFBOARD":

            self.send_vehicle_command(
                VehicleCommand.VEHICLE_CMD_DO_SET_MODE,
                1.0,
                6.0
            )
            return

        elif msg.data == "LAND":

            self.send_vehicle_command(
                VehicleCommand.VEHICLE_CMD_NAV_LAND
            )
            return

        try:

            pitch, roll, yaw, vertical = map(
                int,
                msg.data.split(',')
            )

        except Exception:

            return

        self.pitch_input = pitch
        self.roll_input = roll
        self.yaw_input = yaw
        self.vertical_input = vertical
        self.get_logger().info(
            f"Received: P={pitch} R={roll} Y={yaw} T={vertical}"
        )
    def publish_setpoint(self):

        offboard = OffboardControlMode()

        offboard.timestamp = self.timestamp_us()

        offboard.position = False
        offboard.velocity = True
        offboard.acceleration = False
        offboard.attitude = False
        offboard.body_rate = False
        offboard.thrust_and_torque = False
        offboard.direct_actuator = False

        self.offboard_pub.publish(offboard)
        dt = 0.05            # timer period
        yaw_rate = 0.8       # rad/s

        self.yaw_setpoint += (
            self.yaw_input *
            yaw_rate *
            dt
        )

        # Keep angle in [-pi, pi]
        self.yaw_setpoint = math.atan2(
        math.sin(self.yaw_setpoint),
        math.cos(self.yaw_setpoint)
        )

        forward_x = math.cos(self.heading)
        forward_y = math.sin(self.heading)

        right_x = -math.sin(self.heading)
        right_y = math.cos(self.heading)

        speed = 3.0

        vx = (
            self.pitch_input * forward_x +
            self.roll_input * right_x
        ) * speed

        vy = (
            self.pitch_input * forward_y +
            self.roll_input * right_y
        ) * speed

        vz = -2.0 * self.vertical_input

        msg = TrajectorySetpoint()

        msg.timestamp = self.timestamp_us()

        msg.position = [
            float('nan'),
            float('nan'),
            float('nan')
        ]

        msg.velocity = [
            float(vx),
            float(vy),
            float(vz)
        ]

        msg.acceleration = [
            float('nan'),
            float('nan'),
            float('nan')
        ]

        msg.yaw = float(self.yaw_setpoint)

        msg.yawspeed = float(
            0.8 * self.yaw_input
        )

        self.trajectory_pub.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = FPVHeadingBridgeNode()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()

