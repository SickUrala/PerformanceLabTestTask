import json
import sys


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def build_value_map(values_data):
    value_map = {}
    for item in values_data.get('values', []):
        value_map[item['id']] = item.get('value', '')
    return value_map


def fill_values(node, value_map):
    if isinstance(node, dict):
        if 'id' in node and node['id'] in value_map:
            node['value'] = value_map[node['id']]

        for key, val in node.items():
            if isinstance(val, (dict, list)):
                fill_values(val, value_map)

    elif isinstance(node, list):
        for item in node:
            fill_values(item, value_map)


def main():
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    value_map = build_value_map(values_data)

    fill_values(tests_data, value_map)

    save_json(tests_data, report_path)

    print(f"Отчёт успешно сохранён в {report_path}")


if __name__ == "__main__":
    main()
