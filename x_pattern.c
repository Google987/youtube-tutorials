#include <stdio.h>

int main()
{
    int i, j, n;
    printf("Enter Number of Rows: ");
    scanf("%d",&n);
    for(i = 1; i <= n; i++)
    {
        for(j = 1 ;j <=n; j++)
        {
            if(j == i || (j+i) == n+1)
                printf("*");
                else printf(" ");
        }
        printf("\n");
    }
}
