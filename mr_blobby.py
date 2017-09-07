#! /usr/bin/env python
import json
import random
import sys
import textblob


def main():
    for line in sys.stdin:
        d = json.loads(line)
        blobbed = textblob.TextBlob(d['text'])
        print(json.dumps({
            'example': d['example'],
            'lang': blobbed.detect_language(),
        }))


if __name__ == "__main__":
    main()
