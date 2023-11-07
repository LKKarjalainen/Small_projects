#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int montako(int lista[], int pituus, int alaraja, int ylaraja)
{
    int luku = 0;
    for(int i = 0; i < pituus; i++)
    {
        if (lista[i] >= alaraja && lista[i] <= ylaraja)
        {
            luku++;
        }
    }
    return luku;
}

int main()
{
    // List of randomly chosen integers using rand.
    int lista[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int pituus = sizeof(lista)/sizeof(lista[0]);
    srand(time(NULL));
    for(int i = 0; i < pituus; i++)
    {
        lista[i] = rand() % 100;
    }
    for(int i = 0; i < pituus; i++)
    {
        printf("%d ", lista[i]);
    }
    printf("\n%d\n", montako(lista, pituus, 0, 10));
    printf("%d\n", montako(lista, pituus, 50, 100));
    printf("%d", montako(lista, pituus, 67, 75));
}