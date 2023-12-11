#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int front(int** t, int size){
    return t[0][size-1];
}

bool isEmpty(int** t, int size) {
    if(size == 0) {
        return true;
    }
    return false;
}

// Removes and returns the first element in a list.
int dequeue(int** t, int size) {
    int* new = (int*)malloc((size - 1) * sizeof(int));
    int last = (int)t[0][size-1];

    for(int i = 0; i < size-1; i++) {
        new[i] = t[0][i];
    }
    
    free(*t);
    *t = new;
    return last;
}

// Add x into queue.
void enqueue(int** t, int size, int x){
    int* new = (int*)malloc((size + 1) * sizeof(int));

    for(int i = 0; i < size; i++) {
        new[i+1] = (*t)[i];
    }
    new[0] = x;

    free(*t);
    *t = new;
}

int main()
{
    srand(time(NULL));
    
    int size = 10;
    int* t = (int*)malloc(size * sizeof(int));;
    printf("%d\n", sizeof(&t));
    for(int i = 0; i < size; i++)
    {
        t[i] = rand() % 100;
    }
    for(int i = 0; i < size; i++)
    {
        printf("%d ", t[i]);
    }

    printf("\nenqueue 10\n");
    enqueue(&t, size, 10);
    size++;
    for(int i = 0; i < size; i++)
    {
        printf("%d ", t[i]);
    }

    int removed = dequeue(&t, size);
    size--;
    printf("\ndequeue %d\n", removed);
    for(int i = 0; i < size; i++)
    {
        printf("%d ", t[i]);
    }

    printf("\nFront is: %d", front(&t, size));

    printf("\nNew list with zero elements\n");
    int* r = (int*)malloc(0 * sizeof(int));;
    printf("%d", isEmpty(&r, 0));

    free(t);
}