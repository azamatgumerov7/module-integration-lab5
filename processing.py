# Модуль <Обработка>. Автор: <Ильнур>
def has_same_sign(elements):
    """Проверка массива: True, если все элементы > 0 или все элементы < 0.
    В процедуру передаются все элементы рассматриваемого массива."""
    if not elements:
        return False
    all_positive = all(x > 0 for x in elements)
    all_negative = all(x < 0 for x in elements)
    return all_positive or all_negative


def check_arrays(arrays):
    """Возвращает список результатов проверки для каждого массива."""
    return [has_same_sign(arr) for arr in arrays]

