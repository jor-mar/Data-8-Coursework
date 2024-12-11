import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
import numpy as np
import math

examples = {
    'x^2': lambda x: x**2,
    'x^3': lambda x: x**3,
    'x': lambda x: x,
    '5x^2': lambda x: 5*x**2,
    '5x' : lambda x: 5*x,
    'e^x' : lambda x: math.exp(x),
    'e^-x' : lambda x: math.exp(-x),
    'e^2x + x^2' : lambda x: math.exp(2*x) + x**2,
    'x^3 + x^2' : lambda x: x**3 + x**2,
    'x^5 + x^2 + 1' : lambda x: x**5 + x**2 + 1
}


def unit_delta_x():
    a = []
    n = 1
    while True:
        next_val = input(F'Please enter the {n}th value [x = {n-1}]: ')
        if next_val.isalpha():
            plot_models(np.arange(1, n), a)
            break
        a.append(float(next_val))
        n += 1


def custom_delta_x():
    x, y = [], []
    while True:
        x_inp = input(F'Please enter the {len(y)+1}th value of x: ')
        if x_inp.isalpha():
            plot_models(x, y)
            break
        x.append(float(x_inp))
        y_inp = input(F'Please enter the {len(y)+1}th value of y [x = {x[-1]}]: ')
        y.append(float(y_inp))


def plot_models(x, y, func = ''):
    plt.scatter(x, y)

    rounding_digits = 5

    slope, intercept, r, p, std_err = stats.linregress(x, y)
    line = lambda val: slope * val + intercept
    model = list(map(line, x))
    equation = f'{round(slope, rounding_digits)}x + {round(intercept, rounding_digits)}'
    plt.plot(x, model, color = 'red', label = f'linear regression {equation}')

    curve = lambda inp, a, exp, b: a*inp**exp+b
    param, param_cov = curve_fit(curve, x, y, p0=[1, 1, 0])
    equation = f'{round(param[0], rounding_digits)}x^{round(param[1], rounding_digits)} + {round(param[2], rounding_digits)}'
    eqn = curve(x, param[0], param[1], param[2])
    plt.plot(x, eqn, color='orange', label=f"simple curve fit {equation}")

    curve = lambda inp,exp1,exp2,a,b,c: a*inp**exp1 + b*inp**exp2 + c
    param, param_cov = curve_fit(curve, x, y, p0 = [1, 1, 1, 1, 0])
    equation = f'{round(param[2], rounding_digits)}x^{round(param[0], rounding_digits)} + {round(param[3], rounding_digits)}x^{round(param[1], rounding_digits)} + {round(param[4], rounding_digits)}'
    eqn = curve(x, param[0], param[1], param[2], param[3], param[4])
    plt.plot(x, eqn, color ='green', label = f"curve fit {equation}")

    plt.legend()
    plt.title(func)
    plt.show()


def main():
    while True:
        word = input("What would you like to do next? [udx, cdx, examples, end]: ").lower()
        if word == 'udx':
            unit_delta_x()
        elif word == 'cdx':
            custom_delta_x()
        elif word == 'examples':
            print(list(examples.keys()))
            ex = input('What example would you like to try? ')
            if ex in examples:
                n = int(input('How many values should be in the training data? '))
                plot_models(np.arange(n), list(map(examples[ex], np.arange(n))), ex)
            elif not ex.isalpha() and int(ex) < len(list(examples.keys())):
                fn = examples[list(examples.keys())[int(ex)]]
                n = int(input('How many values should be in the training data? '))
                plot_models(np.arange(n), list(map(fn, np.arange(n))), list(examples.keys())[int(ex)])
        elif word == 'end':
            break
        print()

if __name__ == '__main__':
    main()