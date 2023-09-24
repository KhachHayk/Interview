class Stack(list):

    """Класс Stack со следующими методами:
        is_empty — проверка стека на пустоту. Метод возвращает True или False;
        push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
        pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
        peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
        size — возвращает количество элементов в стеке."""

    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def push(self, item):
        self.values.append(item)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def size(self):
        return len(self.values)