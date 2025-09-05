import queue
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()
request_id = 1  # Лічильник заявок

# Функція генерації нової заявки
def generate_request():
    global request_id
    request = f"Заявка №{request_id}"
    request_id += 1
    request_queue.put(request)
    print(f"✅ Створено та додано до черги: {request}")

# Функція обробки заявки
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"🔄 Обробляється: {request}")
        # Імітація часу обробки
        time.sleep(random.uniform(0.5, 1.5))
        print(f"☑️ Завершено: {request}")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Головний цикл програми
def main():
    print("Система обробки заявок запущена. Натисніть Ctrl+C для зупинки.")
    try:
        while True:
            # Генеруємо нову заявку з імовірністю
            if random.random() < 0.7:
                generate_request()
            else:
                process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограму зупинено користувачем.")

# Запуск програми
if __name__ == "__main__":
    main()
