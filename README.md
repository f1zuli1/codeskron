# codeskron
# Codeskron - Dinamik Səbət Sistemi

[cite_start]Bu layihə, veb-səhifələrdə istifadəçi təcrübəsini artırmaq üçün hazırlanmış, JavaScript əsaslı dinamik bir alış-veriş səbəti moduludur. [cite: 1]

## 🚀 Ümumi Baxış

[cite_start]Codeskron, məhsulların səbətə əlavə edilməsi, miqdarın idarə olunması, ümumi məbləğin avtomatik hesablanması və səbət panelinin interaktiv idarəsini təmin edir. [cite: 1, 82]

## 🛠️ Əsas Komponentlər və Elementlər

Sistem aşağıdakı əsas HTML elementləri və JavaScript strukturları üzərində qurulub:

* [cite_start]**`toggleBtn`**: Səbət panelini açmaq üçün istifadə olunan düymə. [cite: 2, 6]
* [cite_start]**`sidePanel`**: Məhsulların siyahısının göstərildiyi yan panel alanı. [cite: 3, 7]
* [cite_start]**`closeBtn`**: Paneli bağlamaq üçün istifadə olunan düymə. [cite: 4, 8]
* [cite_start]**`cart`**: Məhsul adlarını, qiymətlərini və miqdarlarını saxlayan obyekt (`{}`). [cite: 5, 9]

## ⚙️ Funksionallıq

### 1. Panelin İdarə Edilməsi
* [cite_start]**Açılma**: Səbət aç düyməsinə basıldıqda panel görünür və açma düyməsi gizlənir. [cite: 11, 13, 19]
* [cite_start]**Bağlanma**: "X" düyməsinə basıldıqda panel bağlanır və açma düyməsi yenidən aktiv olur. [cite: 15, 17, 20]
* [cite_start]**Avtomatik Aktivləşmə**: Hər hansı bir məhsul səbətə əlavə edildikdə, panel avtomatik olaraq istifadəçiyə göstərilir. [cite: 75, 76, 84]

### 2. Məhsulların Səbətə Əlavə Edilməsi
[cite_start]"Add to cart" düyməsinə basıldıqda sistem aşağıdakı addımları yerinə yetirir: [cite: 63, 64]
* [cite_start]Məhsulun kartından (card) ad və qiymət məlumatlarını götürür. [cite: 66, 67, 68]
* [cite_start]Məhsul artıq səbətdə varsa, miqdarını (quantity) bir vahid artırır. [cite: 69, 70, 83]
* [cite_start]Məhsul yeni əlavə edilirsə, obyektə yeni məlumat kimi daxil edir. [cite: 71, 72, 82]

### 3. Panelin Yenilənməsi (`updatePanel`)
Hər bir əməliyyatdan sonra səbət paneli dinamik olaraq yenilənir:
* [cite_start]**Təmizləmə**: Köhnə məlumatların üst-üstə düşməməsi üçün panel əvvəlcə təmizlənir. [cite: 22, 23]
* [cite_start]**DOM Elementlərinin Yaradılması**: Hər məhsul üçün `flexbox` düzəni ilə yeni bir `div` yaradılır. [cite: 26, 28, 34, 35]
* [cite_start]**Məhsul Silmə**: Hər bir elementin yanında olan "X" düyməsi vasitəsilə məhsul tamamilə səbətdən silinir. [cite: 38, 41, 46]

### 4. Qiymət Hesablanması
[cite_start]Sistem avtomatik olaraq ümumi məbləği hesablayır: [cite: 47, 61]
* [cite_start]Hər bir məhsulun qiyməti onun miqdarına vurulur və cəmlənir. [cite: 58, 62]
* [cite_start]Yekun məbləğ panelin sonunda qalın şriftlə (`bold`) göstərilir. [cite: 52, 60]

## 💻 Quraşdırma

Layihəni lokal mühitinizdə işlətmək üçün:

1. Repozitoriyanı kopyalayın.
2. HTML faylınızda `sidePanel`, `toggleBtn` və `closeBtn` ID-li elementlərin olduğundan əmin olun.
3. [cite_start]Məhsul kartlarınızda `.cart-button`, `.title span` və `.price span` klaslarından istifadə edin. [cite: 64, 67, 68]

---
Bu layihə JavaScript-də DOM manipulyasiyası və obyektlərlə işləmək üçün mükəmməl bir nümunədir.
