![alt text](../src/image1.jpg)

================================================================================================
- **S** - __принцип единой ответсвенности__    *(Single Responsibility)*
- **O** - __принцип открытости-закрытости__    *(Open-Close)*
- **L** - __подставновка Барбары Лисков__      *(Liskov Sybtitusion)*
- **I** - __розделения инферфейсов__            *(Interface Segregation)*
- **D** - __инверсия зависимости__             *(Dependency Inversion)*

================================================================================================
# 1. S - Single Responsibility Principle (SRP)

    Описание :

    Каждый класс имеет свою зону ответсвенности.

### <span style="color:red">Пример 1: Плохой код</span>

``` 
    class User
        def __init__(self, name):
            self.name = name

        def get_user_data(self):
            pass  # fetch user data from the database

        def save_user_data(self):
            pass  # save user data to the database
        
        def generate_display_string(self):
            return f"User: {self.name}"
```
Клас *User* отвечает за получаение, сохранени данных а также генерацию строки отображения.

### <sapan style="color:green">Улучшеный подход:</spna>

``` 
    class User

        def __init__(self, name):
            self.name = name

    class UserDatabase:

        @staticmethod
        def get_user_data(user:User):
            pass  # fetch user data from the database

        @staticmethod
        def save_user_data(user:User):
            pass  # save user data to the database

    class UserDisplay:
        
        @staticmethod
        def generate_display_string(user:User):
            return f"User: {name}"
```
Разделена ответсвенность между тремя класами.


### <span style="color:red">Пример 2: Плохой код</span>

```
    class Rectangle:

        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height
        
        def draw(self):
            pass #logic to draw a rectangle
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class RecrangleDrawer:

    @staticmethod
    def draw(recrtangle: Recrangle):
        pass#logic to draw a rectangle
```
### <span style="color:red">Пример 3: Плохой код</span>
```
class Report:

    def __init__(self, content):
        self.content = content

    def generate_report(self):
        pass #logic to generate a report
    
    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.content)
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Report:

    def __init__(self, content):
        self.content = content
    
    def genetate_reporn(self):
        pass #logic to genetate a report

class ReportSaver:

    @staticmethod
    def save_to_file(report: Report, file_path):
        with open(file_path, 'w') as file:
            file.write(self.content)
```

# 2. O - Open Close Principle (OCP)
    Описание:

    Классы должны бать открыты для разширения, но закрыты для изменения.
### <span style="color:red">Пример 1: Плохой код.</span>
```
class Recrangle:

    def __init__(self, width, height):
        sefl.width = width
        self.height = height
    
class AreaCalculator:

    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
```

Eсли мы заходим добавить еще одну фигуру, нам нужно будет менять класс *AreaCalculator*.

### <sapan style="color:green">Улучшеный подход:</spna>
```
class Shape(ABC):

    @abstractmethod
    def area(self): ...

class Rectangle(Shape):

    def __init__(self, width, height):
        sefl.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_area(self, shape:Shape):
        return shape.area()

```
### <span style="color:red">Пример 2: Плохой код.</span>
```
class Logger:

    def log_to_file(self, message):
        print(message)

    def log_to_file(self, message, filename):
        wuth open(filename, 'w') as file:
            file.write(message)    
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Logger(ABC):

    @abstractmethod
    def log(self, message): ..

class ConfoleLogger(Logger):

    def log(self, message): 
        print(message)

class FileLogger(Logger):
    
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        with open('filename' 'w') as file:
            file.wtite(message)
```
В этом подходе если мы захотим добавить новый тип логирования, например в базу данных, нужно будет только создать новый класс наследованный от базового класса *Logger*.

### <span style="color:red">Пример 3: Плохой код.</span>
```
class Discount:

    def apply(self, order_type, price):
        if order_type == 'summer':
            return ptice * 0.9
        elif order_type == 'black_friday':
            return price * 0.7
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Dicsount(ABC):

    @abstractmethod
    def apply(self, price): ...

class SummerDicount(Discount):

    def apply(self, price):
        return ptice * 0.9

class BlackFridayDiscount(Discount):

    def apply(self, price):
            return ptice * 0.7
```
В этом примере, если захотим  создать новый вид скидок, нужно будет создать новый класс унаследованный от *Discount*.
# 3. L - Liskov Substitution Principle (LSP)

    Описание:

    Обьекты унаследованные от родительсткого класса могут быть заменены на обьекты родительсокого класса, и наоборот.

### <span style="color:red">Пример 1: Плохой код.</span>
```
class Bird:
    def fly(self): 
        return 'I can fly'

class Ostrich(Bied):
    def fly(self): 
        raise Exeprion('Cant I fly')
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Bird(ABC):

    @abstractmethod
    def move(self):
        pass

class Sparrow(Bird):

    def move(self):
        return "I can fly"

class Ostrich(Bird):

    def move(self):
        return "I can run"
```
### <span style="color:red">Пример 2: Плохой код.</span>
```
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```
### <span style="color:red">Пример 3: Плохой код.</span>
```
class Engine:

    def start(self):
        return "Engine started"

class ElectricEngine(Engine):

    def start(self):
        raise Exception("Starts differently")

class Car:

    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        return f"Car started with: {self.engine.start()}"

class ElectricCar(Car):

    def start(self):
        if isinstance(self.engine, ElectricEngine):
            return "Electric car: Electric engine started with a button"
        else:
            return super().start()
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

class GasEngine(Engine):

    def start(self):
        return "Gas engine started"

class ElectricEngine(Engine):

    def start(self):
        return "Electric engine started with a button"

class Car(ABC):

    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def start(self):
        pass

class GasCar(Car):

    def start(self):
        return f"Gas car: {self.engine.start()}"

class ElectricCar(Car):

    def start(self):
        return f"Electric car: {self.engine.start()}"

gas_engine = GasEngine()
electric_engine = ElectricEngine()

bmw = GasCar(gas_engine)
tesla = ElectricCar(electric_engine)

print(bmw.start())  # Output: Gas car: Gas engine started
print(tesla.start())  # Output: Electric car: Electric engine started with a button
```
# 4. I - Interface Segregation Principle (ISP)
    Описание:

    Клиенты не должны использовать интерфесы которые они не используют. Большие интерфесы следует розбивать на интерфейсы поменьше. Так клиенты могут использовать только те интерфесы которые им нужны.
### <span style="color:red">Пример 1: Плохой код.</span>
```
class Worker(ABC):

    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass

class Man(Worker):

    def work(self):
        return "Working hard."
    
    def eat(self):
        return "Eating lunch."

class Robot(Worker):

    def work(self):
        return "Working automatically."

    def eat(self):
        raise Exception("Robots don't eat!")
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Workable(ABC):

    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass

class Man(Workable, Eatable):

    def work(self):
        return "Working hard."
    
    def eat(self):
        return "Eating lunch."

class Robot(Workable):

    def work(self):
        return "Working automatically."
```
### <span style="color:red">Пример 2: Плохой код.</span>
```
class MultiFunctionDevice(ABC):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

class OldPrinter(MultiFunctionDevice):

    def print(self, document):
        # actual print logic
        pass

    def scan(self, document):
        raise Exception("This device can't scan!")

    def fax(self, document):
        raise Exception("This device can't fax!")
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Printer(ABC):

    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):

    @abstractmethod
    def scan(self, document):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        # actual print logic
        pass
```
### <span style="color:red">Пример 3: Плохой код.</span>
```
class Bird:
    def fly(self):
        pass
    
    def swim(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "Flying in the sky!"

    def swim(self):
        raise Exception("Sparrow can't swim!")

class Duck(Bird):
    def fly(self):
        return "Flying a short distance."

    def swim(self):
        return "Swimming in the pond!"
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class SwimmingBird(ABC):
    @abstractmethod
    def swim(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        return "Flying in the sky!"

class Duck(FlyingBird, SwimmingBird):
    def fly(self):
        return "Flying a short distance."

    def swim(self):
        return "Swimming in the pond!"
```
# 5. D - Dependency Inversion Principle (DIP)
    Описание:

    Зависимости должны строится от абстракций, а не от конкретный реализаций. Зависимости идут сверху вниз, от абстракций к реализациям.
### <span style="color:red">Пример 1: Плохой код.</span>

```
class LightBulb:

    def turn_on(self):
        return 'LightBulb turned on'

    def turn_off(self):
        return 'LightBulb turned off'

class Switch:

    def __init__(self, bulb):
        self.bulb = bulb
    
    def opetate(self):
        return self.bulb.turn_on()
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass
        
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):

    def turn_on(self):
        return "LightBulb: Bulb turned on..."
        
    def turn_off(self):
        return "LightBulb: Bulb turned off..."

class Switch:

    def __init__(self, device: Switchable):
        self.device = device
        
    def operate(self):
        return self.device.turn_on()
```
### <span style="color:red">Пример 2: Плохой код.</span>
```
class MySQLDatabase:

    def connect(self):
        return 'Connect to database'

    def disconect(self): 
        return 'Disconnect database connection'

class Application:

    def __init__(self, database):
        self.database = MySQLDatabase() # жесткая зависимость от MySQL базы данных
    
    def start(self):
        self.database.connect()
```
Тут *Application* зависит от конеретного класса *MySQLDatabase*.Если нужно заменить MySQL на PostgreSQL, придется менять код класса *Application*.`
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Database(ABC):

    @abstractmethod
    def connect(self): ...
    
    @abstractmethod
    def disconnect(self): ...

class MySQLDatabase(Database):
    def connect(self): ...

    def disconnect(self): ...

class Application:
    def __init__(self, database:Database):
        self.database = database
    
    def start(self):
        self.database.connect()
```
### <span style="color:red">Пример3: Плохой код.</span>
```
class PDFBook:

    def read(self):
        return 'reading a pdf book ...'

class EbookReader:

    def __init__(self):
        self.book = PDFBook()
    
    def read(self):
        return self.book.read()
```
### <sapan style="color:green">Улучшеный подход:</spna>
```
class Book(ABC):

    @abstractmethod
    def read(self): ...

class PDFBook(Book):
    def read(self):
        return 'reading a pdf book ... '

class EBookReader:
    def __init__(self, book:Book):
        self.book = book
    
    def read(self):
        return self.book.read()

```