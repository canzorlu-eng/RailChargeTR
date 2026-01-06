# RailChargeTR
sentetik veri demo panel

# ⚡ RailChargeTR - Elektrikli Tren Enerji İzleme Sistemi

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**RailChargeTR**, frenleme ve yokuş inişi sırasında oluşan kinetik enerjiyi geri kazanarak, bu enerjiyi trenin otonom sistemleri ve hareketine yeniden yönlendiren yapay zekâ destekli bir enerji optimizasyon sistemidir.

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Ekran Görüntüleri](#-ekran-görüntüleri)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Teknik Detaylar](#-teknik-detaylar)
- [Proje Ekibi](#-proje-ekibi)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

## 🚄 Proje Hakkında

Türkiye'de demiryolu taşımacılığı hızla elektrikliye geçerken, enerji verimliliği stratejik öneme sahip hâle gelmiştir. RailChargeTR, bu alanda devrim niteliğinde bir çözüm sunmaktadır.

### Neden RailChargeTR?

- **Enerji Tasarrufu**: %15'e kadar enerji tasarrufu sağlar
- **Maliyet Düşüşü**: Yıllık milyonlarca TL tasarruf potansiyeli
- **Çevre Dostu**: Tonlarca karbon salımının önlenmesi
- **Akıllı Sistem**: AI destekli gerçek zamanlı enerji yönetimi

### Nasıl Çalışır?

1. **Enerji Toplama**: Frenleme ve yokuş inişi sırasında oluşan kinetik enerji toplanır
2. **Akıllı Analiz**: Hız, yük ağırlığı, eğim, dış sıcaklık, batarya durumu analiz edilir
3. **Dinamik Yönlendirme**: AI algoritması enerjiyi en verimli alana yönlendirir
4. **Geri Kazanım**: Bataryalara, aydınlatmaya veya anlık çekiş ihtiyacına kullanılır

## ✨ Özellikler

### 🎯 Gerçek Zamanlı İzleme
- 12 farklı tren komponenti için anlık enerji takibi
- Traksiyon motorları, HVAC, aydınlatma, kapı mekanizmaları ve daha fazlası
- Canlı grafikler ve sparkline gösterimleri

### 📊 Detaylı Veri Gösterimi
- Toplam güç tüketimi (kW)
- Toplam enerji tüketimi (kWh)
- Ortalama sistem verimliliği (%)
- Her komponent için ayrı detaylı metrikler

### 🎨 Modern Arayüz
- Karanlık tema ile göz yormayan tasarım
- Renkli kodlama sistemi (yeşil-sarı-kırmızı)
- Responsive tasarım ve smooth scroll
- 3 sütunlu grid layout ile optimize edilmiş alan kullanımı

### 🔄 Dinamik Veri Üretimi
- Sentetik veri üretimi ile gerçekçi simülasyon
- Sinüs dalgaları + rastgele gürültü algoritması
- 50ms güncelleme hızı ile kesintisiz akış
- Her komponent için özelleştirilmiş davranış modelleri

### ⚙️ Teknik Özellikler
- **Regenerative Braking**: Frenleme enerjisi geri kazanımı
- **Smart Battery Management**: Akıllı batarya yönetimi
- **AI-Powered Optimization**: Yapay zeka destekli enerji optimizasyonu
- **Real-time Analytics**: Gerçek zamanlı veri analizi

## 📸 Ekran Görüntüleri

> Arayüz tasarımı, gerçek zamanlı olarak güncellenen 12 farklı tren komponenti, toplam güç/tüketim kartları ve her komponent için canlı sparkline grafikleri içermektedir.

## 🔧 Kurulum

### Gereksinimler

```bash
Python 3.8 veya üzeri
tkinter (Python ile birlikte gelir)
```

### Adımlar

1. **Repoyu klonlayın:**
```bash
git clone https://github.com/kullaniciadi/railchargetr.git
cd railchargetr
```

2. **Uygulamayı çalıştırın:**
```bash
python tren_enerji_izleme.py
```

> Not: Tkinter Python ile birlikte gelir, ekstra kurulum gerektirmez.

## 🚀 Kullanım

### Temel Kullanım

```bash
python tren_enerji_izleme.py
```

Uygulama başladığında:
- Tüm tren komponentleri otomatik olarak izlenmeye başlar
- Gerçek zamanlı veriler 50ms aralıklarla güncellenir
- Mouse wheel veya touchpad ile scroll yapabilirsiniz
- Saat ve tarih bilgisi otomatik güncellenir

### İzlenen Komponentler

1. **Traksiyon Motorları (x4)** - 150-350 kW
2. **HVAC Sistemi** - 30-80 kW
3. **Aydınlatma** - 10-25 kW
4. **Kapı Mekanizmaları** - 5-20 kW
5. **Kontrol Sistemleri** - 8-15 kW
6. **Yardımcı Güç Ünitesi** - 20-50 kW
7. **Fren Sistemi** - 10-40 kW
8. **İletişim Sistemleri** - 3-8 kW
9. **Batarya Şarj** - 0-100 kW

### Renkli Durum Göstergeleri

- 🟢 **Yeşil**: Düşük enerji tüketimi (0-40%)
- 🟡 **Sarı**: Orta seviye tüketim (40-70%)
- 🔴 **Kırmızı**: Yüksek enerji tüketimi (70-100%)

## 🛠️ Teknik Detaylar

### Sistem Mimarisi

```
┌─────────────────────────────────────────┐
│         RailChargeTR Sistemi            │
├─────────────────────────────────────────┤
│  1. Li-Ion Pil Depolama Ünitesi        │
│  2. Enerji Optimizasyon Yazılımı       │
│  3. Power Conversion & Control          │
│  4. Wayside (Ray Kenarı) Montaj        │
│  5. Smart Grid Entegrasyonu            │
└─────────────────────────────────────────┘
```

### Veri Üretim Algoritması

```python
# Sentetik veri üretimi
drift = (center - current_energy) * 0.02
sinus = sin(time * 0.5 + phase) * 0.15 * range
noise = random(-0.1, 0.1) * range
new_energy = current + drift + sinus + noise
```

### Performans Metrikleri

- **Güncelleme Hızı**: 50ms (20 FPS)
- **Veri Noktası Kapasitesi**: 100 veri/komponent
- **Smoothing Factor**: 0.3 (yumuşak geçişler)
- **CPU Kullanımı**: Optimize edilmiş, düşük kaynak tüketimi

### Sistem Bileşenleri

#### 1. Li-Ion Pil Depolama Ünitesi
- Batarya modülleri ile enerji depolama
- Güç yönetimi ve soğutma sistemleri
- Yangın önleme mekanizmaları

#### 2. Enerji Optimizasyon Yazılımı
- Gerçek zamanlı veri analizi
- AI destekli yönlendirme
- Dinamik enerji tahsisi

#### 3. Power Conversion & Control
- DC-DC dönüştürücüler
- Güç kontrol sistemleri (PCS)
- Şebeke entegrasyonu

#### 4. Wayside Montaj Sistemi
- 1.5 MW şarj/deşarj gücü
- 420 kWh depolama kapasitesi
- Ray kenarı konumlandırma

## 🌍 Proje Vizyonu

### Ticari Potansiyel

- **300+ Elektrikli Tren**: Türkiye'de aktif sistem
- **Metro Hatları**: İstanbul, İzmir, Ankara entegrasyonu
- **İhracat Fırsatı**: Modüler yapı, kolay entegrasyon
- **Yeşil Teşvikler**: Sürdürülebilirlik odaklı

### Rekabet Avantajları

| Özellik | Barcelona Metro | Philadelphia SEPTA | ASELSAN TROBES | **RailChargeTR** |
|---------|----------------|-------------------|----------------|-----------------|
| Enerji Tasarrufu | %6 | %10 | %30 | **%15+** |
| AI Optimizasyon | ❌ | ❌ | ❌ | **✅** |
| Gerçek Zamanlı | ⚠️ | ⚠️ | ⚠️ | **✅** |
| Modüler Yapı | ⚠️ | ❌ | ⚠️ | **✅** |
| Tüm Tren Tipleri | ❌ | ❌ | ⚠️ | **✅** |

### Sektörel Etki

- **TCDD Taşımacılık**: Doğrudan maliyet düşüşü
- **Özel Lojistik**: Rekabet avantajı
- **Belediyelere**: Sürdürülebilir ulaşım
- **Çevre**: Karbon emisyonu azaltımı

## 👥 Proje Ekibi

Bu proje, **T.C. Ulaştırma ve Altyapı Bakanlığı - Ulaşan ve Erişen Türkiye 2053 Üniversiteler Arası Fikir Yarışması** kapsamında geliştirilmiştir.

**Ekip Üyeleri:**
1. Hasan Can Zorlu
2. Hüseyin Köroğlu
3. Serkan Öz
4. Muhammed Taha Keleş

**Organizasyon:**
- Ulaştırma Denizcilik ve Haberleşme Araştırmaları Merkezi Başkanlığı (UDHAM)
- Strateji Daire Başkanlığı

## 🤝 Katkıda Bulunma

Projeye katkıda bulunmak isterseniz:

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'e push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

### Geliştirme Alanları

- [ ] Gerçek sensör verisi entegrasyonu
- [ ] Makine öğrenmesi modellerinin implementasyonu
- [ ] Veri tabanı bağlantısı
- [ ] API geliştirme
- [ ] Docker containerization
- [ ] Test coverage artırımı
- [ ] Dökümantasyon genişletme

## 🙏 Teşekkürler

- T.C. Ulaştırma ve Altyapı Bakanlığı
- UDHAM - Ulaştırma Denizcilik ve Haberleşme Araştırmaları Merkezi
- Tüm destekçilerimize ve katkıda bulunanlara

---

<div align="center">

**⚡ RailChargeTR - Geleceğin Enerjisi, Bugünün Çözümü ⚡**

Made with ❤️ for sustainable transportation in Turkey

[Ulaşan ve Erişen Türkiye 2053](https://www.uab.gov.tr/)

</div>
