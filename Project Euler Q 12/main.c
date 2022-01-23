#include <stdio.h>
#include <math.h>

int main(){
  int triNum = 0;

  for(int i = 1; ; i++){
    int divisorCount = 0;
    triNum += i;
    printf("%d : ", triNum);

    for(int d = 1; d <= sqrt(triNum); d++){
      if(triNum % d == 0){
        divisorCount++;
        // printf("%d ", d);
        if(triNum/d != d){
        //   printf("%d ", triNum/d);
          divisorCount++;
        }
      }
    }
    printf(", divisorCount: %d \n", divisorCount);
    if(divisorCount > 500){
        printf("Ans: %d", triNum); // 76576500
        exit(0);
    }
  }

  return 0;
}