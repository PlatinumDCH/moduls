def InfinitiNaturals():
    start = 1

    while start < 100:
        yield start
        start += 1

numbers = InfinitiNaturals()
for item in numbers:
    print(item)

class NaturalNumbers:
    """infiniti iterator to return natural numbers"""

    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        num = self.num
        self.num += 1
        return num

value = iter(NaturalNumbers())

for item in range(10):
    print(next(value))