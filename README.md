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
```
.
├── Datasheets
│   ├── MOSFET.pdf
│   ├── RASBERRY_PI.pdf
│   ├── REGULATEUR.pdf
│   ├── TOF.pdf
│   ├── datasheet_Driver_pichlerXQ30.pdf
│   ├── datasheet_IMU.pdf
│   ├── datasheet_LDO_BU33TD3WG.pdf
│   └── datasheet_buck_17395xx36.pdf
├── Firmware
├── Hardware
│   ├── KiCAD
│   │   ├── BOM.csv
│   │   ├── BOMv2.csv
│   │   ├── BOMv3.csv
│   │   ├── Ingenuity-2024-10-08_151421.zip
│   │   ├── Ingenuity-backups
│   │   │   ├── Ingenuity-2024-10-22_171040.zip
│   │   │   ├── Ingenuity-2024-10-22_172052.zip
│   │   │   ├── Ingenuity-2024-10-22_172850.zip
│   │   │   ├── Ingenuity-2024-10-22_173410.zip
│   │   │   ├── Ingenuity-2024-10-22_174615.zip
│   │   │   ├── Ingenuity-2024-11-05_145632.zip
│   │   │   ├── Ingenuity-2024-11-05_150528.zip
│   │   │   ├── Ingenuity-2024-11-05_151113.zip
│   │   │   ├── Ingenuity-2024-11-05_193304.zip
│   │   │   ├── Ingenuity-2024-11-06_155747.zip
│   │   │   ├── Ingenuity-2024-11-11_232102.zip
│   │   │   ├── Ingenuity-2024-11-12_145402.zip
│   │   │   ├── Ingenuity-2024-11-12_150233.zip
│   │   │   ├── Ingenuity-2024-11-12_155449.zip
│   │   │   ├── Ingenuity-2024-11-12_170709.zip
│   │   │   ├── Ingenuity-2024-11-12_173056.zip
│   │   │   └── Ingenuity-2024-11-19_144244.zip
│   │   ├── Ingenuity.kicad_pcb
│   │   ├── Ingenuity.kicad_prl
│   │   ├── Ingenuity.kicad_pro
│   │   ├── Ingenuity.kicad_sch
│   │   ├── desktop.ini
│   │   ├── fp-info-cache
│   │   ├── gerber
│   │   │   ├── Ingenuity-B_Cu.gbr
│   │   │   ├── Ingenuity-B_Mask.gbr
│   │   │   ├── Ingenuity-B_Silkscreen.gbr
│   │   │   ├── Ingenuity-Edge_Cuts.gbr
│   │   │   ├── Ingenuity-F_Cu.gbr
│   │   │   ├── Ingenuity-F_Mask.gbr
│   │   │   ├── Ingenuity-F_Paste.gbr
│   │   │   ├── Ingenuity-F_Silkscreen.gbr
│   │   │   ├── Ingenuity-In1_Cu.gbr
│   │   │   ├── Ingenuity-In2_Cu - GND.gbr
│   │   │   ├── Ingenuity-NPTH-drl_map.gbr
│   │   │   ├── Ingenuity-NPTH.drl
│   │   │   ├── Ingenuity-PTH-drl_map.gbr
│   │   │   ├── Ingenuity-PTH.drl
│   │   │   └── Ingenuity-job.gbrjob
│   │   └── myLib.pretty
│   │       ├── LDO_BU33TD3WG.kicad_mod
│   │       └── wurth_17395xx36.kicad_mod
│   ├── PIN_STM32.png
│   ├── SchemaArchi_Ingenuity_V1.jpg
│   ├── SchemaArchi_Ingenuity_V2.jpg
│   ├── SchemaArchi_Ingenuity_V3.png
│   └── SchemaArchi_Ingenuity_V4.jpg
├── Ingenuity_Mars2020.md
├── Output
│   └── Matériel Projet 2A.xlsx
├── README.md
└── Software
    ├── Ingenuity_2A
    │   ├── Core
    │   │   ├── Inc
    │   │   │   ├── main.h
    │   │   │   ├── stm32l4xx_hal_conf.h
    │   │   │   └── stm32l4xx_it.h
    │   │   ├── Src
    │   │   │   ├── main.c
    │   │   │   ├── stm32l4xx_hal_msp.c
    │   │   │   ├── stm32l4xx_it.c
    │   │   │   ├── syscalls.c
    │   │   │   ├── sysmem.c
    │   │   │   └── system_stm32l4xx.c
    │   │   └── Startup
    │   │       └── startup_stm32l412kbtx.s
    │   ├── Drivers
    │   │   ├── CMSIS
    │   │   │   ├── Device
    │   │   │   │   └── ST
    │   │   │   │       └── STM32L4xx
    │   │   │   │           ├── Include
    │   │   │   │           │   ├── stm32l412xx.h
    │   │   │   │           │   ├── stm32l4xx.h
    │   │   │   │           │   └── system_stm32l4xx.h
    │   │   │   │           ├── LICENSE.txt
    │   │   │   │           ├── License.md
    │   │   │   │           └── Source
    │   │   │   │               └── Templates
    │   │   │   ├── Include
    │   │   │   │   ├── cmsis_armcc.h
    │   │   │   │   ├── cmsis_armclang.h
    │   │   │   │   ├── cmsis_armclang_ltm.h
    │   │   │   │   ├── cmsis_compiler.h
    │   │   │   │   ├── cmsis_gcc.h
    │   │   │   │   ├── cmsis_iccarm.h
    │   │   │   │   ├── cmsis_version.h
    │   │   │   │   ├── core_armv81mml.h
    │   │   │   │   ├── core_armv8mbl.h
    │   │   │   │   ├── core_armv8mml.h
    │   │   │   │   ├── core_cm0.h
    │   │   │   │   ├── core_cm0plus.h
    │   │   │   │   ├── core_cm1.h
    │   │   │   │   ├── core_cm23.h
    │   │   │   │   ├── core_cm3.h
    │   │   │   │   ├── core_cm33.h
    │   │   │   │   ├── core_cm35p.h
    │   │   │   │   ├── core_cm4.h
    │   │   │   │   ├── core_cm7.h
    │   │   │   │   ├── core_sc000.h
    │   │   │   │   ├── core_sc300.h
    │   │   │   │   ├── mpu_armv7.h
    │   │   │   │   ├── mpu_armv8.h
    │   │   │   │   └── tz_context.h
    │   │   │   └── LICENSE.txt
    │   │   └── STM32L4xx_HAL_Driver
    │   │       ├── Inc
    │   │       │   ├── Legacy
    │   │       │   │   └── stm32_hal_legacy.h
    │   │       │   ├── stm32l4xx_hal.h
    │   │       │   ├── stm32l4xx_hal_adc.h
    │   │       │   ├── stm32l4xx_hal_adc_ex.h
    │   │       │   ├── stm32l4xx_hal_cortex.h
    │   │       │   ├── stm32l4xx_hal_def.h
    │   │       │   ├── stm32l4xx_hal_dma.h
    │   │       │   ├── stm32l4xx_hal_dma_ex.h
    │   │       │   ├── stm32l4xx_hal_exti.h
    │   │       │   ├── stm32l4xx_hal_flash.h
    │   │       │   ├── stm32l4xx_hal_flash_ex.h
    │   │       │   ├── stm32l4xx_hal_flash_ramfunc.h
    │   │       │   ├── stm32l4xx_hal_gpio.h
    │   │       │   ├── stm32l4xx_hal_gpio_ex.h
    │   │       │   ├── stm32l4xx_hal_i2c.h
    │   │       │   ├── stm32l4xx_hal_i2c_ex.h
    │   │       │   ├── stm32l4xx_hal_pwr.h
    │   │       │   ├── stm32l4xx_hal_pwr_ex.h
    │   │       │   ├── stm32l4xx_hal_rcc.h
    │   │       │   ├── stm32l4xx_hal_rcc_ex.h
    │   │       │   ├── stm32l4xx_hal_spi.h
    │   │       │   ├── stm32l4xx_hal_spi_ex.h
    │   │       │   ├── stm32l4xx_hal_tim.h
    │   │       │   ├── stm32l4xx_hal_tim_ex.h
    │   │       │   ├── stm32l4xx_hal_uart.h
    │   │       │   ├── stm32l4xx_hal_uart_ex.h
    │   │       │   ├── stm32l4xx_ll_adc.h
    │   │       │   ├── stm32l4xx_ll_bus.h
    │   │       │   ├── stm32l4xx_ll_cortex.h
    │   │       │   ├── stm32l4xx_ll_crs.h
    │   │       │   ├── stm32l4xx_ll_dma.h
    │   │       │   ├── stm32l4xx_ll_dmamux.h
    │   │       │   ├── stm32l4xx_ll_exti.h
    │   │       │   ├── stm32l4xx_ll_gpio.h
    │   │       │   ├── stm32l4xx_ll_i2c.h
    │   │       │   ├── stm32l4xx_ll_lpuart.h
    │   │       │   ├── stm32l4xx_ll_pwr.h
    │   │       │   ├── stm32l4xx_ll_rcc.h
    │   │       │   ├── stm32l4xx_ll_spi.h
    │   │       │   ├── stm32l4xx_ll_system.h
    │   │       │   ├── stm32l4xx_ll_tim.h
    │   │       │   ├── stm32l4xx_ll_usart.h
    │   │       │   └── stm32l4xx_ll_utils.h
    │   │       ├── LICENSE.txt
    │   │       └── Src
    │   │           ├── stm32l4xx_hal.c
    │   │           ├── stm32l4xx_hal_adc.c
    │   │           ├── stm32l4xx_hal_adc_ex.c
    │   │           ├── stm32l4xx_hal_cortex.c
    │   │           ├── stm32l4xx_hal_dma.c
    │   │           ├── stm32l4xx_hal_dma_ex.c
    │   │           ├── stm32l4xx_hal_exti.c
    │   │           ├── stm32l4xx_hal_flash.c
    │   │           ├── stm32l4xx_hal_flash_ex.c
    │   │           ├── stm32l4xx_hal_flash_ramfunc.c
    │   │           ├── stm32l4xx_hal_gpio.c
    │   │           ├── stm32l4xx_hal_i2c.c
    │   │           ├── stm32l4xx_hal_i2c_ex.c
    │   │           ├── stm32l4xx_hal_pwr.c
    │   │           ├── stm32l4xx_hal_pwr_ex.c
    │   │           ├── stm32l4xx_hal_rcc.c
    │   │           ├── stm32l4xx_hal_rcc_ex.c
    │   │           ├── stm32l4xx_hal_spi.c
    │   │           ├── stm32l4xx_hal_spi_ex.c
    │   │           ├── stm32l4xx_hal_tim.c
    │   │           ├── stm32l4xx_hal_tim_ex.c
    │   │           ├── stm32l4xx_hal_uart.c
    │   │           └── stm32l4xx_hal_uart_ex.c
    │   ├── Ingenuity_2A.ioc
    │   └── STM32L412KBTX_FLASH.ld
    └── Python
        ├── Codes temporaires
        │   ├── Clav.py
        │   ├── Clav2.py
        │   ├── Tempo.py
        │   └── test.py
        ├── Notice.md
        ├── client.py
        └── server.py

``````

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

## Env used: 

- Kicad 
- Python 
- STM32 CubeIDE
- OnShape

## Mini-Ingenuity on the 3/12/24

![picture mini ingenuity](https://github.com/penelopehnr/2425_Projet2A_Ingenuity/blob/main/Assets/Drone.png)



