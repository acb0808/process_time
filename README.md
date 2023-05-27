# Process_time
해당 프로그램은 `파이썬`에서 contextmanager을 이용한 구간 내 코드가 몇초에 걸려 실행되었는지를 구해주는 프로그램입니다. 

```py
with timing(n=10):
    # TODO Sometime...
```
위 코드로 with문 안에있는 코드가 실행이 된 후 with문을 나오게 되면 걸린 시간이 매개변수n의 자리에서 반올림한 값을 출력합니다.