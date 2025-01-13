import hashlib

names = {'name': 'Dima', 'age': 12}

print(hash('Dima')) #8889197145612194737

hashed_dima = hashlib.md5('Dima'.encode())
print(hashed_dima.digest())
print(hashed_dima.hexdigest())

import os

def get_hash(path):
    """возвращает хеш-значение для файла"""
    with open(path, 'rb') as file:
        bytes = file.read()
        redeable_hash = hashlib.sha256(bytes).hexdigest()
        return redeable_hash
    
def find_duplicates(directory):
    hashes = {}
    duplicate = []
    for dirpath, dirname, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            file_hash = get_hash(path)
            if file_hash not in hashes:
                hashes[file_hash] = path
            else:
                duplicate.append(path, hashes[file_hash])
    return duplicate


duplicates = find_duplicates('/Users/plarium/Develop/moduls/extra_course_algo')
for duplticate in duplicates:
    print(f'Duplicate files {duplticate[0]} and {duplticate[1]}')

