# Introducing C

## A Simple Example of C

The `first.c` Program

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

# Data and C

## A Sample Program

The `platinum.c` Program

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

# Character Strings and Formatted Input/Output

## Introductory Program

The `talkback.c` Program

```c
// talkback.c -- nosy, informative program
#include <stdio.h>
#include <string.h>
#define DENSITY 62.4
int main() {
    float weight, volume;
    int size, letters;
    char name[40];
    
    printf("Hi! What's your first name?\n");
    scanf("%s", name);
    
    printf("%s, what's your weight in pounds?\n", name);
    scanf("%f", &weight);
    
    
    size = sizeof name;
    letters = strlen(name);
    volume = weight / DENSITY;
    printf("Well, %s, your volume is %2.2f cubic feet.\n", name, volume);
    printf("Also, your first name has %d letters,\n", letters);
    printf("and we have %d bytes to store it.\n", size);
    
    return 0
}
```

# Arrays and Pointers

## Array

The `day_mo1.c` Program

```c
/* day_mon1.c -- prints the days for each month */
#include <stdio.h>
#define MONTHS 12
int main(void) {
    int days[MONTHS] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int index;
    for (index = 0; index < MONTHS; index++)
        printf("Month %d has %2d days.\n", index +1, days[index]);
    return 0;
}
```



# Storage Classes, Linkage, and Memory Management

## Storage Classes

```c
// hiding.c -- variables in blocks
#include <stdio.h>
int main() 
{
    int x = 30; // original x
    printf("x in outer block: %d at %p\n", x, &x);
 	{
        int x = 77; // new x, hides first x
        printf("x in inner block: %d at %p\n", x, &x);
    }
    
    printf("x in outer block: %d at %p\n", x, &x);
    while (x++ < 33) // original x
    {
        int x = 100; // new x, hides first x
        x++;
        printf("x in while loop: %d at %p\n", x, &x);
    }
    
    printf("x in outer block: %d at %p\n", x, &x);  
    return 0;
}
```

