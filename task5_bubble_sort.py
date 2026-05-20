def bubble_sort(arr):
    sorted_arr = list(arr)
    n = len(sorted_arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break
    return sorted_arr

def run_demo():
    print("--- Демонстрація роботи бульбашкового сортування ---")
    demo_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Список до сортування : {demo_list}")
    
    sorted_list = bubble_sort(demo_list)
    print(f"Список після сортування: {sorted_list}")
    print("-" * 52)

def main():
    run_demo()
    
    print("Бажаєте спробувати самостійно?")
    try:
        user_input = input("Введіть список чисел через пробіл (або натисніть Enter для пропуску): ").strip()
        if not user_input:
            print("Інтерактивний режим пропущено.")
            return
            
        arr = list(map(int, user_input.split()))
        print(f"Введений список до сортування: {arr}")
        sorted_arr = bubble_sort(arr)
        print(f"Відсортований список: {sorted_arr}")
    except ValueError:
        print("Помилка: Будь ласка, вводьте лише цілі числа, розділені пробілами.")

if __name__ == "__main__":
    main()
