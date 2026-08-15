# Source Map — Metabolized Reader Stub

**Lifecycle:** METABOLIZED_PRIMITIVE_STUB  
**Current eligibility as fixed source map:** false

舊版把 GitHub／board_index／Gamma／Replit 路徑寫成 canonical Source Map；此設計已退休。

## 保留 Primitive
- Source pointer、Stable Identity、Version/Revision、Evidence、Writer/Authority、Return Target 必須可追溯。
- Mirror／Interaction／Projection 不得取代 Source。
- Path failure 應 fail-stop 到 read-only／HOLD，而不是猜測補鏈。

現行修正：Native Source Root 可在合法 Domain；GitHub 只是 Cloud/Carrier。Reader 先判 Domain→Authority→State，再 bounded resolve Source Pointer。

完整舊 fixed path map 保留於 Git history。
