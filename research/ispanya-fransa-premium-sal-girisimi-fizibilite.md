# Türkiye → İspanya → Fransa: Premium Kadın Şal/Fular DTC Girişimi — Fizibilite Raporu

**Tarih:** 2026-09-17
**Hazırlanan kişi:** Kaan Yılmaz
**Soru:** Türkiye'den kaliteli kadın şalı/fuları düşük-orta maliyetle tedarik edip, bunu İspanya'da (sonra Fransa'da) premium bir European fashion-accessories markası olarak konumlandırıp Meta + Google Ads ile 2026 Q4'e kârlı şekilde ölçekleyebilir miyiz?

---

## Yöntem ve sınırları — rakamlara güvenmeden önce bunu oku

Araştırma, dış ağ erişiminin egress proxy tarafından kısıtlandığı bir sandbox ortamında yapıldı. **Bu oturumda erişilebilen tek dış alan adı GitHub'dı** (test edildi: `en.wikipedia.org`, `google.com`, `eur-lex.europa.eu`, `r.jina.ai`, rakip siteler — hepsi bloklu, hem WebFetch hem curl ile). Pratik sonuçları:

- **Canlı rakip sitelerini açamadım.** Senin "rakiplerin gerçek fiyatlarını canlı sitelerden doğrula" talebini bu ortamdan teknik olarak yerine getirmek mümkün değil. Bunun yerine yaptığım şey: her marka ve her ürün için **hedefli arama turları** çalıştırıp ürün sayfalarından arama motoruna yansıyan gerçek fiyatları çıkardım. Bu, ilk rapordan **belirgin şekilde daha iyi** ama "canlı doğrulanmış" değil.
- §11'deki fiyat tablosuna bu yüzden bir **"Doğrulama durumu"** kolonu ekledim: `ÜRÜN SAYFASI` (arama sonucu doğrudan o markanın ürün sayfasından fiyat döndürdü — yüksek güven), `AGREGATÖR` (Lyst/Fashiola gibi karşılaştırma sitesi — orta güven), `DOĞRULANMADI` (fiyat alınamadı — tahmin yazmadım).
- **§26'nın sonunda sana 15 dakikalık kendi doğrulama listeni bıraktım.** 12 URL, ne arayacağın ve hangi hücreyi güncelleyeceğin yazılı. Bu iş senin tarafında 15 dakika, benim tarafımda imkânsız.
- **Anahtar kelime hacmi verisi alınamadı.** Google Keyword Planner erişilemedi. §17 sana keyword mimarisini ve yöntemi veriyor, hacim vermiyor. Google'a bütçe ayırmadan önce hacimleri kendin çekmen gerekiyor.
- Pazar araştırma şirketlerinin rapor satmak için yayınladığı rakamları **[satıcı tahmini]** olarak etiketledim. Hiçbir kararı bunlara dayandırmadım. Resmî kaynaklar (CNMC, INE, FEVAD, IAB Spain, Avrupa Komisyonu, INSEE/IFM) ağırlığı taşıyor.
- USD rakamları **1 USD ≈ €0,92** ile çevrildi ve etiketlendi.

Doğrulayamadığım hiçbir şeyi doğrulanmış gibi yazmadım.

## İlk rapora göre ne değişti

Bu tur dört fiyat düzeltmesi çıktı. İkisi karar-ilgili:

| Bulgu | İlk raporda | Bu turda | Etkisi |
|---|---|---|---|
| **Massimo Dutti** | "fularlar €30'dan başlıyor" (ipek olmayan varsaydım) | **%100 ipek desenli fular €29,95**; keten fular €39,95 | **Ciddi. Güvenilen bir İspanyol premium markası %100 ipeği €29,95'e satıyor.** Senin €59,90'ın farklılaşma yükü sandığımdan ağır. Fiyatı düşürmek çözüm değil (§6.2) — çözüm baskı deseni + sunum + hediye paketi |
| **Fio de Martié** | "€48,90'dan başlıyor" | 33×33 cm **€16,90**; bandana **€48,90'dan**; **70×70 ve 90×90 cm = €94,90**; İtalyan ipeği, İspanya'da el yapımı | **Lehine. Bir İspanyol markası 90×90 ipek kareyi €94,90'a satıyor.** €59,90 bunun çok altında — premium konumlandırma için tavan sandığımdan yüksek |
| **ARKET** | "kaşmir €39" | **Kaşmir ~£85 (≈€98), desenli ipek ~£45 (≈€52)** | Lehine. €39 kaşmir tehdidi büyük olasılıkla yanlıştı (indirim ya da farklı ürün). "Plain kaşmirle yarışamazsın" argümanı zayıflıyor ama yine de geçerli |
| **Hamzah** (İspanyol zanaatkâr) | doğrulanmadı | **İpek fular €35–49**, büyük boy €47, "Noisette" €69, €50 üzeri ücretsiz kargo | Nötr. İspanyol bağımsız-premium bandını teyit ediyor |

**Net etki: €59,90 hero fiyatı ayakta kalıyor**, çünkü İspanyol bağımsız-premium bandı düşündüğümden geniş çıktı — Hamzah €35 ile Fio de Martié €94,90 arası. €59,90 tam ortada. Ama Massimo Dutti'nin €29,95 ipeği, "farkı görünür kılma" işini opsiyonel olmaktan çıkarıp zorunlu hale getiriyor.

---

# 1. YÖNETİCİ ÖZETİ

## Tek paragraflık cevap

Talep gerçek, kategori şu anda gerçekten moda, brüt marj yapısı çalışıyor ve senin creative avantajın ölçülebilir bir para değerine sahip. Ama **temel varsayımın güncelliğini yitirmiş**: 2026'da Türkiye ucuz tedarik hikâyesi değil, *hızlı, düşük-MOQ, orta maliyetli* tedarik hikâyesi — ve Türk tekstil sektörü belgelenmiş bir maliyet krizinde. Aritmetik ise şu spesifik biçimde affetmiyor: **pazar ortalaması Meta performansında bu iş para kaybediyor** ve ancak creative + conversion + AOV'de aynı anda üst çeyrekte olduğunda kâra geçiyor. Bu, vazgeçme gerekçesi değil — bahsi **launch değil test** olarak boyutlandırma ve iki sayıya kilitleme gerekçesi.

**Karar: ÖNCE TEST ET (TEST FIRST).** Sadece İspanya. €5.000. Tek ürün ailesi, tek fiyat, tek ülke, 60 gün, önceden taahhüt edilmiş kill kriterleriyle. Detay §26'da.

## 15 sorunun cevabı

| # | Soru | Cevap | Kararı belirleyen kanıt |
|---|---|---|---|
| 1 | İş modeli mantıklı mı? | **Koşullu evet.** €59,90+ seviyesinde brüt marj net gelirin %64–69'u. Paid acquisition'ı finanse etmeye yeter — ama ancak CTR × CVR belirli bir barajı geçerse | €8 landed COGS ve %10 return ile €59,90'da break-even CAC €27,18 (kendi modelim, §7) |
| 2 | İspanya'da gerçek talep var mı? | **Evet.** 27,4M online alışverişçi (16–74 yaşın %77'si); giyim = 2025 Q4 e-ticaret cirosunun %7'si; kadınlar online moda alıcılarının %56,5'i; moda Noel'de #2 hediye kategorisi (%43) | IAB Spain *Estudio Ecommerce 2025*; CNMC Q4 2025; OCU Noel 2025 |
| 3 | Fransa'da gerçek talep var mı? | **Evet, daha büyük ama daha zor.** Giyim e-ticareti €7,7 milyar, tüm giyim tüketiminin %30,7'si artık dijital. Ama ortalama sepet €62'ye **düştü** (−%3) ve moda hacimde düşen tek sektör | FEVAD *Chiffres Clés 2025* / *Mode et Internet 2025* |
| 4 | Şal/fular kategorisi kadınlar için ne kadar güçlü? | **Güçlü ve şu anda trend.** İpek fular 2026 ilkbaharın en büyük aksesuar trendlerinden biri ilan edilmiş, SS26 podyumlarında (Totême, Dries Van Noten); arama ilgisi **Ekim ve Aralık'ta** zirve yapıyor | WWD, Marie Claire UK, trend/arama analizleri (§5) |
| 5 | Premium konumlandırma yapılabilir mi? | **Evet, €49–79 bandında. Üstünde değil.** Gerçek, dolu, fiyatı doğrulanmış bir katman var: Hamzah €35–69, Philéone €42–95, Le Châle Bleu €39–169, **Fio de Martié 90×90 = €94,90** | Rakip fiyat taraması (§11) |
| 6 | Türkiye'den tedarik avantaj sağlar mı? | **Evet — ama sandığın avantajı değil.** Avantaj: **renk başına 10 adet MOQ**, dokuma etiket, özel nakış, markalı ambalaj, 5–8 gün transit ve iterasyon hızı. **Fiyat değil:** Türkiye'de asgari ücret 2022–2024'te %249 arttı, enerji maliyeti ikiye katlandı, sektör 7 milyar $ üretim ve 210.000 iş kaybetti, lira reel olarak değerlendi | Hicabistan (fabrika-direkt €1,90/adetten, renk başına 10 adet MOQ); WWD Sourcing Journal; Turkish Minute; ING |
| 7 | Meta acquisition ekonomisi çalışır mı? | **Sadece benchmark'ın üstünde.** Pazar ortalamasında (€13 CPM, %1,5 link CTR, %1,8 CVR) CAC €54,71, tavan €27,96 — 2 kat aşım. **link CTR × session CVR ≥ %0,053** gerekiyor (€59,90 AOV'de). Yani %2,0 × %3,0, %1,5 × %1,8 değil | Kendi modelim (§7–8), Triple Whale 2025 yıl-sonu ve 2026 e-ticaret benchmark'larına karşı |
| 8 | Google ne kadar önemli? | **Çok — ama kâr kanalı, büyüme kanalı değil.** Avrupa e-ticaret Shopping CPC'si €0,29–0,35. %3 CVR'de bu ~€18 CAC. Ama İspanya'da şal arama talebi ince; Google düşük hacimde tavan yapacak. Blended CAC'i sübvanse etmek için kullan, işi taşıması için asla | smec Market Observer (yıllık €450M Avrupa perakende reklam harcaması paneli) |
| 9 | Q4 / BF / Noel gerçek fırsat mı? | **Evet — bu işi yapmanın en güçlü yapısal gerekçesi.** İspanya: kişi başı €796 bayram harcaması, €370'i hediye, hediye alımlarının %43'ü moda ve **Reyes (€192) Noel arifesini (€178) geçiyor** — sezonun 5 Ocak'a kadar uzuyor. Şal araması Ekim ve Aralık'ta zirve | OCU; Oney; Google Trends analizleri |
| 10 | Creative üretim yeteneğim gerçek avantaj yaratır mı? | **Evet ve ölçülebilir.** Ayda 15+ yeni konsept test eden markalar, <5 test edenlere göre aynı harcamada **1,8 kat yüksek medyan ROAS** gösterdi. Bu çıktıyı satın almak ayda €3.000–6.000 (20 asset × €150–450). Sen ~€240/ay araç maliyetiyle üretiyorsun | MHI'nin 80 DTC hesabı analizi, 2025; Avrupa UGC fiyat listeleri |
| 11 | En büyük riskler? | (1) Ortalama creative → garantili zarar, mütevazı kâr değil. (2) **AB 1 Temmuz 2026'da €150 gümrük muafiyetini kaldırıyor** ve adet başına sabit €3 vergi getiriyor — bu, 2026 Q4 launch'ı için Türkiye'den direkt gönderimi kırıyor. (3) Güven: Türkiye, AB alışverişçilerinin "güvendiğim ülkeler" listesinde yok. (4) Fransa **10 Temmuz 2026'dan beri Fransız temsilci zorunlu tutuyor** (tekstil EPR) | Avrupa Komisyonu / AB Konseyi; DHL cross-border; Refashion / Md. L.541-10-9-1 |
| 12 | Test bütçesi ne olmalı? | **€5.000 sert tavan, 30/10/10/40/6/4 dağılımıyla** — §22. Senin taslağındaki "€3.000'i Meta" değil. Ürün/numuneye daha çok, siteye daha az | — |
| 13 | İlk 30 günde ne test edilmeli? | Tek şey: **link CTR × CVR'yi €65+ AOV'de %0,055'in üstüne çıkarabiliyor musun.** Bu geçmeden gerisi gürültü | §22 |
| 14 | İlk 90 gün nasıl ilerlemeli? | Gün 1–30 funnel barajını kanıtla. Gün 31–60 AOV mimarisini kanıtla ve stok al. Gün 61–90 Q4'ü yükle, Google + TikTok Shop ekle, Reyes uzatmasını önceden kur | §23 |
| 15 | İspanya mı Fransa mı, yoksa ikisi birden mi? | **Önce İspanya, tek başına.** Daha düşük CPM, orada yaşıyorsun, Reyes sezonu 3 hafta uzatıyor ve Fransa'da tek ürün satmadan önce ödemen gereken bir uyum yığını var (Refashion UIN + Fransız temsilci + Triman). Fransa 2027 Q2 genişlemesi, 2026 Q4 ortak launch'ı değil | §4, §20 |

## Bir euro harcamadan önce itiraz ettiğim dört şey

**1. "Türkiye = ucuz."** Bu 2019'da doğruydu. 2026'da Türk tekstil sektörü bu ticaretin *sıkıntıdaki* tarafı, avantajlı tarafı değil: asgari ücret +%249 (2022–2024), enerji maliyeti ikiye katlandı, finansman %50'ye kadar faizle, 7 milyar $ üretim kaybı, 210.000 iş gitti, ihracat 2026'ya sarkan düşüşte, fabrikalar kapanıyor. Lira, politika gereği Türk enflasyonundan **yavaş** değer kaybediyor (12 ayda USD'ye karşı −%17, buna karşı %32,6 TÜFE) — yani **Türk maliyetleri her yıl euro bazında artıyor.** €5–10 landed maliyetin bugün mümkün ve eriyen bir varlık. Ürünü **2028'de €12 landed** olacak şekilde fiyatla, ve tedarikçi fiyatını TRY değil **EUR** üzerinden 12 ay kilitle.

**2. "Pazar büyük = benim ürün satar."** İspanyol hanelerinin giyim-ayakkabı harcaması 2025'te hane başına €16 **düştü** ve bütçenin %4,03'üne geriledi. Fransa'da moda sepeti %4,2 düştü ve moda hacimde düşen tek sektör oldu; Shein + Temu online giyim alımlarının %16'sını €9 ortalama fiyatla aldı. Orta segment alttan yok ediliyor. Bu, **premium (€49–79) için bir argüman** ve €24,90 civarında yarışmaya karşı güçlü bir argüman.

**3. "Meta çalışır çünkü creative'de iyiyim."** Creative yeteneğin CTR'yi ve dolaylı olarak CVR'yi hareket ettirir. CPM'i, KDV'yi, kargoyu, iadeleri ya da €59,90'da müşteri kazanmak için €27,96'nın olduğu gerçeğini hareket ettirmez. Creative beş değişkenden biri. Diğer dördü — offer mimarisi, landing page CVR'si, AOV ve repeat rate — founder seviyesinde daha önce yapmadığın işler. Dikkatini sadece reklamlara değil onlara da ayır.

**4. Tarih problemi.** 2026 Q4'ü hedefliyorsun; AB'nin de-minimis kaldırması **1 Temmuz 2026**'da, 2028'e kadar adet başına sabit €3 vergiyle devreye giriyor. Türk menşeli malların AB–Türkiye Gümrük Birliği (A.TR) kapsamında bundan muaf olup olmadığı kamuya açık rehberlikte **gerçekten belirsiz**. Direkt gönderim modelini bunun muaf olduğu varsayımı üzerine kurma. Birinci hafta bir İspanyol gümrük müşavirinden yazılı görüş al. **İspanya'da stok tutmayı planla.**

---

# 2. İSPANYA PAZAR ANALİZİ

## 2.1 Pazar büyüklüğü ve yapısı

| Metrik | Değer | Yıl | Kaynak |
|---|---|---|---|
| Toplam e-ticaret cirosu | **€114,8 milyar**, +%20,6 YoY | 2025 | CNMC (The Corner üzerinden) |
| Q4 e-ticaret cirosu | €31,42 milyar, +%22 YoY | 2025 Q4 | CNMC basın notu |
| Q4 işlem sayısı | >575M, +%20,2 | 2025 Q4 | CNMC |
| Q4 cirosunun İspanya içinde üretilen payı | %42,2 | 2025 Q4 | CNMC |
| **Giyimin Q4 cirosundaki payı** | **%7,0** (tek çeyrekte ≈ €2,2 milyar) | 2025 Q4 | CNMC |
| Moda e-ticaret cirosu | 9.863M USD ≈ **€9,1 milyar**, %5–10 büyüme | 2025 | ECDB **[satıcı tahmini]** |
| Modanın online perakende payı | %25–30 | 2025 | ECDB **[satıcı tahmini]** |
| Online alışverişçi penetrasyonu (16–74) | **%77 = 27,4M kişi** | 2025 | IAB Spain *Estudio Ecommerce 2025* |
| Alışverişçi başına kanal sayısı | 3,2 (Amazon %82, **marka DTC %47**, diğer pazar yerleri %47, çok markalı %39) | 2025 | IAB Spain 2025 |

**Kanal rakamını dikkatli oku.** Amazon İspanyol online alışverişçilerin %82'si tarafından kullanılıyor, ama **marka kendi e-ticareti %47'si tarafından** — neredeyse yarısı. İspanyol bir kadının €59'luk bir fuları markanın kendi sitesinden alması normal bir davranış, uç bir vaka değil. Bu iş için İspanya'daki en önemli yapısal gerçek bu.

## 2.2 Kadın modası ve aksesuar

**İspanya'ya özgü şal/fular pazarı için güvenilir kamusal bir rakam yok.** Statista'nın şal seviyesindeki verisi ödeme duvarının arkasında; kamuya açık tek kategori-seviyesi rakam global satıcı tahminleri (§5). "İspanya şal pazarı €X" diyen her iddiayı uydurma kabul et. **Belgelenen** şunlar:

| Metrik | Değer | Kaynak |
|---|---|---|
| Kadınların online moda alıcıları içindeki payı | **%56,5** | Statista/Elogia (2022) |
| Online moda alıcılarının en büyük yaş bandı | **35–54** | Statista/Elogia (2023) |
| En çok satan online moda kategorisi | **Kadın modası** — online moda alıcılarının ~2/3'ü alıyor | Statista/Elogia (2024) |
| Kadınların ortalama online moda sepeti | **€70'in hemen altı** | Statista/Elogia (2024) |
| Erkeklerin ortalama online moda sepeti | ~€84 | Statista/Elogia (2024) |

**Bu bölümün en aksiyona dönük verisi €70 rakamı.** Ortalama İspanyol kadının online moda siparişi €70'in hemen altında. Bu şunu söylüyor:

- **€59,90 tek ürün fiyatı normal davranışın içinde**, zorlama değil.
- **€69,90–€79,90 bundle veya hediye seti ortalama sepetin üstünde ama yakınında** — bir gerekçeyle (hediye, set, ücretsiz kargo) ulaşılabilir.
- €99,90, ortalama kadın moda sepetinin ~1,4 katı. Noel hediyesi SKU'su olarak mümkün, çekirdek fiyat olarak değil.

## 2.3 Harcama gücü ve nerede olduğu

| Metrik | Değer | Yıl | Kaynak |
|---|---|---|---|
| Ortalama hane geliri (kira eşdeğeri dahil) | €42.269 | 2024 | INE ECV |
| Ortalama hane harcaması | €35.101 (+%3,1) | 2025 | INE EPF 2025 |
| Kişi başı ortalama harcama | €14.066 (+%3,2) | 2025 | INE EPF 2025 |
| Giyim + ayakkabının hane bütçesindeki payı | **%4,03** (2024'te %4,21) | 2025 | INE EPF 2025 |
| Hane başı giyim + ayakkabı | €1.432 | 2024 | INE EPF |
| Giyim + ayakkabı harcamasındaki YoY değişim | **hane başı −€16** | 2025 | INE EPF 2025 / Modaes |

**Bu, reel olarak daralan bir kategori ve planını buna göre kurmalısın.** İspanyol haneleri 2025'te giyime 2024'ten hem mutlak hem oransal olarak daha az harcadı. Kişi başı moda harcaması, dört yıllık toparlanmanın ardından 2025'te düştü (Modaes). Değer bazında küçülen, fiyatta kutuplaşan bir pazara giriyorsun. Bu yapıda kazananlar çok ucuz (Shein/Temu) ve net şekilde "değer" veren premium. Markalar ortada ölüyor.

**En yüksek gelirli bölgeler (eşdeğer ortalama gelir, INE ECV 2023 dalgası):**

| Bölge | Eşdeğer ortalama gelir | Not |
|---|---|---|
| País Vasco | €26.298 | Belediyelerinin %90,9'u İspanya'nın en yüksek gelir çeyreğinde |
| Comunidad de Madrid | €24.991 | En büyük mutlak pazar |
| Navarra | €24.495 | Belediyelerinin %69,1'i en yüksek çeyrekte |

**Premium aksesuar markası için şehir hedefleme önceliği:**

| Kademe | Şehirler | Gerekçe |
|---|---|---|
| **Kademe 1 — buradan aç** | Madrid, Barcelona | En yüksek gelir yoğunluğu + premium-moda satın alma davranışının en yoğun olduğu yer + en iyi teslimat altyapısı |
| **Kademe 2 — ölçeklerken ekle** | Bilbao / San Sebastián, Pamplona, Valencia, Sevilla, Málaga, Zaragoza | Bilbao/Pamplona gelir için; Valencia/Sevilla/Málaga hacim ve iklime uygun hafif ürün için |
| **Kademe 3 — sadece sezonluk** | Palma, Marbella, A Coruña, Santander | Palma ve Marbella yüksek gelirli ama sezonluk-ikamet ağırlıklı; always-on değil Q4 hediye geo'su olarak kullan |
| **Test aşamasında bilinçli olarak dışla** | Canarias, Ceuta, Melilla | Bu amaçlar için İspanya'nın AB KDV/gümrük bölgesi dışında — farklı vergi ve kargo işleyişi. Küçük hacim kazancı için ops gürültüsü yaratmaya değmez |

## 2.4 İspanyol kadınlar şal/fuları online almaya yatkın mı?

Dürüst cevap: **İspanya'ya özgü şal satın alma sıklığı veya malzeme tercihi verisi kamuya açık değil.** Uydurmayacağım. Meşru şekilde çıkarılabilenler ve gerçek cevabı nasıl alacağın:

**Verinin desteklediği:**
- Kadın modası en çok satan online moda kategorisi (online moda alıcılarının ~2/3'ü).
- Aksesuarların giyime karşı yapısal bir avantajı var: **beden yok.** Uyum/beden, giyim iadelerinin ~%50'sinin nedeni. Şalın bedeni yok, dolayısıyla iade oranı %20–40 giyim bandının çok altında — aksesuar ve hediyelik ürünlerde tipik olan %5–10 aralığına yakın olmalı. **Bu kategori için en güçlü tek ekonomik argüman bu** ve doğrudan §7'ye akıyor.
- Moda İspanya'da #2 Noel hediye kategorisi (%43 niyet, parfümün %47'sinin ardından) ve #2 Black Friday niyet kategorisi (%34).

**Desteklenmeyen ve varsaymaman gerekenler:** İspanyol kadınlara özgü malzeme tercihi, renk tercihi, styling alışkanlıkları veya tekrar sıklığı. Bu rakamları sana veren kişi uydurmuştur.

**Birinci haftada ~€300'e nasıl alınır:** İspanyol bir panel sağlayıcısı üzerinden 400 kişilik anket, Madrid/Barcelona'da son 6 ayda online moda alışverişi yapmış 28–55 yaş kadınlarla filtrelenmiş. Altı soru: son aldığı şal (fiyat/yer), ipek dokulu bir şala kabul edilebilir fiyat, malzeme tercihi, hediye mi kendine mi, marka hatırlama, bilinmeyen markadan alma isteği. Bu veri, satın alabileceğin her rapordan daha değerli.

## 2.5 Sezonluk yapı ve İspanya'daki Q4 şekli

| Metrik | Değer | Kaynak |
|---|---|---|
| Kişi başı toplam bayram harcaması | **€796** | OCU (Noel 2025) |
| Bunun hediye kısmı | **€370** | OCU |
| Reyes (5–6 Ocak) hediyeleri | **€192** | OCU |
| Noel arifesi hediyeleri | €178 | OCU |
| En çok alınan hediye kategorileri | Parfüm %47, **moda %43**, oyuncak %35 | OCU |
| Kişi başı ortalama online bayram harcaması | €250 (+%4 YoY) | Ecommerce News ES |
| Zirve satın alma pencereleri | **9–18 Aralık** ve **Reyes'ten hemen önceki günler** | Retail Actual |
| Black Friday ortalama hediye harcaması | €411 (+%4,8 YoY) | Oney 2025 |
| BF'yi hediye almak için kullananlar | **10'da 8** | Oney 2025 |
| Erken alıcı primi | Erken alanlar Aralık alıcılarına göre **+€140** harcıyor | Oney 2025 |
| BF'de tercih edilen harcama kategorisi olarak moda | %71,3 satın alma niyeti | Oney 2025 |

**Reyes Magos yapısı gerçek ve yeterince kullanılmayan bir avantaj.** İspanyol hediyeleşmesi 25 Aralık'ta bitmiyor — en büyük tek hediye harcaması 5–6 Ocak'taki Reyes. Yabancı DTC markalarının çoğu teslimat riski için Q4 kampanyalarını 20 Aralık'ta kapatıyor. **İspanya'da stok tutarsan, çökmüş CPM'lerle ve neredeyse sıfır rekabetle 2–5 Ocak arası kârlı satış yapabilirsin** — hem de hiçbir sınır ötesi rakibin veremeyeceği 24 saatlik yurt içi teslimat vaadiyle. Bunu planın birinci gününden içine koy (§14).

---

# 3. FRANSA PAZAR ANALİZİ

## 3.1 Pazar büyüklüğü ve yapısı

| Metrik | Değer | Yıl | Kaynak |
|---|---|---|---|
| Toplam e-ticaret cirosu | **€196,4 milyar**, +%7 YoY | 2025 | FEVAD |
| Önceki yıl | €175,3 milyar | 2024 | FEVAD |
| İlk yarı büyümesi | +%7,9 | 2025 H1 | FEVAD |
| **Ortalama sepet** | **€62, −%3 YoY** (ürün −%4, hizmet −%3) | 2025 | FEVAD |
| Giyim e-ticaret penetrasyonu | **giyim satışlarının %23'ü = €7,7 milyar** | 2025 | FEVAD |
| Dijitalin toplam giyim tüketimindeki payı (tüm yaşlar) | **%30,7** | 2025 | FEVAD *Mode et Internet 2025* |
| Moda sıklığı | **Daha sık alıyorlar, +%3,9** | 2025 | FEVAD |
| Moda sepeti | **−%4,2** | 2025 | FEVAD |
| Moda hacmi | **−%0,5 — düşen tek sektör** | 2025 | FEVAD |
| Giyim zincirlerinin mağaza cirosu | −%1,2 | 2025 | Républik Retail / IFM |
| Fransız moda pazarı (aksesuar dahil) | **€34,7 milyar** | 2025 | Institut Français de la Mode |
| Aksesuar + ayakkabının Fransız moda pazarındaki payı | **%10** | 2025 | IFM |
| Kişi başı giyim/ayakkabı/aksesuar bütçesi | **€668/yıl** | güncel | INSEE (IFM üzerinden) |

**Online modada pazar payları:** Amazon %22,6, **Vinted %21,4**, Shein %17,3. Shein + Temu birlikte **online giyim alımlarının %16'sını ve tüm giyim alımlarının hacim olarak %5'ini** alıyor, **€9 ortalama fiyatla** — geleneksel oyuncularda bu €14–74 (FEVAD).

## 3.2 Bu yapı sana ne söylüyor

Fransa daha büyük ve daha zor pazar, üç yapısal nedenle:

1. **Sepet düşüyor, yükselmiyor.** €62 ve −%3. Fransız tüketici daha sık, daha düşük değerde alıyor. FEVAD'ın genel delegesi bunu "artan tasarruf olgusu" artı Çinli düşük maliyetli platformlar ve ikinci el büyümesine bağlıyor. **€59,90 tek ürün fiyatı ulusal ortalama sepetin ~%97 üstünde.** İspanya'da karşılaştırılabilir çapa (kadın moda sepeti, €70'in hemen altı) €59,90'ı normal gösteriyor; Fransa'da €62'lik tüm-kategori ortalaması onu "düşünülmüş satın alma" yapıyor.
2. **Vinted'in %21,4'ü, İspanya'da aynı derecede olmayan kategoriye özgü bir tehdit.** İkinci el, Fransa'da #2 moda kanalı. Şal ideal bir resale ürünü — küçük, bedensiz, marka-okunur, dayanıklı. Hermès kareleri için müzayede evi değerleme hizmetleri olan tam bir ikincil pazar var. Senin €59'luk yeni şalın, benzer fiyata gerçek bir ikinci el tasarımcı şalıyla yarışıyor.
3. **Fransız alışverişçi pazar yerini tercih ediyor.** Fransız tüketicilerin %83'ü Amazon ve Etsy gibi pazar yerlerine güçlü tercih gösteriyor (DHL cross-border araştırması). Yeni bağımsız bir DTC sitesi Fransa'da İspanya'dan daha yüksek bir güven eşiğiyle karşılaşıyor.

## 3.3 Tüketici profili ve hediyeleşme

| Metrik | Değer | Kaynak |
|---|---|---|
| Noel bütçesi 2025 | **€491 — 2017'den beri en düşük** (−€6 YoY) | Cofidis 9. edisyon / franceinfo |
| Medyan Noel bütçesi | **€350 (−€50)** | Cofidis |
| Bunun hediye kısmı | **€297** | Cofidis |
| Yemekler | €123 | Cofidis |
| 65+ | €638 | Cofidis |
| 18–24 | €538 | Cofidis |
| CSP+ (üst sosyo-profesyonel) | **€517** | Cofidis |
| CSP− | €370 | Cofidis |
| Ortalama hediye sayısı | **9 — 2017'den beri rekor** | Cofidis |
| Instagram kullanıcısı | **32,87M, %54,4 kadın**, 25–34 en büyük kohort | Statista (Haziran 2026) |
| Baskın kart şeması | **Cartes Bancaires ~%79** kart payı; CB checkout dönüşümü ~%85 (sektör ~%75) | Antom / Payplug |
| Klarna ayak izi | 7M kullanıcı, 57.500 üye işyeri, 5 yılda €6,2 milyar TTV | Crowdfund Insider 2026 |

**Hediyeleşme sinyali karışık ve bunu yeşil ışık değil uyarı olarak okumalısın.** Fransız Noel bütçesi dokuz yılın en düşüğünde, *ama* ortalama hediye sayısı dokuzla rekor kırdı. Fransızlar **daha fazla hediyeyi daha düşük birim değerde** alıyor. Bu, €59,90–79,90'lık tek premium hediye için tam ters yön — ve **€34,90–44,90 "küçük güzel hediye"** SKU'su için tam doğru yön. Fransa'ya girersen hero SKU daha küçük bir format (65 cm kare, ince twilly tarzı fular) ve İspanya hero'ndan daha düşük fiyat olmalı. Bu, verinin zorladığı gerçek bir ürün kararı.

**Premium aksesuar launch'ı için şehirler:**

| Kademe | Şehir | Gerekçe |
|---|---|---|
| 1 | **Paris / Île-de-France** | Gelir yoğunluğu, premium aksesuar okuryazarlığı, hedef avatarın en yoğun olduğu yer. Aynı zamanda Fransa'nın en rekabetçi ve en yüksek CPM'li geo'su |
| 2 | **Lyon, Bordeaux, Nice** | Lyon: ipek mirası şehri (Croix-Rousse), zengin, güçlü perakende. Bordeaux: yüksek gelir, stil bilinçli, Paris'ten düşük CPM. Nice: zengin + Akdeniz estetiği uyumu + sezonluk ikamet zenginliği |
| 3 | **Toulouse, Nantes, Strasbourg, Montpellier** | Sağlam gelir, daha ucuz medya, premium moda doygunluğu düşük |
| 4 | **Lille, Marseille** | Daha büyük nüfus ama premium aksesuar için daha zayıf ortalama sepet; Marseille fiyat hassas, Lille Belçika ile sınır ötesi rekabetli |

**Lyon'a özel uyarı:** Lyon, Fransız ipeğinin tarihî başkenti. Türk tedarik zinciriyle ve atölye hikâyesi olmadan "premium ipek" pazarlamasını Lyon'a yapmak, tam da hayatta kalamayacağın türden bir incelemeyi davet ediyor. Lyon harika bir *ciro* geo'su ve berbat bir *ilk izlenim* geo'su. Paris/Bordeaux'dan aç, yorumlar ve basın geldikten sonra Lyon ekle.

## 3.4 Türkiye'den gelen bir marka Fransız tüketicide güven oluşturabilir mi?

**Doğrudan cevap: evet — marka hukuken ve operasyonel olarak Avrupalıysa ve Türkiye unsuru "marka menşei" değil "zanaat" olarak sunulursa. Hayır — alışverişçinin ilk izlenimi "Türk şal markası" ise.**

Kanıtlar:

| Kanıt | Sonuç |
|---|---|
| **10 alışverişçiden 7'si sadece güvendiği ülkelerden alıyor.** DHL'in 2025 cross-border araştırmasında güvenilen liste: ABD, İngiltere, Almanya, Çin, Fransa, İtalya, Kanada, Avustralya. **Türkiye yok.** | "Türkiye'den gönderiliyor" ya da Türk şirket adı satın alma öncesi asla görünür olmasın. Bu bir şeyi saklamak değil — ödemene gerek olmayan bir güven cezasını gönüllü ödememek |
| **Fransız tüketicilerin %83'ü pazar yerini tercih ediyor** (Amazon, Etsy) | Üçüncü taraf doğrulama Fransa'da İspanya'dan daha önemli. Yorumlar, basın logoları, muhtemelen sosyal kanıt için paralel bir Etsy/Amazon varlığı |
| Menşe ülke etkisi araştırması, tüketicilerin gelişmiş ekonomilerden gelen ürünleri kalitede daha yüksek puanladığını ve hem *bilişsel* hem *duygusal* ülke-imajı faktörlerinin ürün inançlarını yönlendirdiğini gösteriyor (Türkiye'de üretilmiş ürünler üzerine İsveç/Hollanda karşılaştırmalı çalışması) | Kazanabileceğin kanal duygusal olan. "Anadolu zanaat geleneği" duygusal bir varlık. Çıplak bir etiket olarak "Made in Turkey" bilişsel bir yükümlülük. İlkiyle öne çık |
| Türkiye'nin kendi devlet programı (Turquality) tam olarak Türk ürünlerinin kalitenin tek başına kapatmadığı bir marka-algı açığı taşıdığı için var | Açığın gerçek ve yapısal olduğunu, hayal olmadığını teyit ediyor |
| **Le Châle Bleu**, bir Fransız lüks markası, "Fransa'da elle çizildi, İtalya'da (Como) üretildi"yi €39–169 bandında açıkça satıyor | Bölünmüş-menşe hikâyesi bu kategoride kanıtlanmış, premium-uyumlu bir yapı. Hiçbir şey icat etmiyorsun |

**İşleyen kurgu:** İspanyol ya da Fransız tescilli şirket, Avrupalı marka adı, AB fulfilment, ürün sayfasında ve etikette "Designed in Seville / Made in Türkiye" (AB tekstil etiketleme mevzuatı zaten menşe konusunda doğru olmanı gerektiriyor — §20) ve zanaat-spesifik anlatı: dokuma tesisi, doku, elle kıvrılmış kenar, adıyla. §10 bunu düzgün işliyor.

## 3.5 Fransız rakipler ve fiyatlar

Tam tablo §11'de. Kısa versiyon: Fransa, Avrupa'nın en yoğun şal-markası pazarı.

| Marka | Konumlandırma | Fiyat (doğrulama durumu) |
|---|---|---|
| Hermès | Kategorinin fiyat tavanı ve kültürel referansı | **€580** (90 cm karé) — üç yıl önce ~€460; %7–10 artışlar, Şub 2025 zammı *(agregatör/basın)* |
| Petrusse (Made in France) | Yerleşik premium | **$395** (105 cm) / **$215** (65 cm) ≈ €364 / €198; **eurozone'da €190 üzeri ücretsiz kargo** *(ürün sayfası, USD store)* |
| Philéone (Made in France) | Erişilebilir premium — **senin doğrudan rakibin** | Fularlar **€42–95**; Emmanuelle ve Sylvia ikisi de **€68**; elle boyanmış şal €98; tüm aralık €35–190 *(ürün sayfası)* |
| Le Châle Bleu (FR tasarım, IT üretim) | Erişilebilir premium, bölünmüş menşe | **€39–169** *(agregatör)*; kargo Fransa içi €7,10 *(site)* |
| monfoulardensoie.fr | Fransız ipek fular perakendecisi | **€70,90–75,90** *(agregatör)* |
| Genel Fransız pazar referansı | 50×50 cm kaliteli saf ipek "gavroche" | **~€40 beklenen fiyat** *(sektör yorumu)* |
| Sézane | Mass-premium Fransız DTC | Cleopatra ipek fular 52×52 cm; EUR fiyat **DOĞRULANMADI**. RealReal'de ikinci el $85–155 |
| Soeur, SOI Paris, Fleuron Paris, Foularchic (70×70), Lollipops, Balaboosté | Orta–erişilebilir premium DTC / Instagram-doğumlu | **DOĞRULANMADI** — canlı kontrol gerekiyor |

**Kritik bulgu: €68, bağımsız bir Fransız markasının Fransa'da üretilmiş ipek fuları için doğrulanmış, dolu bir fiyat noktası (Philéone).** Bunu menşe üzerinden yenemezsin. Creative, offer mimarisi ve hediye sunumu üzerinden yenebilirsin — avantajın da tam orada.

---

# 4. İSPANYA vs FRANSA — YAN YANA

| Metrik | İspanya | Fransa | Farkın nedeni ve önemi |
|---|---|---|---|
| **Moda e-ticaret büyüklüğü** | ≈€9,1 milyar (9.863M USD) **[satıcı tahmini]**; giyim = 2025 Q4 e-tic. cirosunun %7'si ≈ çeyrekte €2,2 milyar (CNMC) | **€7,7 milyar online giyim** (FEVAD, resmî) | Fransa'nın rakamı resmî ve daha dar (sadece giyim); İspanya'nın daha geniş bir tanım üzerinde satıcı tahmini. **"İspanya > Fransa" sonucuna varma.** Karşılaştırılabilir sadece-giyim tanımında Fransa muhtemelen daha büyük |
| **Kadın modası büyüklüğü** | Kadın modası = en çok satan online moda kategorisi, alıcıların ~2/3'ü | FEVAD ayrıca yayınlamıyor | İkisi de kadın-ağırlıklı; ikisi de net kadın-özel rakam vermiyor. İkisinde de ~%55–60 kadın payı varsay |
| **Aksesuar pazarı** | Kamusal şal/aksesuar izolatı yok | Aksesuar + ayakkabı = **€34,7 milyarın %10'u ≈ €3,5 milyar** (IFM) | Fransa'nın aksesuar pazarı daha iyi ölçümlenmiş. Boyutlandırma için faydalı, hedefleme için değil |
| **Online moda penetrasyonu** | Moda perakendesinin %25–30'u **[satıcı tahmini]** | **Tüm giyim tüketiminin %30,7'si** (FEVAD, resmî) | Fransa dijital kaymada daha ileri. Daha normalleşmiş satın alma, aynı zamanda daha rekabetçi |
| **Ortalama moda AOV'si** | **Kadın online moda sepeti €70'in hemen altı** | **Tüm-kategori sepet €62, %3 düşüyor; moda sepeti −%4,2** | Belirleyici. €59,90 İspanyol kadın moda davranışının *içinde*, Fransız ortalama sepetinin *üstünde*. İspanya hedef fiyatını daha iyi destekliyor |
| **Kadın alıcı payı** | Online moda alışverişçilerinin **%56,5'i** | Yayınlanmamış; Instagram %54,4 kadın | Karşılaştırılabilir. İki tarafta da avantaj yok |
| **Premium konumlandırma potansiyeli** | **Orta-iyi.** Premium-şal rekabeti daha seyrek; El Corte Inglés ve Massimo Dutti orta-premium'u çapalıyor; **Fio de Martié 90×90'ı €94,90'a satarak tavanı kanıtlıyor** — ama **Massimo Dutti %100 ipeği €29,95'e satıyor** | **Yüksek tavan, yüksek zorluk.** Hermès yerli; Philéone €68'e Made-in-France; Vinted %21,4 ile premium ikinci el besliyor | İspanya'da premium seçenek *olma* alanı var. Fransa'da en ucuz premium seçenek olursun ki bu daha kötü bir yer |
| **Rekabet** | Orta. Perakende-öncülüklü (El Corte Inglés, Cortefiel, Massimo Dutti) + zanaatkâr DTC (Fio de Martié, Hamzah, Julunggul, Munira) | **Ağır.** Hermès, Petrusse, Philéone, Le Châle Bleu, Fleuron, Soeur, SOI Paris, Sézane, Foularchic, Lollipops, Balaboosté + Vinted resale + Etsy | Fransa'da Avrupa'nın herhangi bir pazarından daha fazla doğrudan DTC şal markası var. İspanya'nın rekabeti çoğunlukla perakende zincirleri — onlar seninle Meta creative'de dövüşmüyor |
| **Meta Ads potansiyeli** | **Daha iyi.** İspanya ortalama CPM'i **~€6** olarak bildirilmiş (tüm sektör; soğuk e-tic. dönüşüm için €10–18 bekle). Daha ucuz açık artırma | Paris CPM'leri Batı Avrupa'nın en yükseklerinden; Kademe-1 aralığı $10–23 CPM | Aynı euroyla İspanya'da daha çok creative iterasyonu alıyorsun. Creative-öncelikli bir operatör için iki pazar arasındaki en değerli fark bu |
| **Google Ads potansiyeli** | Daha düşük arama hacmi, daha ince premium-şal niyeti | **Daha yüksek.** "foulard" gerçek markalı/jenerik ekosistemiyle köklü bir Fransız arama davranışı | Fransa belirgin şekilde daha iyi Google pazarı. Avrupa Shopping CPC'si iki tarafta da €0,29–0,35 (smec) |
| **Tüketici satın alma gücü** | Hane geliri €42.269 (2024); harcama €35.101/hane. **Giyim harcaması düşüyor (hane başı −€16, bütçenin %4,03'ü)** | Daha yüksek kişi başı GSYH; **Noel bütçesi 9 yılın en düşüğü (€491)**; CSP+ €517 | İkisi de yumuşak. Fransa daha zengin ama şu anda harcanabilir harcamada daha savunmacı |
| **Kargo karmaşıklığı** | **Düşük.** Stok tuttuğunda yurt içi: SEUR ~€5,40'tan, GLS ~24 saat, Correos + 8.000 CityPaq locker. Canarias/Ceuta/Melilla'yı dışla | **Orta.** Sınır ötesi ES→FR parça başına ~€1 ve 1–2 gün ekliyor; eninde sonunda Fransız 3PL veya Colissimo/Mondial Relay entegrasyonu gerekiyor | İspanya belirgin şekilde daha basit ve İspanya'da depolarsan sipariş başına ~€1 daha ucuz |
| **İadeler** | Kategori avantajı: beden yok → %5–10 bekle, %20–40 giyim bandının çok altında. İspanyol alışverişçi **ücretsiz kargoyu #1 sıralıyor (~%65)** mağaza seçiminde | Aynı kategori avantajı. Ama **Vinted iadenin yerine resale'i normalleştiriyor**; Fransız tüketici hukukî olarak daha bilinçli | İkisi de şal için zararsız. İadeler bu işin riski değil — CAC riski |
| **KDV / vergi karmaşıklığı** | **%21 KDV.** €10.000 AB genelinde mesafeli satış eşiğini geçince OSS kapsar | **%20 KDV.** Aynı OSS mekanizması | Marjinal: Fransa'nın düşük KDV'si €59,90'lık siparişte ~€1,00 fazla katkı demek (§7). Belirleyici faktör değil |
| **Regülasyon giriş maliyeti** | **Tekstil EPR hâlâ taslak.** Kraliyet Kararnamesi 23 Haz 2025'te yayınlandı, 27 May 2026'da Komisyona bildirildi, standstill 28 Ağu 2026'ya kadar, kabul 2026'da bekleniyor. Yürürlüğe girdiğinde muafiyet eşiği yok | **Yürürlükte ve uygulanıyor.** Refashion EPR + **ADEME UIN satış yapmanın ön koşulu** (pazar yerleri dahil); **Triman + info-tri 1 Şub 2023'ten beri giyimde zorunlu**; **Fransa'da yerleşik olmayan üretici yazılı vekâletle Fransız temsilci atamak zorunda (10 Tem 2026'dan beri)**; eko-katkı ~€0,58/giysi (2026 basitleştirilmiş oran) | **Belirleyici operasyonel fark bu.** Fransa'da ilk satıştan *önce* geçmen gereken sert bir kapı var: UIN, vekâletli Fransız temsilci, etiket ve ambalajda Triman görseli. İspanya'nın muadili henüz yürürlükte değil. Fransa ciro öncesi haftalar ve ücret götürüyor |
| **Q4 fırsatı** | **Üstün.** Kişi başı €796 bayram harcaması, €370 hediye, hediye alımlarının %43'ü moda, 10'da 8 kişi BF'yi hediye için kullanıyor, erken alıcı +€140 | İyi ama yumuşuyor. €491 bütçe (9 yılın en düşüğü), €297 hediye, rekor 9 hediye = daha düşük birim değer | İspanya'nın Q4'ü hem kişi başına daha büyük hem €50–80'lik hediye için daha uygun şekilli |
| **Noel hediyeleşme potansiyeli** | **Olağanüstü ve daha uzun.** **Reyes (€192) > Noel arifesi (€178)** — sezon 5 Ocak'a kadar, ikinci bir zirveyle | Tek 24–25 Aralık zirvesi; daha çok hediye, daha düşük değer | İspanya sana neredeyse hiç rakibin çalışmadığı, çökmüş CPM'li ~3 hafta fazla satış penceresi veriyor |
| **Pazara giriş zorluğu** | **Düşük-orta.** Orada yaşıyorsun, dili biliyorsun, KDV tek kayıt, EPR henüz bağlayıcı değil, CPM daha ucuz | **Orta-yüksek.** Uyum kapısı, yoğun rekabet, yüksek CPM, pazar yeri tercihi, fiyatının altında sepet | Net |

**Hedging yapmadan sonuç: Önce İspanya, tek başına.** İspanya'nın daha büyük pazar olması sebebiyle değil — sadece-giyim resmî verisinde muhtemelen değil. İspanya birinci, çünkü **€5.000'lik bir testin temiz sinyal üretip üretmeyeceğini belirleyen her operasyonel ve ekonomik değişken orada daha iyi:** daha ucuz açık artırma (euro başına daha çok creative iterasyonu), launch öncesi uyum kapısı yok, hedef fiyatını kuşatan bir kadın moda sepeti, 3 hafta daha uzun bir Q4, yurt içi 24 saat teslimat ve pazarın kendi dilinde sahada sen.

Fransa, *farklı bir hero SKU ve daha düşük fiyatla*, İspanya kârıyla finanse edilerek, Refashion ve temsilci evrakı önceden bitirildikten sonra girilecek bir 2027 genişlemesi.

---

# 5. ŞAL / FULAR ÜRÜN PAZARI

## 5.1 Kategori seviyesinde talep kanıtı

| Kanıt | Detay | Kaynak |
|---|---|---|
| Global şal & atkı pazarı | 26,22 milyar USD (2025) → 28,04 milyar (2026) → 56,37 milyar (2034), %9,12 CAGR | Fortune Business Insights **[satıcı tahmini — sadece yön gösterir]** |
| **Moda trend durumu** | İpek fular **2026 ilkbaharın en büyük aksesuar trendi** ilan edilmiş; "2026 fular yılı" | WWD, Marie Claire UK |
| SS26 podyum doğrulaması | **Totême, Dries Van Noten, Maria McManus, Maison Magdalena** — püsküllü uzun ipek fularlar; ince akışkan fularlar | WWD |
| 2026 styling yönü | Fular **odak noktası** olarak (2025 minimalist aksandı): daha büyük ölçüler, iki yüzlü baskılar, etek/kemer/şal olarak, çantada, saçta | Marie Claire UK, WWD |
| 2026 renk yönü | Yoğun kırmızı, derin mavi, jade yeşili; 70'ler zincirleri, binicilik motifleri, barok baskılar, elle boyama, suluboya çiçek | Trend analizleri |
| **Arama sezonluğu** | "Silk scarf" yıl boyu en yüksek hacimli terim, **Ekim (81) ve Aralık (85)** zirveleri. "Wool scarf" **Aralık (96)** zirvesi, Ağustos'ta 21. "Designer scarf" Ekim'den Aralık'a 7 → 30 | Google Trends analizleri |
| **AB'nin Türkiye'den HS6214 ithalatı** (şal, fular, atkı, mantilla, peçe) | **2025'te 8,42 milyon USD** ≈ €7,7 milyon | Trading Economics |

**Pazar büyüklüğü rakamından daha önemli iki gözlem.**

**Birincisi, trend gerçek ve şimdi.** Bunu bir blogdan okumuyorum. İsmi geçen SS26 podyum evleri, WWD ve Marie Claire editöryeli, ve tam satmak istediğin Eki–Ara penceresinde zirve yapan arama ilgisi. Kategori rüzgârı creative-öncelikli bir launch için gerçek bir varlık, çünkü trend-komşusu creative ucuz organik dağıtım alıyor. **Ama aynı zamanda bir saat.** Aksesuarda trendler 18–30 ay sürüyor. 2026 Q4'te girersen ön fazda değil orta-son fazda giriyorsun. Bu, hızlı hareket etmeyi ve trendin ötesine geçecek bir sahip olunan varlık (e-posta listesi, tekrar eden müşteri) kurmayı savunuyor; uzun bir inşayı değil.

**İkincisi, o 8,42 milyon $ ithalat rakamı bu raporun en ilginç sayısı.** AB'nin *Türkiye'den* toplam şal ithalatı 2025'te €8 milyonun altındaydı. Karşılaştırma: tek başına İspanyol giyim e-ticareti çeyrekte ~€2,2 milyar. İki yönlü kesiyor:

- **Ayı okuması:** Türkiye Avrupa'ya büyük bir şal tedarikçisi değil. Türk şalı harika bir arbitraj olsaydı daha çok kişi yapıyor olurdu.
- **Boğa okuması, bence doğru olan:** şerit *boş*. Yerinden etmen gereken yerleşik bir Türkiye-kaynaklı Avrupa şal markası yok. Kalabalık bir arbitraja değil, işlenmemiş bir arbitraja giriyorsun. Rakam ayrıca serbest dolaşımdaki mallar ve küçük koliler tutarsız yakalandığı için muhtemelen akışı olduğundan az gösteriyor.

## 5.2 Ürün ürün analiz

Aşağıdaki fiyatlar **rakip taramasında (§11) gözlenen pazar perakende bantları**, benim önerilerim değil. "Premium perakende" = iyi sunumu ve hikâyesi olan bağımsız bir markanın tutabileceği fiyat. Kargo ağırlıkları tipik konstrüksiyondan tahmin; tedarikçinin gerçek spec'iyle doğrula.

| Ürün | Malzeme gerçeği | Tipik perakende | Premium perakende | Zirve sezon | Müşteri profili | Hediye potansiyeli | Algılanan değer | Rekabet | İade riski | Kargo ağırlığı | Upsell potansiyeli |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **İpek fular (90 cm karé)** | Dut ipeği twill, elle kıvrılmış kenar | €30–95 | **€69–99** | **Eki + Ara zirveleri; yıl boyu taban** | 35–55, klasik, marka-okuryazar | **Çok yüksek** | **Kategoride en yüksek** — "ipek" değer kelimesi | Ağır (Hermès referansı, Philéone €68, **Massimo Dutti €29,95**) | Düşük (%5–7) | 60–90 g | Yüksek — ring, kutu, ikinci renk |
| **İpek fular (65 cm / küçük kare)** | Aynı kumaş, daha azı | €17–55 | **€49–69** | İlkbahar + Aralık | 28–45, saç/çanta styling | Yüksek | İyi — düşük fiyatta premium okunuyor | Yüksek | Düşük | 30–45 g | **En yüksek — ideal 2'li paket ve add-on** |
| **Saten fular** | Polyester saten; ipek *görünümü*, ipek dokusu değil | €15–30 | €29–39 | Eki–Ara | 25–35, fiyat ve trend odaklı | Orta | **Kırılgan** — "saten" bilgili alıcıya sentetik sinyali verir | Çok yüksek (Zara/H&M/Shein) | Düşük | 40–70 g | Orta |
| **Pamuk fular** | Pamuk vual/lawn, genelde baskılı | €20–40 | €34–49 | İlkbahar/yaz; Aralık'ta en zayıf | 30–50, casual-elegant, Akdeniz | Orta | Orta — dürüst, lüks değil | Yüksek | Düşük | 80–120 g | Orta |
| **Kaşmir fular** | %100 kaşmir veya yün-kaşmir karışım | €39–120 | **€89–149** | **Kas–Şub** | 40–60, kalite-öncelikli, hediye | **Çok yüksek** | **Çok yüksek** — en güçlü "değer" malzemesi | Orta (ARKET ~£85/≈€98 — ilk düşündüğümden yumuşak) | Düşük | **200–350 g** | Yüksek — eldiven, bere, uyumlu set |
| **Yün fular** | Merino/lambswool, dokuma veya örme | €25–60 | €59–89 | **Kas–Şub** | 30–55, pratik-premium | Yüksek | İyi | Yüksek | Düşük | **180–300 g** | Yüksek |
| **Modal fular** | Modal veya modal-ipek karışım; mükemmel drape, düşük maliyet | €20–40 | €39–59 | Yıl boyu | 28–45 | Orta | Orta — tüketici kelimeyi bilmiyor | Orta | Düşük | 70–110 g | Orta |
| **Viskon fular** | Viskon/rayon; en ucuz premium-*görünen* seçenek | €12–30 | €29–39 | Yıl boyu | 25–40, fiyat odaklı | Düşük-orta | **Zayıf** — adı söylendiğinde ucuz okunuyor | Çok yüksek | Düşük | 60–100 g | Düşük |
| **Oversize şal / stola** | Yün, kaşmir karışım veya modal-ipek; 200×70 cm+ | €45–120 | **€89–139** | **Kas–Oca** | 40–65, akşam/seyahat | **Çok yüksek** | **Çok yüksek** — boyut değer okunuyor | Orta | Düşük-orta | **250–400 g** | Yüksek — hediye kutusu, seyahat kesesi |
| **Şık uzun baskılı fular** | İpek dokulu veya modal, 180×70 cm | €30–70 | €59–79 | Eyl–Ara | 30–55 | Yüksek | İyi | Yüksek | Düşük | 80–140 g | Yüksek |
| **Kışlık kalın örgü atkı** | Yün/akrilik karışım örme | €20–50 | €49–69 | **Sadece Kas–Oca** | 25–45 | Orta-yüksek | Orta | Çok yüksek | Düşük | **250–450 g** | Orta |
| **Hafif fular** | Pamuk-ipek, modal, vual | €20–45 | €39–59 | **Mar–Eyl** | 28–50 | Orta | Orta | Yüksek | Düşük | 50–90 g | Orta |
| **Baş fuları / bandana** | İpek veya pamuk kare, 50–55 cm | €17–48 | €34–49 | İlkbahar/yaz | 22–38, styling odaklı, güçlü TikTok uyumu | Orta | Orta | Yüksek (Etsy dahil) | Düşük | 25–40 g | **Yüksek — doğal 3'lü paket** |
| **Boyun fuları / twilly** | İnce ipek bant, 5–120 cm | €15–35 | €29–45 | Yıl boyu; **Aralık hediye zirvesi** | 25–45, çanta styling | **Yüksek** — klasik impulse hediye | İyi — lükse komşu format | Orta | **Çok düşük** | **10–20 g** | **En yüksek — saf marj add-on** |
| **Lüks fular (konumlandırma, malzeme değil)** | Savunabildiğin her şey | €90–200 | €149–249 | Aralık | 45–65 | Çok yüksek | Tamamen henüz sahip olmadığın marka değerine bağlı | Hermès/Ferragamo ile doğrudan — birinci yılda buraya girme | Düşük | değişir | — |
| **Baskılı fular (tasarım odaklı)** | Herhangi bir taban; ürün baskının kendisi | €30–95 | €59–99 | Eki–Ara | 30–55, tasarım bilinçli | Yüksek | **İyi — ve en savunulabilir**, çünkü sana özel bir baskı fiyat-karşılaştırılamaz | Orta | Düşük | değişir | Yüksek — baskı ailesi / koleksiyon |

## 5.3 Gerçekte hangi ürünü launch etmeli

**Hero SKU: sana özel baskılı, elle kıvrılmış kenarlı 90 cm ipek-dokulu kare, €59,90.** Gerekçe:

- **"İpek" değer kelimesi** ve ipek kareler kategoride en yüksek algılanan değeri taşıyor.
- **Sana özel bir baskı, elindeki tek savunulabilir hendek.** Düz bir kaşmir fular anında ARKET'le karşılaştırılıyor ve kaybediyorsun. **Massimo Dutti %100 ipeği €29,95'e satıyor — düz ipekte de kaybediyorsun.** Kimsede olmayan bir baskı fiyat-karşılaştırılamaz — ve baskı tasarımı AI görsel hattının gerçekten iyi olduğu bir iş.
- **60–90 g kargo ağırlığı** seni en ucuz koli kademesinde ve €150 IOSS/gümrük eşiğinin çok altında tutuyor.
- **Ekim *ve* Aralık arama zirveleri** sana bir değil iki talep penceresi veriyor.
- İade riski düşük (beden yok) — tüm birim ekonomi modelini hayatta tutan şey bu.

**İkinci SKU (aynı anda launch et, AOV motorun): ince twilly / boyun fuları, €24,90–29,90.** 10–20 g, neredeyse sıfır ek kargo, saf marj ve "€24,90'a ekle" post-purchase upsell'in doğal adayı. §15–16 bunun üstüne kuruyor.

**Birinci yılda launch etmeyeceklerin:** kaşmir (ARKET/& Other Stories gerçek marka güveniyle altını kesiyor), saten veya viskon *adıyla* (premium iddianı öldürür) ve "lüks fular" €149+ bandı (savunacak marka değerin yok).

---

# 6. FİYAT KONUMLANDIRMA

## 6.1 Fiyat merdiveni, değerlendirilmiş

Aşağıdaki break-even CAC §7'deki modelden geliyor (İspanya, %21 KDV, €8,00 landed COGS, €2,00 ambalaj, €1,80 pick/pack, €4,20 yurt içi kargo, %2,5 + €0,25 ödeme komisyonu, €0,20 EPR karşılığı, %10 iade oranı). "Maks CAC" gerçek kısıt: bir siparişi kazanmak için ödeyebileceğin ve yine sıfır kâr edeceğin en yüksek tutar.

| Brüt fiyat | KDV hariç | Katkı | Katkı %net | **Maks CAC** | Dönüşüm potansiyeli | Algılanan kalite | Premium algı | Marj potansiyeli | Hediye potansiyeli | Karar |
|---|---|---|---|---|---|---|---|---|---|---|
| €19,90 | €16,45 | **−€0,50** | **−%3** | **−€1,58** | Çok yüksek | Düşük | Yok | **Negatif** | Düşük | **Yapısal olarak imkânsız.** Reklam öncesi zarar ediyorsun |
| €24,90 | €20,58 | €3,51 | %17 | **€2,02** | Çok yüksek | Düşük | Yok | İhmal edilebilir | Düşük | **Tek başına imkânsız.** Sadece CAC'in ödendiği mevcut bir siparişe **€24,90 add-on** olarak mantıklı — zaten kullanım şekli bu |
| €29,90 | €24,71 | €7,51 | %30 | **€5,61** | Yüksek | Düşük-orta | Zayıf | Çok ince | Orta | Sadece add-on veya sert upsell'li zararına front-end olarak. Paid trafikte alınamaz |
| €34,90 | €28,84 | €11,52 | %40 | **€9,21** | Yüksek | Orta | Zayıf | İnce | Orta | Zara/Mango bölgesi. €9 CAC Meta soğuk trafikte ulaşılamaz. **Hayır** |
| €39,90 | €32,98 | €15,53 | %47 | **€12,80** | Orta-yüksek | Orta | Oluşuyor | Uygulanabilir | Orta-yüksek | Sınırda. €12,80 CAC olağanüstü creative *ve* %3+ CVR gerektiriyor. Hero değil, promosyon veya bundle bileşeni olarak kullan |
| €44,90 | €37,11 | €19,53 | %53 | **€16,39** | Orta | Orta-yüksek | Orta | İyi | Yüksek | Hero için uygulanabilir taban. Sıkı ama gerçek |
| **€49,90** | €41,24 | €23,54 | **%57** | **€19,99** | Orta | **Yüksek** | **İyi** | **İyi** | **Yüksek** | **Uygulanabilir hero fiyatı. Muhafazakâr seçim.** Hamzah'ın üst bandı (€49) ile aynı hizada |
| **€59,90** | €49,50 | €31,56 | **%64** | **€27,18** | Orta | **Yüksek** | **Güçlü** | **Güçlü** | **Çok yüksek** | **★ Önerilen hero fiyatı.** İspanyol kadın moda sepetinin içinde (€70 altı), Philéone'nin €68'inin altında, Fio de Martié'nin €94,90'ının çok altında, hızlı moda tavanının üstünde. CAC payı ve dönüşüm arasında en iyi denge |
| €69,90 | €57,77 | €39,57 | %69 | **€34,36** | Orta-düşük | Çok yüksek | Çok güçlü | Çok güçlü | Çok yüksek | **Önerilen ikinci kademe / hediye seti fiyatı.** Görünür kalite ipuçları gerekiyor (kutu, kenar, gramaj, baskı hikâyesi). Philéone'nin €68'iyle tam karşı karşıya — sunumla kazanmak zorundasın |
| €79,90 | €66,03 | €47,59 | %72 | **€41,55** | Düşük-orta | Çok yüksek | Çok güçlü | Mükemmel | Çok yüksek | Hediye seti ve 2'li paket bölgesi. Bilinmeyen bir markadan *tek* fular olarak birinci yılda zor satış |
| €89,90 | €74,30 | €55,60 | %75 | **€48,74** | Düşük | Çok yüksek | Mükemmel | Mükemmel | Çok yüksek | Sadece çok ürünlü hediye seti veya oversize kaşmir şal olarak. Tek 90 cm kare olarak değil |
| €99,90 | €82,56 | €63,61 | %77 | **€55,93** | Düşük | Mükemmel | Mükemmel | Mükemmel | Mükemmel | Sadece koleksiyon/bundle. €99,90 ortalama İspanyol kadın moda sepetinin ~1,4 katı |

## 6.2 Çekirdek soru: €4–10 landed → €39,90–69,90 gerçekçi mi?

**Evet, ve agresif olan kısım çarpan değil.** Landed maliyet üzerine 6–8 kat markup moda aksesuarında *standart*, istisnai değil. Agresif olan, o çarpanın finanse etmesi gereken CAC.

| Landed COGS | @ €39,90 | @ €49,90 | @ €59,90 | @ €69,90 |
|---|---|---|---|---|
| **€5,00** | 8,0x markup, maks CAC **€15,53** | 10,0x, **€22,72** | 12,0x, **€29,91** | 14,0x, **€37,09** |
| **€7,00** | 5,7x, **€13,71** | 7,1x, **€20,90** | 8,6x, **€28,09** | 10,0x, **€35,27** |
| **€10,00** | 4,0x, **€10,98** | 5,0x, **€18,17** | 6,0x, **€25,36** | 7,0x, **€32,54** |

*(Hepsi %10 iade oranında. %5/15/20 dahil tam grid §7.3'te.)*

**Belirleyici gözlem: COGS neredeyse önemsiz.** Landed maliyeti €10'dan €5'e indirmek — %50'lik bir tedarik iyileştirmesi, zor bir müzakere — sana **€59,90'da €4,55 ek CAC payı** kazandırıyor. Perakende fiyatını €49,90'dan €59,90'a çıkarmak — tek bir fiyatlama kararı — **€7,19** kazandırıyor. Ve CVR'yi %1,8'den %2,6'ya çıkarmak CAC'i kabaca **yarıya indiriyor**.

Kaldıraçlar, çaba birimi başına etkiye göre sıralı:

1. **Conversion rate** (CAC'i yarıya indirir) — landing page, offer, sosyal kanıt
2. **AOV / bundle mimarisi** (tavanı oransal yükseltir) — §16
3. **Perakende fiyatı** (her €10 fiyata +€7 pay, dönüşüm korunursa)
4. **Creative CTR** (CAC'le oransal)
5. **COGS** (%50'lik tedarik kazancı için +€4,55) — **ilk optimize etmeyi planladığın şey en az değerli kaldıraç**

Bu yeniden sıralama, bence bu raporun en faydalı tek çıktısı.

## 6.3 Psikolojik fiyatlama notları

- **€59,90, €60 değil.** Charm pricing AB modasında hâlâ ölçülebilir şekilde çalışıyor; €59,90 "ellili" okunuyor.
- **€.99 sonu kullanma.** ES/FR'de €59,99 indirim perakendesi sinyali verir; €59,90 veya yuvarlak €60 marka sinyali verir. .90 kuralı İspanyol ve Fransız premium perakende normu.
- **Asla sahte RRP ile çapa atma.** AB Omnibus Direktifi'nin önceki-fiyat referansı kuralları uygulanıyor; gerçek 30 günlük önceki fiyatı olmayan "€120 idi, şimdi €59,90" haksız ticari uygulama ve İspanyol tüketici otoriteleri bunun üzerine gidiyor.
- **Çizgili fiyatla değil, setle çapa at.** €139,90 koleksiyonu önce göster; €59,90 o zaman erişilebilir seçenek olarak okunur. Bu yasal, kalıcı ve AOV'yi yükseltiyor.

---

# 7. BİRİM EKONOMİSİ (UNIT ECONOMICS)

## 7.1 Maliyet yığını varsayımları

| Satır | İspanya | Fransa | Dayanak |
|---|---|---|---|
| KDV | **%21** | **%20** | Standart oranlar; €10.000 AB mesafeli satış eşiği geçilince OSS ile raporlanır |
| Landed ürün maliyeti | €5 / €7 / €10 modellendi; **€8 baz** | aynı | Türk fabrika-direkt €1,90/adetten (Hicabistan, renk başına 10 MOQ); 50–100 adet MOQ'da FOB 3–4 $; 1.000 adet MOQ'da ipek €1,50–2/adet. €8 baz, giriş kademesinden iyi kumaş + özel baskı + dokuma etiket + iç navlun + gümrük işlemi varsayıyor |
| Ambalaj | **€2,00** (zarf, pelür, kart, sticker) / sert hediye kutusuyla €5,50 | aynı | Pazar oranları; hediye kutusu premium algı satın alma kalemi |
| Pick & pack (3PL) | **€1,80** | €1,80 | Avrupa 3PL pick & pack €1,50–2,50/sipariş |
| Giden kargo | **€4,20** | **€5,20** | İspanya yurt içi: SEUR liste ~€5,40'tan, GLS ~24 saat — €4,20 pazarlıklı hafif koli oranı varsayıyor. FR ~€1 sınır ötesi ekliyor. Avrupa all-in fulfilment benchmark'ı €4–8/sipariş |
| Ödeme komisyonu | **%2,5 + €0,25** | aynı | Kart + Bizum/PayPal harmanı |
| EPR / eko-katkı | **€0,20 karşılık** | **€0,58** | FR Refashion 2026 basitleştirilmiş oranı ~€0,58/giysi. ES kararnamesi henüz yürürlükte değil — €0,20 ihtiyatlı karşılık |
| İade oranı | %5/10/15/20 modellendi; **%10 baz** | aynı | Giyim %20–40 (AB merkez ~%30, Landmark/IPC 2025'e göre %46'ya kadar) ama **giyim iadelerinin ~%50'sinin nedeni uyum/beden ve şalın bedeni yok.** %10 benim bazım; %5 makul; güvenlik için %20'ye kadar modelledim |
| Bir iade siparişinin maliyeti | **€12,20** | — | Kaybedilen giden kargo €4,20 + iade bacağı €4,50 + iade edilmeyen PSP komisyonu €1,75 + kontrol/raf €1,00 + iade edilen üründe %10 zayi €0,80 |

## 7.2 Tam maliyet yığını, €59,90 tek ürün (İspanya)

| Satır | € | Brütün %'si | Netin %'si |
|---|---|---|---|
| **Brüt gelir (KDV dahil)** | **59,90** | %100,0 | — |
| KDV (%21) | (10,40) | %17,4 | — |
| **Net gelir** | **49,50** | %82,6 | %100,0 |
| Landed COGS | (8,00) | %13,4 | %16,2 |
| Ambalaj | (2,00) | %3,3 | %4,0 |
| Pick & pack | (1,80) | %3,0 | %3,6 |
| Giden kargo | (4,20) | %7,0 | %8,5 |
| Ödeme komisyonu | (1,75) | %2,9 | %3,5 |
| EPR karşılığı | (0,20) | %0,3 | %0,4 |
| **Toplam değişken maliyet** | **(17,95)** | %30,0 | %36,3 |
| **Reklam ve iade öncesi katkı** | **31,56** | %52,7 | **%63,7** |
| İade yükü (%10) | (4,38) | | |
| **İade sonrası katkı = MAKS CAC** | **27,18** | **%45,4** | **%54,9** |

**Bu yapıda break-even blended ROAS: 2,14x.** 2,14x'in altındaki her şey sermaye yakıyor.

## 7.3 Break-even CAC gridi — fiyat × COGS × iade oranı (İspanya)

**Landed COGS €5,00**

| Fiyat | İade %5 | %10 | %15 | %20 |
|---|---|---|---|---|
| €29,90 | €9,43 | €8,34 | €7,26 | €6,17 |
| €39,90 | €17,03 | €15,53 | €14,03 | €12,53 |
| €49,90 | €24,63 | €22,72 | €20,81 | €18,89 |
| **€59,90** | **€32,23** | **€29,91** | €27,58 | €25,26 |
| €69,90 | €39,83 | €37,09 | €34,36 | €31,62 |
| €79,90 | €47,43 | €44,28 | €41,13 | €37,98 |

**Landed COGS €7,00**

| Fiyat | İade %5 | %10 | %15 | %20 |
|---|---|---|---|---|
| €29,90 | €7,52 | €6,52 | €5,53 | €4,53 |
| €39,90 | €15,12 | €13,71 | €12,30 | €10,89 |
| €49,90 | €22,72 | €20,90 | €19,08 | €17,25 |
| **€59,90** | **€30,32** | **€28,09** | €25,85 | €23,62 |
| €69,90 | €37,92 | €35,27 | €32,63 | €29,98 |
| €79,90 | €45,52 | €42,46 | €39,40 | €36,34 |

**Landed COGS €10,00**

| Fiyat | İade %5 | %10 | %15 | %20 |
|---|---|---|---|---|
| €29,90 | €4,65 | €3,79 | €2,93 | €2,07 |
| €39,90 | €12,25 | €10,98 | €9,71 | €8,43 |
| €49,90 | €19,86 | €18,17 | €16,48 | €14,79 |
| **€59,90** | **€27,46** | **€25,36** | €23,26 | €21,16 |
| €69,90 | €35,06 | €32,54 | €30,03 | €27,52 |
| €79,90 | €42,66 | €39,73 | €36,81 | €33,88 |

**Nasıl okunur:** en kötümser köşede bile (€10 COGS, %20 iade, €59,90) hâlâ **€21,16 CAC payın** var. Model tedarik ve iade şoklarına dayanıklı. **€30'un üstündeki bir CAC'e dayanıklı değil.** Bu işin riski tamamen acquisition satırında yaşıyor.

## 7.4 Aynı brüt fiyatta İspanya vs Fransa

| Fiyat | İspanya net | İspanya maks CAC | Fransa net | Fransa maks CAC | Δ |
|---|---|---|---|---|---|
| €49,90 | €41,24 | €19,99 | €41,58 | €18,96 | **−€1,03** |
| €59,90 | €49,50 | €27,18 | €49,92 | €26,21 | **−€0,97** |
| €69,90 | €57,77 | €34,36 | €58,25 | €33,46 | **−€0,91** |

Fransa'nın 1 puanlık KDV avantajı (€59,90'da €0,34 fazla net), €0,58 Refashion eko-katkısı ve ~€1,00 daha yüksek sınır ötesi kargo tarafından **fazlasıyla iptal ediliyor. Fransa, İspanya deposundan sipariş başına ~€1 daha kötü** — daha yüksek CPM'leri ve uyum kurulum maliyetini saymadan. Fransa'da yerel stok tuttuğunda bu hafifçe pozitife dönüyor ama bunun için birinci yılda olmayacak hacim gerekiyor.

## 7.5 Bundle ekonomisi — bu iş gerçekte burada para kazanıyor

| Offer | Brüt | COGS | Katkı | Katkı %net | **Maks CAC** |
|---|---|---|---|---|---|
| 1 fular | €59,90 | €8,00 | €31,56 | %63,7 | **€27,18** |
| Fular + fular ringi | €74,90 | €10,50 | €40,48 | %65,4 | **€35,13** |
| **Hediye seti (fular + ring + sert kutu)** | **€89,90** | €10,50 | **€49,00** | **%66,0** | **€42,72** |
| 2'li fular bundle | €99,90 | €16,00 | €54,71 | %66,3 | **€47,80** |
| 3'lü fular bundle | €134,90 | €24,00 | €73,67 | %66,1 | **€64,63** |
| **Premium koleksiyon (2 fular + ring + kutu)** | **€139,90** | €18,50 | **€79,97** | **%69,2** | **€70,33** |

**Bu tablo işin kendisi.** Bir müşteriyi tek €59,90 fulardan €89,90 hediye setine taşımak CAC tavanını €27,18'den €42,72'ye çıkarıyor — **kazanılabilir müşteri maliyetinde %57 artış** — ve karşılığında sadece €2,50 COGS, €0,60 ambalaj ve kargo ekliyor. Elindeki en ucuz ROAS iyileştirmesi ve hiç media-buying yeteneği gerektirmiyor.

**Launch şekli için sonuç: tek ürünlü mağaza açma.** Birinci günden 3 kademeli mimariyle (tek / hediye seti / koleksiyon) aç, hediye seti görsel olarak varsayılan seçenek olsun. Tek-SKU launch'ı seni €27,18 CAC tavanında kilitliyor ve muhtemelen sadece bu yüzden testi kaybedersin.

## 7.6 Tekrar satın alma duyarlılığı

| 12 aylık tekrar oranı | Müşteri başına 12 aylık katkı | 1,0x payback'te maks CAC |
|---|---|---|
| %0 | €27,96 | €27,96 |
| %15 | €32,16 | €32,16 |
| %25 | €34,95 | €34,95 |
| %35 | €37,75 | €37,75 |

**Kötü bir CAC'i LTV'nin kurtarmasını planlama.** Güçlü bir %35 tekrar oranı bile tavanını €28'den €38'e çıkarıyor. Şal düşük frekanslı bir kategori — yılda en fazla bir-iki alım, ağırlıklı hediye odaklı. "€55 CAC'i kabul ederiz çünkü LTV" diyen her plan ~1,5 kat yanlış. **Birinci sipariş katkısı pozitif ya da pozitife yakın olmak zorunda.** Bu kategorinin talep ettiği disiplin bu.

---

# 8. META ADS ANALİZİ

## 8.1 Benchmark'lar (2025 yıl sonu / 2026)

| Metrik | Değer | Kaynak / kayıt |
|---|---|---|
| Meta CPM, tüm sektörler | **14,19 $** ≈ €13,05 | 2025 yıl sonu (Triple Whale / agregatörler) |
| Meta CTR, tüm tıklamalar | %2,19 | 2025 yıl sonu. **Bu all-clicks, link CTR değil** — link CTR tipik olarak yarısı kadar |
| Meta dönüşüm oranı | %1,60 | 2025 yıl sonu |
| E-ticarette medyan Meta CVR | %1,57 | 2025 |
| Meta CPA, tüm sektörler | 38,19 $ ≈ €35,13 | 2025 yıl sonu |
| **Meta CPA, hazır giyim** | **36,76 $ ≈ €33,82** | 2025 — platform medyanından hafif iyi |
| Sağlıklı 2026 e-tic. hesabı | **link CTR %1,2–2,5, soğuk CPM €8–18, CPC €0,50–1,80, blended ROAS 2,0–3,5x** | 2026 benchmark derlemeleri |
| **İspanya ortalama CPM** | **~€6** | Tüm sektör, tüm hedef olarak bildirilmiş. **Buna göre plan yapma.** Premium moda açık artırmasında soğuk dönüşüm kampanyaları €10–18 çalışıyor. €6'yı "İspanya Fransa'dan ucuz açık artırma" kanıtı olarak kullan, media planı olarak değil |
| Meta CPM YoY enflasyonu | **+%20,03** (2025) | Triple Whale, Nis 2026 |
| Site CVR, moda | %2,5–3,1 | Sektör benchmark'ı |
| Site CVR, Shopify ortalaması | %1,40 | Sektör benchmark'ı |
| Site CVR, lüks/mücevher | %0,8–1,2 | Sektör benchmark'ı — uyarı: çok yukarı konumlanırsan CVR çöküyor |
| **Q4 CPM enflasyonu** | Q4 **Q1'e göre +%26**; **Kasım yıllık ortalamanın +%41 üstü**; Q4 genel olarak **ortalamanın %35–45 üstü**; **BFCM zirve günleri baz seviyenin 2–3 katı** | Birden çok 2025/2026 benchmark kaynağı |

## 8.2 €5.000 harcamada üç senaryo (Q4 dışı CPM)

Funnel: gösterim → link tıklaması → landing-page oturumu (tıklamaların %88'i) → sipariş. Katkı net gelirin %65,5'i (tek/bundle harmanı), %10 iade uygulanmış.

| Senaryo | CPM | Link CTR | CVR | Gösterim | Tıklama | Oturum | Sipariş | CPC | **CAC** | AOV | Ciro | **ROAS** | Katkı | **Reklam sonrası net** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Muhafazakâr** | €16 | %1,00 | %1,0 | 312.500 | 3.125 | 2.656 | 27 | €1,60 | **€188,24** | €49,90 | €1.325 | **0,27** | €613 | **−€4.387** |
| **Baz** | €13 | %1,50 | %1,8 | 384.615 | 5.769 | 5.077 | 91 | €0,87 | **€54,71** | €59,90 | €5.474 | **1,09** | €2.555 | **−€2.445** |
| **Agresif** | €12 | %2,50 | %2,6 | 416.667 | 10.417 | 9.375 | 244 | €0,48 | **€20,51** | €72,00 | €17.550 | **3,51** | €8.253 | **+€3.253** |

**Aynı senaryolar Kasım CPM'leriyle (+%40):**

| Senaryo | Q4 CPM | CAC | ROAS | Reklam sonrası net |
|---|---|---|---|---|
| Muhafazakâr | €22,40 | €263,53 | 0,19 | −€4.562 |
| Baz | €18,20 | €76,60 | 0,78 | −€3.175 |
| Agresif | €16,80 | **€28,72** | **2,51** | **+€895** |

## 8.3 Üzerinde oturman gereken bulgu

**Pazar ortalaması Meta performansında bu iş para kaybediyor — ve marjinal olarak değil.** Baz senaryo savunulabilir, benchmark-tutarlı girdiler kullanıyor (€13 CPM, %1,5 link CTR, %1,8 site CVR) ve **€27,96 tavana karşı €54,71 CAC** üretiyor. Bu 2 kat aşım ve €5.000'lik testte €2.445 zarar.

**Burada çalışan bir "ortalama" versiyonu yok.** Tek ürün €59,90'ın pazar ortalaması Meta'da başa baş gelmesi için **€114,81 AOV** gerekiyordu. %2,5 CVR'de bile **€83,36** gerekiyor.

| CPM | Link CTR | CVR | → CAC | Başa baş için gereken AOV |
|---|---|---|---|---|
| €13 | %1,5 | %1,8 | €54,71 | **€114,81** |
| €13 | %1,5 | %2,5 | €39,39 | €83,36 |
| **€13** | **%2,0** | **%2,5** | **€29,55** | **€63,15** |
| €16 | %1,5 | %1,8 | €67,34 | €140,73 |

**Üçüncü satıra dikkat et.** Link CTR'yi %2,0'a ve CVR'yi %2,5'e çıkarmak gereken AOV'yi €63,15'e indiriyor — hediye-seti öncelikli offer mimarisiyle ulaşılabilir. **Tüm plan tek satırda bu: %2 CTR × %2,5 CVR × €65 AOV.**

## 8.4 Tek baraj: gereken (link CTR × session CVR)

Başa baş, 1.000 gösterim başına siparişin ≥ CPM ÷ maks CAC olmasını gerektiriyor. Bölüştürünce, gereken **link CTR ile session CVR çarpımı**:

| AOV | Maks CAC | CPM €10 | CPM €13 | CPM €16 | CPM €20 |
|---|---|---|---|---|---|
| €39,90 | €18,22 | %0,062 | %0,081 | %0,100 | %0,125 |
| €49,90 | €23,09 | %0,049 | %0,064 | %0,079 | %0,098 |
| **€59,90** | **€27,96** | **%0,041** | **%0,053** | **%0,065** | %0,081 |
| €69,90 | €32,83 | %0,035 | %0,045 | %0,055 | %0,069 |
| €79,90 | €37,71 | %0,030 | %0,039 | %0,048 | %0,060 |
| €99,90 | €47,45 | %0,024 | %0,031 | %0,038 | %0,048 |

**Referans noktaları:** %1,5 × %2,0 funnel = %0,030. %2,0 × %3,0 funnel = %0,060.

**Bu tek sayı senin tüm KPI dashboard'un.** €59,90 AOV ve €13 CPM'de **%0,053** gerekiyor. Kasım CPM'leriyle (~€18) €65 AOV'de yaklaşık **%0,065**. `link CTR × CVR`'yi günlük olarak tek bir rakam olarak takip et. Creative kalitesini, offer kalitesini ve landing-page kalitesini, bir işin olup olmadığına karar veren tek metriğe indiriyor. Geri kalan her şey — CPM, CPC, ATC oranı, ROAS — o sayının *neden* orada olduğunun teşhis detayı.

## 8.5 Test için pratik Meta yapısı

| Unsur | Öneri | Neden |
|---|---|---|
| Kampanya hedefi | Birinci günden Sales / purchase conversion | Ekonomi test ediyorsun, kitle öğrenmiyorsun |
| Yapı | **1 kampanya, 2–3 ad set, ad set başına 8–15 çeşitli creative** | Meta'nın kendi rehberliği ad set başına 8–15 reklam. **25 çeşitli creative'li tek ad set, beşer creative'li beş ad set'e göre %17 daha fazla dönüşüm ve %16 daha düşük maliyet** üretti |
| Hedefleme | **Broad + Advantage+ audience**, İspanya (Canarias/Ceuta/Melilla hariç), kadın 25–60. Kontrol olarak bir interest-stack ad set | Andromeda sonrası Meta alıcıyı creative sinyalinden buluyor; manuel interest yığınlama çoğunlukla dağılımı kısıtlıyor |
| Creative çeşitliliği | **Gerçekten farklı açılar, varyasyon değil.** Benzer reklamlar (>%60 benzerlik) tek bir Entity ID'ye birleştirilip tek slot için birbiriyle yarıştırılıyor | §13'teki 32 açı kütüphanesinin, tek bir açının 30 hook varyantından neden daha değerli olduğunun teknik nedeni bu |
| Hacim kadansı | **Ayda minimum 15–20 yeni *konsept*** | Ayda 15+ konsept test eden markalar aynı harcamada **1,8 kat yüksek medyan ROAS**; ayda 20+ yeni reklam → <10'a göre %65 yüksek ROAS |
| Bütçe akışı | İlk 14 gün €80–120/gün; CTR×CVR barajı geçmeden ölçekleme | €100/gün'de €13 CPM'de günde ~7.700 gösterim — CTR okuması için 3–4 gün yeter ama CVR okuması için ~2 hafta gerekiyor |
| Q4 zamanlaması | **Ekim'i öne yükle.** Kasım CPM'leri yıllık ortalamanın +%41 üstünde, BFCM zirve günleri 2–3 kat | Ekim'de ucuza müşteri al, Kas–Ara'da retargeting ve e-postayla hasat et, sonra CPM'ler çökerken Reyes penceresini çalış |

---

# 9. CREATIVE AVANTAJIN — SAYISALLAŞTIRILMIŞ

## 9.1 Avantajın nakit değeri

| Model | Asset başına maliyet | 20 asset/ay | Yıllık |
|---|---|---|---|
| Ajans / UGC creator pazar oranı | €150–450 (orta kademe €150–500; kullanım hakları +%30–50; whitelisting +%30/ay; hook varyantı ~€46) | **€3.000–9.000/ay** (€300 ort.: €6.000) | **€36.000–108.000** |
| Freelance editör + ücretli creator | ~€150 | €3.000/ay | €36.000 |
| **Sen + AI stack** | **~€12** (araç ~€240/ay ÷ 20 asset) | **€240/ay** | **€2.880** |

**Doğrudan nakit avantajı: yılda kabaca €33.000–70.000 satın almak zorunda olmadığın creative üretimi.** €5.000'lik test ölçeğinde bu, reklama €3.000 + creative'e €2.000 harcamakla **reklama €4.400 + araca €600** harcamak arasındaki fark — aynı sermayeden %47 daha büyük medya bütçesi.

## 9.2 Avantajın performans değeri (daha büyük rakam)

| Kanıt | Rakam | Kaynak |
|---|---|---|
| **Ayda 15+ yeni konsept** test edenler vs <5, eşit harcamada | **1,8 kat yüksek medyan ROAS** | MHI analizi, 80 DTC hesabı, 2025 |
| **Ayda 20+ yeni reklam** test edenler vs <10 | **%65 yüksek ROAS** | 2025 benchmark analizi |
| 25 çeşitli creative'li tek ad set vs beşer creative'li beş ad set | **+%17 dönüşüm, −%16 maliyet** | Meta rehberliği / uygulayıcı verisi |
| Andromeda (2025 ortası) Meta'nın işlediği reklam hacmini **10.000 kat** artırdı; creative sinyali artık reklamını kimin göreceğinin birincil girdisi; >%60 benzer reklamlar tek Entity ID'ye birleşiyor | Yapısal | Meta / Andromeda uygulayıcı rehberleri |

**Bunu kendi modelime uygula.** Baz senaryo CAC'i €54,71'di — zarar. ROAS'ı 1,8 ile çarp (ölçülmüş creative-velocity etkisi) ve Baz ROAS **1,09x → 1,96x** oluyor. Başa baş 2,14x. **Yani creative avantajın tek başına seni "paranın yarısını kaybetmekten" "neredeyse başa başa" taşıyor — çizginin ötesine değil.**

Dürüst aritmetik bu ve bu raporun en önemli şeyi. Avantajın büyük, gerçek ve ölçülmüş — *ve tek başına yeterli değil.* Creative avantajına **artı** €65+ AOV'ye **artı** %2,5+ CVR'ye ihtiyacın var. Üçünden herhangi ikisi para kaybediyor.

## 9.3 Normal founder vs senin modelin

| Maliyet / yetenek | Tipik yeni DTC founder | Sen | Fark |
|---|---|---|---|
| Creative üretimi, 20 asset/ay | €3.000–6.000 | €240 | **−€3.000 ile −€5.800/ay** |
| Creative iterasyon gecikmesi | 7–21 gün (brief → çekim → kurgu → revizyon) | **Saatler** | Bileşik: çeyrek başına ~10–20 kat daha fazla öğrenme döngüsü |
| Media buying | €1.500–3.000/ay ajans veya harcamanın %10–15'i | €0 | −€1.500 ile −€3.000/ay |
| Hook/açı kütüphanesi derinliği | 3–8 açı, geri dönüşümlü | **32+ farklı açı, genişletilebilir** | Andromeda'nın semantik çeşitlilik talebini doğrudan besliyor |
| Ürün fotoğrafı | Çekim başına €800–2.500 | AI + bir gerçek numune çekimi | −€800 ile −€2.000 |
| Video/VSL yeteneği | Dışarıdan veya hiç yok | **9 yıl, VSL dahil** | Farklılaştırıcı varlık — §9.4 |
| **Aylık kaçınılan toplam gider** | — | — | **~€5.000–9.000/ay** |
| **Hâlâ satın alman veya öğrenmen gerekenler** | — | CRO/landing-page dönüşümü, offer tasarımı, İspanyolca/Fransızca copy nüansı, 3PL ops, AB uyumu, e-posta/retention, İspanyolca müşteri hizmeti | **Gerçek açık burada. Buna bütçe ayır** |

## 9.4 Geçmişinin en çok işe yarayan kısmı — ve o UGC değil

DTC'deki herkes UGC satın alabilir. €59'luk aksesuar satan neredeyse kimsenin yapamadığı şey **yapılandırılmış uzun-form ikna varlığı** kurmak. Malaberg'de VSL kurguladığın dört yıl burada gerçekten kıt olan yetenek ve bu işe spesifik bir şekilde oturuyor:

- **Şalın fiyat itirazı değil, yetkinlik itirazı var.** İspanyol bir kadının €59'luk ipek fular almama nedeni *"nasıl takacağımı bilmiyorum ve çekmecede kalacak."* Bu 6 saniyelik bir hook'la çözülmüyor. **Yetkinlik korkusunu çözen 90 saniyelik bir styling gösterimiyle** çözülüyor — yani bir moda ürününe uygulanmış VSL yapısı.
- "60 saniyede 5 farklı şekil" videosu mini-VSL'dir: problem (kombin sıkıcı) → mekanizma (tek aksesuar, beş yerleşim) → kanıt (beş görünüm) → offer → CTA. Bunun 20 varyantını bir haftada üretebilirsin.
- **Bu aynı zamanda sadece CTR'yi değil CVR'yi de yükseltiyor** — ki §6.2'ye göre en önemli kaldıraç o. Styling videosunu ürün sayfasına, fold üstüne göm. Şal markalarının çoğu düz flat-lay fotoğraf gösteriyor ve satışı orada kaybediyor.

**Bu girişimin gerçek tezi, düzgün ifade edilirse şu:** "ucuz Türk şalını premium fiyata satmak" değil, *"moda aksesuarındaki styling-yetkinlik itirazı direct-response video ile çözülebilir, ben bunu sektörün 20 katı hızda ve maliyetinin %4'üne üretebiliyorum, ve aksesuarın bedeni olmadığı için iadeler marjı geri almıyor."*

---

# 10. MARKA KONUMLANDIRMA

## 10.1 Türkiye sorusu, çözülmüş

Üç yapısal seçeneğin var. Sadece biri hem yasal hem düşük riskli.

| Seçenek | Kurgu | Avantaj | Dezavantaj | Karar |
|---|---|---|---|---|
| **A. Sessiz menşe** | Avrupalı marka, Avrupalı şirket, yasal olarak zorunlu kompozisyon/menşe etiketi dışında hiçbir yerde Türkiye geçmiyor | Sıfır güven cezası; maksimum konumlandırma özgürlüğü | Bir müşteri ya da rakip bunu "yakalama" olarak ortaya çıkarırsa kaçamak görünürsün. Reddit/forum riski. Ve AB tekstil mevzuatı zaten doğru bir kompozisyon etiketi istiyor | **Yasal olarak sorunsuz, stratejik olarak kırılgan.** Sakladığın bir gerçek üzerine inşa etme |
| **B. "Designed in Europe, crafted in Türkiye"** | Avrupalı marka/şirket/fulfilment, Türk zanaatı açıkça ve spesifik olarak adlandırılmış (tesis, doku, elle kıvrılmış kenar) | Dürüst, savunulabilir ve **tam bu kategoride kanıtlanmış** — Le Châle Bleu "Fransa'da elle çizildi, İtalya'da üretildi"yi €39–169'a satıyor. Aksesuarda *pozitif* bir varlık olan zanaat hikâyesi veriyor | Türkiye, AB alışverişçilerinin güvendiğini söylediği ülkeler listesinde yok (DHL). Zanaat mirası olarak, asla fiyat sinyali olarak işlenmemeli | **★ Önerilen** |
| **C. Türk mirası markası** | Anadolu/Osmanlı tekstil mirasını marka kimliğinin çekirdeği yap | Gerçekten farklılaşmış; Avrupa premium aksesuarında kimse burayı tutmuyor; güçlü baskı/hikâye potansiyeli | İspanya ve özellikle Fransa'da en yüksek güven maliyeti; "hediyelik eşya" veya etnik-zanaat olarak okunma riski, premium gardırop olarak değil | **İspanya/Fransa birinci yıl için hayır.** Almanya/Hollanda/ABD için sonra tekrar değerlendir — orada Türk diasporası ve zanaat-pazarı alıcılığı farklı |

**B seçeneğini şöyle uygula:**

- **Şirket ve marka Avrupalı.** İspanyol SL (ya da mevcut yapın), İspanyol/Avrupalı tınlayan marka adı, İspanyol adres, İspanyol iade adresi, İspanyol telefon/WhatsApp, `.es` veya `.com` alan adı.
- **Türkiye zanaat olarak ve spesifik biçimde görünür.** "Türkiye'de üretildi" değil. Yerine: *"İpek şehri Bursa'da, dört nesildir çalışan tezgâhlarda dokundu. Kenarlar elle kıvrılıp dikildi — fular başına sekiz dakika."* Spesifiklik, menşei yükümlülükten kanıt noktasına çeviren şey. Bursa'nın ipek tarihi gerçek ve doğrulanabilir — tam bu yüzden işe yarıyor.
- **Türkiye'yi asla fiyatı açıklamak için kullanma.** "Doğrudan Türkiye'den tedarik ettiğimiz için harika kaliteyi adil fiyata veriyoruz" okuyucuyu Temu'ya çapa atmaya davet ediyor. Fiyat tasarım, el işçiliği ve sunumla haklılaştırılır — asla ucuz işçilikle.
- **Nerede görünür:** Hakkımızda sayfası, ürün sayfasındaki "Zanaat" akordeonu, bir hangtag, bir-iki founder-story creative'i. **Reklam hook'unda, marka adında, sloganda ve ana sayfa hero'sunda DEĞİL.**
- **Uyumu düzgün yap.** Yönerge (AB) 1007/2011 uyarınca İspanyolca lif kompozisyonu etiketi (Fransa'ya girdiğinde Fransızca) ve AB adresli bir GPSR Sorumlu Kişi'si; ürün, ambalaj veya beraberindeki dokümanda. Bunu doğru yapmak hikâyeyi anlatmayı güvenli kılan şey.

## 10.2 Beş konumlandırma yönü

| # | Yön | Hedef müşteri | Fiyat konumu | Creative yönü | Marka hikâyesi | Benim okumam |
|---|---|---|---|---|---|---|
| **1** | **Parisian luxury** | 35–55, özlem duyan, marka-okuryazar, Madrid/Barcelona | €69–99 | Siyah-beyaz film grain, Rive Gauche daireleri, trençkot, sigara-espresso, Jane Birkin referansları | "Bir Parisli kadının on beş yıldır sahip olduğu fular" | **En yüksek CVR potansiyeli, en kötü savunulabilirlik.** Gerçek Fransız provenance'ı olan gerçek Fransız markalarının kendi sahasında yarışıyorsun. İspanya için güçlü, Fransa için ölümcül |
| **2** | **★ Mediterranean elegance** | 30–55, İspanyol ve Güney Avrupalı, sıcak iklim, "effortless" öz-imaj | **€49–79** | Altın ışık, badanalı duvarlar, zeytin ve terracotta paleti, keten, Sevilla/Cádiz/Mallorca kıyıları, deniz rüzgârı | "Güneyin ışığı için yapıldı. Havanın hareket ettiği gibi hareket eden ipek." Sevilla'da tasarlandı, Bursa'da dokundu — **iki Akdeniz kültürü, tek aksesuar** | **★ Önerilen.** Coğrafi olarak doğru (Sevilla'dasın), Türkiye'yi garip olmaktan çıkarıp *tutarlı* kılıyor (ikisi de Akdeniz tekstil kültürü), kalabalık değil ve hafif ürün İspanya'nın gerçek iklimine uyuyor. **Ayrıca seni bir Fransız markasının kopyalayamayacağı şekilde yerelleştiriyor** |
| **3** | **Modern minimalist** | 28–42, kentli profesyonel, Madrid/Barcelona/Paris | €49–69 | Editöryel beyaz alan, tek model, soluk palet, Helvetica-komşusu tipografi, COS/ARKET görsel grameri | "Tek fular. Beş şekil. Gürültü yok." | Güvenli, ölçeklenebilir, üretimi ucuz, Meta'da iyi dönüşüyor — ve **tamamen savunulamaz.** ARKET bunu gerçek güvenle yapıyor. **Markanın kendisi değil, 2. yön içinde bir creative stili** olarak kullan |
| **4** | **Old-money feminine / quiet luxury** | 40–60, yüksek gelir, País Vasco / Madrid / Marbella | €79–139 | Binicilik motifleri, monogramlar, ahırlar, kütüphaneler, vintage arabalar, koyu yeşiller ve bordolar, logo yok | "Yetersiz ifade, sahip olmaya değer tek statü" | **En iyi marjlar, en küçük erişilebilir pazar, kurması en yavaş.** "Quiet luxury" estetiği 2023'ten beri yoğun işlendi. €89–139'luk bir Q4 hediye seti SKU'su için iyi; markanın tamamı olarak çok dar |
| **5** | **Artisan European** | 35–60, değer odaklı, hızlı-moda karşıtı | €59–99 | Eller, tezgâhlar, boya kazanları, kanıt olarak kusur, uzun-form video, adlı ustalar | "Kenar başına sekiz dakika el dikişi. Göstereceğiz." | **En güçlü güven inşası ve VSL yeteneğine en iyi uyum.** Scroll durdurma gücünde zayıf. **2. yönün altındaki kanıt katmanı olarak kullan** |

**Önerilen yığın: Mediterranean elegance (2) marka kimliği + Artisan European (5) kanıt katmanı + Modern minimalist (3) ürün sayfası görsel grameri.** Bu kombinasyon doğru, kalabalık değil, Fransız rakiplere karşı savunulabilir ve Türk tedariki itiraf yerine varlık haline getiriyor.

## 10.3 Kullanılacak ve kaçınılacak konumlandırma dili

| Kullan | Kaçın | Neden |
|---|---|---|
| "Bursa'da dokundu" | "Türkiye'de üretildi" | Spesifik > jenerik; şehir adı zanaat okunuyor, ülke adı imalat okunuyor |
| "Elle kıvrılmış kenar" | "Yüksek kalite" | Doğrulanabilir bir detay, doğrulanamayan bir sıfattan iyi |
| "Sevilla'da tasarlandı" | "Avrupa tasarımı" | Somut bir yer, ve doğru |
| "Silk-touch modal" veya gerçek lif adı | "İpek gibi", "saten dokulu" | AB mevzuatı doğru lif adı istiyor; "ipek gibi" ayrıca taklit sinyali veriyor |
| "Baskı başına 200 adet" | "Limited edition" | Numaralı kıtlık inandırıcı; belirsiz kıtlık değil |
| "Güneyin ışığı için" | "Daha azına lüks" | Lüksten ucuz olmak üzerinden asla yarışma |
| "€59,90" | "€120 idi, şimdi €59,90" | Omnibus Direktifi'nin önceki-fiyat kuralları İspanya'da uygulanıyor |

---

# 11. RAKİP ANALİZİ — FİYATLAR VE DOĞRULAMA DURUMU

**Doğrulama notu.** Bu ortamdan tek bir rakip sitesini bile açamadım (egress allowlist'te sadece GitHub var; WebFetch ve curl ikisi de test edildi ve bloklandı). Bu turda yaptığım: her marka ve ürün için **hedefli arama turları** çalıştırıp arama motorunun döndürdüğü gerçek fiyatları çıkardım. İlk rapordan belirgin şekilde iyi — ama **"canlı doğrulanmış" değil.**

**Doğrulama durumu kolonu:**
- `ÜRÜN SAYFASI` = arama sonucu doğrudan o markanın ürün sayfasından fiyat döndürdü → **yüksek güven**
- `AGREGATÖR` = Lyst / Fashiola / basın / karşılaştırma sitesi → **orta güven**
- `DOĞRULANMADI` = fiyat alınamadı → **tahmin yazmadım**

§26'nın sonunda 15 dakikada kendin bitirebileceğin doğrulama listesi var.

## Kademe 1 — Lüks referans noktaları (tavanı belirler; buraya asla girmezsin)

| # | Marka | Ülke | Ürün | Malzeme | Fiyat | Doğrulama | Konumlandırma / USP |
|---|---|---|---|---|---|---|---|
| 1 | **Hermès** | FR | Carré 90 | İpek twill | **€580** (üç yıl önce ~€460; %7–10 artışlar, Şub 2025 zammı) | AGREGATÖR | Kategorinin kültürel tanımı; müzayede evi değerlemeli işleyen ikincil pazar |
| 2 | Ferragamo | IT | İpek fularlar | İpek | €100–300 (giriş-lüks bandı) | AGREGATÖR | İtalyan miras lüksü; baskı arşivi |
| 3 | Burberry | UK | Fularlar | Kaşmir/ipek | €100–300+ | AGREGATÖR | Heritage check deseni |
| 4 | Dior | FR | Fularlar | İpek | €100–300+ | AGREGATÖR | Couture, monogram |
| 5 | Chanel / Louis Vuitton | FR | Fularlar | İpek | €300+ | AGREGATÖR | Yatırım kademesi |

## Kademe 2 — Premium bağımsızlar (gerçek özlemin; en çok bunları incele)

| # | Marka | Ülke | Fiyat | Doğrulama | Notlar |
|---|---|---|---|---|---|
| 6 | **Petrusse** (Made in France) | FR | **$395** (105 cm ipek karé) / **$215** (65 cm) ≈ €364 / €198. **Eurozone'da €190 üzeri ücretsiz kargo** | ÜRÜN SAYFASI (USD store) + ÜRÜN SAYFASI (kargo eşiği) | 1996 kuruluş; Fransız imalat. Printemps, BeFrenched, BeyondStyle üzerinden de satıyor — saf DTC değil, çok kanallı. **EUR fiyat listesi doğrulanmadı** |
| 7 | **Philéone** (Made in France) | FR | Fularlar **€42–95**; **Emmanuelle €68**, **Sylvia €68**; elle boyanmış Alma şal **€98**; tüm aralık €35–190 | **ÜRÜN SAYFASI** | **En önemli tek rakibin.** Gerçek Fransız imalatıyla €68, sunumla — fiyatla değil — yenmen gereken sayı |
| 8 | **Le Châle Bleu** (FR tasarım, IT/Como üretim) | FR | **€39–169**; Fransa içi gavroche kargosu €7,10 | AGREGATÖR (fiyat) + ÜRÜN SAYFASI (kargo) | **"Fransa'da elle çizildi, İtalya'da üretildi"** — kopyalaman gereken bölünmüş-menşe yapısının ta kendisi. Şeffaf bölünmüş menşenin premium fiyatı desteklediğinin kanıtı |
| 9 | monfoulardensoie.fr | FR | **€70,90–75,90** | AGREGATÖR | Fransız ipek fular perakendecisi; Fransız orta-premium bandını çapalıyor |
| 10 | Fransız pazar referansı | FR | 50×50 cm kaliteli saf ipek gavroche: **~€40 beklenen** | SEKTÖR YORUMU | Küçük format için Fransız fiyat beklentisi. Fransa'ya girerken hero SKU fiyatını bu belirliyor |
| 11 | Fleuron Paris | FR | **DOĞRULANMADI** | — | Fransa'da tasarım ve üretim; bandana + fular geçişi; ABD storefront'u işletiyor |
| 12 | SOI Paris | FR | **DOĞRULANMADI** | — | Parisli DTC, styling odaklı içerik; Shopify deseni |
| 13 | Soeur | FR | **DOĞRULANMADI** | — | "Noble malzemeler" (ipek, kaşmir, yün); tam gardırop markası, fular aksesuar hattı |
| 14 | Sézane | FR | EUR **DOĞRULANMADI**. Cleopatra ipek fular 52×52 cm. İkinci el: RealReal $85–155; Mercari $38–45 | ÜRÜN SAYFASI (ürün) / AGREGATÖR (resale) | Fransız DTC benchmark'ı. **Fiyatlamasını değil, e-posta/drop mekaniğini incele** |
| 15 | Foularchic | FR | **DOĞRULANMADI**; ürünler 70×70 cm | ÜRÜN SAYFASI (ölçü) | **Kendini "fular uzmanı" olarak konumlandıran kategori-uzmanı DTC** — senin kuracağın şeyin Fransızca'da hâlihazırda kurulmuş hali |
| 16 | Lollipops / Balaboosté / Duger / Carnaby | FR | **DOĞRULANMADI** | — | Fransız erişilebilir-premium ve Instagram-doğumlu fular markaları. Fransa'nın DTC yoğunluk problemi tek satırda |
| 17 | **Fio de Martié** | **ES** | **33×33 cm €16,90**; bandana **€48,90'dan**; **70×70 cm "Jardín rojo" €94,90**; **90×90 cm "Dibujo floral" €94,90**; indirimliler €89,90 → €29,90 ve €89,90 → €74,90; El Corte Inglés'te €64,90 → €34,90 | **ÜRÜN SAYFASI** | **İspanya'daki en önemli rakibin ve premium tavan kanıtın.** İtalya'dan ithal baskılı doğal ipek, **İspanya'da el yapımı**, kumaş/nakış/etiket kişiselleştirme, El Corte Inglés'te satışta. **Bir İspanyol markası 90×90'ı €94,90'a satıyor — senin €59,90'ın çok altında kalıyor** |
| 18 | **Hamzah** | **ES** | **İpek fular €35–49**, bazıları €39'a indirimli, **büyük boy €47**, **"Noisette" €69**. €50 üzeri ücretsiz kargo | **ÜRÜN SAYFASI** | İspanyol zanaatkâr, %100 doğal ipek, sanatçı/zanaatkâr aile hikâyesi, özel desenler. Toptan da yapıyor. **İspanyol bağımsız-premium bandının alt ucunu tanımlıyor** |
| 19 | **Julunggul** | **ES** | **DOĞRULANMADI**. €50 üzeri ücretsiz kargo | ÜRÜN SAYFASI (kargo) | Zaragoza merkezli; ipek fular, şal ve ısmarlama kimono; **tamamı İspanya'da el yapımı**, kişiselleştirilebilir; WhatsApp üzerinden satış |
| 20 | Munira | ES | **DOĞRULANMADI** | — | İpek fular ve şallar, tasarım odaklı; çok sayfalı katalog = gerçek çeşit derinliği |
| 21 | Elizabetta | IT/US | **$120–250** ≈ €110–230 | AGREGATÖR | "Fransız fular alternatifi" olarak konumlanıyor. **Konumlandırma playbook'u okunmaya değer — Fransız markalarının açıkça *karşısında* pazarlama yapıyorlar** |
| 22 | Atelier Hoi An | VN/EU | **€100 altı** kademesi | AGREGATÖR | Zanaatkâr otantiklik; €100-altı zanaatkâr kademesinin tanınmış bir segment olduğunun kanıtı |
| 23 | Soieries du Mékong | FR/KH | €100 altı kademesi | AGREGATÖR | Sosyal girişim zanaatkâr; Kamboçya dokuma kooperatifi — etik-zanaatkâr playbook'unun iyi yapılmış hali |
| 24 | Como Milano | IT | **DOĞRULANMADI** | — | Como ipek bölgesi provenance'ı |
| 25 | MaraSilk / La Caressette | EU | **DOĞRULANMADI** | — | İçerik odaklı DTC; **"silk scarf trends" üzerine ağır SEO.** §18'deki kümelerin tam üzerinde sıralanıyorlar — SEO'larını incele |

## Kademe 3 — Erişilebilir premium ve high-street (satışı gerçekte burada kazanıyor veya kaybediyorsun)

| # | Marka | Ülke | Fiyat | Doğrulama | Sana neden önemli |
|---|---|---|---|---|---|
| 26 | **Massimo Dutti** | ES (Inditex) | **%100 ipek baskılı (paisley) fular €29,95**; keten fular €39,95; fularlar genel olarak €30'dan; %100 kaşmir fular mevcut | **ÜRÜN SAYFASI** (€29,95 ipek) + AGREGATÖR ("€30'dan") | **İspanya'daki en tehlikeli rakip ve bu turun en kritik bulgusu.** İspanyol, güvenilen, premium algılanan, fiziksel olarak mevcut ve **%100 ipeği hero fiyatının yarısına satıyor.** Onu fiyatla ya da güvenle değil; sadece baskı özgünlüğü, hediye sunumu ve styling içeriğiyle yenersin. **Bu fiyatı canlı doğrulaman gereken 1 numaralı kalem — boyut ve indirim durumu belirsiz** |
| 27 | **ARKET** | SE (H&M) | **Kaşmir ~£85 (≈€98)**; **baskılı ipek ~£45 (≈€52)** | AGREGATÖR (GBP) | **İlk raporda "€39 kaşmir" yazmıştım — bu tur çelişti.** £85 ≈ €98 kaşmir çok daha yumuşak bir tehdit. "Plain kaşmirle yarışamazsın" argümanı geçerli ama sandığımdan zayıf. **EUR fiyatı doğrulanmalı** |
| 28 | & Other Stories | SE (H&M) | Kaşmir örme fular EUR mağazasında listeli; fiyat **DOĞRULANMADI**. Önceki turda İspanyolca kaynakta "kaşmir €49" geçti | AGREGATÖR (çelişkili) | Yorum, ipek ve baskılı fular hattı var. **Doğrulanması gereken 2 numaralı kalem** |
| 29 | H&M | SE | Baskılı **€9,99**, ince örme **€14,99**, püsküllü şifon **€19,99** | AGREGATÖR (ES sitesi) | Tabanı belirliyor. €35 altına fiyatladığın her şey buraya karşılaştırılıyor |
| 30 | Zara / Mango | ES | ~€15–40 | AGREGATÖR | Hacim tabanı; büyük İspanyol marka aşinalığı |
| 31 | Cortefiel | ES | **DOĞRULANMADI** | — | İspanyol orta segment; fular + bandana; yerleşik aksesuar çeşidi |
| 32 | Nice Things Paloma S. | ES | **DOĞRULANMADI** | — | İspanyol baskı odaklı moda — senin de şeridin; baskılarını incele |
| 33 | Falconeri | IT | **DOĞRULANMADI** | — | Kaşmir/ipek uzmanı; malzeme-uzmanı güvenilirliği |
| 34 | Bijou Brigitte | DE | **DOĞRULANMADI** | — | İspanya'da erişilebilir aksesuar zinciri |
| 35 | La Casa de la Moda | ES | **DOĞRULANMADI** | — | İspanyol online fular perakendecisi; çeşit ve fiyatla yarışıyor |

## Kademe 4 — Pazar yerleri ve kanallar (gerçek rekabet kümesi)

| # | Kanal | Fiyat bandı | Doğrulama | Neden önemli |
|---|---|---|---|---|
| 36 | **El Corte Inglés** | Kendi markasından **Lauren Ralph Lauren, Calvin Klein, Tommy Hilfiger, Bimba y Lola, Jo & Mr. Joe, Adolfo Domínguez, Maje, Claudie Pierlot, Scalpers**'a kadar; Fio de Martié örneği €64,90 → €34,90 | **ÜRÜN SAYFASI** (marka listesi + örnek fiyat) | İspanya'nın fularda mağaza otoritesi. **Aynı zamanda potansiyel bir partner** — Fio de Martié orada satılıyor, bu senin ölçekte şablonun. 48 saatte teslimat |
| 37 | **Amazon.es** | Çoğunlukla €10–50 | AGREGATÖR | İspanyol online alışverişçilerin **%82'si** kullanıyor. Listelesen de listelemesen de burada fiyat-karşılaştırılacaksın |
| 38 | **Etsy** | **Türk ipek fularlar €20–113** | AGREGATÖR | **Senin tedarik arbitrajın, hâlihazırda perakendeye çıkmış.** Biri Avrupa'ya Türk ipek fularını €20–113'e satıyor. Listelerini, yorumlarını ve fotoğraflarını oku — tam senin ürününde bedava pazar araştırması |
| 39 | **Vinted** | Değişken; **Fransız online modanın %21,4'ü** | AGREGATÖR | Fransa'da ikinci el tasarımcı fularlar senin €59'luk yeni fularınla doğrudan yarışıyor |
| 40 | **Shein / Temu** | **€9 ortalama** | FEVAD | Fransız online giyim alımlarının %16'sını aldılar. Çok uzak durman gereken bir taban |
| 41 | **TikTok Shop** | İtalya karşılaştırması: **€20–30 ortalama ürün değeri** | TikTok Newsroom | İspanya'da (Ara 2024) ve Fransa'da (Mar 2025) canlı; 100 bin+ AB satıcısı; **cironun %69,9'u affiliate creator'lardan.** Senin için fırsat ve aynı zamanda rekabet kanalı |
| 42 | Stylight / Fashiola / Lyst / Place des Tendances | Agregatör, −%60'a kadar indirim | AGREGATÖR | Fiyat karşılaştırma yüzeyi; aynı zamanda ucuz trafik kaynağı |

## 11.1 Rakip haritası aslında ne söylüyor

**1. En büyük stratejik tehdidin Massimo Dutti'nin €29,95 %100 ipek fuları — ve bir şal markasından gelmiyor.** Güvenilen, İspanyol, fiziksel olarak iade edilebilir bir premium high-street markası ipeği senin hero fiyatının yarısına satıyor. **Sonuç: markayı malzeme kalitesi iddiası üzerine kurma.** Onu sana özel baskı + sunum + styling rehberliği üzerine kur. Bir baskı fiyat-karşılaştırılamaz; "%100 ipek" karşılaştırılabilir ve kaybedersin.

**2. Ama premium tavan sandığımdan yüksek: Fio de Martié 90×90'ı €94,90'a satıyor.** Ve o da İspanyol, o da İspanya'da el yapımı, o da El Corte Inglés'te. Yani İspanyol tüketici bir bağımsız markanın ipek karesine €94,90 ödüyor. **€59,90 bu iki uç arasında (€29,95 Massimo Dutti — €94,90 Fio de Martié) tam ortada oturuyor ve savunulabilir.** Fiyatı düşürmek çözüm değil (§6.2: €49,90 maks CAC'i €27,18'den €19,99'a düşürüyor). Çözüm farkı tartışmasız kılmak.

**3. İspanya'nın premium-şal DTC alanı ince; Fransa'nın doygun.** İspanya'da üç-dört gerçek zanaatkâr DTC oyuncusu var (Fio de Martié, Hamzah, Julunggul, Munira), çoğu yetersiz pazarlanıyor ve neredeyse kesinlikle sofistike Meta creative çalıştırmıyor. Fransa'da bir düzine var, artı Hermès, artı Vinted, artı kendini "fular uzmanı" ilan etmiş bir DTC markası (Foularchic). **Bu, §4'teki Önce-İspanya kararını medya maliyeti argümanından bağımsız olarak teyit ediyor.**

**4. Doğrulanmış bağımsız-premium bandı: İspanya €35 (Hamzah) – €94,90 (Fio de Martié); Fransa €39 (Le Châle Bleu alt uç) – €98 (Philéone elle boyama).** €59,90 her iki pazarda da bandın içinde. Bu, §6'daki önerinin bağımsız bir teyidi.

**5. Etsy bu hafta sömürmen gereken bedava rekabet istihbaratı.** Türk ipek fularlar orada €20–113'e satılıyor. En çok satan listelerin fotoğraflarını, metnini, yorumlarını ve itirazlarını oku. Hedef müşterin sana sorulmadan neyi önemsediğini söylüyor.

---

# 12. MÜŞTERİ AVATARLARI

## Avatar 1 — "Lucía", kentli profesyonel (28–35)

| Özellik | Detay |
|---|---|
| Yaş / gelir | 30; kişisel €28–40 bin, genelde çift gelirli hane |
| Şehir | Madrid (Chamberí, Malasaña), Barcelona (Eixample, Gràcia) |
| Yaşam tarzı | Ofis veya hibrit; spor salonu; brunch; yılda 2–3 seyahat; yoğun Instagram; 5–10 moda creator takip ediyor |
| Moda tercihleri | Zara/Mango tabanı + 2–3 "daha iyi" parça; Massimo Dutti ve COS'a özeniyor; minimum çabayla toparlanmış görünmek istiyor |
| **İtirazlar** | **"Nasıl takacağımı bilmiyorum ve çekmecede kalacak."** Sonra: "Bu gerçekten ipek mi yoksa hikâyesi olan polyester mi?" |
| Satın alma tetikleyicileri | Güvendiği bir creator'ın styling'i; "60 saniyede beş şekil"; ücretsiz kargo; checkout'ta Bizum; kendi vücut tipine benzer birinde görmek |
| Tercih ettiği fiyat | **€39–59** (€69 üstü güçlü bir gerekçe istiyor) |
| Platformlar | Instagram Reels > TikTok > Pinterest |
| **Muhtemel reklam açısı** | "Tek fular, beş kombin" / kombin-yükseltme dönüşümü |
| **Creative formatı** | 15–25 sn dikey, hızlı styling kesmeleri, trend-komşusu ses, creator-çekimi görünüm |

## Avatar 2 — "Carmen", premium moda alıcısı (35–45)

| Özellik | Detay |
|---|---|
| Yaş / gelir | 40; hane €45–70 bin, profesyonel veya işletme sahibi |
| Şehir | Madrid, Barcelona, Bilbao, Valencia, Sevilla |
| Yaşam tarzı | Yerleşik kariyer, 5–12 yaş çocuklar, zaman-yoksul para-daha-az-yoksul; nicelikten çok nitelik; daha az ama daha iyi alıyor |
| Moda tercihleri | Massimo Dutti, COS, Sandro, Uterqüe-mirası zevk; bir tasarımcı çantası var; kumaş kompozisyonunu önemsiyor ve etiketi okuyor |
| **İtirazlar** | **"Bilinmeyen bir marka için €60 mu?"** "Nerede üretildi?" "Kolayca iade edebilir miyim?" |
| Satın alma tetikleyicileri | Kumaş ve konstrüksiyon detayı (momme gramajı, elle kıvrılmış kenar); founder meşruiyeti; fotoğraflı yorumlar; İspanyol iade adresi; adı olan bir tasarımcı |
| Tercih ettiği fiyat | **€59–89** — hero fiyatın çalışmasının nedeni o |
| Platformlar | Instagram feed + Stories, Facebook, satın almadan önce marka adını Google'da arıyor |
| **Muhtemel reklam açısı** | Malzeme/zanaat kalitesi + "lüks fiyatı olmadan lüks görünüm" + founder hikâyesi |
| **Creative formatı** | 30–60 sn zanaat filmi (tezgâh, eller, kenar), makro kumaş dokusu, sakin tempo, altyazılı voiceover — **senin VSL yeteneğinin küçültülmüş hali** |

## Avatar 3 — "Pilar", şık klasik alıcı (45–60)

| Özellik | Detay |
|---|---|
| Yaş / gelir | 52; hane €50–90 bin, genelde beş avatarın en yüksek harcanabilir geliri |
| Şehir | Madrid (Salamanca), Bilbao, San Sebastián, Sevilla, Marbella, Palma |
| Yaşam tarzı | Çocuklar büyümüş; sosyal takvim (öğle yemekleri, düğünler, tiyatro); seyahat ediyor; bir Hermès karesi olabilir ya da istiyor |
| Moda tercihleri | Klasik, kalite-öncelikli, renk-cesur; El Corte Inglés ve Massimo Dutti varsayılanı; kazanıldığında marka-sadık |
| **İtirazlar** | "Gerçek ipek mi?" "Rengi akar mı?" "Elde ucuz mu görünecek?" Fotoğraf kalitesine karşı şüphesi yüksek |
| Satın alma tetikleyicileri | **Miras kalitesi algısı**; hediye kutusu; telefon veya WhatsApp desteği; net iade politikası; klasik baskılar (binicilik, barok, çiçek); ölçü ipuçları (90 cm) |
| Tercih ettiği fiyat | **€69–139** — hediye setlerini ve şalları o alıyor |
| Platformlar | Facebook > Instagram feed; WhatsApp; **e-posta onda çok etkili** |
| **Muhtemel reklam açısı** | Zamansız zarafet / old-money quiet luxury / "her şeyi yükselten tek aksesuar" |
| **Creative formatı** | Statik editöryel görseller + carousel, daha uzun Facebook videosu, uzun-metin landing page, e-posta |

## Avatar 4 — "Álvaro", hediye alıcısı (30–55, erkek)

| Özellik | Detay |
|---|---|
| Yaş / gelir | 42; partner, anne, kardeş, kayınvalide için alıyor |
| Şehir | Her kentsel yer |
| Yaşam tarzı | Moda alışverişçisi değil. **Yanlış seçmekten ödü kopuyor.** Son tarih baskısı altında 20 dakikalık bir pencerede alıyor |
| Moda tercihleri | Kendine ait hiçbiri. Neyin güvenli ve doğru olduğunun söylenmesi gerekiyor |
| **İtirazlar** | **"Beğenmezse ne olur?"** "Renk yanlış olursa?" "Zamanında gelir mi?" |
| Satın alma tetikleyicileri | **"En çok satan renk"** işaretlemesi; hazır paketlenmiş hediye kutusu; ücretsiz iade/değişim; garantili teslim tarihi; hediye mesaj kartı; "yanlış cevap yok" çerçevesi |
| Tercih ettiği fiyat | **€59–99** — *aynı ürün için kadınlardan daha fazla harcıyor*, çünkü fiyat özen sinyali |
| Platformlar | Instagram, Facebook, **Google arama ("regalo mujer elegante", "regalo para mi madre")** — beşinin en arama-odaklısı |
| **Muhtemel reklam açısı** | "İade etmeyeceği hediye" / tek beden herkese / hazır paketli |
| **Creative formatı** | Hediye kutusu unboxing, ambalaj-öncelikli, sert offer overlay'i, kısa ve düz. **Aynı zamanda en iyi Google Search hedefi** |

## Avatar 5 — "Marta", Noel / Reyes alıcısı (25–60)

| Özellik | Detay |
|---|---|
| Yaş / gelir | Her; yukarıdaki kadınların farklı moddaki hali, artı erkek hediye alıcıları |
| Şehir | Tüm İspanya |
| Yaşam tarzı | Sabit bütçeyle 6 haftalık pencerede 5–9 hediye alıyor (€796 toplamın €370'i hediye) |
| Moda tercihleri | İkincil — önemli olan *alıcının* zevki |
| **İtirazlar** | **"24'ünden / 5'inden önce gelir mi?"** "Paketli mi?" "Ocak'ta değiştirebilirler mi?" |
| Satın alma tetikleyicileri | **Teslim tarihi garantisi**, hediye paketi, uzatılmış Ocak iadesi, çoklu alım ("3 hediye tamam"), fiyat kademesi navigasyonu ("€60 altı hediyeler") |
| Tercih ettiği fiyat | Hediye başına **€39–79**, ama **aynı anda 2–3 alıyor** — en yüksek AOV müşterin o |
| Platformlar | Instagram, Facebook, Google, WhatsApp yönlendirme |
| **Muhtemel reklam açısı** | "Üç hediye, tek sipariş, paketli" / Reyes geri sayımı / uzatılmış iade güvencesi |
| **Creative formatı** | Hediye rehberi carousel, geri sayım aciliyeti, çok ürünlü flat-lay, **hiçbir rakibin çalışmayacağı Reyes-özel creative seti** |

**Bunları nasıl kullanacaksın:** Avatar 2 ve 3 (Carmen, Pilar) €59–89 fiyatını haklılaştırıyor ve para orada. Avatar 1 (Lucía) ucuz erişim ve styling içerik motorunu veriyor. Avatar 4 ve 5 (Álvaro, Marta) **Q4 işinin kendisi** ve tamamen farklı creative gerektiriyor — ambalaj, teslim tarihleri, güvence — ki neredeyse hiçbir rakip bunu üretmeye zahmet etmeyecek.

---

# 13. OTUZ İKİ REKLAM AÇISI

Her açı: **Hook → Visual → Body → CTA.** Türkçe yazıldı; üretim için İspanyolcaya çevir — deyimin önemli olduğu yerlerde İspanyolca hook'u parantezle verdim. Format köşeli parantezde.

## Çok yönlülük kümesi (işin çekirdeği — çekmece itirazını çözer)

**1. Tek fular, beş kombin** *[15–25 sn dikey]*
- **Hook:** "Tek fular. Beş kombin. Altmış saniye." *("Un pañuelo. Cinco looks.")*
- **Visual:** Her 3 sn'de sert kesme: boyun düğümü → saç → çanta sapı → kemer → omza atma. Aynı kadın, aynı kot, beş dönüşüm.
- **Body:** "Kadınların çoğu fular alıp tek şekilde takıyor. Aslında ne için olduğunu göstereyim."
- **CTA:** "Baskıyı keşfet — beş şekil kutuda anlatılıyor."

**2. Kombin fenaydı. Sonra bu.** *[10 sn]*
- **Hook:** "Kombinin sıkıcı değil. Sadece bitmemiş."
- **Visual:** Düz beyaz tişört + kot, statik, yavan. Fular kadraja giriyor. Tamamlanmış görünüme sert kesme.
- **Body:** "Giyinmiş olmakla toparlanmış olmak arasındaki fark tek bir aksesuar."
- **CTA:** "Kombini bitir — €59,90."

**3. Annenin sana öğretmediği üç düğüm** *[30 sn tutorial]*
- **Hook:** "Üç düğüm. İki dakika. İkincisini her gün kullanacaksın."
- **Visual:** Tepeden sadece eller, yavaş, temiz, numaralı altyazı.
- **Body:** "Parisli, Gevşek Atış, Çanta Sarmalı."
- **CTA:** "Baskı + çizimli düğüm kartı, kutunun içinde."

**4. Aynı fular, pazartesiden cumaya** *[20 sn]*
- **Hook:** "Aynı fular. Beş gün. Kimse fark etmedi."
- **Visual:** Gün etiketli beş kombin, resmiyet artıyor.
- **Body:** "Kullanım başına maliyet: birinci haftada €12."
- **CTA:** "Bir tanesiyle başla."

**5. Kullanım başına €12'lik aksesuar** *[15 sn, statik + metin]*
- **Hook:** "€59,90 ÷ 5 kullanım = €12. Ve sen bunu 50 kez takacaksın."
- **Visual:** Tipografik, temiz, tek ürün çekimi.
- **Body:** İki kez giyilen €40'lık bir üste karşı değer matematiği.
- **CTA:** "Hesabı yap. Sonra baskıyı al."

## Dönüşüm kümesi

**6. Öncesi / sonrası, kıyafet değişmedi** *[8 sn]*
- **Hook:** Bölünmüş ekran, 2 saniye boyunca yazı yok.
- **Visual:** Sol: düz. Sağ: aynı kombin + fular.
- **Body:** "Bundan başka hiçbir şey değişmedi."
- **CTA:** "Baskıları gör."

**7. Havalimanı testi** *[20 sn]*
- **Hook:** "Sabah 6 uçağında pahalı görünmenin yolu."
- **Visual:** Kapüşonlu + tayt + fular + güneş gözlüğü. Terminal, valiz, kahve.
- **Body:** "Seyahat kıyafeti artı bir ipek aksesuar, üşengeç değil kasıtlı okunuyor."
- **CTA:** "Seyahate hazır — 70 g, hiçbir yer kaplamıyor."

**8. Okul servisinden akşam yemeğine tek hareketle** *[20 sn]*
- **Hook:** "08:00 okul servisi. 20:00 akşam yemeği. Tek değişiklik."
- **Visual:** Aynı kombin, fular çantadan boyna geçiyor, ışık değişiyor.
- **Body:** Carmen için. Zaman-yoksul, zevk-yoksul değil.
- **CTA:** "Tek aksesuar, iki hayat."

## Lükse komşuluk kümesi

**9. €580'lik fular ve €59'luk fular** *[15 sn]*
- **Hook:** "Bunlardan biri €580."
- **Visual:** Mermer yüzeyde yan yana iki fular, kenarlarda makro.
- **Body:** "İkisi de elle kıvrılmış kenar. İkisi de ipek gramajında drape. Birinde logo var." *(Bunu yayınlamadan önce kendi kenarını ve lifini doğrula — ve Hermès'i asla adıyla anma.)*
- **CTA:** "Kimsenin fiyatını bilemeyeceği olanı seç."

**10. Lüks görünüm, logo yok** *[20 sn]*
- **Hook:** "En pahalı görünen kadınlar en az logo taşıyor."
- **Visual:** Old-money estetiği: ahırlar, kütüphane, camel palto, görünür marka yok.
- **Body:** Quiet-luxury çerçevesi.
- **CTA:** "Yetersiz ifade, €59,90."

**11. Baskının gerçek üretim maliyeti** *[45 sn]*
- **Hook:** "Neden €59'luk ve €500'lük fuların üretim maliyeti aynı."
- **Visual:** Tezgâh, serigrafi, el dikişi, sonra perakende markup diyagramı.
- **Body:** Şeffaflık hamlesi. Perakende ve pazarlama markup'ı hariç maliyet dökümü.
- **CTA:** "Ürünü satın al, markup'ı değil."

## Menşe / zanaat kümesi

**12. Bursa, ipek şehri** *[45–60 sn]*
- **Hook:** "Türkiye'de 600 yıldır ipek dokuyan bir şehir var. Adını hiç duymadın."
- **Visual:** Tezgâhlar, atölye penceresinden sabah ışığı, eller, dut yaprakları.
- **Body:** Bursa'nın İpek Yolu tarihi; aynı tezgâhlarda dört nesil; elle dikilen kenar.
- **CTA:** "Bursa'da dokundu. Sevilla'da tasarlandı."

**13. Kenar başına sekiz dakika** *[30 sn ASMR]*
- **Hook:** "Sekiz dakika el dikişi. Her fular için."
- **Visual:** Aşırı makro, iğne kenarı kıvırıyor, sadece doğal ses.
- **Body:** "Makine dikişi dokuz saniye sürüyor. Farkı boynunda hissediyorsun."
- **CTA:** "Farkı hisset."

**14. Sevilla'da tasarlandı, Bursa'da dokundu** *[20 sn]*
- **Hook:** "İki Akdeniz şehri. Tek fular."
- **Visual:** Bölünmüş: Sevilla ışığı, beyaz duvarlar, portakal ağaçları / Bursa tezgâhları, ipek ipliği.
- **Body:** Bölünmüş-menşe hikâyesi bir varlık olarak anlatılıyor.
- **CTA:** "Koleksiyonla tanış."

**15. Founder hikâyesi: dokuz yıl başkalarının reklamını yaptım** *[60 sn talking head]*
- **Hook:** "Dokuz yıl boyunca başkalarının ürünlerinin reklamını yaptım. Sonra kendimi yaptım."
- **Visual:** Sen, gerçek, cilalanmamış, fular elinde. Sevilla ışığı.
- **Body:** Neden aksesuar, neden Türkiye, neyden ödün vermedin. Fiyatı dürüstçe söylemek.
- **CTA:** "Bu ilk koleksiyon. Baskı başına 200 adet."
- *(Bu muhtemelen ilk üç performansın arasında olacak. Gerçek prodüksiyon yeteneği olan birinden founder-yüzü videosu bu kategoride nadir.)*

## Malzeme / kalite kümesi

**16. Buruşma testi** *[12 sn]*
- **Hook:** "Fuların bunu yapıyorsa €60 değmez."
- **Visual:** Ucuz bir fular sıkılıyor → kırışıklar kalıyor. Senin sıkılıyor → düzgün dökülüyor.
- **Body:** Drape ve geri dönüş, kalite kanıtı olarak.
- **CTA:** "Kendin test et. 30 gün iade."

**17. Su testi** *[12 sn]*
- **Hook:** "Gerçek boya akmaz."
- **Visual:** Baskıya su damlatılıyor; renk duruyor.
- **Body:** Renk haslığı — Pilar'ın gerçek itirazı, görsel olarak cevaplanmış.
- **CTA:** "Güvenle al."

**18. Gram önemli** *[15 sn]*
- **Hook:** "70 gram. Fuların tamamı bu."
- **Visual:** Mutfak terazisinde fular, sonra bir alyansın içinden geçiriliyor.
- **Body:** Ağırlık ve incelik, kalite kanıtı olarak.
- **CTA:** "Telefonundan hafif."

**19. Neden kaşındırmıyor** *[15 sn]*
- **Hook:** "Bir fular kaşındırıyorsa, yanlış fular."
- **Visual:** Boyun yakın planları, cilt teması, konfor.
- **Body:** Lif ve finiş açıklaması.
- **CTA:** "Cildine değdirerek tak."

## Hediye kümesi (Q4 motoru)

**20. İade etmeyeceği hediye** *[20 sn]*
- **Hook:** "Tek beden. Her kadın. İade yok."
- **Visual:** Erkek elleri seçiyor, sonra bir kadın kutuyu açıyor.
- **Body:** "Yanlış gidecek beden yok. Tahmin edilecek stil yok. Paketli geliyor."
- **CTA:** "19 Aralık'a kadar sipariş ver."

**21. Unboxing, anlatım yok** *[20 sn ASMR]*
- **Hook:** Kurdele çekimi, ilk üç saniye, kelime yok.
- **Visual:** Sert kutu → pelür → fular → düğüm kartı. Ses öncelikli.
- **Body:** Sessiz. Sadece metin overlay: "Böyle geliyor."
- **CTA:** "Standart olarak hediye paketli."

**22. Annem için** *[30 sn]*
- **Hook:** "Annemde her şey var. Bunu sakladı."
- **Visual:** Gerçek nesiller arası an, sıcak, kurgusuz.
- **Body:** Duygusal hediyeleşme, ürün özelliği değil.
- **CTA:** "Saklayacağı bir hediye."

**23. Kızım için** *[25 sn]*
- **Hook:** "Ona aldığım ilk düzgün şey."
- **Visual:** Genç kadın alıyor, yaşlı kadın izliyor.
- **Body:** Geçiş ritüeli çerçevesi; miras dili.
- **CTA:** "Koleksiyonu başlat."

**24. Üç hediye, tek sipariş** *[20 sn]*
- **Hook:** "Anne. Kardeş. Kayınvalide. Tek sipariş."
- **Visual:** Üç kutu, üç baskı, tek sepet.
- **Body:** Çoklu hediye verimliliği. **AOV creative'i bu.**
- **CTA:** "Üç hediye, paketli, €149,90."

**25. Reyes geri sayımı** *[15 sn, sadece 2–5 Ocak]*
- **Hook:** "Reyes için hâlâ bir şey yok mu? Pazara kadar vaktin var."
- **Visual:** Takvim, 5 Ocak daire içinde, 24 saat teslimat rozeti.
- **Body:** "İspanya'da stokta. Yarın teslim."
- **CTA:** "4 Ocak 14:00'e kadar sipariş ver."
- *(Neredeyse hiçbir rakip bunu çalışmıyor. CPM'ler 26 Aralık'tan sonra çöküyor.)*

## Estetik / kimlik kümesi

**26. Fransız kızı fuları** *[15 sn]*
- **Hook:** "Fransız kadınlar neden hep bitmiş görünüyor."
- **Visual:** Siyah-beyaz, kafe, trençkot, zahmetsiz düğüm.
- **Body:** Estetik özlem açısı.
- **CTA:** "Tek düğüm. Bütün sır bu."

**27. Akdeniz ışığı** *[20 sn]*
- **Hook:** "İpek bu ışık için yapılmıştı."
- **Visual:** Altın saat, badanalı duvarlar, kumaşı hareket ettiren deniz rüzgârı.
- **Body:** Markanın çekirdek konumlandırması, mood film olarak.
- **CTA:** "Güney için yapıldı."

**28. Kapsül gardırop matematiği** *[25 sn]*
- **Hook:** "Beş kıyafet, üç fular, on beş kombin."
- **Visual:** Kombinasyonların çoğaldığını gösteren grid animasyonu.
- **Body:** Kombinatoryal değer — daha az kıyafet al, aksesuar ekle.
- **CTA:** "Gardırobunu çarp."

**29. Sokak stili, Madrid** *[20 sn]*
- **Hook:** "Salamanca'da beş kadına kendi usulünce bağlamalarını söyledik."
- **Visual:** Gerçek sokak röportajları, beş farklı düğüm.
- **Body:** Sosyal kanıt ve styling eğitimi tek asset'te.
- **CTA:** "Kendi düğümünü bul."

**30. Sezonun rengi** *[15 sn]*
- **Hook:** "Jade. Bordo. Derin mavi. Birini seç."
- **Visual:** Üç baskı dönüyor, renk bloklu kareler.
- **Body:** Belgelenmiş 2026 renk yönüne bağlanıyor (yoğun kırmızı, derin mavi, jade yeşili).
- **CTA:** "Üç renk. Her birinden 200."

## Kıtlık / offer kümesi

**31. Baskı başına 200** *[12 sn]*
- **Hook:** "200 adet bastık. Sonra kalıbı kırdık."
- **Visual:** Numaralı etiket makrosu, sonra kalıbın kırılması.
- **Body:** İnandırıcı, numaralı kıtlık — belirsiz "limited edition" değil.
- **CTA:** "200'ün 47'si hâlâ mevcut."

**32. İkincisi kargonun yarısı** *[10 sn, post-purchase upsell]*
- **Hook:** "İkinci baskıyı €44,90'a ekle."
- **Visual:** İki fular, tek kutu, tek koli.
- **Body:** Bundle mantığı düz anlatılıyor. Tek tık post-purchase offer olarak çalışıyor.
- **CTA:** "Siparişime ekle."

**Üretim planı:** 32 açıda **Andromeda'nın ödüllendirdiği semantik çeşitliliğe** sahip oluyorsun — bunlar farklı konseptler, varyant değil, dolayısıyla tek Entity ID'ye birleşmezler. Launch için 15'ini üret (küme 1 + 2'nin tamamı, artı 12, 15, 20, 21, 24, 31), sonra ayda 8–10 yeni konsept ekle. §9.2'deki 1,8 kat ROAS çarpanını kazandıran kadans bu.

---

# 14. 2026 Q4 STRATEJİSİ

## 14.1 İspanya Q4 takvimi — ve neden herkesinkinden 3 hafta uzun

| Dönem | Hedef | Offer | Ürün odağı | Creative açısı | Bütçe payı | Kitle | Mesaj | Aciliyet | Landing page |
|---|---|---|---|---|---|---|---|---|---|
| **Eylül** (sezon öncesi) | **Ucuza öğren.** CTR×CVR barajını kur, pixel'i besle, e-posta listesini tohumla | İndirim yok. €50 üzeri ücretsiz kargo | Sadece hero tek fular | Çok yönlülük (1–5), zanaat (12–15) | **%20** | Broad soğuk, kadın 25–60, ES (adalar hariç) | "Tek fular, beş kombin" | Yok — bu temiz okuma ayı | Ürün sayfası, fold üstünde styling videosu |
| **Ekim** (inşa) | **Enflasyon öncesi CPM'lerde müşteri al.** Retargeting havuzları ve e-posta listesini 3.000+'a çıkar | €50 üzeri ücretsiz kargo + düğüm kartı. **Erken hediye rehberi launch'ı** | Hero + twilly + ilk hediye seti | Hediye (20–24), estetik (26–30) ekle | **%25** | Soğuk + satın alanların %1 lookalike'ı + e-posta yakalama | "Hediye listesi şimdi başlıyor" | Yumuşak: "Yeni baskı, 200 adet" | Koleksiyon sayfası + "€70 altı hediyeler" |
| **Kasım başı** (1–20) | **Çalışanı ölçekle.** Gerçek kâr penceren bu | **VIP erken erişim**, indirim değil. E-posta/SMS kapılı | Tam merdiven: tek / hediye seti / koleksiyon | En iyi 8 performans + 24, 31 | **%15** | Kazananları ölçekle, lookalike'ları %2–3'e genişlet | "Black Friday'den önce erken erişim" | "VIP penceresi perşembe kapanıyor" | Kapılı VIP sayfası + hediye rehberi |
| **Black Friday haftası** (23–29 Kas) | **Hasat et, satın alma.** CPM'ler bazın 2–3 katı | **Yüzde indirim yok.** §14.2'ye bak | Sadece hediye setleri ve bundle'lar | 20, 21, 24, 31 | **%10** *(bilinçli olarak düşük)* | **Önce retargeting + e-posta + SMS.** Minimum soğuk | "İndirim değil. Bundle." | Sert: "Bundle fiyatı pazartesi bitiyor" | Özel BF bundle sayfası |
| **Cyber Monday** (30 Kas) | Tereddütlüleri dönüştür | Tüm siparişlerde ücretsiz hediye kutusu + ücretsiz kargo | Bundle'lar | 24, 32 | %3 | Retargeting, sepet terk edenler | "Ücretsiz hediye paketi için son gün" | Sert | Aynı BF sayfası, geri sayım |
| **1–18 Aralık** (zirve) | **Maksimum ciro. Teslimat kesinliği mesajın tamamı** | Ücretsiz hediye paketi + garantili teslimat + **iadelerin 15 Ocak'a uzatılması** | Hediye setleri, 3 hediye bundle | 20, 21, 22, 23, 24 | **%20** | Soğuk + retargeting + e-posta. Google Shopping'i ağır ekle | "19'una kadar sipariş ver. Paketli gelir." | **Teslimat son tarih geri sayımı** | Fiyat kademesine ve alıcıya göre hediye rehberi |
| **19–24 Aralık** (son dakika) | Panik alıcıyı yakala | **Dijital hediye kartı** + ekspres teslimat | Hediye kartı + stokta hero | 20, 25 | %3 | Sadece retargeting + arama. **Soğuk Meta'yı kes** | "Kargolamak için çok geç. Vermek için değil." | Aşırı | Hediye kartı sayfası |
| **26–31 Aralık** (boşluk) | **Çökmüş CPM'lerde kendine alım + Reyes ön hazırlığı** | "Kendine hediye" çerçevesi; indirim gereksiz | Hero tek, tam fiyat | 2, 5, 27, 28 | %2 | Soğuk — **çeyreğin en ucuz CPM'leri burada** | "Herkese aldın" | Yok | Ürün sayfası |
| **2–5 Ocak** (**Reyes**) | **Kimsenin çalışmadığı avantaj.** Reyes hediyelerine kişi başı €192, Noel arifesine €178 | 24 saat teslimat garantisi (yurt içi stok) | Hediye setleri | **25** (Reyes geri sayımı) | **%2** | Retargeting + soğuk; neredeyse sıfır rekabet | "İspanya'da stokta. Yarın." | **Aşırı: "4 Ocak 14:00'e kadar"** | Reyes landing page |
| **7–31 Ocak** (tut) | Alıcıyı tek seferlik değil listeye çevir | Mevcut müşterilere yeni baskı drop'u; iadeleri → değişime | Yeni renk | 30, 31 | Artakalan | **Q4 alıcı tabanına e-posta/SMS.** Paid yok | "Zaten sahip olanlara ilk bakış" | Yumuşak kıtlık | Üyeler sayfası |

**Bütçe notu:** Kasıtlı asimetri, **Q4 medyasının %45'ini Eylül–Ekim'de**, Kasım'ın +%41 CPM enflasyonundan önce harcamak ve BFCM penceresine sadece %13 ayırmak. Markaların çoğu tersini yapıyor ve müşterilerini yılın en pahalı anında satın alıyor.

## 14.2 Premium bir marka Black Friday'de indirim vermeli mi?

**Hayır. Ve bunu marka içgüdüsü değil veri destekliyor.**

İndirime karşı argüman:
- **Gücün yok.** €59,90'da maks CAC'in €27,18. %20 indirim katkıyı €31,56'dan **€22,00'a** düşürüyor, CAC tavanını ~€18'e indiriyor — tam CPM'lerin bazın 2–3 katı olduğu anda. Medya en pahalı hâlindeyken acquisition bütçeni yarıya indiriyorsun. Bu, geriye giden bir markanın aritmetiği.
- **Birinci yıl premium markası indirim çapasından geri dönemez.** Fiyatın senin kalite iddian. Mirasın, basının, yorum duvarın yok. Markanın ilk haftasında indirim yaparsan €47,90 sonsuza kadar gerçek fiyat olur.
- **İspanyol alışverişçi sadece indirim odaklı değil.** Ücretsiz kargo mağaza seçiminde **#1 sürücü (~%65)**, hızlı teslimat ikinci (%33). İkisi de bir-iki euroya verebileceğin ve yüzde-indiriminden daha önemli şeyler.

**Yerine ne çalıştırmalı, beklenen katkıya göre sıralı:**

| Alternatif | Mekanik | Katkıya etkisi | Karar |
|---|---|---|---|
| **1. Bundle fiyatlaması** | 2 fular €99,90 (ayrı ayrı €119,80) | Katkı **€54,71**, maks CAC **€47,80** — tek ürün tavanının *neredeyse iki katı* | **★ Birincil BF offer'ı.** İndirim gibi görünüyor, AOV artışı gibi davranıyor, tek ürün fiyatını koruyor |
| **2. Ücretsiz sert kutuyla hediye seti** | Fular + ring + kutu €89,90 | Katkı **€49,00**, maks CAC **€42,72** | **★ İkincil.** €3'lük ambalaj €15,50 CAC payı satın alıyor |
| **3. 2+ üründe ücretsiz hediye** | €90 üzeri ücretsiz twilly (COGS ~€2,50) | €2,50 maliyet, €24,90 algılanan değer | **★ Euro başına en yüksek algılanan değer aracı** |
| **4. Tüm siparişlerde ücretsiz kargo** | BF haftası için €50 eşiğini kaldır | Sipariş başına €4,20; İspanya'daki #1 sürücüyü karşılıyor | **★ Çalıştır.** Ucuz ve doğrudan en büyük beyan edilmiş satın alma sürücüsünün üstünde |
| **5. VIP erken erişim** | BF'den önce 48 saat e-posta/SMS kapılı pencere | Maliyeti yok; hacmi zirve CPM'den daha ucuz günlere kaydırıyor | **★ Çalıştır. Çeyreğin en iyi ROI mekaniği** |
| **6. Limited edition BF baskısı** | 200 adet, numaralı, sadece BF rengi | Tam fiyat, kıtlık odaklı | **★ Çalıştır.** Tam marj artı harekete geçme gerekçesi |
| **7. İadeleri 15 Ocak'a uzatma** | Hediye alıcısına güvence | Marjinal maliyet; Álvaro'nun çekirdek itirazını kaldırıyor | **★ Çalıştır** |
| **8. 2 al, 3.'sü %50** | Kademeli adet kırılımı | ~€134,90'da katkı ~€64; hâlâ tekin üstünde | Kabul edilebilir — hacim kırılımı, marka indirimi değil |
| **9. Site genelinde yüzde indirim** | −%20/30 | Yılın en pahalı medya haftasında CAC tavanını yarıya indiriyor | **Yapma** |

**Bir nüans:** Eylül–Ekim testi tam fiyatta CTR×CVR barajını geçemediğini gösterirse, bu BFCM'e indirimle girme sinyali *değil*. Offer'ın veya ürünün yanlış olduğunun sinyali; BFCM teşhisi gizlerken bütçeyi yakar.

---

# 15. UPSELL / CROSS-SELL ÜRÜN HARİTASI

**Aşağıdaki tedarik maliyetleri tahmindir.** Aksesuar seviyesinde tedarikçi fiyatlaması doğrulanamadı — sadece şal/fular fiyatlaması (Türk fabrika-direkt €1,90/adetten, renk başına 10 MOQ; 1.000 adet MOQ'da ipek €1,50–2). Maliyet kolonunu gerçek tedarikçi tekliflerle değiştirilecek planlama tahmini olarak gör.

| # | Ürün | Tahmini tedarik | Perakende | Tahmini marj % | Kargo ağırlığı | Algılanan değer | Cross-sell uyumu | Bundle potansiyeli |
|---|---|---|---|---|---|---|---|---|
| 1 | **Fular ringi (metal)** | €1,50–3,00 | **€19,90–24,90** | **~%88** | **8–15 g** | Yüksek — gerçek bir styling problemini çözüyor | **Mükemmel** | **★★★ 1 numaralı add-on** |
| 2 | **İpek scrunchie** (uyumlu baskı) | €1,00–2,00 | €14,90–19,90 | ~%90 | **5–10 g** | Yüksek — uyumlu set mantığı | Mükemmel | **★★★ Baskı eşleşmeli set** |
| 3 | **İnce twilly / çanta fuları** | €2,00–3,50 | **€24,90–29,90** | **~%88** | **10–20 g** | Yüksek — lükse komşu format | Mükemmel | **★★★ İkinci hero SKU** |
| 4 | **İpek saç bandı / bandeau** | €1,50–2,50 | €19,90 | ~%88 | 8–15 g | Orta-yüksek | Mükemmel | ★★★ |
| 5 | **Fular klipsi / mıknatıslı toka** | €1,50–3,00 | €19,90 | ~%87 | 10–20 g | Orta — gösterim gerektiriyor | Çok iyi | ★★ |
| 6 | **Küçük ipek kare (45–55 cm)** | €3,00–5,00 | **€34,90–39,90** | ~%87 | 25–40 g | Yüksek | Mükemmel | **★★★ 3'lü küçük kare paketi** |
| 7 | **İpek göz bandı** | €2,50–4,00 | €29,90 | ~%86 | 20–30 g | **Çok yüksek** — hediye favorisi | İyi (hediye mantığı) | **★★★ "İpek hediye seti"** |
| 8 | **İpek yastık kılıfı** | €6,00–10,00 | €49,90–59,90 | ~%80 | **150–250 g** | Çok yüksek | İyi (ipek mantığı, fular mantığı değil) | ★★ Üst kademe hediye seti |
| 9 | **Sert hediye kutusu (markalı)** | €2,00–3,50 | **€6,90** veya €90 üzeri ücretsiz | — | **60–120 g** | **Euro başına çok yüksek** | **Zorunlu, opsiyonel değil** | **★★★ AOV kilidi** |
| 10 | **Premium hediye paketi + kart** | €0,60–1,20 | €4,90 veya ücretsiz | — | 15–30 g | Yüksek | Q4'te zorunlu | ★★★ |
| 11 | **Seyahat / toz kesesi (ipek veya pamuk)** | €1,00–2,00 | €12,90 | ~%88 | 15–25 g | Orta-yüksek | İyi | ★★ Bundle dolgusu |
| 12 | **Makyaj çantası (kapitone, baskı eşleşmeli)** | €3,00–5,50 | €34,90 | ~%85 | 60–110 g | Yüksek | İyi | ★★★ |
| 13 | **Mücevher seyahat kutusu** | €4,00–7,00 | €39,90 | ~%82 | 100–180 g | Yüksek | Orta | ★★ |
| 14 | **Broş / fular iğnesi** | €2,00–4,00 | €24,90 | ~%85 | 10–25 g | Orta-yüksek | Çok iyi | ★★ |
| 15 | **Mine veya altın kaplama küpe** | €2,00–4,50 | €29,90–34,90 | ~%87 | **5–15 g** | Yüksek | Orta — farklı kategori | ★★ Tam görünüm bundle'ı |
| 16 | **İnce zincir kolye** | €2,50–5,00 | €34,90 | ~%86 | 5–15 g | Yüksek | Orta | ★★ |
| 17 | **Deri eldiven (astarsız)** | €8,00–14,00 | €59,90–69,90 | ~%78 | **120–200 g** | **Çok yüksek** | **Mükemmel kış eşleşmesi** | **★★★ Kış hediye seti** |
| 18 | **Yün/kaşmir bere** | €5,00–9,00 | €39,90–49,90 | ~%80 | 80–140 g | Yüksek | Mükemmel kış eşleşmesi | ★★★ |
| 19 | **Örme bileklik/kolluk** | €3,50–6,00 | €29,90 | ~%82 | 50–90 g | Orta | İyi | ★★ |
| 20 | **Oversize şal / stola** | €10,00–16,00 | **€89,90–119,90** | ~%80 | **250–400 g** | **Çok yüksek** — boyut değer okunuyor | Mükemmel | **★★★ Premium kademe hero'su** |
| 21 | **Deri kartlık** | €4,00–8,00 | €39,90 | ~%82 | 30–60 g | Yüksek | Orta | ★★ |
| 22 | **İpek astarlı mücevher rulosu** | €4,50–8,00 | €44,90 | ~%82 | 80–150 g | Yüksek | Orta | ★★ |
| 23 | **Baskı eşleşmeli kumaş kaplı defter** | €2,00–4,00 | €19,90 | ~%84 | 150–250 g | Orta | Zayıf — markayı seyreltiyor | ★ Atla |
| 24 | **Kokulu kese / çekmece kesesi** | €0,80–1,80 | €12,90 veya **ücretsiz hediye** | ~%89 | 15–30 g | Orta-yüksek | **Ücretsiz hediye olarak mükemmel** | ★★★ hediye olarak |

## 15.1 Gerçekten önemli olan üçü

**Marj % × cross-sell uyumu × (1 ÷ kargo ağırlığı) ile filtrelenmiş:**

| Sıra | Ürün | Neden |
|---|---|---|
| **1** | **Fular ringi, €19,90** | ~%88 marj, 8–15 g (sıfır ek kargo) ve **satışı bloke eden itirazın tam kendisini çözüyor** ("nasıl bağlayacağımı bilmiyorum"). Aynı anda hem upsell hem dönüşüm aracı. Her hediye setine koy |
| **2** | **İnce twilly, €24,90–29,90** | ~%88 marj, 10–20 g, lükse komşu format ve **tek başına €24,90 giriş ürünü, tek tık post-purchase upsell ve €90 üzeri ücretsiz hediye** olarak çalışıyor. Üç iş, tek SKU |
| **3** | **Sert hediye kutusu, €6,90 (€90 üzeri ücretsiz)** | Marj ürünü değil — **davranış değiştiren ürün.** €3'lük karton €59,90'lık teki €89,90'lık hediye setine çeviriyor, CAC tavanını €27,18'den €42,72'ye taşıyor. Bu listedeki en yüksek kaldıraçlı kalem |

**Birinci yılda kaçınacakların:** yastık kılıfı ve mücevher kutusu (ağırlık ve kategori kayması), defter (marka seyrelmesi) ve pazarlıklı koli oranları almadan 250 g üstü her şey. İpek göz bandı, ağırlık-toleranslı tek istisna çünkü hediye olarak olağanüstü iyi çalışıyor.

---

# 16. AOV STRATEJİSİ — €40 → €60 → €80

## 16.1 Fiyat mimarisi

| Kademe | Offer | Fiyat | Katkı | Maks CAC | Rolü |
|---|---|---|---|---|---|
| Giriş | Twilly / boyun fuları | €24,90 | ~€5 | ~€3 | **Asla reklam verilmez.** Sadece add-on ve ücretsiz hediye |
| **Çekirdek** | **1 × 90 cm baskılı ipek kare** | **€59,90** | €31,56 | €27,18 | Reklam verilen hero ve fiyat çapası |
| **Adım 1** | Fular + fular ringi | €74,90 | €40,48 | €35,13 | Sepet içi upsell, tek tık |
| **★ Adım 2** | **Hediye seti: fular + ring + sert kutu** | **€89,90** | **€49,00** | **€42,72** | **Q4'te ürün sayfasında varsayılan seçili olan** |
| Adım 3 | 2'li fular bundle | €99,90 | €54,71 | €47,80 | "İki baskı" — kendine alım ve 2 hediye alıcısı |
| **★ Adım 4** | **Premium koleksiyon: 2 fular + ring + kutu** | **€139,90** | **€79,97** | **€70,33** | Q4 hero'su; "üç hediye tamam" siparişi |
| Adım 5 | 3'lü fular bundle | €134,90 | €73,67 | €64,63 | Çoklu hediye alıcısı, Reyes |

## 16.2 Mekanikler, kurman gereken sırayla

| # | Mekanik | Uygulama | Beklenen etki | İnşa çabası |
|---|---|---|---|---|
| **1** | **Hediye setini varsayılan seç** | Ürün sayfasında üç seçenek göster, **€89,90 hediye seti önceden seçili**, €59,90 tek ürün "sadece fular" alt seçeneği olarak | En büyük tek AOV kaldıracı. Varsayılanlar seçime hükmediyor | **Düşük — bunu ilk yap** |
| **2** | **€69'da ücretsiz kargo eşiği** | Hero fiyatın hemen üstünde, böylece bir add-on eşiği geçiyor. İspanyol alışverişçi ücretsiz kargoyu #1 sıralıyor (~%65) | Tek alıcıyı €74,90 kademesine itiyor | Düşük |
| **3** | **Ürün sayfasında kargo maliyetini göster** | **İspanyol tüketicilerin %62'si kargo maliyetini ürün sayfasında görmek istiyor**; sepet terki %73,5–74 ve #1 tetikleyici teslimat maliyetinin son ekranda çıkması | Doğrudan CVR kazancı, AOV değil — ama CVR daha büyük kaldıraç (§6.2) | Düşük |
| **4** | **Tek tık post-purchase upsell** | Ödemeden sonra ikinci baskıyı €44,90'a teklif et (açı 32). Ödeme bilgisi tekrar girilmiyor | Tipik olarak DTC yığınındaki en yüksek dönüşen offer. Saf ek katkı — CAC zaten ödenmiş | Düşük (uygulama) |
| **5** | **Sepette "görünümü tamamla"** | Ring €19,90, twilly €24,90, hediye kutusu €6,90 | ~%88 marjda ek AOV | Düşük |
| **6** | **Bundle kurucu: "2 seç, €20 kazan"** | Müşteri iki baskı seçiyor. Seçim tabanlı bundle'lar sabit olanlardan iyi performans gösteriyor | €99,90 kademesini hareket ettiriyor | Orta |
| **7** | **Fiyata göre hediye rehberi navigasyonu** | "€40 altı / €70 altı / €100 altı hediyeler" | Marta'nın sabit bütçeli, çoklu hediye davranışına hizmet ediyor | Düşük |
| **8** | **€90 üzeri ücretsiz hediye** | Ücretsiz kokulu kese veya twilly (COGS ~€2,50, algılanan €12,90–24,90) | 2 ürünlü siparişleri neredeyse sıfır maliyetle eşiğin üstüne itiyor | Düşük |
| **9** | **BNPL (Klarna ve/veya SeQura)** | Klarna üye işyeri AOV'sinde **+%23** ve dönüşümde %20'ye kadar artış bildiriyor; Klarna FR: 7M kullanıcı, 57.500 üye işyeri | €89,90+ seviyesinde anlamlı AOV ve CVR artışı | Orta |
| **10** | **Checkout'ta Bizum (İspanya)** | İspanyol müşterilerin %20–30'u Bizum kullanıyor; 2025'te 100M+ e-ticaret ödemesi | Saf CVR — eksik bir yerel ödeme yöntemi sessiz bir dönüşüm vergisi | **Düşük — İspanya için pazarlığa kapalı** |
| **11** | **Baskı aboneliği / koleksiyoner programı** | "Her çeyrekte yeni baskı, üyeler önce" | Tekrar oranını yükseltiyor — ama §7.6'ya göre buraya aşırı yatırım yapma | Orta — sonra |

## 16.3 Psikolojik fiyatlama kontrolü

| Mimari | Psikolojik olarak sağlam mı? | Gerekçe |
|---|---|---|
| 1 fular €59,90 / 2'si €99,90 | **Evet** | €99,90 vs €119,80 = görünür €19,90 tasarruf ve bu tam olarak bir twilly'ye eşit. Yuvarlak sayı bariyeri (€100 altı) korunuyor. Güçlü |
| Hediye seti €89,90, €6,90'lık kutu ücretsiz gösterilerek | **Evet** | Müşteri kutuyu €6,90 fiyatlıyor, dolayısıyla €89,90 = €59,90 + €19,90 ring + ücretsiz kutu okunuyor. Değer yığını okunur ve dürüst |
| €139,90 koleksiyon | **Evet, ama** | €100 psikolojik bariyerinin üstünde. Yanında €99,90 kademesinin görünür olması gerekiyor ki €139,90 *yükseltme* okunsun, atlama değil |
| 3'ü €134,90 | **Zayıf** | €134,90, €139,90 koleksiyonunun *altında* ama içinde bir fular fazla var. **Düzeltme: 3'lü paketi €149,90'a taşı** ya da at ve €139,90 koleksiyonu it. Ucuz olanın daha fazla ürün içerdiği iki komşu offer kafa karıştırıcı bir merdiven |
| Twilly €24,90 tek başına | **Hayır** | Maks CAC ~€3. Asla reklam verme. Add-on ve ücretsiz hediye, başka bir şey değil |
| €99,90 vs €100 | **Evet** | Üç hanenin altında kal. Bu bantta gerçek etkisi var |

**Önerilen nihai merdiven: €59,90 / €74,90 / €89,90 (varsayılan) / €99,90 / €149,90.** €134,90'lık 3'lü paketi at — merdivenin mantığını kırıyor.

**Hedef:** varsayılan seçili €89,90 hediye seti, €69 ücretsiz kargo eşiği ve post-purchase upsell'li bir €59,90 hero, Q4'te **€72–82 harmanlanmış AOV** getirmeli. §8.3'e göre bu bantta bir AOV, €29–30'luk bir CAC'i zarardan kâra çeviren şey.

---

# 17. GOOGLE ADS

## 17.1 Kanal ne için

**Google senin kâr kanalın, büyüme kanalın değil.** Kanıt:

| Metrik | Değer | Kaynak |
|---|---|---|
| Avrupa e-ticaret **Shopping CPC'si** | **€0,29–0,35** (2025 Q3 ~€0,29–0,30; Kas–Ara 2025 €0,34'e sıçrama; Mar 2026'da €0,35) | smec Market Observer (yıllık €450M Avrupa perakende reklam harcaması paneli) |
| Q4 Shopping CPC enflasyonu | **+%25–30**; Black Friday CPM'leri YoY +%18 | 2025/2026 benchmark'ları |
| Hazır giyim Google CPC (global) | 1,64 $ ≈ €1,51 | 2025/2026 benchmark'ları |
| Hazır giyim/moda/mücevher ort. CPC | 4,31 $ ≈ €3,97 | 2026 benchmark'ı — **ABD ağırlıklı; Avrupa için dikkate alma** |
| Avrupa CPC YoY büyümesi | ~%13'ten (2025 sonu) ~%4'e (2026 Q3) yavaşlıyor | smec |

**€0,35 CPC ve %3 CVR'de CAC'in yaklaşık €11,70.** €27,18 tavana karşı son derece kârlı — modellediğim her senaryoda Meta'dan iyi. §8'in harmanlanmış görünümünde işlendi: €0,55 harmanlanmış CPC ve %3 CVR'de €5.000 Google, €18 CAC'le ~273 sipariş ve **3,27x ROAS** üretiyor; Meta'nın Q4 CPM'lerinde 0,88x'ine karşı.

**Ama — ve bunu nasıl kullanacağını belirleyen kısıt bu — İspanya'da premium şal arama hacmi ince.** "Foulard" olgun bir Fransız arama davranışı; İspanyolca karşılıkları daha düşük hacimli. **Anahtar kelime hacmi alamadım** (sandbox'tan Keyword Planner erişimi yok). Dolayısıyla: Google İspanya'da muhtemelen €1.500–5.000/ay bandında tavan yapacak, nitelikli niyet tükenip CPC'ler yükselmeden önce. İşi taşıyamaz. **Harmanlanmış CAC'ini sübvanse edebilir** ve marjinal bir Meta performansını genel olarak kârlı kılabilir.

**Bütçe ayırmadan önceki aksiyon:** aşağıdaki keyword setleri için Keyword Planner'dan gerçek hacimleri çek (Google Ads hesabıyla ücretsiz, 30 dakika). İspanya'da markalı olmayan exact-match toplam hacim ~5.000/ay altındaysa Google'ı €1.500/ay ile sınırla ve onu büyüme değil marj olarak gör.

## 17.2 İspanyolca keyword mimarisi

| Küme | Anahtar kelimeler | Niyet | Beklenen CPC | Öncelik |
|---|---|---|---|---|
| **Hediye niyeti (en değerli)** | `regalo mujer elegante`, `regalo para mi madre`, `regalo original mujer`, `regalo mujer 50 años`, `regalo navidad mujer`, `regalo reyes mujer`, `regalos elegantes para mujer` | **Çok yüksek — Álvaro** | Orta-yüksek | **★★★ İlk bunu finanse et.** En yüksek AOV, en düşük fiyat hassasiyeti ve Meta'nın ulaşmakta zorlandığı avatar |
| **Ürün + malzeme** | `pañuelo de seda mujer`, `pañuelo seda natural`, `fular de seda mujer`, `pañuelo seda 100%`, `foulard seda mujer` | Yüksek | Düşük-orta | ★★★ Çekirdek Search + Shopping |
| **Ürün + kalite/stil** | `pañuelo mujer elegante`, `fular elegante mujer`, `bufanda elegante mujer`, `pañuelo estampado mujer`, `pañuelo cuadrado mujer 90x90` | Yüksek | Düşük-orta | ★★★ |
| **Ürün jenerik** | `pañuelo mujer`, `fular mujer`, `foulard mujer`, `bufanda mujer`, `chal mujer`, `pashmina mujer` | Orta — karışık niyet | Düşük | ★★ Sadece Shopping; Search için çok geniş |
| **Vesile / sezon** | `pañuelo para boda`, `fular para invitada`, `chal para vestido`, `pañuelo primavera`, `bufanda invierno mujer` | Yüksek ve spesifik | Düşük-orta | ★★ Sezonluk kampanyalar |
| **Rakip / conquest** | `pañuelo massimo dutti`, `fular el corte inglés`, `pañuelo seda hermes alternativa`, `pañuelos como hermes` | Yüksek | Orta-yüksek | ★ Küçük ve dikkatli çalıştır. Reklam metninde asla marka adı kullanma |
| **Markalı (bunu kur)** | `[markan]`, `[markan] pañuelos`, `[markan] opiniones` | En yüksek CVR | **Çok düşük** | **★★★ Her zaman açık.** Agregatör teklifine karşı savunma ve Meta reklamından sonra arayanı yakalama — **gerçek Meta dönüşümlerinin önemli bir kısmı, birkaç sent ödemen gereken markalı bir Google aramasıyla gelecek** |

## 17.3 Fransızca keyword mimarisi (2027 için)

| Küme | Anahtar kelimeler | Not |
|---|---|---|
| **Hediye niyeti** | `cadeau femme élégante`, `cadeau femme original`, `cadeau pour ma mère`, `cadeau noël femme`, `idée cadeau femme 50 ans`, `cadeau maman noël` | İspanya'yla aynı en-değerli mantık |
| **Ürün + malzeme** | `foulard soie femme`, `foulard en soie`, `carré de soie femme`, `écharpe soie femme`, `foulard soie made in France` | **Sondakine dikkat** — "made in France" bu kategoride aktif bir arama niteleyicisi. Bunu karşılayamazsın. Negatif olarak ekle |
| **Ürün + stil** | `foulard femme élégant`, `foulard imprimé femme`, `carré de soie 90x90`, `étole soie femme`, `châle femme élégant` | Çekirdek |
| **Ürün jenerik** | `foulard femme`, `écharpe femme`, `châle femme`, `étole femme`, `bandana soie femme` | Sadece Shopping |
| **Vesile** | `foulard mariage invitée`, `étole pour robe de soirée`, `foulard cheveux soie` | `foulard cheveux` ayrı ve güçlü bir Fransız davranışı — kendi ürün sayfasına değer |
| **Conquest** | `foulard type hermès`, `alternative foulard hermès`, `foulard comme sézane` | Dikkatli, küçük bütçe |

## 17.4 Kampanya yapısı

| Kampanya | Tip | Bütçe payı | Amaç |
|---|---|---|---|
| Marka savunması | Search, exact + phrase | %5 | Ucuz, ~%100 CVR, agregatörlere karşı savunma |
| **Hediye niyeti** | Search, phrase + exact, **ağırlıklı Eki–Ara + 26 Ara–5 Oca** | **%30** | Hesaptaki en yüksek AOV'li trafik |
| Ürün + malzeme/stil | Search, phrase + exact | %25 | Çekirdek ticari niyet |
| **Shopping / feed'li PMax** | Önce Shopping; **PMax sadece ayda 30+ dönüşüm olunca** | **%35** | €0,29–0,35 Shopping CPC'si, herhangi bir yerde alabileceğin en ucuz nitelikli tıklama |
| Conquest | Search, sadece exact, düşük tavan | %5 | Test et, CAC €30'u geçerse hızla kapat |

**Performance Max'e dair özel not:** oradan başlama. PMax optimize etmek için dönüşüm hacmine ihtiyaç duyuyor, yoksa bütçeni düşük niyetli Display ve YouTube envanterine harcar. **Standart Shopping artı sıkı bir Search hesabıyla başla.** Ayda tutarlı 30+ dönüşümün olunca PMax'e geç ve o zaman bile Brand-excluded Search'le yan yana çalıştır, yerine değil.

**Merchant Center ön koşulları:** varyant başına GTIN veya MPN, doğru `product_type` ve `google_product_category` taksonomisi ve bu kategori için kritik olarak **doğru `material` ve `size` niteliği.** Shopping'de oyunun tamamı feed kalitesi ve bu, yeni markaların çoğunun kötü yaptığı bir günlük iş.

---

# 18. SEO FIRSATI

**Değerlendirme: kurmaya değer, test penceresi içinde geri dönmez.** İspanyol moda aksesuarında anlamlı organik trafiğe gerçekçi süre 6–12 ay. Yani SEO, 2026 Q4'te başlaman gereken bir **2027 Q4** varlığı — çünkü içerik aynı zamanda reklam creative'i ve e-posta içeriği olarak ikiye katlanıyor, ki bu özellikle senin için gerçek maliyetini sıfıra yaklaştırıyor.

**Yine de yapmanın stratejik nedeni:** MaraSilk ve La Caressette tam bu kümelerde ("silk scarf trends 2026", "silk scarf colours and prints") zaten sıralanıyor. Trafiğin var olduğunu kanıtlıyorlar. Ve yazdığın her styling makalesi, halihazırda yazmış olduğun bir Reels senaryosu.

## 18.1 İspanyolca keyword kümeleri

| Küme | Hedef sayfalar | Arama niyeti | Ticari değer | Çaba |
|---|---|---|---|---|
| **Nasıl takılır / styling** | `cómo llevar un pañuelo`, `cómo atar un pañuelo al cuello`, `formas de llevar un fular`, `nudos de pañuelo`, `cómo poner un pañuelo en el pelo`, `cómo llevar pañuelo en el bolso` | Bilgilendirici, **yüksek hacimli evergreen** | **Yüksek** — bu, çekmece itirazının ölçekli hali ve trafik dönüşüyor çünkü zaten ürün-meraklı | Orta. **★★★ Buradan başla** |
| **Hediye rehberleri** | `regalos para mujer elegante`, `qué regalar a una mujer de 50 años`, `regalos originales para mi madre`, `regalos de navidad para mujer`, `regalos de reyes para mujer` | Ticari araştırma | **Çok yüksek** — ve sezonluk, yani bir kez sıralanıp her Q4 hasat edebilirsin | Orta. **★★★ Aralık'ta sıralanmak için Ağustos'ta yayınla** |
| **Kombin fikirleri** | `looks con pañuelo`, `outfits con fular`, `cómo combinar un pañuelo estampado`, `pañuelo con abrigo` | Bilgilendirici | Orta-yüksek | Orta |
| **Malzeme eğitimi** | `seda natural vs poliéster`, `qué es la seda de morera`, `cómo lavar un pañuelo de seda`, `cómo cuidar la seda` | Bilgilendirici | **Orta — ama yüksek güven değeri.** Bakım içeriği, Carmen ve Pilar'ın satın almadan önce okuduğu şey | Düşük. **★★ Ucuz otorite** |
| **Stil kimliği** | `estilo francés mujer`, `cómo vestir con estilo parisino`, `estilo mediterráneo`, `armario cápsula mujer` | Bilgilendirici, özlem | Orta | Orta |
| **Sezonluk / trend** | `tendencias pañuelos 2027`, `colores de temporada`, `accesorios de invierno mujer` | Bilgilendirici | Orta, yıllık yenilenir | Şablon kurulduktan sonra düşük |
| **Karşılaştırma / alternatif** | `alternativas al pañuelo de hermès`, `mejores marcas de pañuelos de seda` | **Ticari, yüksek niyet** | **Yüksek** | Orta. Olgusal ol — asla kötüleme |

## 18.2 Fransızca kümeler (2027)

`comment porter un foulard` · `comment nouer un foulard` · `nœuds de foulard` · `foulard dans les cheveux` · `idée cadeau femme élégante` · `cadeau femme 50 ans` · `style parisien femme` · `comment laver un foulard en soie` · `soie naturelle ou polyester` · `tendances foulards 2027` · `alternative foulard hermès`

## 18.3 Çift iş yapan içerik varlığı

**Tek bir şey kur: "Fular bağlamanın 12 yolu" sayfası + 12 bölümlük video serisi.** O tek asset aynı anda:

1. En değerli SEO sayfan (en üst bilgilendirici kümeyi hedefliyor)
2. 12 ayrı Reels/TikTok (creative açıları 1, 3, 4, 29)
3. CVR'yi yükselten ürün sayfası gömülü videosu — **§6.2'ye göre en önemli kaldıraç**
4. 12 e-postalık welcome flow
5. Kutudaki basılı düğüm kartı, ki tekrar alımı ve referansı sürüklüyor
6. Fular styling içeriğinin gerçek uzun-kuyruk keşfi olduğu Pinterest asset seti

**Bu, plandaki en yüksek kaldıraçlı içerik yatırımı ve doğrudan senin zaten yaptığın işe oynuyor.** İkinci haftada, medyaya gerçek para harcamadan önce kur.

---

# 19. TEDARİK ZİNCİRİ

## 19.1 Türk tedarik manzarası

| Tedarikçi | Konum | Yetenek | Fiyatlama (bildirilen) | MOQ | Private label |
|---|---|---|---|---|---|
| **Hicabistan** | İstanbul | 2004'ten beri fabrika-direkt başörtü/fular üreticisi, 50+ ülkeye gönderiyor | **adet €1,90'dan** | **renk başına 10 adet** | **Dokuma etiket, özel nakış, renk eşleşmeli kumaş, markalı ambalaj.** 5–8 gün kargo |
| **Woolgold** | İstanbul | Moda markaları için premium el yapımı şal/fular; ileri dokuma ve baskı | Yayınlanmamış | Yayınlanmamış | Toplu üretim, private label, global teslimat. Kaşmir, yün, ipek, karışımlar |
| **Alıcıoğlu** | Türkiye | 1941'den beri üretici/toptancı/ihracatçı; ayrıca başka şal markalarının yetkili distribütörü | "Rekabetçi toptan, hacim indirimi" | **"Esnek"** | **Private label & OEM, özel etiketleme, butikler için özel tasarım üretimi** |
| Pazar genel | Bursa, İstanbul, Denizli, İzmir | — | 50–100 adet MOQ'da **FOB 3–4 $**; 1.000 adet MOQ'da **ipek €1,50–2/adet** | Tedarikçiye göre 50–1.000 | Yaygın |
| Referans markalar | — | **Armine, Aker** Bursa/İstanbul'dan 140+ ülkeye ihraç ediyor | — | — | Üretim tabanının ihracat kapasitesinin kanıtı |

**Kritik operasyonel bulgu: dokuma etiket ve markalı ambalajla renk başına 10 adet MOQ.** Bu olağanüstü düşük bir taahhüt. **Beş baskı × üç renk = 150 adedi kabaca €300–800 ürün maliyetiyle** doğrulayabilir ve içine kendi etiketini koydurabilirsin. Hiçbir Çinli tedarikçi bunu yapmaz, hiçbir Avrupalı üretici bu fiyata yapmaz.

**Fiyat değil, bu, Türk avantajı — ve fiyattan daha değerli.** Bir ürün bahsini bir creative testine çeviriyor, ki bu tam senin iyi olduğun bahis türü.

## 19.2 Fiyatlaman gereken maliyet avantajı problemi

| Kanıt | Rakam | Kaynak |
|---|---|---|
| Türkiye'de asgari ücret artışı | **2022–2024 arasında +%249**, rakip ülkeleri fazlasıyla aşarak | WWD Sourcing Journal |
| Enerji maliyeti | **İkiye katlandı** | Turkish Minute |
| Finansman | **%50'ye kadar** faiz | Turkish Minute |
| Sektör hasarı | Hazır giyimde **7 milyar $ üretim kaybı, 210.000 iş kaybı** | Kohan Textile Journal / PolyesterTime |
| İhracat | Tekstil ve hazır giyim ihracatı **2025 boyunca ve 2026'ya sarkarak düştü**; fabrika kapanışları; düşen kapasite kullanımı; işten çıkarmalar | Çoklu sektör basını |
| Lira | USD'ye karşı **yılbaşından beri −%8, 12 ayda −%17**, buna karşı **%32,6 TÜFE** (May 2026). USD/TRY ~46 | ING, Naga, Trading Economics |
| Politika niyeti | Merkez bankası, kur zayıflığının enflasyon beklentilerini beslememesi için **nominal değer kaybını enflasyondan yavaş** tutuyor | TCMB çerçevesi (ING üzerinden) |
| Sektörün kendi değerlendirmesi | "Kurun baskılanmaya devam etmesi Türk tekstil sektörünün küresel pazarlardaki rekabetçiliğini daha da azalttı" | Türk tekstil sektörü analizi |

**Düz anlamı: Türk maliyetleri her yıl euro bazında, tasarım gereği artıyor.** %32,6 enflasyona karşı %17 nominal değer kaybı, yılda kabaca %13–15 reel lira değerlenmesi aritmetiği. Bugünkü €8 landed maliyetin, aynı spesifikasyonda 2028'de makul biçimde €10–11.

**Üç somut aksiyon:**
1. **TRY değil EUR üzerinden teklif al ve sözleşme yap.** Kur riskini tedarikçiye it. Siparişe ihtiyaçları olduğu için kabul ederler.
2. **12 aylık fiyat kilidi** al, hacim taahhüdüyle, ideal olarak Türk TÜFE'si değil AB TÜFE'si ile sınırlanmış bir fiyat-revizyon maddesiyle.
3. **İşi €8 değil €12 landed üzerinden modelle.** €12 landed, €59,90 perakende ve %10 iadeyle maks CAC'in hâlâ ~€23 — iş ayakta. Planın sadece €5 landed'de çalışıyorsa, çalışmıyor.

## 19.3 Türkiye'den direkt gönderim vs İspanya'da stok

| Faktör | Türkiye'den direkt | **İspanya'da stok** |
|---|---|---|
| İşletme sermayesi | **Minimum** — stok riski yok | Stokta €2.000–6.000 bağlı |
| Müşteriye teslim süresi | 5–8 gün (Hicabistan 50+ ülkeye 5–8 gün belirtiyor) | **24–48 saat** yurt içi (GLS ~24 s; SEUR aynı gün/13:30 seçenekleri) |
| Sipariş başına kargo | Değişken, birim başına yüksek; uluslararası tarife | €4,20 pazarlıklı yurt içi |
| **1 Temmuz 2026'dan itibaren gümrük** | **Açıkta.** AB €150 muafiyetini kaldırdı ve **adet başına geçici sabit €3** getiriyor (tarife satırı başına, 1 Tem 2028'e kadar), AB'ye giren e-ticaret akışlarının ~%93'ünü kapsıyor | **Açıkta değil.** Tek toplu ithalat, bir kez gümrüklendi |
| AB–Türkiye Gümrük Birliği muaf tutar mı | **ÇÖZÜLMEMİŞ.** A.TR belgeleri tekstil dahil sanayi malları için gümrüksüz dolaşım sağlıyor, ama A.TR koli başına B2C için değil ticari sevkiyatlar için tasarlanmış bir *serbest dolaşım* belgesi. Kamusal rehberlik yeni sabit ücretle etkileşimi net biçimde ele almıyor | Çözülmüş: A.TR ile toplu ithalat, gümrüksüz, bitti |
| KDV mekanizması | IOSS (asli değeri ≤€150 olan sevkiyatlar; asli değerin ayrıca kalemlenmiş kargoyu dışladığını not et) | **OSS** — daha basit, ve zaten İspanyol KDV'sine kayıtlısın |
| İadeler | **Ciddi problem.** €59'luk bir fuları Türkiye'ye iade ettirmek ürünün kendisinden pahalı. Yine de bir İspanyol iade adresine ihtiyacın olurdu | Önemsiz — 3PL hallediyor |
| Ücretsiz kargo ekonomisi | Zor. **Ücretsiz kargo İspanya'da #1 mağaza seçim sürücüsü (~%65)** — vermek zorundasın ve uluslararası tarife bunu acı verici kılıyor | €4,20/koli ile kolay |
| Müşteri güveni | **Kolinin üstünde Türk gönderici adresi görünüyor.** Türkiye, AB alışverişçilerinin güvendiğini söylediği ülkeler arasında yok | İspanyol gönderici, İspanyol iade adresi |
| Q4/Reyes kabiliyeti | **Teslim tarihi vaat edemezsin.** Álvaro ve Marta avatarlarını öldürüyor, ki Q4 işi onlar | **4 Ocak'ta 24 saat teslimat.** Reyes avantajı bu |
| Kalite kontrol | Kör — ürünleri hiç görmüyorsun | Partiyi denetliyorsun |
| 3PL maliyeti | — | Pick & pack €1,50–2,50/sipariş; depolama €8–45/palet/ay; mal kabul €20–30/palet |

**Karar: İspanya'da stok tut. Bu yakın bir karar değil.**

Her biri tek başına yeterli olacak beş bağımsız neden: 1 Temmuz 2026 gümrük değişikliği launch'ından önce iniyor; Türkiye'den Noel veya Reyes teslim tarihi vaat edemezsin; ücretsiz kargo #1 satın alma sürücüsü ve uluslararası olarak karşılanamaz; iadeler ekonomik olarak imkânsız; ve kolinin kendisi müşterilerinin güvendiğini söylemediği bir ülkeyi ilan ediyor.

**Doğru yapı:** A.TR belgeli 300–600 adetlik tek bir hava kargo sevkiyatı, İspanya'ya bir kez gümrüklenip bir İspanyol 3PL'de tutulur (ya da ilk 200 sipariş için kendi evinde — gerçekten uygulanabilir ve öğrenirken sipariş başına €1,80 tasarruf ettirir). 70 g'lık fularlardan 600 adetlik bir sevkiyat ~45 kg — tek bir hava kargo paleti, hatta birkaç büyük kutu. **Bu küçük, ucuz, düşük riskli bir lojistik operasyon; kategorinin iyi seçildiğinin bir başka nedeni de bu.**

## 19.4 Gelen lojistik kontrol listesi

| Kalem | Aksiyon |
|---|---|
| Menşe belgesi | Her sevkiyat için Türk tedarikçiden **A.TR dolaşım belgesi**. Geçerlilik 4 ay. Olmazsa tekstile ~%6–12 MFN vergisi uygulanıyor |
| HS sınıflandırması | HS **6214** (şal, fular, atkı, mantilla, peçe). Kesin alt başlığı lif kompozisyonuna göre müşavirinle doğrula — ipek, yün ve sentetik için alt başlık farklı |
| Gümrük müşaviri | **Birinci haftada bir İspanyol müşavir tut** ve iki soruya yazılı cevap al: (a) 1 Temmuz 2026 sabit €3 ücreti, Gümrük Birliği kapsamındaki Türk menşeli düşük değerli B2C sevkiyatlara uygulanıyor mu, (b) toplu ithalatın için hangi belgeler gerekiyor |
| Navlun | İstanbul → Madrid/Barselona hava kargo. 45 kg küçük ve ucuz bir sevkiyat |
| Gelen denetim | İlk sevkiyatın her adedini kontrol et: kenar kalitesi, baskı register'ı, onaylanmış numuneye karşı renk tutarlılığı, etiket tutunması |
| Etiketleme | Ürünler 3PL'e girmeden önce İspanyolca lif kompozisyonu, kalıcı şekilde takılı (§20). Bunu siparişin parçası olarak tedarikçiyle ayarla — dokuma etiket veriyorlar |
| 3PL | Shopify entegrasyonlu İspanyol 3PL. Özellikle iade yönetimi ve Q4 kesim tarihlerini sor |

---

# 20. HUKUK / VERGİ / E-TİCARET UYUMU

## 20.1 İspanya

| Alan | Gereklilik | Notlar |
|---|---|---|
| **KDV** | **%21 standart oran** | İspanyol KDV'sine kayıt ol. Tüketiciye KDV dahil fiyat ver — AB'de B2C için yasal zorunluluk |
| **OSS** | AB genelinde tek **€10.000 mesafeli satış eşiği**. Altında kendi ülke oranını uygulayabilirsin; üstünde varış ülkesi KDV'si uygulamak ve **OSS** üzerinden raporlamak zorundasın — tek kayıt, tek üç aylık beyan | €10.000'i hızla geçeceksin. OSS'ye proaktif kayıt ol. 1 Oca 2025'ten beri ayrıca €100.000 eşikli opsiyonel bir KOBİ muafiyet şeması var — muhasebecine yapına uygulanıp uygulanmadığını sor |
| **Cayma hakkı** | Teslimden itibaren **14 gün**, gerekçe gerekmiyor. **14 gün** içinde iade, **standart giden teslimat maliyeti dahil** | Pazarlığa kapalı |
| **İade kargosu** | Tüketici iade postasını **sadece satın alma öncesinde söylediğin takdirde** ödüyor. Söylemezsen sen ödüyorsun | **Doğru bilgilendirmemek cayma süresini 14 günden 12 aya kadar uzatabiliyor.** Sözleşme öncesi bilgiyi doğru yap |
| **Tekstil etiketleme** | **Yönerge (AB) 1007/2011.** Kalıcı, okunabilir, görünür ve sağlam takılı etikette lif kompozisyonu, yalnızca yönergenin onaylı lif adlarıyla, **İspanyolca**. "%100", "saf" veya "tamamı" sadece tek lifli ürünler için. Ağırlıkça ≥%80 tekstil lifi içeren ürünlere uygulanıyor, moda aksesuarları dahil | Ayrıca "piyasaya arz edilen" ürünlere uygulanıyor, ki online satış buna dahil. Etiketleri Türk tedarikçiyle ayarla |
| **GPSR** | **Yönerge (AB) 2023/988, 13 Ara 2024'ten beri yürürlükte.** AB dışı bir üretici bir **AB Sorumlu Kişi**'si atamak zorunda; **adı, posta adresi, e-postası ve telefonu ürün, ambalaj veya beraberindeki dokümanda yer almalı** | **Şirketin AB'de yerleşikse bu büyük ölçüde kendi tüzel kişiliğinle çözülüyor.** Türk bir tüzel kişilikten işletirsen atama yapmak zorundasın. Pazar yerleri uyumsuz listeleri kaldırıyor |
| **Tekstil EPR** | **Tekstil ve ayakkabı atığı Kraliyet Kararnamesi taslağı**, 23 Haz 2025'te yayınlandı, 27 May 2026'da Komisyona bildirildi, standstill 28 Ağu 2026'ya kadar, **kabul 2026'da bekleniyor**. Üreticiler — açıkça **İspanyol pazarına ürün arz eden online satıcılar dahil, yerleşik olup olmadıklarına bakılmaksızın** — kayıt olmak, bir **SCRAP**'a katılmak ve toplama/yeniden kullanım/geri dönüşümü finanse etmek zorunda. **Muafiyet eşiği yok.** Ücretler ağırlık ve geri dönüştürülebilirlik bazlı, hızlı-moda uygulamaları dikkate alınıyor. **Ücret faturada ayrı gösterilmeli** | **Henüz bağlayıcı değil — ama ilk tam yılında devreye girmesi muhtemel.** Şimdi adet başına €0,20 karşılık ayır (modelim ayırıyor) ve durumu üç ayda bir kontrol et. "Faturada ayrı gösterilmeli" gerekliliği fatura değişikliği gerektirecek |
| **GDPR** | Pazarlama için hukuki dayanak, gizlilik politikası, her işleyenle DPA (Shopify, Klaviyo, Meta, 3PL), veri sahibi talep süreci | Standart. Shopify-native bir onay uygulaması kullan |
| **Çerezler** | **AEPD rehberliği:** onay özgürce verilmeli; **reddetmek kabul etmek kadar kolay olmalı**; alternatifsiz çerez duvarı yok; onay öncesi zorunlu olmayan çerez yok | İspanya'nın düzenleyicisi bu konuda aktif. Meta pixel'i çalıştırmadan önce uyumlu bir CMP zorunlu |
| **Faturalama** | Satıcı kimliği, KDV dökümü, sıralı numaralandırma içeren basitleştirilmiş fatura/fiş. **Verifactu** e-fatura yükümlülükleri İspanyol işletmeler için kademeli geliyor | İspanyol muhasebecine tüzel kişilik tipin için Verifactu takvimini sor |
| **Mesafeli satış bilgi yükümlülükleri** | Tam tacir kimliği, coğrafi adres, vergi ve teslimat dahil toplam fiyat, ödeme/teslimat düzenlemeleri, cayma hakkı + model form, şikâyet yönetimi, garanti | Eksik kalemler cayma haklarını uzatıyor. Bu sayfayı bir kez, düzgün yaz |
| **Avrupa Erişilebilirlik Yasası (EAA)** | **28 Haz 2025'ten beri yürürlükte.** E-ticaret hizmetleri erişilebilirlik gerekliliklerini karşılamak zorunda (WCAG 2.1 AA / EN 301 549). **Hizmetler için mikroişletme muafiyeti: <10 çalışan VE ≤€2M ciro** | **Launch'ta muhtemelen mikroişletme muafiyetine gireceksin** — ama eşiklerden birini geçtiğin anda muafiyet **geçiş süresi olmadan** kayboluyor. Baştan erişilebilir kur; bir mağazayı sonradan uyarlamak pahalı |
| **Fiyat gösterimi** | **Omnibus Direktifi:** her "eskiden/şimdi" fiyatı, önceki 30 gündeki gerçek en düşük fiyata referans vermek zorunda | Black Friday creative'ini doğrudan kısıtlıyor. §14.2'nin bundle stratejisi problemi tamamen atlatıyor |

## 20.2 Fransa — farkı ne, ve önemsiz değil

| Alan | Fransa'ya özgü gereklilik | Maliyet / çaba |
|---|---|---|
| **KDV** | **%20** standart oran | Aynı OSS mekanizması |
| **Refashion EPR (tekstil)** | Zorunlu kayıt; **ADEME'den alınan Tek Kimlik Numarası (UIN), pazar yerleri dahil Fransa'da tekstil satmanın ön koşulu**. Eko-katkı ~**giysi başına €0,58** (2026 basitleştirilmiş oran) | **İlk satıştan önce sert kapı.** Haftalar süren hazırlık |
| **Fransız temsilci** | **10 Temmuz 2026'dan beri, Fransa'da yerleşik olmayan her EPR yükümlüsü üretici yazılı vekâletle bir Fransız temsilci atamak zorunda** (Çevre Kanunu Md. L.541-10-9-1) | **Yinelenen üçüncü taraf ücreti.** Fransa'nın 2026 Q4 ortak launch'ı olmamasının en büyük tek nedeni bu |
| **Triman + info-tri** | Fransız pazarına arz edilen tüm giyim, ev tekstili ve ayakkabıda **1 Şub 2023'ten beri zorunlu**: Triman logosu artı ayrıştırma talimatı | **Fransa için ayrı etiket ve/veya ambalaj görseli gerekiyor.** Fiziksel bir SKU farkı, sadece web sitesi değişikliği değil |
| **Tekstil etiketleme** | Aynı Yönerge 1007/2011, ama **Fransızca** | Tedarikçiden ikinci etiket varyantı |
| **Tüketici hukuku** | Aynı 14 gün cayma, ama Fransız tüketici belirgin şekilde daha hak-bilinçli ve DGCCRF denetimi aktif | Şartların makine değil profesyonel Fransızca çevirisi gerekiyor |
| **Ödemeler** | **Cartes Bancaires kart payının ~%79'u**, ~%85 checkout dönüşümüyle (sektör ~%75). Wero yükseliyor | **Özellikle CB'yi aktif et.** Etmemek sessiz bir dönüşüm vergisi |
| **Dil** | Fransızca site, destek ve hukuki sayfalar pratikte zorunlu | Gerçek maliyet: profesyonel çeviri, DeepL değil |

**Fransa için özet: uyum yığını (UIN + vekâletli Fransız temsilci + Triman görseli + Fransızca etiketler + çevrilmiş hukuki metinler) tek bir fuları yasal olarak satmadan *önce* sana para ve birkaç hafta götürüyor.** Bunu bir Q4 penceresinde İspanya launch'ıyla eşzamanlı yapmak, founder'ların bir çeyrek kaybetme şekli. Önce İspanya.

---

# 21. MARKA ADI VE KİMLİĞİ

## 21.1 İsimlendirme yönü

**Kriterler:** İspanyolca ve Fransızca telaffuz edilebilir; sert "Türk markası" okuması yok; Hermès'e komşuluk yok (hukuki risk); `.com` veya `.es` müsait; dokuma etikete sığacak kadar kısa; aranabilir (sözlük kelimesi değil).

| Yön | Mantık | Örnek şekiller | Risk |
|---|---|---|---|
| **★ Akdeniz yeri / ışığı** | Konumlandırmaya sadık; ES ve FR'de çalışıyor; sıcak | *Solaria, Meridia, Cala —, Levantine, Poniente, Mistral, Almeria-komşusu türetmeler* | Bazıları alınmış olabilir; iyice kontrol et |
| **★ Uydurma Latince** | Ayırt edici, sahiplenilebilir, tescil edilebilir, sözlük rekabeti yok | *Serilla, Velura, Miralda, Oriela, Lumara* | Bir şey ifade etmesi için marka inşası gerekiyor |
| Founder / atölye | İnandırıcı, insani, founder-video gücüne uyuyor | *Casa —, Atelier —, Maison —* | Fransız olmayan bir markadan "Maison" Fransız alıcıya özenti okunuyor. Fransa planın varsa kaçın |
| Zanaat / malzeme | Anında kategori-okunur | *Seda —, Trama, Urdimbre, Filatura* | Dar; fuların ötesine genişletmek zor |
| İki kelimeli çağrışımlı | Akılda kalıcı, sahiplenilebilir | *Sur & Seda, Casa Poniente* | Daha uzun; etikette zor |

**Öneri: 2–3 heceli, sesli harfle biten uydurma bir Latince kelime.** Hem İspanyolca hem Fransızca'da Avrupa premium okunuyor, tescil edilebilir, alan adı müsaitliği temiz ve seni sadece fulara kilitlemiyor. Bir şey satın almadan önce EUIPO'da Nice sınıf 24 (tekstil) ve 25 (giyim) kontrolü yap.

**Kaçın:** marka adının içinde "Silk", "Luxe", "Premium", "Co.", "Studio" veya bir Türk yer adı geçen her şey. Bursa hikâyeye ait, etikete değil.

## 21.2 Kimlik sistemi

| Unsur | Yön | Gerekçe |
|---|---|---|
| **Renk paleti** | **Taban:** sıcak kırık beyaz (#F5F1EA), derin mürekkep (#1C1C1A). **Aksanlar baskılarından:** terracotta, zeytin, jade, bordo, derin mavi | Sıcak nötrler İskandinav-minimal değil Akdeniz-premium okunuyor, ki bu seni ARKET/COS'tan ayırıyor. Aksan renkleri belgelenmiş 2026 yönüyle eşleşiyor (yoğun kırmızı, derin mavi, jade yeşili) |
| **Tipografi** | **Display:** modern eksenli, yüksek kontrastlı bir serif (Didot değil — çok editöryel-klişe). **Gövde:** nötr hümanist sans | Serif = maliyetsiz kalite iddiası. İki ağırlıkta kal ve aşırı tasarlama |
| **Fotoğraf** | **Bilinçli olarak iki register.** (1) **Editöryel:** altın saat, gerçek Endülüs mimarisi, kumaşta rüzgâr, hareket hâlinde model. (2) **Makro zanaat:** kenarlar, doku, boya, eller. **Minimum flat-lay** | Flat-lay, şal markalarının çoğunun satışı kaybettiği yer — fuları bir kumaş dikdörtgeni gibi gösteriyor. Hareket drape'i iletiyor, ki ürünün gerçek kalitesi o |
| **Ambalaj** | Kraft veya kırık beyaz sert kutu, pelür, mühür sticker, **basılı düğüm kartı** (12 yol), el yazısı tarzı teşekkür notu | §15'e göre kutu AOV kilidi. Düğüm kartı retention ve referans aracı. Toplam maliyet ~€3,50 |
| **Web sitesi** | **Fold üstünde styling videolu** ürün sayfası, hediye seti önceden seçili üç kademeli seçici, ürün sayfasında görünür kargo maliyeti, fotoğraflı yorum duvarı, akordeonlarda lif/bakım/menşe, Bizum + kart + PayPal + Klarna | Bunların her biri belgelenmiş bir İspanyol satın alma sürücüsüne veya itirazına karşılık geliyor |
| **Instagram grid** | %60 styling (nasıl yapılır), %25 editöryel, %15 zanaat/founder. **Reels öncelikli** | Styling içeriği hem funnel'ın üstü hem CVR varlığı |
| **Ses tonu** | Direkt, sıcak, spesifik. Sıfat değil sayı ("kenar başına sekiz dakika", "70 gram", "baskı başına 200"). "Yükselt" yok, "curated" yok, "effortless chic" yok | Spesifiklik, bilinmeyen bir markanın inandırıcılık kazanma yolu |

---

# 22. TEST PLANI — €5.000 SERT TAVAN

## 22.1 Bütçe dağılımı (senin taslağından değişiklik gerekçeli)

| Satır | Senin taslağın | **Benim önerim** | Değişikliğin nedeni |
|---|---|---|---|
| Ürün / numune / ilk stok | €500 | **€1.500 (%30)** | Renk başına 10 adet MOQ'da 5 baskı × 3 renk artı 200–300 adetlik gerçek bir ilk sevkiyat alıp kaliteyi denetleyebilirsin. **Ucuz stok Türk tedarikçinin tüm anlamı — kullan.** €500 numune alır ama başarılı bir testi karşılama kabiliyeti almaz |
| Web sitesi | €500 | **€500 (%10)** | Shopify + iyi bir tema + 4 uygulama (post-purchase upsell, yorumlar, CMP, Bizum). Özel tasarıma para verme. Görselleri kendin üretebiliyorsun |
| İçerik / creative | €500 | **€500 (%10)** | İki ay için ~€250/ay AI araç, artı otantiklik çapaları için modelli bir yarım günlük çekim. **Avantajının bütçe olarak göründüğü yer burası** |
| **Meta Ads** | €3.000 | **€2.000 (%40)** | ~3 hafta boyunca €80–120/gün ile temiz bir okuma için yeterli. **Senin taslağından bilinçli olarak düşük** — CTR×CVR barajı geçmeden €3.000'e çıkmak aynı cevabın daha pahalı versiyonunu satın almak |
| Google Ads | €500 | **€300 (%6)** | Sadece marka savunması + hediye niyeti Search + Standart Shopping. Küçük, çünkü önce keyword hacimlerini çekmen gerekiyor (§17.1) |
| **Uyum / hukuk / müşavir** | €0 | **€200 (%4)** | Gümrük müşaviri yazılı görüşü, GPSR kontrolü, İspanyolca hukuki sayfalar. **Sen bunu sıfır bırakmışsın; işi durdurma olasılığı en yüksek kalem bu** |
| **Anket (400 İspanyol kadın)** | €0 | **€0–300** | Opsiyonel ama yüksek değer (§2.4). Gerekirse ürün satırından finanse et |

**Toplam: €5.000.** Değişikliğin şekli: daha çok ürün, daha az medya. Kazanan bir test seni sevk edemez halde bırakıyorsa reklamlardan hiçbir şey öğrenemezsin.

## 22.2 İlk 30 gün KPI'ları ve sert karar kuralları

Karar hiyerarşisi: **CTR×CVR barajı her diğer metriği geçersiz kılar.** Barajı geçmeyen güzel bir CPM, başarısız bir test.

| KPI | Öldür | Optimize et | Devam et / ölçekle | Notlar |
|---|---|---|---|---|
| **★ Link CTR × session CVR** | 15 konsept ve 150 bin gösterimden sonra **< %0,030** | **%0,030–0,052** | **≥ %0,053** (€13 CPM, €59,90 AOV'de) | **Test bu.** Aşağıdaki her şey nedeninin teşhisi |
| CPM | Sürekli > €25 | €16–25 | < €16 | CPM yüksek *ve* CTR iyiyse kitle/açık artırma. CPM yüksek *ve* CTR düşükse creative |
| Link CTR | 15 konsept sonrası < %0,8 | %0,8–1,5 | **> %1,5** | Avantajın burada görünmeli. 15 konseptle %1,5 link CTR'yi geçemiyorsan problem creative değil ürün veya offer |
| CPC | > €2,00 | €1,00–2,00 | < €1,00 | Türetilmiş; onun yerine CTR'ye bak |
| Landing-page view oranı (LPV/tıklama) | < %70 | %70–85 | > %85 | %70 altı site hızı problemi. Daha fazla harcamadan önce düzelt |
| **Add-to-cart oranı** | Oturumların < %3'ü | %3–7 | **> %7** | Offer gücünün en net okuması. İyi CTR ile düşük ATC = fiyat veya ürün sayfası yanlış |
| Initiate-checkout oranı | ATC'nin < %40'ı | %40–60 | > %60 | Düşükse kargo maliyeti sürprizi veya ödeme yöntemi eksiği. **Bizum'un canlı olduğunu kontrol et** |
| **Session CVR** | < %1,2 | %1,2–2,2 | **> %2,2** | Moda benchmark'ı %2,5–3,1; Shopify ortalaması %1,40. %1,2 altı trafik problemi değil site problemi |
| **CAC** | **> €45** | €28–45 | **< €28** | €27,18 tek ürün tavanı; hediye-seti AOV'sinde €42,72 |
| **AOV** | < €55 | €55–70 | **> €70** | AOV €55 altındaysa hediye-seti mimarisi çalışmıyor; reklamlara dokunmadan önce varsayılan seçimi düzelt |
| ROAS (blended) | < 1,4x | 1,4–2,1x | **> 2,14x** | 2,14x bu maliyet yapısında matematiksel başa baş |
| **Katkı marjı (reklam sonrası)** | €2.000 harcamadan sonra negatif | Başa baş ±%10 | **Pozitif** | Gerçek olan tek metrik |
| İade oranı | > %15 | %10–15 | < %10 | %15 üstü ürün/fotoğraf uyumsuzluğu demek — fotoğraflar fazla vaat ediyor |
| E-posta yakalama oranı | Oturumların < %2'si | %2–5 | > %5 | Q4 için önemli — liste, Kasım'ı soğuk CPM'ler olmadan kârlı kılan şey |

## 22.3 Test sıralaması

| Gün | Odak | Harcama | Başarı koşulu |
|---|---|---|---|
| **1–7** | Mağaza canlı, 15 creative yüklü, pixel çalışıyor, Bizum canlı, uyum sayfaları hazır | €0 medya | Mağaza sipariş alıp sevk edebiliyor. Kendine test siparişi ver |
| **8–14** | **Creative okuması.** €80/gün, tek kampanya, broad, 15 konsept | €560 | En az 3 konseptte **link CTR > %1,2**. Hiçbiri %1,2'yi geçmiyorsa dur ve creative'i yeniden kur — üstüne harcama |
| **15–24** | **Dönüşüm okuması.** €100/gün, en iyi 5 konsepti ölçekle, hediye setini varsayılan seç, post-purchase upsell ekle | €1.000 | **CTR×CVR ≥ %0,040 ve AOV ≥ €65** |
| **25–30** | **Ekonomi okuması.** €70/gün, Google marka + hediye niyeti Search ekle | €420 + €300 | **CTR×CVR ≥ %0,053, CAC < €30, katkı ≈ başa baş veya üstü** |
| **Karar noktası, gün 30** | — | €5.000'in ~€2.300'ü harcandı | **Baraj geçti → Q4'ü finanse et ve stok sipariş et. Baraj %30'dan az kaçırıldı → offer + landing page'in bir kez 30 günlük yeniden kurulumu, creative'in değil. %30'dan fazla kaçırıldı → dur.** Elinde hâlâ ~€2.700 olacak |

**Bu planın en önemli özelliği: €5.000 değil €2.300 karşılığında başarısız olabiliyor.** Gün 30 kill kapısını kur ve ona uy.

---

# 23. 90 GÜNLÜK YOL HARİTASI

## Gün 1–30: Barajı kanıtla

| Track | Aksiyonlar |
|---|---|
| **Ürün** | Numune siparişi: 2 tedarikçiden paralel 5 baskı × 3 renk (~150 adet, ~€300–800). Kenar, baskı register'ı, renk, gramaj denetle. Tek tedarikçi seç. **Dokuma etiket + İspanyolca lif etiketiyle 250–300 adetlik ilk siparişi ver.** Fular ringi ve sert kutu tedarik et |
| **Branding** | İsim + EUIPO kontrolü (sınıf 24, 25) + alan adı. Logo, palet, tipografi. Ambalaj görseli. **Sevilla'da tek modelle yarım günlük çekim** — AI genişletmesi için gerçek çapalar |
| **Web sitesi** | Shopify + tema. Fold üstünde styling videolu ürün sayfası, **€89,90 hediye seti önceden seçili** 3 kademeli seçici, ürün sayfasında kargo maliyeti, lif/bakım/menşe akordeonları. **Bizum + kart + PayPal.** Reddetmek-kabul-etmek-kadar-kolay CMP. Tam hukuki sayfalar. Uçtan uca test siparişi |
| **Creative** | §13'ten **15 konsept**: küme 1'in tamamı (1–5), dönüşüm (6–7), zanaat (12, 13, 15), hediye (20, 21, 24), kıtlık (31). **12 yol video serisini kur** — SEO sayfası, Reels, ürün sayfası videosu, e-posta akışı ve düğüm kartı, hepsi tek şeyde |
| **Meta** | 1 kampanya, 2 ad set, her birinde 8–15 çeşitli creative, broad + Advantage+, İspanya (adalar hariç), kadın 25–60. €80–100/gün. **CTR×CVR'yi günlük izle** |
| **Google** | GTIN, `material` ve `size` nitelikleriyle Merchant Center feed'i. Marka savunması + hediye niyeti Search + Standart Shopping. €10/gün. **Keyword Planner'dan gerçek hacimleri çek ve Fransa Google durumuna karar ver** |
| **CRO** | Birinci siparişten yorum uygulaması. Fotoğraflı yorumlar teşvikli. LPV oranı %85 altındaki her şeyi düzelt |
| **E-posta** | Klaviyo. Welcome flow (12 yol), sepet terk, gezinme terk, satın alma sonrası. İndirim değil styling rehberi teklif eden pop-up |
| **Upsell'ler** | Post-purchase tek tık: ikinci baskı €44,90. Sepette: ring €19,90, twilly €24,90, hediye kutusu €6,90 |
| **Stok / ops** | 3PL mi kendin mi (~200 siparişe kadar kendin iyi ve sipariş başına €1,80 tasarruf). **1 Temmuz 2026 sabit ücreti ve Türk menşei üzerine gümrük müşaviri yazılı görüşü** |
| **Uyum** | İspanyol KDV + OSS kaydı. GPSR Sorumlu Kişi teyit. İspanyolca lif etiketleri. Cayma/iade bilgilendirmesi ilk satıştan *önce* doğru yazılmış |

**Gün 30 barajı: CTR×CVR ≥ %0,053, AOV ≥ €65, CAC < €30.**

## Gün 31–60: Offer'ı kanıtla ve stoğu al

| Track | Aksiyonlar |
|---|---|
| **Ürün** | Kazanan 2–3 baskıdan **600–1.000 adet tekrar sipariş** (yalnızca baraj geçtiyse). Twilly SKU'sunu ekle. **12 aylık EUR fiyatlaması** müzakere et, TÜFE-sınırlı revizyon maddesiyle |
| **Branding** | İspanyol moda medyasına ve 10 mikro-creator'a ulaşma (ücretli değil, hediye). Yorum duvarını fotoğraflı 25+'a çıkar |
| **Web sitesi** | **Fiyat kademesine ve alıcıya göre hediye rehberi sayfaları.** Reyes landing page'i şimdi kur, gizli tut. Hız optimizasyonu. Erişilebilirlik geçişi (muhtemelen mikroişletme muafındasın ama doğru kur) |
| **Creative** | **+10 yeni konsept.** Açı 15 (founder hikâyesi) ve açı 12 (Bursa) uzun-form test et — bunlar farklılaştırıcı asset'lerin. Styling serisini sürekli içerik motoru olarak başlat |
| **Meta** | CAC tutuyorsa kazananları €200–300/gün'e ölçekle. Lookalike ekle (satın alanların %1'i, sonra %2–3). Retargeting havuzlarını kasıtlı kur — Kasım'ı ucuz kılan şey onlar. **Prospecting ve retargeting raporlamasını ayır, yoksa blended ROAS seni kandırır** |
| **Google** | CAC < €25 ise Shopping'i ölçekle. Vesile keyword'leri ekle. PMax'i **sadece** ayda 30+ dönüşümün üstündeyse düşün |
| **CRO** | Varsayılan kademe seçimi, ücretsiz kargo eşiği (€59 vs €69) ve ürün sayfası video pozisyonu A/B testi. **Klarna veya SeQura ekle** (AOV +%23 bildiriliyor) |
| **E-posta** | Alıcı vs gezinen segmentasyonu. BF erken erişim penceresi için VIP listesi başlat. Gün 60'ta 3.000+ abone hedefi |
| **Upsell'ler** | €139,90 premium koleksiyonu başlat. **Merdiveni düzelt: 3'lü paketi €149,90'a taşı veya at** |
| **Stok / ops** | İspanyol 3PL'e geç. Q4 kesim tarihlerini ve iade sürecini **yazılı olarak** anlaş |

## Gün 61–90: Q4'ü yükle

| Track | Aksiyonlar |
|---|---|
| **Ürün** | **Stok 30 Eylül'e kadar gelmiş ve denetlenmiş.** Limited edition BF baskısı üretilmiş (200 numaralı adet). Hediye kutuları ve düğüm kartları tahminin 1,2 katı stokta |
| **Branding** | Reyes kampanya creative'i kurulmuş ve onaylanmış. Hediye paketleme hizmeti canlı. İadelerin 15 Ocak'a uzatılması politikası yayınlanmış |
| **Web sitesi** | Teslimat son tarih geri sayım bileşeni. "€40/€70/€100 altı hediyeler" navigasyonu. Reyes sayfası 26 Aralık'ta yayına hazır |
| **Creative** | **Hediye kümesini (20–25) tamamla.** Reyes setini (açı 25) üret — neredeyse hiç kimsenin olmayacak. 35+ toplam konsepte ulaşmak için 10 tane daha |
| **Meta** | **Ekim'i +%41 Kasım CPM enflasyonundan önce öne yükle.** 1–20 Kasım'da VIP erken erişim. **BFCM haftasında soğuk harcamayı sert kes** ve retargeting + e-postayla hasat et. 26 Ara–5 Oca için CPM'ler çökerken bütçe ayır |
| **Google** | Hediye niyeti Search'ü Ekim–Aralık boyunca sert ölçekle. Reyes için 26 Ara–5 Oca arası açık tut |
| **CRO** | Teslim tarihi garantisi öne çıkarılmış. Hediye mesajı alanı. Tek sayfa checkout. Checkout'ta güven işaretleri (İspanyol alışverişçilerin %38'i hâlâ ödeme güvenliği kaygısı belirtiyor) |
| **E-posta/SMS** | Tam Q4 takvimi. VIP erken erişim. Teslimat son tarih dizisi. **27 Ara–4 Oca Reyes dizisi** |
| **Upsell'ler** | "Üç hediye, tek sipariş" bundle €149,90. €90 üzeri ücretsiz twilly |
| **Stok / ops** | Tekrar sipariş temin süresi teyit (Türkiye 5–8 gün kargo + üretim). **Aralık'ın ikinci haftasında stok tükenmesin** — hero baskıda %20 tampon tut |

---

# 24. EN KÖTÜ / BAZ / EN İYİ SENARYO, ÖLÇEKTE

CAC, 0,15 esneklikle harcamayla birlikte şişiyor (her katlamada CAC ~%11 artıyor) — tek bir ülkede dar bir kategori için muhafazakâr-gerçekçi bir varsayım. Katkı net gelirin %65,5'i, %10 iade.

**Bu maliyet yapısında break-even blended ROAS: 2,14x.**

## En kötü senaryo — düşük CTR (%1,0), düşük CVR (%1,0), €16 CPM, €49,90 AOV

| Reklam harcaması | CAC | Sipariş | Ciro | ROAS | Katkı | **Reklam sonrası net** | Cironun %'si |
|---|---|---|---|---|---|---|---|
| €5.000 | €188 | 27 | €1.325 | 0,27 | €613 | **−€4.387** | −%331 |
| €10.000 | €209 | 48 | €2.386 | 0,24 | €1.104 | **−€8.896** | −%373 |
| €25.000 | €240 | 104 | €5.199 | 0,21 | €2.405 | **−€22.595** | −%435 |
| €50.000 | €266 | 188 | €9.372 | 0,19 | €4.335 | **−€45.665** | −%487 |

**Okuma:** bu, ölçekle birlikte kötüleşen tam bir kayıp. Ayrıca link CTR'yi izlersen **14 gün ve €560 harcama içinde tespit edilebilir.** En kötü senaryo "€50.000 kaybetmek" değil — gün 30 barajına uyduğun sürece "€2.300 kaybetmek ve durmak."

## Baz senaryo — pazar ortalaması Meta (%1,5 CTR, %1,8 CVR, €13 CPM, €59,90 AOV)

| Reklam harcaması | CAC | Sipariş | Ciro | ROAS | Katkı | **Reklam sonrası net** | Cironun %'si |
|---|---|---|---|---|---|---|---|
| €5.000 | €54,71 | 91 | €5.474 | 1,09 | €2.555 | **−€2.445** | −%45 |
| €10.000 | €60,71 | 165 | €9.866 | 0,99 | €4.605 | **−€5.395** | −%55 |
| €25.000 | €69,65 | 359 | €21.499 | 0,86 | €10.035 | **−€14.965** | −%70 |
| €50.000 | €77,28 | 647 | €38.751 | 0,78 | €18.087 | **−€31.913** | −%82 |

**Okuma — ve kararını yönetmesi gereken bulgu bu: pazar ortalaması performans, cironun her euro'sunda kabaca 45–50 sent kaybediyor ve ölçeklemek daha da kötüleştiriyor.** Ortalama uygulamanın kâra geçtiği bir hacim yok. Bunu, ortalama uygulamanın ince kâr ürettiği e-ticaret kategorilerinin çoğuyla karşılaştır. **Bu kategori, girmenin bedeli olarak ortalamanın üstünde uygulama talep ediyor.**

## En iyi senaryo — güçlü creative (%2,5 CTR, %2,6 CVR, €12 CPM, €72 AOV)

| Reklam harcaması | CAC | Sipariş | Ciro | ROAS | Katkı | **Reklam sonrası net** | Cironun %'si |
|---|---|---|---|---|---|---|---|
| €5.000 | €20,51 | 244 | €17.550 | 3,51 | €8.253 | **+€3.253** | +%19 |
| €10.000 | €22,76 | 439 | €31.631 | 3,16 | €14.875 | **+€4.875** | +%15 |
| €25.000 | €26,11 | 958 | €68.948 | 2,76 | €32.417 | **+€7.417** | +%11 |
| €50.000 | €28,97 | 1.726 | €124.255 | 2,49 | €58.420 | **+€8.420** | +%7 |

**Okuma:** en iyi senaryo bile **€50.000 harcamada €8.400 net katkı** üretiyor — kârlı bir iş, ama *ince* bir iş, çünkü ölçeklerken CAC enflasyonu marjı yiyor. Net marj €5 bin ile €50 bin arasında %19'dan %7'ye düşüyor.

**Üç sonuç:**
1. **Bu, gerçekçi ölçekte yılda €100–300 bin katkılı bir iş, €1 milyonluk değil** — pazar eklemedikçe, kategori eklemedikçe ya da AOV ve tekrar oranını modellediğimin belirgin ötesine taşımadıkça.
2. **Gerçek para tekrar satın almada ve e-postada, paid ölçekte değil.** €21'e kazanılan ve müşterisi €0 CAC'le tekrar alan her sipariş €28–34 saf katkı ekliyor. Varlık, liste.
3. **Q4 konsantrasyonu senin lehine.** €50.000'i düşen verimlilikle yıla yaymak yerine, €25.000'i Q4'te zirve niyette harca ve yılın kalanında harcamayı düşük tut. Sezonluk yapı gerçek (Eki ve Ara arama zirveleri) ve ekonomi konsantrasyonu ödüllendiriyor.

## Q4 harmanlanmış görünüm — Baz senaryo, €25 bin Meta + €5 bin Google

| Kanal | Harcama | Sipariş | Ciro | CAC | ROAS |
|---|---|---|---|---|---|
| Meta (+%25 ortalama Q4 CPM'de) | €25.000 | 366 | €21.896 | €68,39 | 0,88 |
| **Google** (Shopping + hediye niyeti Search, €0,55 CPC, %3 CVR) | €5.000 | 273 | €16.336 | **€18,33** | **3,27** |
| **Harmanlanmış** | **€30.000** | **639** | **€38.232** | **€46,95** | **1,27** |

Katkı €17.848, eksi €30.000 reklam harcaması, eksi ~€3.600 sabit gider = **yaklaşık €15.750 faaliyet zararı.**

**O tablodaki ders:** €18 CAC'le Google olağanüstü, baz-senaryo performansında Meta yıkıcı ve **ikisini harmanlamak teşhisi gizliyor.** 1,27x harmanlanmış ROAS "neredeyse başardık" gibi görünüyor, gerçekte "bir kanal mükemmel, diğeri sermaye yakıyor." **Prospecting Meta CAC'ini Google'dan ve retargeting'den ayrı, her hafta raporla — yoksa yanlış kanalı ölçekleyeceksin.**

---

# 25. EN ÖNEMLİ SORU

**"Kaan'ın sahip olduğu creative production + AI + DTC advertising deneyimi göz önüne alındığında, bu iş modelini normal bir e-ticaret girişiminden farklılaştıran gerçek avantaj nedir?"**

## 25.1 Yanlış cevap

Yanlış cevap — ve senin konumundaki insanların çoğunun kendilerine verdiği cevap — *"daha iyi reklamı daha ucuza yapabiliyorum, dolayısıyla CAC'im düşük olacak."* Bu doğru, yılda €33.000–70.000 kaçınılan maliyet ve ölçülmüş 1,8 kat ROAS çarpanı değerinde, **ve yeterli değil.** §9.2 aritmetiği gösteriyor: tam ölçülmüş creative-velocity çarpanını baz senaryoya uygula, ROAS 1,09x → 1,96x oluyor; başa baş 2,14x. Avantajın, belgelenmiş tam değeriyle ve geri kalan her şey ortalamayken devreye girdiğinde bile para kaybediyor.

Tüm avantajın "daha iyi reklam" ise, elinde baz senaryonun biraz daha az kötü bir versiyonu var.

## 25.2 Doğru cevap

Gerçek avantajın daha iyi reklam yapman değil. **Bu kategoride kimsenin göze alamayacağı hacimde ikna deneyi çalıştırabilmen — ve satın alma itirazının ekonomik değil bilgisel olduğu bir kategoride.**

Bunu dört adımda aç:

**Adım 1 — Bu kategorideki bloke edici itiraz fiyat değil, yetkinlik.**
İspanyol bir kadın €59'luk ipek fuları almıyorsa bunun nedeni €59'un çok fazla olması değil. Online moda sepeti zaten €70'in hemen altında. Almıyor çünkü *nasıl takacağını bilmiyor ve çekmecede kalacağını düşünüyor.* Bu bir **bilgi problemi** ve bilgi problemleri gösterimle çözülüyor.

**Adım 2 — Gösterim senden başka herkes için pahalı.**
Bunu çözmek çok sayıda styling gösterimi üretmeyi gerektiriyor: farklı düğümler, vücut tipleri, kombinler, yaşlar, mekânlar, sezonlar, vesileler. Düzgün kapsamak için 100+ video asset. Avrupa pazar oranlarında asset başına €150–450 ile bir rakibin o kütüphaneyi kurması **€15.000–45.000** artı 3–6 ay prodüksiyon planlaması demek. Sen bunu iki haftada, araç maliyetine kuruyorsun. **§11'deki rakip listesine bak: Fransız ve İspanyol premium şal markaları flat-lay fotoğraf ve mood filmle satıyor. Hiçbiri sistematik bir styling-eğitim motoru çalıştırmıyor.** Açık orada.

**Adım 3 — Gösterim asset'i CVR'yi yükseltiyor, ki modeldeki en değerli kaldıraç o.**
§6.2'ye göre conversion rate CAC'i kabaca *yarıya indiriyor* — fiyattan, COGS'tan ve CTR'den büyük bir etki. Creative avantajının çoğu CTR'ye harcanıyor, ki o doğrusal. Senin avantajın **CVR'ye** harcanabilir, çünkü bir styling videosu sadece reklam değil ürün sayfası asset'i. CVR'yi %1,8'den %2,6'ya taşı ve baz senaryo aynı CPM ve aynı CTR'de −€2.445'ten kâra geçiyor.

**Adım 4 — Ve kategorinin yapısı kazancı korumana izin veriyor.**
Şalın **bedeni yok**, dolayısıyla giyim DTC'sini yıkan iadeler (%20–40, ~%50'sinin nedeni beden) geçerli değil. Katkın net gelirin %64–69'unda hayatta kalıyor. Giyimde bir CVR kazancı doğrudan iade masasında geri veriliyor. Burada elinde kalıyor.

## 25.3 Tek cümlede

> **Moda aksesuarında satışı bloke eden itiraz "nasıl takacağımı bilmiyorum." Bunu çözmek, kategorinin karşılayamayacağı hacimde direct-response video gerektiriyor. Ben o hacmi pazar maliyetinin ~%4'üne üretebiliyorum, bu sadece tıklama oranını değil dönüşüm oranını yükseltiyor, ve aksesuarın bedeni olmadığı için iadeler kazancı geri almıyor.**

Bu gerçek, savunulabilir ve — önemli olarak — **test edilebilir** bir tez. Ayrıca 30 günde ~€2.300'e yanlışlanabilir, ki §22 tam bunun için tasarlandı.

## 25.4 Gerçekte kurduğun sistem

Hedefi tekrarlanabilir bir sistem olarak tanımladın: *Türkiye'den yüksek brüt marjlı ürün → Avrupa'da premium marka → AI destekli creative → Meta → Q4 talebi → bundle/upsell → tekrar eden müşteri.* İşte o sistem, zayıf halkaları adlandırılmış ve bileşik kısımları işaretlenmiş hâliyle.

| Aşama | Bileşik mi? | Güç | Gerçek risk |
|---|---|---|---|
| Yüksek brüt marjla Türk tedariki | **Hayır — eriyor.** Türk maliyetleri politika gereği euro bazında artıyor (asgari ücret +%249 2022–24, reel lira değerlenmesi) | **10 adet MOQ** gerçek varlık, fiyat değil. Ürün kararlarını ucuz creative testlerine çeviriyor | Sadece €5 landed'de çalışan bir model kurmak. €12 modelle |
| Avrupa premium markası | **Evet — en güçlü bileşik varlık** | Marka değeri, yorumlar, e-posta listesi ve basın, burada sen uyurken değeri artan tek şeyler | Kurması yavaş; birinci yılda bir indirim döngüsü kalıcı hasar veriyor |
| AI destekli creative üretimi | **Evet, ama değeri azalıyor** | Bugünkü gerçek avantajın. Yılda €33–70 bin maliyet avantajı artı 1,8 kat ROAS çarpanı | **Buradaki her şeyden hızlı değer kaybediyor.** AI creative araçları aydan aya emtialaşıyor. 24 ayda üretim-maliyeti avantajının çoğu gitmiş olur. **O zaman avantajın muhakeme — hangi açının çalıştığını bilmek — ki AI bunu kimseye vermiyor** |
| Birincil acquisition olarak Meta | **Hayır — şişiyor.** CPM'ler sadece 2025'te %20 arttı | Tam senin yeteneğini ödüllendiren, yüksek hacimli, hızlı öğrenen kanal | Kiralık arazi. Asla varlık değil |
| Q4 talep konsantrasyonu | **Yapısal, her yıl tekrarlanıyor** | Gerçekten mükemmel: İspanya'da kişi başı €796, hediye alımlarının %43'ü moda ve **Reyes sezonu 5 Ocak'a uzatıyor** | Konsantrasyon riski. Kötü bir Q4 kötü bir yıl |
| Bundle / upsell | **Evet, bir kez kurulduğunda** | **Plandaki en yüksek ROI'li iş.** €3'lük hediye kutusu CAC tavanını €27'den €43'e taşıyor | Eğlenceli olmadığı için sıkça eksik kuruluyor. Harcamayı ölçeklemeden önce kur |
| Tekrar eden müşteri | **Evet — ama sınırlı** | E-posta + düğüm kartı + baskı drop'ları | §7.6'ya göre %35 tekrar oranı bile CAC tavanını €28→€38 taşıyor. **LTV'yi aşırı modellemeyin.** Düşük frekanslı kategori |

**O sistemde gerçekten bileşik olan üç şey: marka değeri, sahip olunan e-posta listesi ve neyin ikna ettiğine dair muhakemen.** Tedarik avantajı eriyor, AI maliyet avantajı değer kaybediyor ve Meta kanalı şişiyor. Dolayısıyla bunu yaparsan, harcanan her euro medyanın aynı zamanda bir abone, bir yorum ya da sana özel bir creative öğrenmesi satın alacağı şekilde kur — çünkü 2029'da hâlâ sahip olduğun kısım o.

## 25.5 Bunu hiç yapmamaya dair stratejik itirazım

Bunu bir kez, açıkça söyleyeceğim; çünkü senin beyan ettiğin hedef bileşik kaldıraç, önündeki görevi bitirmek değil.

Şu anda zamanının üzerinde iki talep var: EY Digital — ortaklık yüzdesinin gündeme geldiği yer — ve build-to-exit bir ABD DTC markası. Bu şal girişimi **üçüncü** bir şey; **üçüncü** bir pazarda (ABD değil İspanya/Fransa), senin için **yeni bir kategoride**, **tek gelirli** bir hanede, ve yaklaşık 12 ay ötede olan bir 2026 Q4 penceresine nişan alıyor.

Dürüst gözlem: **bu raporda değerli olan hemen her şey mevcut ABD DTC markana transfer edilebilir.** Creative-velocity avantajı, CVR'nin CTR'den önemli olduğu içgörüsü, hediye-seti AOV mimarisi, styling-gösterim tezi — hiçbiri şala özgü değil. ABD markan bloke edici itirazın bilgisel olduğu *herhangi* bir kategorideyse, aynı avantaj daha yüksek AOV'de, İngilizce, daha iyi CPM-AOV oranı olan bir pazarda ve EPR/Triman/etiketleme yığını olmadan geçerli.

Ve ölçek tavanı önemli: §24'ün en iyi senaryosu **€50.000 harcamada ~€8.400 net katkı.** Bu gerçek bir iş ve alternatif aynı içgörüyü zaten sahip olduğun bir varlığa uygulamaksa, elindeki tek kıt kaynağın kötü bir kullanımı.

**Yani testten önce sorulmaya değer soru:** burası creative-velocity avantajını konuşlandıracağın en yüksek kaldıraçlı yer mi, yoksa en *ilginç* yer mi? Cevap, şal girişiminin hem EY'den hem ABD markasından farklı risk profiliyle Avrupa ayak izli bir şeye sahip olma yolu olmasıysa — bu meşru bir cevap ve €5.000'lik test bilgiyi satın almanın ucuz yolu. Cevap iyi bir arbitraj gibi görünmesiyse, arbitraj tezin en zayıf kısmı.

Görevi yapmadan önce yanlış hamle olduğunu düşünüyorsam söylememi istedin. İtirazım bu. Aşağıdaki öneriyi değiştirmiyor, çünkü €5.000'lik barajlı bir test ucuz ve bilgi gerçek — ama barajı geçerse ona ne kadar dikkat ayıracağını değiştirmeli.

---

# 26. NİHAİ KARAR ÇERÇEVESİ

| Soru | Kanıt | Sonuç |
|---|---|---|
| **Talep var mı?** | İspanya: 27,4M online alışverişçi (16–74'ün %77'si); giyim = 2025 Q4 e-tic. cirosunun %7'si; kadınlar online moda alıcılarının %56,5'i; kadın online moda sepeti €70'in hemen altı. Fransa: online giyim €7,7 milyar, tüm giyim tüketiminin %30,7'si. İpek fular SS26'nın üst aksesuar trendi, Eki ve Ara arama zirveleri | **Evet.** Talep risk değil. Hedef fiyatın normal İspanyol kadın moda davranışının içinde |
| **Premium satabilir miyiz?** | Doğrulanmış bağımsız-premium bandı: **Hamzah €35–69 (ES)**, **Fio de Martié 90×90 €94,90 (ES, İspanya'da el yapımı)**, Philéone €42–95 / tipik €68 (FR, Fransa'da üretim), Le Châle Bleu €39–169. Hermès €580 tavanı. **Ama Massimo Dutti %100 ipeği €29,95'e satıyor** | **Evet, €49–79'da. Üstünde değil.** Ve malzeme iddiası üzerinden değil — **premium, sana özel baskı + sunum + styling rehberliği üzerine oturmak zorunda.** €94,90'lık İspanyol emsal tavanın yeterince yüksek olduğunu kanıtlıyor; €29,95'lik Massimo Dutti farklılaşmanın opsiyonel olmadığını kanıtlıyor |
| **Meta Ads çalışır mı?** | Pazar ortalaması (€13 CPM, %1,5 CTR, %1,8 CVR) → €54,71 CAC, €27,96 tavana karşı. Başa baş **link CTR × CVR ≥ %0,053** gerektiriyor (€59,90 AOV). Ayda 15+ konsept creative velocity'si ölçülmüş 1,8 kat ROAS değerinde | **Sadece benchmark üstünde.** Ortalama uygulama cironun euro'sunda ~45–50 sent kaybediyor **ve ölçekle kötüleşiyor.** Girişimin merkezî riski bu |
| **Google çalışır mı?** | Avrupa e-tic. Shopping CPC'si **€0,29–0,35** (smec, €450M harcama paneli) → %3 CVR'de ~€12–18 CAC. Ama İspanyolca şal terimleri için **hiçbir keyword hacmi alınamadı** | **Evet, ve en iyi ekonomili kanal — ama hacim sınırlı.** İspanya'da muhtemelen €1.500–5.000/ay. Kâr kanalı, büyüme kanalı değil. **Bütçe ayırmadan önce hacimleri çek** |
| **>€50 AOV başarılabilir mi?** | Tek €59,90 → katkı €31,56. Hediye seti €89,90 → €49,00 (CAC tavanı €42,72). Premium koleksiyon €139,90 → €79,97 (tavan €70,33). Klarna AOV +%23 bildiriyor | **Evet, ve zorunlu.** Varsayılan seçili hediye seti artı post-purchase upsell Q4'te €72–82 harmanlanmış getirmeli. **Tek-SKU launch seni €27 CAC tavanında kilitliyor ve muhtemelen sadece bu yüzden testi kaybedersin** |
| **Marjlar paid acquisition'ı taşır mı?** | Net gelirde %64–69 katkı. Maks CAC €27,18 (tek) – €70,33 (koleksiyon). €10 COGS ve %20 iadede bile dayanıklı (€21,16 tavan) | **Evet — maliyet yapısı problem değil.** Tedarik ve iade şoklarına dayanıklı, sadece CAC'e kırılgan. **Tüm risk tek bir satırda yaşıyor** |
| **Q4 çekici mi?** | İspanya: kişi başı €796 bayram harcaması, €370 hediye, hediye alımlarının %43'ü moda, 10'da 8 BF'yi hediye için kullanıyor, erken alıcı +€140. **Reyes €192 > Noel arifesi €178.** Şal araması Eki ve Ara zirveleri. Karşı ağırlık: Kasım CPM'leri +%41, BFCM zirve günleri 2–3 kat | **Evet — girişimin en güçlü yapısal argümanı.** Ama müşteriyi **Eylül–Ekim'de** almak zorundasın, BFCM haftasında değil |
| **İspanya çekici mi?** | Daha ucuz açık artırma (İspanya CPM ~€6 tüm sektör, Kademe-1 $10–23'e karşı), hedef fiyatını kuşatan kadın moda sepeti, ince premium-şal DTC rekabeti, **henüz bağlayıcı olmayan tekstil EPR**, 24 saat yurt içi teslimat, Reyes uzatması ve orada yaşıyorsun | **Evet — tartışmasız birinci pazar** |
| **Fransa çekici mi?** | Daha büyük giyim e-ticareti (€7,7 milyar resmî) ve daha yüksek Google potansiyeli. Ama: sepet **€62 ve %3 düşüyor**, moda sepeti −%4,2, Vinted %21,4, Shein/Temu online giyimin %16'sını €9 ortalamayla, bir düzine DTC şal rakibi (Philéone €68 made-in-France dahil) ve **sert satış öncesi uyum kapısı** (Refashion UIN + 10 Tem 2026'dan beri vekâletli Fransız temsilci + Triman görseli) | **Evet, sonra, ve farklı SKU'yla.** 2027 Q2, İspanya kârıyla finanse, hero SKU daha küçük formatta €34,90–44,90 — çünkü Fransızlar **9 yılın en düşük bütçesinde rekor 9 hediye** alıyor: daha fazla hediye, daha düşük birim değer |
| **Türk tedariki avantajlı mı?** | **Lehine:** fabrika-direkt €1,90/adetten, **renk başına 10 adet MOQ**, dokuma etiket, özel nakış, markalı ambalaj, 5–8 gün transit, Bursa ipek mirası. **Aleyhine:** asgari ücret +%249 (2022–24), enerji ikiye katlandı, finansman %50'ye, 7 milyar $ üretim kaybı, 210.000 iş, düşen ihracat, reel lira değerlenmesi ve AB'nin Türkiye'den toplam HS6214 ithalatı 2025'te yalnızca ~8,4 milyon $ | **Evet — ama esneklik için, fiyat için değil.** 10 adet MOQ birim maliyetten değerli. **€12 landed üzerinden modelle, EUR üzerinden sözleşme yap, 12 ay kilitle.** "Ucuz Türkiye" varsayımı güncelliğini yitirmiş |
| **Creative avantajım önemli mi?** | Yılda €33–70 bin kaçınılan üretim maliyeti; ayda 15+ konseptte ölçülmüş **1,8 kat medyan ROAS**; Andromeda yapısal olarak semantik çeşitliliği ödüllendiriyor (>%60 benzer reklamlar tek Entity ID'ye birleşiyor); haftalar değil saatler süren iterasyon; ve VSL yeteneği kategorinin gerçek itirazına oturuyor | **Evet, belirgin şekilde — ve tek başına yeterli değil.** Tam creative çarpanı baz senaryoyu 1,09x → 1,96x taşıyor, 2,14x başa başa karşı. **Creative avantajı + €65 AOV + %2,5 CVR gerekiyor. Üçten ikisi para kaybediyor** |
| **En büyük risk** | Ortalama creative ve ortalama dönüşüm, **garantili** ve ölçekle kötüleşen bir zarar üretiyor — ince kâr değil. İkincil: **1 Temmuz 2026**'da €150 muafiyetinin kaldırılması ve adet başına sabit €3, ki Gümrük Birliği kapsamındaki Türk menşeli mallarla etkileşimi kamusal rehberlikte **çözülmemiş** | **Gün 30 kill kapısıyla azalt (€5.000 değil €2.300'e kaybet) ve İspanya'da stok tut.** Birinci haftada yazılı gümrük müşaviri görüşü al |
| **En büyük fırsat** | Kategori genelinde styling-yetkinlik itirazını video ile çözmedeki başarısızlık; **bedensiz** bir kategoride (iadeler kazancı yemiyor); belgelenmiş bir şal trendi sırasında; **Reyes'in Q4'ü üç hafta uzattığı** ve neredeyse hiç rakibin o pencereyi çalışmadığı bir pazarda | **Tez bu. Medyaya gerçek para harcamadan önce 12-yol motorunu kur** |

## İŞ MODELİ

| Alan | Cevap |
|---|---|
| **Ürün** | 90 cm baskılı ipek-dokulu kare, elle kıvrılmış kenar, sana özel baskı, 2–3 renk. İkinci SKU: €24,90'lık ince twilly |
| **Hedef müşteri** | İspanyol kadınlar 32–55, kentli, €40 bin+ hane, moda ilgili; Eyl–Kas kendine, Kas–Oca hediye olarak alıyor. Artı Q4'te 35–55 erkek hediye alıcıları (Google öncülüklü) |
| **Ülke** | **Sadece İspanya.** Fransa 2027 Q2 |
| **Perakende fiyatı** | **€59,90** hero |
| **Hedef AOV** | **€72–82** harmanlanmış (Q4) |
| **Hedef brüt marj** | **Net gelirin %64–69'u** (tekten koleksiyona) |
| **Hedef CAC** | **< €28** harmanlanmış; prospecting Meta'da **< €24** |
| **Hedef katkı marjı** | **Sipariş başına €28–43**, ilk siparişte pozitif |
| **Birincil acquisition** | Meta (Reels/Stories, styling-gösterim creative'i, ayda 15–20 yeni konsept) |
| **İkincil acquisition** | Google — marka savunması + **hediye niyeti Search** + Standart Shopping. Sonra TikTok Shop İspanya (Ara 2024'ten beri canlı; cironun %69,9'u creator odaklı, ki sana uyuyor) |
| **Ana upsell** | **€19,90 fular ringi** (~%88 marj, 8–15 g) ve €44,90'a post-purchase ikinci baskı |
| **Ana bundle** | **Hediye seti — fular + ring + sert kutu — €89,90, ürün sayfasında varsayılan seçili** |
| **Q4 offer'ı** | **Yüzde indirim yok.** Bundle fiyatlaması + ücretsiz sert hediye kutusu + VIP erken erişim + ücretsiz kargo + iadelerin 15 Ocak'a uzatılması + 200 adetlik numaralı limited baskı |

## PAZARA GİRİŞ (GO-TO-MARKET)

| Alan | Cevap |
|---|---|
| **İlk ülke** | İspanya (Canarias, Ceuta, Melilla hariç) |
| **İlk ürün** | Tek sana özel baskı, 90 cm kare, 3 renk — biri klasik (binicilik/barok), biri sezonluk (jade veya derin mavi), biri nötr |
| **İlk fiyat** | Tek €59,90 / ringli €74,90 / **hediye seti €89,90 (varsayılan)** / ikili €99,90 / koleksiyon €149,90 |
| **İlk reklam bütçesi** | **€2.000 Meta + €300 Google**, 30 gün, €5.000 toplam tavan içinde |
| **İlk 10 creative** | (1) Tek fular beş kombin · (2) Kombin fenaydı sonra bu · (3) Annenin öğretmediği üç düğüm · (6) Öncesi/sonrası kıyafet değişmedi · (13) Kenar başına sekiz dakika · (15) Founder hikâyesi · (20) İade etmeyeceği hediye · (21) Unboxing anlatım yok · (24) Üç hediye tek sipariş · (31) Baskı başına 200 |
| **İlk 3 kitle** | (1) Broad / Advantage+, kadın 25–60, İspanya adalar hariç — birincil. (2) Interest stack: premium moda + hediye + Massimo Dutti/COS/Zara-komşusu ilgiler — kontrol. (3) Retargeting: video izleyici %50+, ATC, 30 gün site ziyaretçisi |
| **İlk landing page** | Ürün sayfası, ana sayfa değil. **Fold üstünde styling videosu**, €89,90 önceden seçili üç kademeli seçici, ürün sayfasında görünür kargo maliyeti, fotoğraflı yorum duvarı, lif/bakım/menşe akordeonları, Bizum + kart + PayPal, mobil öncelikli |
| **İlk offer** | "Tek fular. Beş şekil. €69 üzeri ücretsiz kargo. Hediye kutusunda gelir." |

## NİHAİ ÖNERİ

# ➤ ÖNCE TEST ET (TEST FIRST)

GO değil, NO-GO değil. Gerekçesi tam olarak şu.

**Neden GO değil.** GO kararı baz senaryonun kârlı olmasını gerektirirdi. Değil. Pazar ortalaması Meta performansında bu iş cironun her euro'sunda kabaca 45–50 sent kaybediyor **ve zarar ölçekle genişliyor** — €5.000 harcamada €2.445, €50.000'de €31.913. Bu, ortalama uygulamanın ince kâr getirdiği e-ticaretin çoğundan belirgin biçimde farklı bir risk profili. Creative avantajın gerçek ve ölçülmüş (ayda 15+ konseptte 1,8 kat ROAS, yılda €33–70 bin kaçınılan maliyet) ve bunu baz senaryoya tam olarak uygulamak 1,96x'te, 2,14x başa başın altında bırakıyor. **Girişim, üç değişkende — creative, dönüşüm oranı ve AOV — aynı anda benchmark üstü performansı, iyi performansın yolu olarak değil girmenin bedeli olarak talep ediyor.** Bunu test etmeden sermaye bağlamak sorumlu olmaz.

**Neden NO-GO değil.** Acquisition verimliliği dışındaki her girdi lehte, birkaçı belirgin biçimde. Maliyet yapısı dayanıklı — net gelirde %64–69 katkı, €10 COGS ve %20 iade kötümser köşesinde bile hâlâ €21 CAC payı. İadeler yapısal olarak düşük çünkü şalın bedeni yok, ki giyim DTC'sinin çoğunu öldüren başarısızlık modu o. Hedef fiyatın belgelenmiş İspanyol kadın moda davranışının içinde (€70 altı sepete karşı €59,90) ve doğrulanmış bağımsız-premium bandının içinde (Hamzah €35–69, Fio de Martié €94,90'a kadar, Philéone €68). Kategori Eki ve Ara arama zirveleriyle belgelenmiş bir moda trendinde. İspanya'da Q4 olağanüstü ve Reyes sayesinde herkesinkinden üç hafta uzun. Tedarik esnekliği olağanüstü — kendi dokuma etiketinle renk başına 10 adet. Google ekonomisi mükemmel. Ve sömüreceğin spesifik açık — kategoride kimse sistematik bir styling-gösterim motoru çalıştırmıyor — rakip listesinde görünür ve tam olarak dokuz yıllık işinin senin için ucuz kıldığı şey. **Bu tez üzerine €5.000'lik barajlı bir test, bilgiyi satın almanın rasyonel yolu.**

**ÖNCE TEST ET somut olarak ne demek:** €5.000 sert tavan, sadece İspanya, tek ürün ailesi, varsayılan seçili hediye setli tek fiyat merdiveni, baraja 30 gün ve **gün 30'da önceden taahhüt edilmiş kill kararı**:

| Gün 30 sonucu | Aksiyon |
|---|---|
| **link CTR × CVR ≥ %0,053, AOV ≥ €65, CAC < €30** | **Q4'ü finanse et.** 600–1.000 adet sipariş et, §23 gün 31–90'ı uygula, €25–30 bin Q4 medyası planla |
| **Baraj %30'dan az kaçırıldı** (yani ≥ %0,037) | **Bir kez 30 günlük yeniden kurulum — offer'ın ve landing page'in, creative'in değil.** §6.2'ye göre CVR ve AOV daha büyük kaldıraçlar. Sonra bir kez daha barajla |
| **Baraj %30'dan fazla kaçırıldı** (< %0,037) | **Dur.** ~€2.300 harcamış, ~€2.700 korumuş ve ABD markana transfer edilebilir bir şey öğrenmiş olacaksın. Yanlış bir hipotez için iyi bir sonuç |

**Testin sonucunun yorumlanabilir olması için üç koşul:**

1. **AOV mimarisini birinci günde launch et.** Tek-SKU launch CAC tavanını €27,18'de kilitler ve muhtemelen tezle hiç ilgisi olmayan nedenlerle barajı kaçırır. Hediye seti ilk siparişten itibaren canlı ve varsayılan seçili olmak zorunda.
2. **Birinci haftada gümrük müşaviri görüşünü al.** Spesifik olarak: **1 Temmuz 2026** sabit €3/adet ücreti, AB–Türkiye Gümrük Birliği kapsamındaki Türk menşeli düşük değerli B2C sevkiyatlara uygulanıyor mu? Kamusal rehberlik bunu çözmüyor. Uygulanıyorsa direkt gönderim ölü — ki plan bu yüzden her hâlükârda İspanya'da depoluyor.
3. **`link CTR × session CVR`'yi tek sayı olarak günlük izle.** ROAS'ı değil. ROAS, Google'ı (mükemmel) prospecting Meta'yla (gerçek soru) harmanlıyor ve sana rahatlatıcı bir yalan söyleyecek. §24'ün harmanlanmış tablosu tam nasıl olduğunu gösteriyor — 0,88x Meta ile 3,27x Google'ı gizleyen 1,27x'lik bir rakam.

---

# ★ CANLI FİYAT DOĞRULAMA LİSTESİ (senin 15 dakikan)

Bu ortamdan tek bir rakip sitesi açılamadı. Aşağıdaki 12 satırı kendin doldurduğunda §11 tamamlanmış olur. **Sırayla önemlilik derecesine göre dizildi — ilk üçü karar-ilgili, gerisi teyit.**

| # | Marka / URL | Ne arayacaksın | Şu anki kaydım | Önemi |
|---|---|---|---|---|
| **1** | **massimodutti.com/es** → Mujer › Accesorios › Fulares | %100 ipek fuların **gerçek fiyatı ve ölçüsü**. İndirimli mi tam fiyat mı? En pahalı ipek kaç? | %100 ipek baskılı €29,95; keten €39,95 | **★★★ En kritik kalem.** €29,95 tam fiyat ve 90×90 ise farklılaşma yükün maksimum. Küçük bir ölçü veya indirimse rahatladın |
| **2** | **fiodemartie.com** → Pañuelos de seda | 90×90 ve 70×70 **tam fiyat listesi**; indirim sıklığı; hangi ölçüler var | 33×33 €16,90; bandana €48,90'dan; 70×70 ve 90×90 €94,90; indirimliler €29,90–74,90 | **★★★ Premium tavan kanıtın.** €94,90 teyit edilirse €59,90 çok güvenli konumda |
| **3** | **phileone.fr/collections/femmes-foulards** | Tüm fular fiyat aralığı; hangi ölçü €68 | Fularlar €42–95; Emmanuelle/Sylvia €68; Alma €98 | **★★★ Fransa'nın referans fiyatı.** Fransa planını bu belirliyor |
| 4 | **hamzah.es** → Pañuelos de seda | Ölçü başına fiyat; hangi ölçü €47 ve €69 | €35–49, büyük €47, Noisette €69 | ★★ İspanyol alt bandı |
| 5 | **arket.com** (EUR mağazası) → Scarves | Kaşmir ve baskılı ipeğin **EUR** fiyatı | Kaşmir ~£85 (≈€98); baskılı ipek ~£45 (≈€52). **İlk raporda "€39 kaşmir" yazmıştım, çelişkili** | ★★ Çelişkiyi çöz. €39 doğruysa kaşmirden kesin uzak dur |
| 6 | **stories.com** (EUR) → Scarves | Kaşmir ve ipek fular EUR fiyatı | Doğrulanmadı; önceki turda ES kaynakta "kaşmir €49" | ★★ Aynı çelişki |
| 7 | **elcorteingles.es** → Pañuelos y fulares › Seda | Fiyat filtresini kullan: €0–40 / 40–70 / 70–100 / 100+ bantlarında kaç ürün var | Marka listesi alındı; sadece bir örnek fiyat (€64,90→€34,90) | ★★ İspanyol premium bandının **dağılımını** verir — tek fiyattan değerli |
| 8 | **julunggul.com** → Fulares de seda | Fiyat aralığı | Doğrulanmadı | ★ İspanyol zanaatkâr bandı |
| 9 | **foularchic.com** → Foulard en soie femme | 70×70 ipek fiyatı; kategori-uzmanı konumlandırması nasıl fiyatlanıyor | Doğrulanmadı; ürün 70×70 | ★ Fransa'daki "senin kurduğun şey"in fiyatı |
| 10 | **sezane.com/es** veya **/fr** → Foulards | EUR fiyatları; Cleopatra 52×52'nin fiyatı | Doğrulanmadı; resale $85–155 | ★ Mass-premium referansı |
| 11 | **lechalebleu.fr/shop** | Tam aralık; €39 ve €169 hangi ürünler | €39–169 (agregatör) | ★ Bölünmüş-menşe emsalini teyit |
| 12 | **etsy.com** → "turkish silk scarf" (en çok satana göre sırala) | İlk 20 listenin fiyatı, **ve yorumlardaki itirazlar** | €20–113 | ★★ Fiyat için değil — **yorumlar müşterinin neyi önemsediğini bedava söylüyor.** Fiyatlardan bunu daha çok oku |

**Nasıl kaydedeceksin:** her satır için fiyat, ölçü, malzeme, tam fiyat mı indirim mi, ve tarih. Bu tablo dolduğunda §6'nın fiyat merdivenini ve §11'i bir kez daha gözden geçir — ama **§7'nin birim ekonomisi değişmeyecek**, çünkü o senin maliyet yapına bağlı, rakiplerin fiyatına değil.

---

# ★ BEN SENİN YERİNDE OLSAM: İLK 14 GÜN

Maliyetler €5.000'in içinden. Günler, EY'nin yanında hafta içi ~3–4 odaklı saat varsayıyor.

| Gün | Aksiyon | Maliyet | Çıktı |
|---|---|---|---|
| **1** | **Ucuz-Türkiye varsayımını düzgün öldür.** 5 tedarikçiye (Hicabistan, Woolgold, Alıcıoğlu + Europages'ten 2) tek bir spec'le yaz: 90×90 cm baskılı kare, elle kıvrılmış kenar, benim görselim, dokuma etiket, EUR fiyatlama, 12 aylık fiyat kilidi, renk başına 10 MOQ. 150 / 500 / 1.000 adette Madrid'e landed maliyet iste | €0 | EUR cinsinden 5 teklif. **Hiçbiri EUR'da 12 ay fiyat tutmuyorsa, bu bir bulgudur** |
| **2** | **Gümrük + uyum, yazılı.** İspanyol gümrük müşaviri tut. İki soru: (a) 1 Temmuz 2026 sabit €3/adet ücreti vs Gümrük Birliği kapsamında Türk menşei; (b) toplu A.TR ithalatı için belgeler. Ayrıca GPSR Sorumlu Kişi durumunu teyit et | €200 | Modeli geçersiz kılabilecek tek soruya yazılı cevap |
| **3** | **★ Rakip teardown — canlı siteler.** Yukarıdaki doğrulama listesinin 12 satırını bitir. Her marka için: tam fiyat, ölçüler, malzemeler, kargo maliyeti ve eşiği, iade politikası, ödeme yöntemleri, ürün sayfası yapısı, **styling videosu kullanıyorlar mı**. Sonra en çok satan 20 Etsy Türk-ipek listesini oku ve **yorumlardaki itirazları not et** | €0 | Gerçek fiyat merdiveni ve doğrulanmış itiraz listesi — benim arama-kaynaklı tahminlerimin yerini alıyor |
| **4** | **Google keyword hacimlerini çek.** Google Ads hesabı aç. §17.2'deki tüm kümeler için Keyword Planner, İspanya, exact match. Markalı olmayan ticari hacmi topla | €0 | **Google'ın €1.500/ay mı €5.000/ay mı kanal olduğu kararı** |
| **5** | **Baskıları tasarla.** 3 baskı yönü: biri binicilik/barok klasik, biri belgelenmiş 2026 paletinde botanik (jade/derin mavi/yoğun kırmızı), biri geometrik-Akdeniz. AI görsel hattını kullan. Baskıya hazır repeat dosyaları üret | €0 | 3 görsel dosya — tek gerçek hendeğin (bir baskı fiyat-karşılaştırılamaz) |
| **6** | **İsim, alan adı, marka kontrolü.** Uydurma Latince, 2–3 hece, sesli harfle biten. EUIPO'da Nice sınıf 24 ve 25 araması. Alan adını ve hesapları al | €50 | Marka var oldu |
| **7** | **Numune sipariş et.** En iyi 2 tedarikçi × 3 baskı × 2 renk ≈ 60–120 adet. Ekspres öde. Dokuma etiket ve İspanyolca lif etiketi şart koş | €600 | Ürün yolda — ve kalite cevabı |
| **8** | **Mağaza iskeletini kur.** Shopify, temiz tema, §21.2'ye göre yapılandırılmış ürün sayfası, **€89,90 önceden seçili** üç kademeli seçici, ürün sayfasında kargo maliyeti, Bizum + kart + PayPal, reddetmek-kabul-kadar-kolay CMP. Yorum ve post-purchase upsell uygulamalarını kur | €200 | Para alabilen bir mağaza |
| **9** | **Hukuki metinleri bir kez, düzgün yaz.** Cayma hakkı (14 gün, standart teslimat dahil 14 günde iade), **iade kargosunu kimin ödediği satın alma öncesinde belirtilmiş**, gizlilik, çerezler, şartlar, tam tacir kimliği ve adresi. İspanyolca, insan eliyle | €0 | Yokluğu cayma yükümlülüğünü 12 aya uzatan şey |
| **10** | **12 yolun senaryosunu yaz.** 12 düğüm, her biri 15–25 sn dikey: hook, tepeden sadece eller, numaralı altyazı, vücutta sonuç. 12 senaryoyu ve shot list'i bugün yaz | €0 | Aynı anda SEO sayfası, 12 Reels, ürün sayfası videosu, 12 e-postalık akış ve düğüm kartı olan asset |
| **11** | **§13'ten 15 launch creative'i kur** — AI + mevcut footage ve stillerinle. Gerçekten farklı konseptler, varyant değil (Andromeda >%60 benzer reklamları tek Entity ID'ye birleştiriyor) | €100 | Gün 30 barajının üzerinden yargılanacağı 15 asset |
| **12** | **Ölçümü kur.** Meta pixel + CAPI, GA4 ve tek satırlık günlük tablo: harcama, gösterim, link tıklaması, oturum, ATC, sipariş, ciro, **ve hesaplanmış tek hücre olarak `link CTR × CVR`.** %0,053 barajını koşullu biçimlendirme kuralı olarak ekle | €0 | Cevabı yorumlamak zorunda kalmadan göreceksin |
| **13** | **Numuneler geldi → karar ver.** Kenar, baskı register'ı, görsele karşı renk, gramaj, tuşe, etiket tutunması denetle. Düzgün fotoğrafla. **Kazanan tedarikçiye 250–300 adetlik ilk siparişi ver.** Ring, sert kutu, düğüm kartı sipariş et | €900 | Stok umut değil kanıt üzerine bağlandı |
| **14** | **Launch.** 1 kampanya, 2 ad set, 15 creative, broad + Advantage+, kadın 25–60, İspanya adalar hariç, €80/gün. Google: marka savunması + hediye niyeti Search + Standart Shopping, €10/gün. Sonra **72 saat dokunma** | €90/gün başlıyor | Canlı. Gün 30 barajının saati başladı |

**Gün 14'e kadar bağlanan toplam: €5.000'in ~€2.050'si.** Launch çizgisine ~€2.950 pist ve önceden taahhüt edilmiş bir kill tarihiyle geliyorsun.

**İlk 14 günde bilinçli olarak yapmayacakların:** kimseyi işe almak; özel site yaptırmak; numuneler gelmeden profesyonel çekim yapmak; Fransa için herhangi bir şey kurmak; Refashion'a kayıt olmak; TikTok Shop açmak; indirim yapmak; ya da CTR okuması olmadan günlük bütçeyi €80'in üstüne çıkarmak. Bunların her biri, önemli olan tek soru cevaplanmadan önce ilerleme hissi satın almanın bir yolu.

---

## Kaynaklar

**Resmî ve sektör kuruluşu kaynakları**
- CNMC — İspanya e-ticaret çeyreklik verisi, 2025 Q4 ([basın notu PDF](https://www.cnmc.es/sites/default/files/editor_contenidos/Notas%20de%20prensa/2026/20260703_NP_CE_IV_2025%20(en).pdf)); [2025 toplamı, The Corner üzerinden](https://thecorner.eu/news-spain/e-commerce-in-spain-exceeds-e114-8-billion-in-2025-up-20-6-per-cent-on-previous-year/126596/)
- [IAB Spain — *Estudio Ecommerce 2025*](https://iabspain.es/estudio/estudio-ecommerce-2025-iab-spain/) (Elogia ile)
- INE — [*Encuesta de Presupuestos Familiares* 2025](https://www.ine.es/dyngs/Prensa/EPF2025.htm); [*Atlas de Distribución de Renta de los Hogares*](https://www.ine.es/dyngs/Prensa/ADRH2023.htm); [comunidad autónoma'ya göre renta media](https://www.ine.es/jaxiT3/Tabla.htm?t=68338)
- [Modaes — 2025 kişi başı moda harcaması](https://www.modaes.com/entorno/el-gasto-en-moda-por-persona-vuelve-a-caer-en-2025-tras-cuatro-anos-de-recuperacion)
- FEVAD — [*Chiffres Clés e-commerce 2025*](https://www.fevad.com/chiffres-cles-ecommerce-2025/); [2025 yıllık değerlendirme](https://www.fevad.com/bilan-du-e-commerce-en-france-les-francais-ont-depense-pres-de-200-milliards-deuros-sur-internet-en-2025/); [*Mode et Internet 2025*](https://www.fevad.com/mode-et-internet-en-2025-bilans-et-perspectives/); [ortalama sepet](https://www.fevad.com/chiffre-mois-75e/)
- [Républik Retail / Institut Français de la Mode — 2025 Fransız moda pazarı](https://www.republik-retail.fr/strategie-retail/enseignes/pratiques/le-marche-francais-de-la-mode-en-2025-chiffres-cles-et-tendances.html)
- [Cofidis — 2025 Fransız Noel bütçesi](https://www.cofidis.fr/fr/question-de-budget/projets-des-francais/budget-francais-noel-2025.html); [franceinfo](https://www.franceinfo.fr/decouverte/noel/noel-2025-le-budget-des-francais-au-plus-bas-depuis-2017-avec-491-euros-en-moyenne_7601780.html)
- [OCU Noel harcaması, Cuatro üzerinden](https://www.cuatro.com/noticias/economia/20251210/cuanto-gastan-espanoles-navidad-reyes-magos-ganan-papa-noel_18_017823601.html); [Oney Black Friday & Noel araştırması 2025](https://blog.oney.es/somos-oney/estudio-oney-blackfriday-navidad/); [Emprendedores](https://emprendedores.es/notas-de-prensa/el-black-friday-impulsa-el-gasto-navideno-los-espanoles-gastaran-casi-411e-de-media-en-regalos-segun-oney/); [Retail Actual](https://www.retailactual.com/noticias/20251211/compras-regalos-ultima-hora-navidad); [Ecommerce News ES](https://ecommerce-news.es/el-gasto-medio-online-sera-de-250e-esta-avidad/)
- [DataReportal — Digital 2025: Spain](https://datareportal.com/reports/digital-2025-spain); [NapoleonCat Instagram İspanya](https://stats.napoleoncat.com/instagram-users-in-spain/); [Statista — yaşa göre Instagram Fransa](https://www.statista.com/statistics/1196396/instagram-users-by-age-france/)

**Hukuk, vergi ve gümrük**
- [Avrupa Komisyonu — düşük değerli koliler için €3 gümrük vergisi](https://commission.europa.eu/news-and-media/news/ensuring-fairness-and-safety-eur3-customs-duty-low-value-parcels-2026-06-29_en); [AB Konseyi, 12 Ara 2025](https://www.consilium.europa.eu/en/press/press-releases/2025/12/12/customs-council-agrees-to-levy-customs-duty-on-small-parcels-as-of-1-july-2026/); [DG TAXUD rehberlik ve yasal metin, 8 Haz 2026](https://taxation-customs.ec.europa.eu/news/guidance-and-legal-text-temporary-flat-fee-low-value-imports-which-will-apply-until-1-july-2028-2026-06-08_en)
- [Access2Markets — AB–Türkiye Gümrük Birliği](https://trade.ec.europa.eu/access-to-markets/en/content/eus-custom-union-turkey); [DG TAXUD — Türkiye gümrük birlikleri](https://taxation-customs.ec.europa.eu/turkey-customs-unions-and-preferential-arrangements_en); [A.TR belgesi açıklaması](https://www.customssupport.com/atr-certificate-explained/)
- [Yönerge (AB) No 1007/2011 — tekstil lif adları ve etiketleme (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2011/1007/oj/eng); [Komisyon sayfası](https://single-market-economy.ec.europa.eu/sectors/textiles-ecosystem/regulation-eu-10072011_en)
- GPSR — [AB dışı satıcılar için AB Sorumlu Kişi gerekliliği](https://eumandate.com/insights/gpsr-eu-responsible-person); [genel bakış](https://euverify.com/resource/eu-responsible-person-under-gpsr/)
- [Refashion Pro — hukuki çerçeve](https://pro.refashion.fr/en/the-legal-framework); [Fransız tekstil EPR 2025 uyumu](https://deutsche-recycling.com/blog/compliance-solutions-for-selling-textiles-in-france/); [Triman & info-tri](https://www.traceforgood.com/ressources/article/french-new-compulsory-triman-label-and-textile-recycling-information); [Refashion yetkili temsilci](https://ekovio.com/epr-authorized-representative-textiles-france-refashion/)
- İspanya tekstil EPR — [Reconomy, TRIS bildirimi](https://www.reconomy.com/2026/07/06/spain-textile-epr-decree/); [Valpak, taslak kararname](https://www.valpak.co.uk/spain-textile-epr-draft-decree/); [Reverse Logistics Group](https://rev-log.com/spain-proposes-new-epr-rules-for-textiles/)
- [Cayma hakkı — Your Europe (Avrupa Komisyonu)](https://europa.eu/youreurope/citizens/consumers/shopping/returns/faq/index_en.htm); [Centro Europeo del Consumidor en España](https://portal-cec.consumo.gob.es/en/informacion-general/compras-online/devoluciones); [Stripe — İspanya'da iadeler](https://stripe.com/resources/more/purchase-returns-in-spain)
- [OSS / mesafeli satış eşikleri — Marosa](https://marosavat.com/vat-manual-chapters/e-commerce-european-vat-regulations); [Taxology](https://taxology.co/distance-selling-treshholds/); [IOSS açıklaması](https://crossbordertaxtool.com/en/guide/ioss-explained); [Avalara, €150 muafiyetinin sonu](https://www.avalara.com/blog/en/europe/2025/11/eu-end-150-customs-duty-exemption-2026.html)
- Avrupa Erişilebilirlik Yasası — [Bird & Bird online perakendeci rehberi](https://www.twobirds.com/en/insights/2025/a-guide-to-navigating-the-european-accessibility-act-for-online-retailers-service-providers-and-plat); [e-ticaret hizmet gereklilikleri](https://accessible.org/eaa-ecommerce-services-requirements/); [mikroişletme muafiyeti](https://www.xictron.com/en/blog/accessibility-act-exemptions-microenterprises-2026/)

**Reklam benchmark'ları**
- [Triple Whale — sektöre göre Facebook reklam benchmark'ları](https://www.triplewhale.com/blog/facebook-ads-benchmarks); [e-ticaret benchmark'ları](https://www.triplewhale.com/blog/ecommerce-benchmarks)
- [Facebook Ads benchmarks 2026 (influee derlemesi)](https://influee.co/gb/blog/facebook-ads-benchmarks); [e-ticaret için Meta ads benchmark'ları](https://27five.com/blog/meta-ads-benchmarks-ecommerce-2026/); [adlibrary.com Meta e-ticaret benchmark'ları](https://adlibrary.com/posts/meta-ad-benchmarks-ecommerce-2026)
- Ülkeye göre CPM — [Adamigo](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026); [Lebesgue](https://lebesgue.io/facebook-ads/facebook-cpm-by-country); [Adligator](https://adligator.com/blog/meta-ads-cpm-by-country-benchmarks); [Meta Ads İspanya playbook](https://adlibrary.com/posts/meta-ads-spain-playbook-2026)
- Q4 sezonluğu — [Benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns); [Scigrowth BFCM playbook](https://scigrowth.com/blogs/strategy-growth-1/meta-ads-black-friday-playbook-launch-timeline-budget-scaling); [Clouted CPM enflasyon istatistikleri](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics)
- Creative hacmi ve Andromeda — [MHI Growth Engine, haftada kaç creative](https://mhigrowthengine.com/blog/how-many-creatives-to-test-meta-ads/); [Adamigo creative test benchmark'ları 2025](https://www.adamigo.ai/blog/meta-ad-creative-testing-benchmarks-2025); [Atria Andromeda rehberi](https://www.tryatria.com/blog/andromeda-meta-ads); [Madwise, creative çeşitliliği](https://madwise-agency.com/blog/meta-ads-facebook-algorithms-andromeda/); [Wonderful — Andromeda creative stratejileri](https://www.usewonderful.com/blog/meta-andromeda-creative-strategies)
- Google — [smec Market Observer CPC benchmark'ları](https://smarter-ecommerce.com/en/smec-market-observer/metrics/cpc/); [2025 Q4 raporu](https://smarter-ecommerce.com/en/smec-market-observer/reports/Q4_2025/); [WordStream Google Ads benchmark'ları](https://www.wordstream.com/blog/2025-google-ads-benchmarks); [kategoriye göre Google Shopping benchmark'ları](https://foundrycro.com/blog/google-shopping-benchmarks-by-category-2026/)
- Dönüşüm ve iadeler — [Blend Commerce dönüşüm benchmark'ları](https://blendcommerce.com/blogs/shopify/ecommerce-conversion-rate-benchmarks-2026); [Enavi Shopify benchmark'ları](https://www.enavi.co/blogs/shopify-conversion-rate-benchmarks); [Richpanel iade oranları](https://www.richpanel.com/learn/ecommerce-return-rates); [Eightx AB iade benchmark'ı](https://eightx.co/blog/eu-ecommerce-return-rate-benchmark); [Prime AI, ülke ve kategoriye göre giyim iade oranları](https://www.prime-ai.com/en/media/clothing-return-rates-by-category-and-country-csf-a/)
- UGC ve prodüksiyon maliyetleri — [Superscale UGC fiyatlama](https://superscale.ai/learn/how-much-does-ugc-cost-real-pricing-breakdown-for-2025/); [Atlas Cloud UGC ajans maliyetleri](https://www.atlascloud.ai/blog/tips/ugc-video-agency); [ppc.io UGC oranları](https://ppc.io/blog/ugc-pricing); [Sovran video reklam prodüksiyon maliyeti](https://sovran.ai/benchmarks/video-ad-production-cost)

**Türkiye tedariki ve maliyet tablosu**
- [Hicabistan — fabrika-direkt toptan, İstanbul](https://hicabistan.com/); [Woolgold — şal & fular üreticisi, İstanbul](https://woolgold.com/shawl-scarf-manufacturer-in-istanbul/); [go4WorldBusiness — Türk fular tedarikçileri ve toptan fiyatlar](https://www.go4worldbusiness.com/suppliers/turkey/scarves.html); [Europages — şallar, Türkiye](https://www.europages.co.uk/companies/turkey/shawls.html)
- [WWD Sourcing Journal — Türkiye'de asgari ücret %27 arttı](https://wwd.com/sourcing-journal/industry-news/turkey-minimum-wage-surges-27-percent-1238860787/); [Yahoo Finance](https://finance.yahoo.com/news/turkey-rising-minimum-wage-puts-120000444.html); [Turkish Minute — tekstil sektörü zorlanıyor](https://www.turkishminute.com/2025/05/27/turkeys-textile-industry-struggles-amid-rising-costs-global-competition/); [Kohan Textile Journal — 7 milyar $ kayıp, 210.000 iş](https://kohantextiljournal.com/turkeys-textile-apparel-industry-faces-7b-loss-210000-job-cuts/); [PolyesterTime — derin kriz](https://www.polyestertime.com/turkey-textile-industry-in-deep-crisis/)
- [ING THINK — Türkiye'de dezenflasyon](https://think.ing.com/snaps/disinflation-continues-moving-below-of-the-central-banks-forecast-range/); [Naga — lira tahmini](https://naga.com/en/news-and-analysis/articles/turkish-lira-forecast-and-price-predictions); [Trading Economics — AB'nin Türkiye'den şal/fular ithalatı](https://tradingeconomics.com/european-union/imports/turkey/shawls-scarves-mufflers-mantillas-veils)

**Rakipler, ürün ve trend**
- [Petrusse](https://www.petrusse.com/collections/carres-de-soie) · [Philéone](https://phileone.fr/en/collections/femmes-foulards) · [Le Châle Bleu](https://lechalebleu.fr/shop) · [Fleuron Paris](https://us.fleuron.paris/collections/foulards-bandeaux-soie) · [SOI Paris](https://soi-paris.com/en/collections/les-foulards-en-soie) · [Soeur](https://www.soeur.fr/en/collections/foulards) · [Foularchic](https://foularchic.com/collections/foulard-en-soie-femme) · [Lollipops](https://lollipops.fr/collections/foulard) · [Balaboosté](https://www.balabooste.com/collections/foulards) · [monfoulardensoie.fr](https://monfoulardensoie.fr/75-foulards-en-soie-femme)
- [Fio de Martié](https://www.fiodemartie.com/en/categoria/for-her/panuelos-seda-special-design/) · [Hamzah](https://hamzah.es/en/silk-scarves/) · [Julunggul](https://julunggul.com/) · [Munira](https://munira.net/collections/scarves-and-shawls) · [El Corte Inglés — ipek fular](https://www.elcorteingles.es/moda-mujer/accesorios/panuelos-y-fulares/attr.fashion_material_principal::Seda/) · [Cortefiel](https://cortefiel.com/es/es/mujer/complementos/fulares) · [H&M İspanya](https://www2.hm.com/es_es/mujer/accessories/bufandas.html) · [Massimo Dutti — ipek fular](https://www.massimodutti.com/es/mujer/accesorios/fular-seda-estampado-cachemir-c1748116p7795070.html) · [& Other Stories](https://www.stories.com/en-us/accessories/scarves/) · [ARKET fularlar (endource)](https://www.endource.com/shop/arket-scarves)
- [Hermès fular fiyat karşılaştırması (Bagaholic)](https://lvbagaholic.com/blogs/lv_bagaholic/hermes-scarf-prices-comparison) · [Elizabetta — Fransız fular alternatifleri](https://elizabetta.net/blogs/the-elizabetta-fashion-accessories-journal/french-scarf-alternatives) · [Atelier Hoi An — en iyi ipek fular markaları](https://atelierhoian.com/en/best-silk-scarf-brands/)
- Trend — [Marie Claire UK — ipek fular 2026 ilkbaharın en akıllı styling hilesi](https://www.marieclaire.co.uk/fashion/shopping/silk-scarf-trend-2026); [WWD — küçük ipek fular trendi 2026](https://wwd.com/fashion-news/fashion-trends/silk-scarf-trend-1238940326/); [La Caressette — 2026 ipek fular trendleri](https://lacaressette.com/en/blogs/lart-du-nouage-et-du-stylisme/2026-silk-scarf-trends-colors-and-prints)
- Pazar boyutlandırma **[satıcı tahminleri]** — [Fortune Business Insights — şal & atkı pazarı](https://www.fortunebusinessinsights.com/scarves-shawls-market-110358); [ECDB — İspanya moda endüstrisi](https://ecdb.com/resources/sample-data/market/es/fashion); [Grand View Research — Türkiye tekstil pazarı](https://www.grandviewresearch.com/horizon/outlook/textile-market/turkey)

**Ödemeler, lojistik ve kanallar**
- [PPRO — İspanyol e-ticaret ödemeleri ve Bizum](https://www.ppro.com/countries/spain/); [Stripe — işletmeler için Bizum](https://stripe.com/resources/more/bizum-for-buisinesses-spain); [Antom — Cartes Bancaires](https://knowledge.antom.com/cartes-bancaires-explained-what-global-merchants-need-to-know); [Payplug — CB şeması](https://www.payplug.com/blog/cb-scheme/); [Crowdfund Insider — Klarna'nın Fransa'da 5 yılı](https://www.crowdfundinsider.com/2026/06/287201-bnpl-fintech-klarna-marks-5th-year-of-steady-business-growth-in-france/)
- [Cross-Border Magazine — CTT Express Flash araştırması, İspanya & Portekiz 2025](https://cross-border-magazine.com/ecommerce-trends-spain-portugal-2025-ctt-flash-study/); [DHL eCommerce — 2025 sınır ötesi satın alma trendleri](https://www.dhl.com/global-en/microsites/ec/ecommerce-insights/insights/e-commerce-logistics/2025-cross-border-trends.html)
- [ShippyPro — SEUR ile kargo](https://www.shippypro.com/blog/en/shipping-with-seur-a-guide-to-costs-and-services-2026); [Zunapro — İspanyol e-ticaret lojistiği ve kuryeler](https://www.zunapro.com/spain/en/blog/ecommerce-logistics-spain-carriers); [Avrupa fulfilment maliyet benchmark'ları](https://fulfillment-france.eu/european-fulfillment-cost/)
- [TikTok Newsroom — TikTok Shop Avrupa'da genişliyor](https://newsroom.tiktok.com/tiktok-shop-expands-across-europe?lang=en-150); [Lengow — TikTok Shop Avrupa 2026 Q2](https://blog.lengow.com/tiktok-shop-europe-q2-2026-e500m-across-four-markets/); [Dataïads — TikTok Shop Fransa](https://www.dataiads.io/en/blog/tiktok-shop-arrive-en-france)

*§6, §7, §8, §16 ve §24'teki tüm hesaplamalar, yukarıda atıf verilen maliyet ve benchmark girdileri üzerine kurulu kendi modellerimdir. Model betikleri tekrar üretilebilir; varsayımlar her bölümde satır içinde belirtilmiştir.*

*İngilizce versiyon: `research/spain-france-premium-scarf-venture-feasibility.md`*
