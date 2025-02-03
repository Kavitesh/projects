# run ai guard
venv\Scripts\activate
mitmdump -s ai-guard.py --listen-port 8081

# run ai guard demo
venv\Scripts\activate
python ai-guard-demo.py