#include <stdio.h>
int main(){
    int a=10;
    int *ptr; 
    ptr=&a;
    printf("%u",&a);
    printf("%u",&ptr);
    return 0;
}