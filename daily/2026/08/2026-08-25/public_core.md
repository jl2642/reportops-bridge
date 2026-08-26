# 能源周期日报｜2026-08-25｜Public-Safe Recovery Core

- Product role: `SIGNAL_RADAR`
- Target date: `2026-08-25`
- Fixed window: `[2026-08-24 10:00, 2026-08-25 10:00) Asia/Shanghai`
- Provenance: `FORMAL_RECOVERY_DAILY_FROM_CONFIRMED_SAME_DAY_FALLBACK_WITH_CHAT_REVALIDATION`
- Recovery note: 当日 contemporaneous fallback 的存在已被先前审计确认，但原始 row-level ledger 当前不可见；本稿是基于同一固定窗口重新核验后的 public-safe recovery core，不声称逐字恢复原始 ledger。

## 1. Executive Signal Summary

窗口内最重要的新增信号不是单一价格波动，而是中东能源物流受阻开始更清晰地向三个层面传导：**霍尔木兹海峡实际通行仍远低于常态、中国大型炼厂主动扩大非海湾原油来源、全球 LNG 高价正在同时制造供应替代机会与需求抑制风险。** 欧洲天然气库存补库经济性依旧偏弱，说明全球气价高企并没有自动转化为充足的库存安全垫。

## 2. Market & Event Delta

### Signal A｜霍尔木兹实际航运仍处于低通行状态
Reuters 基于 Kpler 与 UKMTO 信息显示，周日仅 4 艘、周六 13 艘商品船通过霍尔木兹海峡；UKMTO 所述 AIS 可见通行量仍约比冲突前基线低 90%。过去三日仍有大型 LPG 船通过，说明通道并非完全关闭，但能源物流能力明显低于正常水平。

**Why it matters:** 风险焦点应从“海峡是否名义开放”转向“可持续有效通行能力”。低通行率意味着原油、成品油和 LPG 的运输时间、保险、船舶调度与区域库存继续承压。

**Falsifier:** 若未来连续多日实际船舶通行和能源货量恢复接近冲突前水平，本信号显著减弱。

### Signal B｜中国炼厂开始把供应安全从库存管理推进到来源重构
Sinopec 表示将提高来自巴西、非洲等海湾以外地区的原油采购，并继续通过沙特 Yanbu、阿联酋海湾外装运点等方式保障供应。公司披露的商业库存约可支持 20 天炼油加工、15 天成品油销售。

**Transmission:** 海湾供应风险 → 炼厂扩大远距离/替代来源 → 原油贸易流重排 → 航程与运费结构变化 → 不同原油品质和炼化利润重新定价。

**China-chain implication:** 这不是简单的短期抢油，而是大型炼厂在高地缘风险环境下主动提高供应组合冗余度；后续应观察巴西/西非进口、红海/管线绕行以及炼厂加工负荷是否持续变化。

### Signal C｜美国 LNG 的供应替代优势正面对高价需求弹性测试
Reuters Open Interest 引述 LSEG/Kpler 数据称，2026 年前七个月美国 LNG 出口超过 7,300 万吨，同比增长约 23%；但亚洲第四季度远期 LNG 价格预计超过 22 美元/MMBtu，欧洲 7 月 LNG 进口降至 2021 年以来同期低位。

**Transmission:** 卡塔尔/海湾 LNG 受阻 → 美国 LNG 出口替代增强 → 全球气价上升 → 高价抑制价格敏感型买家与库存补库 → 供应紧张与需求破坏同时存在。

**Boundary:** Reuters Open Interest 属专业评论，方向性判断必须由其引用的 LSEG/Kpler 数据支撑；Work formalization 时应再次核对所有强数字主张。

### Signal D｜欧洲补库仍受夏冬价差倒挂抑制
Uniper 表示已填充其签约储气容量约 70%，但德国整体储气水平当时仅略高于 50%，欧盟约 62%。夏季价格高于冬季的倒挂结构削弱正常季节性注气激励。

**Why it matters:** 欧洲的风险不是“完全没有气”，而是高价格环境降低商业补库意愿，使冬季安全边际变薄；若全球 LNG 高价持续，补库成本与需求抑制之间的张力将继续存在。

## 3. Price & Spread Delta

本 recovery core 不使用无法在固定窗口内独立核验的即时油价/气价作为核心结论。明确可核验的价格结构信号是：亚洲后续月份 LNG 远期价格处于高位、欧洲夏冬天然气价差倒挂导致储气经济性受损。正式 Work 产品如加入具体价格值，必须重新核验 value/unit/currency/geography/basis/observation_time。

## 4. China Chain Delta

- 大型炼厂的供应安全策略从单纯库存缓冲扩展到原油来源和出口港口多元化。
- 中东至中国传统贸易流若长期受阻，巴西、西非等长航程桶的边际价值可能上升。
- 同时，Sinopec 预计全年原油加工量同比下降，显示供应风险与中国成品油需求趋弱可以同时存在，不能把进口多元化等同于总需求扩张。

## 5. Global Energy Delta

- 油：霍尔木兹有效通行量仍是核心物理约束。
- LNG：美国供应替代增强，但高价正在测试终端需求承受力。
- 欧洲气：库存仍在补充，但商业储气激励偏弱。
- LPG：海峡中仍观察到大型 LPG 船通行，意味着 LPG 物流是“受抑而非归零”，后续需关注 VLGC 实际货量、运价和亚洲到岸价差。

## 6. Research Trigger Board

- `WATCH`：霍尔木兹连续 3–5 天船舶/能源货量是否形成持续恢复。
- `WATCH`：中国巴西/西非原油进口与长航程运费是否显著上升。
- `WATCH`：亚洲 LNG >$22/MMBtu 环境下，现货采购是否出现更明显需求破坏。
- `WATCH`：德国/EU 储气水平与夏冬价差是否重新形成有效注气激励。

## 7. Industry Chain & Operator Exposure

- 上游与非海湾出口商：供应多元化需求提升其边际战略价值。
- 航运：长航程替代与海湾风险溢价提高吨海里需求，但同时受实际可通行能力约束。
- 炼化：原料来源改变、价格传导受限和成品油需求走弱共同影响利润，不应只看原油价格。
- LNG 贸易与终端：美国供应商短期受益于供应缺口，但高价可能削弱边际需求。
- 欧洲储气/公用事业：需要在高现货成本与冬季库存安全之间权衡。

## 8. Evidence, Gaps & Falsifiers

主要缺口：窗口内没有建立完整的多来源独立价格快照；部分运输量来自 AIS/Kpler 估算且存在关闭 transponder 的误差；美国 LNG 需求弹性部分来自 Reuters 专业评论而非单一官方数据集。

因此本稿允许进入 Work reconciliation，但所有涉及正式 Canonical 的强数字、价格和 private-layer 结论仍需 Work 按内部 Authority 门禁复验。

## 9. Next Verification

下一窗口重点验证：海峡实际船舶/货量、原油和 LNG 绕行贸易流、VLGC/LNG 运费、亚洲与欧洲气价、欧洲储气注入速度、中国炼厂加工负荷与非海湾原油采购变化。

## Public Sources

1. Reuters, 2026-08-24 — Fewer than 20 ships transit key Strait of Hormuz over weekend, data shows  
   https://www.reuters.com/business/energy/fewer-than-20-ships-transit-key-strait-hormuz-over-weekend-data-shows-2026-08-24/
2. Reuters, 2026-08-24 — Chinese refiner Sinopec to boost oil imports from outside the Gulf  
   https://www.reuters.com/business/energy/chinese-refiner-sinopec-boost-oil-imports-outside-gulf-2026-08-24/
3. Reuters Open Interest, 2026-08-24 — US LNG exports set for endurance test as high gas prices bite  
   https://www.reuters.com/commentary/reuters-open-interest/us-lng-exports-set-endurance-test-high-gas-prices-bite-2026-08-24/
4. Reuters, 2026-08-24 — Germany's Uniper says it has filled 70% of its contracted gas storage  
   https://www.reuters.com/business/energy/germanys-uniper-says-it-has-filled-70-its-contracted-gas-storage-2026-08-24/
