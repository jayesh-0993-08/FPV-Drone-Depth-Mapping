# Setup Guide

This guide explains how to prepare your system for running this project.

---

# Operating System

This project was developed and tested on:

- Ubuntu 22.04 LTS

Other Linux distributions may also work but are not officially tested.

---

# Prerequisites

Before starting, you should have a basic understanding of:

- Python
- Linux Terminal
- ROS2 Basics
- Git
- OpenCV Fundamentals

Recommended learning order:

1. Python
2. Linux Commands
3. Git & GitHub
4. ROS2 Basics
5. OpenCV

---

# Software Requirements

Install the following software:

- Python 3.10+
- ROS2 Humble
- OpenCV
- PyTorch
- NumPy

---

# Hardware Requirements

Minimum

- Ubuntu PC
- Webcam or FPV Camera
- 8 GB RAM

Recommended

- NVIDIA GPU
- 16 GB RAM
- USB FPV Camera

---

# Clone Repository

```bash
git clone https://github.com/jayesh-0993-08/FPV-Drone-Depth-Mapping.git

cd FPV-Drone-Depth-Mapping
```

---

# Install Dependencies

Example:

```bash
pip install opencv-python numpy torch torchvision
```

Install ROS2 according to the official documentation.

---

# Running the Project

Start the required ROS2 nodes.

Example:

```bash
python3 src/fpv_heading_bridge_node.py
```

Open another terminal.

```bash
python3 src/fpv_key_input_node.py
```

Additional commands and launch procedures will be added as the project evolves.

---

# Troubleshooting

Common issues

### Camera not detected

Check:

```bash
ls /dev/video*
```

---

### ROS2 not sourced

Run:

```bash
source /opt/ros/humble/setup.bash
```

---

### Python module missing

Install using

```bash
pip install <module_name>
```

---

# Project Structure

```
README.md

docs/

src/

media/

results/
```
