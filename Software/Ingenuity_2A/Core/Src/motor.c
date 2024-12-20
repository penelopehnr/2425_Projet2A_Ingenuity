/*
 * motor.c
 *
 *  Created on: May 27, 2024
 *      Author: JoelC
 */


#include "motor.h"
#include "stdio.h"

// There are currently lots of prints in this file for testing
// Once the tests pass, they can be deleted

// assuming counter counts microseconds
// 20000 = 5% of 2ms
#define COUNTER_PERIOD 19999 //Maximal counter value
#define MIN_POWER_DUTY_CYCLE 6 //%
#define MAX_POWER_DUTY_CYCLE 10 //%


int percentageToMicrosecondsAtHighState(int percentage) {
	int neededDutyCycle = MIN_POWER_DUTY_CYCLE + (MAX_POWER_DUTY_CYCLE - MIN_POWER_DUTY_CYCLE) * 0.01 * percentage;
	printf("->      neededDutyCycle = %d percent \r\n", neededDutyCycle);

	return (int) (COUNTER_PERIOD + 1) * 0.01 * neededDutyCycle;
}


void motor_SetPower(h_motor_t* h_motor, int percentage) {
	printf("-> power set to %d percent \r\n", percentage);

	int microsecondsAtHighState = percentageToMicrosecondsAtHighState(percentage);

	__HAL_TIM_SET_COMPARE(h_motor->htim, h_motor->channel, microsecondsAtHighState);

	printf("->      microsecondsAtHighState = %d \r\n", microsecondsAtHighState);

	h_motor -> PercentageOfTotalPower = percentage;
}


void motor_Init(h_motor_t* h_motor) {
	printf("INITIALISATION STARTED\r\n");

	motor_SetPower(h_motor, 100);

	HAL_TIM_PWM_Start(h_motor->htim, h_motor->channel);

	HAL_Delay(2000);

	motor_SetPower(h_motor, 0);
	HAL_Delay(3000);

	printf("INITIALISATION COMPLETED\r\n");
}


void motor_TurnOff(h_motor_t* h_motor) {
	motor_SetPower(h_motor, 0);
}

