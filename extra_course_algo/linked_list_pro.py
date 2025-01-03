from abc import ABC

class BaseDubleLinkedList(ABC):

    @classmethod
    def add_to_end(self, data):
        """
        добавление елемента в конец списка

        создать новую ноду
        если длина списка = 0
            назначить head tail на новый елемент
        иначе
            следующее значение tail = новый елемент
            предыдущее значение нового елемента назначить на tail
            переназначить tail на новый елемент
        увеличить значение длины списка на +1 
        """
        pass
    
    @classmethod
    def del_end(self):
        """
        удалить крайний елемент

        если длина списка равна 0, нечего удалять
        если длина списка равна 1
            удаляем единственный елемент
            назначив head tail, None
        иначе
            назачить голову на tail.prev
            tail.next = None
        уменьшить длину списка на один
        """
        pass
    
    @classmethod
    def add_to_begin(self, data):
        """
        добавить в начало

        создать новую ноду
        елси длина списка равна нулю
            head, tail будет указывать на новуд голову
        иначе
            next element new node -> head
            current head prev -> new node
            cbrend head -> new node
        increment lenght list on +1 
        """
        pass
    
    @classmethod
    def del_to_begin(self):
        """
        удалить с начала

        если длина списка равна нулю
            raise список пустой
        если длина списка равна 1 
            haed tail назначить на None
        иначе
            переназначить head на слудующий елемент
            предидущий елемент actual head назначить на None
        уменьшить длину списка на один елемент
        """
        pass
    
    @classmethod
    def display(self):
        """
        print all list, mark head and tail

        save in value curent head
        print [Head], end=''
        start while loop if current != None
            print('current.data' end='->')
            current -> current next
        print  [Tail]
        """
        pass

    @classmethod
    def if_containts(self, data):
        """
        проверить что такой елемент есть 

        current element = head
        start while loop if corent element != None
            if data carent element == data
                return True 
            curent element = curent next
        return False
        """
        pass
    
    @classmethod
    def insert_before(self, search_item, new_item):
        """
        вставить елемент перед search_item

        создать новую ноду
        если head == None:
            вернуть пустой список
        если искомый елмент не найден
            return 'sersh element not fount'
        текущий елемент =  head        
        While текущий елемент не равен None:
            if current.data == searchItem:
                если теущий елемент равeн head
                    логика вставки нового елемента
                иначе
                    логика вставки в средину списка
                увеличить длину списка на один
                return 'elemen added'               
            текущий елемент = next
        """
        pass

    @classmethod
    def insert_after(self, search_item, new_item):
        """
        вставить перед определенным елементом

        создать новый узел с данными для вставки
        проверить кореектность списка и существование елемента
        инициализировать ткущий узел как head
        перебор списка
            если текущий елемент data == search_item
                обновить связи

                Если current не последний узел
                Если current последний узел, обновляем tail

                увеличить длину списка на один
            текущий елемент = next
        """
        pass
class LengInterface(ABC):

    @classmethod
    def get_lenght(self):
        """получить длину"""
        pass
    
    @classmethod
    def increment(self):
        """увеличение на одни"""
        pass

    @classmethod
    def decrement(self):
        """уменьшение на один"""
        pass


class Lenght(LengInterface):
    def __init__(self):
        self._lenght = 0
    
    def get_lenght(self):
        if self._lenght < 0:
            raise ValueError('Lenght catnnot be less zero')
        return self._lenght
    
    def _minus_lenght(self):
        if self.lenght <= 0:
            raise ValueError('Lenght cannot be less zero')
        self.lenght -= 1
    
    def increment(self):
        self._lenght += 1
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList(BaseDubleLinkedList):
    def __init__(self, lenght_manager: LengInterface):
        self.head = None
        self.tail = None
        self.lenght_manager = lenght_manager
    
    def add_to_end(self, data):
        new_node = Node(data)
        if self.lenght_manager.get_lenght() == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.lenght_manager.increment()

    def del_end(self):
        if self.lenght_manager.get_lenght() == 0:
            raise ValueError('List is empty')
        if self.lenght_manager.get_lenght() == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.lenght_manager.decrement()


    def add_to_begin(self, data):
        new_node = Node(data)
        if self.lenght_manager.get_lenght == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.lenght_manager.increment()

    def del_to_begin(self):
        if self.lenght_manager.get_lenght() == 0:
            raise ValueError('list is empty')
        if self.lenght_manager.get_lenght() == 1:
            self.head = self.tail = None
        else:
            new_head = self.head.next
            new_head.prev = (None)
            self.head = new_head
        self.lenght_manager.decrement()

    def if_containts(self, data):
        current = self.head
        while current:
            if current.data== data:
                return True
            current = current.next
        return False
 
    def display(self):
        current  = self.head
        print('[Head]',end="")
        while current:
            print(f'{current.data}', end=' -> ')
            current = current.next
        print('[Tail]')

    def _check_list(self, search_item):
        if self.head is None:
            return 'List is empty'
        
        if not self.if_containts(search_item):
            return 'sersh element not fount'

    def insert_before(self, search_item, new_item):

        new_node = Node(new_item)

        self._check_list(search_item)
        
        current = self.head
        
        while current:
            if current.data == search_item:

                if current == self.head:              
                    new_node.next = self.head
                    self.head.prev = (new_node)
                    self.head = new_node
                else:
                    previous = current.prev
                    previous.next = (new_node)
                    new_node.prev = (previous)
                    new_node.next = (current)
                    current.prev = (new_node)
                self.lenght_manager.increment()
                return 'elemen added'               
            current = current.next

    
    def insert_after(self, search_item, new_item):

        new_node = Node(new_item)

        self._check_list(search_item)
        
        current = self.head
        
        while current:
            if current.data == search_item:
                new_node.prev = current
                new_node.next = current.next

                if current.next is not None:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                
                current.next = new_node

                self.lenght_manager.increment()

                return 'element aded'
            current = current.next


if __name__ == '__main__':
    length_manager = Lenght()
    dll = DoubleLinkedList(length_manager)
    dll.add_to_end(1)
    dll.add_to_end(2)
    dll.add_to_begin(0)
    dll.display()  # Output: [Head]0 -> 1 -> 2 -> [Tail]


    print(dll.insert_after(2,-1))
    dll.display()

    
    

