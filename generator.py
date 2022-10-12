nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f','h',False],
    [1, 2, None, ['e', 'f','h', [1, 2, 3, 4, [False, True, None]]]], 5]

def recursive_iterator(list_):
    for iter_ in list_: # считываем элементы внешнего списка
        if isinstance(iter_, list): # проверяем является ли вложенный объект списком
            yield from recursive_iterator(iter_) # если является то итерируесмся по нему с помощью нашей функции
        else: # если элемент списка не являетя итерируемым объектом
            yield iter_ # возвращаем его

if __name__ == '__main__':
    for it in recursive_iterator(nested_list):
        print(it, end =' ')
