/**
 *****************************************************************************
 * @file	vl53l1x.c
 * @author 	Arnaud C.
 *****************************************************************************
 */

#include "vl53l1x.h"

/* Variables ----------------------------------------------------------------*/
vl53l1x_Cfg tof[VL53L1X_MAX_NB]; // library sensor configurations
uint8_t status = 0;

/* End of variables ---------------------------------------------------------*/

/* Functions ----------------------------------------------------------------*/

/**
 * vl53l1x_init: sensors initialization
 * @param xshutCfg Structure which contains xshut pins informations
 * @param nb_sensors number of sensors used
 * @return 0 if succeeded
 */
int vl53l1x_init(xshut *xshutCfg, int nb_sensors)
{
	printf("\r\n");
	printf("Initialization started for %d vl53l1x sensor(s)\r\n", nb_sensors);

	// Clear library configuration
	if(vl53l1x_clearCfg() != 0){
		return -1;
	}
	printf("VL53L1X library configuration cleared...\r\n");

	// Retrieve user parameters
	for(int i=0; i<nb_sensors; i++){
		tof[i].pin_xshut = xshutCfg[i];
		HAL_GPIO_WritePin(tof[i].pin_xshut.GPIOx, tof[i].pin_xshut.GPIO_Pin,
			GPIO_PIN_RESET);
	}

	HAL_Delay(250);

	// Initialization
	for(int j=0; j<nb_sensors; j++)
	{
		uint8_t sensorState = 0;
		uint8_t byteData; uint16_t wordData;

		// Xshut pin drive to high state
		HAL_GPIO_WritePin(tof[j].pin_xshut.GPIOx, tof[j].pin_xshut.GPIO_Pin,
				GPIO_PIN_SET);
		HAL_Delay(250);

		// Retrieve sensor informations
		status = VL53L1_RdByte(tof[j].i2c_address, 0x010F, &byteData);
		printf("VL53L1X Model_ID[%d]: %X\r\n", j, byteData);
		status = VL53L1_RdByte(tof[j].i2c_address, 0x0110, &byteData);
		printf("VL53L1X Module_Type[%d]: %X\r\n", j, byteData);
		status = VL53L1_RdWord(tof[j].i2c_address, 0x010F, &wordData);
		printf("VL53L1X[%d]: %X\r\n", j, wordData);

		// Retrieve sensor boot state
		while(sensorState == 0){
			status = VL53L1X_BootState(tof[j].i2c_address, &sensorState);
			HAL_Delay(250);
		}
		printf("Chip booted...\r\n");

		// Sensor init
		status = VL53L1X_SensorInit(tof[j].i2c_address);

		// Set new i2c address
		if((status = VL53L1X_SetI2CAddress(tof[j].i2c_address, 0x52 + (j+1) * 2)) == VL53L1_ERROR_NONE){
			tof[j].i2c_address = 0x52 + (j+1) * 2;
			printf("tof[%d] -> new i2c addr: 0x%2X\r\n", j, tof[j].i2c_address);
		}

		/* TO DO: Understand why incrementing i2c addresses one by one does not work. */

		HAL_Delay(250);

		// Set sensor parameters
		if((status = vl53l1x_setParameters(j)) != VL53L1_ERROR_NONE){
			return -1;
		}
		printf("vl53l1x parameters set...\r\n");

		printf("\r\n");
		HAL_Delay(250);
	}

	// Start ranging
	for(int k=0; k<nb_sensors; k++){
		if((status = VL53L1X_StartRanging(tof[k].i2c_address)) == VL53L1_ERROR_NONE){
			printf("vl53l1x[%d] started...\r\n", k);
		}
		HAL_Delay(250);
	}

	return 0;
}

/**
 * vl53l1x_clearCfg: clear lib config structure
 * @return 0
 */
int vl53l1x_clearCfg()
{
	for(int i=0; i<VL53L1X_MAX_NB; i++)
	{
		status = 0;

		tof[i].i2c_address = VL53L1X_DEFAULT_ADDRESS;
		tof[i].pin_xshut.GPIOx = NULL;
		tof[i].pin_xshut.GPIO_Pin = 0;
	}

	return 0;
}


/**
 * vl53l1x_setParameters: set sensor parameters
 * @param i sensor index
 * @return status
 */
int vl53l1x_setParameters(int i)
{
	status = VL53L1X_SetDistanceMode(tof[i].i2c_address, 1); // 1=short, 2=long
	status = VL53L1X_SetInterMeasurementInMs(tof[i].i2c_address, 200); // in ms, IM must be > = TB
	status = VL53L1X_SetTimingBudgetInMs(tof[i].i2c_address, 200); // in ms possible values [20, 50, 100, 200, 500]
	//status = VL53L1X_SetDistanceThreshold(tof[i].i2c_address, 500, 10, 1, 0); // config sympa
	//status = VL53L1X_SetROI(tof[i].i2c_address, 16, 16); // minimum ROI 4,4

	//status = VL53L1X_SetOffset(tof[i].i2c_address, 20); // offset compensation in mm
	//status = VL53L1X_CalibrateOffset(dev, 140, &offset); // may take few second to perform the offset cal
	//status = VL53L1X_CalibrateXtalk(dev, 1000, &xtalk); // may take few second to perform the xtalk cal

	return status;
}

/**
 * vl53l1x_getDistance: get distance value
 * @param i sensor index
 * @return distance
 */
uint16_t vl53l1x_getDistance(int i){
	uint16_t distance = 0;

	if((status = VL53L1X_GetDistance(tof[i].i2c_address, &distance)) != VL53L1_ERROR_NONE){
		printf("VL53L1X_GetDistance failed...\r\n");
	}

	if((status = VL53L1X_ClearInterrupt(tof[i].i2c_address)) != VL53L1_ERROR_NONE){
		printf("VL53L1X_ClearInterrupt failed...\r\n");
		return -1;
	}

	return distance;
}

/* End of functions ---------------------------------------------------------*/
