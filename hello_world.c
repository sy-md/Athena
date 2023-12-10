#include <stdio.h>
#include <string.h>

/*
void functions used as a template for the compiler to know what to expect
*/
char test_function();
char secret_name();
char add_test();
void WhoFreindsWithWho();

//char greet = "Hello, world!"; this way doesnt work
char name[] = "martell";
char greet[] = "Hello, world!";

int main(void) {
	//can i call a funtion from within a function? making my main function cleaner and only caling one function
	test_function();
	printf("\n");
	add_test();
	printf("\n");
	secret_name();
	printf("\n");
	printf("hello world\n");
    return 0;
}

char test_function() {
	/*
		a simpl first function that checks if a name is equal to a string
		if it is then print a message, else print default messsge
	*/
	if (name == "martell"); {
		printf("this a name thats works");
	}
	printf("%s\n", greet);
}

char secret_name() {
	/*
		a charcter function that takes a variable and loos through it, counting
		the number of characters in the string then displaying the name
	*/
	int i;
	for (i = 0; i < strlen(name); i++) {
		i = i;
	}
	printf("your name is %s \n", name);
	printf("your name has %i chartcers \n", i);
}

char add_test() {
	/*
		a function to test the array system in c... can i add to an array?
		while using concatenation
	*/
	char* friends[5] = {"tim"}; // OR : --> char friends[0][5]; --> works on if your use snprintf()
	printf("the old list of friends --> [ %s ] \n", friends[0]);
	friends[1] = "wow";
	printf("changeing %s to %s\n", friends[0], friends[1] );
	friends[2] = "jimmy";
	printf("the new list of friends --> [ %s ]", friends[2]);
}

void WhoFreindsWithWho() {
	/*
		creating a struct to hold data
	*/
	struct people {
		char name[50]; // char* use string literal
		int age;
		char friends[2][50];
	};
	
	struct people peeps[] = { {.name = "martell", .age = 21, .friends = "tim" }, {"tim", 21, "martell"} };


	// what is the difference between the two?

	struct people p1 = {"martell", 21, "tim"}; 
	struct people p2 = {"tim", 21, "martell"};
	char* friends[2] = {p1[0].name, p1[2].friends};

	/* 	
		so why does it wont me to do it like this: 
		isnt this creating another whole struct?
	*/
	 struct people myPeople[2]  = {
		{"martell", 21, "tim"},
		{"tim", 21, "martell"}
	};

	// but why cant i do this?

	struct people p1 = {"martell", 21, "tim"}; 
	struct people p2 = {"tim", 21, "martell"};
	struct people friends[2] = {&p1, &p2};

	printf("%s is %d years old and his friends is %s",p1.name, p1.age, p1.friends);
	// or
	//printf("%s is %d years old and his friends is %s",myPeople[0].name, myPeople[0].age, myPeople[0].friends);
}


/*

next play with the for loops and while loops and u should have the basics isshhh

lifetimes of variables
	- static
	- automatic
	- allocated
	- thread
	- register
 
  int myNumbers[4] = {25, 50, 75, 100};
  int *ptr = myNumbers;
  int i;

  for (i = 0; i < 4; i++) {
    printf("[Pointer Method] --> %d: i is %d\n", *(ptr + i), i);
  }
    // same as
  for (i = 0; i < 4; i++) {
    printf("[Array calling Method] --> %d: i is %d\n", myNumbers[i],i);
  }
  return 0;
}



 

*/





