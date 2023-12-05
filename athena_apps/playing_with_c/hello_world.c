#include <stdio.h>
#include <string.h>

/*
void functions used as a template for the compiler to know what to expect
*/
char test_function();
char secret_name();
char add_test();

//char greet = "Hello, world!"; this way doesnt work
char name[] = "martell";
char greet[] = "Hello, world!";

int main(void) {
	test_function();
	printf("\n");
	add_test();
	prtinf("\n");
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
	char* friends[5] = {"tim"};
	//or
	//char friends[0][5]; --> works on if your use snprintf()
	printf("the old list of friends --> [ %s ] \n", friends[0]);
	friends[1] = "wow";
	printf("changeing %s to %s\n", friends[0], friends[1] );
	friends[2] = "jimmy";
	printf("the new list of friends --> [ %s ]", friends[2]);
}



/**

for loops 2 more

start using structs and arrays




*/



