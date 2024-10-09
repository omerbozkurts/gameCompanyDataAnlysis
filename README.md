# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

Bu proje, uluslararası bir oyun şirketinin müşterilerinin demografik özelliklerini kullanarak, seviye tabanlı (level-based) yeni müşteri tanımları (persona) oluşturarak ve bu müşteri tanımlarına göre segmentasyon yaparak yeni müşterilerin şirkete ortalama ne kadar kazandırabileceğini tahmin etmeyi amaçlar.

## Dosya Yapısı

- `persona.csv`: Oyun şirketinin sattığı ürünlerin fiyatları ve bu ürünleri satın alan kullanıcıların bazı demografik bilgilerini içeren veri seti.
- `main.py`: Veri seti üzerinde işlem yapan Python kodu. Bu kod, veri analizi, seviye tabanlı müşteri tanımları oluşturma ve segmentasyon işlemlerini gerçekleştirir.
- `Kural_Tabanli_Siniflandirma.pdf`: Proje problemini, veri setini, değişkenleri ve yapılacak görevleri içeren detaylı açıklama dokümanı.

## Proje Hedefi

Bu projede, bir oyun şirketinin müşterilerinin:

- **Cihaz türü (SOURCE)**
- **Cinsiyeti (SEX)**
- **Ülkesi (COUNTRY)**
- **Yaşı (AGE)**

gibi özelliklerini kullanarak yeni müşteri tanımları oluşturulmuş ve bu tanımlara göre müşteri segmentasyonu yapılmıştır. Bu segmentlere göre yeni müşterilerin şirkete ortalama ne kadar kazandırabileceği hesaplanmıştır.

### Veri Seti

`persona.csv` dosyası, her satış işleminde oluşan kayıtlardan meydana gelir. Kullanıcılar birden fazla alışveriş yapabileceğinden, tablo tekilleştirilmemiştir. Veri seti aşağıdaki değişkenleri içerir:

- `PRICE`: Müşterinin harcama tutarı
- `SOURCE`: Müşterinin bağlandığı cihaz türü (Android, iOS)
- `SEX`: Müşterinin cinsiyeti (Male, Female)
- `COUNTRY`: Müşterinin ülkesi (TUR, BRA, USA vb.)
- `AGE`: Müşterinin yaşı

### Proje Adımları

1. **Veri Analizi:** 
   - Veri seti yüklenip incelenmiş, cihaz türlerine, ülkelere ve cinsiyetlere göre satış sayıları ve ortalama fiyatlar hesaplanmıştır.
   - Fiyat ve ülkelere göre segmentasyon yapılmıştır.

2. **Seviye Tabanlı Müşteri Tanımları:**
   - Ülke, cihaz türü, cinsiyet ve yaş bilgilerine göre seviye tabanlı müşteri tanımları (`customers_level_based`) oluşturulmuştur.
   - Bu müşteri tanımları daha sonra segmente edilmiştir.

3. **Segment Analizi:**
   - Fiyatlara göre müşteri segmentleri (`D`, `C`, `B`, `A`) oluşturulmuştur. Bu segmentlerin tanımları yapılmış ve her segmentin ortalama, minimum ve maksimum fiyatları hesaplanmıştır.

4. **Yeni Müşteri Getirisi Tahmini:**
   - Belirli demografik özelliklere sahip yeni müşterilerin hangi segmente dahil oldukları ve ortalama ne kadar gelir getirebilecekleri tahmin edilmiştir.
   
   Örneğin:
   - 33 yaşında Android kullanan bir Türk kadınının hangi segmente ait olduğu ve ortalama gelir kazandırma potansiyeli tahmin edilmiştir.

### Kullanılan Kütüphaneler

`main.py` dosyasında kullanılan Python kütüphaneleri:

- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`

### Kurulum

Projeyi kendi bilgisayarınıza klonlamak için:

```bash
git clone https://github.com/yourusername/kural-tabanli-siniflandirma.git
```

### Gerekli kütüphaneleri yüklemek için:
```bash
pip install pandas numpy seaborn matplotlib
```

### Kullanım
 `persona.csv` dosyasını proje dizinine ekleyin.
 `main.py` dosyasını çalıştırın. Python 3.x versiyonunu kullandığınızdan emin olun.
```bash
python main.py
```
Kod çalıştırıldığında, yeni seviye tabanlı müşteri tanımları oluşturulacak, segmentasyon yapılacak ve belirli müşterilerin tahmini gelirleri hesaplanacaktır.

