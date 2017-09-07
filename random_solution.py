import json
import random
import sys



def main():
    lang_codes = ('fr', 'it', 'en', 'tw')
    for line in sys.stdin:
        d = json.loads(line)
        print(json.dumps({
            'example': d['example'],
            'lang': random.choice(lang_codes),
        }))


if __name__ == "__main__":
    main()
