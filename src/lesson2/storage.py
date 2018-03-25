import os
import argparse
import json
import tempfile

parser = argparse.ArgumentParser(description='Key value arguments')

parser.add_argument('--key', type=str)
parser.add_argument('--value', type=str)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.json')

if not os.path.isfile(storage_path):
    open(storage_path, 'w').write('{}')

with open(storage_path, 'r+') as f:
    storage = json.load(f)

    if args.value is not None:
        if args.key in storage is not None:
            value = storage[args.key]

            if isinstance(value, str):
                storage.update({args.key: [value, args.value]})
            else:
                value.append(args.value)
                storage.update({args.key: value})
        else:
            storage.update({args.key: args.value})
        f.seek(0)
        f.write(json.dumps(storage))
    else:
        if args.key in storage is not None:
            value = storage[args.key]

            if isinstance(value, str):
                print(value)
            else:
                print(', '.join(value))
        else:
            print(None)
