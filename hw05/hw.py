import timeit

# --- Алгоритм Кнута-Морріса-Пратта (KMP) ---
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# --- Алгоритм Рабіна-Карпа (Rabin-Karp) ---
def rabin_karp(text, pattern, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s+m] == pattern:
                return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return -1

# --- Алгоритм Боєра-Мура (Boyer-Moore) ---
def boyer_moore(text, pattern):
    def bad_char_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = i
        return table

    bad_char = bad_char_table(pattern)
    m = len(pattern)
    n = len(text)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

# --- Основна логіка для завантаження текстів і тестування ---
def run_comparison():
    # Зчитування текстів з файлів
    with open("стаття 1.txt", encoding="utf-8-sig") as f1:
        text1 = f1.read()
    with open("стаття 2.txt", encoding="utf-8-sig") as f2:
        text2 = f2.read()

    # Підрядки
    patterns = {
        "стаття_1": {
            "існує": "жадібний алгоритм",
            "немає": "кіберспортивна ліга"
        },
        "стаття_2": {
            "існує": "графові моделі",
            "немає": "пінгвінові дані"
        }
    }

    # Алгоритми
    algorithms = {
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp,
        "Boyer-Moore": boyer_moore
    }

    # Тексти
    texts = {
        "стаття_1": text1,
        "стаття_2": text2
    }

    # Вимір часу
    print("Результати пошуку (час у секундах, 3 повторення):")
    for text_name, content in texts.items():
        for presence in ["існує", "немає"]:
            pattern = patterns[text_name][presence]
            print(f"\nТекст: {text_name}, Підрядок: {presence}, Пошук: '{pattern}'")
            for algo_name, algo_func in algorithms.items():
                t = timeit.timeit(lambda: algo_func(content, pattern), number=3)
                print(f"{algo_name}: {t:.6f} с")

# Запуск
if __name__ == "__main__":
    run_comparison()
