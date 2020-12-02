msg = "hello world"
print(msg)

testList = [1, 21, 18, 40, 45]
print(testList)
print(testList[2:4])


def isGreaterThan19( inputlist ):

    for num in inputlist:

        if ( num > 19 ):
            print("value is greater than 19")
        else:
            print("value is less than 19")


isGreaterThan19(testList)


def fizzBuzz(num):

    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Fizz'
    elif num % 3 == 0:
        return 'Buzz'


print(fizzBuzz(15))
print(fizzBuzz(5))
print(fizzBuzz(3))

teststring = 'abcdef'

def reverse(string):
    return string[::-1]
        

print(reverse(teststring))

class literallyAPotato():
    name = str('potato')

    
simon = literallyAPotato()

print('simon is a', simon.name)