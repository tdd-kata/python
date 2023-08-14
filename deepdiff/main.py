from pprint import pprint

import requests
from deepdiff import DeepDiff


def main():
    item1 = {
        'asd': {
            'qwe': {
                'zxc': {
                }
            }
        }
    }

    item2 = {
        'asd': {
            'qwe': {
                '111': 222
            }
        }
    }

    ddiff = DeepDiff(
        t1=item1,
        t2=item2,
        ignore_order=True
    )

    pprint(ddiff, indent=2)
    if len(ddiff) == 0:
        print('No Differences')
    else:
        print('Differences Found')


def http_response():
    url1 = "https://fakestoreapi.com/products/1"
    request1 = requests.get(url1, timeout=5)
    # print(request1.status_code)
    # print(request1.headers)
    # print(request1.content)

    url2 = "https://fakestoreapi.com/products/2"
    request2 = requests.get(url2, timeout=5)
    # print(request2.status_code)
    # print(request2.headers)
    # print(request2.content)

    ddiff = DeepDiff(
        t1=request1.json()['title'],
        t2=request2.json()['title'],
        ignore_order=True,
        exclude_paths={
            'totalCount'
        }
    )

    pprint(ddiff, indent=2)
    if len(ddiff) == 0:
        print('No Differences')
    else:
        print('Differences Found')


if __name__ == '__main__':
    # main()
    http_response()
