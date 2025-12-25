Anladım, istediğin düzenlemeleri yaparak, kaynak dosyadaki bilgilere sadık kalarak ve yalnızca sistem gereği olan atıf formatını kullanarak profesyonel bir README.md hazırladım.

Codeskron - Dinamik Alışveriş Sepeti Sistemi
Bu proje, bir web arayüzü üzerinde ürünlerin dinamik olarak sepete eklenmesini, yönetilmesini ve toplam maliyetin hesaplanmasını sağlayan JavaScript tabanlı bir sistemdir.

Temel Bileşenler ve Elementler
Sistem, kullanıcı etkileşimi için aşağıdaki DOM elementlerini ve veri yapılarını kullanır:


toggleBtn: Yan paneli açmak için kullanılan tetikleyici düğmedir.


panel: Ürünlerin listelendiği ve sepet içeriğinin gösterildiği yan panel alanıdır.


closeBtn: Paneli kapatmak için kullanılan düğmedir.


cart: Sepetteki ürünlerin isimlerini, fiyatlarını ve miktarlarını saklayan merkezi JavaScript objesidir.

Fonksiyonel Özellikler
1. Panel Yönetimi

Açma: toggleBtn tıklandığında panele "show" sınıfı eklenir ve panel görünür hale gelir; bu sırada açma düğmesi gizlenir.


Kapatma: closeBtn tıklandığında panelden "show" sınıfı kaldırılır ve açma düğmesi tekrar görünür hale gelir.


Otomatik Gösterim: Bir ürün sepete eklendiğinde, panel o an kapalıysa otomatik olarak açılır.

2. Sepet Güncelleme Mantığı (updatePanel)
Sepet içeriği her değişimde şu adımlarla yenilenir:


Temizleme: Paneldeki eski ürün listesi, verilerin üst üste binmemesi için her güncelleme öncesi temizlenir.


Dinamik Listeleme: cart objesindeki her ürün için Flexbox düzeninde yeni bir div oluşturulur.



Miktar Gösterimi: Eğer bir üründen birden fazla varsa, ürün adının yanında miktarı (örneğin: x2) otomatik olarak belirtilir.



Ürün Silme: Her ürünün yanında bulunan "X" butonu aracılığıyla ilgili ürün sepetten tamamen kaldırılabilir.



3. Otomatik Hesaplamalar

Toplam Tutar: Sistem, sepetteki her ürünün birim fiyatı ile miktarını çarparak toplam sepet tutarını hesaplar.



Anlık Güncelleme: Hesaplanan tutar, panelin alt kısmında oluşturulan totalDiv alanında anlık olarak güncellenerek kullanıcıya gösterilir.


4. Ürün Ekleme Süreci
"Add to cart" butonuna basıldığında sistem şu işlemleri gerçekleştirir:

İlgili ürün kartından ürünün ismini ve fiyat bilgisini ayıklar.

Ürün sepette zaten mevcutsa miktarını bir artırır; mevcut değilse yeni bir kayıt olarak ekler.


Sepet verisi güncellendikten sonra paneli otomatik olarak yeniler.

Bu proje, Vanilla JavaScript kullanarak efektif bir DOM manipülasyonu ve nesne tabanlı veri yönetimi örneği sunmaktadır.
