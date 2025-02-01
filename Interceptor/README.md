
1. Run proxy server
```
mitmdump -s log_http_traffic.py --listen-port 8080
```

2. Make a call to run through proxy
```
python target.py
```
