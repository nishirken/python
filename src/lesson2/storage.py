import argparse
import json

parser = argparse.ArgumentParser(description='Key value arguments')

parser.add_argument('--key', type=str)
parser.add_argument('--value', type=str)
args = parser.parse_args()


f = open('./storage.json', 'r+')

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
        print(args.key, '- key does not exists')
