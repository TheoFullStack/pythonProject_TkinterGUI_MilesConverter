def adder(*args):
    total = 0
    for n in args:
        total += n
    print(total)

adder(30,12,25,10,45,50)