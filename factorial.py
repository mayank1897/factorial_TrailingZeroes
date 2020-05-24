def factorial(number):
    if (number==0 or number==1):
        return 1
    return (number*factorial(number-1))
    
def trailing_zeroes(number):
    i=5
    c=0
    while((number//i)!=0):
        c+=int(number//i)
        i*=5
    return c

if __name__ == "__main__":
    n=int(input("enter a number= "))
    print(f"Factorial= {factorial(n)}")
    print(f"Number of trailing zeroes= {trailing_zeroes(n)}")    