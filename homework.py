
def onlyEven(lst):
    """
    Задание 1.
    Реализуйте функцию, которая принимает список чисел lst и возвращает
    список только из четных чисел.
    При выполнении этого задания используйте функцию filter.
    Помните, что функция filter возвращает итератор.

    >>> onlyEven([1, 2, 3, 4, 5])
    [2, 4]
    >>> onlyEven([1, 3, 5])
    []
    >>> onlyEven([2, 4, 6, 8, 10])
    [2, 4, 6, 8, 10]
    """

    return list(filter(lambda x: x % 2 == 0,lst))

def squareList(lst):
    """
    Задание 2.
    Реализуйте функцию, которая принимает список чисел lst и возвращает
    список квадратов чисел.
    При выполенении этого задания использовать функцию map.
    Помните, что функция map возвращает итератор.

    >>> squareList([1, 2, 3, 4])
    [1, 4, 9, 16]
    >>> squareList([-1, -2, 3, 4])
    [1, 4, 9, 16]
    """

    return list(map(lambda x: x** 2,lst))

def squereOnlyEven(lst):
    """
    Задание 3.
    Реализуйте функцию, которая принимает список lst и возвращает
    сприсок квадратов только четных чисел.
    При выполенении этого задания использовать функцию map и filter

    >>> squereOnlyEven([1, 2, 3, 4, 5])
    [4, 16]
    >>> squereOnlyEven([1, 3, 5])
    []
    >>> squereOnlyEven([2, 4, 6, 8, 10])
    [4, 16, 36, 64, 100]
    """
    return list(map(lambda x: x ** 2,list(filter(lambda x: x % 2 == 0, lst))))
    

def allUpper(lst):
    """
    Задание 4
    Реализуйте функцию, которая принимает список строк lst и возвращает
    список, в котром все строки преобразованы к верхнему регистру.
    При выполнении этого задания использовать функцию map

    >>> allUpper(['hello', 'world'])
    ['HELLO', 'WORLD']
    >>> allUpper(['test'])
    ['TEST']
    """
    return list(map(lambda x: x.upper(),lst))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
