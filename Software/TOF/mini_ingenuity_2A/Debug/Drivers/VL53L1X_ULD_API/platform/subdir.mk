################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (13.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/VL53L1X_ULD_API/platform/vl53l1_platform.c 

OBJS += \
./Drivers/VL53L1X_ULD_API/platform/vl53l1_platform.o 

C_DEPS += \
./Drivers/VL53L1X_ULD_API/platform/vl53l1_platform.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/VL53L1X_ULD_API/platform/%.o Drivers/VL53L1X_ULD_API/platform/%.su Drivers/VL53L1X_ULD_API/platform/%.cyclo: ../Drivers/VL53L1X_ULD_API/platform/%.c Drivers/VL53L1X_ULD_API/platform/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32L412xx -c -I../Core/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../Drivers/CMSIS/Include -I"/Users/penelopehenner/STM32CubeIDE/workspace_1.13.1/mini_ingenuity_2A/Drivers/VL53L1X_ULD_API/core" -I"/Users/penelopehenner/STM32CubeIDE/workspace_1.13.1/mini_ingenuity_2A/Drivers/VL53L1X_ULD_API/platform" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-VL53L1X_ULD_API-2f-platform

clean-Drivers-2f-VL53L1X_ULD_API-2f-platform:
	-$(RM) ./Drivers/VL53L1X_ULD_API/platform/vl53l1_platform.cyclo ./Drivers/VL53L1X_ULD_API/platform/vl53l1_platform.d ./Drivers/VL53L1X_ULD_API/platform/vl53l1_platform.o ./Drivers/VL53L1X_ULD_API/platform/vl53l1_platform.su

.PHONY: clean-Drivers-2f-VL53L1X_ULD_API-2f-platform

