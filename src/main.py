import json
from src.operation_func import filter_and_sorting, prepare_user_message


with open('../data/operations.json') as file:
    data = json.load(file)

items = filter_and_sorting(data)

for i in range(5):
    print(prepare_user_message(items[i]))