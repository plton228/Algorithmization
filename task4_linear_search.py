def linear_search(arr, target):
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx
    return -1

def run_demo():
    print("--- Демонстрація роботи лінійного пошуку ---")
    demo_list = [10, 25, 3, 47, 8, 19, 4]
    print(f"Початковий список для демонстрації: {demo_list}")
    
    target_found = 8
    index_found = linear_search(demo_list, target_found)
    print(f"\nШукаємо число: {target_found}")
    if index_found != -1:
        print(f"Результат: Число {target_found} знайдено на позиції (індексі): {index_found}")
    else:
        print(f"Результат: Число {target_found} відсутнє у списку")
        
    target_not_found = 99
    index_not_found = linear_search(demo_list, target_not_found)
    print(f"\nШукаємо число: {target_not_found}")
    if index_not_found != -1:
        print(f"Результат: Число {target_not_found} знайдено на позиції (індексі): {index_not_found}")
    else:
        print(f"Результат: Число {target_not_found} відсутнє у списку")
    print("-" * 45)

def main():
    run_demo()
    
    print("Бажаєте спробувати самостійно?")
    try:
        user_input = input("Введіть список чисел через пробіл (або натисніть Enter для пропуску): ").strip()
        if not user_input:
            print("Інтерактивний режим пропущено.")
            return
            
        arr = list(map(int, user_input.split()))
        target = int(input("Введіть число, яке потрібно знайти: "))
        
        print(f"Список: {arr}")
        print(f"Шукане число: {target}")
        
        index = linear_search(arr, target)
        if index != -1:
            print(f"Результат: Число {target} знайдено на індексі {index}.")
        else:
            print(f"Результат: Число {target} відсутнє в списку.")
    except ValueError:
        print("Помилка: Некоректні вхідні дані! Будь ласка, вводьте лише цілі числа.")

if __name__ == "__main__":
    main()
