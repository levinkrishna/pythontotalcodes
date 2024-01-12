def dec_square(fn):
    def wrapper(n1,n2):
        return fn(n1**2,n2**2)
    return wrapper


@dec_square
def add(n1,n2):
    return n1+n2

@dec_square
def product(n1,n2):
    return n1*n2

print(add(2,3))
print(product(2,3))