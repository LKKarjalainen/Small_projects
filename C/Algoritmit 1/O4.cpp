#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(int list[], int length){
    int swapped = 1;
    while(swapped){
        swapped = 0;
        for(int i = 0; i < length; i++){
            if(list[i-1]>list[i]){
                int helper = list[i-1];
                list[i-1] = list[i];
                list[i] = helper;
                swapped = 1;
            }
        }
    }
}

void selectionSort(int list[], int length){
    for(int i = 0; i < length-1; i++){
        int p = list[i];
        int k = i;
        for(int j = i+1; j < length; j++){
            if(list[j] < p){
                p = list[j];
                k = j;
            }
        }
        if(k != i){
            list[k] = list[i];
            list[i] = p;
        }
    }
}

int main() {
    // List of randomly chosen integers using rand.
    int list[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int length = sizeof(list)/sizeof(list[0]);
    srand(time(NULL));
    for(int i = 0; i < length; i++)
    {
        list[i] = rand() % 100;
    }
    for(int i = 0; i < length; i++)
    {
        printf("%d ", list[i]);
    }
    printf("\n");
    bubbleSort(list, length);
    for(int i = 0; i < length; i++)
    {
        printf("%d ", list[i]);
    }
    for(int i = 0; i < length; i++)
    {
        list[i] = rand() % 100;
    }
    printf("\n");
    for(int i = 0; i < length; i++)
    {
        printf("%d ", list[i]);
    }
    printf("\n");
    selectionSort(list, length);
    for(int i = 0; i < length; i++)
    {
        printf("%d ", list[i]);
    }
}