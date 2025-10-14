def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)

    print("\n📄 Таблиця зсувів:")
    print(f"{'Символ':^10} | {'Індекс':^6} | {'Зсув':^5} | {'Запис у таблицю':^20}")
    print("-" * 50)

    for index, char in enumerate(pattern[:-1]):
        shift = length - index - 1
        table[char] = shift
        print(f"{repr(char):^10} | {index:^6} | {shift:^5} | {repr(char)}: {shift:^5}")

    # Останній символ
    last_char = pattern[-1]
    shift = length
    table.setdefault(last_char, shift)
    print(f"{repr(last_char):^10} | {length-1:^6} | {shift:^5} | {repr(last_char)}: {shift:^5}")

    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)

    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


# 🔍 Тест
text = "Being a developer is not easy"
pattern = "developer"

position = boyer_moore_search(text, pattern)
if position != -1:
    print(f"\n✅ Підрядок знайдено на позиції {position}")
else:
    print("\n❌ Підрядок не знайдено")
