# 🩸 Hemoglobin Regresyon ile Anemi Tanı Destek Sistemi

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/Lisans-Eğitim%20Amaçlı-green)

**Ders:** Tıbbi İstatistik ve Tıp Bilişimine Giriş  
**Proje Türü:** Final Projesi  
**Tarih:** Aralık 2025

</div>

---

## 📋 İçindekiler

1. [Proje Hakkında](#-proje-hakkında)
2. [Özellikler](#-özellikler)
3. [Kurulum](#-kurulum)
4. [Kullanım](#-kullanım)
5. [Proje Yapısı](#-proje-yapısı)
6. [Teknik Detaylar](#-teknik-detaylar)
7. [Veri Seti](#-veri-seti)
8. [Model Performansı](#-model-performansı)
9. [Ekran Görüntüleri](#-ekran-görüntüleri)
10. [Önemli Uyarılar](#-önemli-uyarılar)

---

## 🎯 Proje Hakkında

Bu proje, kan tahlili verilerinden **Hemoglobin (Hb)** değerini tahmin etmek için **Linear Regression** modeli kullanır ve tahmin edilen değere göre **WHO klinik kurallarına** dayalı anemi tespiti yapar.

### Temel Özellikler

| Özellik | Açıklama |
|---------|----------|
| **Makine Öğrenmesi** | Linear Regression (regresyon modeli) |
| **Anemi Tespiti** | WHO eşik değerlerine dayalı kural tabanlı karar |
| **Arayüz** | Streamlit web uygulaması + Konsol |
| **Hedef Değişken** | Hb - Hemoglobin (g/dL) |
| **Özellikler** | RBC, MCV, MCH, MCHC |

> **⚠️ Önemli:** Bu projede sınıflandırıcı (Decision Tree, Logistic Regression vb.) **kullanılmamaktadır**. Anemi tespiti WHO klinik eşik değerlerine dayalıdır.

---

## ✨ Özellikler

### 🖥️ Streamlit Web Arayüzü
- Modern ve şık tasarım
- Animasyonlu gradient arka plan
- Glassmorphism cam efekti
- Mobil uyumlu responsive tasarım

### 📊 Tahmin ve Analiz
- Hemoglobin değeri tahmini
- Anemi durumu tespiti
- Güven skoru hesaplama
- Benzer vaka analizi

### 📈 Yüzde Tabanlı Metrikler
- **Confidence:** Tahmin güvenilirlik yüzdesi
- **Within ±1 g/dL:** Benzer vakaların %'si
- **Within ±2 g/dL:** Benzer vakaların %'si
- **Match Rate:** Veri setindeki benzer vaka oranı

---

## 🛠 Kurulum

### Gereksinimler

- **Python:** 3.8 veya üzeri
- **İşletim Sistemi:** Windows 10/11 (PowerShell)
- **RAM:** Minimum 4 GB

### Adım 1: Projeyi İndirin

```powershell
# Git ile klonlama (eğer Git kuruluysa)
git clone <repository-url>
cd Kansizlik_Tanisinda_Regresyon

# Veya ZIP dosyasını indirip çıkarın
```

### Adım 2: Python Bağımlılıklarını Yükleyin

PowerShell'i **Yönetici olarak** açın ve aşağıdaki komutları çalıştırın:

```powershell
# Proje dizinine gidin
cd C:\Kansizlik_Tanisinda_Regresyon

# Gerekli paketleri yükleyin
pip install pandas numpy scikit-learn joblib streamlit openpyxl
```

### Tüm Bağımlılıklar

| Paket | Sürüm | Açıklama |
|-------|-------|----------|
| `pandas` | ≥1.3.0 | Veri işleme |
| `numpy` | ≥1.20.0 | Sayısal hesaplamalar |
| `scikit-learn` | ≥1.0.0 | Machine Learning |
| `joblib` | ≥1.0.0 | Model kaydetme/yükleme |
| `streamlit` | ≥1.0.0 | Web arayüzü |
| `openpyxl` | ≥3.0.0 | Excel dosyası okuma |

---

## 🚀 Kullanım

### Yöntem 1: Streamlit Web Arayüzü (Önerilen)

```powershell
# Proje dizinine gidin
cd C:\Kansizlik_Tanisinda_Regresyon

# Modeli eğitin (ilk kez)
python train.py

# Web arayüzünü başlatın
streamlit run app.py
```

Tarayıcınızda otomatik olarak açılacaktır: **http://localhost:8501**

### Yöntem 2: Konsol Arayüzü

```powershell
# Proje dizinine gidin
cd C:\Kansizlik_Tanisinda_Regresyon

# Modeli eğitin (ilk kez)
python train.py

# Tahmin yapın
python predict.py
```

---

## 📁 Proje Yapısı

```
Kansizlik_Tanisinda_Regresyon/
│
├── 📂 data/
│   └── 📊 anemia_new.csv          # Veri seti (1000 kayıt)
│
├── 📂 model/
│   └── 🤖 hemoglobin_model.pkl    # Eğitilmiş model (joblib)
│
├── 🐍 train.py                    # Model eğitim scripti
├── 🐍 predict.py                  # Konsol tahmin scripti
├── 🐍 utils.py                    # Klinik karar fonksiyonları
├── 🐍 app.py                      # Streamlit web arayüzü
│
└── 📄 README.md                   # Bu dosya
```

### Dosya Açıklamaları

| Dosya | Görev |
|-------|-------|
| `train.py` | Veriyi yükler, Linear Regression modeli eğitir, model kaydeder |
| `predict.py` | Konsoldan girdi alır, Hb tahmin eder, anemi durumunu belirler |
| `utils.py` | `anemia_decision()` fonksiyonu - WHO kural tabanlı karar |
| `app.py` | Streamlit web arayüzü - modern tasarım, interaktif kullanım |

---

## 🔬 Teknik Detaylar

### Model Özellikleri

| Parametre | Değer |
|-----------|-------|
| **Algoritma** | Linear Regression (sklearn) |
| **Özellikler** | RBC, MCV, MCH, MCHC |
| **Hedef** | Hb (Hemoglobin) |
| **Train/Test Oranı** | 80% / 20% |
| **Random State** | 42 |
| **Ölçeklendirme** | Yok (StandardScaler kullanılmıyor) |
| **Kaydetme Formatı** | joblib (.pkl) |

### Klinik Karar Kuralları (WHO Standartları)

| Cinsiyet | Eşik Değeri | Karar |
|----------|-------------|-------|
| Erkek (m/male) | Hb < 13 g/dL | **Anemia** |
| Erkek (m/male) | Hb ≥ 13 g/dL | Normal |
| Kadın (f/female) | Hb < 12 g/dL | **Anemia** |
| Kadın (f/female) | Hb ≥ 12 g/dL | Normal |

### Sistem Mimarisi

```
┌─────────────────────────────────────────────────────────────────┐
│                     SİSTEM MİMARİSİ                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐    ┌─────────────────┐    ┌──────────────┐   │
│   │  Kan        │    │  Linear         │    │  Tahmin      │   │
│   │  Değerleri  │───▶│  Regression     │───▶│  Hemoglobin  │   │
│   │  RBC,MCV,   │    │  Modeli         │    │  (g/dL)      │   │
│   │  MCH,MCHC   │    │  (train.py)     │    │              │   │
│   └─────────────┘    └─────────────────┘    └──────┬───────┘   │
│                                                     │           │
│                                                     ▼           │
│                      ┌─────────────────────────────────────┐   │
│                      │  Klinik Karar Kuralı (utils.py)     │   │
│                      │                                     │   │
│                      │  Erkek (m):  Hb < 13 g/dL → Anemi   │   │
│                      │  Kadın (f):  Hb < 12 g/dL → Anemi   │   │
│                      └─────────────────────────────────────┘   │
│                                                     │           │
│                                                     ▼           │
│                      ┌─────────────────────────────────────┐   │
│                      │  Sonuç: "Anemia" veya "Normal"      │   │
│                      └─────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Veri Seti

| Bilgi | Değer |
|-------|-------|
| **Kaynak** | Anemia Dataset (Kaggle) |
| **Format** | CSV |
| **Dosya** | `data/anemia_new.csv` |
| **Toplam Kayıt** | 1000 hasta |
| **Sütun Sayısı** | 9 |

### Veri Seti Sütunları

| Sütun | Açıklama | Kullanım |
|-------|----------|----------|
| **Gender** | Cinsiyet (m: Erkek, f: Kadın) | Sadece klinik karar için |
| **Age** | Yaş | Kullanılmıyor |
| **Hb** | Hemoglobin miktarı (g/dL) | **Hedef (Target)** |
| **RBC** | Kırmızı kan hücresi sayısı | **Özellik (Feature)** ⭐ |
| **PCV** | Packed Cell Volume | Kullanılmıyor |
| **MCV** | Mean Corpuscular Volume (fL) | **Özellik (Feature)** |
| **MCH** | Mean Corpuscular Hemoglobin (pg) | **Özellik (Feature)** |
| **MCHC** | Mean Corpuscular Hb Concentration | **Özellik (Feature)** |
| **Decision_Class** | Anemi etiketi (0/1) | ❌ Kullanılmıyor |

### Girdi Değer Aralıkları

| Parametre | Normal Aralık | Birim |
|-----------|---------------|-------|
| RBC | 2.0 - 7.0 | million cells/mcL |
| MCV | 60 - 120 | fL |
| MCH | 15 - 40 | pg |
| MCHC | 25 - 40 | g/dL |

---

## 📈 Model Performansı

| Metrik | Değer | Açıklama |
|--------|-------|----------|
| **MAE** | 0.47 g/dL | Ortalama mutlak hata |
| **RMSE** | ~0.55 g/dL | Kök ortalama kare hata |
| **R²** | **0.79** | Belirleme katsayısı (%79 açıklama gücü) |

> 💡 **RBC (Kırmızı Kan Hücresi)** özelliğinin eklenmesi model performansını önemli ölçüde artırmıştır!

---

## 🖼 Ekran Görüntüleri

### Streamlit Web Arayüzü

```
┌─────────────────────────────────────────────────────────────────┐
│  🌈 Animated Gradient Background                                │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║  Hemoglobin Prediction & Anemia Diagnosis                 ║  │
│  ║  ─────────────────────────────────────────────────────    ║  │
│  ║                                                           ║  │
│  ║  Enter Blood Parameters                                   ║  │
│  ║  ┌─────────────┐ ┌─────────────┐                          ║  │
│  ║  │ RBC: 4.5    │ │ MCH: 27     │                          ║  │
│  ║  │ MCV: 80     │ │ MCHC: 33    │                          ║  │
│  ║  └─────────────┘ └─────────────┘                          ║  │
│  ║                                                           ║  │
│  ║  Patient Information                                      ║  │
│  ║  ┌───────────────┐ ┌───────────────┐                      ║  │
│  ║  │  👩 Female    │ │  👨 Male      │                      ║  │
│  ║  └───────────────┘ └───────────────┘                      ║  │
│  ║                                                           ║  │
│  ║  [🔬 Predict Hemoglobin]                                  ║  │
│  ║                                                           ║  │
│  ║  ─────────────────────────────────────────────────────    ║  │
│  ║  Results                                                  ║  │
│  ║  Predicted Hemoglobin: 11.93 g/dL                         ║  │
│  ║  Confidence: 85%                                          ║  │
│  ║                                                           ║  │
│  ║  ⚠️ Result: Anemia                                        ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Önemli Uyarılar

### 🏥 Klinik Kullanım Hakkında

> **Bu proje eğitim amaçlıdır** ve gerçek klinik ortamda tek başına kullanılmamalıdır.

Anemi tanısı şunları gerektirir:
- Kapsamlı laboratuvar testleri
- Fiziksel muayene
- Hasta öyküsü
- Uzman hekim değerlendirmesi

### 📋 Tasarım Kısıtlamaları

- Bu projede **sınıflandırıcı kullanılmamaktadır** (Decision Tree, Logistic Regression vb. yok)
- Accuracy, confusion matrix, precision, recall gibi **sınıflandırma metrikleri kullanılmamaktadır**
- Veri setindeki `Decision_Class` sütunu **kullanılmamaktadır**

---

## 🔄 Hızlı Başlangıç (Quick Start)

PowerShell'de aşağıdaki komutları sırayla çalıştırın:

```powershell
# 1. Proje dizinine git
cd C:\Kansizlik_Tanisinda_Regresyon

# 2. Bağımlılıkları yükle
pip install pandas numpy scikit-learn joblib streamlit openpyxl

# 3. Modeli eğit
python train.py

# 4. Web arayüzünü başlat
streamlit run app.py
```

Tarayıcıda açılan **http://localhost:8501** adresinden uygulamayı kullanabilirsiniz.

---

## 📚 Kaynaklar

- [Scikit-learn Linear Regression Documentation](https://scikit-learn.org/stable/modules/linear_model.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [WHO Hemoglobin Thresholds for Anemia](https://www.who.int/vmnis/indicators/haemoglobin.pdf)

---

## 📝 Lisans

Bu proje **eğitim amaçlı** hazırlanmıştır ve akademik kullanım için serbesttir.

---

<div align="center">

**Tıbbi İstatistik ve Tıp Bilişimine Giriş Dersi – Final Projesi**

🩸 *Sağlıklı Günler Dileriz* 🩸

</div>
