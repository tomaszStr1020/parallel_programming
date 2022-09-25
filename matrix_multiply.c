#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#include <malloc.h>

int main(int argc, char* argv[]){
    FILE *out_file = fopen("matrix_12.txt", "w"); // write only 
     if ( out_file == NULL) 
            {   
              printf("Error! Could not open file\n"); 
              exit(-1); // must include stdlib.h 
            } 
    fprintf(out_file, "Results in form: numbers;time"); 

    clock_t start, stop, whole_start, whole_stop;
    int n = 16;
    int i,j,k;
    int ** A = NULL;
    int ** B = NULL;
    int ** C = NULL;
    
    
    
    
    int threadsnumber = 12;
    omp_set_num_threads(threadsnumber);
    for(n=16; n<2100; n = n*2){

    
    A = (int **) malloc(n*sizeof(int *)); 
    B = (int **) malloc(n*sizeof(int *)); 
    C = (int **) malloc(n*sizeof(int *)); 

    for (i=0;i<n;i++)
    {
        A[i]=(int *) malloc(n*sizeof(int));
        B[i]=(int *) malloc(n*sizeof(int));
        C[i]=(int *) malloc(n*sizeof(int));
    } 

    for (i=0;i<n;i++){
        for(j=0; j<n; j++){
            A[i][j] = 2;
            B[i][j] = 2;
        }
    }

        start = clock();
        #pragma omp parallel for private (i,j,k)schedule (static,  n/threadsnumber) shared(A,B,C, threadsnumber)
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
            int sum=0;
            for (int i = 0; i < n; i++)
            {
                sum = sum + A[i][k] * B[k][j];
            }
            C[i][j]=sum;
            }
        }
            stop = clock();
            float time = (double)(stop - start)/10000000.0;
            printf("\nTime of calculations %f on %d instance", time, n);
            fprintf(out_file, "\n%d;%f", n, time); 
    }
    return EXIT_SUCCESS;
}