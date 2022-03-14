import csv
import json

def open_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_to_txt(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for value in data:
            file.writelines(f'{value}\n')

def write_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
