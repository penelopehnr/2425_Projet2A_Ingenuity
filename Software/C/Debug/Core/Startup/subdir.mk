################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (12.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
S_SRCS += \
../Core/Startup/startup_stm32l412kbtx.s 

OBJS += \
./Core/Startup/startup_stm32l412kbtx.o 

S_DEPS += \
./Core/Startup/startup_stm32l412kbtx.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Startup/%.o: ../Core/Startup/%.s Core/Startup/subdir.mk
	arm-none-eabi-gcc -mcpu=cortex-m4 -g3 -DDEBUG -c -I"C:/Users/PC/Desktop/Programacion/Programacion_2025/Projet2A/2425_Projet2A_Ingenuity/Software/Ingenuity_2A/Drivers/VL53L1X_ULD_API" -I"C:/Users/PC/Desktop/Programacion/Programacion_2025/Projet2A/2425_Projet2A_Ingenuity/Software/Ingenuity_2A/Drivers/VL53L1X_ULD_API/platform" -I"C:/Users/PC/Desktop/Programacion/Programacion_2025/Projet2A/2425_Projet2A_Ingenuity/Software/Ingenuity_2A/Drivers/VL53L1X_ULD_API/core" -x assembler-with-cpp -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@" "$<"

clean: clean-Core-2f-Startup

clean-Core-2f-Startup:
	-$(RM) ./Core/Startup/startup_stm32l412kbtx.d ./Core/Startup/startup_stm32l412kbtx.o

.PHONY: clean-Core-2f-Startup

