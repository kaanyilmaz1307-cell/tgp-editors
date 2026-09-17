# Turkey → Spain → France: Premium Women's Scarf DTC Venture — Feasibility Report

**Date:** 2026-09-17
**Prepared for:** Kaan Yılmaz
**Question:** Can we source quality scarves/foulards from Turkey at low-to-mid cost, position them as a premium European fashion-accessories brand in Spain (then France), and scale profitably on Meta + Google Ads into Q4 2026?

**Method and its limits — read this before you trust a number.**
Research was done from a sandboxed environment where outbound page fetching was blocked by the network egress proxy. That means:

- Every figure below comes from **search-surfaced content** (press, official press notes, industry bodies, benchmark aggregators), not from me opening the primary PDF or the competitor's live product page.
- **I could not open Meta Ad Library, Google Keyword Planner, Google Shopping, or a single competitor storefront directly.** Competitor prices are the prices reported in search results for those brands, dated where possible. Before you commit to a price ladder, re-verify the ~10 competitors that matter on their live sites. It takes an hour.
- **No keyword volume data was obtainable.** Section 17 gives you the keyword architecture and a method, not volumes. You must pull volumes yourself from Keyword Planner (free with a Google Ads account) before funding Google.
- Where a number comes from a market-research vendor selling a report (Fortune Business Insights, Grand View, ECDB, Mordor), I label it **[vendor estimate]**. Those are directional at best and I have not used any of them to justify a decision. Official-source numbers (CNMC, INE, FEVAD, IAB Spain, European Commission, INSEE/IFM) carry the weight.
- USD figures converted at **1 USD ≈ €0.92** and labelled.

Anything I could not verify, I say so rather than filling the gap.

> **UPDATE — 2026-09-17, second verification pass.** A targeted second round of price research corrected four figures in §11. Two are decision-relevant:
> - **Massimo Dutti sells a 100% silk printed (paisley) scarf at €29,95** (linen €39,95). My first pass read "scarves from €30" as non-silk. A trusted Spanish premium brand selling 100% silk at half the hero price makes the differentiation burden heavier than §11 originally implied. **This is the #1 price to verify live** — size and discount status unknown.
> - **Fio de Martié's 70×70 cm and 90×90 cm silk squares are €94,90** (33×33 cm €16,90; bandanas from €48,90; Italian silk, handmade in Spain). My first pass said "from €48.90". The Spanish premium ceiling is therefore *higher* than I stated, which makes €59.90 safer, not riskier.
> - **ARKET cashmere is ~£85 (≈€98) and printed silk ~£45 (≈€52)**, contradicting the "€39 cashmere" figure in §11. The plain-cashmere threat is softer than stated. Unresolved — verify in EUR.
> - **Hamzah (ES artisan): silk scarves €35–49, large €47, "Noisette" €69**, free shipping over €50. Confirms the Spanish independent-premium band.
>
> Net effect: the €59.90 hero price holds, because the verified Spanish independent-premium band is wider than first stated (Hamzah €35 → Fio de Martié €94,90) with €59.90 in the middle. But Massimo Dutti's €29,95 silk makes making the difference visible mandatory rather than optional.
>
> **Live-site verification remains impossible from this environment** — the egress proxy allows only GitHub (WebFetch and curl both tested and blocked). The Turkish version of this report carries the full corrected table with a per-row verification-status column and a 12-row checklist you can complete yourself in 15 minutes: `research/ispanya-fransa-premium-sal-girisimi-fizibilite.md`.

---

# 1. EXECUTIVE SUMMARY

## The one-paragraph answer

The demand is real, the category is genuinely in fashion right now, the gross margin structure works, and your creative advantage is worth a measurable amount of money. But your **core premise is out of date**: Turkey in 2026 is not a cheap-sourcing story, it is a *fast, low-MOQ, mid-cost* sourcing story, and the Turkish textile sector is in a documented cost crisis. And the arithmetic is unforgiving in a specific way: at market-average Meta performance this business **loses money**, and only becomes profitable in the top quartile of creative + conversion + AOV simultaneously. That is not a reason to walk away — it is a reason to size the bet as a test, not a launch, and to gate it on two numbers.

**Verdict: TEST FIRST.** Spain only. €5,000. One product family, one price, one country, 60 days, with pre-committed kill criteria. Details in Section 26.

## The 15 questions, answered

| # | Question | Answer | The evidence that decides it |
|---|---|---|---|
| 1 | Is the business model sound? | **Conditionally yes.** Gross margin is 64–69% of net revenue at €59.90+. That is enough to fund paid acquisition — but only if CTR × CVR clears a specific bar. | Break-even CAC €27.18 at €59.90 with €8 landed COGS and 10% returns (my model, §7) |
| 2 | Real customer demand in Spain? | **Yes.** 27.4M online shoppers (77% of 16–74s); clothing = 7% of Q4 2025 e-commerce turnover; women = 56.5% of online fashion buyers; fashion is the #2 Christmas gift category at 43% | IAB Spain *Estudio Ecommerce 2025*; CNMC Q4 2025; OCU Christmas 2025 |
| 3 | Real customer demand in France? | **Yes, larger but harder.** Clothing e-commerce = €7.7bn, 30.7% of all clothing consumption is now digital. But the average basket *fell* to €62 (−3%) and fashion was the only sector down in volume | FEVAD *Chiffres Clés 2025* / *Mode et Internet 2025* |
| 4 | How strong is the scarf/foulard category for women? | **Strong and currently trending.** Silk scarves are named a top spring 2026 accessory trend, on SS26 runways (Totême, Dries Van Noten); search interest peaks in October and December | WWD, Marie Claire UK, trend/search analyses (§5) |
| 5 | Can you do premium positioning? | **Yes, in the €49–79 band. Not above.** There is a real, occupied, price-validated tier there: Philéone €42–95, Le Châle Bleu €39–169, Fio de Martié from €48.90, & Other Stories cashmere €49 | Competitor price scan (§11) |
| 6 | Does Turkish sourcing give you an edge? | **Yes — but not the edge you think.** The edge is MOQ of 10 pieces per colourway, woven labels, custom embroidery, branded packaging, 5–8 day transit, and 3 time zones of iteration speed. It is *not* price: Turkish minimum wage rose 249% 2022–2024, energy costs doubled, the sector lost $7bn of production and 210,000 jobs, and the lira has appreciated in real terms | Hicabistan (factory-direct from €1.90/pc, MOQ 10/colour); WWD Sourcing Journal; Turkish Minute; ING |
| 7 | Can Meta acquisition economics work? | **Only above benchmark.** At market-average Meta (CPM €13, 1.5% link CTR, 1.8% CVR) CAC is €54.71 against a €27.96 ceiling — a 2x loss. You need **link CTR × session CVR ≥ 0.053%** at €59.90 AOV. That means e.g. 2.0% × 3.0%, not 1.5% × 1.8% | My model (§7–8) against Triple Whale 2025 full-year and 2026 e-commerce benchmarks |
| 8 | How important is Google? | **Very — as the profit channel, not the growth channel.** European e-commerce Shopping CPC is €0.29–0.35. At 3% CVR that is a ~€18 CAC. But scarf search demand in Spain is thin; Google will cap out at low volume. Use it to subsidise blended CAC, never to carry the business | smec Market Observer (€450M annual EU retail ad spend panel) |
| 9 | Is Q4 / BF / Christmas a real opportunity? | **Yes — the single best structural reason to do this.** Spain: €796/person festive spend, €370 on gifts, fashion is 43% of gift purchases, and **Reyes (€192) outspends Christmas Eve (€178)**, extending your season to 5 January. Scarf search peaks Oct and Dec | OCU; Oney; Google Trends analyses |
| 10 | Does your creative production create real advantage? | **Yes, and it is quantifiable.** Brands testing 15+ new concepts/month showed 1.8x higher median ROAS than those testing <5 at equal spend. Buying that output costs €3,000–6,000/month (20 assets at €150–450). You produce it for ~€240/month of tooling | MHI analysis of 80 DTC accounts, 2025; European UGC rate cards |
| 11 | Biggest risks? | (1) Average creative → guaranteed loss, not modest profit. (2) **EU abolishes the €150 duty exemption on 1 July 2026** and imposes a flat €3/item duty — this breaks Turkey-direct-ship for a Q4 2026 launch. (3) Trust: Turkey is not on the list of countries EU shoppers say they trust. (4) France **requires a French representative** for textile EPR since 10 July 2026 | European Commission / Council of the EU; DHL cross-border trends; Refashion / Art. L.541-10-9-1 |
| 12 | What budget should the test be? | **€5,000 hard cap, allocated 30/10/10/40/10** — see §22. Not €5,000 of which €3,000 is Meta. You need more on product/sample and less on website than the default split | — |
| 13 | What to test in the first 30 days? | One thing: **can you get link CTR × CVR above 0.055% at ≥€65 AOV.** Everything else is noise until that clears | §22 |
| 14 | How to progress in the first 90 days? | Days 1–30 prove the funnel gate. Days 31–60 prove AOV architecture and buy inventory. Days 61–90 load Q4, add Google + TikTok Shop, and pre-build the Reyes extension | §23 |
| 15 | Spain or France first, or both? | **Spain first, alone.** Lower CPMs, you live there, Reyes extends the season by 3 weeks, and France carries a compliance stack (Refashion UIN + French representative + Triman) that costs money and weeks before you may sell a single unit. France is a Q2 2027 expansion, not a Q4 2026 co-launch | §4, §20 |

## What I would push back on before you spend a euro

**1. "Turkey = cheap."** This was true in 2019. In 2026 the Turkish textile sector is the *distressed* side of this trade, not the advantaged side: minimum wage +249% (2022–2024), energy costs doubled, financing at up to 50%, $7bn of lost production, 210,000 jobs gone, exports falling into 2026, factories closing. The lira depreciates *slower* than Turkish inflation by policy design (−17% vs USD over 12 months against 32.6% CPI), which means Turkish costs are **rising in euro terms every year.** Your €5–10 landed cost is achievable today and is a wasting asset. Price your product for a €12 landed cost in 2028 and lock 12-month supplier pricing in EUR, not TRY.

**2. "Big market = my product sells."** Spanish household clothing-and-footwear spend *fell* €16 per household in 2025 and dropped to 4.03% of budget. In France the fashion basket fell 4.2% and fashion was the only sector declining in volume, while Shein + Temu took 16% of online clothing purchases at a €9 average price. The mid-market is being destroyed from below. This is an argument **for** premium (€49–79) and a strong argument against ever competing near €24.90.

**3. "Meta will work because I'm good at creative."** Your creative skill moves CTR and, indirectly, CVR. It does not move CPM, VAT, shipping, returns, or the fact that at €59.90 you have €27.96 to spend acquiring a customer. Creative is one of five variables. The other four — offer architecture, landing-page CVR, AOV, and repeat rate — are jobs you have not done before at a founder level. Budget attention for those, not just for ads.

**4. The date problem.** You are aiming at Q4 2026, and the EU's de-minimis abolition lands **1 July 2026** with a temporary flat €3/item duty until 2028. Whether Turkish-origin goods escape it under the EU–Türkiye Customs Union (A.TR) is genuinely unresolved in public guidance. Do not build a direct-ship model on the assumption that it does. Get a written opinion from a Spanish customs broker in week one. Plan on holding stock in Spain.

---

# 2. SPAIN MARKET ANALYSIS

## 2.1 Market size and structure

| Metric | Value | Year | Source |
|---|---|---|---|
| Total e-commerce turnover | **€114.8bn**, +20.6% YoY | 2025 | CNMC (via The Corner) |
| Q4 e-commerce turnover | €31.42bn, +22% YoY | Q4 2025 | CNMC press note |
| Q4 transactions | >575M, +20.2% | Q4 2025 | CNMC |
| Share of Q4 turnover generated inside Spain | 42.2% | Q4 2025 | CNMC |
| **Clothing share of Q4 turnover** | **7.0%** (≈ €2.2bn in one quarter) | Q4 2025 | CNMC |
| Fashion e-commerce revenue | US$9,863M ≈ **€9.1bn**, growing 5–10% | 2025 | ECDB **[vendor estimate]** |
| Online share of fashion retail | 25–30% | 2025 | ECDB **[vendor estimate]** |
| Fashion/apparel share of e-commerce category spend | 29.49% | 2025 | ECDB **[vendor estimate]** |
| Online shopper penetration (16–74) | **77% = 27.4M people** | 2025 | IAB Spain *Estudio Ecommerce 2025* |
| Avg. channels used per shopper | 3.2 (Amazon 82%, brand DTC 47%, other marketplaces 47%, multibrand 39%) | 2025 | IAB Spain 2025 |

**Read the channel number carefully.** Amazon is used by 82% of Spanish online shoppers, but **brand-owned e-commerce is used by 47%** — nearly half. A Spanish woman buying a €59 scarf directly from a brand's own site is a normal behaviour, not an edge case. That is the single most important structural fact for this business in Spain.

## 2.2 Women's fashion and accessories

There is **no reliable public figure for the Spanish scarves/foulards market specifically.** Statista's scarf-level data sits behind a paywall; the only category-level numbers available publicly are global vendor estimates (see §5). Treat any "Spanish scarf market is worth €X" claim as fabricated. What *is* documented:

| Metric | Value | Source |
|---|---|---|
| Women as share of online fashion shoppers | **56.5%** | Statista/Elogia (2022) |
| Largest age band of online fashion shoppers | **35–54** | Statista/Elogia (2023) |
| Top online fashion category | **Women's fashion** — bought by ~2/3 of online fashion buyers | Statista/Elogia (2024) |
| Average online fashion ticket, women | **just under €70** | Statista/Elogia (2024) |
| Average online fashion ticket, men | ~€84 | Statista/Elogia (2024) |

**The €70 number is the most actionable data point in this section.** The average Spanish woman's online fashion order is just under €70. That tells you:

- A **€59.90 single-unit price is inside normal behaviour**, not a stretch.
- A **€69.90–€79.90 bundle or gift set sits at or just above the average ticket** — achievable with a reason (gifting, a set, free shipping threshold).
- €99.90 is roughly 1.4x the average female fashion ticket. Possible as a Christmas gift SKU, not as a core price.

## 2.3 Spending power and where it is

| Metric | Value | Year | Source |
|---|---|---|---|
| Mean household income (incl. imputed rent) | €42,269 | 2024 | INE ECV |
| Mean household expenditure | €35,101 (+3.1%) | 2025 | INE EPF 2025 |
| Mean expenditure per person | €14,066 (+3.2%) | 2025 | INE EPF 2025 |
| Clothing + footwear, share of household budget | **4.03%** (down from 4.21%) | 2025 | INE EPF 2025 |
| Clothing + footwear per household | €1,432 | 2024 | INE EPF |
| YoY change in clothing + footwear spend | **−€16 per household** | 2025 | INE EPF 2025 / Modaes |

**This is a declining category in real terms, and you must plan around it.** Spanish households spent less on clothing in 2025 than 2024, both absolutely and as a share of budget. Per-person fashion spend fell in 2025 after four years of recovery (Modaes). You are entering a shrinking-value, price-polarising market. The winners in that structure are the very cheap (Shein/Temu) and the clearly-worth-it premium. The middle is where brands die.

**Highest-income regions (equivalent mean income, INE ECV 2023 wave):**

| Region | Equivalent mean income | Note |
|---|---|---|
| País Vasco | €26,298 | 90.9% of its municipalities in Spain's top income quartile |
| Comunidad de Madrid | €24,991 | Largest absolute market |
| Navarra | €24,495 | 69.1% of municipalities in top quartile |

**City targeting priority for a premium accessories brand:**

| Tier | Cities | Rationale |
|---|---|---|
| **Tier 1 — open here** | Madrid, Barcelona | Highest income density + highest concentration of premium-fashion buying behaviour + best delivery infrastructure |
| **Tier 2 — add at scale** | Bilbao / San Sebastián, Pamplona, Valencia, Sevilla, Málaga, Zaragoza | Bilbao/Pamplona for income; Valencia/Sevilla/Málaga for volume and climate-appropriate lightweight product |
| **Tier 3 — seasonal only** | Palma, Marbella, A Coruña, Santander | Palma and Marbella skew high-income but seasonal-resident; treat as Q4 gifting geos, not always-on |
| **Deliberately exclude at test stage** | Canarias, Ceuta, Melilla | Outside the EU VAT/customs territory of Spain for these purposes — different tax and shipping handling. Excluding them at test avoids ops noise on a tiny volume gain |

## 2.4 Are Spanish women inclined to buy scarves online?

Honest answer: **there is no scarf-specific purchase-frequency or preferred-material data publicly available for Spain.** I will not invent it. Here is what can be legitimately inferred, and how to actually get the answer:

**What the data supports:**
- Women's fashion is the top online fashion category (~2/3 of online fashion buyers).
- Accessories carry a structural advantage over apparel: **no sizing.** Fit and sizing causes ~50% of apparel returns. A scarf has no size, so its return rate should sit far below the 20–40% apparel band — closer to the 5–10% range typical of accessories and giftables. **This is the strongest single economic argument for this category** and it flows straight into §7.
- Fashion is the #2 Christmas gift category in Spain at 43% intent (behind perfume at 47%), and the #2 Black Friday intent category at 34%.

**What is not supported and you should not assume:** preferred materials, preferred colours, styling habits, or repeat frequency for Spanish women specifically. Anyone who hands you those numbers made them up.

**How to get it for ~€300 in week one:** run a 400-respondent survey via a Spanish panel provider, filtered to women 28–55 in Madrid/Barcelona with online fashion purchases in the last 6 months. Six questions: last scarf purchased (price/where), acceptable price for a silk-feel scarf, material preference, gift vs self-purchase, brand recall, willingness to buy from an unfamiliar brand. That data is worth more than any report you can buy.

## 2.5 Seasonality and the Q4 shape in Spain

| Metric | Value | Source |
|---|---|---|
| Total festive spend per person | **€796** | OCU (Christmas 2025) |
| Of which gifts | **€370** | OCU |
| Reyes (5–6 Jan) gifts | **€192** | OCU |
| Christmas Eve gifts | €178 | OCU |
| Top gift categories | Perfume 47%, **fashion 43%**, toys 35% | OCU |
| Average online festive spend per person | €250 (+4% YoY) | Ecommerce News ES |
| Peak purchase windows | **9–18 December**, and **the days immediately before Reyes** | Retail Actual |
| Black Friday average gift spend | €411 (+4.8% YoY) | Oney 2025 |
| Share using BF to buy gifts | **8 in 10** | Oney 2025 |
| Early-buyer premium | Those who buy early spend **+€140** vs December buyers | Oney 2025 |
| Fashion as preferred BF spend category | 71.3% purchase intent | Oney 2025 |

**The Reyes Magos structure is a genuine, underexploited edge.** Spanish gifting does not end on 25 December — the largest single gift outlay is Reyes, on 5–6 January. Most foreign DTC brands switch off their Q4 campaigns on 20 December to avoid delivery-cut-off risk. If you hold stock in Spain, you can sell profitably through **2–5 January against collapsed CPMs and near-zero competition**, with a 24-hour domestic delivery promise no cross-border competitor can match. Build this into the plan from day one (§14).

---

# 3. FRANCE MARKET ANALYSIS

## 3.1 Market size and structure

| Metric | Value | Year | Source |
|---|---|---|---|
| Total e-commerce turnover | **€196.4bn**, +7% YoY | 2025 | FEVAD |
| Prior year | €175.3bn | 2024 | FEVAD |
| H1 growth | +7.9% | H1 2025 | FEVAD |
| **Average basket** | **€62, −3% YoY** (products −4%, services −3%) | 2025 | FEVAD |
| Clothing e-commerce penetration | **23% of clothing sales = €7.7bn** | 2025 | FEVAD |
| Digital share of total clothing consumption (all ages) | **30.7%** | 2025 | FEVAD *Mode et Internet 2025* |
| Fashion frequency | Buying **more often, +3.9%** | 2025 | FEVAD |
| Fashion basket | **−4.2%** | 2025 | FEVAD |
| Fashion volume | **−0.5% — the only sector in decline** | 2025 | FEVAD |
| In-store apparel chain revenue | −1.2% | 2025 | Républik Retail / IFM |
| French fashion market incl. accessories | **€34.7bn** | 2025 | Institut Français de la Mode |
| Accessories + footwear share of French fashion market | **10%** | 2025 | IFM |
| Clothing/footwear/accessories budget per person | **€668/year** | recent | INSEE (cited via IFM/modelling sources) |

**Top online fashion players by share:** Amazon 22.6%, **Vinted 21.4%**, Shein 17.3%. Shein + Temu together take **16% of online clothing purchases and 5% of all clothing purchases by volume**, at a **€9 average price** versus €14–74 for traditional players (FEVAD).

## 3.2 What that structure actually tells you

France is the bigger market and the harder one, for three structural reasons:

1. **The basket is falling, not rising.** €62 average and −3%. French consumers are buying more frequently at lower value. FEVAD's own delegate general attributes it to "an increased savings phenomenon" plus Chinese low-cost platforms and second-hand growth. A €59.90 single-unit price is **~97% above the national average basket.** In Spain the comparable anchor (women's fashion ticket, just under €70) makes €59.90 look normal; in France, €62 all-category makes it look like a considered purchase.
2. **Vinted at 21.4% is a category-specific threat you do not have in the same degree in Spain.** Second-hand is the #2 fashion channel in France. Scarves are an ideal resale item — small, non-sized, brand-legible, durable. Hermès carrés have an entire secondary market with auction-house valuation services. Your €59 new scarf competes against a genuine pre-owned designer scarf at a similar price.
3. **French shoppers prefer marketplaces.** 83% of French consumers show a strong preference for marketplaces like Amazon and Etsy (DHL cross-border research). A brand-new independent DTC site faces a higher trust hurdle in France than in Spain.

## 3.3 Consumer profile and gifting

| Metric | Value | Source |
|---|---|---|
| Christmas budget 2025 | **€491 — lowest since 2017** (−€6 YoY) | Cofidis 9th edition / franceinfo |
| Median Christmas budget | **€350 (−€50)** | Cofidis |
| Of which gifts | **€297** | Cofidis |
| Meals | €123 | Cofidis |
| 65+ | €638 | Cofidis |
| 18–24 | €538 | Cofidis |
| CSP+ (higher socio-professional) | **€517** | Cofidis |
| CSP− | €370 | Cofidis |
| Average number of gifts | **9 — a record since 2017** | Cofidis |
| Instagram users | **32.87M, 54.4% women**, 25–34 largest cohort | Statista (June 2026) |
| Dominant card scheme | **Cartes Bancaires ~79%** of card share; CB checkout conversion ~85% vs ~75% industry average | Antom / Payplug |
| Klarna footprint | 7M users, 57,500 merchants, €6.2bn TTV over 5 years | Crowdfund Insider 2026 |

**The gifting signal is mixed and you should read it as a warning, not a green light.** The French Christmas budget is at a nine-year low, *but* the average number of gifts hit a record nine. The French are buying **more gifts at lower unit value.** That is precisely the wrong direction for a €59.90–79.90 premium single gift — and precisely the right direction for a **€34.90–44.90 "small beautiful gift"** SKU. If you enter France, the hero SKU should be a smaller format (a 65cm square, a narrow twilly-style scarf) at a lower price point than your Spanish hero. That is a real product decision that the data forces.

**Cities, ranked for a premium accessories launch:**

| Tier | City | Rationale |
|---|---|---|
| 1 | **Paris / Île-de-France** | Income concentration, premium-accessory literacy, highest density of the target avatar. Also the most competitive and highest-CPM geo in France |
| 2 | **Lyon, Bordeaux, Nice** | Lyon: silk heritage city (Croix-Rousse), affluent, strong retail. Bordeaux: high-income, style-conscious, lower CPM than Paris. Nice: affluent + Mediterranean aesthetic fit + seasonal resident wealth |
| 3 | **Toulouse, Nantes, Strasbourg, Montpellier** | Solid income, cheaper media, less premium-fashion saturation |
| 4 | **Lille, Marseille** | Larger populations but weaker average basket for premium accessories; Marseille skews price-sensitive, Lille skews cross-border-competitive with Belgium |

**A warning on Lyon specifically:** Lyon is the historic capital of French silk. Marketing "premium silk" into Lyon with a Turkish supply chain and no atelier story invites exactly the scrutiny you cannot survive. Lyon is a great *revenue* geo and a terrible *first-impression* geo. Launch Paris/Bordeaux, add Lyon once you have reviews and press.

## 3.4 Can a Turkish-sourced brand build trust with French consumers?

**Direct answer: yes, if the brand is legally and operationally European and the Turkish element is presented as craft, not as origin-of-brand. No, if the shopper's first impression is "Turkish scarf brand."**

The evidence:

| Evidence | Implication |
|---|---|
| **7 in 10 shoppers will only buy from countries they trust.** The trusted list cited in DHL's 2025 cross-border research: USA, UK, Germany, China, France, Italy, Canada, Australia. **Turkey is absent.** | Never let "shipping from Turkey" or a Turkish company name be visible pre-purchase. This is not about hiding anything — it is about not volunteering a trust penalty you don't need to pay |
| **83% of French consumers prefer marketplaces** (Amazon, Etsy) | Third-party validation matters more in France than Spain. Reviews, press logos, and possibly an Etsy/Amazon presence running in parallel for social proof |
| Country-of-origin research consistently shows consumers rate products from developed economies higher on quality, and that both *cognitive* and *affective* country-image factors drive product beliefs (cross-national Swedish/Dutch study on Turkish-made products) | The affective channel is the one you can win. "Anatolian craft tradition" is an affective asset. "Made in Turkey" as a bare label is a cognitive liability. Lead with the former |
| Turkey's own state programme (Turquality) exists precisely because Turkish products carry a brand-perception gap that quality alone does not close | Confirms the gap is real and structural, not imagined |
| **Le Châle Bleu**, a French luxury brand, openly sells "hand-drawn in France, made in Italy" at €39–169 | The split-origin story is a proven, premium-compatible structure in this exact category. You are not inventing anything |

**The workable construction:** a Spanish- or French-registered company, a European brand name, EU fulfilment, "Designed in Seville / Made in Türkiye" on the product page and label (which EU textile labelling law effectively requires you to be truthful about anyway — §20), and craft-specific storytelling: the mill, the weave, the hand-rolled hem, named. Section 10 works this through properly.

## 3.5 French competitors and prices

See §11 for the full table. The short version: France is the most densely populated scarf-brand market in Europe.

| Brand | Positioning | Price (as reported) |
|---|---|---|
| Hermès | The category's price ceiling and cultural reference | **€580** for a 90cm carré (was ~€460 three years earlier; +7–10% increases, Feb 2025 hike) |
| Petrusse (Made in France) | Established premium | **$395** (105cm silk) / **$215** (65cm) ≈ €364 / €198 |
| Philéone (Made in France) | Accessible premium — **your direct comp** | Scarves **€42–95**; Emmanuelle and Sylvia both **€68**; hand-painted stole €98; full range €35–190 |
| Le Châle Bleu (drawn FR, made IT) | Accessible premium, split-origin | **€39–169** |
| Sézane | Mass-premium French DTC | Scarves within a broad accessories range (specific prices not verifiable from search) |
| Soeur, SOI Paris, Fleuron Paris, Foularchic, Lollipops, Balaboosté | Mid to accessible premium DTC / Instagram-native | Prices not verifiable from search — **must be checked live** |

**The critical finding: €68 is a validated, occupied French price point for a made-in-France silk scarf from an independent brand (Philéone).** You cannot beat that on provenance. You can beat it on creative, on offer architecture, and on gifting presentation — which is exactly where your advantage lies.

---

# 4. SPAIN VS FRANCE — SIDE BY SIDE

| Metric | Spain | France | Why the difference matters |
|---|---|---|---|
| **Fashion e-commerce size** | ≈€9.1bn (US$9,863M) **[vendor est.]**; clothing = 7% of Q4 2025 e-comm turnover ≈ €2.2bn/quarter (CNMC) | **€7.7bn clothing online** (FEVAD, official) | France's number is official and narrower (clothing only); Spain's is a vendor estimate on a wider definition. **Do not conclude Spain > France.** On comparable clothing-only definitions France is likely the larger clothing e-commerce market |
| **Women's fashion size** | Women's fashion = top online fashion category, bought by ~2/3 of online fashion buyers | Not separately published by FEVAD | Both are majority-female categories; neither publishes a clean women's-only figure. Plan on ~55–60% female share in both |
| **Accessories market** | No public scarf/accessories isolate | Accessories + footwear = **10% of €34.7bn = ~€3.5bn** (IFM) | France has the better-instrumented accessories market. Useful for sizing, not for targeting |
| **Online fashion penetration** | 25–30% of fashion retail **[vendor est.]** | **30.7% of all clothing consumption** (FEVAD, official) | France is further along the digital shift. More normalised buying, also more competitive |
| **Average fashion AOV** | **Women's online fashion ticket just under €70** | **All-category basket €62, falling 3%; fashion basket −4.2%** | Decisive. A €59.90 price sits *inside* normal Spanish female fashion behaviour and *above* the French average basket. Spain supports your target price better |
| **Female buyer share** | **56.5%** of online fashion shoppers | Not published; Instagram 54.4% female | Comparable. No advantage either way |
| **Premium positioning potential** | **Moderate-to-good.** Less dense premium-scarf competition; El Corte Inglés and Massimo Dutti anchor the mid-premium; Fio de Martié proves €48.90+ works | **High ceiling, high difficulty.** Hermès is domestic; Philéone at €68 with Made-in-France is a brutal comp; Vinted at 21.4% supplies premium second-hand | Spain gives you room to *be* the premium option. France makes you the cheapest premium option, which is a worse place to stand |
| **Competition** | Moderate. Retail-led (El Corte Inglés, Cortefiel, Massimo Dutti), some artisan DTC (Fio de Martié, Julunggul, Hamzah, Munira) | **Severe.** Hermès, Petrusse, Philéone, Le Châle Bleu, Fleuron, Soeur, SOI Paris, Sézane, Foularchic, Lollipops, Balaboosté + Vinted resale + Etsy | France has more direct DTC scarf brands than any market in Europe. Spain's competition is mostly retail chains, which do not fight you on Meta creative |
| **Meta Ads potential** | **Better.** Spain's average CPM reported at **~€6** (all-industry; expect €10–18 for cold e-comm conversion). Cheaper auction | Paris CPMs are among Western Europe's highest; Tier-1 range $10–23 CPM | You get more creative iterations per euro in Spain. For a creative-led operator, that is the single most valuable difference between the two markets |
| **Google Ads potential** | Lower search volume, thinner premium-scarf intent | **Higher.** "foulard" is a deeply established French search behaviour with a real branded/generic ecosystem | France is the better Google market by some distance. European Shopping CPC €0.29–0.35 either way (smec) |
| **Consumer purchasing power** | Household income €42,269 (2024); spend €35,101/household. **Clothing spend falling (−€16/household, 4.03% of budget)** | Higher GDP/capita; **Christmas budget at a 9-year low (€491)**; CSP+ €517 | Both are soft. France is richer but currently more defensive on discretionary spend |
| **Shipping complexity** | **Low.** Domestic once you hold stock: SEUR from ~€5.40, GLS ~24h, Correos + 8,000 CityPaq lockers. Exclude Canarias/Ceuta/Melilla | **Moderate.** Cross-border ES→FR adds ~€1/parcel and 1–2 days; a French 3PL or Colissimo/Mondial Relay integration eventually needed | Spain is materially simpler and ~€1/order cheaper if you warehouse in Spain |
| **Returns** | Category advantage: no sizing → expect 5–10%, far below the 20–40% apparel band. Spanish shoppers rank **free shipping #1 (≈65%)** in store choice | Same category advantage. But **Vinted normalises resale over return**, and French consumers are more procedurally rights-aware | Both benign for scarves. Returns are not the risk in this business — CAC is |
| **VAT / tax complexity** | **21% VAT.** OSS covers it once you pass the €10,000 EU-wide distance-selling threshold | **20% VAT.** Same OSS mechanism | Marginal: France's lower VAT is worth ~€1.00 more contribution per €59.90 order (my model, §7). Not a deciding factor |
| **Regulatory entry cost** | **Textile EPR is still a draft.** Royal Decree published 23 June 2025, notified to the Commission 27 May 2026, standstill to 28 Aug 2026, adoption expected 2026. No exemption threshold when it lands | **Live and enforced.** Refashion EPR + **ADEME UIN is a prerequisite to sell at all**, incl. via marketplaces; **Triman + info-tri mandatory on clothing since 1 Feb 2023**; **a non-French producer must appoint a French representative by written mandate (since 10 July 2026)**; eco-contribution ~€0.58/garment (2026 simplified rate) | **This is the decisive operational difference.** France has a hard compliance gate you must clear *before* first sale: UIN, a mandated French representative, and Triman artwork on labels and packaging. Spain's equivalent is not yet in force. France costs you weeks and fees before revenue |
| **Q4 opportunity** | **Superior.** €796/person festive spend, €370 gifts, fashion 43% of gift purchases, 8-in-10 use BF for gifts, early buyers +€140 | Good but softening. €491 budget (9-year low), €297 gifts, record 9 gifts = lower unit value | Spain's Q4 is both larger per head and better shaped for a €50–80 gift |
| **Christmas gifting potential** | **Exceptional, and longer.** **Reyes (€192) > Christmas Eve (€178)** — the season runs to 5 January with a second peak | Single 24–25 December peak; more gifts at lower value | Spain gives you ~3 extra selling weeks at collapsed CPMs that almost no competitor works |
| **Market entry difficulty** | **Low-moderate.** You live there, speak the language, VAT is one registration, EPR not yet binding, CPMs cheaper | **Moderate-high.** Compliance gate, denser competition, higher CPMs, marketplace-preference bias, basket below your price point | Clear |

**Conclusion, stated without hedging: Spain first, alone.** Not because Spain is the bigger market — on clothing-only official data it probably is not. Spain is first because *every operational and economic variable that determines whether a €5,000 test produces a clean signal* is better there: cheaper auction (more creative iterations per euro), no pre-launch compliance gate, a female fashion ticket that brackets your target price, a 3-week-longer Q4, domestic 24-hour delivery, and you on the ground in the market's own language.

France is a 2027 expansion, entered with a *different hero SKU at a lower price*, funded by Spanish profit, after the Refashion and representative paperwork is done in advance.

---

# 5. SCARF / SHAWL PRODUCT MARKET

## 5.1 Category-level demand evidence

| Evidence | Detail | Source |
|---|---|---|
| Global scarves & shawls market | US$26.22bn (2025) → US$28.04bn (2026) → US$56.37bn (2034), 9.12% CAGR | Fortune Business Insights **[vendor estimate — directional only]** |
| **Fashion trend status** | Silk scarves named **spring 2026's biggest accessory trend**; "2026 is the year of the scarf" | WWD, Marie Claire UK |
| SS26 runway validation | **Totême, Dries Van Noten, Maria McManus, Maison Magdalena** — long silk scarves with crochet tassels; narrow fluid scarves with statement tassels | WWD |
| 2026 styling direction | Scarf as **focal point** (2025 was minimalist accent): larger dimensions, double-sided prints, worn as skirts, belts, shawls, on bags, in hair | Marie Claire UK, WWD, trend analyses |
| 2026 colour direction | Intense red, deep blue, jade green; 70s chains, equestrian motifs, baroque prints, hand-painted and watercolour florals | Trend analyses |
| **Search seasonality** | "Silk scarf" is the highest-volume year-round term, peaking **October (81) and December (85)**. "Wool scarf" peaked **December (96)**, down to 21 by August. "Designer scarf" grew 7 → 30 from Oct to Dec | Google Trends analyses |
| EU imports of HS6214 (shawls, scarves, mufflers, mantillas, veils) **from Turkey** | **US$8.42M in 2025** ≈ €7.7M | Trading Economics |

**Two observations that matter more than the market-size number.**

**First, the trend is real and it is now.** This is not me reading a blog. Named SS26 runway houses, WWD and Marie Claire editorial, and search interest peaking in exactly the Oct–Dec window you want to sell in. A category tailwind is a genuine asset for a creative-led launch, because trend-adjacent creative gets cheap organic distribution. **But it is also a clock.** Trends in accessories run 18–30 months. If you launch Q4 2026 you are launching into the middle-to-late phase, not the front. That argues for moving fast and for building an owned asset (email list, repeat customers) that outlives the trend, not for a long build.

**Second, that $8.42M EU-import figure is the most interesting number in this report.** Total EU imports of scarves *from Turkey* were under €8M in 2025. For context, Spanish clothing e-commerce alone runs ~€2.2bn per quarter. This cuts both ways:

- **Bearish read:** Turkey is not a major scarf supplier to Europe. If Turkish scarves were a great arbitrage, more people would be doing it.
- **Bullish read, and I think the correct one:** the lane is *empty*. There is no incumbent Turkish-sourced European scarf brand you have to displace. You are not entering a crowded arbitrage; you are entering an unworked one. The figure also likely understates the flow, since goods in free circulation and small parcels are inconsistently captured.

## 5.2 Product-by-product analysis

Prices below are **market retail bands observed in the competitor scan (§11)**, not my recommendations. "Premium retail" = what an independent brand with good presentation and a story can hold. Shipping weights are estimates from typical construction; verify with your supplier's actual specs.

| Product | Material reality | Typical retail | Premium retail | Peak season | Customer profile | Gift potential | Perceived value | Competition | Return risk | Ship weight | Upsell potential |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Silk scarf (90cm carré)** | Mulberry silk twill, hand-rolled hem | €40–90 | **€69–99** | **Oct + Dec peaks; year-round base** | 35–55, classic, brand-literate | **Very high** | **Highest in category** — "silk" is the value word | Severe (Hermès reference, Philéone €68, **Massimo Dutti 100% silk €29,95**) | Low (5–7%) | 60–90g | High — ring, box, second colourway |
| **Silk scarf (65cm / small square)** | Same fabric, less of it | €30–55 | **€49–69** | Spring + Dec | 28–45, hair/bag styling | High | Good — reads premium at lower price | High | Low | 30–45g | **Highest — ideal 2-pack and add-on** |
| **Satin scarf** | Polyester satin; silk *look*, not silk feel | €15–30 | €29–39 | Oct–Dec | 25–35, price-led, trend-led | Medium | **Fragile** — "satin" signals synthetic to informed buyers | Very high (Zara/H&M/Shein) | Low | 40–70g | Medium |
| **Cotton scarf** | Cotton voile / lawn, often printed | €20–40 | €34–49 | Spring/summer; weakest Dec | 30–50, casual-elegant, Mediterranean | Medium | Moderate — honest, not luxurious | High | Low | 80–120g | Medium |
| **Cashmere scarf** | 100% cashmere or wool-cashmere blend | €39–120 | **€89–149** | **Nov–Feb** | 40–60, quality-first, gifting | **Very high** | **Very high** — strongest "worth it" material | Moderate (ARKET €39, & Other Stories €49 undercut brutally) | Low | **200–350g** | High — gloves, beanie, matching set |
| **Wool scarf** | Merino / lambswool, woven or knit | €25–60 | €59–89 | **Nov–Feb** | 30–55, practical-premium | High | Good | High | Low | **180–300g** | High |
| **Modal scarf** | Modal or modal-silk blend; excellent drape, low cost | €20–40 | €39–59 | Year-round | 28–45 | Medium | Moderate — consumers don't know the word | Moderate | Low | 70–110g | Medium |
| **Viscose scarf** | Viscose / rayon; cheapest premium-*looking* option | €12–30 | €29–39 | Year-round | 25–40, price-led | Low-medium | **Weak** — reads cheap when named | Very high | Low | 60–100g | Low |
| **Oversized shawl / stole** | Wool, cashmere-blend, or modal-silk; 200×70cm+ | €45–120 | **€89–139** | **Nov–Jan** | 40–65, evening/travel | **Very high** | **Very high** — size reads as value | Moderate | Low-medium | **250–400g** | High — gift box, travel pouch |
| **Elegant women's scarf (long, printed)** | Silk-feel or modal, 180×70cm | €30–70 | €59–79 | Sep–Dec | 30–55 | High | Good | High | Low | 80–140g | High |
| **Winter scarf (chunky knit)** | Wool/acrylic blend knit | €20–50 | €49–69 | **Nov–Jan only** | 25–45 | Medium-high | Moderate | Very high | Low | **250–450g** | Medium |
| **Lightweight scarf** | Cotton-silk, modal, voile | €20–45 | €39–59 | **Mar–Sep** | 28–50 | Medium | Moderate | High | Low | 50–90g | Medium |
| **Head scarf / bandana** | Silk or cotton square, 50–55cm | €18–40 | €34–49 | Spring/summer | 22–38, styling-led, strong TikTok fit | Medium | Moderate | High (incl. Etsy) | Low | 25–40g | **High — natural 3-pack** |
| **Neck scarf / twilly** | Narrow silk band, 5–120cm | €15–35 | €29–45 | Year-round; **Dec gifting spike** | 25–45, bag-styling | **High** — classic impulse gift | Good — luxury-adjacent format | Moderate | **Very low** | **10–20g** | **Highest — pure margin add-on** |
| **Luxury scarf (positioning, not material)** | Whatever you can defend | €90–200 | €149–249 | Dec | 45–65 | Very high | Depends entirely on brand equity you don't have yet | Direct with Hermès/Ferragamo — do not go here in year one | Low | varies | — |
| **Printed scarf (design-led)** | Any base; the print is the product | €30–90 | €59–99 | Oct–Dec | 30–55, design-conscious | High | **Good — and the most defensible**, because a proprietary print cannot be price-compared | Moderate | Low | varies | High — print family / collection |

## 5.3 Which product to actually launch

**Hero SKU: a 90cm printed silk-feel square with hand-rolled hem, in a proprietary print, at €59.90.** Reasoning:

- **"Silk" is the value word** and silk squares carry the highest perceived value in the category.
- **A proprietary print is the only defensible moat available to you.** A plain cashmere scarf is instantly comparable to ARKET at €39 and you lose. A print nobody else has cannot be price-compared — and print design is a task your AI image pipeline is genuinely good at.
- **60–90g ship weight** keeps you in the cheapest parcel tier and well under the €150 IOSS/customs threshold.
- **October *and* December search peaks** give you two demand windows, not one.
- Return risk is low (no sizing), which is what makes the whole unit economic model survivable.

**Second SKU (launch simultaneously, it is your AOV engine): a narrow twilly / neck scarf at €24.90–29.90.** 10–20g, near-zero incremental shipping, pure margin, and it is the natural "add for €24.90" post-purchase upsell. Section 15–16 build on this.

**What not to launch in year one:** cashmere (undercut by ARKET €39 / & Other Stories €49 with real brand trust), satin or viscose by name (kills your premium claim), and anything in the "luxury scarf" €149+ band (you have no equity to defend it).

---

# 6. PRICE POSITIONING

## 6.1 The price ladder, evaluated

Break-even CAC below comes from the model in §7 (Spain, 21% VAT, €8.00 landed COGS, €2.00 packaging, €1.80 pick/pack, €4.20 domestic shipping, 2.5% + €0.25 payment fees, €0.20 EPR provision, 10% return rate). "Max CAC" is the true constraint: the most you can pay to acquire an order and still make zero.

| Gross price | Net of VAT | Contribution | CM % of net | **Max CAC** | Conversion potential | Perceived quality | Premium perception | Margin potential | Gift potential | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| €19.90 | €16.45 | **−€0.50** | **−3%** | **−€1.58** | Very high | Low | None | **Negative** | Low | **Structurally impossible.** You lose money before advertising |
| €24.90 | €20.58 | €3.51 | 17% | **€2.02** | Very high | Low | None | Negligible | Low | **Impossible as a standalone.** Viable only as a €24.90 *add-on* to an existing order where CAC is already paid — which is exactly how to use it |
| €29.90 | €24.71 | €7.51 | 30% | **€5.61** | High | Low-medium | Weak | Very thin | Medium | Only works as an add-on or as a loss-leader front-end with a hard upsell. Unbuyable on paid traffic |
| €34.90 | €28.84 | €11.52 | 40% | **€9.21** | High | Medium | Weak | Thin | Medium | The Zara/Mango zone. €9 CAC is not achievable on Meta cold traffic. **No** |
| €39.90 | €32.98 | €15.53 | 47% | **€12.80** | Medium-high | Medium | Emerging | Workable | Medium-high | Borderline. €12.80 CAC requires exceptional creative *and* 3%+ CVR. Use as a promotional or bundle-component price, not as the hero |
| €44.90 | €37.11 | €19.53 | 53% | **€16.39** | Medium | Medium-high | Moderate | Good | High | Viable floor for a hero SKU. Tight but real |
| **€49.90** | €41.24 | €23.54 | **57%** | **€19.99** | Medium | **High** | **Good** | **Good** | **High** | **Viable hero price. The conservative choice.** Matches & Other Stories cashmere (€49) and Fio de Martié (€48.90) — both validated |
| **€59.90** | €49.50 | €31.56 | **64%** | **€27.18** | Medium | **High** | **Strong** | **Strong** | **Very high** | **★ Recommended hero price.** Sits inside the Spanish female fashion ticket (just under €70), below Philéone's €68, above the fast-fashion ceiling. Best balance of CAC headroom and conversion |
| €69.90 | €57.77 | €39.57 | 69% | **€34.36** | Medium-low | Very high | Very strong | Very strong | Very high | **Recommended second tier / gift-set price.** Requires visible quality cues (box, hem, weight, print story). Directly at Philéone's €68 — you must win on presentation |
| €79.90 | €66.03 | €47.59 | 72% | **€41.55** | Low-medium | Very high | Very strong | Excellent | Very high | Gift-set and 2-pack territory. As a *single* scarf from an unknown brand this is a hard sell in year one |
| €89.90 | €74.30 | €55.60 | 75% | **€48.74** | Low | Very high | Excellent | Excellent | Very high | Only as a multi-item gift set or oversized cashmere shawl. Not a single 90cm square |
| €99.90 | €82.56 | €63.61 | 77% | **€55.93** | Low | Excellent | Excellent | Excellent | Excellent | Collection/bundle only. €99.90 is ~1.4x the average Spanish female fashion ticket |

## 6.2 The core question: is €4–10 landed → €39.90–69.90 realistic?

**Yes, and the multiple is not the aggressive part.** A 6–8x markup on landed cost is *standard* in fashion accessories, not exceptional. What is aggressive is the CAC that multiple has to fund.

| Landed COGS | @ €39.90 retail | @ €49.90 | @ €59.90 | @ €69.90 |
|---|---|---|---|---|
| **€5.00** | 8.0x markup, max CAC **€15.53** | 10.0x, **€22.72** | 12.0x, **€29.91** | 14.0x, **€37.09** |
| **€7.00** | 5.7x, **€13.71** | 7.1x, **€20.90** | 8.6x, **€28.09** | 10.0x, **€35.27** |
| **€10.00** | 4.0x, **€10.98** | 5.0x, **€18.17** | 6.0x, **€25.36** | 7.0x, **€32.54** |

*(All at 10% returns. Full grid including 5/15/20% return rates in §7.3.)*

**The decisive observation: COGS barely matters.** Moving landed cost from €10 to €5 — a 50% sourcing improvement, which is a hard negotiation — buys you **€4.55 more CAC headroom at €59.90**. Moving retail price from €49.90 to €59.90 — a single pricing decision — buys you **€7.19**. And improving CVR from 1.8% to 2.6% roughly **halves your CAC**.

So the ranked levers, by impact per unit of effort:

1. **Conversion rate** (halves CAC) — landing page, offer, social proof, payment methods
2. **AOV / bundle architecture** (raises the ceiling proportionally) — §16
3. **Retail price** (+€7 headroom per €10 of price, if conversion holds)
4. **Creative CTR** (proportional to CAC)
5. **COGS** (+€4.55 for a 50% sourcing win) — **the thing you were planning to optimise first is the least valuable lever**

That reordering is, I think, the single most useful output of this report.

## 6.3 Psychological pricing notes

- **€59.90 not €60.** Charm pricing still measurably works in EU fashion; €59.90 reads as "fifties".
- **Do not use €.99 endings.** €59.99 signals discount retail in ES/FR; €59.90 or a round €60 signals brand. The .90 convention is the Spanish and French premium-retail norm.
- **Never anchor with a fake RRP.** EU Omnibus Directive rules on prior-price reference are enforced; a "was €120, now €59.90" with no genuine 30-day prior price is an unfair commercial practice and Spanish consumer authorities do act on it.
- **Anchor with the set, not with a strikethrough.** Show the €139.90 collection first; €59.90 then reads as the accessible option. That is legal, durable, and raises AOV.

---

# 7. UNIT ECONOMICS

## 7.1 Cost stack assumptions

| Line | Spain | France | Basis |
|---|---|---|---|
| VAT | **21%** | **20%** | Standard rates; OSS-reported once past the €10,000 EU distance-selling threshold |
| Landed product cost | €5 / €7 / €10 modelled; **€8 base** | same | Turkish factory-direct from €1.90/pc (Hicabistan, MOQ 10/colour); FOB $3–4 at 50–100pc MOQ reported; silk €1.50–2/pc at 1,000pc MOQ. €8 base assumes better fabric than entry tier + custom print + woven label + inbound freight + duty handling |
| Packaging | **€2.00** (mailer, tissue, card, sticker) / €5.50 with rigid gift box | same | Market rates; gift box is the premium-perception purchase |
| Pick & pack (3PL) | **€1.80** | €1.80 | European 3PL pick & pack €1.50–2.50/order |
| Outbound shipping | **€4.20** | **€5.20** | Spain domestic: SEUR from ~€5.40 list, GLS ~24h — €4.20 assumes a negotiated light-parcel rate. FR adds ~€1 cross-border. European all-in fulfilment benchmark €4–8/order |
| Payment processing | **2.5% + €0.25** | same | Card + Bizum/PayPal blended |
| EPR / eco-contribution | **€0.20 provision** | **€0.58** | FR Refashion 2026 simplified rate ~€0.58/clothing item. ES decree not yet in force — €0.20 is a prudent provision |
| Return rate | 5 / 10 / 15 / 20% modelled; **10% base** | same | Apparel is 20–40% (EU central ~30%, up to 46% per Landmark/IPC 2025) but **fit/sizing causes ~50% of apparel returns and scarves have no size.** 10% is my base; 5% is plausible; I model to 20% for safety |
| Cost of a returned order | **€12.20** | — | Lost outbound €4.20 + return leg €4.50 + non-refunded PSP fee €1.75 + inspection/restock €1.00 + 10% write-off on returned units €0.80 |

## 7.2 Full cost stack, single unit at €59.90 (Spain)

| Line | € | % of gross | % of net |
|---|---|---|---|
| **Gross revenue (VAT incl.)** | **59.90** | 100.0% | — |
| VAT (21%) | (10.40) | 17.4% | — |
| **Net revenue** | **49.50** | 82.6% | 100.0% |
| Landed COGS | (8.00) | 13.4% | 16.2% |
| Packaging | (2.00) | 3.3% | 4.0% |
| Pick & pack | (1.80) | 3.0% | 3.6% |
| Outbound shipping | (4.20) | 7.0% | 8.5% |
| Payment processing | (1.75) | 2.9% | 3.5% |
| EPR provision | (0.20) | 0.3% | 0.4% |
| **Total variable cost** | **(17.95)** | 30.0% | 36.3% |
| **Contribution before ads & returns** | **31.56** | 52.7% | **63.7%** |
| Returns drag @10% | (4.38) | | |
| **Contribution after returns = MAX CAC** | **27.18** | **45.4%** | **54.9%** |

**Break-even blended ROAS at this structure: 2.14x.** Anything below 2.14x blended is destroying capital.

## 7.3 Break-even CAC grid — price × COGS × return rate (Spain)

**Landed COGS €5.00**

| Price | Returns 5% | 10% | 15% | 20% |
|---|---|---|---|---|
| €29.90 | €9.43 | €8.34 | €7.26 | €6.17 |
| €39.90 | €17.03 | €15.53 | €14.03 | €12.53 |
| €49.90 | €24.63 | €22.72 | €20.81 | €18.89 |
| **€59.90** | **€32.23** | **€29.91** | €27.58 | €25.26 |
| €69.90 | €39.83 | €37.09 | €34.36 | €31.62 |
| €79.90 | €47.43 | €44.28 | €41.13 | €37.98 |

**Landed COGS €7.00**

| Price | Returns 5% | 10% | 15% | 20% |
|---|---|---|---|---|
| €29.90 | €7.52 | €6.52 | €5.53 | €4.53 |
| €39.90 | €15.12 | €13.71 | €12.30 | €10.89 |
| €49.90 | €22.72 | €20.90 | €19.08 | €17.25 |
| **€59.90** | **€30.32** | **€28.09** | €25.85 | €23.62 |
| €69.90 | €37.92 | €35.27 | €32.63 | €29.98 |
| €79.90 | €45.52 | €42.46 | €39.40 | €36.34 |

**Landed COGS €10.00**

| Price | Returns 5% | 10% | 15% | 20% |
|---|---|---|---|---|
| €29.90 | €4.65 | €3.79 | €2.93 | €2.07 |
| €39.90 | €12.25 | €10.98 | €9.71 | €8.43 |
| €49.90 | €19.86 | €18.17 | €16.48 | €14.79 |
| **€59.90** | **€27.46** | **€25.36** | €23.26 | €21.16 |
| €69.90 | €35.06 | €32.54 | €30.03 | €27.52 |
| €79.90 | €42.66 | €39.73 | €36.81 | €33.88 |

**How to read this:** even at the pessimistic corner (€10 COGS, 20% returns, €59.90), you still have **€21.16 of CAC headroom**. The model is robust to sourcing and returns shocks. It is **not** robust to a CAC above €30. The risk in this business lives entirely in the acquisition line.

## 7.4 Spain vs France at identical gross price

| Price | Spain net | Spain max CAC | France net | France max CAC | Δ |
|---|---|---|---|---|---|
| €49.90 | €41.24 | €19.99 | €41.58 | €18.96 | **−€1.03** |
| €59.90 | €49.50 | €27.18 | €49.92 | €26.21 | **−€0.97** |
| €69.90 | €57.77 | €34.36 | €58.25 | €33.46 | **−€0.91** |

France's 1-point VAT advantage (€0.34 more net at €59.90) is **more than cancelled** by the €0.58 Refashion eco-contribution and ~€1.00 higher cross-border shipping. **France is ~€1/order worse on unit economics from a Spanish warehouse,** before you count the higher CPMs and the compliance setup cost. Once you hold French stock locally this flips slightly positive, but that requires volume you will not have in year one.

## 7.5 Bundle economics — where this business actually makes money

| Offer | Gross | COGS | Contribution | CM % net | **Max CAC** |
|---|---|---|---|---|---|
| 1 scarf | €59.90 | €8.00 | €31.56 | 63.7% | **€27.18** |
| Scarf + scarf ring | €74.90 | €10.50 | €40.48 | 65.4% | **€35.13** |
| **Gift set (scarf + ring + rigid box)** | **€89.90** | €10.50 | **€49.00** | **66.0%** | **€42.72** |
| 2-scarf bundle | €99.90 | €16.00 | €54.71 | 66.3% | **€47.80** |
| 3-scarf bundle | €134.90 | €24.00 | €73.67 | 66.1% | **€64.63** |
| **Premium collection (2 scarves + ring + box)** | **€139.90** | €18.50 | **€79.97** | **69.2%** | **€70.33** |

**This table is the business.** Moving a customer from a single €59.90 scarf to an €89.90 gift set raises your CAC ceiling from €27.18 to €42.72 — **a 57% increase in affordable acquisition cost** — while adding only €2.50 of COGS and €0.60 of packaging and shipping. It is the cheapest ROAS improvement available to you, and it requires no media-buying skill at all.

**Implication for how you launch: do not launch a single-product store.** Launch with a 3-tier architecture (single / gift set / collection) on day one, with the gift set as the visually default option. An all-single-SKU launch caps you at a €27 CAC ceiling and you will probably fail the test on that alone.

## 7.6 Repeat purchase sensitivity

| 12-month repeat rate | 12-month contribution per customer | Max CAC at 1.0x payback |
|---|---|---|
| 0% | €27.96 | €27.96 |
| 15% | €32.16 | €32.16 |
| 25% | €34.95 | €34.95 |
| 35% | €37.75 | €37.75 |

**Do not plan on LTV rescuing a bad CAC.** Even a strong 35% repeat rate only lifts your ceiling from €28 to €38. Scarves are a low-frequency category — one or two purchases a year at most, heavily gift-driven. Any plan that says "we'll accept a €55 CAC because LTV" is wrong by a factor of ~1.5x. **First-order contribution must be positive, or close to it.** That is the discipline this category demands.

---

# 8. META ADS ANALYSIS

## 8.1 Benchmarks (2025 full-year / 2026)

| Metric | Value | Source / caveat |
|---|---|---|
| Meta CPM, all industries | **$14.19** ≈ €13.05 | Full-year 2025 (Triple Whale / aggregators) |
| Meta CTR, all-clicks | 2.19% | Full-year 2025. **This is all-clicks, not link clicks** — link CTR typically runs roughly half |
| Meta conversion rate | 1.60% | Full-year 2025 |
| Median e-commerce CVR on Meta | 1.57% | 2025 |
| Meta CPA, all industries | $38.19 ≈ €35.13 | Full-year 2025 |
| **Meta CPA, apparel** | **$36.76 ≈ €33.82** | 2025 — slightly better than platform median |
| Meta ROAS, all industries | 1.86x | Full-year 2025 |
| Healthy 2026 e-comm account | **link CTR 1.2–2.5%, CPM €8–18 cold, CPC €0.50–1.80, blended ROAS 2.0–3.5x** | 2026 benchmark aggregations |
| **Spain average CPM** | **~€6** | Reported all-industry, all-objective. **Do not plan on this.** Cold conversion campaigns in a premium-fashion auction run €10–18. Use €6 as evidence Spain is a *cheaper auction than France*, not as your media plan |
| Meta CPM YoY inflation | **+20.03%** in 2025 | Triple Whale, Apr 2026 |
| Site CVR, fashion | 2.5–3.1% | Industry benchmark |
| Site CVR, Shopify average | 1.40% | Industry benchmark |
| Site CVR, luxury/jewellery | 0.8–1.2% | Industry benchmark — a warning: if you position too far upmarket, CVR collapses |
| **Q4 CPM inflation** | Q4 **+26% vs Q1**; **November +41%** above annual average; Q4 overall **35–45% above average**; **BFCM peak days 2–3x baseline** | Multiple 2025/2026 benchmark sources |

## 8.2 Three scenarios at €5,000 spend (non-Q4 CPM)

Funnel: impressions → link clicks → landing-page sessions (88% of clicks) → orders. Contribution taken at 65.5% of net revenue (the single/bundle blend), with 10% returns applied.

| Scenario | CPM | Link CTR | CVR | Impressions | Clicks | Sessions | Orders | CPC | **CAC** | AOV | Revenue | **ROAS** | Contribution | **Net after ads** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Conservative** | €16 | 1.00% | 1.0% | 312,500 | 3,125 | 2,656 | 27 | €1.60 | **€188.24** | €49.90 | €1,325 | **0.27** | €613 | **−€4,387** |
| **Base** | €13 | 1.50% | 1.8% | 384,615 | 5,769 | 5,077 | 91 | €0.87 | **€54.71** | €59.90 | €5,474 | **1.09** | €2,555 | **−€2,445** |
| **Aggressive** | €12 | 2.50% | 2.6% | 416,667 | 10,417 | 9,375 | 244 | €0.48 | **€20.51** | €72.00 | €17,550 | **3.51** | €8,253 | **+€3,253** |

**Same scenarios with November CPMs (+40%):**

| Scenario | Q4 CPM | CAC | ROAS | Net after ads |
|---|---|---|---|---|
| Conservative | €22.40 | €263.53 | 0.19 | −€4,562 |
| Base | €18.20 | €76.60 | 0.78 | −€3,175 |
| Aggressive | €16.80 | **€28.72** | **2.51** | **+€895** |

## 8.3 The finding you need to sit with

**At market-average Meta performance, this business loses money — and not marginally.** The Base case uses defensible, benchmark-consistent inputs (€13 CPM, 1.5% link CTR, 1.8% site CVR) and produces a **€54.71 CAC against a €27.96 ceiling**. That is a 2x overshoot and a €2,445 loss on a €5,000 test.

**There is no version of "average" that works here.** For a single-unit €59.90 product to break even at market-average Meta, you would need an AOV of **€114.81**. At a 2.5% CVR you'd still need **€83.36**.

| CPM | Link CTR | CVR | → CAC | AOV required to break even |
|---|---|---|---|---|
| €13 | 1.5% | 1.8% | €54.71 | **€114.81** |
| €13 | 1.5% | 2.5% | €39.39 | €83.36 |
| **€13** | **2.0%** | **2.5%** | **€29.55** | **€63.15** |
| €16 | 1.5% | 1.8% | €67.34 | €140.73 |

**Notice the third row.** Getting link CTR to 2.0% and CVR to 2.5% brings the required AOV down to €63.15 — which is achievable with a gift-set-led offer architecture. **That is the whole plan in one line: 2% CTR × 2.5% CVR × €65 AOV.**

## 8.4 The single gate: required (link CTR × session CVR)

Break-even requires orders per 1,000 impressions ≥ CPM ÷ max CAC. Dividing through, the required **product of link CTR and session CVR** is:

| AOV | Max CAC | CPM €10 | CPM €13 | CPM €16 | CPM €20 |
|---|---|---|---|---|---|
| €39.90 | €18.22 | 0.062% | 0.081% | 0.100% | 0.125% |
| €49.90 | €23.09 | 0.049% | 0.064% | 0.079% | 0.098% |
| **€59.90** | **€27.96** | **0.041%** | **0.053%** | **0.065%** | 0.081% |
| €69.90 | €32.83 | 0.035% | 0.045% | 0.055% | 0.069% |
| €79.90 | €37.71 | 0.030% | 0.039% | 0.048% | 0.060% |
| €99.90 | €47.45 | 0.024% | 0.031% | 0.038% | 0.048% |

**Reference points:** a 1.5% × 2.0% funnel = 0.030%. A 2.0% × 3.0% funnel = 0.060%.

**This one number is your entire KPI dashboard.** At €59.90 AOV and €13 CPM you need **0.053%**. At €65 AOV with November CPMs (~€18) you need about **0.065%**. Track `link CTR × CVR` daily as a single figure. It collapses creative quality, offer quality, and landing-page quality into the only metric that decides whether you have a business. Everything else — CPM, CPC, ATC rate, ROAS — is diagnostic detail for *why* that number is where it is.

## 8.5 Practical Meta structure for the test

| Element | Recommendation | Why |
|---|---|---|
| Campaign objective | Sales / purchase conversion from day one | You are testing economics, not learning audiences |
| Structure | **1 campaign, 2–3 ad sets, 8–15 diverse creatives per ad set** | Meta's own guidance is 8–15 ads per ad set. One ad set with 25 diverse creatives produced **17% more conversions at 16% lower cost** than five ad sets of five |
| Targeting | **Broad + Advantage+ audience**, Spain excluding Canarias/Ceuta/Melilla, women 25–60. One interest-stack ad set as a control | Andromeda-era Meta finds the buyer from creative signal; manual interest stacking mostly constrains delivery |
| Creative diversity | **Genuinely different angles, not variations.** Similar ads (>60% similarity) are collapsed into a single Entity ID and made to compete with each other for one slot instead of expanding reach | This is the technical reason your 30-angle library (§13) is worth more than 30 hook variants of one angle |
| Volume cadence | **15–20 new *concepts* per month, minimum** | Brands testing 15+ concepts/month showed **1.8x higher median ROAS** than <5 at equal spend; 20+ new ads/month → 65% higher ROAS than <10 |
| Budget pacing | €80–120/day for the first 14 days; do not scale until the CTR×CVR gate clears | At €100/day you get ~7,700 impressions/day at €13 CPM — enough for a read on CTR in 3–4 days, but you need ~2 weeks for a CVR read |
| Q4 timing | **Front-load October.** November CPMs run +41% above annual average and BFCM peak days hit 2–3x | Acquire cheaply in Oct, harvest in Nov–Dec with retargeting and email, then work the Reyes window when CPMs collapse |

---

# 9. YOUR CREATIVE ADVANTAGE — QUANTIFIED

## 9.1 What the advantage is worth in cash

| Model | Cost per ad asset | 20 assets/month | Annual |
|---|---|---|---|
| Agency / UGC creator market rate | €150–450 (mid-tier €150–500; usage rights +30–50%; whitelisting +30%/mo; hook variants ~€46 each) | **€3,000–9,000/mo** (at €300 avg: €6,000) | **€36,000–108,000** |
| Freelance editor + paid creators | ~€150 | €3,000/mo | €36,000 |
| **You + AI stack** | **~€12** (tooling ~€240/mo ÷ 20 assets) | **€240/mo** | **€2,880** |

**Direct cash advantage: roughly €33,000–70,000 per year of creative production you do not have to buy.** At the €5,000 test scale, that is the difference between spending €3,000 on ads and €2,000 on creative, versus **€4,400 on ads and €600 on tooling** — a 47% larger media budget from the same capital.

## 9.2 What the advantage is worth in performance (the bigger number)

| Evidence | Figure | Source |
|---|---|---|
| Brands testing **15+ new concepts/month** vs <5, at equal spend | **1.8x higher median ROAS** | MHI analysis, 80 DTC accounts, 2025 |
| Brands testing **20+ new ads/month** vs <10 | **65% higher ROAS** | 2025 benchmark analysis |
| One ad set, 25 diverse creatives vs five ad sets of five | **+17% conversions at −16% cost** | Meta guidance / practitioner data |
| Andromeda (mid-2025) increased the ad volume Meta processes by **10,000x**; creative signal is now the primary input to who sees your ads; ads >60% similar collapse into one Entity ID | Structural | Meta / Andromeda practitioner guides |

**Apply that to my own model.** Base case CAC was €54.71 — a loss. Multiply ROAS by 1.8x (the measured creative-velocity effect) and Base-case ROAS goes from **1.09x → 1.96x**. Break-even is 2.14x. **So your creative advantage alone gets you from "losing half your money" to "almost break-even" — and not past the line.**

That is the honest arithmetic, and it is the most important thing in this report. Your edge is large, real, and measured — *and it is not sufficient on its own.* You need the creative advantage **plus** a €65+ AOV **plus** a 2.5%+ CVR. Any two of the three loses money.

## 9.3 Normal founder vs your model

| Cost / capability | Typical new DTC founder | You | Delta |
|---|---|---|---|
| Creative production, 20 assets/mo | €3,000–6,000 | €240 | **−€3,000 to −5,800/mo** |
| Creative iteration latency | 7–21 days (brief → shoot → edit → revisions) | **Hours** | Compounding: ~10–20x more learning cycles per quarter |
| Media buying | €1,500–3,000/mo agency or 10–15% of spend | €0 | −€1,500 to −3,000/mo |
| Hook/angle library depth | 3–8 angles, recycled | **30+ distinct angles, expandable** | Directly feeds Andromeda's demand for semantic diversity |
| Product photography | €800–2,500 per shoot | AI + one real sample shoot | −€800 to −2,000 |
| Video/VSL capability | Outsourced or absent | **9 years, including VSL** | The differentiated asset — see §9.4 |
| **Total monthly overhead avoided** | — | — | **~€5,000–9,000/mo** |
| **What you must still buy or learn** | — | CRO/landing-page conversion, offer design, Spanish/French copy nuance, 3PL ops, EU compliance, email/retention, customer service in Spanish | **This is the real gap. Budget for it** |

## 9.4 The part of your background that matters most — and it isn't UGC

Everyone in DTC can buy UGC. What almost nobody selling €59 accessories can do is build a **structured long-form persuasion asset.** Your four years cutting VSLs at Malaberg is the genuinely scarce skill here, and it maps onto this business in a specific way:

- **Scarves have a styling-competence objection, not a price objection.** The reason a Spanish woman doesn't buy a €59 silk scarf is *"I don't know how to wear it and it will sit in a drawer."* That is not solved by a 6-second hook. It is solved by a **90-second styling demonstration that resolves the competence fear** — which is a VSL structure applied to a fashion product.
- A "5 ways in 60 seconds" styling video is a mini-VSL: problem (outfit feels flat) → mechanism (one accessory, five placements) → proof (five looks) → offer → CTA. You can produce 20 variants of that in a week.
- **This also raises CVR, not just CTR** — which is the lever that matters most per §6.2. Embed the styling video on the product page, above the fold. Most scarf brands show flat-lay photography and lose the sale there.

**That is the actual thesis of this venture, stated properly:** not "cheap Turkish scarves sold at premium prices," but *"the styling-competence objection in fashion accessories is solvable with direct-response video, I can produce that at 20x the industry's rate for 4% of the cost, and accessories have no sizing so the returns don't eat the margin."*

---

# 10. BRAND POSITIONING

## 10.1 The Turkey question, resolved

You have three structural options. Only one of them is both legal and low-risk.

| Option | Construction | Advantage | Disadvantage | Verdict |
|---|---|---|---|---|
| **A. Silent origin** | European brand, European company, no mention of Turkey anywhere except the legally required composition/origin label | Zero trust penalty; maximum positioning freedom | If a customer or a competitor surfaces it as a "gotcha," you look evasive. Reddit/forum risk. And EU textile labelling law requires a truthful fibre-composition label anyway | **Legally fine, strategically fragile.** Don't build on a fact you're hiding |
| **B. "Designed in Europe, crafted in Türkiye"** | European brand/company/fulfilment, Turkish craft named openly and specifically (mill, weave, hand-rolled hem) | Honest, defensible, and **proven in this exact category** — Le Châle Bleu sells €39–169 on "hand-drawn in France, made in Italy." Gives you a craft story, which is a *positive* asset in accessories | Turkey is not on the list of countries EU shoppers name as trusted (DHL). Must be handled as craft heritage, never as a price signal | **★ Recommended** |
| **C. Turkish heritage brand** | Lead with Anatolian/Ottoman textile heritage as the core brand identity | Genuinely differentiated; nobody occupies it in European premium accessories; strong print/story potential | Highest trust cost in Spain and especially France; risks reading as "souvenir" or ethnic-craft rather than premium European wardrobe | **No for Spain/France year one.** Revisit for Germany/Netherlands/US later, where Turkish diaspora and craft-market receptivity differ |

**Execute Option B like this:**

- **Company and brand are European.** Spanish SL (or your existing structure), Spanish or European-sounding brand name, Spanish address, Spanish returns address, Spanish phone/WhatsApp, `.es` or `.com` domain.
- **Turkey appears as craft, and specifically.** Not "made in Turkey." Instead: *"Woven in Bursa, the silk city, on looms that have run for four generations. Hems rolled and stitched by hand — eight minutes per scarf."* Specificity is what converts origin from a liability into a proof point. Bursa's silk history is genuine and verifiable, which is exactly why it works.
- **Never use Turkey to explain the price.** "Great quality at a fair price because we source directly from Türkiye" invites the reader to price-anchor against Temu. The price is justified by design, hand-finishing, and presentation — never by cheap labour.
- **Where it appears:** About page, product-page "Craft" accordion, a hangtag, one or two founder-story creatives. **Not** in the ad hook, not in the brand name, not in the tagline, not on the homepage hero.
- **Comply properly.** Fibre composition label in Spanish (and French when you enter France) per Reg. (EU) 1007/2011, and a GPSR Responsible Person with EU address on the product, packaging or accompanying document. Getting this right is also what makes the story safe to tell.

## 10.2 Five positioning directions

| # | Direction | Target customer | Price positioning | Creative direction | Brand story | My read |
|---|---|---|---|---|---|---|
| **1** | **Parisian luxury** | 35–55, aspirational, brand-literate, Madrid/Barcelona | €69–99 | Black-and-white film grain, Rive Gauche apartments, trench coats, cigarettes-and-espresso, Jane Birkin references | "The scarf a Parisian woman has owned for fifteen years" | **Highest CVR potential, worst defensibility.** You will be competing on the home turf of actual French brands with actual French provenance. Strong for Spain, fatal for France |
| **2** | **★ Mediterranean elegance** | 30–55, Spanish and Southern European, warm-climate, "effortless" self-image | **€49–79** | Golden light, whitewashed walls, olive and terracotta palette, linen, Seville/Cádiz/Mallorca coastlines, sea wind | "Made for the light of the South. Silk that moves the way the air does here." Seville-designed, Bursa-woven — **two Mediterranean cultures, one accessory** | **★ Recommended.** Geographically true (you are in Seville), it makes Türkiye *coherent* rather than awkward (both are Mediterranean textile cultures), it is uncrowded, and lightweight product fits Spain's actual climate. **It also localises you in a way a French brand cannot copy** |
| **3** | **Modern minimalist** | 28–42, urban professional, Madrid/Barcelona/Paris | €49–69 | Editorial white space, single-model, muted palette, Helvetica-adjacent type, COS/ARKET visual grammar | "One scarf. Five ways. No noise." | Safe, scalable, cheap to produce, converts well on Meta — and **completely undefensible.** ARKET does this at €39 with real trust. Use it as a *creative style within* direction 2, not as the brand |
| **4** | **Old-money feminine / quiet luxury** | 40–60, high income, País Vasco / Madrid / Marbella | €79–139 | Equestrian motifs, monograms, stables, libraries, vintage cars, deep greens and burgundies, no logos | "Understatement is the only status worth having" | **Best margins, smallest reachable market, slowest to build.** The "quiet luxury" aesthetic has been heavily worked since 2023. Good for a Q4 gift-set SKU at €89–139; too narrow as the whole brand |
| **5** | **Artisan European** | 35–60, values-driven, anti-fast-fashion | €59–99 | Hands, looms, dye vats, imperfection as proof, long-form video, named makers | "Eight minutes of hand-stitching per hem. We'll show you." | **Strongest trust-building and the best fit for your VSL skill.** Weaker on scroll-stopping hook power. **Use as the proof layer under direction 2** |

**Recommended stack: Mediterranean elegance (2) as brand identity + Artisan European (5) as the proof layer + Modern minimalist (3) as the product-page visual grammar.** That combination is true, uncrowded, defensible against French competitors, and makes Turkish sourcing an asset instead of a confession.

## 10.3 Positioning language to use and to avoid

| Use | Avoid | Why |
|---|---|---|
| "Woven in Bursa" | "Made in Turkey" | Specific > generic; city names read as craft, country names read as manufacturing |
| "Hand-rolled hem" | "High quality" | A verifiable detail beats an unverifiable adjective |
| "Designed in Seville" | "European design" | Concrete place, and it's true |
| "Silk-touch modal" or the true fibre name | "Silk-like", "satin feel" | EU labelling law requires truthful fibre names; "silk-like" also signals fake |
| "Limited to 200 per print" | "Limited edition" | Numbered scarcity is credible; vague scarcity isn't |
| "For the light of the South" | "Luxury for less" | Never compete on being cheaper than luxury |
| "€59.90" | "Was €120, now €59.90" | Omnibus Directive prior-price rules are enforced in Spain |

---

# 11. COMPETITOR ANALYSIS

**Verification warning.** I could not open a single storefront — the egress proxy blocked all of them, and Meta Ad Library was unreachable. Every price below is **as reported in search results**, with the date where available. Treat the price column as an *indication of the band the brand plays in*, and re-verify the ten brands marked ★ on their live sites before you set your price ladder. Where I could not get a price at all, I have written "not verified" rather than guessing.

## Tier 1 — Luxury reference points (set the ceiling; you never compete here)

| # | Brand | Country | Product | Material | Price | Positioning | USP | Meta presence |
|---|---|---|---|---|---|---|---|---|
| 1 | **Hermès** ★ | FR | Carré 90 | Silk twill | **€580** (was ~€460 three years prior; +7–10% recent increases, Feb 2025 hike) | The category's cultural definition | Cultural ownership of the silk square; functioning secondary market with auction-house valuation | Minimal paid social; brand-led |
| 2 | Ferragamo | IT | Silk scarves | Silk | €100–300 (entry-luxury band) | Italian heritage luxury | Print archive | Low |
| 3 | Burberry | UK | Scarves | Cashmere/silk | €100–300+ | Heritage check | Iconic pattern | Moderate |
| 4 | Dior | FR | Scarves | Silk | €100–300+ | Couture | Monogram | Low paid |
| 5 | Chanel / Louis Vuitton | FR | Scarves | Silk | €300+ | Investment-grade | — | Low paid |

## Tier 2 — Premium independents (your actual aspiration; study these hardest)

| # | Brand | Country | Product | Material | Price | Positioning | USP | Notes |
|---|---|---|---|---|---|---|---|---|
| 6 | **Petrusse** ★ | FR | Silk 105 / 65 squares, wool scarves | Silk, wool | **$395** (105cm) / **$215** (65cm) ≈ €364/€198 | Made-in-France premium, timeless | Founded 1996; French manufacture; intricate patterns, French heritage | Sells via BeFrenched, BeyondStyle, Printemps — multi-channel, not pure DTC |
| 7 | **Philéone** ★ | FR | Silk scarves, squares, bandanas, hand-painted stoles | Silk, cotton-linen-silk | **€42–95** for scarves; **Emmanuelle €68, Sylvia €68**; hand-painted Alma stole €98; full range €35–190 | **Made-in-France accessible premium** | Textile-first brand (also sells fabric); hand-painted line | **Your single most important comp.** €68 with genuine French manufacture is the number you must beat on presentation, not price |
| 8 | **Le Châle Bleu** ★ | FR | Shawls, scarves | Silk, wool | **€39–169** | French luxury, split-origin | **"Hand-drawn in France, made in Italy"** — the exact split-origin structure you should copy | Proof that a transparent split-origin story supports premium pricing |
| 9 | Fleuron Paris | FR | Silk scarves, headbands | Pure silk | Not verified | Designed and made in France | Headband + scarf crossover | Runs a US storefront — international DTC operation |
| 10 | SOI Paris | FR | Silk scarves | Silk | Not verified | Parisian DTC | Styling-led content | Shopify-pattern site |
| 11 | Soeur | FR | Scarves in "noble materials" | Silk, cashmere, wool | Not verified | Mass-premium French fashion | Full-wardrobe brand; scarf is an accessory line | Strong brand equity; not scarf-specialist |
| 12 | Sézane | FR | Scarves, square scarves | Silk/wool | Not verified | The French DTC benchmark | Community, drop model, Parisian identity | **Study their email/drop mechanics, not their pricing** |
| 13 | **Fio de Martié** ★ | **ES** | Silk squares, bandanas | Italian silk, handmade in Spain | **33×33 cm €16,90; bandanas from €48,90; 70×70 cm and 90×90 cm €94,90**; sale items €89,90 → €29,90 / €74,90; at El Corte Inglés €64,90 → €34,90 | **Spanish premium made-in-Spain** | Fabric/embroidery/label customisation, **also stocked in El Corte Inglés** | **Your closest Spanish comp and your premium-ceiling proof.** A Spanish brand sells a 90×90 silk square at **€94,90** — well above your €59.90 |
| 14 | **Hamzah** ★ | **ES** | Printed silk scarves and foulards, men's + women's | 100% natural silk | Not verified | Spanish artisan | Family of artists/artisans; exclusive designs | Direct Spanish DTC competitor |
| 15 | **Julunggul** ★ | **ES** | Silk foulards, scarves, made-to-measure kimonos | Silk | Not verified | Spanish artisan, made in Spain | Handcrafted, Zaragoza-based, ships all of peninsular Spain + islands | Direct Spanish DTC competitor |
| 16 | Munira | ES | Silk scarves and shawls | Silk | Not verified | Artisan designs | Design-led | Multi-page catalogue = real assortment depth |
| 17 | Elizabetta | IT/US | Women's silk scarves | Italian silk | **$120–250** ≈ €110–230 | "French scarf alternative" | Italian craftsmanship at below-French-luxury price | Positioning playbook worth reading — they market explicitly *against* French brands |
| 18 | Atelier Hoi An | VN/EU | Handcrafted silk | Silk | **Under €100** tier | Artisan authenticity | Direct artisan sourcing | Proof the sub-€100 artisan tier is a recognised segment |
| 19 | Soieries du Mékong | FR/KH | Handwoven silk | Silk | Under €100 tier | Social-enterprise artisan | Cambodian weaving cooperative | The ethical-artisan playbook done well |
| 20 | Como Milano | IT | Silk scarves, shawls | Como silk | Not verified | Italian silk district | Como provenance | Provenance-led |
| 21 | Victoria Ragna | UK | Luxury scarves | Silk | Not verified | Luxury curation | Curated multi-brand | Competes on assortment |
| 22 | MaraSilk / La Caressette | EU | Silk scarves + styling content | Silk | Not verified | Content-led DTC | **Heavy SEO on "silk scarf trends"** | **Study their SEO — they rank on exactly the clusters in §18** |

## Tier 3 — Accessible premium and high-street (where you win or lose the actual sale)

| # | Brand | Country | Price | Positioning | Why it matters to you |
|---|---|---|---|---|---|
| 23 | **Massimo Dutti** ★ | ES (Inditex) | **100% silk printed scarf €29,95**; linen €39,95; range "from €30" | Spanish premium high-street; specialises in cashmere and wool | **The most dangerous competitor in Spain — and the most important correction in this report.** Spanish, trusted, premium-perceived, physically returnable, and selling 100% silk at *half* your hero price. Beat it on proprietary print, gift presentation and styling content — never on price or trust. **Verify this price live first** |
| 24 | **& Other Stories** ★ | SE (H&M) | Cashmere knit and printed silk lines listed on the EUR store; **price unverified** (a first-pass Spanish source gave "cashmere €49") | Accessible premium | If €49 cashmere is real, a €59.90 non-cashmere scarf is a hard sell unless print and presentation clearly differentiate. **Unresolved — verify** |
| 25 | **ARKET** ★ | SE (H&M) | **Cashmere ~£85 (≈€98); printed silk ~£45 (≈€52)** — contradicts the "€39 cashmere" figure from the first pass | Minimalist quality | Softer threat than first stated, but the logic holds: a plain scarf is instantly comparable and you lose. **Your hero must be a proprietary print. Verify EUR pricing** |
| 26 | H&M | SE | Printed **€9.99**, fine-knit **€14.99**, fringed chiffon **€19.99** | Fast fashion | Sets the floor. Anything you price under €35 gets compared here |
| 27 | Zara / Mango | ES | ~€15–40 | Fast fashion premium-look | Volume floor; huge Spanish brand familiarity |
| 28 | Cortefiel | ES | Not verified | Spanish mid-market, foulards + bandanas | Established Spanish accessories assortment |
| 29 | Nice Things Paloma S. | ES | Not verified | Spanish print-led fashion | Print-led is your lane too — study their prints |
| 30 | Falconeri | IT | Not verified | Cashmere/silk specialist | Material-specialist credibility |
| 31 | Bijou Brigitte | DE | Not verified | Accessible accessories chain | Volume accessories retail in Spain |
| 32 | Lollipops / Balaboosté / Foularchic / Duger / Carnaby | FR | Not verified | French accessible-premium and Instagram-native scarf brands. **Foularchic positions as "the scarf specialist"** | The French DTC density problem in one row. Foularchic is a category-specialist DTC — the closest thing to what you'd build, already built, in French |
| 33 | La Casa de la Moda | ES | Not verified | Spanish online scarf retailer | Competes on assortment and price |

## Tier 4 — Marketplaces and channels (the real competitive set)

| # | Channel | Price band | Why it matters |
|---|---|---|---|
| 34 | **El Corte Inglés** | Broad: own-label to Lauren Ralph Lauren, Calvin Klein, Tommy Hilfiger | Spain's department-store authority for foulards. **Also a potential partner** — Fio de Martié is stocked there, which is a template for you at scale |
| 35 | **Amazon.es** | €10–50 mostly | Used by **82% of Spanish online shoppers**. You will be price-compared here whether you list or not |
| 36 | **Etsy** | **Turkish silk scarves €20–113** | **Your direct sourcing arbitrage, already retailed.** Someone is already selling Turkish silk scarves to Europe at €20–113. Read their listings, reviews and photography — it is free market research on exactly your product |
| 37 | **Vinted** | Variable; **21.4% of French online fashion** | In France, pre-owned designer scarves compete directly with your new €59 scarf |
| 38 | **Shein / Temu** | **€9 average** | Took 16% of French online clothing purchases. Sets a floor you must stay far away from |
| 39 | **TikTok Shop** | Italy comparable: **€20–30 average product value** | Live in Spain (Dec 2024) and France (Mar 2025); 100k+ EU sellers; **69.9% of revenue from affiliated creators.** An opportunity for you, and a competitive channel |
| 40 | Stylight / Fashiola / Lyst / Place des Tendances | Aggregators, discounts to −60% | Price-comparison surface; also a cheap traffic source |

## 11.1 What the competitive map actually tells you

1. **The €39–49 cashmere problem is your biggest strategic threat, and it is not from a scarf brand.** ARKET at €39 and & Other Stories at €49 sell real cashmere with Scandinavian trust. **Conclusion: do not build the brand on material quality claims. Build it on proprietary print + presentation + styling guidance.** A print cannot be price-compared.

2. **Spain's premium-scarf DTC field is thin; France's is saturated.** Spain has three or four real artisan DTC players (Fio de Martié, Hamzah, Julunggul, Munira) mostly under-marketed and almost certainly not running sophisticated Meta creative. France has a dozen, plus Hermès, plus Vinted, plus a self-described "scarf specialist" DTC brand. **This corroborates the Spain-first call from §4 independently of the media-cost argument.**

3. **€48.90–€68 is the validated independent-premium band** in both markets (Fio de Martié €48.90 Spain, Philéone €68 France). €59.90 sits precisely in the middle. That is a strong independent confirmation of the §6 recommendation.

4. **Massimo Dutti from €30 is the one you will actually lose sales to in Spain.** Spanish, trusted, premium-looking, physically returnable. You beat it only on print exclusivity, gifting presentation, and styling content — never on price or trust.

5. **Etsy is free competitive intelligence you should exploit this week.** Turkish silk scarves already retail there at €20–113. Read the top listings' photography, copy, reviews and objections. That is your target customer telling you, unprompted, what they care about.

---

# 12. CUSTOMER AVATARS

## Avatar 1 — "Lucía", the urban professional (28–35)

| Attribute | Detail |
|---|---|
| Age / income | 30; €28–40k personal, often dual-income household |
| City | Madrid (Chamberí, Malasaña), Barcelona (Eixample, Gràcia) |
| Lifestyle | Office or hybrid; gym; brunch; 2–3 trips a year; heavy Instagram; follows 5–10 fashion creators |
| Fashion preferences | Zara/Mango base with 2–3 "better" pieces; aspires to Massimo Dutti and COS; wants to look put-together with minimal effort |
| **Objections** | **"I don't know how to wear it and it'll end up in a drawer."** Then: "Is this actually silk or is it polyester with a story?" |
| Purchase triggers | A creator she trusts styling it; "five ways in sixty seconds"; free shipping; Bizum at checkout; seeing it on a body shape like hers |
| Preferred price | **€39–59** (over €69 needs a strong reason) |
| Platforms | Instagram Reels > TikTok > Pinterest |
| **Likely ad angle** | "One scarf, five outfits" / outfit-upgrade transformation |
| **Creative format** | 15–25s vertical, fast styling cuts, trending-adjacent audio, creator-shot look |

## Avatar 2 — "Carmen", the premium fashion buyer (35–45)

| Attribute | Detail |
|---|---|
| Age / income | 40; €45–70k household, professional or business owner |
| City | Madrid, Barcelona, Bilbao, Valencia, Seville |
| Lifestyle | Established career, kids 5–12, time-poor and money-less-poor; values quality over quantity; buys fewer, better pieces |
| Fashion preferences | Massimo Dutti, COS, Sandro, Uterqüe-heritage taste; owns one designer bag; cares about fabric composition and will read the label |
| **Objections** | **"€60 for an unknown brand?"** "Where is it made?" "Can I return it easily?" |
| Purchase triggers | Fabric and construction detail (momme weight, hand-rolled hem); founder legitimacy; reviews with photos; Spanish returns address; a named designer |
| Preferred price | **€59–89** — she is the reason the hero price works |
| Platforms | Instagram feed + Stories, Facebook, Google search on the brand name before buying |
| **Likely ad angle** | Material/craft quality + "luxury look without the luxury price" + founder story |
| **Creative format** | 30–60s craft film (loom, hands, hem), macro fabric texture, calm pacing, subtitled voiceover — **your VSL skill, downsized** |

## Avatar 3 — "Pilar", the elegant classic buyer (45–60)

| Attribute | Detail |
|---|---|
| Age / income | 52; €50–90k household, often highest disposable income of the five |
| City | Madrid (Salamanca), Bilbao, San Sebastián, Seville, Marbella, Palma |
| Lifestyle | Kids grown or leaving; social calendar (lunches, weddings, theatre); travels; may already own a Hermès carré or want one |
| Fashion preferences | Classic, quality-first, colour-confident; El Corte Inglés and Massimo Dutti are her default; brand-loyal once won |
| **Objections** | "Is it real silk?" "Will the colour run?" "Will it look cheap in person?" Photo-quality scepticism is high |
| Purchase triggers | **Perceived heirloom quality**; gift box; phone support or WhatsApp; a clear returns policy; classic prints (equestrian, baroque, florals); size cues (90cm) |
| Preferred price | **€69–139** — she buys the gift sets and the shawls |
| Platforms | Facebook > Instagram feed; WhatsApp; email is **highly effective** for her |
| **Likely ad angle** | Timeless elegance / old-money quiet luxury / "the one accessory that upgrades everything" |
| **Creative format** | Static editorial images + carousels, longer-form Facebook video, long-copy landing page, email |

## Avatar 4 — "Álvaro", the gift buyer (30–55, male)

| Attribute | Detail |
|---|---|
| Age / income | 42; buying for partner, mother, sister, mother-in-law |
| City | Anywhere urban |
| Lifestyle | Not a fashion shopper. **Terrified of choosing wrong.** Buys in a 20-minute window under deadline pressure |
| Fashion preferences | None of his own. Needs to be told what is safe and correct |
| **Objections** | **"What if she doesn't like it?"** "What if it's the wrong colour?" "Will it arrive on time?" |
| Purchase triggers | **"Best-selling colour"** designation; pre-wrapped gift box; free returns/exchange; guaranteed delivery date; gift message card; a "no wrong answer" framing |
| Preferred price | **€59–99** — he *spends more than women do on the same product* because price signals care |
| Platforms | Instagram, Facebook, **Google search ("regalo mujer elegante", "regalo para mi madre")** — the most search-driven of the five |
| **Likely ad angle** | "The gift she won't return" / one-size-fits-all / pre-wrapped |
| **Creative format** | Unboxing the gift box, packaging-first, hard offer overlay, short and literal. **Also the best Google Search target** |

## Avatar 5 — "Marta", the Christmas / Reyes buyer (25–60)

| Attribute | Detail |
|---|---|
| Age / income | Any; the same women above in a different mode, plus male gifters |
| City | All Spain |
| Lifestyle | Buying 5–9 gifts across a 6-week window on a fixed budget (€370 gifts of €796 total festive spend) |
| Fashion preferences | Secondary — the *recipient's* taste is what matters |
| **Objections** | **"Will it arrive before the 24th / before the 5th?"** "Is it wrapped?" "Can they exchange it in January?" |
| Purchase triggers | **Delivery-date guarantee**, gift wrapping, extended January returns, multi-buy ("3 gifts sorted"), price-tier navigation ("gifts under €60") |
| Preferred price | **€39–79 per gift**, but **buys 2–3 at once** — she is your highest-AOV customer |
| Platforms | Instagram, Facebook, Google, WhatsApp forwarding |
| **Likely ad angle** | "Three gifts, one order, wrapped" / Reyes countdown / extended-returns reassurance |
| **Creative format** | Gift-guide carousel, countdown urgency, multi-product flat-lay, **a Reyes-specific creative set nobody else will run** |

**How to use these:** Avatars 2 and 3 (Carmen, Pilar) justify the €59–89 price and are where the money is. Avatar 1 (Lucía) gives you cheap reach and the styling-content engine. Avatars 4 and 5 (Álvaro, Marta) are **the Q4 business** and require completely different creative — packaging, delivery dates, reassurance — which almost no competitor will bother producing.

---

# 13. THIRTY-TWO CREATIVE ANGLES

Each angle: **Hook → Visual → Body → CTA.** Written in English per your working standard; translate to Spanish for production (I've noted the Spanish hook where the idiom matters). Format noted in brackets.

## Versatility cluster (the core of the business — solves the drawer objection)

**1. One scarf, five outfits** *[15–25s vertical]*
- **Hook:** "One scarf. Five outfits. Sixty seconds." / *"Un pañuelo. Cinco looks."*
- **Visual:** Hard cut every 3s: neck knot → hair → bag handle → belt → shoulder drape. Same woman, same jeans, five transformations.
- **Body:** "Most women buy a scarf and wear it one way. Here's what it's actually for."
- **CTA:** "Shop the print — five ways included in the box."

**2. The outfit was fine. Then this.** *[10s]*
- **Hook:** "Your outfit isn't boring. It's just unfinished."
- **Visual:** Plain white tee + jeans, static, flat. Scarf enters frame. Snap cut to the completed look.
- **Body:** "The difference between dressed and put-together is one accessory."
- **CTA:** "Finish the outfit — €59.90."

**3. Three knots your mother never taught you** *[30s tutorial]*
- **Hook:** "Three knots. Two minutes. You'll use the second one every day."
- **Visual:** Overhead hands-only, slow, clean, numbered captions.
- **Body:** "The Parisian, the Loose Drape, the Bag Twist."
- **CTA:** "Print + illustrated knot card, in the box."

**4. Same scarf, Monday to Friday** *[20s]*
- **Hook:** "Same scarf. Five days. Nobody noticed."
- **Visual:** Five day-labelled outfits, escalating formality.
- **Body:** "Cost per wear: €12 in week one."
- **CTA:** "Start with one."

**5. The €12-per-wear accessory** *[15s, static + text]*
- **Hook:** "€59.90 ÷ 5 wears = €12. And you'll wear it 50 times."
- **Visual:** Typographic, clean, one product shot.
- **Body:** Value-math framing against a €40 top worn twice.
- **CTA:** "Do the maths. Then get the print."

## Transformation cluster

**6. Before / after, no clothes changed** *[8s]*
- **Hook:** Split-screen, no words for 2 seconds.
- **Visual:** Left: plain. Right: identical outfit + scarf.
- **Body:** "Nothing changed except this."
- **CTA:** "See the prints."

**7. The airport test** *[20s]*
- **Hook:** "How to look expensive on a 6am flight."
- **Visual:** Hoodie + leggings + scarf + sunglasses. Terminal, trolley, coffee.
- **Body:** "Travel clothes plus one silk accessory reads as intentional, not lazy."
- **CTA:** "Travel-ready — 70g, folds into nothing."

**8. From school run to dinner in one move** *[20s]*
- **Hook:** "8am school run. 8pm dinner. One change."
- **Visual:** Same outfit, scarf repositioned from bag to neck, lighting shifts.
- **Body:** For Carmen. Time-poor, not taste-poor.
- **CTA:** "One accessory, two lives."

## Luxury-adjacency cluster

**9. The €580 scarf and the €59 scarf** *[15s]*
- **Hook:** "One of these costs €580."
- **Visual:** Two scarves side by side on a marble surface, macro on hems.
- **Body:** "Both hand-rolled hems. Both silk-weight drape. One has a logo." *(Verify your own hem and fibre claims before running this — and never name Hermès.)*
- **CTA:** "Choose the one nobody can price."

**10. Luxury look, no logo** *[20s]*
- **Hook:** "The women who look most expensive wear the fewest logos."
- **Visual:** Old-money aesthetic: stables, library, camel coat, no branding visible.
- **Body:** Quiet-luxury framing.
- **CTA:** "Understatement, €59.90."

**11. What the print actually costs to make** *[45s]*
- **Hook:** "Why a €59 scarf and a €500 scarf cost the same to produce."
- **Visual:** Loom, screen-printing, hand-hemming, then a retail markup diagram.
- **Body:** Transparency play. Cost breakdown minus the retail and marketing markup.
- **CTA:** "Buy the product, not the markup."

## Origin / craft cluster

**12. Bursa, the silk city** *[45–60s]*
- **Hook:** "There's a city in Türkiye that's been weaving silk for 600 years. You've never heard of it."
- **Visual:** Looms, morning light through a workshop window, hands, mulberry leaves.
- **Body:** Bursa's silk-road history; four generations on the same looms; hem stitched by hand.
- **CTA:** "Woven in Bursa. Designed in Seville."

**13. Eight minutes per hem** *[30s ASMR]*
- **Hook:** "Eight minutes of hand-stitching. Per scarf."
- **Visual:** Extreme macro, needle rolling the hem, natural sound only.
- **Body:** "A machine hem takes nine seconds. You can feel the difference on your neck."
- **CTA:** "Feel the difference."

**14. Designed in Seville, woven in Bursa** *[20s]*
- **Hook:** "Two Mediterranean cities. One scarf."
- **Visual:** Split: Seville light, white walls, orange trees / Bursa looms, silk thread.
- **Body:** The split-origin story told as an asset.
- **CTA:** "Meet the collection."

**15. Founder story: I spent nine years making other people's ads** *[60s talking head]*
- **Hook:** "For nine years I made adverts for other people's products. Then I made my own."
- **Visual:** You, real, unpolished, holding the scarf. Seville light.
- **Body:** Why accessories, why Türkiye, what you refused to compromise. Naming the price honestly.
- **CTA:** "This is the first collection. 200 per print."
- *(This will likely be one of your top three performers. Founder-face video from someone with genuine production skill is rare in this category.)*

## Material / quality cluster

**16. The wrinkle test** *[12s]*
- **Hook:** "If your scarf does this, it isn't worth €60."
- **Visual:** Crush a cheap scarf → creases stay. Crush yours → falls smooth.
- **Body:** Drape and recovery as a quality proof.
- **CTA:** "Test it yourself. 30-day returns."

**17. The water test** *[12s]*
- **Hook:** "Real dye doesn't run."
- **Visual:** Water dropped on the print; colour holds.
- **Body:** Colourfastness — Pilar's actual objection, answered visually.
- **CTA:** "Shop with confidence."

**18. Grams matter** *[15s]*
- **Hook:** "70 grams. That's the whole scarf."
- **Visual:** Scarf on a kitchen scale, then pulled through a wedding ring.
- **Body:** Weight and fineness as proof of quality.
- **CTA:** "Lighter than your phone."

**19. Why it doesn't itch** *[15s]*
- **Hook:** "If a scarf itches, it's the wrong scarf."
- **Visual:** Neck close-ups, skin contact, comfort.
- **Body:** Fibre and finish explanation.
- **CTA:** "Wear it against your skin."

## Gifting cluster (the Q4 engine)

**20. The gift she won't return** *[20s]*
- **Hook:** "One size. Every woman. No returns."
- **Visual:** Male hands choosing, then a woman opening the box.
- **Body:** "No size to get wrong. No style to guess. Comes wrapped."
- **CTA:** "Order by 19 December."

**21. Unboxing, no narration** *[20s ASMR]*
- **Hook:** Ribbon pull, first three seconds, no words.
- **Visual:** Rigid box → tissue → scarf → knot card. Sound-forward.
- **Body:** Silent. Text overlay only: "Arrives like this."
- **CTA:** "Gift-wrapped as standard."

**22. For my mother** *[30s]*
- **Hook:** "My mother has everything. She kept this."
- **Visual:** Real intergenerational moment, warm, unstaged.
- **Body:** Emotional gifting, not product features.
- **CTA:** "A gift she'll keep."

**23. For my daughter** *[25s]*
- **Hook:** "The first proper thing I ever bought her."
- **Visual:** Younger woman receiving, older woman watching.
- **Body:** Rite-of-passage framing; heirloom language.
- **CTA:** "Start the collection."

**24. Three gifts, one order** *[20s]*
- **Hook:** "Mother. Sister. Mother-in-law. One order."
- **Visual:** Three boxes, three prints, one basket.
- **Body:** Multi-gift efficiency. **This is the AOV creative.**
- **CTA:** "Three gifts, wrapped, €149.90."

**25. Reyes countdown** *[15s, 2–5 January only]*
- **Hook:** "Still nothing for Reyes? You have until Sunday."
- **Visual:** Calendar, 5 January circled, 24h-delivery badge.
- **Body:** "In stock in Spain. Delivered tomorrow."
- **CTA:** "Order by 4 January, 14:00."
- *(Almost no competitor runs this. CPMs collapse after 26 December.)*

## Aesthetic / identity cluster

**26. The French-girl scarf** *[15s]*
- **Hook:** "Why French women always look finished."
- **Visual:** Black-and-white, café, trench, effortless knot.
- **Body:** Aesthetic-aspiration angle.
- **CTA:** "One knot. That's the whole secret."

**27. Mediterranean light** *[20s]*
- **Hook:** "Silk was made for this light."
- **Visual:** Golden hour, whitewashed walls, sea wind moving the fabric.
- **Body:** The brand's core positioning, as a mood film.
- **CTA:** "Made for the South."

**28. Capsule wardrobe maths** *[25s]*
- **Hook:** "Five clothes, three scarves, fifteen outfits."
- **Visual:** Grid animation showing combinations multiplying.
- **Body:** Combinatorial value — buy fewer clothes, add accessories.
- **CTA:** "Multiply your wardrobe."

**29. Street style, Madrid** *[20s]*
- **Hook:** "We asked five women in Salamanca to tie it their way."
- **Visual:** Real street interviews, five different knots.
- **Body:** Social proof plus styling education in one asset.
- **CTA:** "Find your knot."

**30. Colour of the season** *[15s]*
- **Hook:** "Jade. Burgundy. Deep blue. Pick one."
- **Visual:** Three prints rotating, colour-blocked frames.
- **Body:** Ties to documented 2026 colour direction (intense red, deep blue, jade green).
- **CTA:** "Three colourways. 200 each."

## Scarcity / offer cluster

**31. 200 per print** *[12s]*
- **Hook:** "We printed 200. Then the screen is destroyed."
- **Visual:** Numbered label macro, then the screen being broken.
- **Body:** Credible, numbered scarcity — not vague "limited edition."
- **CTA:** "Number 47 of 200 is still available."

**32. The second one is half the shipping** *[10s, post-purchase upsell]*
- **Hook:** "Add a second print for €44.90."
- **Visual:** Two scarves, one box, one parcel.
- **Body:** Bundle logic stated plainly. Runs as a one-click post-purchase offer.
- **CTA:** "Add to my order."

**Production plan:** at 32 angles you have **the semantic diversity Andromeda rewards** — these are distinct concepts, not variants, so they won't collapse into one Entity ID. Produce 15 for launch (all of cluster 1 + 2, plus 12, 15, 20, 21, 24, 31), then add 8–10 new concepts monthly. That cadence is what earns the 1.8x ROAS multiple from §9.2.

---

# 14. Q4 2026 STRATEGY

## 14.1 The Spanish Q4 calendar — and why it's 3 weeks longer than everyone else's

| Period | Objective | Offer | Product focus | Creative angle | Budget share | Audience | Messaging | Urgency | Landing page |
|---|---|---|---|---|---|---|---|---|---|
| **September** (pre-season) | **Learn cheaply.** Establish the CTR×CVR gate, build the pixel, seed the email list | No discount. Free shipping over €50 | Hero single scarf only | Versatility (1–5), craft (12–15) | **20%** | Broad cold, women 25–60, ES excl. islands | "One scarf, five outfits" | None — this is the clean-read month | Product page, styling video above fold |
| **October** (build) | **Acquire at pre-inflation CPMs.** Build retargeting pools and email list to 3,000+ | Free shipping over €50 + knot card. **Early gift-guide launch** | Hero + twilly + first gift set | Add gifting (20–24), aesthetic (26–30) | **25%** | Cold + 1% lookalikes of purchasers + email capture | "The gift list starts now" | Soft: "New print, 200 made" | Collection page + "Gifts under €70" page |
| **Early November** (1–20) | **Scale what works.** This is your real profit window | **VIP early access**, not discount. Email/SMS-gated | Full ladder: single / gift set / collection | Best 8 performers scaled + 24, 31 | **15%** | Scale winners, expand lookalikes to 2–3% | "Early access before Black Friday" | "VIP window closes Thursday" | Gated VIP page + gift guide |
| **Black Friday week** (23–29 Nov) | **Harvest, don't buy.** CPMs hit 2–3x baseline | **No percentage discount.** See §14.2 | Gift sets and bundles only | 20, 21, 24, 31 | **10%** *(deliberately low)* | **Retargeting + email + SMS first.** Minimal cold | "Not a sale. A bundle." | Hard: "Bundle pricing ends Monday" | Dedicated BF bundle page |
| **Cyber Monday** (30 Nov) | Convert the hesitaters | Free gift box + free shipping, all orders | Bundles | 24, 32 | 3% | Retargeting, cart abandoners | "Last day for free gift wrapping" | Hard | Same BF page, countdown |
| **December 1–18** (peak) | **Maximum revenue. Delivery certainty is the whole message** | Gift wrapping free + guaranteed delivery + **extended returns to 15 January** | Gift sets, 3-gift bundle | 20, 21, 22, 23, 24 | **20%** | Cold + retargeting + email. Add Google Shopping heavily | "Order by the 19th. Arrives wrapped." | **Delivery deadline countdown** | Gift guide by price tier and by recipient |
| **December 19–24** (last-minute) | Capture the panic buyer | **Digital gift card** + express delivery | Gift cards + in-stock hero | 20, 25 | 3% | Retargeting + search only. **Cut cold Meta** | "Too late to ship. Not too late to give." | Extreme | Gift-card page |
| **December 26–31** (the gap) | **Self-purchase + Reyes pre-build at collapsed CPMs** | "Treat yourself" framing; no discount needed | Hero single, full-price | 2, 5, 27, 28 | 2% | Cold — **CPMs are cheapest of the quarter here** | "You bought for everyone else" | None | Product page |
| **January 2–5** (**Reyes**) | **The edge nobody works.** €192/person on Reyes gifts vs €178 Christmas Eve | 24h delivery guarantee (domestic stock) | Gift sets | **25** (Reyes countdown) | **2%** | Retargeting + cold; near-zero competition | "In stock in Spain. Tomorrow." | **Extreme: "Order by 4 Jan, 14:00"** | Reyes landing page |
| **January 7–31** (retain) | Convert buyers into a list, not a one-off | New print drop for existing customers; returns → exchanges | New colourway | 30, 31 | Residual | **Email/SMS to the Q4 buyer base.** No paid | "First look, for people who already own one" | Soft scarcity | Members page |

**Budget note:** the deliberate asymmetry is to spend **45% of Q4 media in September–October**, before the +41% November CPM inflation, and only 13% in the BFCM window. Most brands do the opposite and buy their customers at the most expensive moment of the year.

## 14.2 Should a premium brand discount on Black Friday?

**No. And the data supports the decision rather than just brand instinct.**

The argument against discounting:
- **You cannot afford it.** At €59.90 your max CAC is €27.18. A 20% discount cuts contribution from €31.56 to **€22.00**, dropping your CAC ceiling to about €18 — at the exact moment CPMs are 2–3x baseline. You would be halving your acquisition budget when media is at its most expensive. That is the arithmetic of a brand going backwards.
- **A first-year premium brand cannot recover from a discount anchor.** Your price *is* your quality claim. You have no heritage, no press, no review wall. Discount in week one of the brand's life and €47.90 becomes the real price forever.
- **The Spanish shopper isn't only discount-driven.** Free shipping is the **#1 store-choice driver at ~65%**, with fast delivery second at 33%. Both are things you can give away for a euro or two and both outrank a percentage-off in importance.

**What to run instead, ranked by expected contribution:**

| Alternative | Mechanic | Effect on contribution | Verdict |
|---|---|---|---|
| **1. Bundle pricing** | 2 scarves €99.90 (vs €119.80 separate) | Contribution **€54.71**, max CAC **€47.80** — *nearly double* the single-unit ceiling | **★ Primary BF offer.** It looks like a discount, behaves like an AOV increase, and protects the single-unit price |
| **2. Gift set with free rigid box** | Scarf + ring + box at €89.90 | Contribution **€49.00**, max CAC **€42.72** | **★ Secondary.** €3 of packaging buys €15.50 of CAC headroom |
| **3. Free gift with 2+ items** | Free twilly (COGS ~€2.50) over €90 | Costs €2.50, perceived value €24.90 | **★ Highest perceived-value-per-euro tool you have** |
| **4. Free shipping, all orders** | Remove the €50 threshold for BF week | Costs €4.20/order; addresses the #1 Spanish driver | **★ Run it.** Cheap and directly on the biggest stated purchase driver |
| **5. VIP early access** | Email/SMS-gated 48h window before BF | Costs nothing; shifts volume out of peak CPM into cheaper days | **★ Run it.** Best ROI mechanic in the whole quarter |
| **6. Limited edition BF print** | 200 units, numbered, BF-only colourway | Full price, scarcity-driven | **★ Run it.** Full margin plus a reason to act |
| **7. Extended returns to 15 January** | Reassurance for gift buyers | Marginal cost; removes Álvaro's core objection | **★ Run it** |
| **8. Buy 2, get 3rd at 50%** | Tiered quantity break | Contribution ~€64 at €134.90-ish; still above single | Acceptable — a volume break, not a brand discount |
| **9. Percentage off sitewide** | −20/30% | Halves your CAC ceiling in the most expensive media week | **Do not** |

**One nuance:** if the September–October test shows you cannot clear the CTR×CVR gate at full price, that is *not* a signal to discount into BFCM. It is a signal that the offer or the product is wrong, and BFCM will hide the diagnosis while burning the budget.

---

# 15. UPSELL / CROSS-SELL PRODUCT MAP

**Sourcing costs below are estimates.** I could not verify accessory-level supplier pricing — only scarf/shawl pricing (Turkish factory-direct from €1.90/pc, MOQ 10/colour; silk €1.50–2/pc at 1,000pc). Treat the cost column as a planning estimate to be replaced with real supplier quotes.

| # | Product | Est. sourcing cost | Retail | Est. margin % | Ship weight | Perceived value | Cross-sell fit | Bundle potential |
|---|---|---|---|---|---|---|---|---|
| 1 | **Scarf ring (metal)** | €1.50–3.00 | **€19.90–24.90** | **~88%** | **8–15g** | High — solves a real styling problem | **Perfect** | **★★★ The #1 add-on** |
| 2 | **Silk scrunchie** (matching print) | €1.00–2.00 | €14.90–19.90 | ~90% | **5–10g** | High — matching-set logic | Perfect | **★★★ Print-matched set** |
| 3 | **Narrow twilly / bag scarf** | €2.00–3.50 | **€24.90–29.90** | **~88%** | **10–20g** | High — luxury-adjacent format | Perfect | **★★★ Second hero SKU** |
| 4 | **Silk hair ribbon / bandeau** | €1.50–2.50 | €19.90 | ~88% | 8–15g | Medium-high | Perfect | ★★★ |
| 5 | **Scarf clip / magnetic slide** | €1.50–3.00 | €19.90 | ~87% | 10–20g | Medium — needs demonstrating | Very good | ★★ |
| 6 | **Small silk square (45–55cm)** | €3.00–5.00 | **€34.90–39.90** | ~87% | 25–40g | High | Perfect | **★★★ 3-pack of small squares** |
| 7 | **Silk eye mask** | €2.50–4.00 | €29.90 | ~86% | 20–30g | **Very high** — gifting favourite | Good (gift logic) | **★★★ "Silk gift set"** |
| 8 | **Silk pillowcase** | €6.00–10.00 | €49.90–59.90 | ~80% | **150–250g** | Very high | Good (silk logic, not scarf logic) | ★★ Higher-tier gift set |
| 9 | **Rigid gift box (branded)** | €2.00–3.50 | **€6.90** or free over €90 | — | **60–120g** | **Very high per euro** | **Essential, not optional** | **★★★ The AOV unlock** |
| 10 | **Premium gift wrapping + card** | €0.60–1.20 | €4.90 or free | — | 15–30g | High | Essential in Q4 | ★★★ |
| 11 | **Travel / dust pouch (silk or cotton)** | €1.00–2.00 | €12.90 | ~88% | 15–25g | Medium-high | Good | ★★ Bundle filler |
| 12 | **Cosmetic pouch (quilted, print-matched)** | €3.00–5.50 | €34.90 | ~85% | 60–110g | High | Good | ★★★ |
| 13 | **Jewellery travel case** | €4.00–7.00 | €39.90 | ~82% | 100–180g | High | Medium | ★★ |
| 14 | **Brooch / scarf pin** | €2.00–4.00 | €24.90 | ~85% | 10–25g | Medium-high | Very good | ★★ |
| 15 | **Enamel or gold-plated earrings** | €2.00–4.50 | €29.90–34.90 | ~87% | **5–15g** | High | Medium — different category | ★★ Full-look bundle |
| 16 | **Fine chain necklace** | €2.50–5.00 | €34.90 | ~86% | 5–15g | High | Medium | ★★ |
| 17 | **Leather gloves (unlined)** | €8.00–14.00 | €59.90–69.90 | ~78% | **120–200g** | **Very high** | **Excellent winter pairing** | **★★★ Winter gift set** |
| 18 | **Wool/cashmere beanie** | €5.00–9.00 | €39.90–49.90 | ~80% | 80–140g | High | Excellent winter pairing | ★★★ |
| 19 | **Knitted wrist warmers** | €3.50–6.00 | €29.90 | ~82% | 50–90g | Medium | Good | ★★ |
| 20 | **Oversized shawl / stole** | €10.00–16.00 | **€89.90–119.90** | ~80% | **250–400g** | **Very high** — size reads as value | Excellent | **★★★ Premium tier hero** |
| 21 | **Leather card holder** | €4.00–8.00 | €39.90 | ~82% | 30–60g | High | Medium | ★★ |
| 22 | **Silk-lined jewellery roll** | €4.50–8.00 | €44.90 | ~82% | 80–150g | High | Medium | ★★ |
| 23 | **Print-matched fabric-covered notebook** | €2.00–4.00 | €19.90 | ~84% | 150–250g | Medium | Weak — dilutes the brand | ★ Skip |
| 24 | **Scented sachet / drawer sachet** | €0.80–1.80 | €12.90 or **free gift** | ~89% | 15–30g | Medium-high | **Excellent as a free gift** | ★★★ as a giveaway |

## 15.1 The three that actually matter

**Filtered by margin % × cross-sell fit × (1 ÷ ship weight):**

| Rank | Product | Why |
|---|---|---|
| **1** | **Scarf ring, €19.90** | ~88% margin, 8–15g (zero incremental shipping), and it **solves the exact objection that blocks the sale** ("I don't know how to tie it"). It is simultaneously an upsell and a conversion tool. Put it in every gift set |
| **2** | **Narrow twilly, €24.90–29.90** | ~88% margin, 10–20g, luxury-adjacent format, and it works as a **standalone €24.90 entry product, a post-purchase one-click upsell, and a free gift over €90.** Three jobs, one SKU |
| **3** | **Rigid gift box, €6.90 (free over €90)** | Not a margin product — a **behaviour-change product.** €3 of cardboard converts a €59.90 single into an €89.90 gift set, raising your CAC ceiling from €27.18 to €42.72. Highest leverage item on this entire list |

**What to avoid in year one:** pillowcases and jewellery cases (weight and category drift), notebooks (brand dilution), and anything over 250g until you have negotiated parcel rates. Silk eye masks are the one weight-tolerable exception because they gift exceptionally well.

---

# 16. AOV STRATEGY — €40 → €60 → €80

## 16.1 The price architecture

| Tier | Offer | Price | Contribution | Max CAC | Role |
|---|---|---|---|---|---|
| Entry | Twilly / neck scarf | €24.90 | ~€5 | ~€3 | **Never advertised.** Add-on and free-gift only |
| **Core** | **1 × 90cm printed silk-feel square** | **€59.90** | €31.56 | €27.18 | The advertised hero and the price anchor |
| **Step 1** | Scarf + scarf ring | €74.90 | €40.48 | €35.13 | In-cart upsell, one click |
| **★ Step 2** | **Gift set: scarf + ring + rigid box** | **€89.90** | **€49.00** | **€42.72** | **The default-selected option on the product page in Q4** |
| Step 3 | 2-scarf bundle | €99.90 | €54.71 | €47.80 | "Two prints" — self-purchase and 2-gift buyer |
| **★ Step 4** | **Premium collection: 2 scarves + ring + box** | **€139.90** | **€79.97** | **€70.33** | Q4 hero; the "three gifts sorted" order |
| Step 5 | 3-scarf bundle | €134.90 | €73.67 | €64.63 | Multi-gift buyer, Reyes |

## 16.2 The mechanics, in the order you should build them

| # | Mechanic | Implementation | Expected effect | Build effort |
|---|---|---|---|---|
| **1** | **Default-select the gift set** | On the product page, show three options with the **€89.90 gift set pre-selected** and the €59.90 single as the "just the scarf" downgrade | Largest single AOV lever. Defaults dominate choice | **Low — do this first** |
| **2** | **Free shipping threshold at €69** | Just above the hero price, so one add-on clears it. Spanish shoppers rank free shipping #1 (~65%) | Pushes single-buyers into the €74.90 tier | Low |
| **3** | **Show shipping cost on the product page** | **62% of Spanish consumers want shipping cost visible from the PDP**; cart abandonment runs 73.5–74%, and the top trigger is delivery cost appearing at the last screen | Direct CVR gain, not AOV — but CVR is the bigger lever (§6.2) | Low |
| **4** | **One-click post-purchase upsell** | After payment, offer a second print at €44.90 (angle 32). No re-entry of payment details | Typically the single highest-converting offer in a DTC stack. Pure incremental contribution — CAC already paid | Low (app) |
| **5** | **"Complete the look" in-cart** | Ring at €19.90, twilly at €24.90, gift box at €6.90 | Incremental AOV at ~88% margin | Low |
| **6** | **Bundle-builder: "Pick 2, save €20"** | Customer chooses two prints. Choice-based bundles outperform fixed ones | Moves the €99.90 tier | Medium |
| **7** | **Gift-guide navigation by price** | "Gifts under €40 / under €70 / under €100" | Serves Marta's fixed-budget, multi-gift behaviour | Low |
| **8** | **Free gift over €90** | Free scented sachet or twilly (COGS ~€2.50, perceived €12.90–24.90) | Pushes 2-item orders over the line at near-zero cost | Low |
| **9** | **BNPL (Klarna and/or SeQura)** | Klarna reports merchant AOV **+23%** and conversion uplift up to 20%; Klarna FR: 7M users, 57,500 merchants | Meaningful AOV and CVR lift, especially at €89.90+ | Medium |
| **10** | **Bizum at checkout (Spain)** | 20–30% of Spanish customers use Bizum; >100M e-commerce payments in 2025 | Pure CVR — a missing local payment method is a silent conversion tax | **Low — non-negotiable for Spain** |
| **11** | **Print subscription / collector programme** | "New print every quarter, members first" | Raises repeat rate — but per §7.6 don't over-invest here | Medium — later |

## 16.3 Psychological pricing, checked

| Architecture | Psychologically sound? | Reasoning |
|---|---|---|
| 1 scarf €59.90 / 2 for €99.90 | **Yes** | €99.90 vs €119.80 = a visible €19.90 saving that happens to equal exactly one twilly. Round-number barrier (sub-€100) preserved. Strong |
| Gift set €89.90 with a €6.90 box shown as free | **Yes** | The customer prices the box at €6.90, so €89.90 reads as €59.90 + €19.90 ring + free box. The value stack is legible and honest |
| €139.90 collection | **Yes, but** | Above the €100 psychological barrier. Needs the €99.90 tier visible beside it so €139.90 reads as an *upgrade*, not a leap |
| 3 for €134.90 | **Weak** | €134.90 sits awkwardly *below* the €139.90 collection while containing one more scarf. **Fix: move the 3-pack to €149.90** or drop it and push the €139.90 collection instead. Two adjacent offers where the cheaper one contains more product is a confusing ladder |
| Twilly at €24.90 standalone | **No** | Max CAC ~€3. Never advertise it. It is an add-on and a free gift, nothing else |
| €99.90 vs €100 | **Yes** | Stay under three digits. Real effect in this band |

**Recommended final ladder:** **€59.90 / €74.90 / €89.90 (default) / €99.90 / €149.90.** Drop the €134.90 3-pack — it breaks the logic of the ladder.

**Target:** a €59.90 hero with a default-selected €89.90 gift set, a €69 free-shipping threshold, and a post-purchase upsell should land a blended AOV of **€72–82** in Q4. Per §8.3, an AOV in that range is what turns a €29–30 CAC from a loss into a profit.

---

# 17. GOOGLE ADS

## 17.1 What the channel is for

**Google is your profit channel, not your growth channel.** The evidence:

| Metric | Value | Source |
|---|---|---|
| European e-commerce **Shopping CPC** | **€0.29–0.35** (Q3 2025 ~€0.29–0.30; Nov–Dec 2025 spike to €0.34; €0.35 by Mar 2026) | smec Market Observer (panel of €450M annual European retail ad spend) |
| Q4 Shopping CPC inflation | **+25–30%**; Black Friday CPMs +18% YoY | 2025/2026 benchmarks |
| Apparel Google CPC (global) | $1.64 ≈ €1.51 | 2025/2026 benchmarks |
| Apparel/fashion/jewellery avg CPC | $4.31 ≈ €3.97 | 2026 benchmark — **US-weighted; ignore for Europe** |
| YoY European CPC growth | Decelerating from ~13% (late 2025) to ~4% (Q3 2026) | smec |

**At €0.35 CPC and 3% CVR, your CAC is about €11.70.** Against a €27.18 ceiling that is extremely profitable — better than Meta in any scenario I modelled. Worked through in §8's blended view: €5,000 of Google at €0.55 blended CPC and 3% CVR produces ~273 orders at an €18 CAC and a **3.27x ROAS**, against Meta's 0.88x at Q4 CPMs.

**But — and this is the constraint that decides how you use it — search volume for premium scarves in Spain is thin.** "Foulard" is a mature French search behaviour; the Spanish equivalents are lower-volume. **I could not obtain keyword volumes** (no Keyword Planner access from the sandbox). So: Google will likely cap out somewhere in the €1,500–5,000/month range in Spain before you exhaust qualified intent and CPCs climb. It cannot carry the business. It *can* subsidise your blended CAC and make a marginal Meta performance profitable overall.

**Action before you fund it:** pull real volumes for the keyword sets below in Keyword Planner (free with a Google Ads account, 30 minutes). If combined non-branded exact-match volume in Spain is under ~5,000/month, cap Google at €1,500/month and treat it as margin, not growth.

## 17.2 Spanish keyword architecture

| Cluster | Keywords | Intent | Expected CPC | Priority |
|---|---|---|---|---|
| **Gift intent (highest value)** | `regalo mujer elegante`, `regalo para mi madre`, `regalo original mujer`, `regalo mujer 50 años`, `regalo navidad mujer`, `regalo reyes mujer`, `regalos elegantes para mujer` | **Very high — Álvaro** | Medium-high | **★★★ Fund first.** Highest AOV, lowest price sensitivity, and it is the exact avatar Meta struggles to reach |
| **Product + material** | `pañuelo de seda mujer`, `pañuelo seda natural`, `fular de seda mujer`, `pañuelo seda 100%`, `foulard seda mujer` | High | Low-medium | ★★★ Core Search + Shopping |
| **Product + quality/style** | `pañuelo mujer elegante`, `fular elegante mujer`, `bufanda elegante mujer`, `pañuelo estampado mujer`, `pañuelo cuadrado mujer 90x90` | High | Low-medium | ★★★ |
| **Product generic** | `pañuelo mujer`, `fular mujer`, `foulard mujer`, `bufanda mujer`, `chal mujer`, `pashmina mujer` | Medium — mixed intent | Low | ★★ Shopping only; too broad for Search |
| **Occasion / season** | `pañuelo para boda`, `fular para invitada`, `chal para vestido`, `pañuelo primavera`, `bufanda invierno mujer` | High and specific | Low-medium | ★★ Seasonal campaigns |
| **Competitor / conquest** | `pañuelo massimo dutti`, `fular el corte inglés`, `pañuelo seda hermes alternativa`, `pañuelos como hermes` | High | Medium-high | ★ Run small and carefully. Never bid on a trademark in ad copy |
| **Branded (build it)** | `[your brand]`, `[your brand] pañuelos`, `[your brand] opiniones` | Highest CVR | **Very low** | **★★★ Always on.** Defends against aggregator bidding and captures the post-Meta-ad searcher — **a large share of your true Meta conversions will arrive via a branded Google search you must pay a few cents for** |

## 17.3 French keyword architecture (for 2027)

| Cluster | Keywords | Notes |
|---|---|---|
| **Gift intent** | `cadeau femme élégante`, `cadeau femme original`, `cadeau pour ma mère`, `cadeau noël femme`, `idée cadeau femme 50 ans`, `cadeau maman noël` | Same highest-value logic as Spain |
| **Product + material** | `foulard soie femme`, `foulard en soie`, `carré de soie femme`, `écharpe soie femme`, `foulard soie made in France` | **Note that last one** — "made in France" is an active search qualifier in this category. You cannot satisfy it. Exclude it as a negative |
| **Product + style** | `foulard femme élégant`, `foulard imprimé femme`, `carré de soie 90x90`, `étole soie femme`, `châle femme élégant` | Core |
| **Product generic** | `foulard femme`, `écharpe femme`, `châle femme`, `étole femme`, `bandana soie femme` | Shopping only |
| **Occasion** | `foulard mariage invitée`, `étole pour robe de soirée`, `foulard cheveux soie` | `foulard cheveux` is a distinct, strong French behaviour — worth its own product page |
| **Conquest** | `foulard type hermès`, `alternative foulard hermès`, `foulard comme sézane` | Careful, small budget |

## 17.4 Campaign structure

| Campaign | Type | Budget share | Purpose |
|---|---|---|---|
| Brand defence | Search, exact + phrase | 5% | Cheap, near-100% CVR, defends against aggregators |
| **Gift intent** | Search, phrase + exact, **heavy Oct–Dec + 26 Dec–5 Jan** | **30%** | Highest-AOV traffic in the account |
| Product + material/style | Search, phrase + exact | 25% | Core commercial intent |
| **Shopping / PMax with feed** | Shopping first; **PMax only once you have 30+ conversions/month** | **35%** | Shopping CPCs of €0.29–0.35 are the cheapest qualified clicks available to you anywhere |
| Conquest | Search, exact only, low cap | 5% | Test, kill fast if CAC exceeds €30 |

**On Performance Max specifically:** do not start there. PMax needs conversion volume to optimise and will otherwise spend your budget on low-intent Display and YouTube placements. Start with **Standard Shopping plus a tight Search account.** Move to PMax once you are consistently above 30 conversions/month, and even then run it alongside Brand-excluded Search, not instead of it.

**Merchant Center prerequisites:** a GTIN or MPN per variant, correct `product_type` and `google_product_category` taxonomy, and — critically for this category — **accurate `material` and `size` attributes.** Feed quality is the entire game in Shopping, and it is a one-day job that most new brands do badly.

---

# 18. SEO OPPORTUNITY

**Assessment: worth building, will not pay inside the test window.** Realistic timeline to meaningful organic traffic in Spanish fashion accessories is 6–12 months. So SEO is a **Q4 2027** asset that you should start in Q4 2026 because the content doubles as ad creative and email content — which makes its true cost close to zero for you specifically.

**The strategic reason to do it anyway:** MaraSilk and La Caressette already rank on exactly these clusters ("silk scarf trends 2026", "silk scarf colours and prints"). They are proving the traffic exists. And every styling article you write is a script you have already written for a Reel.

## 18.1 Spanish keyword clusters

| Cluster | Target pages | Search intent | Commercial value | Effort |
|---|---|---|---|---|
| **How to wear / styling** | `cómo llevar un pañuelo`, `cómo atar un pañuelo al cuello`, `formas de llevar un fular`, `nudos de pañuelo`, `cómo poner un pañuelo en el pelo`, `cómo llevar pañuelo en el bolso` | Informational, **high-volume evergreen** | **High** — this is the drawer objection at scale, and the traffic converts because it is already product-curious | Medium. **★★★ Start here** |
| **Gift guides** | `regalos para mujer elegante`, `qué regalar a una mujer de 50 años`, `regalos originales para mi madre`, `regalos de navidad para mujer`, `regalos de reyes para mujer` | Commercial investigation | **Very high** — and seasonal, which means you can rank once and harvest every Q4 | Medium. **★★★ Publish by August to rank for December** |
| **Outfit ideas** | `looks con pañuelo`, `outfits con fular`, `cómo combinar un pañuelo estampado`, `pañuelo con abrigo` | Informational | Medium-high | Medium |
| **Material education** | `seda natural vs poliéster`, `qué es la seda de morera`, `cómo lavar un pañuelo de seda`, `cómo cuidar la seda` | Informational | **Medium — but high trust value.** Care content is what Carmen and Pilar read before buying | Low. **★★ Cheap authority** |
| **Style identity** | `estilo francés mujer`, `cómo vestir con estilo parisino`, `estilo mediterráneo`, `armario cápsula mujer` | Informational, aspirational | Medium | Medium |
| **Seasonal / trend** | `tendencias pañuelos 2027`, `colores de temporada`, `accesorios de invierno mujer` | Informational | Medium, refreshes annually | Low once the template exists |
| **Comparison / alternatives** | `alternativas al pañuelo de hermès`, `mejores marcas de pañuelos de seda` | **Commercial, high intent** | **High** | Medium. Be factual — never disparage |

## 18.2 French clusters (2027)

`comment porter un foulard` · `comment nouer un foulard` · `nœuds de foulard` · `foulard dans les cheveux` · `idée cadeau femme élégante` · `cadeau femme 50 ans` · `style parisien femme` · `comment laver un foulard en soie` · `soie naturelle ou polyester` · `tendances foulards 2027` · `alternative foulard hermès`

## 18.3 The content asset that does double duty

Build **one page: "12 ways to tie a scarf" with a 12-part video series.** That single asset is simultaneously:

1. Your highest-value SEO page (targets the top informational cluster)
2. 12 individual Reels/TikToks (creative angles 1, 3, 4, 29)
3. The embedded product-page video that raises CVR — **the lever that matters most per §6.2**
4. A 12-email welcome flow
5. The printed knot card in the box, which drives repeat and referral
6. A Pinterest asset set, where scarf-styling content has genuine long-tail discovery

**This is the highest-leverage content investment in the whole plan, and it plays directly to what you already do.** Build it in week two, before you spend real money on media.

---

# 19. SUPPLY CHAIN

## 19.1 Turkish sourcing landscape

| Supplier | Location | Capability | Pricing (as reported) | MOQ | Private label |
|---|---|---|---|---|---|
| **Hicabistan** | Istanbul | Factory-direct hijab/scarf manufacturer since 2004, ships to 50+ countries | **from €1.90/piece** | **10 pieces per colourway** | **Woven labels, custom embroidery, colour-matched fabrics, branded packaging.** 5–8 day shipping |
| **Woolgold** | Istanbul | Premium handcrafted scarves/shawls for fashion brands; advanced weaving and printing | Not published | Not published | Bulk production, private labelling, global delivery. Cashmere, wool, silk, blends |
| **Alıcıoğlu** | Türkiye | Manufacturer/wholesaler/exporter since 1941; also authorised distributor for other scarf brands | "Competitive wholesale, volume discounts" | **"Flexible"** | **Private label & OEM, custom labelling, exclusive design manufacturing for boutiques** |
| Market generally | Bursa, Istanbul, Denizli, İzmir | — | **FOB $3–4** at 50–100 pc MOQ; **silk €1.50–2/pc at 1,000 pc MOQ** | 50–1,000 depending on supplier | Widely available |
| Reference brands | — | **Armine, Aker** export to 140+ countries from Bursa/Istanbul | — | — | Proof of the manufacturing base's export capability |

**The key operational finding: a 10-piece-per-colourway MOQ with woven labels and branded packaging.** That is an extraordinarily low commitment. It means you can validate **five prints × three colourways = 150 units for roughly €300–800 of product** and still get your own label in it. No Chinese supplier will do that, and no European manufacturer will do it at that price.

**That — not price — is the Turkish advantage, and it is worth more than price.** It converts a product bet into a creative test, which is exactly the kind of bet you are good at.

## 19.2 The cost-advantage problem you need to price in

| Evidence | Figure | Source |
|---|---|---|
| Turkish minimum wage increase | **+249% between 2022 and 2024**, far outpacing competing nations | WWD Sourcing Journal |
| Energy costs | **Doubled** | Turkish Minute |
| Financing | Interest rates **up to 50%** | Turkish Minute |
| Sector damage | **$7bn of lost production, 210,000 jobs lost** in ready-made garments | Kohan Textile Journal / PolyesterTime |
| Exports | Textile and apparel exports **declined through 2025 and into 2026**; factory closures; falling utilisation; layoffs | Multiple trade press |
| Lira | **−8% YTD, −17% over 12 months vs USD** against **32.6% CPI** (May 2026). USD/TRY ~46 | ING, Naga, Trading Economics |
| Policy intent | The central bank deliberately runs **nominal depreciation slower than inflation** to avoid feeding inflation expectations | TCMB framework (via ING) |
| Direct industry assessment | "The continued suppression of exchange rates has further reduced the competitiveness of the Turkish textile sector in global markets" | Turkish textile sector analysis |

**What this means in plain terms: Turkish costs rise in euro terms every year, by design.** Real lira appreciation of roughly 13–15%/year is the arithmetic of 32.6% inflation against 17% nominal depreciation. Your €8 landed cost today is plausibly €10–11 in 2028 at constant specification.

**Three concrete actions:**
1. **Quote and contract in EUR, not TRY.** Push the currency risk to the supplier. They will accept it because they need the order.
2. **Lock 12-month pricing** with a volume commitment, ideally with a price-review clause capped at EU CPI rather than Turkish CPI.
3. **Model the business at €12 landed, not €8.** At €12 landed and €59.90 retail with 10% returns your max CAC is still around €23 — the business survives. If your plan only works at €5 landed, it doesn't work.

## 19.3 Direct-ship from Türkiye vs. inventory in Spain

| Factor | Direct ship from Türkiye | **Inventory in Spain** |
|---|---|---|
| Working capital | **Minimal** — no stock risk | €2,000–6,000 tied up in inventory |
| Delivery time to customer | 5–8 days (Hicabistan states 5–8 to 50+ countries) | **24–48h** domestic (GLS ~24h; SEUR same-day/13:30 options) |
| Shipping cost per order | Variable, higher per unit; international rates | €4.20 negotiated domestic |
| **Customs from 1 July 2026** | **Exposed.** The EU abolished the €150 duty exemption and imposes a **temporary flat €3 per item** (per tariff line, until 1 July 2028), covering ~93% of e-commerce flows into the EU | **Not exposed.** One bulk import, cleared once |
| Whether the EU–Türkiye Customs Union exempts you | **UNRESOLVED.** A.TR certificates give duty-free movement for industrial goods incl. textiles, but A.TR is a *free-circulation* document designed for commercial consignments, not per-parcel B2C. Public guidance does not clearly address the interaction with the new flat fee | Resolved: bulk import with A.TR, duty-free, done |
| VAT mechanism | IOSS (consignments ≤€150 intrinsic value; note intrinsic value excludes separately itemised shipping) | **OSS** — simpler, and you are already registered for Spanish VAT |
| Returns | **Severe problem.** Returning a €59 scarf to Türkiye costs more than the product. You would need a Spanish return address anyway | Trivial — 3PL handles it |
| Free shipping economics | Hard. **Free shipping is the #1 Spanish store-choice driver at ~65%** — you must offer it, and international rates make that painful | Easy at €4.20/parcel |
| Customer trust | **Turkish sender address is visible on the parcel.** Turkey is absent from the countries EU shoppers name as trusted | Spanish sender, Spanish return address |
| Q4/Reyes capability | **Cannot promise a delivery date.** Kills the Álvaro and Marta avatars, which are the Q4 business | **24h delivery on 4 January.** This is the Reyes edge |
| Quality control | Blind — you never see the units | You inspect the batch |
| 3PL cost | — | Pick & pack €1.50–2.50/order; storage €8–45/pallet/month; receiving €20–30/pallet |

**Decision: hold inventory in Spain. This is not close.**

Five independent reasons, any one of which would be sufficient: the 1 July 2026 duty change lands before your launch; you cannot promise Christmas or Reyes delivery dates from Türkiye; free shipping is the #1 purchase driver and is unaffordable internationally; returns are economically impossible; and the parcel itself would announce a country your customers don't name as trusted.

**The right structure:** one air-freight consignment of 300–600 units with an A.TR certificate, cleared once into Spain, held at a Spanish 3PL (or your own flat for the first 200 orders — genuinely viable and saves €1.80/order while you're learning). A 600-unit consignment of 70g scarves is ~45kg — a single air-freight pallet or even a few large boxes. **This is a small, cheap, low-risk logistics operation, which is another reason the category is well chosen.**

## 19.4 Inbound logistics checklist

| Item | Action |
|---|---|
| Origin documentation | **A.TR movement certificate** from the Turkish supplier for every consignment. Validity 4 months. Without it, MFN duty of ~6–12% applies to textiles |
| HS classification | HS **6214** (shawls, scarves, mufflers, mantillas, veils). Confirm the exact subheading against fibre composition with your broker — the subheading differs for silk vs wool vs man-made fibres |
| Customs broker | **Engage a Spanish broker in week one** and get a written opinion on two questions: (a) does the 1 July 2026 flat €3 fee apply to Turkish-origin low-value B2C consignments under the Customs Union, and (b) what documentation do you need for your bulk import |
| Freight | Air freight Istanbul → Madrid/Barcelona. 45kg is a small, cheap shipment |
| Inbound inspection | Check every unit of the first consignment: hem quality, print registration, colour consistency against your approved sample, label attachment |
| Labelling | Fibre composition in Spanish, attached durably, before the units enter the 3PL (§20). Arrange this with the supplier as part of the order — they offer woven labels |
| 3PL | Spanish 3PL with Shopify integration. Ask specifically about returns handling and Q4 cut-off dates |

---

# 20. LEGAL / TAX / E-COMMERCE COMPLIANCE

## 20.1 Spain

| Area | Requirement | Notes |
|---|---|---|
| **VAT** | **21% standard rate** | Register for Spanish VAT. Charge VAT-inclusive prices to consumers — legally required for B2C in the EU |
| **OSS** | Single EU-wide **€10,000 distance-selling threshold**. Below it you may charge your home rate; above it you must charge destination-country VAT and report via **OSS** — one registration, one quarterly return | You will cross €10,000 fast. Register for OSS proactively. From 1 Jan 2025 there is also an optional SME exemption scheme with a €100,000 threshold — ask your accountant whether it applies to your structure |
| **Right of withdrawal** | **14 days** from delivery, no justification needed. Refund within **14 days**, including **the standard outbound delivery cost** | Non-negotiable |
| **Return shipping** | The consumer pays return postage **only if you tell them before purchase.** If you don't, you pay | **Failing to inform properly can extend the withdrawal period from 14 days to up to 12 months.** Get the pre-contractual information right |
| **Textile labelling** | **Reg. (EU) 1007/2011.** Fibre composition on a durable, legible, visible, securely attached label, using only the regulation's approved fibre names, **in Spanish**. "100%", "pure" or "all" only for single-fibre products. Applies to products with ≥80% textile fibres by weight, including fashion accessories | Also applies to products "made available on the market", which includes online sale. Arrange labels with the Turkish supplier |
| **GPSR** | **Reg. (EU) 2023/988, enforceable since 13 Dec 2024.** A non-EU manufacturer must designate an **EU Responsible Person**, whose **name, postal address, email and phone must appear on the product, its packaging, or an accompanying document** | **If your company is EU-established this is largely solved by your own entity.** If you operate from a Turkish entity, you must appoint one. Marketplaces delist non-compliant listings |
| **Textile EPR** | **Draft Royal Decree on textile and footwear waste**, published 23 June 2025, notified to the Commission 27 May 2026, standstill to 28 Aug 2026, **adoption expected 2026**. Producers — explicitly including **online sellers placing products on the Spanish market regardless of establishment** — must register, join a **SCRAP**, and fund collection/reuse/recycling. **No exemption threshold.** Fees weight- and recyclability-based, with fast-fashion practices considered. **The fee must be shown separately on invoices** | **Not yet binding — but likely to bite during your first full year.** Provision €0.20/unit now (my model does) and check status quarterly. The "must be shown separately on invoices" requirement will need an invoicing change |
| **GDPR** | Lawful basis for marketing, privacy policy, DPA with every processor (Shopify, Klaviyo, Meta, 3PL), data-subject request process | Standard. Use a Shopify-native consent app |
| **Cookies** | **AEPD guidance:** consent must be freely given; **reject must be as easy as accept**; no cookie walls without an alternative; no non-essential cookies before consent | Spain's regulator is active on this. A compliant CMP is required before you run the Meta pixel |
| **Invoicing** | Simplified invoice/receipt with seller identification, VAT breakdown, sequential numbering. **Verifactu** e-invoicing obligations are phasing in for Spanish businesses | Ask your Spanish accountant about the Verifactu timeline for your entity type |
| **Distance-selling information duties** | Full trader identity, geographic address, total price incl. taxes and delivery, payment/delivery arrangements, withdrawal right + model form, complaint handling, guarantee | Missing items extend withdrawal rights. Get this page written once, properly |
| **European Accessibility Act** | **Enforceable since 28 June 2025.** E-commerce services must meet accessibility requirements (WCAG 2.1 AA / EN 301 549). **Microenterprise exemption for services: <10 employees AND ≤€2M turnover** | **You will likely qualify for the microenterprise exemption at launch** — but it disappears immediately when you cross either threshold, with no grace period. Build accessibly from the start; retrofitting a store is expensive |
| **Price display** | **Omnibus Directive:** any "was/now" price must reference the genuine lowest price in the prior 30 days | Directly constrains your Black Friday creative. §14.2's bundle strategy avoids the problem entirely |

## 20.2 France — what's different, and it's not trivial

| Area | France-specific requirement | Cost / effort |
|---|---|---|
| **VAT** | **20%** standard rate | Same OSS mechanism |
| **Refashion EPR (textiles)** | Mandatory registration; **a Unique Identification Number (UIN) from ADEME is a prerequisite for selling textiles in France, including via marketplaces**. Eco-contribution ~**€0.58 per clothing item** (2026 simplified rate) | **Hard gate before first sale.** Weeks of lead time |
| **French representative** | **Since 10 July 2026, any EPR-liable producer not established in France must appoint a French representative by written mandate** (Art. L.541-10-9-1, Environmental Code) | **Recurring third-party fee.** This is the single biggest reason France is not a Q4 2026 co-launch |
| **Triman + info-tri** | **Mandatory since 1 Feb 2023** on all clothing, household linen and footwear placed on the French market: the Triman logo plus sorting instructions | **Requires separate label and/or packaging artwork for France.** A physical SKU difference, not just a website change |
| **Textile labelling** | Same Reg. 1007/2011, but **in French** | Second label variant from the supplier |
| **Consumer law** | Same 14-day withdrawal, but French consumers are notably more procedurally rights-aware, and DGCCRF enforcement is active | Your terms need a proper French translation, not a machine one |
| **Payments** | **Cartes Bancaires is ~79% of card share**, with ~85% checkout conversion vs ~75% industry average. Wero is emerging | **Enable CB specifically.** Not enabling it is a silent conversion tax |
| **Language** | French-language site, support, and legal pages are effectively mandatory in practice | Real cost: professional translation, not DeepL |

**Bottom line on France: the compliance stack (UIN + mandated French representative + Triman artwork + French labels + translated legals) costs you money and several weeks *before* you may lawfully sell a single scarf.** Doing that concurrently with a Spanish launch in a Q4 window is how founders lose a quarter. Spain first.

---

# 21. BRAND NAME AND IDENTITY

## 21.1 Naming direction

**Criteria:** pronounceable in Spanish and French; no hard "Turkish brand" read; no Hermès-adjacency (legal risk); `.com` or `.es` available; short enough for a woven label; searchable (not a dictionary word).

| Direction | Logic | Example shapes | Risk |
|---|---|---|---|
| **★ Mediterranean place / light** | True to the positioning; works in ES and FR; warm | *Solaria, Meridia, Cala —, Levantine, Poniente, Mistral, Almeria-adjacent coinages* | Some are taken; check thoroughly |
| **★ Invented Latinate** | Distinctive, ownable, trademarkable, no dictionary competition | *Serilla, Velura, Miralda, Oriela, Lumara* | Requires brand-building to mean anything |
| Founder / atelier | Credible, human, matches your founder-video strength | *Casa —, Atelier —, Maison —* | "Maison" from a non-French brand reads as pretence to French buyers. Avoid if you plan France |
| Craft / material | Immediately category-legible | *Seda —, Trama, Urdimbre, Filatura* | Narrow; hard to extend beyond scarves |
| Two-word evocative | Memorable, ownable | *Sur & Seda, Casa Poniente* | Longer; harder on a label |

**Recommendation: an invented Latinate word of 2–3 syllables, ending in a vowel.** It reads as European premium in both Spanish and French, is trademarkable, has clean domain availability, and does not lock you into scarves only. Check EUIPO for Nice classes 24 (textiles) and 25 (clothing) before buying anything.

**Avoid:** anything containing "Silk", "Luxe", "Premium", "Co.", "Studio", or a Turkish place name in the brand name itself. Bursa belongs in the story, not on the label.

## 21.2 Identity system

| Element | Direction | Reasoning |
|---|---|---|
| **Colour palette** | **Base:** warm off-white (#F5F1EA), deep ink (#1C1C1A). **Accents drawn from your prints:** terracotta, olive, jade, burgundy, deep blue | Warm neutrals read Mediterranean-premium rather than Scandinavian-minimal, which differentiates you from ARKET/COS. Accent colours match the documented 2026 direction (intense red, deep blue, jade green) |
| **Typography** | **Display:** a high-contrast serif with a modern axis (not Didot — too editorial-cliché). **Body:** a neutral humanist sans | Serif = quality claim without cost. Keep to two weights and don't over-design |
| **Photography** | **Two registers, deliberately.** (1) **Editorial:** golden hour, real Andalusian architecture, wind in the fabric, model mid-movement. (2) **Macro craft:** hems, weave, dye, hands. **Minimal flat-lay** | Flat-lay is where most scarf brands lose the sale — it makes a scarf look like a rectangle of fabric. Movement communicates drape, which is the product's actual quality |
| **Packaging** | Kraft or off-white rigid box, tissue, wax-seal sticker, **printed knot card** (the 12 ways), handwritten-style thank-you | Per §15, the box is the AOV unlock. The knot card is the retention and referral device. Total cost ~€3.50 |
| **Website** | Product page with **styling video above the fold**, three-tier option selector with the gift set pre-selected, shipping cost visible on the PDP, review wall with photos, fibre/care/origin in accordions, Bizum + card + PayPal + Klarna | Every one of these maps to a documented Spanish purchase driver or objection |
| **Instagram grid** | 60% styling (how-to), 25% editorial, 15% craft/founder. **Reels-first** | The styling content is both the top-of-funnel and the CVR asset |
| **Tone of voice** | Direct, warm, specific. Numbers not adjectives ("eight minutes per hem", "70 grams", "200 per print"). No "elevate", no "curated", no "effortless chic" | Specificity is how an unknown brand earns belief |

---

# 22. TEST PLAN — €5,000 HARD CAP

## 22.1 Budget allocation (revised from your draft split, with reasoning)

| Line | Your draft | **My recommendation** | Why the change |
|---|---|---|---|
| Product / samples / first inventory | €500 | **€1,500 (30%)** | At a 10-piece-per-colourway MOQ you can get 5 prints × 3 colourways plus a real first consignment of 200–300 units and inspect quality. **Cheap inventory is the whole point of the Turkish supplier — use it.** €500 buys samples but no ability to fulfil a successful test |
| Website | €500 | **€500 (10%)** | Shopify + a good theme + 4 apps (post-purchase upsell, reviews, CMP, Bizum). Do not pay for custom design. You can produce the visual assets yourself |
| Content / creative | €500 | **€500 (10%)** | AI tooling ~€250/mo for two months, plus one real half-day shoot with a model for authenticity anchors. **This is where your advantage shows up as budget you don't need** |
| **Meta Ads** | €3,000 | **€2,000 (40%)** | Enough for a clean read at €80–120/day over ~3 weeks. **Deliberately lower than your draft** — going to €3,000 before the CTR×CVR gate clears just buys a more expensive version of the same answer |
| Google Ads | €500 | **€300 (6%)** | Brand defence + gift-intent Search + Standard Shopping only. Small because you must pull keyword volumes first (§17.1) |
| **Compliance / legal / broker** | €0 | **€200 (4%)** | Customs broker written opinion, GPSR check, Spanish legal pages. **You had this at zero; it is the item most likely to stop the business** |
| **Survey (400 Spanish women)** | €0 | **€0–300** | Optional but high value (§2.4). Fund from the product line if needed |

**Total: €5,000.** The shape of the change: more product, less media. You cannot learn anything from ads if a winning test leaves you unable to ship.

## 22.2 First-30-day KPIs with hard decision rules

Decision hierarchy: **the CTR×CVR gate overrides every other metric.** A beautiful CPM with a failing gate is a failing test.

| KPI | Kill | Optimise | Continue / scale | Notes |
|---|---|---|---|---|
| **★ Link CTR × session CVR** | **< 0.030%** after 15 concepts and 150k impressions | **0.030–0.052%** | **≥ 0.053%** (at €13 CPM, €59.90 AOV) | **This is the test.** Everything below is diagnosis of why |
| CPM | > €25 sustained | €16–25 | < €16 | If CPM is high *and* CTR is good, it's audience/auction. If CPM is high *and* CTR is low, it's creative |
| Link CTR | < 0.8% after 15 concepts | 0.8–1.5% | **> 1.5%** | Your advantage should land here. If you can't beat 1.5% link CTR with 15 concepts, the product or the offer is the problem, not the creative |
| CPC | > €2.00 | €1.00–2.00 | < €1.00 | Derived; watch CTR instead |
| Landing-page view rate (LPV/click) | < 70% | 70–85% | > 85% | Below 70% = a site-speed problem. Fix before spending more |
| **Add-to-cart rate** | < 3% of sessions | 3–7% | **> 7%** | The clearest read on offer strength. Low ATC with good CTR = the price or the product page is wrong |
| Initiate-checkout rate | < 40% of ATC | 40–60% | > 60% | Low = shipping cost surprise or a payment-method gap. **Check Bizum is live** |
| **Session CVR** | < 1.2% | 1.2–2.2% | **> 2.2%** | Fashion benchmark is 2.5–3.1%; Shopify average 1.40%. Below 1.2% is a site problem, not a traffic problem |
| **CAC** | **> €45** | €28–45 | **< €28** | €27.18 is the single-unit ceiling; €42.72 at gift-set AOV |
| **AOV** | < €55 | €55–70 | **> €70** | If AOV is under €55 the gift-set architecture isn't working — fix the default selection before touching ads |
| ROAS (blended) | < 1.4x | 1.4–2.1x | **> 2.14x** | 2.14x is mathematically break-even at this cost stack |
| **Contribution margin (after ads)** | Negative after €2,000 spend | Break-even ±10% | **Positive** | The only metric that is actually real |
| Return rate | > 15% | 10–15% | < 10% | Above 15% means a product/photography mismatch — the photos are over-promising |
| Email capture rate | < 2% of sessions | 2–5% | > 5% | Matters for Q4 — the list is what makes November profitable without cold CPMs |

## 22.3 Test sequencing

| Days | Focus | Spend | Success condition |
|---|---|---|---|
| **1–7** | Store live, 15 creatives loaded, pixel firing, Bizum live, compliance pages done | €0 media | Store can take an order and ship it. Test-order it yourself |
| **8–14** | **Creative read.** €80/day, one campaign, broad, 15 concepts | €560 | **Link CTR > 1.2%** on at least 3 concepts. If nothing beats 1.2%, stop and rebuild creative — don't spend into it |
| **15–24** | **Conversion read.** €100/day, scale the top 5 concepts, default-select the gift set, add the post-purchase upsell | €1,000 | **CTR×CVR ≥ 0.040% and AOV ≥ €65** |
| **25–30** | **Economics read.** €70/day, add Google brand + gift-intent Search | €420 + €300 | **CTR×CVR ≥ 0.053%, CAC < €30, contribution ≈ break-even or better** |
| **Decision point, day 30** | — | ~€2,300 of €5,000 spent | **Gate cleared → fund Q4 and order inventory. Gate missed by <30% → one 30-day rebuild of offer + landing page, not creative. Gate missed by >30% → stop.** You will still have ~€2,700 |

**The most important feature of this plan: it can fail for €2,300 instead of €5,000.** Build the kill gate at day 30 and honour it.

---

# 23. 90-DAY ROADMAP

## Days 1–30: Prove the gate

| Track | Actions |
|---|---|
| **Product** | Order samples: 5 prints × 3 colourways (~150 units, ~€300–800) from 2 suppliers in parallel. Inspect hems, print registration, colour, weight. Pick one supplier. **Place a 250–300 unit first order with woven labels + Spanish fibre-composition labels.** Source scarf rings and rigid boxes |
| **Branding** | Name + EUIPO check (classes 24, 25) + domain. Logo, palette, type. Packaging artwork. **Half-day photo shoot with one model in Seville** — real anchors for AI extension |
| **Website** | Shopify + theme. Product page with styling video above the fold, 3-tier selector with **€89.90 gift set pre-selected**, shipping cost on the PDP, accordions for fibre/care/origin. **Bizum + card + PayPal.** CMP with reject-as-easy-as-accept. Full legal pages. Test order end to end |
| **Creative** | **15 concepts** from §13: all of cluster 1 (1–5), transformation (6–7), craft (12, 13, 15), gifting (20, 21, 24), scarcity (31). Build the **12-ways-to-tie** video series — it is SEO page, Reels, PDP video, email flow and knot card in one |
| **Meta** | 1 campaign, 2 ad sets, 8–15 diverse creatives each, broad + Advantage+, Spain excl. islands, women 25–60. €80–100/day. **Track CTR×CVR daily** |
| **Google** | Merchant Center feed with GTINs, `material` and `size` attributes. Brand defence + gift-intent Search + Standard Shopping. €10/day. **Pull real keyword volumes in Keyword Planner and decide the France Google case** |
| **CRO** | Reviews app from order one. Photo reviews incentivised. Fix anything with LPV rate <85% |
| **Email** | Klaviyo. Welcome flow (12 ways to tie), abandoned cart, browse abandonment, post-purchase. Pop-up offering the styling guide, not a discount |
| **Upsells** | Post-purchase one-click: second print at €44.90. In-cart: ring €19.90, twilly €24.90, gift box €6.90 |
| **Inventory / ops** | Decide 3PL vs self-fulfil (self-fulfil to ~200 orders is fine and saves €1.80/order). **Customs broker written opinion on the 1 July 2026 flat fee and Turkish origin** |
| **Compliance** | Spanish VAT + OSS registration. GPSR Responsible Person confirmed. Fibre labels in Spanish. Withdrawal/returns information written correctly *before* first sale |

**Day 30 gate: CTR×CVR ≥ 0.053%, AOV ≥ €65, CAC < €30.**

## Days 31–60: Prove the offer and buy the inventory

| Track | Actions |
|---|---|
| **Product** | **Reorder 600–1,000 units** across the 2–3 winning prints (only if the gate cleared). Add the twilly SKU. Negotiate **12-month EUR pricing** with a CPI-capped review clause |
| **Branding** | Press/blogger outreach to Spanish fashion media and 10 micro-creators (gifting, not paid). Build the review wall to 25+ with photos |
| **Website** | **Gift guide pages by price tier and by recipient.** Reyes landing page built now, hidden. Speed optimisation. Accessibility pass (you're likely microenterprise-exempt, but build it right) |
| **Creative** | **+10 new concepts.** Test angle 15 (founder story) and angle 12 (Bursa) as long-form — these are your differentiated assets. Begin the styling series as an ongoing content engine |
| **Meta** | Scale winners to €200–300/day if CAC holds. Add lookalikes (1% then 2–3% of purchasers). Build retargeting pools deliberately — they are what make November cheap. **Separate prospecting and retargeting reporting so blended ROAS doesn't flatter you** |
| **Google** | Scale Shopping if CAC < €25. Add occasion keywords. Consider PMax **only** if above 30 conversions/month |
| **CRO** | A/B the default tier selection, the free-shipping threshold (€59 vs €69), and the product-page video position. **Add Klarna or SeQura** (AOV +23% reported) |
| **Email** | Segment by buyer vs browser. Launch a VIP list for the BF early-access window. Target 3,000+ subscribers by day 60 |
| **Upsells** | Launch the €139.90 premium collection. **Fix the ladder: move the 3-pack to €149.90 or drop it** |
| **Inventory / ops** | Move to a Spanish 3PL. Agree Q4 cut-off dates and a returns process **in writing** |

## Days 61–90: Load Q4

| Track | Actions |
|---|---|
| **Product** | **Inventory landed and inspected by 30 September.** Limited-edition BF print produced (200 numbered units). Gift boxes and knot cards in stock at 1.2x forecast |
| **Branding** | Reyes campaign creative built and approved. Gift-wrapping service live. Extended-returns-to-15-January policy published |
| **Website** | Delivery-deadline countdown component. "Gifts under €40/€70/€100" navigation. Reyes page ready to publish 26 December |
| **Creative** | **Complete the gifting cluster (20–25).** Build the Reyes set (angle 25) — almost nobody else will have one. Produce 10 more concepts to hit 35+ total |
| **Meta** | **Front-load October before the +41% November CPM inflation.** VIP early access 1st–20th November. **Cut cold spend hard during BFCM week** and harvest with retargeting + email. Reserve budget for 26 Dec–5 Jan when CPMs collapse |
| **Google** | Scale gift-intent Search hard through October–December. Keep it running 26 Dec–5 Jan for Reyes |
| **CRO** | Delivery-date guarantee prominent. Gift-message field. One-page checkout. Trust badges at checkout (38% of Spanish shoppers still cite payment-security concern) |
| **Email/SMS** | Full Q4 calendar. VIP early access. Delivery-deadline sequence. **Reyes sequence 27 Dec–4 Jan** |
| **Upsells** | "Three gifts, one order" bundle at €149.90. Free twilly over €90 |
| **Inventory / ops** | Reorder lead time confirmed (Türkiye 5–8 days shipping + production). **Do not stock out in the second week of December** — hold a 20% buffer on the hero print |

---

# 24. WORST / BASE / BEST CASE AT SCALE

CAC inflates with spend at an elasticity of 0.15 (CAC rises ~11% per doubling) — a conservative-to-realistic assumption for a narrow category in a single country. Contribution at 65.5% of net revenue, 10% returns.

**Break-even blended ROAS at this cost stack: 2.14x.**

## Worst case — low CTR (1.0%), low CVR (1.0%), €16 CPM, €49.90 AOV

| Ad spend | CAC | Orders | Revenue | ROAS | Contribution | **Net after ads** | Net % of revenue |
|---|---|---|---|---|---|---|---|
| €5,000 | €188 | 27 | €1,325 | 0.27 | €613 | **−€4,387** | −331% |
| €10,000 | €209 | 48 | €2,386 | 0.24 | €1,104 | **−€8,896** | −373% |
| €25,000 | €240 | 104 | €5,199 | 0.21 | €2,405 | **−€22,595** | −435% |
| €50,000 | €266 | 188 | €9,372 | 0.19 | €4,335 | **−€45,665** | −487% |

**Read:** this is a total loss that gets worse with scale. It is also **detectable inside 14 days and €560 of spend** if you watch link CTR. The worst case is not "lose €50,000" — it is "lose €2,300 and stop," provided you honour the day-30 gate.

## Base case — market-average Meta (1.5% CTR, 1.8% CVR, €13 CPM, €59.90 AOV)

| Ad spend | CAC | Orders | Revenue | ROAS | Contribution | **Net after ads** | Net % of revenue |
|---|---|---|---|---|---|---|---|
| €5,000 | €54.71 | 91 | €5,474 | 1.09 | €2,555 | **−€2,445** | −45% |
| €10,000 | €60.71 | 165 | €9,866 | 0.99 | €4,605 | **−€5,395** | −55% |
| €25,000 | €69.65 | 359 | €21,499 | 0.86 | €10,035 | **−€14,965** | −70% |
| €50,000 | €77.28 | 647 | €38,751 | 0.78 | €18,087 | **−€31,913** | −82% |

**Read, and this is the finding that should govern your decision: market-average performance loses roughly 45–50 cents on every euro of revenue, and scaling makes it worse.** There is no volume at which average execution turns profitable. Contrast that with most e-commerce categories, where average execution produces thin profit. **This category demands above-average execution as the price of entry.**

## Best case — strong creative (2.5% CTR, 2.6% CVR, €12 CPM, €72 AOV)

| Ad spend | CAC | Orders | Revenue | ROAS | Contribution | **Net after ads** | Net % of revenue |
|---|---|---|---|---|---|---|---|
| €5,000 | €20.51 | 244 | €17,550 | 3.51 | €8,253 | **+€3,253** | +19% |
| €10,000 | €22.76 | 439 | €31,631 | 3.16 | €14,875 | **+€4,875** | +15% |
| €25,000 | €26.11 | 958 | €68,948 | 2.76 | €32,417 | **+€7,417** | +11% |
| €50,000 | €28.97 | 1,726 | €124,255 | 2.49 | €58,420 | **+€8,420** | +7% |

**Read:** even the best case produces **€8,400 of net contribution on €50,000 of spend** — a profitable business, but a *thin* one, because CAC inflation eats the margin as you scale. Net margin falls from 19% to 7% between €5k and €50k.

**Three implications:**
1. **This is a €100k–300k/year contribution business at realistic scale, not a €1M one** — unless you add markets, add categories, or lift AOV and repeat rate materially beyond what I've modelled.
2. **Repeat purchase and email are where the real money is,** not paid scale. Every order acquired at €21 whose customer buys again at €0 CAC adds €28–34 of pure contribution. The list is the asset.
3. **Q4 concentration is your friend.** Rather than spending €50,000 across a year at declining efficiency, spend €25,000 in Q4 at peak intent and hold spend low the rest of the year. The seasonality is real (Oct and Dec search peaks) and the economics reward concentration.

## Q4 blended view — Base case, €25k Meta + €5k Google

| Channel | Spend | Orders | Revenue | CAC | ROAS |
|---|---|---|---|---|---|
| Meta (at +25% avg Q4 CPM) | €25,000 | 366 | €21,896 | €68.39 | 0.88 |
| **Google** (Shopping + gift-intent Search, €0.55 CPC, 3% CVR) | €5,000 | 273 | €16,336 | **€18.33** | **3.27** |
| **Blended** | **€30,000** | **639** | **€38,232** | **€46.95** | **1.27** |

Contribution €17,848, less €30,000 ad spend, less ~€3,600 of fixed opex = **an operating loss of about €15,750.**

**The lesson in that table:** Google at a €18 CAC is spectacular and Meta at base-case performance is ruinous, and **blending them hides the diagnosis.** A 1.27x blended ROAS looks like "nearly there" and is actually "one channel is excellent and the other is destroying capital." **Report prospecting Meta CAC separately from Google and from retargeting, every week, or you will scale the wrong channel.**

---

# 25. THE MOST IMPORTANT QUESTION

**"Given Kaan's creative production + AI + DTC advertising experience, what is the real advantage that differentiates this business model from a normal e-commerce venture?"**

## 25.1 The wrong answer

The wrong answer — and the one most people in your position give themselves — is *"I can make better ads cheaper, so my CAC will be lower."* That is true, it is worth €33,000–70,000/year of avoided cost and a measured 1.8x ROAS multiple, and **it is not sufficient.** Section 9.2 shows the arithmetic: apply the full measured creative-velocity multiple to the base case and ROAS goes 1.09x → 1.96x, against a 2.14x break-even. Your advantage, deployed at its documented full value against average everything-else, still loses money.

If your entire edge is "better ads," you have a slightly-less-bad version of the base case.

## 25.2 The right answer

Your real advantage is not that you make better ads. It is that **you can run a volume of persuasion experiments that nobody else in this category can afford to run, in a category where the buying objection is informational rather than economic.**

Unpack that in four steps:

**Step 1 — The blocking objection in this category is competence, not price.**
A Spanish woman does not fail to buy a €59 silk scarf because €59 is too much. Her online fashion basket is already just under €70. She fails to buy because *she does not know how to wear it and expects it to sit in a drawer.* That is an **information problem**, and information problems are solved by demonstration.

**Step 2 — Demonstration is expensive for everyone except you.**
Solving it requires producing a large volume of styling demonstrations: different knots, body types, outfits, ages, settings, seasons, occasions. That is 100+ video assets to cover properly. At European market rates of €150–450 per asset, a competitor needs **€15,000–45,000** to build that library, plus 3–6 months of production scheduling. You can build it in a fortnight for the cost of your tooling. **Look at the competitor list in §11: the French and Spanish premium-scarf brands are selling on flat-lay photography and mood films. Not one of them is running a systematic styling-education engine.** That is the gap.

**Step 3 — The demonstration asset raises CVR, which is the single highest-value lever in the model.**
Per §6.2, conversion rate roughly *halves* CAC — a bigger effect than price, COGS or CTR. Most creative advantage gets spent on CTR, which is linear. Yours can be spent on **CVR**, because a styling video is a product-page asset, not just an ad. Move CVR from 1.8% to 2.6% and the base case goes from −€2,445 to profitable at the same CPM and the same CTR.

**Step 4 — And the category's structure lets you keep the gain.**
Scarves have **no sizing**, so the returns that destroy apparel DTC (20–40%, with fit causing ~50% of them) don't apply. Your contribution survives at 64–69% of net revenue. In apparel, a CVR win gets handed straight back at the returns desk. Here you keep it.

## 25.3 Stated as a single sentence

> **The objection that blocks the sale in fashion accessories is "I don't know how to wear it." Solving it requires direct-response video at a volume the category cannot afford. I can produce that volume at ~4% of market cost, it raises conversion rate rather than just click-through, and because accessories have no sizing the returns don't take the gain back.**

That is a real, defensible, and — importantly — **testable** thesis. It is also falsifiable in 30 days for about €2,300, which is exactly what §22 is designed to do.

## 25.4 The system you are actually building

You described the goal as a repeatable system: *Turkish product at high gross margin → European premium brand → AI-assisted creative → Meta → Q4 demand → bundles/upsells → repeat customers.* Here is that system with the weak links named and the compounding parts identified.

| Stage | Compounds? | Strength | The real risk |
|---|---|---|---|
| Turkish sourcing at high gross margin | **No — it erodes.** Turkish costs rise in euro terms by policy design (+249% min wage 2022–24, real lira appreciation) | The **10-piece MOQ** is the genuine asset, not the price. It turns product decisions into cheap creative tests | You build a model that only works at €5 landed. Model €12 |
| European premium brand | **Yes — the strongest compounding asset** | Brand equity, reviews, email list, and press are the only things here that get more valuable while you sleep | Slow to build; one discount cycle in year one damages it permanently |
| AI-assisted creative production | **Yes, but it decays** | Your genuine edge today. Cost advantage of €33–70k/year plus a 1.8x ROAS multiple | **It decays fastest of anything here.** AI creative tooling is commoditising monthly. In 24 months your production-cost edge is mostly gone. **Your edge then is judgement — knowing which angle works — which is the part AI does not give anyone** |
| Meta as primary acquisition | **No — it inflates.** CPMs rose 20% in 2025 alone | High-volume, fast-learning channel that rewards exactly your skill | Rented land. Never the asset |
| Q4 demand concentration | **Structural, repeats annually** | Genuinely excellent: €796/person in Spain, fashion 43% of gift purchases, and **Reyes extends the season to 5 January** | Concentration risk. A bad Q4 is a bad year |
| Bundles / upsells | **Yes, once built** | **The highest-ROI work in the whole plan.** €3 of gift box raises your CAC ceiling from €27 to €43 | Frequently under-built because it isn't fun. Build it before you scale spend |
| Repeat customers | **Yes — but capped** | Email + the knot card + print drops | Per §7.6, even a 35% repeat rate only lifts the CAC ceiling €28→€38. **Don't over-model LTV.** Low-frequency category |

**The three things in that system that actually compound: brand equity, the owned email list, and your judgement about what persuades.** The sourcing advantage erodes, the AI cost advantage decays, and the Meta channel inflates. So if you do this, structure it so that every euro of media spend also buys a subscriber, a review, or a piece of proprietary creative learning — because that is the part you still own in 2029.

## 25.5 The strategic point I'd make against doing this at all

I'll make it once, plainly, because your stated goal is compounding leverage and not just finishing this task.

You currently have two claims on your time: EY Digital, where a partnership percentage has been floated, and a build-to-exit US DTC brand. This scarf venture is a **third** thing, in a **third** market (Spain/France rather than the US), in a **new category** for you, on a **single income**, aimed at a Q4 2026 window that is roughly 12 months out.

The honest observation: **almost everything valuable in this report is transferable to your existing US DTC brand.** The creative-velocity advantage, the CVR-over-CTR insight, the gift-set AOV architecture, the styling-demonstration thesis — none of it is scarf-specific. If your US brand is in *any* category where the blocking objection is informational, the same edge applies at higher AOV, in English, in a market with better CPM-to-AOV ratios and no EPR/Triman/labelling stack.

And the scale ceiling matters: §24's best case is roughly **€8,400 of net contribution on €50,000 of spend.** That is a real business and a poor use of the one scarce resource you have, if the alternative is applying the same insight to an asset you already own.

**So the question worth asking before the test:** is this the highest-leverage place to deploy your creative-velocity advantage, or is it the most *interesting* place? If the answer is that the scarf venture is a way to own equity in something with a European footprint and a different risk profile from both EY and the US brand — that is a legitimate answer and the €5,000 test is a cheap way to buy the information. If the answer is that it seemed like a good arbitrage, the arbitrage is the weakest part of the thesis.

You asked me to tell you if the task was the wrong move before doing it. That is my objection. It does not change the recommendation below, because a €5,000 gated test is cheap and the information is real — but it should change how much of your attention you give it if it clears the gate.

---

# 26. FINAL DECISION FRAMEWORK

| Question | Evidence | Implication |
|---|---|---|
| **Is there demand?** | Spain: 27.4M online shoppers (77% of 16–74s); clothing = 7% of Q4 2025 e-commerce turnover; women = 56.5% of online fashion buyers; female online fashion ticket just under €70. France: clothing online €7.7bn, 30.7% of all clothing consumption. Silk scarves named a top SS26 accessory trend with Oct and Dec search peaks | **Yes.** Demand is not the risk. Your target price sits inside normal Spanish female fashion behaviour |
| **Can we sell premium?** | Validated independent-premium band: Fio de Martié from €48.90 (ES, made in Spain), Philéone €42–95 / €68 typical (FR, made in France), Le Châle Bleu €39–169 (split-origin). Hermès €580 sets the ceiling | **Yes, at €49–79. Not above.** And not on material claims — ARKET sells €39 cashmere. **Premium must rest on proprietary print + presentation + styling guidance** |
| **Can Meta Ads work?** | Market-average (€13 CPM, 1.5% CTR, 1.8% CVR) → €54.71 CAC vs a €27.96 ceiling. Break-even requires **link CTR × CVR ≥ 0.053%** at €59.90 AOV. Creative velocity of 15+ concepts/month is worth a measured 1.8x ROAS | **Only above benchmark.** Average execution loses ~45–50 cents per euro of revenue **and gets worse with scale.** This is the central risk of the venture |
| **Can Google work?** | European e-commerce Shopping CPC **€0.29–0.35** (smec, €450M spend panel) → ~€12–18 CAC at 3% CVR. But I could obtain **no keyword volumes** for Spanish scarf terms | **Yes, and it is the best-economics channel — but volume-capped.** Likely €1,500–5,000/month in Spain. Profit channel, not growth channel. **Pull volumes before funding it** |
| **Can we achieve >€50 AOV?** | Single €59.90 → contribution €31.56. Gift set €89.90 → €49.00 (CAC ceiling €42.72). Premium collection €139.90 → €79.97 (ceiling €70.33). Klarna reports AOV +23% | **Yes, and it is mandatory.** A default-selected gift set plus a post-purchase upsell should deliver €72–82 blended in Q4. **Launching single-SKU caps you at a €27 CAC ceiling and probably fails the test on that alone** |
| **Can margins support paid acquisition?** | 64–69% contribution on net revenue. Max CAC €27.18 (single) to €70.33 (collection). Robust even at €10 COGS and 20% returns (€21.16 ceiling) | **Yes — the cost stack is not the problem.** It is robust to sourcing and returns shocks and fragile only to CAC. **The entire risk lives in one line item** |
| **Is Q4 attractive?** | Spain: €796/person festive spend, €370 gifts, fashion 43% of gift purchases, 8-in-10 use BF for gifts, early buyers +€140. **Reyes €192 > Christmas Eve €178.** Scarf search peaks Oct and Dec. Counterweight: November CPMs +41%, BFCM peak days 2–3x | **Yes — the strongest structural argument for the venture.** But you must buy customers in **September–October**, not in BFCM week |
| **Is Spain attractive?** | Cheaper auction (Spain CPM reported ~€6 all-industry vs Tier-1 $10–23), female fashion ticket brackets your price, thin premium-scarf DTC competition, **no binding textile EPR yet**, 24h domestic delivery, Reyes extension, and you live there | **Yes — first market, unambiguously** |
| **Is France attractive?** | Larger clothing e-commerce (€7.7bn official) and higher Google potential. But: basket **€62 and falling 3%**, fashion basket −4.2%, Vinted at 21.4%, Shein/Temu at 16% of online clothing at €9 average, a dozen DTC scarf competitors incl. Philéone at €68 made-in-France, and a **hard pre-sale compliance gate** (Refashion UIN + mandated French representative since 10 July 2026 + Triman artwork) | **Yes, later, and with a different SKU.** Q2 2027, funded by Spanish profit, hero SKU at €34.90–44.90 in a smaller format because the French are buying **more gifts at lower unit value** (record 9 gifts on a 9-year-low budget) |
| **Is Turkish sourcing advantageous?** | **Advantage:** factory-direct from €1.90/pc, **MOQ 10 pieces per colourway**, woven labels, custom embroidery, branded packaging, 5–8 day transit, Bursa silk heritage. **Against:** min wage +249% (2022–24), energy costs doubled, financing to 50%, $7bn production lost, 210,000 jobs gone, exports falling, real lira appreciation, and total EU imports of HS6214 from Türkiye were only ~US$8.4M in 2025 | **Yes — but for flexibility, not price.** The 10-piece MOQ is worth more than the unit cost. **Model at €12 landed, contract in EUR, lock 12 months.** The "cheap Turkey" premise is out of date |
| **Does my creative advantage matter?** | €33–70k/year of avoided production cost; measured **1.8x median ROAS** at 15+ concepts/month; Andromeda structurally rewards semantic diversity (>60%-similar ads collapse into one Entity ID); hours not weeks of iteration latency; and VSL skill maps onto the category's actual objection | **Yes, materially — and it is not sufficient alone.** Full creative multiple on the base case gets 1.09x → 1.96x against a 2.14x break-even. **You need creative advantage + €65 AOV + 2.5% CVR. Any two of three loses money** |
| **Biggest risk** | Average creative and average conversion produce a **guaranteed** loss that worsens with scale — not a thin profit. Secondary: the **1 July 2026** abolition of the €150 duty exemption with a flat €3/item fee, whose interaction with Turkish-origin goods under the Customs Union is **unresolved in public guidance** | **Mitigate with the day-30 kill gate (fail for €2,300, not €5,000) and by holding inventory in Spain.** Get a written customs-broker opinion in week one |
| **Biggest opportunity** | A category-wide failure to solve the styling-competence objection with video, in a category with **no sizing** (so returns don't eat the gain), during a documented scarf trend, in a market where **Reyes extends Q4 by three weeks** and almost no competitor works that window | **This is the thesis. Build the 12-ways-to-tie engine before you spend real money on media** |

## BUSINESS MODEL

| Field | Answer |
|---|---|
| **Product** | 90cm printed silk-feel square with hand-rolled hem, proprietary print, 2–3 colourways. Second SKU: narrow twilly at €24.90 |
| **Target customer** | Spanish women 32–55, urban, €40k+ household, fashion-interested, buying for themselves Sep–Nov and as gifts Nov–Jan. Plus male gift buyers 35–55 in Q4 (Google-led) |
| **Country** | **Spain only.** France Q2 2027 |
| **Retail price** | **€59.90** hero |
| **Target AOV** | **€72–82** blended (Q4) |
| **Target gross margin** | **64–69% of net revenue** (single to collection) |
| **Target CAC** | **< €28** blended; **< €24** on prospecting Meta |
| **Target contribution margin** | **€28–43 per order**, positive on first order |
| **Primary acquisition** | Meta (Reels/Stories, styling-demonstration creative, 15–20 new concepts/month) |
| **Secondary acquisition** | Google — brand defence + **gift-intent Search** + Standard Shopping. Then TikTok Shop Spain (live since Dec 2024; 69.9% of its revenue is creator-driven, which suits you) |
| **Main upsell** | **Scarf ring at €19.90** (~88% margin, 8–15g) and a post-purchase second print at €44.90 |
| **Main bundle** | **Gift set — scarf + ring + rigid box — €89.90, default-selected on the product page** |
| **Q4 offer** | **No percentage discount.** Bundle pricing + free rigid gift box + VIP early access + free shipping + returns extended to 15 January + a 200-unit numbered limited print |

## GO-TO-MARKET

| Field | Answer |
|---|---|
| **First country** | Spain (excluding Canarias, Ceuta, Melilla) |
| **First product** | One proprietary print, 90cm square, in 3 colourways — one classic (equestrian/baroque), one seasonal (jade or deep blue), one neutral |
| **First price** | €59.90 single / €74.90 with ring / **€89.90 gift set (default)** / €99.90 two-pack / €149.90 collection |
| **First ad budget** | **€2,000 Meta + €300 Google**, over 30 days, inside a €5,000 total cap |
| **First 10 creatives** | (1) One scarf five outfits · (2) The outfit was fine, then this · (3) Three knots your mother never taught you · (6) Before/after no clothes changed · (13) Eight minutes per hem · (15) Founder story · (20) The gift she won't return · (21) Unboxing, no narration · (24) Three gifts one order · (31) 200 per print |
| **First 3 audiences** | (1) Broad / Advantage+, women 25–60, Spain excl. islands — the primary. (2) Interest stack: premium fashion + gifting + Massimo Dutti/COS/Zara-adjacent affinities — the control. (3) Retargeting: video-viewers 50%+, ATC, site visitors 30 days |
| **First landing page** | Product page, not homepage. **Styling video above the fold**, three-tier selector with €89.90 pre-selected, shipping cost visible on the PDP, photo review wall, fibre/care/origin accordions, Bizum + card + PayPal, mobile-first |
| **First offer** | "One scarf. Five ways. Free shipping over €69. Arrives gift-boxed." |

## FINAL RECOMMENDATION

# ➤ TEST FIRST

Not GO, and not NO-GO. Here is the reasoning in full.

**Why not GO.** A GO verdict would require the base case to be profitable. It is not. At market-average Meta performance this business loses roughly 45–50 cents on every euro of revenue, **and the loss widens with scale** — €2,445 on €5,000 of spend, €31,913 on €50,000. That is a materially different risk profile from most e-commerce, where average execution yields thin profit. Your creative advantage is real and measured (1.8x ROAS at 15+ concepts/month, €33–70k/year of avoided cost) and applying it in full to the base case still lands at 1.96x against a 2.14x break-even. **The venture requires above-benchmark performance on three variables simultaneously — creative, conversion rate, and AOV — as the price of entry, not as the path to outperformance.** You cannot responsibly commit capital to that before testing it.

**Why not NO-GO.** Every input other than acquisition efficiency is favourable, and several are strongly so. The cost stack is robust — 64–69% contribution on net revenue, still €21 of CAC headroom at the pessimistic corner of €10 COGS and 20% returns. Returns are structurally low because scarves have no sizing, which is the failure mode that kills most apparel DTC. Your target price sits inside documented Spanish female fashion behaviour (€59.90 against a sub-€70 average ticket) and inside a validated independent-premium band (€48.90 Fio de Martié to €68 Philéone). The category is in a documented fashion trend with Oct and Dec search peaks. Q4 in Spain is exceptional and three weeks longer than everyone else's because of Reyes. Sourcing flexibility is extraordinary — 10 pieces per colourway with your own woven label. Google economics are excellent. And the specific gap you would exploit — nobody in the category is running a systematic styling-demonstration engine — is visible in the competitor set and is precisely what your nine years of work makes cheap for you. **A €5,000 gated test on that thesis is a rational purchase of information.**

**What TEST FIRST means concretely:** €5,000 hard cap, Spain only, one product family, one price ladder with a default-selected gift set, 30 days to the gate, and **a pre-committed kill decision on day 30**:

| Day-30 outcome | Action |
|---|---|
| **link CTR × CVR ≥ 0.053%, AOV ≥ €65, CAC < €30** | **Fund Q4.** Order 600–1,000 units, execute §23 days 31–90, plan €25–30k of Q4 media |
| **Gate missed by less than 30%** (i.e. ≥ 0.037%) | **One 30-day rebuild — of the offer and the landing page, not the creative.** Per §6.2, CVR and AOV are the bigger levers. Then re-gate once |
| **Gate missed by more than 30%** (< 0.037%) | **Stop.** You will have spent ~€2,300, kept ~€2,700, and learned something transferable to your US brand. That is a good outcome for a wrong hypothesis |

**Three conditions on the test, without which the result is not interpretable:**

1. **Launch the AOV architecture on day one.** A single-SKU launch caps your CAC ceiling at €27.18 and will probably fail the gate for reasons that have nothing to do with the thesis. The gift set must be live and default-selected from the first order.
2. **Get the customs-broker opinion in week one.** Specifically: does the **1 July 2026** flat €3/item fee apply to Turkish-origin low-value B2C consignments under the EU–Türkiye Customs Union? Public guidance does not resolve it. If it does apply, direct-ship is dead — which is why the plan warehouses in Spain regardless.
3. **Track `link CTR × session CVR` as one number, daily.** Not ROAS. ROAS blends Google (excellent) with prospecting Meta (the actual question) and will tell you a comforting lie. §24's blended table shows exactly how — a 1.27x blended figure that conceals a 0.88x Meta and a 3.27x Google.

---

# IF I WERE YOU: THE FIRST 14 DAYS

Cost shown is out of the €5,000. Days assume roughly 3–4 focused hours on weekdays alongside EY.

| Day | Action | Cost | Output |
|---|---|---|---|
| **1** | **Kill the cheap-Turkey assumption properly.** Email 5 suppliers (Hicabistan, Woolgold, Alıcıoğlu + 2 from Europages) with one spec: 90×90cm printed square, hand-rolled hem, my artwork, woven label, EUR pricing, 12-month price hold, MOQ 10/colourway. Ask for landed-to-Madrid cost at 150 / 500 / 1,000 units | €0 | 5 quotes in EUR. **If nobody holds a price in EUR for 12 months, that is a finding** |
| **2** | **Customs + compliance, in writing.** Engage a Spanish customs broker. Two questions: (a) the 1 July 2026 flat €3/item fee vs Turkish origin under the Customs Union; (b) documentation for a bulk A.TR import. Separately confirm your GPSR Responsible Person position | €200 | A written answer to the one question that can invalidate the model |
| **3** | **Competitor teardown, live sites.** Open all ten ★ brands in §11. Record: exact price, sizes, materials, shipping cost and threshold, returns policy, payment methods, product-page structure, whether they use styling video. Then read the top 20 Etsy Turkish-silk-scarf listings and **log the objections in the reviews** | €0 | A real price ladder and a verified objection list — replacing my search-sourced estimates |
| **4** | **Pull Google keyword volumes.** Open a Google Ads account. Keyword Planner for all §17.2 clusters, Spain, exact match. Sum non-branded commercial volume | €0 | **The decision on whether Google is a €1,500/month or a €5,000/month channel** |
| **5** | **Design the prints.** 3 print directions: one equestrian/baroque classic, one botanical in the documented 2026 palette (jade/deep blue/intense red), one geometric-Mediterranean. Use your AI image stack. Produce print-ready repeat files | €0 | 3 artwork files — your only real moat (a print cannot be price-compared) |
| **6** | **Name, domain, trademark check.** Invented Latinate, 2–3 syllables, vowel-ending. EUIPO search in Nice classes 24 and 25. Buy the domain and the handles | €50 | The brand exists |
| **7** | **Order samples.** Best 2 suppliers × 3 prints × 2 colourways ≈ 60–120 units. Pay for express. Specify woven label and Spanish fibre-composition label | €600 | Product on its way — and the quality answer |
| **8** | **Build the store skeleton.** Shopify, clean theme, product page structured per §21.2, three-tier selector with **€89.90 pre-selected**, shipping cost on the PDP, Bizum + card + PayPal, CMP with reject-as-easy-as-accept. Install reviews and post-purchase upsell apps | €200 | A store that can take money |
| **9** | **Write the legals properly, once.** Withdrawal rights (14 days, refund incl. standard delivery within 14 days), **who pays return shipping stated pre-purchase**, privacy, cookies, terms, full trader identity and address. Spanish, human-written | €0 | The thing whose absence extends your withdrawal liability to 12 months |
| **10** | **Script the 12 ways to tie.** 12 knots, each a 15–25s vertical: hook, hands-only overhead, numbered caption, result on-body. Write all 12 scripts and the shot list today | €0 | The asset that is simultaneously SEO page, 12 Reels, the PDP video, a 12-email flow and the knot card |
| **11** | **Build 15 launch creatives** from §13 using AI + your existing footage and stills. Genuinely distinct concepts, not variants — Andromeda collapses >60%-similar ads into one Entity ID | €100 | The 15 assets the day-30 gate will be judged on |
| **12** | **Set up measurement.** Meta pixel + CAPI, GA4, a one-line daily sheet: spend, impressions, link clicks, sessions, ATC, orders, revenue, **and `link CTR × CVR` as a single computed cell.** Add the 0.053% threshold as a conditional-format rule | €0 | You will see the answer without interpreting it |
| **13** | **Samples arrive → decide.** Inspect hems, print registration, colour against artwork, weight, hand-feel, label attachment. Photograph properly. **Place the 250–300 unit first order with the winning supplier.** Order rings, rigid boxes, knot cards | €900 | Inventory committed on evidence, not hope |
| **14** | **Launch.** 1 campaign, 2 ad sets, 15 creatives, broad + Advantage+, women 25–60, Spain excl. islands, €80/day. Google: brand defence + gift-intent Search + Standard Shopping, €10/day. Then **do not touch it for 72 hours** | €90/day begins | Live. The clock on the day-30 gate starts |

**Total committed by day 14: ≈ €2,050 of €5,000.** You reach the launch line with roughly €2,950 of runway and a pre-committed kill date.

**What I would deliberately not do in the first 14 days:** hire anyone; build a custom site; do a professional photo shoot before the samples arrive; set up anything for France; register for Refashion; open TikTok Shop; run a discount; or raise the daily budget above €80 before there is a CTR read. Every one of those is a way of spending money to feel like progress before the only question that matters has been answered.

---

## Sources

**Official and industry-body sources**
- CNMC — Spanish e-commerce quarterly data, Q4 2025 ([press note PDF](https://www.cnmc.es/sites/default/files/editor_contenidos/Notas%20de%20prensa/2026/20260703_NP_CE_IV_2025%20(en).pdf)); [2025 total via The Corner](https://thecorner.eu/news-spain/e-commerce-in-spain-exceeds-e114-8-billion-in-2025-up-20-6-per-cent-on-previous-year/126596/)
- [IAB Spain — *Estudio Ecommerce 2025*](https://iabspain.es/estudio/estudio-ecommerce-2025-iab-spain/) (with Elogia)
- INE — [*Encuesta de Presupuestos Familiares* 2025](https://www.ine.es/dyngs/Prensa/EPF2025.htm); [*Atlas de Distribución de Renta de los Hogares*](https://www.ine.es/dyngs/Prensa/ADRH2023.htm); [renta media by comunidad autónoma](https://www.ine.es/jaxiT3/Tabla.htm?t=68338)
- [Modaes — per-person fashion spend 2025](https://www.modaes.com/entorno/el-gasto-en-moda-por-persona-vuelve-a-caer-en-2025-tras-cuatro-anos-de-recuperacion)
- FEVAD — [*Chiffres Clés e-commerce 2025*](https://www.fevad.com/chiffres-cles-ecommerce-2025/); [2025 annual review](https://www.fevad.com/bilan-du-e-commerce-en-france-les-francais-ont-depense-pres-de-200-milliards-deuros-sur-internet-en-2025/); [*Mode et Internet 2025*](https://www.fevad.com/mode-et-internet-en-2025-bilans-et-perspectives/); [average basket](https://www.fevad.com/chiffre-mois-75e/)
- [Républik Retail / Institut Français de la Mode — French fashion market 2025](https://www.republik-retail.fr/strategie-retail/enseignes/pratiques/le-marche-francais-de-la-mode-en-2025-chiffres-cles-et-tendances.html)
- [Cofidis — French Christmas budget 2025](https://www.cofidis.fr/fr/question-de-budget/projets-des-francais/budget-francais-noel-2025.html); [franceinfo coverage](https://www.franceinfo.fr/decouverte/noel/noel-2025-le-budget-des-francais-au-plus-bas-depuis-2017-avec-491-euros-en-moyenne_7601780.html)
- [OCU Christmas spending via Cuatro](https://www.cuatro.com/noticias/economia/20251210/cuanto-gastan-espanoles-navidad-reyes-magos-ganan-papa-noel_18_017823601.html); [Oney Black Friday & Christmas study 2025](https://blog.oney.es/somos-oney/estudio-oney-blackfriday-navidad/); [Emprendedores coverage](https://emprendedores.es/notas-de-prensa/el-black-friday-impulsa-el-gasto-navideno-los-espanoles-gastaran-casi-411e-de-media-en-regalos-segun-oney/); [Retail Actual — Christmas online](https://www.retailactual.com/noticias/20251211/compras-regalos-ultima-hora-navidad); [Ecommerce News ES](https://ecommerce-news.es/el-gasto-medio-online-sera-de-250e-esta-avidad/)
- [DataReportal — Digital 2025: Spain](https://datareportal.com/reports/digital-2025-spain); [NapoleonCat Instagram Spain](https://stats.napoleoncat.com/instagram-users-in-spain/); [Statista — Instagram France by age](https://www.statista.com/statistics/1196396/instagram-users-by-age-france/)

**Legal, tax and customs**
- [European Commission — €3 customs duty for low-value parcels](https://commission.europa.eu/news-and-media/news/ensuring-fairness-and-safety-eur3-customs-duty-low-value-parcels-2026-06-29_en); [Council of the EU, 12 Dec 2025](https://www.consilium.europa.eu/en/press/press-releases/2025/12/12/customs-council-agrees-to-levy-customs-duty-on-small-parcels-as-of-1-july-2026/); [DG TAXUD guidance and legal text, 8 June 2026](https://taxation-customs.ec.europa.eu/news/guidance-and-legal-text-temporary-flat-fee-low-value-imports-which-will-apply-until-1-july-2028-2026-06-08_en)
- [Access2Markets — EU–Türkiye Customs Union](https://trade.ec.europa.eu/access-to-markets/en/content/eus-custom-union-turkey); [DG TAXUD — Türkiye customs unions](https://taxation-customs.ec.europa.eu/turkey-customs-unions-and-preferential-arrangements_en); [A.TR certificate explained](https://www.customssupport.com/atr-certificate-explained/)
- [Regulation (EU) No 1007/2011 — textile fibre names and labelling (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2011/1007/oj/eng); [Commission page](https://single-market-economy.ec.europa.eu/sectors/textiles-ecosystem/regulation-eu-10072011_en)
- GPSR — [EU Responsible Person requirement for non-EU sellers](https://eumandate.com/insights/gpsr-eu-responsible-person); [overview](https://euverify.com/resource/eu-responsible-person-under-gpsr/)
- [Refashion Pro — the legal framework](https://pro.refashion.fr/en/the-legal-framework); [French textile EPR 2025 compliance](https://deutsche-recycling.com/blog/compliance-solutions-for-selling-textiles-in-france/); [Triman & info-tri](https://www.traceforgood.com/ressources/article/french-new-compulsory-triman-label-and-textile-recycling-information); [authorised representative with Refashion](https://ekovio.com/epr-authorized-representative-textiles-france-refashion/)
- Spain textile EPR — [Reconomy on the TRIS notification](https://www.reconomy.com/2026/07/06/spain-textile-epr-decree/); [Valpak on the draft decree](https://www.valpak.co.uk/spain-textile-epr-draft-decree/); [Reverse Logistics Group](https://rev-log.com/spain-proposes-new-epr-rules-for-textiles/)
- [Right of withdrawal — Your Europe (European Commission)](https://europa.eu/youreurope/citizens/consumers/shopping/returns/faq/index_en.htm); [Centro Europeo del Consumidor en España](https://portal-cec.consumo.gob.es/en/informacion-general/compras-online/devoluciones); [Stripe — returns in Spain](https://stripe.com/resources/more/purchase-returns-in-spain)
- [OSS / distance-selling thresholds — Marosa](https://marosavat.com/vat-manual-chapters/e-commerce-european-vat-regulations); [Taxology](https://taxology.co/distance-selling-treshholds/); [IOSS explained](https://crossbordertaxtool.com/en/guide/ioss-explained); [Avalara on the end of the €150 exemption](https://www.avalara.com/blog/en/europe/2025/11/eu-end-150-customs-duty-exemption-2026.html)
- European Accessibility Act — [Bird & Bird guide for online retailers](https://www.twobirds.com/en/insights/2025/a-guide-to-navigating-the-european-accessibility-act-for-online-retailers-service-providers-and-plat); [e-commerce service requirements](https://accessible.org/eaa-ecommerce-services-requirements/); [microenterprise exemption](https://www.xictron.com/en/blog/accessibility-act-exemptions-microenterprises-2026/)

**Advertising benchmarks**
- [Triple Whale — Facebook ad benchmarks by industry](https://www.triplewhale.com/blog/facebook-ads-benchmarks); [e-commerce benchmarks](https://www.triplewhale.com/blog/ecommerce-benchmarks)
- [Facebook Ads benchmarks 2026 (influee aggregation)](https://influee.co/gb/blog/facebook-ads-benchmarks); [Meta ads benchmarks for e-commerce](https://27five.com/blog/meta-ads-benchmarks-ecommerce-2026/); [adlibrary.com Meta e-commerce benchmarks](https://adlibrary.com/posts/meta-ad-benchmarks-ecommerce-2026)
- CPM by country — [Adamigo](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026); [Lebesgue](https://lebesgue.io/facebook-ads/facebook-cpm-by-country); [Adligator](https://adligator.com/blog/meta-ads-cpm-by-country-benchmarks); [Meta Ads Spain playbook](https://adlibrary.com/posts/meta-ads-spain-playbook-2026)
- Q4 seasonality — [Benly](https://benly.ai/learn/meta-ads/meta-ads-seasonal-campaigns); [Scigrowth BFCM playbook](https://scigrowth.com/blogs/strategy-growth-1/meta-ads-black-friday-playbook-launch-timeline-budget-scaling); [Clouted CPM inflation statistics](https://clouted.com/blog/meta-advertising-CPM-inflation-statistics)
- Creative volume and Andromeda — [MHI Growth Engine on creatives per week](https://mhigrowthengine.com/blog/how-many-creatives-to-test-meta-ads/); [Adamigo creative testing benchmarks 2025](https://www.adamigo.ai/blog/meta-ad-creative-testing-benchmarks-2025); [Atria Andromeda guide](https://www.tryatria.com/blog/andromeda-meta-ads); [Madwise on creative diversity](https://madwise-agency.com/blog/meta-ads-facebook-algorithms-andromeda/); [Wonderful — Andromeda creative strategies](https://www.usewonderful.com/blog/meta-andromeda-creative-strategies)
- Google — [smec Market Observer CPC benchmarks](https://smarter-ecommerce.com/en/smec-market-observer/metrics/cpc/); [Q4 2025 report](https://smarter-ecommerce.com/en/smec-market-observer/reports/Q4_2025/); [WordStream Google Ads benchmarks](https://www.wordstream.com/blog/2025-google-ads-benchmarks); [Google Shopping benchmarks by category](https://foundrycro.com/blog/google-shopping-benchmarks-by-category-2026/)
- Conversion and returns — [Blend Commerce conversion benchmarks](https://blendcommerce.com/blogs/shopify/ecommerce-conversion-rate-benchmarks-2026); [Enavi Shopify benchmarks](https://www.enavi.co/blogs/shopify-conversion-rate-benchmarks); [Richpanel return rates](https://www.richpanel.com/learn/ecommerce-return-rates); [Eightx EU return benchmark](https://eightx.co/blog/eu-ecommerce-return-rate-benchmark); [Prime AI clothing return rates by country and category](https://www.prime-ai.com/en/media/clothing-return-rates-by-category-and-country-csf-a/)
- UGC and production costs — [Superscale UGC pricing](https://superscale.ai/learn/how-much-does-ugc-cost-real-pricing-breakdown-for-2025/); [Atlas Cloud UGC agency costs](https://www.atlascloud.ai/blog/tips/ugc-video-agency); [ppc.io UGC rates](https://ppc.io/blog/ugc-pricing); [Sovran video ad production cost](https://sovran.ai/benchmarks/video-ad-production-cost)

**Turkey sourcing and the cost picture**
- [Hicabistan — factory-direct wholesale, Istanbul](https://hicabistan.com/); [Woolgold — scarf & shawl manufacturer, Istanbul](https://woolgold.com/shawl-scarf-manufacturer-in-istanbul/); [go4WorldBusiness — Turkish scarf suppliers and bulk prices](https://www.go4worldbusiness.com/suppliers/turkey/scarves.html); [Europages — shawls, Türkiye](https://www.europages.co.uk/companies/turkey/shawls.html)
- [WWD Sourcing Journal — Turkey's minimum wage surges 27%](https://wwd.com/sourcing-journal/industry-news/turkey-minimum-wage-surges-27-percent-1238860787/); [Yahoo Finance coverage](https://finance.yahoo.com/news/turkey-rising-minimum-wage-puts-120000444.html); [Turkish Minute — textile industry struggles](https://www.turkishminute.com/2025/05/27/turkeys-textile-industry-struggles-amid-rising-costs-global-competition/); [Kohan Textile Journal — $7bn loss, 210,000 job cuts](https://kohantextilejournal.com/turkeys-textile-apparel-industry-faces-7b-loss-210000-job-cuts/); [PolyesterTime — deep crisis](https://www.polyestertime.com/turkey-textile-industry-in-deep-crisis/)
- [ING THINK — Turkish disinflation](https://think.ing.com/snaps/disinflation-continues-moving-below-of-the-central-banks-forecast-range/); [Naga — lira forecast](https://naga.com/en/news-and-analysis/articles/turkish-lira-forecast-and-price-predictions); [Trading Economics — EU imports of shawls/scarves from Türkiye](https://tradingeconomics.com/european-union/imports/turkey/shawls-scarves-mufflers-mantillas-veils)

**Competitors, product and trend**
- [Petrusse](https://www.petrusse.com/en-us/collections/silk-scarf-maison-petrusse-made-in-france) · [Philéone](https://phileone.fr/en/collections/femmes-foulards) · [Le Châle Bleu](https://lechalebleu.fr/en/) · [Fleuron Paris](https://us.fleuron.paris/collections/foulards-bandeaux-soie) · [SOI Paris](https://soi-paris.com/en/collections/les-foulards-en-soie) · [Soeur](https://www.soeur.fr/en/collections/foulards) · [Foularchic](https://foularchic.com/) · [Lollipops](https://lollipops.fr/collections/foulard) · [Balaboosté](https://www.balabooste.com/collections/foulards)
- [Fio de Martié](https://www.fiodemartie.com/en/categoria/for-her/panuelos-seda-special-design/) · [Hamzah](https://hamzah.es/en/) · [Julunggul](https://julunggul.com/) · [Munira](https://munira.net/collections/scarves-and-shawls) · [El Corte Inglés](https://www.elcorteingles.es/moda-mujer/accesorios/panuelos-y-fulares/) · [Cortefiel](https://cortefiel.com/es/es/mujer/complementos/fulares) · [H&M Spain](https://www2.hm.com/es_es/mujer/accessories/bufandas.html) · [Massimo Dutti via Lyst](https://www.lyst.com/es-es/comprar/bufandas-massimo-dutti/)
- [Hermès scarf price comparison (Bagaholic)](https://lvbagaholic.com/blogs/lv_bagaholic/hermes-scarf-prices-comparison) · [Elizabetta — French scarf alternatives](https://elizabetta.net/blogs/the-elizabetta-fashion-accessories-journal/french-scarf-alternatives) · [Atelier Hoi An — best silk scarf brands](https://atelierhoian.com/en/best-silk-scarf-brands/)
- Trend — [Marie Claire UK — the silk scarf is spring 2026's smartest styling trick](https://www.marieclaire.co.uk/fashion/shopping/silk-scarf-trend-2026); [WWD — the little silk scarf trend 2026](https://wwd.com/fashion-news/fashion-trends/silk-scarf-trend-1238940326/); [La Caressette — 2026 silk scarf trends](https://lacaressette.com/en/blogs/lart-du-nouage-et-du-stylisme/2026-silk-scarf-trends-colors-and-prints)
- Market sizing **[vendor estimates]** — [Fortune Business Insights — scarves & shawls market](https://www.fortunebusinessinsights.com/scarves-shawls-market-110358); [ECDB — fashion industry in Spain](https://ecdb.com/resources/sample-data/market/es/fashion); [Grand View Research — Turkey textile market](https://www.grandviewresearch.com/horizon/outlook/textile-market/turkey)

**Payments, logistics and channels**
- [PPRO — Spanish e-commerce payments and Bizum](https://www.ppro.com/countries/spain/); [Stripe — Bizum for businesses](https://stripe.com/resources/more/bizum-for-buisinesses-spain); [Antom — Cartes Bancaires](https://knowledge.antom.com/cartes-bancaires-explained-what-global-merchants-need-to-know); [Payplug — the CB scheme](https://www.payplug.com/blog/cb-scheme/); [Crowdfund Insider — Klarna's 5 years in France](https://www.crowdfundinsider.com/2026/06/287201-bnpl-fintech-klarna-marks-5th-year-of-steady-business-growth-in-france/)
- [Cross-Border Magazine — CTT Express Flash study, Spain & Portugal 2025](https://cross-border-magazine.com/ecommerce-trends-spain-portugal-2025-ctt-flash-study/); [DHL eCommerce — 2025 cross-border buying trends](https://www.dhl.com/global-en/microsites/ec/ecommerce-insights/insights/e-commerce-logistics/2025-cross-border-trends.html)
- [ShippyPro — shipping with SEUR](https://www.shippypro.com/blog/en/shipping-with-seur-a-guide-to-costs-and-services-2026); [Zunapro — Spanish e-commerce logistics and carriers](https://www.zunapro.com/spain/en/blog/ecommerce-logistics-spain-carriers); [European fulfilment cost benchmarks](https://fulfillment-france.eu/european-fulfillment-cost/)
- [TikTok Newsroom — TikTok Shop expands across Europe](https://newsroom.tiktok.com/tiktok-shop-expands-across-europe?lang=en-150); [Lengow — TikTok Shop Europe Q2 2026](https://blog.lengow.com/tiktok-shop-europe-q2-2026-e500m-across-four-markets/); [Dataïads — TikTok Shop France](https://www.dataiads.io/en/blog/tiktok-shop-arrive-en-france)

*All calculations in sections 6, 7, 8, 16 and 24 are my own models, built on the cost and benchmark inputs cited above. The model scripts are reproducible; assumptions are stated inline in each section.*
