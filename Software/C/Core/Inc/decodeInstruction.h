/*
 * decodeInstruction.h
 *
 *  Created on: Nov 5, 2024
 *      Author: JoelC
 */

#ifndef INC_DECODEINSTRUCTION_H_
#define INC_DECODEINSTRUCTION_H_


typedef struct {
	char label[100];
	float value;
} LabelValue;


typedef struct {
	LabelValue instructions[100];
	int n;
} LabelValueArray;


typedef struct {
	int n;
	char** variableNames;
	float** variables;
} DictOfFloatVariables;



// Function declarations
int inString(char c, char* str);
int isFloat(char* str);
void printLabelValue(LabelValue lv);
LabelValue checkInstruction(char* instruction);
LabelValueArray checkFrameForInstructions(char* frame, char beginning, char end);
int applyLabelValue(LabelValue lv, DictOfFloatVariables dictOfVar);




#endif /* INC_DECODEINSTRUCTION_H_ */
