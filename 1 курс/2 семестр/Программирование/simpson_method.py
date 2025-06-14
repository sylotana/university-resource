def f(x):
    return 32 + 28*x - 9*x**2

def left_rectangle_method(f, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(n):
        xi = a + i*h
        total += f(xi)
    return total * h

def right_rectangle_method(f, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(1, n+1):
        xi = a + i*h
        total += f(xi)
    return total * h

def middle_rectangle_method(f, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(n):
        xi = a + h*(i + 0.5)
        total += f(xi)
    return total * h

def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        xi = a + i*h
        total += f(xi)
    return total * h

def simpson_method(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        xi = a + i*h
        coef = 4 if i % 2 == 1 else 2
        total += coef * f(xi)
    return total * h / 3

if __name__ == "__main__":
    a = 2
    b = 4
    n_values = [10, 50, 100]

    print(f"Вычисление интеграла функции f(x) = 32 + 28x - 9x^2 на интервале [{a}, {b}]")
    print("-" * 70)

    for n in n_values:
        left_res = left_rectangle_method(f, a, b, n)
        right_res = right_rectangle_method(f, a, b, n)
        middle_res = middle_rectangle_method(f, a, b, n)
        trap_res = trapezoid_method(f, a, b, n)
        simp_res = simpson_method(f, a, b, n)

        print(f"n = {n}:")
        print(f"Метод левых прямоугольников: {left_res:.5f}")
        print(f"Метод правых прямоугольников: {right_res:.5f}")
        print(f"Метод средних прямоугольников: {middle_res:.5f}")
        print(f"Метод трапеций: {trap_res:.5f}")
        print(f"Метод Симпсона: {simp_res:.5f}")
        print("-" * 70)