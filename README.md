# 🩸 Hemoglobin Regresyon ile Anemi Tanı Destek Sistemi

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/Lisans-Eğitim%20Amaçlı-green)

**Ders:** Tıbbi İstatistik ve Tıp Bilişimine Giriş  
**Proje Türü:** Final Projesi  
**Tarih:** Aralık 2025

</div>

---

## 📋 Proje Açıklaması

Bu proje, kan tahlili verilerinden **Hemoglobin (Hb)** değerini tahmin etmek için **Linear Regression** modeli kullanır ve tahmin edilen değere göre **klinik kural tabanlı** anemi tespiti yapar.

### 🔑 Temel Özellikler

| Özellik | Açıklama |
|---------|----------|
| **Makine Öğrenmesi** | Sadece Linear Regression (regresyon) |
| **Anemi Tespiti** | Kural tabanlı klinik karar (ML değil) |
| **Hedef Değişken** | Hemoglobin (g/dL) |
| **Özellikler** | MCH, MCHC, MCV |

> **Not:** Bu projede sınıflandırıcı (Decision Tree, Logistic Regression vb.) **kullanılmamaktadır**. Anemi tespiti WHO klinik eşik değerlerine dayalıdır.

---

## 🎯 Proje Hedefleri

- ✅ Kan parametrelerinden Hemoglobin değerini regresyon ile tahmin etmek
- ✅ Tahmin edilen Hb değerine göre klinik kuralla anemi tespiti yapmak
- ✅ Linear Regression modelini uygulamak ve değerlendirmek
- ✅ Regresyon metriklerini (MAE, RMSE, R²) hesaplamak
- ✅ Basit ve anlaşılır bir tıbbi karar destek sistemi oluşturmak

---

## 📊 Veri Seti

| Bilgi | Değer |
|-------|-------|
| **Kaynak** | [Kaggle – biswaranjanrao/anemia-dataset](https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset) |
| **Format** | CSV |
| **Dosya** | `data/anemia.csv` |
| **Toplam Kayıt** | 1421 hasta |

### 🔬 Veri Seti Sütunları

| Sütun | Açıklama | Kullanım |
|-------|----------|----------|
| **Gender** | Cinsiyet (0: Kadın, 1: Erkek) | Sadece klinik karar için |
| **Hemoglobin** | Kandaki hemoglobin miktarı (g/dL) | **Hedef değişken (Target)** |
| **MCH** | Mean Corpuscular Hemoglobin (pg) | **Özellik (Feature)** |
| **MCHC** | Mean Corpuscular Hb Concentration (g/dL) | **Özellik (Feature)** |
| **MCV** | Mean Corpuscular Volume (fL) | **Özellik (Feature)** |
| **Result** | Anemi etiketi (0/1) | ❌ **Kullanılmıyor** |

> **Önemli:** `Result` sütunu veri setinde mevcut ama bu projede **kullanılmamaktadır**. Anemi kararı, tahmin edilen Hemoglobin değerine ve cinsiyete göre klinik kuralla verilir.

---

## 🏗️ Proje Mimarisi

```
┌─────────────────────────────────────────────────────────────────┐
│                     SİSTEM MİMARİSİ                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐    ┌─────────────────┐    ┌──────────────┐   │
│   │  Kan        │    │  Linear         │    │  Tahmin      │   │
│   │  Değerleri  │───▶│  Regression     │───▶│  Hemoglobin  │   │
│   │  MCH,MCHC,  │    │  Modeli         │    │  (g/dL)      │   │
│   │  MCV        │    │  (train.py)     │    │              │   │
│   └─────────────┘    └─────────────────┘    └──────┬───────┘   │
│                                                     │           │
│                                                     ▼           │
│                      ┌─────────────────────────────────────┐   │
│                      │  Klinik Karar Kuralı (utils.py)     │   │
│                      │                                     │   │
│                      │  Erkek:  Hb < 13 g/dL → Anemi       │   │
│                      │  Kadın:  Hb < 12 g/dL → Anemi       │   │
│                      │  Aksi halde       → Normal          │   │
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

## 📁 Proje Yapısı

```
Kansizlik_Tanisinda_Regresyon/
│
├── 📂 data/
│   └── 📊 anemia.csv              # Kaggle veri seti
│
├── 📂 model/
│   └── 🤖 hemoglobin_model.pkl    # Eğitilmiş model (joblib)
│
├── 🐍 train.py                    # Model eğitim scripti
├── 🐍 predict.py                  # Tahmin ve anemi tespiti scripti
├── 🐍 utils.py                    # Klinik karar fonksiyonları
│
└── 📄 README.md                   # Bu dosya
```

### Dosya Sorumlulukları

| Dosya | Görev |
|-------|-------|
| **train.py** | Veriyi yükler, Linear Regression modeli eğitir, model/hemoglobin_model.pkl olarak kaydeder |
| **predict.py** | Modeli yükler, kullanıcıdan girdi alır, Hb tahmin eder, anemi durumunu belirler |
| **utils.py** | `anemia_decision(predicted_hb, gender)` fonksiyonu - klinik kural tabanlı karar |

---

## 🛠 Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- pip paket yöneticisi

### Bağımlılıkları Yükleme

```bash
pip install pandas numpy scikit-learn joblib
```

---

## 🚀 Kullanım

### 1. Modeli Eğitme

```bash
cd Kansizlik_Tanisinda_Regresyon
python train.py
```

**Beklenen Çıktı:**
```
==================================================
  HEMOGLOBIN REGRESSION MODEL TRAINING
==================================================

Dataset loaded: 1421 rows
Data validation passed.
No missing values found.
Features: ['MCH', 'MCHC', 'MCV']
Target: Hemoglobin

Training set: 1136 samples
Test set: 285 samples

Training Linear Regression model...
Training complete.

--------------------------------------------------
  MODEL PERFORMANCE (Test Set)
--------------------------------------------------
  MAE:  1.7256 g/dL
  RMSE: 1.9909 g/dL
  R2:   -0.0125
--------------------------------------------------

Model saved: model\hemoglobin_model.pkl

Training completed successfully!
To make predictions, run: python predict.py
```

### 2. Tahmin Yapma

```bash
python predict.py
```

**Örnek Kullanım:**
```
==================================================
  HEMOGLOBIN PREDICTION & ANEMIA DIAGNOSIS
==================================================

Enter blood parameters:

  MCH (pg): 25
  MCHC (g/dL): 30
  MCV (fL): 85

  Gender (male/female): male

--------------------------------------------------
  RESULTS
--------------------------------------------------
  Predicted Hemoglobin: 13.41 g/dL
  Gender: male
  Threshold: 13.0 g/dL

  Anemia Status: Normal
--------------------------------------------------
```

---

## 🔬 Teknik Detaylar

### Model Özellikleri

| Parametre | Değer |
|-----------|-------|
| **Algoritma** | Linear Regression (sklearn) |
| **Özellikler** | MCH, MCHC, MCV |
| **Hedef** | Hemoglobin |
| **Train/Test Oranı** | 80% / 20% |
| **Random State** | 42 |
| **Ölçeklendirme** | Yok (StandardScaler kullanılmıyor) |
| **Kaydetme Formatı** | joblib (.pkl) |

### Regresyon Metrikleri

| Metrik | Açıklama |
|--------|----------|
| **MAE** | Mean Absolute Error - Ortalama mutlak hata |
| **RMSE** | Root Mean Squared Error - Kök ortalama kare hata |
| **R²** | Coefficient of Determination - Belirleme katsayısı |

### Klinik Karar Kuralları (WHO Standartları)

| Cinsiyet | Eşik Değeri | Karar |
|----------|-------------|-------|
| Erkek (male) | Hb < 13 g/dL | Anemia |
| Erkek (male) | Hb ≥ 13 g/dL | Normal |
| Kadın (female) | Hb < 12 g/dL | Anemia |
| Kadın (female) | Hb ≥ 12 g/dL | Normal |

---

## 📈 Girdi Değer Aralıkları

`predict.py` aşağıdaki aralıklar için uyarı verir:

| Parametre | Normal Aralık | Birim |
|-----------|---------------|-------|
| MCH | 15 - 40 | pg |
| MCHC | 25 - 40 | g/dL |
| MCV | 60 - 120 | fL |

---

## ⚠️ Önemli Uyarılar

> **1. Model Performansı Hakkında**
> 
> R² değerinin düşük olması (≈ 0), mevcut özelliklerin (MCH, MCHC, MCV) tek başına Hemoglobin'i tahmin etmek için yeterli olmadığını gösterir. Gerçek uygulamalarda RBC, RDW gibi ek özellikler gerekebilir.

> **2. Klinik Kullanım Hakkında**
> 
> Bu proje **eğitim amaçlıdır** ve gerçek klinik ortamda tek başına kullanılmamalıdır. Anemi tanısı:
> - Kapsamlı laboratuvar testleri
> - Fiziksel muayene
> - Hasta öyküsü
> - Uzman hekim değerlendirmesi
> 
> gerektirmektedir.

> **3. Tasarım Kısıtlamaları**
> 
> - Bu projede **sınıflandırıcı kullanılmamaktadır** (Decision Tree, Logistic Regression vb. yok)
> - Accuracy, confusion matrix, precision, recall gibi **sınıflandırma metrikleri kullanılmamaktadır**
> - Veri setindeki `Result` sütunu **kullanılmamaktadır**

---

## 🔄 Proje Akışı

```
┌──────────────────────────────────────────────────────────────┐
│                      VERİ AKIŞI                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1️⃣  train.py                                                │
│      │                                                       │
│      ├── data/anemia.csv yükle                               │
│      ├── Eksik veri kontrolü                                 │
│      ├── X = [MCH, MCHC, MCV], y = Hemoglobin                │
│      ├── Train/Test split (80/20)                            │
│      ├── LinearRegression().fit(X_train, y_train)            │
│      ├── MAE, RMSE, R² hesapla                               │
│      └── model/hemoglobin_model.pkl kaydet                   │
│                                                              │
│  2️⃣  predict.py                                              │
│      │                                                       │
│      ├── model/hemoglobin_model.pkl yükle                    │
│      ├── Kullanıcıdan MCH, MCHC, MCV, gender al              │
│      ├── model.predict([MCH, MCHC, MCV]) → predicted_hb      │
│      ├── anemia_decision(predicted_hb, gender) çağır         │
│      └── Sonucu ekrana yazdır                                │
│                                                              │
│  3️⃣  utils.py                                                │
│      │                                                       │
│      └── anemia_decision(predicted_hb, gender):              │
│          • male & Hb < 13  → "Anemia"                        │
│          • female & Hb < 12 → "Anemia"                       │
│          • else            → "Normal"                        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📚 Kaynaklar

- [Scikit-learn Linear Regression Documentation](https://scikit-learn.org/stable/modules/linear_model.html)
- [Kaggle Anemia Dataset](https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset)
- [WHO Hemoglobin Thresholds for Anemia](https://www.who.int/vmnis/indicators/haemoglobin.pdf)

---

## 📝 Lisans

Bu proje **eğitim amaçlı** hazırlanmıştır ve akademik kullanım için serbesttir.

---

<div align="center">

**Tıbbi İstatistik ve Tıp Bilişimine Giriş Dersi – Final Projesi**

🩸 *Sağlıklı Günler Dileriz* 🩸

</div>
