# Project Overview

## Introduction

FPV-Drone-Depth-Mapping is a computer vision project that converts a live FPV (First Person View) camera feed into a depth map and a 3D representation of the surrounding environment.

The primary objective of this project is to understand how modern autonomous drones perceive the world around them. Instead of relying only on a normal RGB camera feed, the system estimates the distance of every visible object and reconstructs the scene in three dimensions.

This project serves as a foundation for future applications such as:

- Autonomous Navigation
- Obstacle Avoidance
- Environment Mapping
- 3D Reconstruction
- Drone Perception

---

## Project Goal

Most FPV drones only provide a standard RGB camera feed, which is sufficient for manual flying but does not provide distance information.

This project demonstrates how a single camera feed can be processed to estimate depth and generate a 3D visualization of the environment.

The goal is not only to build the system but also to understand every stage involved in the perception pipeline.

---

## What this Repository Contains

- ROS2 nodes used during development
- Depth estimation pipeline
- Camera streaming
- Documentation
- Implementation details
- Future roadmap

---

## Who is this Project For?

This repository is intended for:

- Robotics beginners
- ROS2 learners
- Computer Vision enthusiasts
- Drone developers
- Students interested in autonomous systems

No prior experience with depth estimation is required. However, basic Python knowledge is recommended.

---

## Current Status

Current Version: **v0.1**

Implemented

- Live FPV camera streaming
- ROS2 communication
- Keyboard control
- Depth map generation
- 3D visualization

Future versions will focus on improving accuracy, optimization, and integration into larger autonomous systems.
