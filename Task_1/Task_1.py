import json


# TODO решите задачу
def task() -> float:

    with open('input.json', 'r') as file:
        data = json.load(file)

    # Сумма произведений "score" * "weight" для каждого словаря
    result = sum(entry["score"] * entry["weight"] for entry in data)

    result = round(result, 3)

    return result

print(task())
