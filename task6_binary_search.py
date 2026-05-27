def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def run_demo():
    print("--- Демонстрація роботи бінарного пошуку ---")
    sorted_list = [3, 8, 12, 19, 25, 34, 47, 64, 90]
    print(f"Відсортований список для демонстрації: {sorted_list}")
    
    target_found = 25
    index_found = binary_search(sorted_list, target_found)
    print(f"\nШукаємо число: {target_found}")
    if index_found != -1:
        print(f"Результат: Число {target_found} знайдено на індексі: {index_found}")
    else:
        print(f"Результат: Число {target_found} відсутнє у списку")
        
    target_not_found = 50
    index_not_found = binary_search(sorted_list, target_not_found)
    print(f"\nШукаємо число: {target_not_found}")
    if index_not_found != -1:
        print(f"Результат: Число {target_not_found} знайдено на індексі: {index_not_found}")
    else:
        print(f"Результат: Число {target_not_found} відсутнє у списку")
    print("-" * 50)

def main():
    run_demo()
    
    print("Бажаєте спробувати самостійно?")
    try:
        user_input = input("Введіть список чисел через пробіл (вони будуть автоматично відсортовані): ").strip()
        if not user_input:
            print("Інтерактивний режим пропущено.")
            return
            
        arr = list(map(int, user_input.split()))
        arr.sort()
        print(f"Відсортований вхідний список: {arr}")
        
        target = int(input("Введіть число для пошуку: "))
        index = binary_search(arr, target)
        if index != -1:
            print(f"Результат: Число {target} знайдено на індексі {index}.")
        else:
            print(f"Результат: Число {target} відсутнє у списку.")
    except ValueError:
        print("Помилка: Будь ласка, вводьте лише цілі числа.")

if __name__ == "__main__":
    main()
