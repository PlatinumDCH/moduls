from datetime import datetime, date
import faker
from random import randint, choice
import sqlite3
import enum
from connect import create_connection, path_to_database

class SetNum(int, enum.Enum):
    count_companies:int = 3
    count_employess:int = 30
    count_position:int = 5

def generate_fake_data(all_data):

    fake_companies = []
    fake_employes = []
    fake_positions = []

    fake_data = faker.Faker()

    for _ in range(all_data.count_companies.value):
        fake_companies.append(fake_data.company())
    
    for _ in range(all_data.count_employess.value):
        fake_employes.append(fake_data.name())
    
    for _ in range(all_data.count_position.value):
        fake_positions.append(fake_data.job())
    
    return fake_companies, fake_employes, fake_positions


def printing(object):
    for i in object:
        print(i)



def prepea_data(companies, employes, posts)->tuple:
    for_companies = []
    for company in companies:
        for_companies.append((company,))
    
    for_employees = []
    for emp in employes:
        for_employees.append((emp, choice(posts), randint(1, SetNum.count_companies.value )))

    for_payments = []
    for month in range(1, 13):
        payment_date = datetime(2021, month, randint(10,20)).date()
        for emp in range(1, SetNum.count_employess.value + 1):
            for_payments.append((emp, payment_date, randint(1_000, 10_000) ))
    
    return for_companies, for_employees, for_payments

def insert_data(companies, employes, payments)->None:
    with create_connection(path_to_database) as conn:
        cur = conn.cursor()

        sql_comp = '''insert into companies(company_name) values(?)'''
        cur.executemany(sql_comp, companies)

        sql_empl = '''insert into employees(employees, post, company_id)
        values(?,?,?)'''
        cur.executemany(sql_empl, employes)

        sql_pyment = '''insert into payments(employee_id, date_of, total)
        values(?,?,?)'''
        cur.executemany(sql_pyment, payments)

        conn.commit()


        
if __name__ == '__main__':
    c,e,p = prepea_data(*generate_fake_data(SetNum))
    insert_data(c,e,p)
