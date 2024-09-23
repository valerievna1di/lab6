def find_shortest_word():
    # Введення списку слів з клавіатури
    word_list = input("Введіть список слів через пробіл: ").split()

    # Знаходимо найкоротше слово за довжиною
    shortest_word = min(word_list, key=len)

    # Виводимо найкоротше слово
    print("Найкоротше слово:", shortest_word)

# Виклик функції
find_shortest_word()
