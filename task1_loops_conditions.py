def main():
    print("--- Завдання 1: Парні числа та їх сума від 1 до N ---")
    try:
        n = int(input("Введіть натуральне число N (N >= 1): "))
        if n < 1:
            print("Помилка: Число повинно бути натуральним (N >= 1)!")
            return
    except ValueError:
        print("Помилка: Введено не коректне число!")
        return

    even_numbers = []
    total_sum = 0
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
            total_sum += i

    print(f"Парні числа в діапазоні від 1 до {n}: {', '.join(map(str, even_numbers)) if even_numbers else 'відсутні'}")
    print(f"Сума парних чисел: {total_sum}")

if __name__ == "__main__":
    main()
