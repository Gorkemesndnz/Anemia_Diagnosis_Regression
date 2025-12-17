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

Bu bölüm, projeyi sıfırdan kurmak için gereken tüm adımları detaylı şekilde açıklamaktadır.

### 📋 Gereksinimler

| Gereksinim | Minimum | Önerilen |
|------------|---------|----------|
| **Python** | 3.8 | 3.10+ |
| **pip** | 21.0 | En son sürüm |
| **İşletim Sistemi** | Windows 10 | Windows 11 |
| **RAM** | 4 GB | 8 GB |
| **Disk Alanı** | 500 MB | 1 GB |

---

### 📥 Adım 1: Projeyi İndirin

#### Yöntem A: Git ile Klonlama (Önerilen)

```powershell
# Git kurulu değilse: https://git-scm.com/download/win adresinden indirin

# Projeyi klonlayın
git clone https://github.com/Gorkemesndnz/Anemia_Diagnosis_Regression.git

# Proje dizinine gidin
cd Anemia_Diagnosis_Regression
```

#### Yöntem B: ZIP Dosyası İndirme

1. GitHub sayfasında yeşil **"Code"** butonuna tıklayın
2. **"Download ZIP"** seçeneğini seçin
3. İndirilen ZIP dosyasını **C:\** dizinine çıkarın
4. Klasör adını `Kansizlik_Tanisinda_Regresyon` olarak değiştirin

---

### 🐍 Adım 2: Python Kurulumunu Kontrol Edin

PowerShell'i açın ve Python'un kurulu olduğunu doğrulayın:

```powershell
# Python sürümünü kontrol edin
python --version
```

**Beklenen Çıktı:** `Python 3.8.x` veya üzeri

> ⚠️ **Python kurulu değilse:**  
> 1. https://www.python.org/downloads/ adresine gidin  
> 2. "Download Python 3.x.x" butonuna tıklayın  
> 3. Kurulum sırasında **"Add Python to PATH"** seçeneğini işaretleyin ✅  
> 4. Kurulumu tamamlayın ve PowerShell'i yeniden başlatın

---

### ⬆️ Adım 3: pip'i Güncelleyin (Önemli!)

Eski pip sürümleri paket yükleme hatalarına neden olabilir. Mutlaka güncelleyin:

```powershell
# pip'i en son sürüme güncelleyin
python -m pip install --upgrade pip

# Güncellemeyi doğrulayın
pip --version
```

**Beklenen Çıktı:** `pip 23.x.x` veya üzeri

---

### 🗂️ Adım 4: Sanal Ortam Oluşturun (Önerilen)

Sanal ortam, proje bağımlılıklarını sistemdeki diğer Python projelerinden izole eder:

```powershell
# Proje dizinine gidin
cd C:\Kansizlik_Tanisinda_Regresyon

# Sanal ortam oluşturun
python -m venv venv

# Sanal ortamı etkinleştirin (Windows PowerShell)
.\venv\Scripts\Activate.ps1
```

> 💡 **Not:** Sanal ortam aktifken PowerShell'de `(venv)` öneki görünür.

> ⚠️ **PowerShell Yetki Hatası Alırsanız:**
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Komutu çalıştırın ve tekrar deneyin.

---

### 📦 Adım 5: Bağımlılıkları Yükleyin

#### Yöntem A: requirements.txt ile (Önerilen)

```powershell
# Tüm bağımlılıkları tek seferde yükleyin
pip install -r requirements.txt
```

#### Yöntem B: Manuel Kurulum

```powershell
# Her paketi tek tek yükleyin
pip install pandas>=1.3.0
pip install numpy>=1.20.0
pip install scikit-learn>=1.0.0
pip install joblib>=1.0.0
pip install streamlit>=1.0.0
pip install openpyxl>=3.0.0
```

#### Yöntem C: Tek Satırda Kurulum

```powershell
pip install pandas numpy scikit-learn joblib streamlit openpyxl
```

---

### ✅ Adım 6: Kurulumu Doğrulayın

Tüm paketlerin doğru yüklendiğini kontrol edin:

```powershell
# Yüklü paketleri listeleyin
pip list

# Veya belirli paketleri kontrol edin
python -c "import pandas; import numpy; import sklearn; import streamlit; print('Tüm paketler başarıyla yüklendi!')"
```

---

### 📊 Bağımlılık Tablosu

| Paket | Minimum Sürüm | Açıklama | Kurulum Komutu |
|-------|---------------|----------|----------------|
| `pandas` | 1.3.0 | Veri işleme ve DataFrame | `pip install pandas` |
| `numpy` | 1.20.0 | Sayısal hesaplamalar | `pip install numpy` |
| `scikit-learn` | 1.0.0 | Machine Learning algoritmaları | `pip install scikit-learn` |
| `joblib` | 1.0.0 | Model kaydetme/yükleme | `pip install joblib` |
| `streamlit` | 1.0.0 | Web arayüzü framework'ü | `pip install streamlit` |
| `openpyxl` | 3.0.0 | Excel dosyası okuma | `pip install openpyxl` |

---

### 🔧 Sık Karşılaşılan Hatalar ve Çözümleri

#### ❌ Hata 1: `'python' is not recognized`
**Çözüm:** Python PATH'e eklenmemiş.
```powershell
# Python yolunu manuel ekleyin veya Python'u yeniden kurun
# Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin
```

#### ❌ Hata 2: `pip is not recognized`
**Çözüm:** pip kurulu değil veya PATH'te yok.
```powershell
# Python ile pip'i çağırın
python -m pip install --upgrade pip
```

#### ❌ Hata 3: `Permission denied` veya `Access denied`
**Çözüm:** PowerShell'i Yönetici olarak çalıştırın.
```powershell
# Başlat menüsünde PowerShell'e sağ tıklayın
# "Yönetici olarak çalıştır" seçin
```

#### ❌ Hata 4: `ModuleNotFoundError: No module named 'xxx'`
**Çözüm:** İlgili modül yüklenmemiş.
```powershell
# Eksik modülü yükleyin
pip install <modül_adı>
```

#### ❌ Hata 5: `ERROR: Could not install packages due to an EnvironmentError`
**Çözüm:** pip önbelleğini temizleyin ve tekrar deneyin.
```powershell
pip cache purge
pip install <paket_adı> --no-cache-dir
```

#### ❌ Hata 6: Streamlit başlatılamıyor
**Çözüm:** Önce modeli eğitin.
```powershell
python train.py
streamlit run app.py
```

---

### 🚀 Hızlı Kurulum Özeti

Tüm adımları tek seferde çalıştırmak için:

```powershell
# 1. Proje dizinine git
cd C:\Kansizlik_Tanisinda_Regresyon

# 2. pip'i güncelle
python -m pip install --upgrade pip

# 3. Sanal ortam oluştur ve aktifleştir
python -m venv venv
.\venv\Scripts\Activate.ps1

# 4. Bağımlılıkları yükle
pip install pandas numpy scikit-learn joblib streamlit openpyxl

# 5. Modeli eğit
python train.py

# 6. Uygulamayı başlat
streamlit run app.py
```

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
