/*
 * motor.h
 *
 *  Created on: May 27, 2024
 *      Author: JoelC
 */

#include "main.h" // To get the types

#ifndef INC_MOTOR_H_
#define INC_MOTOR_H_

// Handle Motor Type

typedef struct {
	TIM_HandleTypeDef* htim;
	uint32_t channel;
	float PercentageOfTotalPower;
} h_motor_t;


int percentageToMicrosecondsAtHighState(int percentage);
int percentageToMicrosecondsAtHighState(int percentage);
void MOTOR_Init(h_motor_t* h_motor);
void MOTOR_TurnOff(h_motor_t* h_motor);


#endif /* INC_MOTOR_H_ */







