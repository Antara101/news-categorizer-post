# -*- coding: utf-8 -*-

import collections
import json
import os


def main():
    for path in filter(lambda p: p.endswith('_raw.json'), os.listdir('.')):
        with open(path, 'rb') as f:
            data = json.load(f)["results"]
            stitched = collections.defaultdict(str)

            for obj in data['collection1']:
                try:
                    if type(obj['property1']) is unicode:
                        stitched[obj['url']] += obj['property1']
                    else:
                        stitched[obj['url']] += obj['property1']['text']
                except:
                    import ipdb; ipdb.set_trace()
                    a = 1

            out = {'news': [text for text in stitched.itervalues() if text]}
            with open(path[:-len('_raw.json')] + '.json', 'wb') as o:
                json.dump(out, o, indent=2)


if __name__ == '__main__':
    main()
