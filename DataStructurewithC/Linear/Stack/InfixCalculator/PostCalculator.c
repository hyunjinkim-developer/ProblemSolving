#include <ctype.h>
#include <stdio.h>
#include <string.h>

#include "ListBaseStack.h"

int EvalRPNExp(char exp[])
{
	Stack stack;
	int expLen = strlen(exp);
	
	StackInit(&stack);

	char tok;
	for (int i = 0; i < expLen; i++)
	{
		tok = exp[i];
		// if tok is number
		if (isdigit(tok))
		{
			SPush(&stack, tok - '0');
		}
		// if tok is operator
		else
		{
			int op2 = SPop(&stack); // Second operand
			int op1 = SPop(&stack);	// First operand

			switch(tok)
			{
				case '+':
					SPush(&stack, op1 + op2);
					break;
				case '-':
					SPush(&stack, op1 - op2);
					break;
				case '*':
					SPush(&stack, op1 * op2);
					break;
				case '/':
					SPush(&stack, op1 / op2);
					break;
			}
		}
	}
	//return final result
	return SPop(&stack);
}
