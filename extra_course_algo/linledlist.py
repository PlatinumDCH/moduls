import logging
from abc import ABC


logging.basicConfig(
    # filename='example_2.log',#файл в который будет созраняться логи
    encoding="utf-8",  # формать кодировки
    level="INFO",  # епередаваемый уровень логирования
    filemode="w",  # перезапись файла
    format="%(asctime)s:%(levelname)s---%(message)s",  # формат лога
    datefmt="%m/%d/%Y %I:%M:%S",  # можно указывать формат времени
)

# Используем логгер
logger = logging.getLogger(__name__)

class LinkedListBase(ABC):
    """
    абстрактрый базовый класс для односвязновго списка
    self.head = None, указатель на голову
    """

    @classmethod
    def insert_at_and(self, data):
        """
        вставить новый узел в конец
        проверка что голова не пуствя
        оределить текущиее звено
        пройтись по каждому звену сurent.next while
        как только следущее звено будет None
        цикл звершатся
        станавливаем следуйщее звено на Node(data)
        """
        pass
    
    @classmethod
    def insert_at_begin(self, data):
        """
        вставить в начало
        
        создать цепь Node(data)
        установить следуйщее значение новой цепи на страрую голову
        установить head на новое звено
        """
        pass
    
    @classmethod
    def insert_after(self, prev_node, data):
        """
        вставить перед каким-то значением prev_node

        если не указать перед каким значением вставить венуть None
        создать новую ноду
        ссылка на следующий узел из нового узла = rev_node.next
        ссылка на следующий узел елемента перед которым вставляем = 
        новое звено

        пример
        текущий списко
        head(1)->(2)->(3)
        Задача вставить перед 3 елементом

        узать перед каким елеменом будем вставлять -2-
        newnode_link.next = 3
        -2-.next = newnode
        """
        pass
    
    @classmethod
    def search(self, data):
        """
        поиск по информации в узле
        
        назначить текщий елемент используя голову
        пройтись циклом и сравнивать current.data == data
        """

        pass
    
    @classmethod
    def display(self):
        pass

    @classmethod
    def delete(self, data):
        pass
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(LinkedListBase):
    def __init__(self):
        self.head = None

    def isert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current = current.next
        logger.info(f'not found element {data}')

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" - > ".join(map(str, elements)))

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current is None:
            return
        previous.next = current.next
        current = None


if __name__ == "__main__":
    llist = LinkedList()

    llist.isert_at_end(1)
    llist.isert_at_end(2)
    llist.isert_at_end(3)

    logger.info(llist.display())
