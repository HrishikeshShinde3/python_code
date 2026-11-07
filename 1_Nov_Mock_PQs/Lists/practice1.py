
def my_generator():

    yield 10
    yield 20
    yield 30

result = my_generator()
print(next(result))


import struct

print(struct.calcsize("P") * 8, "bit")

#ChooseYourOwnPassword