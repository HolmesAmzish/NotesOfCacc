# 安装与基本设置

## 设置字体

```python
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```



```python
import matplotlib
print(matplotlib.matplotlib_fname())
```

```ini
# 设置字体
font.family: sans-serif
font.sans-serif: SimHei  # 使用黑体（可换成其他支持中文的字体）

axes.unicode_minus: False
```



# Plotting

## Default X-Points

If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
```



# Markers

## Format Strings `fmt`

You can also use the *shortcut string notation* parameter to specify the marker.

This parameter is also called `fmt`, and is written with this syntax:

```
*marker*|*line*|*color*
```

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()
```



# Line

## Linestyle

You can use the keyword argument `linestyle`, or shorter `ls`, to change the style of the plotted line:

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()
```

## Multiple Lines

```python
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
```



# Labels and Title

## Create Labels and Title

You can use the `xlabel()` and `ylabel()` functions to set a label for the x- and y-axis. use the `title()` function to set a title for the plot.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

# Set the title
plt.title("Sports Watch Data")

# Set labels for x and y axis
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
```

## Font Properties

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()
```

## Position

```python
plt.title("Sports Watch Data", loc = 'left')
```



# Grid

## Add Grid Lines

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

# Add the Grid to the plot
plt.grid()

plt.show()
```

## Specify Line

```python
plt.grid(axis = 'x')
```

## Line Properties

```python
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
```

# Function

## Sigmoid function

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 400)

y = sigmoid(x)

plt.plot(x, y)

plt.title("Sigmoid Function")
plt.xlabel("x")
plt.ylabel("sigmoid(x)")

plt.grid(True)

plt.show()
```

## sine function

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6 * np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.title("Sine Function")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
```

## Poisson distribution

```python
"""
plot picture of poisson distribution
and long tail distribution
author: cacc
date: 2024-12-13
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

np.random.seed(0)

# --------- Poisson distribution ---------
lambda_poisson = np.array([1, 4, 10])  # λ values
x_poisson = np.arange(0, 30)  # x-axis values for Poisson

# --------- Long tail distribution ---------
alpha = 2.5
x_power_law = np.linspace(1, 50, 1000)  # x values for Power-law
y_power_law = x_power_law ** (-alpha)  # Power-law distribution

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot Poisson distribution for different lambda values
for lambda_val in lambda_poisson:
    y_poisson = poisson.pmf(x_poisson, lambda_val)
    ax[0].plot(x_poisson, y_poisson, label=f'λ={lambda_val}')

ax[0].set_title('Poisson Distribution')
ax[0].set_xlabel('x')
ax[0].set_ylabel('P(X=x)')
ax[0].legend(title="λ Values")

# Plot Power-law distribution
ax[1].plot(x_power_law, y_power_law, color='red', label=f'Power Law (α={alpha})')
ax[1].set_title('Power Law Distribution')
ax[1].set_xlabel('x')
ax[1].set_ylabel('P(X=x)')
ax[1].set_ylim(0, max(y_power_law)*1.1)

# Show the plot
plt.tight_layout()
plt.show()
```

