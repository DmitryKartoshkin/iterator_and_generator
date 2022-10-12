nested_list = [['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None, [1, 2, 3]]]

class FlatIterator:
    def __init__(self, list_):
        self.flag = False
        self.list_iter = list_
        self.cursor = 0
        self.nested = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.flag:  # пока флаг True
            while self.cursor < len(self.list_iter):  # пока длина списка больше курсора итерация продолжается
                if self.nested < len(self.list_iter[self.cursor]):  # пока длина вложенного списка больше курсора итерация вложенного списка продолжается
                    value = self.list_iter[self.cursor][self.nested]  # формируем значение списка по индексам-курсорам
                    self.nested += 1  # увеличиваем курсор внутреннего цикла на 1
                    return value  # возвращаем полученное значение списка
                self.cursor += 1  # Увеличиваем курсор цикла на 1
                self.nested = 0  # обнуляем курсор внутреннего цикла
            self.flag = True  # После окончания элементов в свиске меняем flag на True
        raise StopIteration  # по окончании элементов в списке останавливаем итерацию

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)

