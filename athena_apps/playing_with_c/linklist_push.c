#include <stdio.h>
#include <string.h>
#include <stdlib.h> // needed for using malloc()

void cycle_linklist();
void insert();

struct node {
  int val;
  struct node *next; 
};

void cycle_linklist(struct node *p) {
    while (p != NULL) {
        printf("%d->", p->val);
        p = p->next;
    }
    printf("END");
};

void push(struct node** p,int data)  {
    struct node *new_node = (struct node *) malloc(sizeof(struct node));
    new_node->val = data;
    new_node->next = *p;
    *p = new_node;
};

int main() {
    struct node *head = malloc(sizeof(struct node)); // create first node in memory

    push(&head, 1);
    push(&head, 2);
    push(&head, 3);
    push(&head, 4);
    push(&head, 5);
    cycle_linklist(head);
};