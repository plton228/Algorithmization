def main():
    print("--- Завдання 3: Пошук мінімуму, максимуму та середнього у списку ---")
    try:
        n = int(input("Введіть кількість чисел N: "))
        if n <= 0:
            print("Помилка: Кількість чисел повинна бути більшою за 0!")
            return
    except ValueError:
        print("Помилка: Введено не коректне число!")
        return
        
    numbers = []
    for i in range(n):
        while True:
            try:
                num = int(input(f"Введіть число {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Помилка: Введіть ціле число!")
                
    print(f"Створений список чисел: {numbers}")
    
    min_val = numbers[0]
    max_val = numbers[0]
    total_sum = 0
    
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        total_sum += num
        
    average = total_sum / n
    
    print(f"Найменший елемент: {min_val}")
    print(f"Найбільший елемент: {max_val}")
    print(f"Середнє арифметичне: {average:.2f}")

if __name__ == "__main__":
    main()
