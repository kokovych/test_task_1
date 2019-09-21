import json

JSON_FILE_PATH = 'categories.json'


def read_json(json_file):
    with open(json_file) as jf:
        return json.load(jf)


def parse_data(element, output, ids=None, tree=None, parrent_id=None):
    children = element.get('children')
    id = element.get('id')
    name = element.get('name')

    if not tree:
        tree = name
    else:
        tree = tree + ' > ' + name

    if not ids:
        ids = [id]
    else:
        ids = ids + [id]
    level = len(ids)
    if level > 1:
        parrent_id = ids[-2]

    append_to_output(
        output=output,
        id=id,
        name=name,
        ids=ids,
        tree=tree,
        level=level,
        parrent_id=parrent_id
    )

    if children:
        for elem in children:
            if elem:
                parse_data(
                    element=elem,
                    output=output,
                    ids=ids,
                    tree=tree,
                    parrent_id=parrent_id
                )


def append_to_output(output, id, name, ids, tree, level, parrent_id):
    output.append({
        "id": id,
        "name": name,
        "ids": ids,
        "tree": tree,
        "level": level,
        "parrent_id": parrent_id
    })


def write_output_json(data):
    with open('result.json', 'w') as fj:
        json.dump(data, fj)


if __name__ == '__main__':
    json_data = read_json(json_file=JSON_FILE_PATH)
    OUTPUT_DATA = []
    for element in json_data:
        parse_data(element=element, output=OUTPUT_DATA)
    write_output_json(OUTPUT_DATA)
