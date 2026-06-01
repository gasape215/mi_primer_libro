# Higher Degree Equations

## What are higher degree equations?

In previous chapters, you studied quadratic equations, which have the general form:

$$ax^2 + bx + c = 0$$

**Higher degree equations** are polynomials of degree 3 or greater. Remember that the **degree** of a polynomial is the highest exponent of the variable.

The most common general forms are:

- **Degree 3 (cubic equations):** $ax^3 + bx^2 + cx + d = 0$
- **Degree 4 (quartic equations):** $ax^4 + bx^3 + cx^2 + dx + e = 0$
- **Degree 5 (quintic equations):** $ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0$

## Solving degree 3 and 4 equations

### Cubic equations

For degree 3 equations, **there is a closed formula** that allows you to calculate the exact roots. It is much more complicated than the formula for quadratic equations, but it exists.

**Cardano's formula** (16th century) allows you to find the exact solutions of any cubic equation. However, it is so complicated that in practice it is rare to use it by hand:

```{admonition} Historical curiosity
:class: tip
Cardano's formula was a revolutionary discovery during the Italian Renaissance. Although mathematicians like Tartaglia and Cardano developed these methods, the formula remains difficult to apply without computational help.
```

### Quartic equations

For degree 4 equations, there is also **a closed formula** (Ferrari's formula, also from the 16th century). As with cubics, it is very complicated, but it exists.

```{admonition} Practical methods
:class: note
Instead of using closed formulas for degrees 3 and 4, modern mathematicians and engineers usually:
- Factor if possible
- Use iterative numerical methods (Newton-Raphson, bisection, etc.)
- Use computational tools like Python, MATLAB, or Mathematica
```

## The jump: degree 5 and beyond

### The Abel-Ruffini theorem

Here comes a **surprising and fundamental result**: for degree 5 or higher equations, **there is no closed formula** that uses only arithmetic operations and roots.

This result, proved in the early 19th century by **Paolo Ruffini** and **Niels Henrik Abel**, is known as the **Abel-Ruffini Theorem** or **Impossibility Theorem**.

```{admonition} Abel-Ruffini Theorem
:class: important
For polynomial equations of degree 5 or higher, **there is no closed formula** that expresses the solutions only by means of addition, subtraction, multiplication, division, and taking nth roots of the coefficients.
```

### What does this mean?

Although we know that every polynomial equation of degree $n$ has exactly $n$ roots (including complex ones), **we cannot write a general formula** that gives us all of them.

This does not mean that the roots do not exist or that we cannot find them. It only means that we cannot express them using a "formula" as we do with second degree equations.

### Conceptual example

For a cubic equation like $x^3 - 2 = 0$, the solution is $x = \sqrt[3]{2}$ (the real cube root of 2). We can express this solution exactly.

But for a degree 5 equation like $x^5 + x + 1 = 0$, **there is no way to write the exact solution** in terms of addition, subtraction, multiplication, division, and roots.

## How do we find solutions then?

Although there is no closed formula, we have **alternative methods**:

### 1. Numerical methods

We use iterative algorithms that approximate solutions to any desired precision:

- **Newton-Raphson method**: starting from an initial approximation, it iteratively improves the solution
- **Bisection method**: divides the interval containing the root in half, repeating until it finds it
- **Modern methods**: sophisticated algorithms implemented in Python, MATLAB, etc.

```{code-block} python
import numpy as np
from scipy.optimize import fsolve

# Find roots of x^5 + x + 1 = 0
def f(x):
    return x**5 + x + 1

# Initial approximation
x0 = -1.0

# Solve
solution = fsolve(f, x0)
print(f"Approximate solution: {solution[0]:.6f}")
```

### 2. Special algebraic methods

For certain degree 5 or higher equations with special structure, sometimes ingenious algebraic techniques can be used to find the roots.

### 3. Graphical methods

Drawing the function and seeing where it crosses the $x$-axis is a visual way to approximate solutions.

## Summary

| Degree | Is there a closed formula? | How to solve? |
|---|---|---|
| 1 | ✅ Yes | Simple algebra |
| 2 | ✅ Yes (Bhaskara) | Quadratic formula |
| 3 | ✅ Yes (Cardano) | Cardano's formula or numerical methods |
| 4 | ✅ Yes (Ferrari) | Ferrari's formula or numerical methods |
| 5+ | ❌ No (Abel-Ruffini) | Numerical methods or special algebraic techniques |

## Final reflection

The discovery that there is no closed formula for degree 5 and higher was a **humbling lesson** for mathematics. It showed that not all natural questions have answers in the form we expect.

However, this "does not exist" led to the development of:
- **Advanced numerical methods** that work for any polynomial
- **Galois theory**, a profound branch of mathematics that studies why certain polynomials do not have solutions with radicals
- **Computational tools** that can solve practically any equation to the precision we need

In modern practice, we rarely need to memorize formulas. We use **software to solve equations of any degree**, but it is important to understand why that is necessary.
