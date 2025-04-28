/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "adc.h"
#include "i2c.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "string.h"
#include "motor.h"
#include "decodeInstruction.h"
#include "stdio.h"
#include "stdlib.h"
#include "math.h"

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#include "VL53L1X_api.h"
#include "vl53l1_error_codes.h"


/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define MAX_ACK_MESSAGE_LENGTH 256

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#define VL53L1X_DEFAULT_ADDRESS (0x29 << 1)

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
int __io_putchar(int ch)
{
  HAL_UART_Transmit(&huart1, (uint8_t *)&ch, 1, HAL_MAX_DELAY);
  return ch;
}

int __io_getchar(void)
{
  uint8_t ch = 0;
  __HAL_UART_CLEAR_OREFLAG(&huart1);
  HAL_UART_Receive(&huart1, (uint8_t *)&ch, 1, HAL_MAX_DELAY);
  HAL_UART_Transmit(&huart1, (uint8_t *)&ch, 1, HAL_MAX_DELAY);
  return ch;
}


char startChar = '@';
char endChar = '#';

uint8_t rx_char; // Variable to store the received character

char instruction[200];
int indexInstruction = 0;

int UARTReceiverState = 0;

volatile int flagUART1 = 0;
volatile int flagTIM6 = 0;


void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef * htim) {
	if (htim -> Instance == TIM6) {
		flagTIM6 = 1;
	}
}


void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart) {

	instruction[indexInstruction] = rx_char;
	indexInstruction++;

	// Re-enable UART interrupt reception
	HAL_UART_Receive_IT(&huart2, &rx_char, 1);

	if (rx_char == '#')
	{
		instruction[indexInstruction] = 0; // 0 character for the printf
		indexInstruction = 0;
		flagUART1 = 1;
	}
}


uint32_t measure_counter = 0;
uint8_t data_available = 0;
uint16_t distance;

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
	if (TOF_INT_Pin == GPIO_Pin)
	{
		measure_counter++;
		data_available++;
	}
}


/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{

  /* USER CODE BEGIN 1 */


  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_ADC1_Init();
  MX_I2C1_Init();
  MX_SPI1_Init();
  MX_TIM2_Init();
  MX_USART1_UART_Init();
  MX_USART2_UART_Init();
  MX_TIM6_Init();
  /* USER CODE BEGIN 2 */

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	printf("\r\n===== VL53L1X-SATEL =====\r\n");

	uint16_t id;
	if (VL53L1X_GetSensorId(VL53L1X_DEFAULT_ADDRESS, &id) != VL53L1_ERROR_NONE)
	{
		Error_Handler();
	}
	printf("SensorID : 0x%X\r\n", id);

	VL53L1X_Version_t version;
	if (VL53L1X_GetSWVersion(&version) != VL53L1_ERROR_NONE)
	{
		Error_Handler();
	}
	printf("Version : %u.%ub%ur%lu\r\n", version.major, version.minor, version.build, version.revision);

	uint8_t boot_state = 0;
	uint8_t boot_state_counter = 0;

	while(boot_state == 0)
	{
		boot_state_counter++;
		if (VL53L1X_BootState(VL53L1X_DEFAULT_ADDRESS, &boot_state) != VL53L1_ERROR_NONE)
		{
			Error_Handler();
		}
		HAL_Delay(1);
	}

	printf("Chip booted in %d...\r\n", boot_state_counter);

	//Loads the 135 bytes default values to initialize the sensor.
	if (VL53L1X_SensorInit(VL53L1X_DEFAULT_ADDRESS) != VL53L1_ERROR_NONE)
	{
		Error_Handler();
	}
	printf("Sensor initialized with the default values\r\n");

	if (VL53L1X_SetDistanceMode(VL53L1X_DEFAULT_ADDRESS, 1) != VL53L1_ERROR_NONE) // 1=short, limited to 1.3m
	{
		Error_Handler();
	}
	printf("Short distance mode\r\n");

	if (VL53L1X_SetTimingBudgetInMs(VL53L1X_DEFAULT_ADDRESS, 50) != VL53L1_ERROR_NONE) // in ms possible values [20, 50, 100, 200, 500]
	{
		Error_Handler();
	}

	if (VL53L1X_SetInterMeasurementInMs(VL53L1X_DEFAULT_ADDRESS, 50) != VL53L1_ERROR_NONE) // in ms, IM must be >= TB
	{
		Error_Handler();
	}

	printf("Timing budget set\r\n");

	if (VL53L1X_StartRanging(VL53L1X_DEFAULT_ADDRESS) != VL53L1_ERROR_NONE)
	{
		Error_Handler();
	}

	  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





  //Start Timer 6
  HAL_TIM_Base_Start_IT(&htim6);

	printf("--------------EXECUTION BEGINS--------------\r\n\n");

	// We define the dictionary of variables that can get modified by receiving a UART signal
	float height = 0.0;
	float LEDState = 0.0;
	float eLanding = 0.0;
	char* variableNames[3] = {"height", "LEDState", "eLanding"};
	float* variablePointers[3] = {&height, &LEDState, &eLanding};
	DictOfFloatVariables dictOfVariables = {
		.n = 3,
		.variableNames = variableNames,
		.variables = variablePointers
	};


	h_motor_t upperMotor;
	h_motor_t lowerMotor;

	upperMotor.htim = &htim2;
	lowerMotor.htim = &htim2;

	upperMotor.channel = TIM_CHANNEL_1;
	lowerMotor.channel = TIM_CHANNEL_2;

	MOTOR_InitBoth(&lowerMotor, &upperMotor);


	// Important, initiate character reception.
	// This line also being in HAL_UART_RxCpltCallback's body ensures continuous reception
	HAL_UART_Receive_IT(&huart2, &rx_char, 1);



  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */

  // This variable sets if the vertical control is constant (0), proportional (1) or proportional-derivative (2)
  int approach = 1;

  // Variables for Proportional Derivative Approach
  float Kp = 1.0;
  float Kd = 0.5;

  float previousError = 0;
  float dt = 0.05; // Time step (I calculated it based on our tim6 configuration)

  while (1)
  {

	  if (data_available > 0)
		{
			data_available = 0;
			uint16_t newDistance;

			if (VL53L1X_ClearInterrupt(VL53L1X_DEFAULT_ADDRESS) != VL53L1_ERROR_NONE)
			{
				Error_Handler();
			}
			if (VL53L1X_GetDistance(VL53L1X_DEFAULT_ADDRESS, &newDistance) != VL53L1_ERROR_NONE)
			{
				Error_Handler();
			}

			if (height != 0 && newDistance == 0) {
				// keep current value of distance to make sure to avoid any division by zero
			} else {
				distance = newDistance;
			}
		}

	  if (flagTIM6 == 1) {
		  flagUART1 = 0;

		  //printf("distance(%lu) : %u\r\n", measure_counter, distance);

		  if (approach == 0) {
			  if(distance < height) {
				  int current_percentage = upperMotor.PercentageOfTotalPower;
				  MOTOR_SetPower(&upperMotor, current_percentage + 1);
				  MOTOR_SetPower(&lowerMotor, current_percentage + 1);
			  } else if(distance > height) {
				  int current_percentage = upperMotor.PercentageOfTotalPower;
				  MOTOR_SetPower(&upperMotor, current_percentage - 1);
				  MOTOR_SetPower(&lowerMotor, current_percentage - 1);
			  }
		  } else if (approach == 1) {
			  int maxPercentageVariation = 5;
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
		  } else if (approach == 2) {
			  int error = height - distance;

			  float P = Kp * error;

			  float derivative = (error - previousError) / dt;
			  float D = Kd * derivative;

			  float pdOutput = P + D;

			  int maxVariation = 5;
			  if (pdOutput > maxVariation) pdOutput = maxVariation;
			  if (pdOutput < -maxVariation) pdOutput = -maxVariation;

			  int currentPower = upperMotor.PercentageOfTotalPower;

			  MOTOR_SetPower(&upperMotor, currentPower + (int)pdOutput);
			  MOTOR_SetPower(&lowerMotor, currentPower + (int)pdOutput);

			  previousError = error;
		  }
	  }


	  // This is a test to check that instructions can correctly be received
	  // by UART and affect change (modified variables, LED toggled)
	  if (flagUART1 == 1) {
		  printf("instruction = %s\r\n", instruction);

		  flagUART1 = 0;

		  LabelValue lv = checkInstruction(instruction);
		  printLabelValue(lv);

		  if (isnan(lv.value)) {
			  // error case
		  } else {
			  int applyLVReturnValue = applyLabelValue(lv, dictOfVariables);

			  if (applyLVReturnValue) { // If the return value is 1, it failed
				  // error case
			  } else {
				  char ackReceivedSuccess[MAX_ACK_MESSAGE_LENGTH];

				  sprintf(ackReceivedSuccess, "Received %s", instruction);
				  HAL_UART_Transmit_IT(&huart2, (uint8_t*)ackReceivedSuccess, strlen(ackReceivedSuccess));
			  }
		  }


		  if (eLanding != 0.0) {
			  MOTOR_SetLinearBoth(&upperMotor, &lowerMotor, 0.0, 5000);
			  //wait 5 s
			  eLanding = 0.0;
		  } else {
			  // Old motor update based solely on height instruction, use if you don't want any control
			  //MOTOR_SetPower(&upperMotor, height);
			  //MOTOR_SetPower(&lowerMotor, height);
		  }


		  // You can use this LED test to check if communication works without any danger
		  if(LEDState != 0.0) {
			  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_15, GPIO_PIN_SET);
		  } else {
			  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_15, GPIO_PIN_RESET);
		  }
	  }
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  if (HAL_PWREx_ControlVoltageScaling(PWR_REGULATOR_VOLTAGE_SCALE1) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_MSI;
  RCC_OscInitStruct.MSIState = RCC_MSI_ON;
  RCC_OscInitStruct.MSICalibrationValue = 0;
  RCC_OscInitStruct.MSIClockRange = RCC_MSIRANGE_6;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_MSI;
  RCC_OscInitStruct.PLL.PLLM = 1;
  RCC_OscInitStruct.PLL.PLLN = 40;
  RCC_OscInitStruct.PLL.PLLQ = RCC_PLLQ_DIV2;
  RCC_OscInitStruct.PLL.PLLR = RCC_PLLR_DIV2;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_4) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
