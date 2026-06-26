# FPV Drone Depth Mapping

> Real-time depth estimation and 3D environment visualization using an FPV drone, ROS2, and Computer Vision.

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Python](https://img.shields.io/badge/Python-3.10-yellow)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange)

---

## 📌 Overview

Modern FPV drones usually provide only a standard RGB camera feed, allowing a pilot to see the surroundings but without any understanding of depth or the three-dimensional structure of the environment.

This project explores how an FPV drone can be combined with Computer Vision techniques to estimate depth from camera images and visualize the environment in 3D.

The long-term goal is to build perception systems that can later be integrated into autonomous UAVs for navigation, obstacle avoidance, mapping, and intelligent decision-making.

This repository documents the complete implementation, experiments, and learning process behind the project.

---

# 🎯 Objectives

The objectives of this project are:

- Capture live video from an FPV camera
- Process the video stream using ROS2
- Generate depth maps from RGB images
- Visualize the environment in 3D
- Understand the complete perception pipeline instead of treating it as a black box
- Build a reusable perception module for future autonomous robotics projects

---

# 📹 Current Features

✔ Live FPV camera streaming

✔ ROS2 communication

✔ Keyboard control

✔ Depth map generation

✔ 3D visualization

---

# 🛣️ Project Roadmap

### Version 0.1 (Current)

- FPV Camera Stream
- ROS2 Integration
- Keyboard Control
- Depth Map Generation
- Basic 3D Visualization

### Future Versions

- Improved depth estimation
- Better visualization
- Point cloud optimization
- ROS2 launch files
- Camera calibration improvements
- PX4 integration
- Onboard deployment
- Obstacle avoidance
- Autonomous navigation

---

# 🧠 How the System Works

```
             FPV Camera
                  │
                  ▼
          RGB Image Stream
                  │
                  ▼
         ROS2 Communication
                  │
                  ▼
         Depth Estimation Model
                  │
                  ▼
            Depth Map
                  │
                  ▼
        3D Environment View
```

Each stage performs a specific task:

### 1. FPV Camera

Captures the real-world environment using a standard RGB camera.

---

### 2. ROS2

ROS2 acts as the communication framework between different components of the system.

---

### 3. Depth Estimation

A depth estimation model predicts the distance of every pixel from the camera.

Instead of simply recognizing objects, the model estimates **how far each object is**, allowing the system to understand the 3D structure of the environment.

---

### 4. 3D Visualization

The generated depth map is converted into a 3D representation, making it easier to understand the surrounding environment.

---

# 📂 Repository Structure

```
FPV-Drone-Depth-Mapping/

├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── project_overview.md
│   ├── setup.md
│   ├── pipeline.md
│   └── future_work.md
│
├── src/
│   ├── fpv_heading_bridge_node.py
│   └── fpv_key_input_node.py
│
├── media/
│
└── results/
```

---

# 💻 Requirements

### Hardware

- Ubuntu PC
- USB Camera / FPV Camera
- Minimum 8 GB RAM

Recommended

- NVIDIA GPU
- 16 GB RAM

---

### Software

- Ubuntu 22.04
- Python 3.10+
- ROS2 Humble
- OpenCV
- NumPy
- PyTorch

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/jayesh-0993-08/FPV-Drone-Depth-Mapping.git

cd FPV-Drone-Depth-Mapping
```

Install dependencies

```bash
pip install opencv-python numpy torch torchvision
```

Make sure ROS2 Humble is installed.

---

# ▶ Running

Open Terminal 1

```bash
python3 src/fpv_heading_bridge_node.py
```

Open Terminal 2

```bash
python3 src/fpv_key_input_node.py
```

Additional launch procedures will be added as the project develops.

---

# 📚 Recommended Learning Path

If you're completely new to robotics, I recommend learning in this order:

1. Python
2. Linux Basics
3. Git & GitHub
4. OpenCV Fundamentals
5. ROS2 Basics
6. Camera Topics
7. Depth Estimation
8. 3D Visualization
9. PX4
10. Autonomous Navigation

Following this order will make the project much easier to understand.

---

# 📖 Documentation

Detailed explanations are available inside the **docs/** folder.

- Project Overview
- Setup Guide
- System Pipeline
- Future Work

---

# 🚧 Current Limitations

This project is still under active development.

Current limitations include:

- Basic visualization
- Limited optimization
- Experimental implementation
- No onboard deployment yet

Future updates will gradually address these limitations.

---

# 🔭 Future Vision

This repository is an independent perception project focused on understanding depth estimation and 3D scene reconstruction.

The knowledge gained here will later be applied to more advanced autonomous robotics systems, where perception is one of many components required for intelligent navigation.

---

# 🤝 Contributing

Suggestions, issues, and discussions are always welcome.

If you have ideas for improving the project, feel free to open an Issue or Pull Request.

---

## 👨‍💻 Author

**Jayesh Shastri**

Robotics • ROS2 • Computer Vision • Autonomous Systems

GitHub: https://github.com/jayesh-0993-08

LinkedIn: *(Add your LinkedIn profile here)*

---

*"Every autonomous robot begins by learning to perceive the world."*
