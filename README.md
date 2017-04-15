# DaaSier

Documentation as a Service - A proof of concept

### Start Up

```
~/daasier > ./run.sh &
[1] 25028
~/daasier > curl -X GET http://127.0.0.1:8080/helloworld
server.get('/helloworld')
GET world!
~/daasier > curl -X POST http://127.0.0.1:8080/codeToJson -d'test.py'
server.POST('/codeToJson')
# This JSON string is stubbed out currently
{ "functionName": "foo" }
```

