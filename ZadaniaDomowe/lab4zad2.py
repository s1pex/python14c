def prime(*numbers):
    for num in numbers:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
            break
        if is_prime:
            print(f"{num} is prime")
        else:
            print(f"{num} is not prime")

prime(1,2,3,4,5,6,11)
