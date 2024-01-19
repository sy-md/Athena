#include <stdio.h>
#include <string.h>
#include <stdlib.h> // needed for using malloc()

void cycle_linklist();

struct node {
  int val;
  struct node *next; 
};

void cycle_linklist(struct node *p) {
    while (p != NULL) {
        printf("%d->", p->val);
        p = p->next;
    }
};

int main() {

    /*
        **initalize the creation of the nodes**

        below we created the node
        struct node *___ = NULL --> {_,NULL}
        we assign it as ___
        the malloc function is telling the machine to make room for
        another node that will be taking up that sapce [64->8bit/ 32->4bits]
    */
    struct node *head;
    struct node *one = malloc(sizeof(struct node));
    struct node *two = malloc(sizeof(struct node));

    // Assign value values
    one->val = 1;
    two->val = 2;

    // Connect nodes
    one->next = two;
    two->next = NULL;

    head = one;

    cycle_linklist(head);

};

/* 
  try looking up the free() function youll be usin this when
  wanted to point to another node for example:

  1->2->3
  make 1's next be 3
  so youll use free() to somehow create
  1->3
  

*/










