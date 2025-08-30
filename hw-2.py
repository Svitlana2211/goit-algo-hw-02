from collections import deque

def is_palindrome(input_string):
    # Нормалізація рядка: нижній регістр і видалення пробілів
    normalized = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Створення двосторонньої черги з символів
    char_deque = deque(normalized)
    
    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        left = char_deque.popleft()
        right = char_deque.pop()
        if left != right:
            return False  # Якщо символи не співпадають — не паліндром
    
    return True  # Якщо цикл завершився — це паліндром


test_strings = [
    "Казак",
    "Я несу гусеня",
    "Не паліндром",
    "123321",
    "Р о т о р"
]

for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' → {'✅ Паліндром' if result else '❌ Не паліндром'}")
