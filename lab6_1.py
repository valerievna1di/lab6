def convert_to_integers():
    # Введення списку дійсних чисел з клавіатури
    input_list = input("Введіть список дійсних чисел через пробіл: ").split()

    # Перетворення введених значень на дійсні числа
    float_list = [float(num) for num in input_list]

    # Перетворення дійсних чисел у цілі з округленням
    int_list = [round(num) for num in float_list]

    # Виведення результату
    print("Список цілих чисел:", int_list)

# Виклик функції
convert_to_integers()
