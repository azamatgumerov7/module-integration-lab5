def print_results(results):
    """Печатает результат по каждому массиву.
    results — список bool, номер массива = индекс + 1."""
    print("\nРезультат:")
    for number, ok in enumerate(results, start=1):
        if ok:
            print(f"Массив №{number}: элементы одного знака.")
        else:
            print(f"Массив №{number}: нет, элементы не одного знака.")

    if not any(results):
        print("Ни один массив не состоит из элементов одного знака.")