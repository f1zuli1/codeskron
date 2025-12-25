codeskron – Alışveriş Sepeti Sitesi

codeskron, JavaScript kullanılarak geliştirilmiş, yan panel (side cart) mantığıyla çalışan basit bir alışveriş sitesi arayüzüdür.
Kullanıcılar ürünleri sepete ekleyebilir, sepeti sağdan açılan panelde görüntüleyebilir ve toplam tutarı anlık olarak görebilir.

🛒 Site Özellikleri

Ürünleri sepete ekleme

Sağdan açılan yan sepet paneli

Aynı ürünü tekrar ekleyince miktar artırma

Sepetten ürün silme (X butonu)

Toplam fiyatın otomatik hesaplanması

Sepet boş değilse panelin otomatik açılması

🎯 Projenin Amacı

Bu site, özellikle:

JavaScript öğrenenler

DOM manipülasyonu pratiği yapmak isteyenler

Basit bir alışveriş sepeti mantığını anlamak isteyenler

için hazırlanmıştır.

⚙️ Çalışma Mantığı
Sepet Verisi
let cart = {};


Ürün adı key

Fiyat ve miktar value olarak tutulur

Sepeti Açma ve Kapatma

Sepet Aç butonuna basınca panel görünür

X butonuna basınca panel kapanır

Panel açıldığında açma butonu gizlenir

Ürün Ekleme

“Add to Cart” butonuna basıldığında:

Ürün sepete eklenir

Ürün zaten varsa miktarı artırılır

Sepet paneli otomatik açılır

Ürün Silme

Her ürünün yanında bir X butonu vardır

X’e basılınca ürün sepetten silinir

Sepet anında güncellenir

Toplam Fiyat

Her ürünün fiyatı miktarıyla çarpılır

Toplam tutar sepetin en altında gösterilir

🧩 Kullanılan Teknolojiler

HTML – Sayfa yapısı

CSS – Tasarım ve yan panel animasyonu

JavaScript (Vanilla JS) – Sepet mantığı ve etkileşimler

codeskron/
├── templates/
│   ├── index.html
│   ├── shop.html
│   └── hediye.html
│
├── static/
│   ├── background3.jpg
│   └── urunphoto/
│       ├── urun1.jpg
│       ├── urun2.jpg
│       ├── urun3.jpg
│       ├── urun4.jpeg
│       ├── urun5.jpeg
│       └── urun6.jpeg
│
|── main.py
└── README.md


💡 Geliştirme Fikirleri

Ürün miktarını artırma/azaltma butonları

Sepeti localStorage ile kaydetme

Mobil uyumlu tasarım

Ödeme simülasyonu

📄 Lisans

Bu proje eğitim ve kişisel kullanım amaçlıdır.
İsteyenler için MIT License eklenebilir.

👨‍💻 Geliştirici: f1zuli1
⭐ Projeyi beğendiysen yıldız vermeyi unutma!
