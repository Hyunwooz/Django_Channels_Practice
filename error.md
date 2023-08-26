## not found

```
Something’s not installed correctly because you’re not running the Daphne version of runserver.

Review the installation docs at Installation — Channels 4.0.0 documentation 19 and ensure you’ve got everything installed and configured correctly.
```
<a href='https://channels.readthedocs.io/en/stable/installation.html'>https://channels.readthedocs.io/en/stable/installation.html</a>

```
[10/Aug/2023 18:13:33] "GET /chat/test/ HTTP/1.1" 404 2270
[10/Aug/2023 18:13:42] "GET /chat/ HTTP/1.1" 200 415
Not Found: /chat/test
```

```
channels            4.0.0
channels-redis      4.0.0
Redis               5.0.14.1
```

```
  File "C:\Users\Hyunwoo\Desktop\ORMI\OrGo\venv\lib\site-packages\django\dispatch\dispatcher.py", line 177, in <listcomp>
    (receiver, receiver(signal=self, sender=sender, **named))
  File "C:\Users\Hyunwoo\Desktop\ORMI\OrGo\notify\consumers.py", line 68, in notification_post_save
    async_to_sync(channel_layer.group_send)(f'notify_{instance.receiver.id}', {
  File "C:\Users\Hyunwoo\Desktop\ORMI\OrGo\venv\lib\site-packages\asgiref\sync.py", line 209, in __call__
    raise RuntimeError(
RuntimeError: You cannot use AsyncToSync in the same thread as an async event loop - just await the async function directly.
```
```
파이썬 비동기 메시지 queue
```
```
알림의 경우 서버에서 단방향 통신으로 이루어져있음.
SSE를 도입해보자.
SSE(Server-Sent-Event)
SSE는 이런 단점을 해결할 수 있는 HTTP 기반의 기술이다.

기본적으로 서버에서 클라이언트로의 단방향이기 때문에, push 작업에 유용하게 쓰일 수 있다.

pip install django-eventstream channels

INSTALLED_APPS = [
    ...
    'django_eventstream',
]

MIDDLEWARE = [
    'django_grip.GripMiddleware',
    ...
]
```