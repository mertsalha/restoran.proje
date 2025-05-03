import tkinter as tk
from tkinter import messagebox


class Urun:
    def __init__(self, ad, fiyat, stok):
        self.ad = ad
        self.fiyat = fiyat
        self.stok = stok

    def __str__(self):
        return f"{self.ad} - {self.fiyat} TL (Stok: {self.stok})"


class Musteri:
    def __init__(self, ad, adres):
        self.ad = ad
        self.adres = adres
        self.siparis_gecmisi = []

    def siparis_ekle(self, siparis):
        self.siparis_gecmisi.append(siparis)


class Siparis:
    sayac = 1

    def __init__(self, musteri, urunler):
        self.siparis_no = Siparis.sayac
        Siparis.sayac += 1
        self.musteri = musteri
        self.urunler = urunler  
        self.toplam = sum(u.fiyat * miktar for u, miktar in urunler)

    def __str__(self):
        urunler_str = "\n".join([f"{u.ad} x{miktar}" for u, miktar in self.urunler])
        return f"Sipariş No: {self.siparis_no}\nMüşteri: {self.musteri.ad}\n{urunler_str}\nToplam: {self.toplam} TL"

# Başlangıç verisi
menu = [
    Urun("Lahmacun", 40, 10),
    Urun("Ayran", 10, 20),
    Urun("Kebap", 80, 5)
]

siparisler = []

# Arayüz fonksiyonları
def siparis_olustur():
    secilenler = []
    for i, entry in enumerate(miktar_girisleri):
        try:
            miktar = int(entry.get())
            if miktar > 0:
                if miktar <= menu[i].stok:
                    secilenler.append((menu[i], miktar))
                else:
                    messagebox.showerror("Hata", f"{menu[i].ad} için yeterli stok yok!")
                    return
        except ValueError:
            continue

    if not secilenler:
        messagebox.showwarning("Uyarı", "Hiç ürün seçilmedi!")
        return

    musteri = Musteri(ad_entry.get(), adres_entry.get())
    siparis = Siparis(musteri, secilenler)
    musteri.siparis_ekle(siparis)
    siparisler.append(siparis)

    for urun, miktar in secilenler:
        urun.stok -= miktar

    messagebox.showinfo("Başarılı", f"Sipariş oluşturuldu!\n{siparis}")
    siparis_listele()

def siparis_listele():
    text.delete(1.0, tk.END)
    for sip in siparisler:
        text.insert(tk.END, str(sip) + "\n" + "-"*40 + "\n")


def urun_ekle():
    urun_ad = urun_ad_entry.get()
    urun_fiyat = urun_fiyat_entry.get()
    urun_stok = urun_stok_entry.get()

    try:
        urun_fiyat = float(urun_fiyat)
        urun_stok = int(urun_stok)
        yeni_urun = Urun(urun_ad, urun_fiyat, urun_stok)
        menu.append(yeni_urun)
        messagebox.showinfo("Başarılı", f"{urun_ad} menüye eklendi.")
        urun_listele()
    except ValueError:
        messagebox.showerror("Hata", "Fiyat ve stok sayısal değerler olmalıdır!")

def urun_guncelle():
    urun_ad = urun_ad_entry.get()
    urun_stok = urun_stok_entry.get()

    try:
        urun_stok = int(urun_stok)
        urun = next((u for u in menu if u.ad == urun_ad), None)

        if urun:
            urun.stok = urun_stok
            messagebox.showinfo("Başarılı", f"{urun_ad} ürünü stok miktarı güncellendi.")
        else:
            messagebox.showerror("Hata", f"{urun_ad} menüde bulunamadı.")
        urun_listele()
    except ValueError:
        messagebox.showerror("Hata", "Stok sayısal bir değer olmalıdır!")

def urun_sil():
    urun_ad = urun_ad_entry.get()
    urun = next((u for u in menu if u.ad == urun_ad), None)

    if urun:
        menu.remove(urun)
        messagebox.showinfo("Başarılı", f"{urun_ad} menüden silindi.")
        urun_listele()
    else:
        messagebox.showerror("Hata", f"{urun_ad} menüde bulunamadı.")

# Ürün listeleme fonksiyonu
def urun_listele():
    urunler_str = "\n".join([str(urun) for urun in menu])
    urunler_text.delete(1.0, tk.END)
    urunler_text.insert(tk.END, urunler_str)


pencere = tk.Tk()
pencere.title("Restoran Sipariş ve Yönetim Sistemi")

# Müşteri bilgisi
tk.Label(pencere, text="Müşteri Adı").grid(row=0, column=0)
ad_entry = tk.Entry(pencere)
ad_entry.grid(row=0, column=1)

tk.Label(pencere, text="Adres").grid(row=1, column=0)
adres_entry = tk.Entry(pencere)
adres_entry.grid(row=1, column=1)


tk.Label(pencere, text="Ürünler ve Miktarları").grid(row=2, column=0, columnspan=2)
miktar_girisleri = []
for i, urun in enumerate(menu):
    tk.Label(pencere, text=str(urun)).grid(row=3+i, column=0)
    entry = tk.Entry(pencere)
    entry.grid(row=3+i, column=1)
    miktar_girisleri.append(entry)


tk.Button(pencere, text="Sipariş Oluştur", command=siparis_olustur).grid(row=6, column=0, pady=10)
tk.Button(pencere, text="Siparişleri Listele", command=siparis_listele).grid(row=6, column=1)

# Ürün ekleme, güncelleme, silme
tk.Label(pencere, text="Yeni Ürün Adı").grid(row=0, column=2)
urun_ad_entry = tk.Entry(pencere)
urun_ad_entry.grid(row=0, column=3)

tk.Label(pencere, text="Yeni Ürün Fiyatı").grid(row=1, column=2)
urun_fiyat_entry = tk.Entry(pencere)
urun_fiyat_entry.grid(row=1, column=3)

tk.Label(pencere, text="Yeni Ürün Stok Miktarı").grid(row=2, column=2)
urun_stok_entry = tk.Entry(pencere)
urun_stok_entry.grid(row=2, column=3)

tk.Button(pencere, text="Ürün Ekle", command=urun_ekle).grid(row=3, column=2)
tk.Button(pencere, text="Ürün Güncelle", command=urun_guncelle).grid(row=4, column=2)
tk.Button(pencere, text="Ürün Sil", command=urun_sil).grid(row=5, column=2)

urunler_text = tk.Text(pencere, height=10, width=40)
urunler_text.grid(row=6, column=2, columnspan=2)


urun_listele()

# Sipariş görüntüleme alanı
text = tk.Text(pencere, height=15, width=50)
text.grid(row=7, column=0, columnspan=2, pady=10)

pencere.mainloop()
