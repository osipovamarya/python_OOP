from datetime import datetime

# находит разницу во времени между двумя соседними вызовами переменной в которой записана функция inner


def timer():
    previous = datetime.now()
    print('init', previous)

    def inner():
        nonlocal previous
        print('delta ', datetime.now() - previous)
        print('iter ', previous)
        print('now ', datetime.now())
        previous = datetime.now()
    return inner


a = timer()

a()



