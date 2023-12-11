#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>


int main () {
    FILE * file;

    file = fopen ("test.txt", "r");

    char line[100];
    int i, j, k;

    char first_digit;
    char last_digit;

    int total = 0;
    int current;

    bool same;
    char *numbers[9] = {
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    };
    int* str_current;

    while(fgets(line, 100, file)) {
        first_digit = 'a';
        last_digit = 'a';
        printf("%s", line);
        for (i = 0; line[i] != '\n'; i++) {
            // printf("%c\n", line[i]);
            if (isdigit(line[i])) {
                if (first_digit == 'a'){
                    first_digit = line[i];
                }
                last_digit = line[i];
            } else {
                for (j = 0; j < 9; j++) {
                    str_current = numbers[j];
                    // printf("%s\n", numbers[j]);
                    // printf("%d\n", strlen(str_current));
                    for (k = 0; k < strlen(str_current); k++) {
                        printf("%c", str_current[k]);
                        printf("%c", line[i+k]);
                        if ((line[i+k] == '\n') || (line[i+k] == str_current[k])) {
                            // || (line[i+k] != str_current[k])
                            break;
                        }
                    }
                    printf("\n%d\n", k);
                    // printf("%d\n", k);
                    // if ((k - 1) == sizeof(numbers[j])) {
                    //     if (first_digit == 'a'){
                    //         first_digit = j;
                    //     }
                    //     last_digit = j;
                    //     break;
                    // }
                    break;
                }
            }
        }
        char cal[3] = {first_digit, last_digit, '\0'};
        current = atoi(cal);
        printf("%d\n", current);
        total = total + current;
    }
    printf("\n%d\n", total);

    fclose(file);
   
    return(0);
}