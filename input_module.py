MAX_SIZE = 100
ARRAYS_COUNT = 5


def read_size(number):
    """Запрашивает размер массива, пока не введено целое число от 1 до 100."""
    while True:
        text = input(f"Массив №{number}. Введите размер (1-{MAX_SIZE}): ").strip()
        try:
            size = int(text)
        except ValueError:
            print("Ошибка: размер должен быть целым числом.")
            continue
        if 1 <= size <= MAX_SIZE:
            return size
        print(f"Ошибка: размер должен быть от 1 до {MAX_SIZE}.")


def read_array(number):
    """Читает один массив: размер, затем элементы в одной строке через пробел."""
    size = read_size(number)
    while True:
        text = input(f"Введите {size} вещественных чисел через пробел: ")
        parts = text.replace(",", ".").split()
        if len(parts) != size:
            print(f"Ошибка: нужно ввести ровно {size} чисел.")
            continue
        try:
            return [float(p) for p in parts]
        except ValueError:
            print("Ошибка: все элементы должны быть числами.")


def read_all_arrays(count=ARRAYS_COUNT):
    """Читает count массивов и возвращает их списком."""
    return [read_array(i) for i in range(1, count + 1)]
