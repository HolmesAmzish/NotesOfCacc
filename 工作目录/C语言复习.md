# C 语言概述

## 2.1 简单的 C 程序示例

```c
#include <stdio.h>
int main(void) {
    int num;
    num = 1;
    
    printf("I am a simple ");
    printf("computer.\n");
    printf("My favorite number is %d because it is first.\n", num);
    
    return 0;
}
```

# 数据和 C

## 3.1 示例程序

```c
/* platinum.c -- your weight in platinum */
#include <stdio.h>
int main(void) {
    float weight;
    float value;
    
    printf("Are you worth your weight in platinum?\n");
    printf("Let's check it out.\n");
    printf("Please enter your weight in pounds: ");
    
    scanf("%f", &weight);
    
    value = 1700.0 * weight * 14.5833;
    printf("Your weight in platinum is worth $%.2f.\n", value);
    
    return 0;
}
```

