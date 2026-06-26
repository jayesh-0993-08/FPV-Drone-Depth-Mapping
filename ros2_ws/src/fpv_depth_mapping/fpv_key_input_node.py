import pygame

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class FPVKeyInputNode(Node):

    def __init__(self):

        super().__init__("fpv_key_input_node")

        self.publisher_ = self.create_publisher(
            String,
            "/fpv_cmd",
            10,
        )

        pygame.init()

        self.screen = pygame.display.set_mode((600, 300))

        pygame.display.set_caption("FPV Controller")

        # Current control state
        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        self.throttle = 0

        self.timer = self.create_timer(
            0.02,
            self.update,
        )

        self.get_logger().info("FPV Controller Started")

    def publish_motion(self):

        msg = String()

        msg.data = (
            f"{self.pitch},"
            f"{self.roll},"
            f"{self.yaw},"
            f"{self.throttle}"
        )
        self.get_logger().info(f"Publishing: {msg.data}")
        self.publisher_.publish(msg)

        pygame.display.set_caption(
            f"P:{self.pitch} "
            f"R:{self.roll} "
            f"Y:{self.yaw} "
            f"T:{self.throttle}"
        )

    def update(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                rclpy.shutdown()
                return

            # ---------------- KEY PRESSED ----------------

            if event.type == pygame.KEYDOWN:

                # Pitch

                if event.key == pygame.K_w:
                    self.pitch = 1

                elif event.key == pygame.K_s:
                    self.pitch = -1

                # Roll

                elif event.key == pygame.K_d:
                    self.roll = 1

                elif event.key == pygame.K_a:
                    self.roll = -1

                # Yaw

                elif event.key == pygame.K_LEFT:
                    self.yaw = 1

                elif event.key == pygame.K_RIGHT:
                    self.yaw = -1

                # Throttle

                elif event.key == pygame.K_UP:
                    self.throttle = 1

                elif event.key == pygame.K_DOWN:
                    self.throttle = -1

                # Commands

                elif event.key == pygame.K_y:
                    msg = String()
                    msg.data = "ARM"
                    self.publisher_.publish(msg)

                elif event.key == pygame.K_t:
                    msg = String()
                    msg.data = "OFFBOARD"
                    self.publisher_.publish(msg)

                elif event.key == pygame.K_l:
                    msg = String()
                    msg.data = "LAND"
                    self.publisher_.publish(msg)

                elif event.key == pygame.K_SPACE:
                    msg = String()
                    msg.data = "HOVER"
                    self.publisher_.publish(msg)

                elif event.key == pygame.K_x:
                    msg = String()
                    msg.data = "KILL"
                    self.publisher_.publish(msg)

            # ---------------- KEY RELEASED ----------------

            elif event.type == pygame.KEYUP:

                if event.key in (pygame.K_w, pygame.K_s):
                    self.pitch = 0

                elif event.key in (pygame.K_a, pygame.K_d):
                    self.roll = 0

                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.yaw = 0

                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    self.throttle = 0

        self.publish_motion()

    def destroy_node(self):

        pygame.quit()

        super().destroy_node()


def main(args=None):

    rclpy.init(args=args)

    node = FPVKeyInputNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
