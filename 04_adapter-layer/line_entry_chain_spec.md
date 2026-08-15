# LINE Entry Chain Specification — Historical Adapter Stub

**Lifecycle:** HISTORICAL_IMPLEMENTATION_STUB  
**Current eligibility:** false  
**Executable authority:** none

舊版把 LINE 固定成 AXIS-01 primary entry、AXIS-05 fallback，並包含當時 API/quota/rate 假設。這些均不是現行架構或可直接執行規格。

## 保留 Primitive
- External message/event 是 Source/Signal Candidate，不因進入介面就成 Truth。
- Adapter 必須分 Input validation、Identity/Context binding、Authority/Purpose、Processing、Review、Reply/Export、Return/Evidence。
- Rate/cost/API constraints 屬 Carrier-specific profile，接入時重新驗證。
- Interface success ≠ Native absorption。

現行 successor：Carrier-neutral Adapter Contract + 六維 Cloud binding + Boundary-first gates。

完整 LINE webhook/API 舊規格保留於 Git history。
