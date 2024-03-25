# Minicity Smart-Intersection

A proof-of-concept for a smart intersection which supports traffic management utilizing SLAM.

## Description

This repository contains the ROS package for AirOU's Smart Intersection.

## Source Files (/src/)

-   vehicle/
    -   Contains all the code (ROS nodes) for a car to communicate with Smart Infrastructure
    -   Targets the (mushr.io)[https://mushr.io/] vehicle platform.
-   infrastructure/
    -   Contains all the code (ROS nodes) for a smart intersection to communicate with cars
    -   Targets Nvidia Jetson Orin Nano single-board computer with Velodyne Puck 3D lidar.
