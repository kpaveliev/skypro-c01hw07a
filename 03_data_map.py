
data_map = {'f': 'surname', 'i': 'name', 'o': 'patronymic'}
user_data = {
    'f': 'Альшевский',
    'i': 'Марк',
    'o': 'Игоревич'
}

def mapper(data, data_map):

    mapped_data = {}
    for key, value in data.items():
        mapped_key = data_map[key]
        mapped_data[mapped_key] = value

    return mapped_data

print(mapper(user_data, data_map))
