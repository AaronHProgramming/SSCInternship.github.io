#include <stdio.h>
#include <stdlib.h>

struct Ball{
	int bounciness;
	int ballNo;
};

int main(){
	int *dayPointer;
	int day;
	int variablesGoHere;
	int isVariable;
	struct Ball ball1;
	ball1.bounciness = 3;
	ball1.ballNo = 1;

	printf("Ball %d has bounciness: %d\n", ball1.ballNo, ball1.bounciness);

	printf("How long have you been working?\n");
	scanf("%d", &day);
	dayPointer = malloc(sizeof(*dayPointer));
	*dayPointer = 32;
	if(day >= 100) {
		printf("Get outta here!\n");
	}
	else {
		printf("That's a lot of days: %d\n", *dayPointer);
	}
	free(dayPointer);
	printf("The variable location is %p \n", &day);
	isVariable = 40;
	printf("Pointer location: %p\n", &isVariable);
	printf("Value: %d\n", isVariable);
	return 0;
}
