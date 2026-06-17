Python Observability Hub (Flask + Prometheus + Grafana)

Bu proje; Docker ortamında çalışan bir **Python Flask** uygulamasının anlık metriklerini **Prometheus** ile periyodik olarak toplayan ve **Grafana** panelleri üzerinde görselleştiren uçtan uca bir **Sistemsel Gözlemlenebilirlik (Observability)** ve alarm yönetim altyapısıdır.

İzlenen Temel Metrikler ve Canlı Gösterge Panelleri

### 1. Ortalama Yanıt Süresi (Gecikme)
Müşteri deneyimini doğrudan etkileyen sistem yavaşlıklarını yakalamak amacıyla isteklerin ne kadar sürede tamamlandığı anlık olarak izlenir.

![Ortalama Yanıt Süresi](images/request_metrics.png)

### 2. İstek Başarı ve Hata Oranları (Trafik Durumu)
Sistemdeki toplam yükü ve kararlılığı ölçmek amacıyla başarılı (`success`) ve hatalı (`error`) isteklerin zamana göre dağılımı takip edilir.

![İstek Başarı ve Hata Oranları](images/request_status.png)

Akıllı Alarm Yönetimi (Alerting)

Sistem performansının düşmesi veya yanıt sürelerinin belirlenen eşikleri aşması durumunda, Grafana'nın yerleşik alarm modülü devreye girer.

* **Alarm Kuralı:** Ortalama gecikme süresi belirlenen kritik eşiğin üzerine çıktığında sistem otomatik olarak **Firing (Aktif)** konumuna geçer.

![Yüksek Gecikme Uyarısı Aktif](images/alert_firing.png)

Projeyi Yerel Bilgisayarda Çalıştırma

### Gereksinimler
* Docker & Docker Desktop
* Python 3.12+

### Adım Adım Kurulum
1. **Docker Konteynerlerini Başlatın:**
   ```bash
   docker-compose up -d
