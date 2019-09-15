#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int getNumVerticies(FILE *graph){
    if(graph != NULL){
        char line[512];
        int verticies = 0;
        while(fgets(line, sizeof(line), graph) != NULL){
            verticies = (int) line;
            //printf(verticies);
            break;
        }
        fclose(graph);
        return verticies;
    }
}
/*int getMatrix(FILE *graph, int size){
    int matrix[size][size];
    int i,j;
    char line[512];
    char row;
    while(fgets(line, sizeof(line), graph) != NULL){
        row = line;
        printf(row);
        break;
    }

}*/
int main() {
    FILE *graph = fopen("C:\\Users\\krish\\Downloads\\Dijkstra_Data_6.txt","r");
    int points = getNumVerticies(graph);
    int *graphPoints;
    printf(points);
    graphPoints = memset(*graphPoints, 0, points*points* sizeof(int));
    //printf(graphPoints);
}