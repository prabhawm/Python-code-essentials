def fun():
    print('fun is running')

def sayHi(a):
    if isinstance(a,str):
        print("Hi", a)

fun()
print(fun())
for x in ['Raj','Ravi','Sam','Lara']:
    sayHi(x)