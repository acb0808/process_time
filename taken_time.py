from contextlib import contextmanager
import time

@contextmanager
def timing(n=5):
    t1 = time.time()
    yield True
    t2 = time.time()
    print(f'pref: {round(t2-t1, n)}')

if __name__ == '__main__':
    with timing(10):
        for i in range(10):
            print(i)
    
    with timing():
        import requests
        requests.get('https://naver.com')