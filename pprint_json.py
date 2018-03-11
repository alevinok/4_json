import json, sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        json_content = json.load(file_handler)
    return json_content


def pretty_print_json(file_data):
    print(json.dumps(file_data, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        pretty_print_json(load_data(path_to_file))
    except IndexError:
        print('Enter the path to the file.')
    except FileNotFoundError:
        print('No such file.')
