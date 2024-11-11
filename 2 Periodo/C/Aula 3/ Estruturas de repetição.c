/*
#include <stdio.h>

int main(){

    int x,t;

    scanf("%d", &x);
    t = x % 2;

    if (t == 0) {
        printf("par");
    } else {
        printf("impar");
    }


    return 0;
}

*/

/*
#include <stdio.h>

int main(){

    int x,y;

    scanf("%d", &x);
    scanf("%d", &y);

    if (x == y) {
        printf("IGUAIS");
    } else {
        printf("DIFERENTES");
    }

    return 0;
}
*/

/*
#include <stdio.h>

int main(){

    int n,m;

    scanf("%d", &n);

    if (n%2 == 0) {
        m = n*n;
    } else {
        m = n*n*n;
    }

    printf("%d", m);

    return 0;
}
*/

/*
#include <stdio.h>

int main(){

    int m,n;

    scanf("%d", &m);
    
    if (m < 0){
        n = -1;
    } else if (m == 0) {
        n = 0;
    } else {
        n = 1;
    }

    printf("%d", n);

    return 0;
}
*/

#include <stdio.h>
#include <ctype.h>

int main() {
    char c;

    // Lê o caractere de entrada
    scanf("%c", &c);

    // Converte o caractere para minúsculo para facilitar a comparação
    c = tolower(c);

    // Verifica se o caractere é uma letra
    if (isalpha(c)) {
        // Verifica se é uma vogal
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            printf("VOGAL\n");
        } else {
            printf("CONSOANTE\n");
        }
    } else {
        // Se não for uma letra, é considerado "NA"
        printf("NA\n");
    }

    return 0;
}
