# Linear Regression
Model
$$
f_{w,b}(x) = wx + b
$$
Parameters: w, b

**Cost function**
$$
J(w, b) = \frac {1} {2m} \sum _{i=1} ^m (\hat y_i - y_i) ^2 = \frac {1} {2m} \sum _{i=1} ^m (f_{w,b}(x) - y_i)^2
$$
Objective: Minimize J(w,b)

**Gradient desent**
$$
w = w - \alpha \frac {\partial} {\partial w} J(w, b) \\
w = w - \alpha \frac {1} {m} \sum _{i=1} ^m (f_{w,b}(x_i) - y_i)x_i
$$
$\alpha$ is learning rate.



## Multiple Linear Regression

Multiple features:

Model:
$$
f _{x,b} (x) = w_1x_1 + w_2x_2 + w_3x_3 + b \\
f _{\vec{w},b} (\vec x) = \vec w \vec x + b
$$


# Logistic Regression

sigmoid function
$$
g(z) = \frac {1} {1+e^{-z}}， 0 < g(z) < 1
$$

$$
z = f_{\vec w, b}(\vec x) = \vec w \cdot \vec x + b \\
f_{\vec w, b}(\vec x) = g(\vec w \cdot \vec x + b) = \frac {1} {1 + e^{-(\vec w \cdot \vec x + b)}}
$$

Interpretation of logistic regression output, the probability that class is 1

$$
f_{\vec w,b}(\vec x) = P(y = 1 | \vec x; \vec w, b) \\
P(y = 0)+P(y = 1) = 1
$$
