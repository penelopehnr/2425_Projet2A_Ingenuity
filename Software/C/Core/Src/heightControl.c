/*
 * heightControl.c
 *
 *  Created on: Apr 1, 2025
 *      Author: PC
 */


// We started separating the control code into this file for cleanliness and organization but have not finished doing so (this functionality is still in main.c)


/*
int* constantHeightControl(int distance, int height, int constantPercentageVariation) {
	if(distance < height) {
		int current_percentage = upperMotor.PercentageOfTotalPower;
		MOTOR_SetPower(&upperMotor, current_percentage + constantPercentageVariation);
		MOTOR_SetPower(&lowerMotor, current_percentage + constantPercentageVariation);
	} else if(distance > height) {
		int current_percentage = upperMotor.PercentageOfTotalPower;
		MOTOR_SetPower(&upperMotor, current_percentage - constantPercentageVariation);
		MOTOR_SetPower(&lowerMotor, current_percentage - constantPercentageVariation);
	}
}




// maxPercentageVariation 5
int* linearHeightControl(int distance, int height, int k, int maxPercentageVariation) {

	if(distance < height) {
		int distanceToGoal = height - distance;

		int percentageVariation = distanceToGoal/10;

		if (percentageVariation > maxPercentageVariation) {
			percentageVariation = maxPercentageVariation;
		}

		int current_percentage = upperMotor.PercentageOfTotalPower;

		MOTOR_SetPower(&upperMotor, current_percentage + percentageVariation);
		MOTOR_SetPower(&lowerMotor, current_percentage + percentageVariation);

	} else if(distance > height) {
		int distanceToGoal = distance - height;

		int percentageVariation = distanceToGoal/10;

		if (percentageVariation > maxPercentageVariation) {
			percentageVariation = maxPercentageVariation;
		}

		int current_percentage = upperMotor.PercentageOfTotalPower;

		MOTOR_SetPower(&upperMotor, current_percentage - percentageVariation);
		MOTOR_SetPower(&lowerMotor, current_percentage - percentageVariation);
	}
}





int* PDHeightControl(float distance, float height, float Kp, float Kd, float previousError, float dt, float maxPercentageVariation) {

	// Compute error
	int error = height - distance;

	// Proportional term
	float P = Kp * error;

	// Derivative term (rate of error change)
	float derivative = (error - previousError) / dt;
	float D = Kd * derivative;

	// Compute PD output
	float pdOutput = P + D;

	// Limit power variation (Optional)
	int maxVariation = 5;
	if (pdOutput > maxVariation) pdOutput = maxVariation;
	if (pdOutput < -maxVariation) pdOutput = -maxVariation;

	// Get current motor power
	int currentPower = upperMotor.PercentageOfTotalPower;

	// Set new motor power
	MOTOR_SetPower(&upperMotor, currentPower + (int)pdOutput);
	MOTOR_SetPower(&lowerMotor, currentPower + (int)pdOutput);

	// Update previous error for next iteration
	previousError = error;
}
*/
