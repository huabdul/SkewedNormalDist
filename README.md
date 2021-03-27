# Skewed Normal Distribution Based on Mode

A python class for calculating the probability density function of a [skewed normal distribution](https://en.wikipedia.org/wiki/Skew_normal_distribution) given its **mode** (i.e. location of the peak), standard deviation, and alpha (skewness parameter).

This allows defining a skewed normal distribution based on **its maximum value at the specified point (mode)**, instead of the standard way to define it based on the mean (which does not correspond with the maximum point for alpha != 0).

Example:

```Python
snd = SkewedNormalDist(mode=2, std=1, alpha=3)
x = np.arange(-3, 7, 0.1)
y = snd.pdf(x)
plt.plot(x,y)
plt.grid()
```

![image](https://user-images.githubusercontent.com/41363258/112726061-1ba00a80-8f24-11eb-9513-01c7bfa841e8.png)
