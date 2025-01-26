from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterator
from enum import Enum

class PathFile(Path, Enum):
    path_file = Path(__file__).parent / 'company_worker.csv'

class IFileReader(ABC):
    """interface class for readfiles"""
    def __init__(self, file_path:str):
        self.file_path = file_path

    @abstractmethod
    def read_lines(self) -> Iterator[str]: ...

class ISalaryProcessor(ABC):
    """processing calculate sum&avg salary"""
    @abstractmethod
    def process(self): ...

    @abstractmethod
    def get_results(self): ...

class ISalaryCalculator(ABC):
    """facade class"""
    @abstractmethod
    def calculate(self): ...


class FileReader(IFileReader):
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_lines(self) -> Iterator[str]:
        try:
            with open(self.file_path) as file:
                for line in file:
                    yield line.strip()

        except FileNotFoundError:
            raise Exception ("file not found")
        except PermissionError:
            raise Exception ("permission danied" ) #недостаточно прав для доступа
        except IsADirectoryError:
            raise Exception ("path is a directory, not a file")
        except Exception as e:
            raise Exception (f'An error occured: {str(e)}')

class SalaryProcessor(ISalaryProcessor):
    """class for processing data salary"""

    def __init__(self, data_sourse: Iterator[str]):
        self.data_sourse = data_sourse
        self.total_salary = 0
        self.valid_workers = 0
    
    def process(self)->None:
        for line in self.data_sourse:
            if not line:
                continue
            
            if ',' not in line:
                raise ValueError ('Invalid data in file')
                
            name, salary_str = line.split(',', 1)
            name = name.strip()
            salary_str = salary_str.strip()
                            
            if not name:
                raise ValueError ('No valid workers to calculate salary')
                
            if not salary_str:
                raise ValueError('Invalid data salary')

            self.total_salary += int(salary_str)
            self.valid_workers += 1

    def get_results(self):
        if self.valid_workers == 0:
            return 'No valid workers to calculate salary'
        
        average_salary = (self.total_salary / self.valid_workers)
        return self.total_salary, average_salary

class SalaryCalculator(ISalaryCalculator):
    """facade patter calculate salary"""

    def __init__(self, file_path:Path):
        self.file_reader = FileReader(file_path)
    
    def calculate(self) -> str:
        try:
            lines = self.file_reader.read_lines()

            processor = SalaryProcessor(lines)
            processor.process()
            total, average = processor.get_results()

            return f'Total salary: {total}, Average salary: {average:.2f}'
        except Exception as e:
            return str(e)
         
        
if __name__ == "__main__":
    path_to_file = PathFile.path_file.value
    calculator = SalaryCalculator(path_to_file)
    result = calculator.calculate()
    print(result)

