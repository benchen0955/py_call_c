#include<stdio.h>

void my_add(int num){

    long int result = 0;
    for (long int i=1; i<=num; i++){
        result += i;
    }
	printf("从1到%d累加的计算结果为%ld\n",num,result);
}
// void print_str(char *s){

//     printf("str=>%s\n",s);
// }

// int main(){
//     print_str("abc");
//     return 0;
// }

