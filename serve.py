"""Локальный просмотр: python3 serve.py"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    print("Откройте http://127.0.0.1:8000")
    ThreadingHTTPServer(("127.0.0.1", 8000), handler).serve_forever()
