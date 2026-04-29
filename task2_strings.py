def main():
    print("--- Завдання 2: Аналіз рядка тексту ---")
    text = input("Введіть рядок тексту: ")
    
    vowels = set("аеєиіїоуюяaeiouy")
    consonants = set("бвгґджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz")
    
    vowel_count = 0
    consonant_count = 0
    
    text_lower = text.lower()
    
    for char in text_lower:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
            
    print(f"Загальна довжина рядка: {len(text)} символів")
    print(f"Кількість голосних літер: {vowel_count}")
    print(f"Кількість приголосних літер: {consonant_count}")

if __name__ == "__main__":
    main()
