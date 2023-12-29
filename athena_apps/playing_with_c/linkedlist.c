#include <stdio.h>
#include <string.h>

int LinkListTest();

struct node {
	int val;
	//int next;
	struct node* next;
    struct node* prev;
};
struct linkedlist {
	//int head;
	//int prev;
	// could i use null
	struct node* head;
	struct node* prev;
};

int main(void) {
	LinkListTest();
    return 0;
};

int LinkListTest() {
	/* 
		
		1.) make a struct that builds a node
		2.) make a struct that builds a linklist{empty}
		3.) create a node and assign it to the head out the linkedlist
		4.) see if you can create another node that is assigned to the heads next
        Questions: where do i use the tmp method
	*/
    
    // create a linkedlist
	struct linkedlist lst; 
	
    // create a node
	struct node nd = {1, NULL};  
	struct node ndd = {2, NULL};
	
    // assign a node the a pos in the linkedlist
	lst.head = &nd; 
	lst.head->next = &ndd;
    lst.head->next->prev = &nd;
	
    //printing the nodes
	printf("%d->",lst.head->val);
	printf("%d->",lst.head->next->val);
    printf("\n");

    // displaying witch node is prev of which node
    printf("prev of node %d is %d", lst.head->next->val,lst.head->next->prev->val);

};





