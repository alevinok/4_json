import json, sys, os


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as file:
        try:
            data = json.load(file)
            pretty_print_json(data)
        except json.decoder.JSONDecodeError:
            sys.exit('Не верный формат файла.')


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):        # Проверка существования файлa
        sys.exit('Введите путь к файлу.')

    load_data(filepath)
