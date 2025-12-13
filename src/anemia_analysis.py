"""
Kansızlık (Anemi) Tanısında Gini Algoritması Kullanımı
======================================================
Tıbbi İstatistik ve Tıp Bilişimine Giriş - Final Projesi

Bu script, CBC (Complete Blood Count) verilerini kullanarak
Gini indeksi temelli karar ağacı ile anemi sınıflandırması yapar.

Yazar: [İsminizi buraya yazın]
Tarih: Aralık 2025
"""

# =============================================================================
# 1. KÜTÜPHANELER
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    recall_score
)
import warnings
warnings.filterwarnings('ignore')

# Görselleştirme ayarları
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
sns.set_style("whitegrid")

# =============================================================================
# 2. VERİ SETİNİN YÜKLENMESİ VE GENEL TANITIMI
# =============================================================================
print("=" * 70)
print("KANSIZLIK (ANEMİ) TANISINDA GİNİ ALGORİTMASI KULLANIMI")
print("=" * 70)
print("\n1. VERİ SETİNİN YÜKLENMESİ VE GENEL TANITIMI")
print("-" * 50)

# Veri setini yükle
df = pd.read_csv("data/anemia.csv")

# İlk 5 satırı göster
print("\n📊 Veri Setinin İlk 5 Satırı:")
print(df.head())

# Veri seti boyutları
print(f"\n📐 Veri Seti Boyutu: {df.shape[0]} satır, {df.shape[1]} sütun")

# Sütun isimleri
print(f"\n📋 Özellikler (Sütunlar): {list(df.columns)}")

# İstatistiksel özet
print("\n📈 Sayısal Değişkenlerin İstatistiksel Özeti:")
print(df.describe())

# Hedef değişken dağılımı
print("\n🎯 Hedef Değişken (Result) Dağılımı:")
print(df['Result'].value_counts())
print(f"\n   0 = Sağlıklı: {(df['Result'] == 0).sum()} kişi ({(df['Result'] == 0).mean()*100:.1f}%)")
print(f"   1 = Anemik:  {(df['Result'] == 1).sum()} kişi ({(df['Result'] == 1).mean()*100:.1f}%)")

# =============================================================================
# 3. EKSİK VERİ VE VERİ TİPİ KONTROLÜ
# =============================================================================
print("\n" + "=" * 70)
print("2. EKSİK VERİ VE VERİ TİPİ KONTROLÜ")
print("-" * 50)

# Veri tipleri
print("\n📊 Veri Tipleri:")
print(df.dtypes)

# Eksik veri kontrolü
print("\n❓ Eksik Veri Sayısı (Her Sütun İçin):")
missing_values = df.isnull().sum()
print(missing_values)

if missing_values.sum() == 0:
    print("\n✅ Veri setinde eksik değer bulunmamaktadır.")
else:
    print(f"\n⚠️ Toplam {missing_values.sum()} eksik değer tespit edildi.")

# =============================================================================
# 4. ÖN İŞLEME ADIMLARI
# =============================================================================
print("\n" + "=" * 70)
print("3. ÖN İŞLEME ADIMLARI")
print("-" * 50)

# Gender sütunu zaten sayısal (0 ve 1) olarak kodlanmış
print("\n📌 Gender değişkeni kontrolü:")
print(f"   Benzersiz değerler: {df['Gender'].unique()}")
print(f"   Gender zaten sayısal formatta (0: Kadın, 1: Erkek)")

# Veri setinin son hali
print("\n📋 İşlenmiş Veri Seti:")
print(df.info())

# =============================================================================
# 5. ÖZELLİKLER (X) VE HEDEF DEĞİŞKENİN (y) AYRILMASI
# =============================================================================
print("\n" + "=" * 70)
print("4. ÖZELLİKLER VE HEDEF DEĞİŞKENİN AYRILMASI")
print("-" * 50)

# Özellikler (bağımsız değişkenler)
X = df.drop('Result', axis=1)

# Hedef değişken (bağımlı değişken)
y = df['Result']

print(f"\n📊 Özellik Matrisi (X) Boyutu: {X.shape}")
print(f"🎯 Hedef Vektör (y) Boyutu: {y.shape}")
print(f"\n📋 Kullanılan Özellikler: {list(X.columns)}")

# =============================================================================
# 6. TRAIN/TEST AYIRIMI (%70/%30)
# =============================================================================
print("\n" + "=" * 70)
print("5. EĞİTİM VE TEST SETİ AYIRIMI")
print("-" * 50)

# Veriyi eğitim (%70) ve test (%30) olarak böl
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.30,  # %30 test
    random_state=42,  # Tekrarlanabilirlik için
    stratify=y  # Sınıf dengesini koru
)

print(f"\n📊 Eğitim Seti Boyutu: {X_train.shape[0]} örnek ({X_train.shape[0]/len(df)*100:.1f}%)")
print(f"📊 Test Seti Boyutu: {X_test.shape[0]} örnek ({X_test.shape[0]/len(df)*100:.1f}%)")

print(f"\n🎯 Eğitim Setinde Sınıf Dağılımı:")
print(f"   Sağlıklı (0): {(y_train == 0).sum()}")
print(f"   Anemik (1): {(y_train == 1).sum()}")

print(f"\n🎯 Test Setinde Sınıf Dağılımı:")
print(f"   Sağlıklı (0): {(y_test == 0).sum()}")
print(f"   Anemik (1): {(y_test == 1).sum()}")

# =============================================================================
# 7. GİNİ ALGORİTMASINA DAYALI KARAR AĞACI MODELİ
# =============================================================================
print("\n" + "=" * 70)
print("6. GİNİ TABANLI KARAR AĞACI MODELİ EĞİTİMİ")
print("-" * 50)

# Karar ağacı modeli oluştur (Gini kriteri ile)
model = DecisionTreeClassifier(
    criterion='gini',  # Gini indeksi kullan
    random_state=42,
    max_depth=5  # Görselleştirme için makul derinlik
)
#Bu satırda karar ağacının bölünme kriteri olarak Gini saflık ölçütü seçilmiştir.
#Model, her düğümde Gini değerini minimize eden bölünmeyi otomatik olarak belirler.


# Modeli eğit
model.fit(X_train, y_train)

print("\n✅ Model başarıyla eğitildi!")
print(f"\n📊 Model Parametreleri:")
print(f"   Kriter: {model.criterion}")
print(f"   Maksimum Derinlik: {model.max_depth}")
print(f"   Ağaç Derinliği: {model.get_depth()}")
print(f"   Yaprak Sayısı: {model.get_n_leaves()}")

# Tahmin yap
y_pred = model.predict(X_test)

# =============================================================================
# 8. MODEL PERFORMANS DEĞERLENDİRMESİ
# =============================================================================
print("\n" + "=" * 70)
print("7. MODEL PERFORMANS DEĞERLENDİRMESİ")
print("-" * 50)

# Accuracy (Doğruluk)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n📈 Accuracy (Doğruluk): {accuracy:.4f} ({accuracy*100:.2f}%)")

# Confusion Matrix (Karışıklık Matrisi)
cm = confusion_matrix(y_test, y_pred)
print("\n📊 Confusion Matrix (Karışıklık Matrisi):")
print(f"   TN (True Negative)  = {cm[0,0]}")
print(f"   FP (False Positive) = {cm[0,1]}")
print(f"   FN (False Negative) = {cm[1,0]}")
print(f"   TP (True Positive)  = {cm[1,1]}")

# Sensitivity (Duyarlılık / Recall) - Anemik olanları doğru tespit etme oranı
sensitivity = recall_score(y_test, y_pred, pos_label=1)
print(f"\n🎯 Sensitivity (Duyarlılık/Recall): {sensitivity:.4f} ({sensitivity*100:.2f}%)")
print("   → Gerçekten anemik olanların ne kadarı doğru tespit edildi?")

# Specificity (Özgüllük) - Sağlıklı olanları doğru tespit etme oranı
specificity = cm[0,0] / (cm[0,0] + cm[0,1])
print(f"\n🎯 Specificity (Özgüllük): {specificity:.4f} ({specificity*100:.2f}%)")
print("   → Gerçekten sağlıklı olanların ne kadarı doğru tespit edildi?")

# Detaylı sınıflandırma raporu
print("\n📋 Detaylı Sınıflandırma Raporu:")
print(classification_report(y_test, y_pred, target_names=['Sağlıklı (0)', 'Anemik (1)']))

# Özellik önemleri
print("\n📊 Özellik Önemleri (Feature Importance):")
feature_importance = pd.DataFrame({
    'Özellik': X.columns,
    'Önem': model.feature_importances_
}).sort_values('Önem', ascending=False)
print(feature_importance.to_string(index=False))

# =============================================================================
# 9. GÖRSELLEŞTİRMELER
# =============================================================================
print("\n" + "=" * 70)
print("8. GÖRSELLEŞTİRMELER")
print("-" * 50)

# --- Görsel 1: Confusion Matrix Heatmap ---
plt.figure(figsize=(8, 6))
sns.heatmap(
    cm, 
    annot=True, 
    fmt='d', 
    cmap='Blues',
    xticklabels=['Sağlıklı (0)', 'Anemik (1)'],
    yticklabels=['Sağlıklı (0)', 'Anemik (1)'],
    annot_kws={'size': 16}
)
plt.title('Confusion Matrix (Karışıklık Matrisi)', fontsize=14, fontweight='bold')
plt.xlabel('Tahmin Edilen', fontsize=12)
plt.ylabel('Gerçek Değer', fontsize=12)
plt.tight_layout()
plt.savefig('data/confusion_matrix.png', dpi=150, bbox_inches='tight')
print("\n✅ Confusion Matrix görselleştirmesi kaydedildi: data/confusion_matrix.png")
plt.close()

# --- Görsel 2: Karar Ağacı ---
plt.figure(figsize=(20, 12))
plot_tree(
    model,
    feature_names=list(X.columns),
    class_names=['Sağlıklı', 'Anemik'],
    filled=True,
    rounded=True,
    fontsize=10,
    proportion=True
)
plt.title('Gini Tabanlı Karar Ağacı - Anemi Sınıflandırması', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('data/karar_agaci.png', dpi=150, bbox_inches='tight')
print("✅ Karar Ağacı görselleştirmesi kaydedildi: data/karar_agaci.png")
plt.close()

# --- Görsel 3: Özellik Önemleri Bar Chart ---
plt.figure(figsize=(10, 6))
colors = sns.color_palette("viridis", len(feature_importance))
bars = plt.barh(feature_importance['Özellik'], feature_importance['Önem'], color=colors)
plt.xlabel('Önem Skoru', fontsize=12)
plt.ylabel('Özellik', fontsize=12)
plt.title('Özellik Önemleri (Feature Importance)', fontsize=14, fontweight='bold')
plt.gca().invert_yaxis()

# Değerleri barların üzerine yaz
for bar, val in zip(bars, feature_importance['Önem']):
    plt.text(val + 0.01, bar.get_y() + bar.get_height()/2, 
             f'{val:.3f}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('data/ozellik_onemleri.png', dpi=150, bbox_inches='tight')
print("✅ Özellik Önemleri görselleştirmesi kaydedildi: data/ozellik_onemleri.png")
plt.close()

# --- Görsel 4: Hedef Değişken Dağılımı ---
plt.figure(figsize=(8, 6))
colors = ['#2ecc71', '#e74c3c']
plt.pie(
    df['Result'].value_counts(), 
    labels=['Sağlıklı', 'Anemik'],
    autopct='%1.1f%%',
    colors=colors,
    explode=(0, 0.05),
    shadow=True,
    startangle=90
)
plt.title('Veri Setindeki Sınıf Dağılımı', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('data/sinif_dagilimi.png', dpi=150, bbox_inches='tight')
print("✅ Sınıf Dağılımı görselleştirmesi kaydedildi: data/sinif_dagilimi.png")
plt.close()

# =============================================================================
# 10. SONUÇ VE YORUM
# =============================================================================
print("\n" + "=" * 70)
print("9. SONUÇ VE YORUMLAMA")
print("=" * 70)

print("""
📌 TIBBI VE İSTATİSTİKSEL YORUM:

1. MODEL PERFORMANSI:
   - Model, %{:.2f} doğruluk oranı ile anemi tahmininde başarılı sonuçlar vermiştir.
   - Sensitivity (Duyarlılık): %{:.2f} - Anemik hastaların büyük çoğunluğu 
     doğru şekilde tespit edilmiştir.
   - Specificity (Özgüllük): %{:.2f} - Sağlıklı bireylerin büyük çoğunluğu
     yanlışlıkla anemik olarak etiketlenmemiştir.

2. EN ÖNEMLİ DEĞİŞKEN:
   - Hemoglobin değeri, anemi tanısında en belirleyici faktör olarak öne çıkmaktadır.
   - Bu, tıbbi literatür ile uyumludur (anemi tanısı genellikle düşük Hb değerine dayanır).

3. KLİNİK ANLAM:
   - Gini tabanlı karar ağacı, yorumlanabilir ve şeffaf bir model sunmaktadır.
   - Karar kuralları, klinisyenler tarafından kolayca anlaşılabilir.

4. LİMİTASYONLAR:
   - Model sadece verilen özellikler ile sınırlıdır.
   - Gerçek klinik uygulamada ek laboratuvar testleri gerekebilir.

5. GELECEKTE YAPILABİLECEK ÇALIŞMALAR:
   - Farklı sınıflandırma algoritmaları ile karşılaştırma (Random Forest, SVM vb.)
   - Çapraz doğrulama (Cross-Validation) ile model güvenilirliğinin artırılması
   - Daha fazla özellik eklenerek model performansının iyileştirilmesi
""".format(accuracy*100, sensitivity*100, specificity*100))

print("\n" + "=" * 70)
print("ANALİZ TAMAMLANDI!")
print("=" * 70)
print("\n📁 Oluşturulan Dosyalar:")
print("   • data/confusion_matrix.png")
print("   • data/karar_agaci.png")
print("   • data/ozellik_onemleri.png")
print("   • data/sinif_dagilimi.png")
