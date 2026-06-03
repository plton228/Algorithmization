class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Помилка: Спроба вилучення елемента з порожнього стеку!")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Стек (дно -> вершина): {self.items}"

def main():
    print("--- Завдання 7: Структура даних Стек (LIFO) ---")
    
    stack = Stack()
    print(f"Ініціалізовано новий стек. Чи порожній він? {stack.is_empty()}")
    print(stack)
    print("-" * 50)
    
    elements_to_push = [10, 20, 30, 40]
    print(f"Послідовно додаємо елементи: {elements_to_push}")
    for elem in elements_to_push:
        stack.push(elem)
        print(f"Додано: {elem} | {stack}")
        
    print("-" * 50)
    
    top_element = stack.peek()
    print(f"Перегляд вершини стеку (peek): {top_element}")
    print(stack)
    
    print("-" * 50)
    
    print("Вилучаємо елементи зі стеку:")
    while not stack.is_empty():
        removed = stack.pop()
        print(f"Вилучено: {removed} | {stack}")
        
    print("-" * 50)
    
    print("Спроба вилучити елемент з уже порожнього стеку:")
    stack.pop()
    print(stack)

if __name__ == "__main__":
    main()
