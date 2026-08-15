# Window Alignment Read Order — Metabolized Primitive Stub

**Lifecycle:** METABOLIZED_PRIMITIVE_STUB  
**Current eligibility as fixed read order:** false

舊版固定要求 W01–07 依特定 GitHub path 順序讀取。該固定 Window／Path read order 已退休。

## 保留 Primitive
- 先建立 Identity／Domain／Authority／State 邊界，再讀 affected delta。
- 不從 Window-local assumption 或 Historical path 建立 Current。
- Reader 應 bounded read，必要時才 escalation。
- Conflict 只凍結 affected branch。

現行 successor：`CURRENT-SURFACE-MANIFEST.json` reader priority、六維 dispatch、Boundary-first／First Failure Gate。

完整舊 read-order list 保留於 Git history。
