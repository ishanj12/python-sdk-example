# python-sdk-example

A minimal HTTP server using the [ngrok Python SDK](https://github.com/ngrok/ngrok-python) (`ngrok`).

## Clone and Run

```sh
git clone git@github.com:ngrok/python-sdk-example.git
cd python-sdk-example
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
NGROK_AUTHTOKEN=<token> python main.py
```

## Add to Existing Code

1. Install the SDK:

   ```sh
   pip install ngrok
   ```

2. Add the following to your app:

   ```python
   import ngrok

   def forward_to_app():
       listener = ngrok.forward("localhost:8080", authtoken_from_env=True)
       print(f"Ingress established at: {listener.url()}")
   ```

## License

MIT
