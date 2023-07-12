# task 1
if __name__ == "__main__":
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    start = int(input("Введіть початкове число діапазону: "))
    end = int(input("Введіть кінцеве число діапазону: "))

    print("Прості числа у заданому діапазоні:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)


# task 2

    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            print(f"{i} * {j} = {result}")


# task 3


    a = int(input("Введіть значення початку діапазону"))
    b = int(input("Введіть значення кінця діапазону"))
    for i in range(a, b+1):
        for j in range(1, b+1):
            result = i * j
            print(f"{i} * {j} = {result}")




