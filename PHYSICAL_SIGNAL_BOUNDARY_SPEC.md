# Physical Signal Boundary — Metabolized Intake Stub

**Lifecycle:** METABOLIZED_PRIMITIVE_STUB  
**Current eligibility as AXIS physical-signal runtime:** false

舊版將 physical signals 固定送入 AXIS-01／AXIS-05 與單一路徑 security review。此 routing ontology 退休。

## 保留 Primitive
- Physical/hardware signal 預設為 untrusted evidence candidate。
- Origin/authentication、timestamp/provenance、schema、rate/anomaly、privacy/purpose、cost、safety 必須可驗證。
- Local/edge preprocessing 與 cloud ingestion 應分界，但具體 topology 由 Carrier/Domain 決定，不是固定架構。
- Action based on sensor evidence 必須能 back-map 到 source packet；representation/aggregation loss 要可追溯。
- Failure HOLD affected signal branch；是否人工、重試或自動恢復取決於 Authority/Risk policy，不固定回單一 Review Axis。

現行 successor：Source↔Projection↔Back-map + Evidence Gate + Six-Dimension Cloud binding + affected-scope failure containment。

完整舊 AXIS/security-routing body 保留於 Git history。
