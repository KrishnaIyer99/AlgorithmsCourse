#include <stdio.h>
int getNumVerticies(FILE *graph){
    if(graph != NULL){
        char line[512];
        int verticies = 0;
        while(fgets(line, sizeof(line), graph) != NULL){
            verticies = line;// the number of points is the number in the first row of the text file
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
    FILE *graph = fopen("Dijkstra_Data_6.txt","r");
    int points = getNumVerticies(graph);
    //int graphPoints[points][points];
    printf(points);
}