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
| **Hedef Değişken** | Hb - Hemoglobin (g/dL) |
| **Özellikler** | RBC, MCV, MCH, MCHC |

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
| **Kaynak** | Anemia Dataset (Excel) |
| **Format** | CSV (Excel'den dönüştürülmüş) |
| **Dosya** | `data/anemia_new.csv` |
| **Toplam Kayıt** | 1000 hasta |

### 🔬 Veri Seti Sütunları

| Sütun | Açıklama | Kullanım |
|-------|----------|----------|
| **Gender** | Cinsiyet (m: Erkek, f: Kadın) | Sadece klinik karar için |
| **Age** | Yaş | Kullanılmıyor |
| **Hb** | Hemoglobin miktarı (g/dL) | **Hedef değişken (Target)** |
| **RBC** | Red Blood Cell - Kırmızı kan hücresi sayısı | **Özellik (Feature)** ⭐ |
| **PCV** | Packed Cell Volume | Kullanılmıyor |
| **MCV** | Mean Corpuscular Volume (fL) | **Özellik (Feature)** |
| **MCH** | Mean Corpuscular Hemoglobin (pg) | **Özellik (Feature)** |
| **MCHC** | Mean Corpuscular Hb Concentration (g/dL) | **Özellik (Feature)** |
| **Decision_Class** | Anemi etiketi (0/1) | ❌ **Kullanılmıyor** |

> **Önemli:** `Decision_Class` sütunu veri setinde mevcut ama bu projede **kullanılmamaktadır**. Anemi kararı, tahmin edilen Hemoglobin değerine ve cinsiyete göre klinik kuralla verilir.

---

## 📈 Model Performansı

| Metrik | Değer | Açıklama |
|--------|-------|----------|
| **MAE** | 0.47 g/dL | Ortalama mutlak hata |
| **RMSE** | ~0.55 g/dL | Kök ortalama kare hata |
| **R²** | **0.79** | Belirleme katsayısı (%79 açıklama gücü) |

> 💡 **RBC (Kırmızı Kan Hücresi)** özelliğinin eklenmesi model performansını önemli ölçüde artırmıştır!

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
│                      │  Aksi halde          → Normal       │   │
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
│   └── 📊 anemia_new.csv          # Veri seti (1000 kayıt)
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
| **train.py** | Veriyi yükler, Linear Regression modeli eğitir, model kaydeder |
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
============================================================
  HEMOGLOBIN REGRESSION MODEL TRAINING
============================================================

Dataset loaded: 1000 rows
Data validation passed.
No missing values found.
Features: ['RBC', 'MCV', 'MCH', 'MCHC']
Target: Hb

Training set: 800 samples
Test set: 200 samples

Training Linear Regression model...
Training complete.

------------------------------------------------------------
  MODEL PERFORMANCE (Test Set)
------------------------------------------------------------
  MAE:  0.4724 g/dL
  RMSE: 0.5512 g/dL
  R2:   0.7888
------------------------------------------------------------

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
============================================================
  HEMOGLOBIN PREDICTION & ANEMIA DIAGNOSIS
============================================================

Enter blood parameters:

  RBC (million cells/mcL): 4.5
  MCV (fL): 80
  MCH (pg): 27
  MCHC (g/dL): 33

  Gender (m/f or male/female): f

------------------------------------------------------------
  RESULTS
------------------------------------------------------------
  Predicted Hemoglobin: 11.93 g/dL
  Gender: female
  Threshold: 12.0 g/dL

  Anemia Status: ** Anemia **
  (Hemoglobin is below 12.0 g/dL for female)
------------------------------------------------------------
```

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

### Regresyon Metrikleri

| Metrik | Açıklama |
|--------|----------|
| **MAE** | Mean Absolute Error - Ortalama mutlak hata |
| **RMSE** | Root Mean Squared Error - Kök ortalama kare hata |
| **R²** | Coefficient of Determination - Belirleme katsayısı |

### Klinik Karar Kuralları (WHO Standartları)

| Cinsiyet | Eşik Değeri | Karar |
|----------|-------------|-------|
| Erkek (m/male) | Hb < 13 g/dL | Anemia |
| Erkek (m/male) | Hb ≥ 13 g/dL | Normal |
| Kadın (f/female) | Hb < 12 g/dL | Anemia |
| Kadın (f/female) | Hb ≥ 12 g/dL | Normal |

---

## 📈 Girdi Değer Aralıkları

`predict.py` aşağıdaki aralıklar için uyarı verir:

| Parametre | Normal Aralık | Birim |
|-----------|---------------|-------|
| RBC | 2.0 - 7.0 | million cells/mcL |
| MCV | 60 - 120 | fL |
| MCH | 15 - 40 | pg |
| MCHC | 25 - 40 | g/dL |

---

## ⚠️ Önemli Uyarılar

> **1. Klinik Kullanım Hakkında**
> 
> Bu proje **eğitim amaçlıdır** ve gerçek klinik ortamda tek başına kullanılmamalıdır. Anemi tanısı:
> - Kapsamlı laboratuvar testleri
> - Fiziksel muayene
> - Hasta öyküsü
> - Uzman hekim değerlendirmesi
> 
> gerektirmektedir.

> **2. Tasarım Kısıtlamaları**
> 
> - Bu projede **sınıflandırıcı kullanılmamaktadır** (Decision Tree, Logistic Regression vb. yok)
> - Accuracy, confusion matrix, precision, recall gibi **sınıflandırma metrikleri kullanılmamaktadır**
> - Veri setindeki `Decision_Class` sütunu **kullanılmamaktadır**

---

## 🔄 Proje Akışı

```
┌──────────────────────────────────────────────────────────────┐
│                      VERİ AKIŞI                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1️⃣  train.py                                                │
│      │                                                       │
│      ├── data/anemia_new.csv yükle                           │
│      ├── Eksik veri kontrolü                                 │
│      ├── X = [RBC, MCV, MCH, MCHC], y = Hb                   │
│      ├── Train/Test split (80/20)                            │
│      ├── LinearRegression().fit(X_train, y_train)            │
│      ├── MAE, RMSE, R² hesapla                               │
│      └── model/hemoglobin_model.pkl kaydet                   │
│                                                              │
│  2️⃣  predict.py                                              │
│      │                                                       │
│      ├── model/hemoglobin_model.pkl yükle                    │
│      ├── Kullanıcıdan RBC, MCV, MCH, MCHC, gender al         │
│      ├── model.predict([RBC, MCV, MCH, MCHC]) → predicted_hb │
│      ├── anemia_decision(predicted_hb, gender) çağır         │
│      └── Sonucu ekrana yazdır                                │
│                                                              │
│  3️⃣  utils.py                                                │
│      │                                                       │
│      └── anemia_decision(predicted_hb, gender):              │
│          • male (m) & Hb < 13  → "Anemia"                    │
│          • female (f) & Hb < 12 → "Anemia"                   │
│          • else                → "Normal"                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📚 Kaynaklar

- [Scikit-learn Linear Regression Documentation](https://scikit-learn.org/stable/modules/linear_model.html)
- [WHO Hemoglobin Thresholds for Anemia](https://www.who.int/vmnis/indicators/haemoglobin.pdf)

---

## 📝 Lisans

Bu proje **eğitim amaçlı** hazırlanmıştır ve akademik kullanım için serbesttir.

---

<div align="center">

**Tıbbi İstatistik ve Tıp Bilişimine Giriş Dersi – Final Projesi**

🩸 *Sağlıklı Günler Dileriz* 🩸

</div>
