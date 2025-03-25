# 2425_Projet2A_Ingenuity

**Students :**

- Pénélope HENNER - penelope.henner@ensea.fr
- Kavin DUGARD - kevin.dugard@ensea.fr 
- Elio FLANDIN - elio.flandin@ensea.fr
- Joel COLASO - joel.colaso@ensea.fr


## Project background:

Mars 2020 is a space mission to deploy the Perseverance rover on the Martian surface to study its surface and collect soil samples. It is the first of a series of three missions whose ultimate aim is to return these samples to Earth for analysis.

Ingenuity is a small helicopter developed by NASA, the US space agency. It is being used experimentally on the surface of Mars during the Mars 2020 mission. The helicopter is on board the Perseverance rover.

On April 19, 2021, for the first time in the history of the space age, a spacecraft makes a powered flight through the tenuous atmosphere of another planet. Ingenuity's objective is optical reconnaissance of the terrain, with the helicopter taking numerous aerial photos used by the pilots of the Perseverance astromobile to identify obstacles and promising sites (taking rock samples from the Martian soil).

Ingenuity is a 1.8 kg helicopter with 2 coaxial counter-rotating rotors. It draws its energy from 6 lithium-ion batteries recharged by solar cells. Its navigation system enables it to follow a pre-programmed route without human intervention. Its only payload is a camera.

The mission recently came to an end (January 18, 2024) when a blade broke during the 72nd flight.

Ingenuity has opened up new prospects for Mars exploration. NASA and ESA, as part of their Mars sample return mission, are now including 2 similar helicopters to collect the tubes containing the Martian samples deposited by the Perseverance astromobile in the event of its failure.

 Our project is therefore to try to build the Ingenuity module in miniature. In other words, we want to create a vehicle that can move through the air and take a photo of what's going on below.

![Ingenuity picture](https://github.com/joel-colaso/2324_Projet1AB_-ingenuity-/assets/161329228/e31ebabd-f48c-485a-bf0c-799dc236c984)

## Our project

Our project is to try and make this helicopter in miniature mode. In other words, we want to create a vehicle that can move through the air and take a photo of what's happening below. To do this, we'll have a total of 10 sessions in which we'll have to mix PCBs, coding, soldering and so on.

## Description of repo structure:

``````
.
├── Assets/            # Project images (drone, PCB)
├── Datasheets/        # Component datasheets
├── Hardware/          # Architecture diagrams and KiCad (PCB) files
├── Software/          # Embedded code (STM32) + Python code + TOF module
├── README.md          # Main project documentation
├── Ingenuity March 2020.md  # Background on the Mars 2020 mission


``````

In the **Assets** folder, you will find pictures of the drone and the assembled PCB.

The **Datasheets** folder contains documentation for all the components we used throughout the project.

The **Hardware** folder includes all the KiCad files needed to reproduce our custom PCB, along with the Bill of Materials (BOM) listing all components, their references, and specifications.

The **Software** folder contains:
- The **Python code** used to build the graphical user interface (GUI) on the PC to communicate with the Raspberry Pi (`Client_GUI.py`).
- The **Python code** running on the Raspberry Pi, which handles communication with the microcontroller and takes pictures (`server.py`).
- The **TOF code** (developed with STM32CubeIDE), which is responsible for sending the drone’s altitude using a Time-of-Flight sensor.
- The **C code** (also under STM32CubeIDE) in `Ingenuity_2A`, running on the STM32 microcontroller, which receives commands from the Raspberry Pi and manages the components such as motors, TOF sensor, etc.


## Logbook

### Session 1 (08/10/2024)
- Start writing the ReadMe.
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
- Unsolder the Buck because we didn't have the right one and the voltage wasn't right in our PCB.
- Solder the new Buck and update the BOM.

### Session 7 (03/12/2024)
- Soldering a Y cable to connect the 2 drivers simultaneously.
- Testing the drone with a GBF only.
- Test the drone with the functional PCB.
- Start of 3D modelling of our drone structure on OnShape.
- Continuation of the Python code.
- Continue with the C code.

### Session 8 (10/12/2024)
- Trip to the FabLab at Cergy Prefecture to use a laser cutter to cut out planks of wood to make the structure of the drone.

### Session 9 (14/12/2024)
- Assembling the structure of our drone.
- Further flight tests of the drone with the drone assembled, with GBF and with the PCB .
- Finalisation of the Git translation.
- Numerous tests on the operation of the camera connected to the RasberryPi.

### Session 10 (21/12/2024)
- Complete modification of the ReadMe + Translation.
- Start coding a graphical interface in Python.
- Soldering a JFT-banana cable to power the RasberryPi more efficiently and continue several tests.

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

### Session 17 (18/03/2025)

### Session 18 (25/03/2025)

## Environments used: 

### Machines Used
- **PC (Windows/macOS/Linux)**: Used for development (STM32CubeIDE, Python, OnShape, etc.).
- **Function Generator (GBF)**: Used to simulate control signals during motor testing.
- **Laser Cutter (FabLab)**: Used to cut the wooden drone structure.

### Hardware
- **Raspberry Pi Zero**: A single-board computer used for image capture, PCB interfacing, and running Python scripts.
- **STM32L412KBT6**: Main microcontroller used on the custom PCB.
- **VL53L1X**: Time-of-Flight (ToF) distance sensor.
- **ESC (Electronic Speed Controllers)**: To control brushless motors.
- **Brushless Motors**: Used to generate drone thrust.
- **LDO BU33TD3WG**: Low-dropout voltage regulator.
- **Buck Converter 17395xx36**: DC-DC converter used to step down voltage.
- **MOSFETs**: Used for power switching and motor control.
- **Camera (connected to Raspberry Pi)**: Captures aerial images.

### Software
#### Embedded Development
- **STM32CubeIDE**: Used to write, compile, and flash firmware to the microcontroller.
- **STM32 HAL Drivers**: Low-level drivers for managing STM32 peripherals.

#### Electronic Design
- **KiCad**: Used for circuit schematic design, PCB layout, and Gerber/BOM export.
- **OnShape**: Used for 3D modeling of the drone structure.

#### Python Development
- **Python 3**: Used for drone communication scripts and the graphical user interface (GUI).
- **Tkinter / PyQt**: Used to build the GUI interface.
- **Pygame / Other sound libraries**: For playing feedback sounds (from the `sounds/` folder).
- **Flask / TCP Sockets**: For communication between the GUI and the drone.


## Picture of Mini-Ingenuity 





