from pathlib import Path
import shutil


def copy_api_key():
    try:
        p = Path('/Users/eliott.legendre/Desktop/news_api.secret')
        target = f'/tmp/{p.name}'
        shutil.copy(p, target)
    except FileNotFoundError:
        print(f'Not found in [{p}] - Trying another source')

    try:
        p = Path('/mnt/news_api.secret')
        target = f'/tmp/{p.name}'
        shutil.copy(p, target)
    except FileNotFoundError:
        print(f'Not found in [{p}] - Trying another source')
        raise FileNotFoundError(f'Api Key secret file not found in [{p}].')

    print(f'Api Key secret file copied to [{target}]')
    return 0


def read_api_key(path: Path = Path('/tmp/news_api.secret')):
    with path.open('r') as f:
        api_key = f.read()
    return api_key


def get_key():
    try:
        api_key = read_api_key()
    except FileNotFoundError:
        copy_api_key()
        api_key = read_api_key()
    return api_key
