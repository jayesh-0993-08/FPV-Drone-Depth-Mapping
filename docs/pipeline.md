# System Pipeline

This document explains how the complete system works.

---

# Pipeline Overview

```
FPV Camera

        │

        ▼

Image Capture

        │

        ▼

ROS2 Communication

        │

        ▼

Depth Estimation

        │

        ▼

Depth Map Generation

        │

        ▼

3D Visualization
```

---

# Step 1 — Camera

The FPV camera continuously captures RGB images.

These images contain color information only.

No depth information is available at this stage.

---

# Step 2 — Image Capture

The image stream is received by the computer and converted into frames for processing.

Each frame becomes the input for the depth estimation model.

---

# Step 3 — ROS2 Communication

ROS2 acts as the communication layer.

Different nodes exchange image data and control information using ROS2 topics.

This modular architecture allows each component to work independently.

---

# Step 4 — Depth Estimation

The RGB image is processed by the depth estimation model.

Instead of predicting object classes, the model predicts the approximate distance of every pixel from the camera.

The output is a depth map.

---

# Step 5 — Depth Map

The depth map represents relative distances.

Typically:

- Bright pixels → closer objects
- Dark pixels → farther objects

The exact color representation depends on the visualization method.

---

# Step 6 — 3D Visualization

The depth map is converted into a point cloud or another 3D representation.

This allows the surrounding environment to be visualized spatially.

---

# Why is this Important?

Depth estimation enables many autonomous robotics applications, including:

- Obstacle Avoidance
- Navigation
- Mapping
- Scene Understanding
- Autonomous Flight
