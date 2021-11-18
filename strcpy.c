#include <stdio.h>

void so_strcpy(char str1[], char str2[]){
    for (int i = 0; i < sizeof(str1); i++){
        str2[i] = str1[i];
    }
}

int main()
{
    char string[] = "cadena 1";
    char string2[sizeof(string)];
    so_strcpy(string, string2);
    printf("El string2 es %s", string2);
    return 0;
}
