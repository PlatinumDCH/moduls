import json

def write_contact_to_file(filename, contacts):
    with open(filename, 'w') as file:
        json.dump({'contacts':contacts}, file)

def read_contacts_from_file(filename):
    with open (filename, 'r') as file:
        connect = json.load(file)
    return connect.get('contacts')      