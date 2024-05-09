#include <string.h>
#include <stdio.h>

void reverse(char* word, size_t word_len, char* res){
    for(int i = word_len, j = 0; i >= 0; j++, i--){
        res[j] = word[i - 1];
    }
}

int main(){
    char* word = "Hello World!";
    int size_of_word = strlen(word);
    char reversed_word[size_of_word];

    reverse(word, size_of_word, reversed_word);

    printf("%s\n", reversed_word);

}