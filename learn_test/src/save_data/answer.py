def save_aplivant_data(source:dict, output:str):
    with open(output, 'w', encoding='utf-8') as f:
        for applicant in source:
            f.write(
                f'{applicant.get('name')},{applicant.get('specialty')},'
                f'{applicant.get('math')},{applicant.get('lang')},'
                f'{applicant.get('eng')}\n'
            )

applicant = [
    {'name': 'test_name1', 'specialty': 101, 'math': 111, 'lang': 111, 'eng': 111},
    {'name': 'test_name2', 'specialty': 101, 'math': 111, 'lang': 111, 'eng': 111}
]
if __name__ == '__main__':
    save_aplivant_data(applicant, 'data.csv')