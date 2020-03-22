import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help="display a values of a given key", type=str)
parser.add_argument("-v", "--val", help="display a keys of a given value", type=str)
args = parser.parse_args()


try:
    with open(storage_path, 'r') as f:
        storage_dict = json.loads(f.read())
        # f.seek(0)
        # print(f.read())
except:
    storage_dict = {args.key: []}
    pass

if args.key and not args.val:
    if args.key in storage_dict:
        print(', '.join(storage_dict[args.key]))
    else:
        print(None)

if args.key and args.val:
    with open(storage_path, 'w') as f:
        if args.key in storage_dict:
            storage_dict[args.key].append(args.val)
            f.write(json.dumps(storage_dict))
        else:
            storage_dict[args.key] = list(args.val.split())
            f.write(json.dumps(storage_dict))
