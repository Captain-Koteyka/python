def fibo_gen(number):
    idx = 1
    result = 1
    if number <= 15:
        while idx <= number:
            result *= idx
            yield result
            idx += 1
    else:
        while idx <= 15:
            result *= idx
            yield result
            idx += 1
        while idx <= number:
            result *= idx
            idx += 1
        yield result


for el in fibo_gen(20):
    print(el)
