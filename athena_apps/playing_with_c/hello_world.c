#include <stdio.h>
#include <string.h>

/*declarations functions above the main fucntions
must match the defintinive functions so void void and char and the 
char i think we should test the dict and arrays and what not*/

//char greet = "Hello, world!"; this way doesnt work
char name[] = "martell";
char greet[] = "Hello, world!";

// void functions used as a template for knowing what file is what and what they return ?
char test_function();
char secret_name();
char add_test();

// main function
int main(void) {
	//test_function();
	//printf("");
	add_test();
	//secret_name();
	//printf("hello world\n");
    	return 0;
}

// and these are defintive functions that run now sure how the layout is suppose to be
char test_function() {
	if (name == "martell"); {
		printf("this a name thats works");
	}
	printf("%s\n", greet);
	//printf("testing");
}

char secret_name() {
	int i;
	for (i = 0; i < strlen(name); i++) {
		i = i;
	}
	printf("your name is %s \n", name);
	printf("your name has %i chartcers \n", i);
	
}


char add_test() {
	char* friends[5] = {"tim"}; //works simply with ____[] = ___;
	//or
	//char friends[0][5]; // works on if your use snprintf()
	printf("the old list of friends --> [ %s ] \n", friends[0]);
	friends[1] = "wow";
	printf("changeing %c to %c\n", friends[0], friends[1] );
	friends[2] = "jimmy";
	printf("the new list of friends --> [ %s ]", friends[2]);

}




