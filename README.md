Kullanıcı Arayüzü

1. Ürün Ekleme:
Ürün Adı: Menüye eklemek istediğiniz ürünün adı.
Fiyat: Ürünün fiyatı.
Stok: Ürünün stok miktarı.
Ürünü eklemek için "Ürün Ekle" butonuna tıklayın.
2. Ürün Güncelleme:
Ürünün fiyatını ve stok durumunu güncelleyebilirsiniz.
3. Ürün Silme:
Menüdeki bir ürünü silmek için ürün adını girin ve "Ürün Sil" butonuna tıklayın.
4. Sipariş Oluşturma:
Müşteri Adı: Siparişi veren müşteri adı.
Adres: Siparişin teslim edileceği adres.
Ürünler: Sipariş edilecek ürünlerin adlarını virgülle ayırarak girin.
Siparişi oluşturmak için "Sipariş Oluştur" butonuna tıklayın.
5. Sipariş Listeleme:
Sistemdeki tüm siparişler listelenir. Bu listeyi görüntülemek için "Siparişleri Listele" butonuna tıklayın.
Kod Yapısı

1. Urun Sınıfı:
Özellikler:
ad: Ürün adı.
fiyat: Ürünün fiyatı.
stok: Ürünün mevcut stok durumu.
Metodlar:
__init__(self, ad, fiyat, stok): Ürün oluşturma.
2. Siparis Sınıfı:
Özellikler:
siparis_no: Sipariş numarası.
urunler: Sipariş edilen ürünler.
musteri_ad: Müşteri adı.
musteri_adres: Müşteri adresi.
Metodlar:
__init__(self, siparis_no, urunler, musteri_ad, musteri_adres): Sipariş oluşturma.
3. RestoranSistemi Sınıfı:
Özellikler:
urunler: Restoranın ürün listesi.
siparisler: Verilen siparişler.
siparis_no: Sipariş numarasını takip eder.
Metodlar:
urun_ekle(self, urun): Yeni bir ürün ekler.
urun_guncelle(self, urun_adi, yeni_fiyat, yeni_stok): Var olan ürünü günceller.
urun_sil(self, urun_adi): Ürünü siler.
siparis_olustur(self, urunler, musteri_ad, musteri_adres): Yeni bir sipariş oluşturur.
urun_listele(self): Menüdeki tüm ürünleri listeler.
siparis_listele(self): Verilen tüm siparişleri listeler.

