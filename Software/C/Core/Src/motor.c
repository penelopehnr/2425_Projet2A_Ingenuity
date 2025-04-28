/*
 * motor.c
 *
 *  Created on: May 27, 2024
 *      Author: JoelC
 */


#include "motor.h"
#include "stdio.h"
#include "math.h"

// There are currently lots of prints in this file for testing
// Once the tests pass, they can be deleted

// assuming counter counts microseconds
// 20000 = 5% of 2ms
#define COUNTER_PERIOD 19999 //Maximal counter value
#define MIN_POWER_DUTY_CYCLE 6 //%
#define MAX_POWER_DUTY_CYCLE 10 //%


int percentageToMicrosecondsAtHighState(float percentage) {
	float neededDutyCycle = MIN_POWER_DUTY_CYCLE + (MAX_POWER_DUTY_CYCLE - MIN_POWER_DUTY_CYCLE) * 0.01 * percentage;
	printf("->      neededDutyCycle = %f percent \r\n", neededDutyCycle);

	return (int) (COUNTER_PERIOD + 1) * 0.01 * neededDutyCycle;
}


void MOTOR_SetPower(h_motor_t* h_motor, float percentage) {
	if (percentage > 100) {
		percentage = 100;
	}

	if (percentage < 0) {
		percentage = 0;
	}

	printf("-> power set to %f percent \r\n", percentage);

	int microsecondsAtHighState = percentageToMicrosecondsAtHighState(percentage);

	__HAL_TIM_SET_COMPARE(h_motor->htim, h_motor->channel, microsecondsAtHighState);

	printf("->      microsecondsAtHighState = %d \r\n", microsecondsAtHighState);

	h_motor -> PercentageOfTotalPower = percentage;
}

void MOTOR_SetBoth(h_motor_t* h_motor1, h_motor_t* h_motor2, float percentage) {
	if (percentage > 100) {
		percentage = 100;
	}

	if (percentage < 0) {
		percentage = 0;
	}

	printf("-> power set to %f percent \r\n", percentage);

	int microsecondsAtHighState = percentageToMicrosecondsAtHighState(percentage);

	__HAL_TIM_SET_COMPARE(h_motor1->htim, h_motor1->channel, microsecondsAtHighState);
	__HAL_TIM_SET_COMPARE(h_motor2->htim, h_motor2->channel, microsecondsAtHighState);

	printf("->      microsecondsAtHighState = %d \r\n", microsecondsAtHighState);

	h_motor1 -> PercentageOfTotalPower = percentage;
	h_motor2 -> PercentageOfTotalPower = percentage;
}



void MOTOR_Init(h_motor_t* h_motor) {
	printf("INITIALISATION STARTED\r\n");

	MOTOR_SetPower(h_motor, 100);

	HAL_TIM_PWM_Start(h_motor->htim, h_motor->channel);

	HAL_Delay(2000);

	MOTOR_SetPower(h_motor, 0);
	HAL_Delay(3000);

	printf("INITIALISATION COMPLETED\r\n");
}


void MOTOR_InitBoth(h_motor_t* h_motor1, h_motor_t* h_motor2) {
	printf("INITIALISATION STARTED\r\n");

	MOTOR_SetPower(h_motor1, 100);
	MOTOR_SetPower(h_motor2, 100);

	HAL_TIM_PWM_Start(h_motor1->htim, h_motor1->channel);
	HAL_TIM_PWM_Start(h_motor2->htim, h_motor2->channel);

	HAL_Delay(2000);

	MOTOR_SetPower(h_motor1, 0);
	MOTOR_SetPower(h_motor2, 0);
	HAL_Delay(3000);

	printf("INITIALISATION COMPLETED\r\n");
}


void MOTOR_TurnOff(h_motor_t* h_motor) {
	MOTOR_SetPower(h_motor, 0);
}


// This function is blocking so it is not recommended
void MOTOR_SetLinear(h_motor_t* h_motor, float finalPercentage, int timeInMilliseconds) {

	float initialPercentage = h_motor -> PercentageOfTotalPower;

	int millisInterval = 50;

	if (2*millisInterval > timeInMilliseconds) {
		millisInterval = 50;
		timeInMilliseconds = 4000;
	}

	int nSteps = timeInMilliseconds / millisInterval;

	float currentPercentage = initialPercentage;
	float percentagePerStep = (finalPercentage - initialPercentage) / nSteps;


	for (int i = 0; i < nSteps; i++) {
		currentPercentage += percentagePerStep;

		MOTOR_SetPower(h_motor, currentPercentage); // Needs SetPower to take float input
		HAL_Delay(millisInterval);
	}

}

void MOTOR_SetLinearBoth(h_motor_t* h_motor1, h_motor_t* h_motor2, float finalPercentage, int timeInMilliseconds) {
	//Assumes both motors are set to the same power value
	float initialPercentage = h_motor1 -> PercentageOfTotalPower;

	int millisInterval = 50;

	if (2*millisInterval > timeInMilliseconds) {
		millisInterval = 50;
		timeInMilliseconds = 4000;
	}

	int nSteps = timeInMilliseconds / millisInterval;

	float currentPercentage = initialPercentage;
	float percentagePerStep = (finalPercentage - initialPercentage) / nSteps;

	for (int i = 0; i < nSteps; i++) {
		currentPercentage += percentagePerStep;

		MOTOR_SetPower(h_motor1, currentPercentage);
		MOTOR_SetPower(h_motor2, currentPercentage);
		HAL_Delay(millisInterval);
	}

}
