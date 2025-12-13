# 🩸 Kansızlık (Anemi) Tanısında Gini Algoritması Kullanımı

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

Bu proje, kan tahlili (CBC - Complete Blood Count) verileri kullanılarak bireylerin **kansız (anemik) olup olmadığının** **Gini indeksi temelli karar ağacı** yöntemiyle sınıflandırılmasını amaçlamaktadır.

Proje, makine öğrenmesi algoritmalarının tıbbi tanı süreçlerinde nasıl kullanılabileceğini göstermek amacıyla tasarlanmıştır.

---

## 🎯 Proje Hedefleri

- ✅ Kan tahlili verilerinden anemi tespiti yapabilmek
- ✅ Gini indeksi tabanlı karar ağacı algoritmasını uygulamak
- ✅ Model performansını değerlendirmek ve yorumlamak
- ✅ Özellik önemlerini analiz etmek
- ✅ Tıbbi karar destek sistemi mantığını anlamak

---

## 📊 Veri Seti

| Bilgi | Değer |
|-------|-------|
| **Kaynak** | [Kaggle – biswaranjanrao/anemia-dataset](https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset) |
| **Format** | CSV |
| **Dosya** | `data/anemia.csv` |
| **Toplam Kayıt** | 1422 hasta |
| **Hedef Değişken** | Result (0 = Sağlıklı, 1 = Anemik) |

### 🔬 Özellikler (Features)

| Özellik | Açıklama | Birim |
|---------|----------|-------|
| **Gender** | Cinsiyet (0: Kadın, 1: Erkek) | Kategorik |
| **Hemoglobin** | Kandaki hemoglobin miktarı | g/dL |
| **MCH** | Mean Corpuscular Hemoglobin - Ortalama eritrosit hemoglobini | pg |
| **MCHC** | Mean Corpuscular Hemoglobin Concentration - Ortalama eritrosit hemoglobin konsantrasyonu | g/dL |
| **MCV** | Mean Corpuscular Volume - Ortalama eritrosit hacmi | fL |

---

## 🛠 Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- pip paket yöneticisi

### Bağımlılıkları Yükleme

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## 🚀 Çalıştırma

```bash
cd Kansizlik_Tanisinda_Gini_Algoritmasi
python src/anemia_analysis.py
```

Çalıştırma sonrasında `data/` klasöründe görsel çıktılar oluşturulacaktır.

---

## 📈 Analiz Akışı & Metodoloji

```
┌─────────────────────────────────────────────────────────────────┐
│                     PROJE ANALİZ AKIŞI                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1️⃣ VERİ YÜKLEME                                                │
│     └── Kaggle veri setinin okunması                            │
│                                                                 │
│  2️⃣ VERİ ÖN İNCELEME                                            │
│     ├── Veri seti boyutu ve değişkenlerin incelenmesi           │
│     └── Hedef değişken dağılımının kontrolü                     │
│                                                                 │
│  3️⃣ ÖN İŞLEME                                                   │
│     ├── Eksik veri kontrolü                                     │
│     └── Kategorik değişkenlerin uygun formata getirilmesi       │
│                                                                 │
│  4️⃣ MODELLEME                                                   │
│     ├── Özellik/hedef değişken ayrımı                           │
│     ├── Train/Test bölünmesi (%70 / %30)                        │
│     └── Gini indeksi temelli karar ağacı eğitimi                │
│                                                                 │
│  5️⃣ PERFORMANS DEĞERLENDİRMESİ                                  │
│     ├── Accuracy (Doğruluk)                                     │
│     ├── Confusion Matrix (Karışıklık Matrisi)                   │
│     ├── Sensitivity / Recall (Duyarlılık)                       │
│     └── Specificity (Özgüllük)                                  │
│                                                                 │
│  6️⃣ GÖRSELLEŞTİRME                                              │
│     ├── Karar ağacı diyagramı                                   │
│     ├── Özellik önemleri grafiği                                │
│     └── Sınıf dağılımı grafiği                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 🧮 Gini İndeksi Nedir?

Gini indeksi, bir veri setindeki homojenliği ölçen bir metriktir. Karar ağaçlarında dallanma kararları için kullanılır:

```
Gini = 1 - Σ(pᵢ)²
```

- **Gini = 0:** Tamamen homojen (tek sınıf)
- **Gini = 0.5:** Maksimum heterojenlik (dengeli dağılım)

---

## 📁 Proje Yapısı

```
Kansizlik_Tanisinda_Gini_Algoritmasi/
│
├── 📂 data/
│   ├── 📊 anemia.csv              # Orijinal veri seti
│   ├── 🖼️ confusion_matrix.png    # Karışıklık matrisi görseli
│   ├── 🌳 karar_agaci.png         # Karar ağacı diyagramı
│   ├── 📈 ozellik_onemleri.png    # Özellik önemleri grafiği
│   └── 📉 sinif_dagilimi.png      # Sınıf dağılımı görseli
│
├── 📂 notebooks/
│   └── 📄 README.md               # Notebook indeks dosyası
│
├── 📂 src/
│   └── 🐍 anemia_analysis.py      # Ana analiz scripti
│
└── 📄 README.md                   # Bu dosya
```

---

## � Çıktılar

Analiz çalıştırıldıktan sonra aşağıdaki görsel çıktılar oluşturulur:

| Dosya | Açıklama |
|-------|----------|
| `confusion_matrix.png` | Modelin tahmin performansını gösteren karışıklık matrisi |
| `karar_agaci.png` | Eğitilmiş karar ağacının görsel diyagramı |
| `ozellik_onemleri.png` | Her özelliğin model için önem derecesi |
| `sinif_dagilimi.png` | Veri setindeki sınıf dağılımı |

---

## 🔍 Performans Metrikleri

| Metrik | Açıklama |
|--------|----------|
| **Accuracy** | Doğru tahminlerin toplam tahminlere oranı |
| **Sensitivity (Recall)** | Gerçek pozitiflerin doğru tespit oranı |
| **Specificity** | Gerçek negatiflerin doğru tespit oranı |
| **Precision** | Pozitif tahminlerin doğruluk oranı |

---

## ⚠️ Önemli Uyarı

> **Bu proje eğitim amaçlı olup karar destek sistemi niteliğindedir.**
> 
> Gerçek klinik tanı süreçlerinde tek başına kullanılmamalıdır. Anemi tanısı, bu modelin çıktılarına ek olarak:
> - Kapsamlı laboratuvar testleri
> - Fiziksel muayene
> - Hasta öyküsü
> - Uzman hekim değerlendirmesi
> 
> gerektirmektedir.

---

## 📚 Kaynaklar

- [Scikit-learn Decision Trees Documentation](https://scikit-learn.org/stable/modules/tree.html)
- [Kaggle Anemia Dataset](https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset)
- [Gini Index - Wikipedia](https://en.wikipedia.org/wiki/Gini_coefficient)

---

## �📝 Lisans

Bu proje **eğitim amaçlı** hazırlanmıştır ve akademik kullanım için serbesttir.

---

<div align="center">

**Tıbbi İstatistik ve Tıp Bilişimine Giriş Dersi – Final Projesi**

🩸 *Sağlıklı Günler Dileriz* 🩸

</div>
