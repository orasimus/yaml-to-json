import io
import json
import os
import sys

import yaml


def yaml_to_json(yaml_filename):
    filename_wo_extension = os.path.splitext(yaml_filename)[0]
    json_filename = f'{filename_wo_extension}.json'
    with io.open(yaml_filename, 'r', encoding='utf-8') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)
        with io.open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Requires YAML filename!')
    else:
        yaml_filename = sys.argv[1]
        yaml_to_json(yaml_filename)
