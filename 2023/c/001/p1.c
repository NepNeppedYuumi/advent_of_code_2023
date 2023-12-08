#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


int main () {
    FILE * file;

    file = fopen ("input.txt", "r");

    char line[100];
    int i;

    char first_digit;
    char last_digit;

    int total = 0;
    int current;

    while(fgets(line, 100, file)) {
        first_digit = 'a';
        last_digit = 'a';
        for (i = 0; line[i] != '\0'; i++) {
            // printf("%c\n", line[i]);
            if (isdigit(line[i])) {
                if (first_digit == 'a'){
                    first_digit = line[i];
                }
                last_digit = line[i];
            }
        }
        char cal[3] = {first_digit, last_digit, '\0'};
        current = atoi(cal);
        total = total + current;
    }
    printf("\n%d\n", total);

    fclose(file);
   
    return(0);
}