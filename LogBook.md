## Project Logbook – Ingenuity

### Table of Contents
- [Session 1 (08/10/2024)](#session-1-08102024)
- [Session 2 (22/10/2024)](#session-2-22102024)
- [Session 3 (05/11/2024)](#session-3-05112024)
- [Session 4 (12/11/2024)](#session-4-12112024)
- [Session 5 (19/11/2024)](#session-5-19112024)
- [Session 6 (26/11/2024)](#session-6-26112024)
- [Session 7 (03/12/2024)](#session-7-03122024)
- [Session 8 (10/12/2024)](#session-8-10122024)
- [Session 9 (14/12/2024)](#session-9-14122024)
- [Session 10 (21/12/2024)](#session-10-21122024)
- [Session 11 (28/12/2024)](#session-11-28122024)
- [Session 12 (28/01/2025)](#session-12-28012025)
- [Session 13 (04/02/2025)](#session-13-04022025)
- [Session 14 (11/02/2025)](#session-14-11022025)
- [Session 15 (04/03/2025)](#session-15-04032025)
- [Session 16 (11/03/2025)](#session-16-11032025)
- [Session 17 (18/03/2025)](#session-17-18032025)
- [Session 18 (25/03/2025)](#session-18-25032025)
- [Session 19 (01/04/2025)](#session-19-01042025)



### Session 1 (08/10/2024)
- Modeled the initial architecture diagram (V1).
- Started writing the project structure.
- Researched higher-performing components compared to last year (Buck, LDO, motors, etc.).
- Added datasheets for the final selected components.

### Session 2 (22/10/2024)
- Reflected on the architecture and created versions V2 and V3.
- Added new component datasheets.

### Session 3 (05/11/2024)
- Uploaded the final datasheets to Git.
- Finalized architecture diagram (V4).
- Started schematic modeling in KiCad.
- Began C programming on the STM32.
- Started the Python code base.

### Session 4 (12/11/2024)
- Updated the Python code.
- Created documentation for the Python scripts.
- Continued PCB routing in KiCad.

### Session 5 (19/11/2024)
- Exported the Bill of Materials (BOM).
- Soldered the PCB at school.
- Completed PCB soldering between sessions 5 and 6.
- Translated the GitHub repository content into English.

### Session 6 (26/11/2024)
- Tested PCB functionality (LEDs lit up correctly).
- Updated and extended Python code.
- Desoldered the Buck converter due to incorrect output voltage (3V instead of 5V).
- Soldered a new Buck converter and updated the BOM.

### Session 7 (03/12/2024)
- Soldered a Y-cable to connect both ESC drivers simultaneously.
- Tested the drone using a Function Generator (GBF) only.
- Conducted a flight test using the functional PCB and GBF instead of a battery.
- Began 3D modeling the drone structure on OnShape.
- Continued development in both Python and C.

### Session 8 (10/12/2024)
- Visited the FabLab in Cergy to use the laser cutter for wooden drone parts.

### Session 9 (14/12/2024)
- Assembled the drone structure.
- Performed additional flight tests with the assembled drone, GBF, and PCB.
- Finalized the GitHub translation.
- Conducted multiple tests with the Raspberry Pi camera.

### Session 10 (21/12/2024)
- Fully revised and translated the README.
- Started development of a Python graphical interface.
- Soldered a JFT-to-banana cable to power the Raspberry Pi more efficiently and continued testing.

### Session 11 (28/12/2024)
- Finalized the Python GUI base.
- Modified KiCad due to a connection issue between the Raspberry Pi Zero and the PCB (reversed connector) → adjusted routing accordingly.
- Started development of TOF (Time-of-Flight) sensor code in C.

### Session 12 (28/01/2025)
- Final adjustments in KiCad: resized PCB to match the Raspberry Pi Zero form factor, completed routing, and prepared for manufacturing.
- Continued TOF sensor code development.

### Session 13 (04/02/2025)
- Drone testing: validated communication and functionality between the PCB, Raspberry Pi Zero, and ESCs using GBF signals. Fixed bugs.
- Improved motor control code in C: enabled gradual speed increases and added keyboard controls.
- Continued TOF code development.

### Session 14 (11/02/2025)
- Soldered the new version of the PCB.
- Tested communication with the Raspberry Pi Zero and improved the C code (added linear acceleration for motors).
- Enhanced the Python GUI: enabled full drone control (connection, camera, power).
- Considered the drone’s weight and explored optimization options.

### Session 15 (04/03/2025)
- Tested the new PCB: power supply and components functioned correctly.
- Added new features to the Python GUI.
- Continued development of C code (motor control + TOF data handling).

### Session 16 (11/03/2025)
- Finalized the TOF code and started IMU integration (C language).
- 3D modeling: designed motor protection casings and an enclosure for electronics.
- Created custom 3D screws and bolts to reduce weight vs traditional threaded rods.
- 3D printed all new parts.

### Session 17 (18/03/2025)
- Full drone test with TOF, IMU, and integrated C code for autonomous flight via GUI.
- Structural optimization: reduced wood frame thickness to cut weight.
- 3D printed updated structural parts.

### Session 18 (25/03/2025)
- 3D modeling: designed propeller protection grilles.
- 3D printed the new protective elements.
- Improved GitHub repository: reorganized and refined the ReadMe.

### Session 19 (01/04/2025)
- Finalized the GitHub repository: added pictures and reorganized the ReadMe and general documentation.
- Assembled the drone: mounted all electronic components onto the 3D-printed frame.
- Gave a flight demonstration of our drone in front of the professors.
