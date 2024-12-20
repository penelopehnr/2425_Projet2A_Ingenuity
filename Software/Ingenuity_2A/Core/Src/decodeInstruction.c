/*
 * decodeInstruction.c
 *
 *  Created on: Nov 5, 2024
 *      Author: JoelC
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include "decodeInstruction.h"


// int used as bool in this function

int inString (char c, char* str){
	char* currentChar = str;

	while (*currentChar != '\0') {
		if(*currentChar == c) {
			return 1;
		}
		currentChar++;
	}
	return 0;
}


int isFloat (char* str){
	char* currentChar = str;
	char* numbers = "0123456789";

	int etat = 0;

	while (*currentChar != '\0') {
		switch (etat) {
		case 0:
			if (*currentChar == '.') {
				etat = 1;

			} else if (inString(*currentChar, numbers)) {
				//ok
			} else {
				return 0;
			}
			break;

		case 1:
			if (*currentChar == '\0') {
				etat = 2;
				return 1;
			} else if (inString(*currentChar, numbers)) {
				//ok
			} else {
				return 0;
			}
			break;
		}
	currentChar++;
	}
	return 1;
}



void printLabelValue(LabelValue lv) {
	printf("LabelValue structure instance. Label: %s, Value: %f", lv.label, lv.value);
}


LabelValue checkInstruction(char* instruction){
	char* i = instruction;
	char* caracteresPermisLabel = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
	char* caracteresPermisValue = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.";

	char caractereDelimitation = '=';

	char label[100];
	char value[100];

	int indiceLabel = 0;
	int indiceValue = 0;

	int etat = 0;

	while(etat != 2) {
		switch (etat) {
		case 0:
			if(*i == '\0'){
				//error case
			} else if(*i == caractereDelimitation){
				etat = 1;
				label[indiceLabel] = '\0';
			} else if (inString(*i, caracteresPermisLabel)) {
				label[indiceLabel] = *i;
				indiceLabel++;
			} else {
				//error case
			}
			break;

		case 1:
			if(*i == '\0'){
				etat = 2;
				value[indiceValue] = '\0';

			} else if(*i == caractereDelimitation){
				//error case
			} else if (inString(*i, caracteresPermisValue)) {
				value[indiceValue] = *i;
				indiceValue++;
			} else {
				//error case
			}
			break;
		}
	i++;
	}
	if (etat == 2) {
		if (isFloat(value)) {
			LabelValue result;
			strcpy(result.label, label);
			result.value = strtof(value, NULL);
			return result;
		} else {
			LabelValue result;
			strcpy(result.label, "LABELVALUE ERROR: VALUE FIELD NOT FLOAT");
			result.value = NAN;
			return result;
		}
	} else {
		LabelValue result = {
			.label = "LABELVALUE ERROR: INPUT DOES NOT FIT INSTRUCTION FORMAT",
			.value = NAN
		};

		return result;
	}
}


LabelValueArray checkFrameForInstructions(char* frame, char beginning, char end) {
	int i = 0;
	int state = 0;
	char instruction[200];
	int instructionCurrentIndex = 0;
	LabelValue instructions[100];
	int numberOfInstructions = 0;

	while (frame[i] != '\0') {
		if (state == 0) {
			if (frame[i] == beginning) {
				state = 1;
			}
		} else if (state == 1) {
			if (frame[i] == end) {
				instruction[instructionCurrentIndex] = '\0';
				instructionCurrentIndex = 0;
				state = 0;

				LabelValue contentsOfInstruction = checkInstruction(instruction);
				instructions[numberOfInstructions] = contentsOfInstruction;
				numberOfInstructions++;
			} else {
				instruction[instructionCurrentIndex] = frame[i];
				instructionCurrentIndex++;
			}
		}
		i++;
	}

	LabelValueArray arrayOfInstructions;
	memcpy(arrayOfInstructions.instructions, instructions, sizeof(LabelValue) * numberOfInstructions);
	arrayOfInstructions.n = numberOfInstructions;

	return arrayOfInstructions;
}



 int applyLabelValue(LabelValue lv, DictOfFloatVariables dictOfVar) {
	 char * nameOfVariableToBeChanged = lv.label;
	 float newValue = lv.value;

	 int i = 0;

	 //strcmp: equal strings => returns 0
	 //strcmp: difft strings => returns 1

	 while (i < dictOfVar.n && strcmp(nameOfVariableToBeChanged, dictOfVar.variableNames[i])) {
		 i++;
	 }

	 if (i == dictOfVar.n) {
		 // Error case
		 return 1;
	 } else {
		 float* pointerToVariableAddress = dictOfVar.variables[i];

		 *pointerToVariableAddress = newValue;
	 }
	 return 0;
 }

