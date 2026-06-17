import time
import random
from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# 1. İstek Sayacı (Mevcut olan)
REQUEST_COUNTER = Counter('http_requests_total', 'Toplam istek sayisi', ['status'])

# 2. YENİ: Yanıt Süresi Ölçer (Histogram)
# Bu metrik isteklerin ne kadar sürdüğünü saniye cinsinden ölçecek
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'İstek yanit süresi (saniye)', ['endpoint'])

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/api/order', methods=['POST'])
def create_order():
    # İstek başladığı an süreyi tutuyoruz
    start_time = time.time()
    
    # Simülasyon gecikmesi (0.1 ile 0.4 saniye arası)
    processing_time = random.uniform(0.1, 0.4)
    time.sleep(processing_time)
    
    if random.random() < 0.15:
        REQUEST_COUNTER.labels(status='error').inc()
        # Hata olsa bile süreyi kaydediyoruz
        REQUEST_LATENCY.labels(endpoint='/api/order').observe(time.time() - start_time)
        return jsonify({"error": "Payment failed"}), 500
        
    REQUEST_COUNTER.labels(status='success').inc()
    # Başarı durumunda süreyi kaydediyoruz
    REQUEST_LATENCY.labels(endpoint='/api/order').observe(time.time() - start_time)
    return jsonify({"status": "success", "order_id": random.randint(1000, 9999)}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)