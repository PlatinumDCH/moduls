from pathlib import Path

path = Path(__file__).parent/'ingredients.csv'

def get_recipe(path, search_id):
    result = None
    with open(path, 'r') as f:
        for line in f:
            (id, name, *recipes) = line.strip().split(',')
            if id == search_id:
                result = {'id':id,'name':name,'ingr':recipes }
    return result

if __name__ == '__main__':
    result = get_recipe(path, '1232')
    print(result)
    