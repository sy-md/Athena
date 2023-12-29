#include <stdio.h>
#include <string.h>

int LinkListTest();

int main(void) {
	LinkListTest();
    return 0;
};

struct node {
	int val;
	//int next;
	struct node* next;
};
struct linkedlist {
	//int head;
	//int prev;
	// could i use null
	struct node* head;
	struct node* prev;
};
int LinkListTest() {
	/* 
		given a array of num 1,2,3 create a linklist
		1.) make a struct that builds a node
		2.) mkae a struct that builds a linklist{empty}
		3.) create a node and assign it to the head out the linkedlist
		4.) see if you can create another node that is assigned to the heads next
	
	*/
	struct linkedlist lst; // create a linkedlist
	
	struct node nd = {1};  // create a node
	struct node ndd = {2};
	
	lst.head = &nd; // assign a node the a pos in the linkedlist
	lst.head->next = &ndd;
	
	printf("%d ->",lst.head->val);
	printf("%d ->",lst.head->next->val);

};





