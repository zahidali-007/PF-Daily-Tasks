def isprime(num):
    #define a flag variable 
    flag = False

    if num <=1:
        print(num,"is not a prime number",-1)
    
    elif num > 1 :
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
        # check if flag is True
        if flag:
            print(-1)
        else:            
            sum = 0
            for i in range(num + 1):
                sum = sum + i
            print(num,"is a prime number and the sum of 0 to the given num : ",sum)

isprime(7)

