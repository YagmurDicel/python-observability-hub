import requests
import time
import sys

print("Sisteme yapay siparis istekleri gonderiliyor... Durdurmak icin Ctrl+C yapin.")
url = "http://127.0.0.1:5000/api/order"

while True:
    try:
        response = requests.post(url, json={"item": "observability-book", "quantity": 1})
        print(f"[Istek] Durum Kodu: {response.status_code} | Yanit: {response.text.strip()}")
    except KeyboardInterrupt:
        print("\nTest sonlandirildi.")
        sys.exit(0)
    except Exception as e:
        print(f"Hata olustu: {e}")
    time.sleep(1)
