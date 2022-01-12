#Basic - Print all integers from 0 to 150.
for x in range(0,150):
    print(x)
    print ("End #Basic")

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(0,1000,5):
    print(x)
    print("End #Multiples of 5")

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,100):
    if x % 10 == 0:
        print("Coding Dojo")

    elif x % 5 == 0:
        print("Coding")

    else:
        print(x)

print("End #Counting the Dojo Way")

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(0,500000):
    
    if x % 2 != 0:
        sum = sum + x

print (sum)
print("End #Whoa. That Sucker's Huge")

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range (2018,0,-4):
    print(x)
    
print ("End #Countdown by Fours")

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flex_counter(low, high, mul):
    lowNum = low
    highNum = high
    mult = mul
    for x in range(lowNum, highNum):
        if x % mult == 0:
            print(x)
    print("end of counter")

flex_counter(0,10,4)
flex_counter(-10,10,3)
