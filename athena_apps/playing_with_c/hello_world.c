
#include <stdio.h>
#include <string.h>

/*declarations functions above the main fucntions
must match the defintinive functions so void void and char and the 
char i think we should test the dict and arrays and what not*/
;
char name[] = "martell";
char greet[] = "Hello, world!";
//char greet = "Hello, world!"; this way doesnt work

// void functions used as a template for knowing what file is what and what they return ?
void test_function();
void secret_name()

// main function
int main(void) {
	test_function();
	printf("");
	secret_name();
	//printf("hello world\n");
    	return 0;
}

// and these are defintive functions that run now sure how the layout is suppose to be
void test_function() {
	if (name == "martell"); {
		printf("this a name thats works");
	}
	printf("%s\n", greet);
	//printf("testing");

}

void secret_name() {
	//int i;
	for (i = 0; i < strlen(name); i++) {
		i = i;
	}
	printf("your name is %s \n", name);
	printf("your name has %i chartcers \n", i);

}





