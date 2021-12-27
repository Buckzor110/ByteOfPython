def outer_func():
    x=2
    def inner_func():
        nonlocal x
        x*=7
    inner_func()
    print(x)
outer_func()
