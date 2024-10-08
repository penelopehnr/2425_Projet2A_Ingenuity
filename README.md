# 2425_Projet2A_Ingenuity

Étudiants: 

- Pénélope HENNER - penelope.henner@ensea.fr
- Kavin DUGARD - kevin.dugard@ensea.fr 
- Elio FLANDIN - elio.flandin@ensea.fr
- Joel COLASO - joel.colaso@ensea.fr


Le contexte du projet:

Mars 2020 est une mission spatiale qui consiste à déployer l'astromobile (rover) Perseverance sur le sol martien pour étudier sa surface et collecter des échnatillons du sol. Elle constitue la première d'une série de trois missions dont l'objectif final est de ramener ces échantillons sur Terre pour leur analyse.

Ingenuity est un petit hélicoptère développé par l'agence spatiale Américaine, la NASA. Il est mis en oeuvre à titre expérimental sur le sol de la planète Mars au cours de la mission Mars 2020. L'hélicoptère est embarqué à bord du rover Perseverance.

Le 19 avril 2021, pour la première fois dans l'histoire de l'ère spatiale, un engin effectue un vol motorisé dans l'atmosphère ténue d'une autre planète. L'objectif d'Ingenuity est la reconnaissance optique du terrain, l'hélicoptère réalise de nombreuses photos aériennes utiliées par les pilotes de l'astromobile Perseverance pour identifier les obstacles et les sites prometteurs (prelèvement d'échantillons rocheux sur le sol martien).

Ingenuity est un hélicoptère de 1,8 kg disposant de 2 rotors contrarotatifs coaxiaux. Il tire son énergie de 6 batteries lithium-ion rechargées par des cellules solaires. Son système de navigation lui permet de suivre sans intervention humaine un trajet pré-programmé. Sa seule charge utile est une caméra.

La mission s'est récemment arrêtée (18 janvier 2024) en raison de la casse d'un pale lors du 72e vol.

Ingenuity a ouvert de nouvelles perspectives pour l'exploration de Mars. La NASA et l'ESA, dans leur mission de retour d'échantillons martien, incluent maintenant 2 hélicopères similaires qui seront chargés de collecter les tubes contenant les échantillons martien déposés par l'astromobile Perseverance en cas de panne de celui-ci.

 Notre projet est donc d'essayer de réaliser le module Ingenuity en miniature. C'est à dire que l'on veut créer un véhicule pouvant se déplacer dans les airs et prendre une photo de ce qu'il se passe en dessous.

![Photo ingenuity](https://github.com/joel-colaso/2324_Projet1AB_-ingenuity-/assets/161329228/e31ebabd-f48c-485a-bf0c-799dc236c984)

Description of repo structure:

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
│   ├── PIN_STM32.png
│   ├── SchemaArchi_Ingenuity_V1.jpg
│   ├── SchemaArchi_Ingenuity_V2.jpg
│   ├── SchemaArchi_Ingenuity_V3.jpg.png
│   └── SchemaArchi_Ingenuity_V4.jpg
├── Ingenuity_Mars2020.md
├── Output
│   └── Matériel Projet 2A.xlsx
├── README.md
└── Software
    └── Ingenuity_2A
        ├── Core
        │   ├── Inc
        │   │   ├── main.h
        │   │   ├── stm32l4xx_hal_conf.h
        │   │   └── stm32l4xx_it.h
        │   ├── Src
        │   │   ├── main.c
        │   │   ├── stm32l4xx_hal_msp.c
        │   │   ├── stm32l4xx_it.c
        │   │   ├── syscalls.c
        │   │   ├── sysmem.c
        │   │   └── system_stm32l4xx.c
        │   └── Startup
        │       └── startup_stm32l412kbtx.s
        ├── Drivers
        │   ├── CMSIS
        │   │   ├── Device
        │   │   │   └── ST
        │   │   │       └── STM32L4xx
        │   │   │           ├── Include
        │   │   │           │   ├── stm32l412xx.h
        │   │   │           │   ├── stm32l4xx.h
        │   │   │           │   └── system_stm32l4xx.h
        │   │   │           ├── LICENSE.txt
        │   │   │           ├── License.md
        │   │   │           └── Source
        │   │   │               └── Templates
        │   │   ├── Include
        │   │   │   ├── cmsis_armcc.h
        │   │   │   ├── cmsis_armclang.h
        │   │   │   ├── cmsis_armclang_ltm.h
        │   │   │   ├── cmsis_compiler.h
        │   │   │   ├── cmsis_gcc.h
        │   │   │   ├── cmsis_iccarm.h
        │   │   │   ├── cmsis_version.h
        │   │   │   ├── core_armv81mml.h
        │   │   │   ├── core_armv8mbl.h
        │   │   │   ├── core_armv8mml.h
        │   │   │   ├── core_cm0.h
        │   │   │   ├── core_cm0plus.h
        │   │   │   ├── core_cm1.h
        │   │   │   ├── core_cm23.h
        │   │   │   ├── core_cm3.h
        │   │   │   ├── core_cm33.h
        │   │   │   ├── core_cm35p.h
        │   │   │   ├── core_cm4.h
        │   │   │   ├── core_cm7.h
        │   │   │   ├── core_sc000.h
        │   │   │   ├── core_sc300.h
        │   │   │   ├── mpu_armv7.h
        │   │   │   ├── mpu_armv8.h
        │   │   │   └── tz_context.h
        │   │   └── LICENSE.txt
        │   └── STM32L4xx_HAL_Driver
        │       ├── Inc
        │       │   ├── Legacy
        │       │   │   └── stm32_hal_legacy.h
        │       │   ├── stm32l4xx_hal.h
        │       │   ├── stm32l4xx_hal_adc.h
        │       │   ├── stm32l4xx_hal_adc_ex.h
        │       │   ├── stm32l4xx_hal_cortex.h
        │       │   ├── stm32l4xx_hal_def.h
        │       │   ├── stm32l4xx_hal_dma.h
        │       │   ├── stm32l4xx_hal_dma_ex.h
        │       │   ├── stm32l4xx_hal_exti.h
        │       │   ├── stm32l4xx_hal_flash.h
        │       │   ├── stm32l4xx_hal_flash_ex.h
        │       │   ├── stm32l4xx_hal_flash_ramfunc.h
        │       │   ├── stm32l4xx_hal_gpio.h
        │       │   ├── stm32l4xx_hal_gpio_ex.h
        │       │   ├── stm32l4xx_hal_i2c.h
        │       │   ├── stm32l4xx_hal_i2c_ex.h
        │       │   ├── stm32l4xx_hal_pwr.h
        │       │   ├── stm32l4xx_hal_pwr_ex.h
        │       │   ├── stm32l4xx_hal_rcc.h
        │       │   ├── stm32l4xx_hal_rcc_ex.h
        │       │   ├── stm32l4xx_hal_spi.h
        │       │   ├── stm32l4xx_hal_spi_ex.h
        │       │   ├── stm32l4xx_hal_tim.h
        │       │   ├── stm32l4xx_hal_tim_ex.h
        │       │   ├── stm32l4xx_hal_uart.h
        │       │   ├── stm32l4xx_hal_uart_ex.h
        │       │   ├── stm32l4xx_ll_adc.h
        │       │   ├── stm32l4xx_ll_bus.h
        │       │   ├── stm32l4xx_ll_cortex.h
        │       │   ├── stm32l4xx_ll_crs.h
        │       │   ├── stm32l4xx_ll_dma.h
        │       │   ├── stm32l4xx_ll_dmamux.h
        │       │   ├── stm32l4xx_ll_exti.h
        │       │   ├── stm32l4xx_ll_gpio.h
        │       │   ├── stm32l4xx_ll_i2c.h
        │       │   ├── stm32l4xx_ll_lpuart.h
        │       │   ├── stm32l4xx_ll_pwr.h
        │       │   ├── stm32l4xx_ll_rcc.h
        │       │   ├── stm32l4xx_ll_spi.h
        │       │   ├── stm32l4xx_ll_system.h
        │       │   ├── stm32l4xx_ll_tim.h
        │       │   ├── stm32l4xx_ll_usart.h
        │       │   └── stm32l4xx_ll_utils.h
        │       ├── LICENSE.txt
        │       └── Src
        │           ├── stm32l4xx_hal.c
        │           ├── stm32l4xx_hal_adc.c
        │           ├── stm32l4xx_hal_adc_ex.c
        │           ├── stm32l4xx_hal_cortex.c
        │           ├── stm32l4xx_hal_dma.c
        │           ├── stm32l4xx_hal_dma_ex.c
        │           ├── stm32l4xx_hal_exti.c
        │           ├── stm32l4xx_hal_flash.c
        │           ├── stm32l4xx_hal_flash_ex.c
        │           ├── stm32l4xx_hal_flash_ramfunc.c
        │           ├── stm32l4xx_hal_gpio.c
        │           ├── stm32l4xx_hal_i2c.c
        │           ├── stm32l4xx_hal_i2c_ex.c
        │           ├── stm32l4xx_hal_pwr.c
        │           ├── stm32l4xx_hal_pwr_ex.c
        │           ├── stm32l4xx_hal_rcc.c
        │           ├── stm32l4xx_hal_rcc_ex.c
        │           ├── stm32l4xx_hal_spi.c
        │           ├── stm32l4xx_hal_spi_ex.c
        │           ├── stm32l4xx_hal_tim.c
        │           ├── stm32l4xx_hal_tim_ex.c
        │           ├── stm32l4xx_hal_uart.c
        │           └── stm32l4xx_hal_uart_ex.c
        ├── Ingenuity_2A.ioc
        └── STM32L412KBTX_FLASH.ld


``````


Description of files: TO DO

Env used: 

- Kicad 
- Python 
- STM32 CubeIDE

Packages req: TO DO




