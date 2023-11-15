import json
def main(file_path: str):
    f = open(file_path, "r")
    file = f.read()
    data = json.loads(file)
    numbers = data['numbers']
    f.close()
    return sum(numbers)

print(main("data.txt"))
