### Session 1 (08/10/2024)
- Modelling of the first architecture diagram (V1).
- Start writing the project structure.
- Search for better performing components than last year (Buck, LDO, engines, etc).
- Add datasheets of the final components found.

### Session 2 (22/10/2024)
- Reflection on the architecture diagram and modelling of V2 and V3 of it.
- Addition of new datasheets.

### Session 3 (05/11/2024)
- Addition of the last datasheets on Git.
- Finalisation of our architecture diagram (V4).
- Start of KiCad modelling (schematic).
- Start coding in C on STM32.
- Start Python code.

### Session 4 (12/11/2024)
- Updating the Python code.
- Creating the notice for the Python code.
- Continuation of KiCad modelling (routing).

### Session 5 (19/11/2024)
- Exporting the Bill of Materials (BOM).
- Soldering the PCB at school.
- End of PCB soldering between sessions 5 and 6.
- Translation of the Git into English between sessions 5 and 6.

### Session 6 (26/11/2024)
- Test that the PCB is working properly (LEDs lighting up correctly).
- Update and continue coding in Python.
- Unsolder the Buck because it was not providing the correct output voltage—instead of converting 6V to 5V, it was outputting 3V, which was insufficient for our PCB.
- Solder the new Buck and update the BOM.

### Session 7 (03/12/2024)
- Soldering a Y cable to connect the 2 drivers simultaneously.
- Testing the drone with a Function Generator (GBF) only.
- Testing the drone with the functional PCB: powered the motors and performed a flight test using a function generator (GBF) instead of a battery.
- Start of 3D modelling of our drone structure on OnShape.
- Continuation of the Python code.
- Continue with the C code.

### Session 8 (10/12/2024)
- Visit to the FabLab in Cergy to use a laser cutter for wooden drone structure components.

### Session 9 (14/12/2024)
- Assembling the structure of our drone.
- Further flight tests of the drone with the drone assembled, with GBF and with the PCB .
- Finalisation of the Git translation.
- Numerous tests on the operation of the camera connected to the Raspberry Pi.

### Session 10 (21/12/2024)
- Complete modification of the ReadMe + Translation.
- Start coding a graphical interface in Python.
- Soldering a JFT-banana cable to power the Raspberry Pi more efficiently and continue several tests.

### Session 11 (28/12/2024)
- Finalisation of the Python code base for the graphical user interface (GUI).
- KiCad modification : Connection problem between the Raspberry Pi Zero and our PCB, the connector is upside down ==> vertical reversal + routing modification.
- Start of TOF code (C code).

### Session 12 (28/01/2025)
- Final KiCad adjustments : Optimized the PCB dimensions to match the Raspberry Pi Zero form factor, completed additional routing, and prepared the design for manufacturing.
- Continuity of TOF Code.

### Session 13 (04/02/2025)
- Drone testing : Verification of connectivity and functionality between our PCB, the Raspberry Pi Zero, and the ESC drivers by simulating signals with a GBF. Bug fixes.
- Drone testing and improvement of the motor control code in C: added the ability to gradually increase motor speed, either by selecting a specific speed or by using the arrow keys on the computer.
- Ongoing development of TOF code : Continued work with the code.

### Session 14 (11/02/2025)
- Soldering of the newly received PCB.
- Testing the communication between the Raspberry Pi Zero and our previous PCB, with improvements to the C code (added linear acceleration for the motors).
- Enhancing the GUI code: the interface now provides full control of the drone (connection, photo capture, power adjustment).
- Consideration of the drone’s weight and potential optimizations to reduce it.

### Session 15 (04/03/2025)
- Testing of the new PCB: proper power supply and correct operation.
- Development of new features for the Python GUI code.
- Continued development of the C code (motor control and TOF sensor data acquisition).

### Session 16 (11/03/2025)
- Completion of TOF sensor code and initiation of IMU coding (C language).
- 3D modeling : Designed a protective casing for the motors and an enclosure for electronic components.
- 3D modeling : Created custom screws and bolts in 3D to reduce weight compared to traditional metal threaded rods.
- 3D printing of the newly designed components.

### Session 17 (18/03/2025)
- Full drone test integrating TOF, IMU, and all C code for autonomous flight with the graphical interface.
- Structural modification: Reduced the thickness of the wooden frame to decrease overall weight.
- 3D printing of updated structural components.

### Session 18 (25/03/2025)
- 3D modeling: Designed protective grilles for the propellers.
- 3D printing of the new protective elements.
- GitHub improvements: Refinement and restructuring of the ReadMe file.


