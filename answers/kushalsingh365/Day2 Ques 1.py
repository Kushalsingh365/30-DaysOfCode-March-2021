while True:
    num = input("Enter a number: ")
    while num.isdigit() == False:
        num = input("Enter a valid number: ")
        
        
    num = int(num)
    
    def isPrime(num):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    return False;
        else:
            return False
        return True
    
    if isPrime(num):
        wee = str(num)[::-1]
        wee = int(wee)
        if isPrime(wee):
            print(num,"and",wee,"is a prime number which means",num,"is a emirp number.")
        else:
             print(num,"is a prime number but not a emirp number.")
    else:
        print(num,"is not a prime number.")
