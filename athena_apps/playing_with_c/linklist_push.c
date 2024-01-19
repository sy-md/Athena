#include <stdio.h>
#include <string.h>
#include <stdlib.h> // needed for using malloc()

void cycle_linklist(); // traverse
void push(); // C
void remove_at(); // R
void insert_at(); // U
void delete_nd(); // D

struct node { // node blueprint
  int val;
  struct node *next; 
};

void cycle_linklist(struct node *p) { // traverse
    while (p != NULL) {
        printf("%d->", p->val);
        p = p->next;
    }
    printf("END");
};

void push(struct node** p,int data)  { //update 
    struct node *new_node = (struct node *) malloc(sizeof(struct node));
    new_node->val = data;
    new_node->next = *p;
    *p = new_node;
};

void remove_at(struct node* p, int trg) { //remove
    /*
        given a linkedlist traverse in till found then remove prev pointer then assign it 
        to given nodes next
        1->2->3
        1->3
    */
    struct node *worker = p; // just reassigning my p to worker
    struct node *prev = NULL; 

    while (worker->next != NULL) {
    
        //printf("%d",worker->val);
        if (worker->val == trg) {
            printf("%d",prev->val);

            struct node *temp = worker->next;
            prev->next = temp;

            free(worker);
            break;
        } else {
            prev = worker;
            worker = worker->next;
        }
    }
};

void insert_at(struct node* p, int data, int trg) { // update at
    /*
        givene a node and data find the node given then
        create a node with the data given
        then have the found nodes next be the newly created node
    */
    struct node *worker = p; // just reassigning my p to worker

    while (worker->next != NULL) {
    
        if (worker->val == trg) { 
            struct node *new_node = (struct node *) malloc(sizeof(struct node));
            new_node->val = data;
            struct node *temp = worker->next;
            worker->next = new_node;
            new_node->next = temp;
            break;
        } else {
            worker = worker->next;
        }
    }

};

void delete_nd(struct node* p) { //deleting end
    /*
        given root of linkedlist traverse then remove the last node

    */
    struct node *worker = p;
    struct node *prev = NULL;
    while (worker != NULL) { // i have worekd->next != NULL wow just wow

        if ( worker->next == NULL) {
            prev->next = NULL;
            free(worker);
            break;
        } else {
            prev = worker;
            worker = worker->next;
        }
    }

};

int main() { // driver code
    struct node *head = malloc(sizeof(struct node));

    push(&head, 1);
    push(&head, 2);
    push(&head, 3);
    push(&head, 4);
    push(&head, 5);
    cycle_linklist(head);
    printf("\n displaying the previous node of 2\n");
    remove_at(head,2);
    printf("\n removing 2\n");
    cycle_linklist(head);
    insert_at(head, 8, 4);
    printf("\n insertin 8 after 4\n");
    cycle_linklist(head);
    delete_nd(head);
    printf("\n deleting last node\n");
    cycle_linklist(head);
};  



