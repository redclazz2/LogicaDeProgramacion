def indeterminados_posicion(*args):
    for arg in args:
        print(arg)


indeterminados_posicion(5, "hola plone", [1, 2, 3, 4, 5])


def super_funcion(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    print("Sumatorio", total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])


super_funcion(50, -1, 1.56, 10, 20, 300, cms="Plone", edad=38)
