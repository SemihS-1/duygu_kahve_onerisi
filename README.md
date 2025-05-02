Duygu Tabanlı Kahve Öneri Sistemi 🧠☕

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-brightgreen)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-yellow)
![DeepFace](https://img.shields.io/badge/DeepFace-0.0.75-orange)

Duygu Tabanlı Kahve Öneri Sistemi, gerçek zamanlı yüz analizi kullanarak kullanıcının duygusal durumunu tespit eden ve buna uygun kahve önerileri sunan yapay zeka destekli bir uygulamadır. DeepFace kütüphanesi kullanılarak yüz ifadelerini analiz eder ve kişinin ruh haline en uygun kahve çeşitlerini önermek için geliştirilmiş bir algoritmaya sahiptir.

## 🌟 Özellikler

- **Gerçek zamanlı duygu analizi**: Kamera kullanarak anlık yüz ifadesi tespiti
- **7 temel duygu durumu tanıma**: Kızgın, tiksinti, korku, mutlu, üzgün, şaşkın ve nötr
- **Gelişmiş sinirlilik tespiti**: Mikro yüz ifadelerini kullanarak daha hassas sinirlilik tespiti
- **Kişiselleştirilmiş kahve önerileri**: Her duygu durumuna özel seçilmiş kahve türleri
- **Duygu geçmişi takibi**: Ani duygu değişimleri yerine tutarlı duygu tespiti
- **Kullanıcı dostu arayüz**: Gerçek zamanlı geri bildirim ve görsel ipuçları
- **Ayrıntılı konsol çıktıları**: Renkli ve düzenli biçimlendirilmiş terminal bilgileri

## 📋 Gereksinimler

```
python >= 3.6
opencv-python
deepface
pygame
numpy
```

## 🚀 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/duygu-kahve-oneri-sistemi.git
cd duygu-kahve-oneri-sistemi
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Programı çalıştırın:
```bash
python duygu_kahve_oneri.py
```

## 💡 Kullanım

Programı çalıştırdığınızda, web kameranız otomatik olarak açılacaktır. Yüzünüzü kameraya doğru tutun ve sistem duygu durumunuzu algılamaya başlayacaktır.

- Ekranın sol üst köşesindeki kontrol panelinde, algılanan duygular ve sayaçlar gösterilir
- Tespit edilen yüz çerçeve ile işaretlenir (yeşil)
- Duygu durumunuza göre önerilen kahveler, yüzünüzün sağ tarafında listelenir
- Programdan çıkmak için `q` tuşuna basın

## 🔍 Nasıl Çalışır?

Sistem, DeepFace kütüphanesinin sunduğu derin öğrenme tabanlı duygu analizi modelini kullanarak, yüz ifadelerini 7 temel duygu kategorisine göre sınıflandırır. Gelişmiş sinirlilik tespiti için:

1. Belirli eşik değerleri kullanılarak mikro ifadeler tespit edilir
2. Ardışık kareler boyunca tutarlı ifadeler takip edilir
3. Duygu geçmişi kullanılarak ani değişimler filtrelenir
4. Tespit edilen duyguya göre özel kahve önerileri sunulur

## 🛠️ Özelleştirme

Kod içerisindeki şu değişkenleri düzenleyerek sistemi özelleştirebilirsiniz:

- `guncelleme_arasi_saniye`: Kahve önerilerinin yenilenme sıklığı (varsayılan: 10 saniye)
- `duygu_gecmisi_uzunlugu`: Kaç duygu durumunun geçmişte saklanacağı (varsayılan: 5)

Ayrıca, `kahve_onerileri` sözlüğünü düzenleyerek kendi kahve önerilerinizi ekleyebilirsiniz.

## 🖼️ Ekran Görüntüleri

![image](https://github.com/user-attachments/assets/a207ea7e-b242-47ce-afb6-8047fa951241)
![image](https://github.com/user-attachments/assets/4ff72dc3-b024-4f25-891e-cf45e01adb59)


