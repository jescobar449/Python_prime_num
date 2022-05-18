#Name: Jose Melquiades Escobar

#Declare local variables under main() program
def main(): 
    #make magic numbers into named constants 
    lowRange = 1
    highRange = 11
    


#Write for loop, use range function to loop through the total numbers.
    print ('number \t is prime')
    print ('------------------------')
    for num in range (lowRange, highRange):
        primeTest = isPrime(num)       #Call is_prime function 
        if primeTest == True:
            print (num,'\t prime')      #print if the number is prime
        elif primeTest == False:
            print (num,'\t not prime')  #print if the number is not prime
                

#Define isPrime function, 'def is_prime(number):'
def isPrime(number):
    possiblePrime  = (number - 1) * (number - 2)    #check if values below the given number can be multiplied to equal the given numbers
    if ((possiblePrime > number) and (number % 2 == 0 or number % 3 == 0)) or (number == 1):      #check for divisible by 2 or 3 or if number is 1
        return False        #the number is not prime
    else:
        return True         #the number is prime
    

main ()
