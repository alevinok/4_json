import json, sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        try:
            json_content = json.load(file_handler)
            pretty_print_json(json_content)
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(data_json):
    print(json.dumps(data_json, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    load_data(path_to_file)
