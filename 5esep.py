
def compose(f, g):
    def h(x):
        return f(g(x))
    return h
def f(x):
    return x**2
def g(x):
    return x + 2
h = compose(f, g)
print(h(2))