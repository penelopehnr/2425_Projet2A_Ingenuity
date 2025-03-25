# Utilisation Notice

## General 

The goal of the drone is to take off, reach a predefined altitude, capture a photo, and then descend.

Altitude commands are sent from the PC to the Raspberry Pi Zero via Wi-Fi using Python scripts. A custom graphical interface has been developed on the PC to control this process. The Raspberry Pi then communicates with the microcontroller on the PCB through a UART (USART) serial connection, using both Python and C code. It is also responsible for capturing images through a CSI camera interface.

The microcontroller, embedded on the custom PCB, manages the drone's motors using PWM signals (written in C), and receives altitude data from a Time-of-Flight (TOF) sensor over an I2C bus, also handled via C code.

## Architecture 

![Mini Ingenuity Drone architecture](Hardware/Architecture/Architecture%20Schematic%20V4.jpg)

## Structure of Mini-Ingenuity

### 3D structural parts 
 
files concerned: `Hardware/3D files/files.stl`:
``````
3D files
│   │   ├── 3D_boulons_structure_drone.stl
│   │   ├── 3D_tube_structure_drone.stl
│   │   └── 3D_vises_structure_drone.stl
``````
The screws, bolts, and tubes allow you to assemble the wooden parts together and build the structure of the drone.

Machine used: a 3D printer

### Wood structure 

files concerned: `Hardware/Wood structure/Bois.stl`

Machine used: a laser cutter
Our wood sheets are 5 mm thick.

### Picture of the Structure 

## PCB 

files concerned: `Hardware/KiCAD/...`

### BOM

First, you will need all the required components. You can find all the necessary information — references, quantities, etc. — in the Bill of Materials (BOM).

[BOM](Hardware/KiCAD/BOMv3.csv)

### KiCad

Software used: KiCad
All the KiCad files required to build the PCB are available in this repository.

## Code

### Python code 

### Code for the microcontroller

### PINs

[PIN](Hardware/STM32_Pins.png)


### TOF 

Start by copying the ```VL53L1X_ULD_API``` in your project. You want to configure the paths in your IDE (eg. in STM32CubeIDE : ```Project > Properties``` then ```C/C++ General > Paths and Symbols```).

detailed explanations: https://github.com/lfiack/tof_VL53L1X-SATEL/blob/main/README.md

You can refer to the datasheet for information on how to connect to the PCB: 

[TOF Datasheet](Datasheets/TOF.pdf)


