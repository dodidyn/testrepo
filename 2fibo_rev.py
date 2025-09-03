# Euler project 2
# The sum of the even-valued  of Fibonacci sequence below 4000000
 
def fibonacci():

 
    fibo = [1, 2]
 
   
    index = 0

    fibo_even = []
        
    while fibo[index+1] < 4000000:


        fibo.append(fibo[index] + fibo[index+1])

        index = index + 1

        if fibo[index] % 2 == 0:

            fibo_even.append(fibo[index])
        
                      
       
     
    print(fibo)
            
    print(fibo_even)

    print(sum(fibo_even))


fibonacci()
