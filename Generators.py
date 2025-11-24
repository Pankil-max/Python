# Genrators store the method on how values are created from iterables but not actual values it generates values on set they give 1 values only when called

def generator():
    for i in range(6):
        yield i;



gen=generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)