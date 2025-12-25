codeskron – Alışveriş Sepeti Sitesi 🛍️codeskron, JavaScript kullanılarak geliştirilmiş, modern bir "yan panel" (side cart) mantığıyla çalışan basit ve etkileşimli bir alışveriş sitesi arayüzüdür. Kullanıcılar ürünleri sepete ekleyebilir, sepeti sağdan açılan şık bir panelde görüntüleyebilir ve toplam tutarı anlık olarak takip edebilirler.🛒 Site ÖzellikleriBu proje aşağıdaki temel e-ticaret işlevlerini içerir:Sepete Ekleme: Ürünler tek tıkla sepete eklenir.Akıllı Yan Panel: Sepet, sağ taraftan kayarak açılan (off-canvas) bir panelde görüntülenir.Miktar Yönetimi: Aynı ürün tekrar eklendiğinde liste uzamaz, ürünün miktarı artar.Ürün Silme: Sepetteki ürünler "X" butonu ile kolayca kaldırılabilir.Otomatik Hesaplama: Toplam sepet tutarı her işlemden sonra anlık olarak güncellenir.Otomatik Etkileşim: Sepete ürün eklendiğinde panel otomatik olarak açılır.🎯 Projenin AmacıBu site, özellikle aşağıdaki geliştiriciler için eğitim amaçlı hazırlanmıştır:JavaScript (ES6+) temellerini öğrenenler.DOM Manipülasyonu pratiği yapmak isteyenler.E-ticaret sitelerindeki sepet algoritmasının mantığını kavramak isteyenler.⚙️ Çalışma Mantığı1. Veri YapısıSepet verileri basit bir JavaScript objesi içinde tutulur:JavaScriptlet cart = {};
// Yapı: { "Ürün Adı": { price: 100, quantity: 2 } }
2. Sepet Etkileşimi (Açma/Kapatma)Açma: "Sepet Aç" butonuna basıldığında CSS class manipülasyonu ile panel görünür hale gelir ve açma butonu gizlenir.Kapatma: Panel üzerindeki "X" butonuna basıldığında panel kapanır ve açma butonu tekrar görünür.3. Ürün Ekleme ve SilmeEkleme: "Add to Cart" butonuna tıklandığında; ürün objede varsa quantity artırılır, yoksa yeni bir giriş oluşturulur. Ardından sepet paneli kullanıcıya açılır.Silme: Ürün yanındaki silme butonuna basıldığında, ilgili key objeden silinir ve HTML yeniden render edilir.4. Fiyat HesaplamaDöngü her çalıştığında (Fiyat * Miktar) işlemi yapılır ve genel toplam sepetin en altında gösterilir.🧩 Kullanılan TeknolojilerTeknolojiKullanım AmacıHTML5Sayfa iskeleti ve semantik yapı.CSS3Tasarım, responsive yapı ve yan panel (slide-in) animasyonları.JavaScript (Vanilla)Tüm sepet mantığı, DOM manipülasyonu ve event listener'lar.Python(Opsiyonel) Sunucu tarafı render işlemleri için (main.py).📂 Dosya YapısıPlaintextcodeskron/
├── templates/
│   ├── index.html        # Ana sayfa
│   ├── shop.html         # Mağaza sayfası
│   └── hediye.html       # Hediye/Kampanya sayfası
├── static/
│   ├── background3.jpg   # Arka plan görseli
│   └── urunphoto/        # Ürün görselleri
│       ├── urun1.jpg
│       ├── urun2.jpg
│       ├── urun3.jpg
│       ├── urun4.jpeg
│       ├── urun5.jpeg
│       └── urun6.jpeg
├── main.py               # Python çalıştırma dosyası
└── README.md             # Proje dokümantasyonu
💡 Geliştirme Fikirleri (To-Do)Proje açık kaynaklıdır ve geliştirmeye açıktır. İşte ekleyebileceğiniz bazı özellikler:[ ] Sepet içindeki ürün miktarını artırma/azaltma (+/-) butonları.[ ] LocalStorage entegrasyonu (Sayfa yenilendiğinde sepetin silinmemesi için).[ ] Tamamen mobil uyumlu (responsive) tasarım iyileştirmeleri.[ ] "Satın Al" butonu ile basit bir ödeme simülasyonu (Modal penceresi).📄 Lisans ve İletişimBu proje eğitim ve kişisel kullanım amaçlıdır.👨‍💻 Geliştirici: f1zuli1⭐ Bu projeyi faydalı bulduysanız yıldız vermeyi unutmayın!
