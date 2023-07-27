from typing import Any

import redis

REDIS_HOST_DICT: dict = {
    'local': 'localhost',
    'dev': '',
    'prod': ''
}

REDIS_HOST: str = REDIS_HOST_DICT['local']
REDIS_PORT: int = 6379
KEY_NAME: str = 'spring:session:index:org.springframework.session.FindByIndexNameSessionRepository.PRINCIPAL_NAME_INDEX_NAME:tester'


def main():
    # r = redis.cluster.RedisCluster(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=False)

    """
    전체 KEY, VALUE 조회
    """
    scan_all_keys(r)

    """
    특정 KEY, VALUE 조회
    """
    # print(get(r, KEY_NAME))


def scan_all_keys(r: redis.Redis):
    for key in r.scan_iter(match='*', count=100):
        print('🚩')
        print(f'[{key.decode("utf-8")}]')
        print(f'TTL: {r.ttl(key)}')
        print(get(r, key))


def get(
    r: redis.Redis,
    key: str
) -> Any:
    b_data_type = r.type(key)
    data_type = b_data_type.decode('utf-8')
    print(f'Data Type: {data_type}')
    if data_type == 'string':
        return r.get(key)
    if data_type == 'list':
        return r.lrange(key, 0, -1)
    if data_type == 'hash':
        return r.hgetall(key)
    if data_type == 'set':
        return r.smembers(key)


if __name__ == "__main__":
    main()
