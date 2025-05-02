import cv2
import pygame
import time
from deepface import DeepFace
import random
import textwrap

# Kamera ve ses başlatma
cap = cv2.VideoCapture(0)
pygame.mixer.init()
#güncelleme
# Duygu çevirileri
duygu_cevirisi = {
    "angry": "Kizgin",
    "disgust": "Tiksinti",
    "fear": "Korku",
    "happy": "Mutlu",
    "sad": "Uzgun",
    "surprise": "Saskin",
    "neutral": "Notr"
}

# Duyguya göre kahve önerileri
kahve_onerileri = {
    "angry": [
        {"isim": "Sade Americano", "aciklama": "Yogun ve guclu bir icim, ofkenizi dindirmek icin"},
        {"isim": "Dark Roast Filtre Kahve", "aciklama": "Yogun aromalar zihninizi rahatlatabilir"},
        {"isim": "Soguk Demleme Kahve", "aciklama": "Dusuk asitli ve sakinlestirici etkili"}
    ],
    "disgust": [
        {"isim": "Tarcinli Latte", "aciklama": "Tarcinin aromatik tadi ruh halinizi degistirebilir"},
        {"isim": "Nane Aromali Soguk Kahve", "aciklama": "Ferahlatici bir tat deneyimi"}
    ],
    "fear": [
        {"isim": "Sicak Cikolatali Mocha", "aciklama": "Cikolatanin rahatlatici etkisiyle"},
        {"isim": "Tarcin ve Bal Karisimli Latte", "aciklama": "Sakinlestirici bal ve tarcin kombinasyonu"}
    ],
    "happy": [
        {"isim": "Karamelli Frappuccino", "aciklama": "Tatli ve eglenceli, mutlulugunuzu kutlayin"},
        {"isim": "Vanilyali Latte", "aciklama": "Hafif ve keyifli bir tat"},
        {"isim": "Buzlu Kahve ve Krema", "aciklama": "Serinletici ve neseli bir icecek"}
    ],
    "sad": [
        {"isim": "Sicak Cikolatali Mocha", "aciklama": "Cikolata endorfin salgilar ve ruh halinizi yukseltir"},
        {"isim": "Balli Tarcinli Latte", "aciklama": "Sicak ve rahatlatici, ruhunuzu isitir"},
        {"isim": "Baharatli Chai Latte", "aciklama": "Sicak baharatlar enerji verir ve ruh halinizi yukseltir"}
    ],
    "surprise": [
        {"isim": "Egzotik Aromatik Filtre Kahve", "aciklama": "Yeni ve ilginc tatlar deneyimleyin"},
        {"isim": "Hindistan Cevizli Buzlu Kahve", "aciklama": "Beklenmedik ve ferahlatici bir lezzet"}
    ],
    "neutral": [
        {"isim": "Klasik Cappuccino", "aciklama": "Dengeli ve tanidik bir lezzet"},
        {"isim": "Filtre Kahve", "aciklama": "Sade ve dogal kahve deneyimi"},
        {"isim": "Hafif Roast Espresso", "aciklama": "Dengeli ve yumusak bir icim"}
    ]
}

# Duygu sesleri
duygu_sesleri = {
    "happy": "happy.mp3",
    "sad": "sad.mp3"
}

son_duygu = None
son_guncelleme_zamani = 0
guncelleme_arasi_saniye = 10  # Her 10 saniyede bir görsel güncelleme yapılacak

# Konsol renkleri
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Font seçenekleri
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 0.6
font_thickness = 1
text_color = (255, 255, 255)  # Beyaz
box_color = (0, 128, 0)  # Koyu yeşil

print(f"{bcolors.HEADER}Duygu Tabanli Kahve Oneri Sistemi Baslatildi{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Cikmak icin 'q' tusuna basin{bcolors.ENDC}")

guncel_duygu = None
guncel_onerileri = []

while True:
    ret, frame = cap.read()
    if not ret:
        print(f"{bcolors.FAIL}Kamera görüntüsü bulunamadı.{bcolors.ENDC}")
        break
        
    frame = cv2.flip(frame, 1)  # Ayna görüntüsü
    
    # Görüntü kopya oluştur
    display_frame = frame.copy()
    
    try:
        # DeepFace analizi
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        
        if len(analysis) > 0:  # En az bir yüz bulunduysa
            face = analysis[0]  # İlk yüzü al
            
            # Yüz bölgesi ve duygu bilgisi
            x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
            emotion = face['dominant_emotion']
            turkce_emotion = duygu_cevirisi.get(emotion, emotion)
            
            # Yüz çerçevesi çiz
            cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Her algılamada duyguyu güncelle
            guncel_duygu = emotion
            
            # Her 5 saniyede bir görsel güncelleme yap
            suanki_zaman = time.time()
            if (suanki_zaman - son_guncelleme_zamani > guncelleme_arasi_saniye):
                # Duyguya göre kahve önerilerini güncelle
                if emotion in kahve_onerileri and len(kahve_onerileri[emotion]) > 0:
                    guncel_onerileri = kahve_onerileri[emotion]
                    
                    # Tüm kahve önerilerini konsola yazdır
                    print(f"\n{bcolors.BOLD}{turkce_emotion} duygusunu algiladim!{bcolors.ENDC}")
                    print(f"{bcolors.OKGREEN}Kahve Onerileri:{bcolors.ENDC}")
                    
                    for i, oneri in enumerate(kahve_onerileri[emotion]):
                        print(f"{bcolors.OKGREEN}{i+1}. {oneri['isim']}{bcolors.ENDC}")
                        print(f"{bcolors.OKCYAN}   {oneri['aciklama']}{bcolors.ENDC}")
                    
                    print(f"\nBir sonraki güncelleme {guncelleme_arasi_saniye} saniye sonra yapılacak.")
                    
                    son_duygu = emotion
                    son_guncelleme_zamani = suanki_zaman
            
            # Duygu bilgisini YÜZ YANINA yazdır
            cv2.putText(display_frame, f"Duygu: {turkce_emotion}", (x + w + 10, y + 20), 
                      font, font_scale, text_color, font_thickness, cv2.LINE_AA)
            
            # Önerileri göster (yüz yanına)
            if guncel_onerileri:
                # Başlık ekle
                baslik = f"{duygu_cevirisi.get(son_duygu, 'Henuz algilanmadi')} icin kahve onerileri:"
                text_size = cv2.getTextSize(baslik, font, font_scale, font_thickness)[0]
                cv2.rectangle(display_frame, (x + w + 10, y + 30), (x + w + 10 + text_size[0], y + 50), box_color, -1)
                cv2.putText(display_frame, baslik, (x + w + 10, y + 45), 
                          font, font_scale, text_color, font_thickness, cv2.LINE_AA)
                
                # Tüm önerileri ve açıklamaları YÜZÜN YANINA göster
                offset_y = 70  # 55'ten 70'e çıkarıldı - başlık ile ilk öneri arasında daha fazla boşluk
                for i, oneri in enumerate(guncel_onerileri):
                    # Öneri başlığı için
                    oneri_text = f"{i+1}. {oneri['isim']}"
                    text_size = cv2.getTextSize(oneri_text, font, font_scale * 0.8, font_thickness)[0]
                    y_pos = y + offset_y
                    cv2.rectangle(display_frame, (x + w + 10, y_pos - 15), 
                                 (x + w + 10 + text_size[0], y_pos + 5), box_color, -1)
                    cv2.putText(display_frame, oneri_text, (x + w + 10, y_pos), 
                              font, font_scale * 0.8, text_color, font_thickness, cv2.LINE_AA)
                    offset_y += 25
                    
                    # Açıklama için
                    aciklama = oneri['aciklama']
                    wrapped_text = textwrap.wrap(aciklama, width=30)
                    for line in wrapped_text:
                        y_pos = y + offset_y
                        text_size = cv2.getTextSize(line, font, font_scale * 0.7, font_thickness)[0]
                        cv2.rectangle(display_frame, (x + w + 20, y_pos - 15), 
                                     (x + w + 20 + text_size[0], y_pos + 5), (30, 80, 30), -1)
                        cv2.putText(display_frame, line, (x + w + 20, y_pos), 
                                  font, font_scale * 0.7, text_color, font_thickness, cv2.LINE_AA)
                        offset_y += 20
                    
                    # Öneriler arası ekstra boşluk
                    offset_y += 5
    
    except Exception as e:
        error_msg = f"Analiz hatası: {str(e)}"
        print(f"{bcolors.FAIL}{error_msg}{bcolors.ENDC}")
        # Hata mesajını görüntü üzerine yazdır
        cv2.putText(display_frame, "Yüz algılanamadı", (10, 30), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

    # Gösterge panosu ekle
    cv2.rectangle(display_frame, (10, 10), (260, 100), (64, 64, 64), -1)
    cv2.putText(display_frame, "Duygu-Kahve Oneri Sistemi", (20, 30), font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(display_frame, "Q: Cikis", (20, 50), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(display_frame, f"Son duygu: {duygu_cevirisi.get(son_duygu, 'Henuz algilanmadi')}", 
              (20, 70), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(display_frame, f"Guncelleme: {int(guncelleme_arasi_saniye - (time.time() - son_guncelleme_zamani))} sn", 
              (20, 90), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    
    # Pencerede göster
    cv2.imshow('Duygu Tabanli Kahve Oneri Sistemi', display_frame)

    # Q tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
print(f"{bcolors.HEADER}Program sonlandirildi.{bcolors.ENDC}")
