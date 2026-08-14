# Public Representation and Disclosure Policy
# 公開表徵與揭露控制規範

**Status / 狀態：** Working Policy  
**Scope / 範圍：** Public repository and externally releasable artifacts

## 1. Purpose / 目的

This policy defines how internal knowledge is transformed into externally releasable representations while preserving source rights, semantic integrity, and claim boundaries.

本規範定義內部知識如何轉換為可對外發布的表徵，同時維持來源權利、語義一致性與聲明邊界。

Public repositories are distribution surfaces, not authoritative native sources. Publication therefore requires both semantic alignment and explicit disclosure control.

公開倉是 Distribution Surface，不是權威 Native Source；因此發布必須同時滿足語義對準與揭露控制。

## 2. Representation profiles / 表徵層級

Externally releasable artifacts are maintained through aligned representation profiles:

- **Human Profile / 人類閱讀層** — Traditional Chinese for direct review and comprehension.
- **External Profile / 外部交換層** — English for publication, interoperability, and external technical review.
- **Canonical Machine Profile / 機器規範層** — minimal machine-consumable identifiers, typed state, version, and public evidence references.

All profiles refer to one governed artifact. They may differ in wording and presentation depth, but must remain equivalent in state, authority, claim ceiling, successor relation, and release classification.

所有表徵層均指向同一受治理物件；文字與詳略可以不同，但 State、Authority、Claim Ceiling、Successor Relation 與 Release Classification 必須一致。

## 3. Disclosure classes / 揭露分級

Every externally relevant artifact SHALL have one of the following disclosure classes:

- `INTERNAL` — not eligible for external release.
- `PUBLIC_CANDIDATE` — sanitized and structurally suitable for release, but not yet authorized.
- `PUBLIC_APPROVED` — explicitly authorized for external publication.
- `WITHHELD` — external representation intentionally unavailable because a release condition is unresolved.

A technically safe artifact is not considered published or release-authorized until the applicable release authority has approved it.

技術上可安全公開的 Artifact，在取得相應 Release Authority 核准前，仍不等於已發布或已獲公開授權。

## 4. Release gate / 發布門

External publication requires resolution of the following controls for the intended audience and purpose:

- source ownership and lawful-use basis;
- audience and purpose limitation;
- privacy and sensitivity classification;
- evidence sufficiency and claim ceiling;
- retention, redistribution, and derivative-use constraints;
- applicable release authority.

If any required control remains unresolved, the External Profile SHALL remain `PUBLIC_CANDIDATE` or `WITHHELD`.

## 5. Public-content boundary / 公開內容邊界

Public repositories may expose concepts, validation methods, bounded examples, release-appropriate evidence, and historical research lineage.

They SHALL NOT expose protected information whose aggregation would materially reveal internal implementation, privileged authority routing, private evidence lineage, sensitive source relationships, credentials, or restricted source bodies.

公開倉可承載概念、驗證方法、有限範例、適合發布的證據與歷史研究脈絡；不得揭露經聚合後會實質還原受保護內部實作、特權權限路由、私有證據血緣、敏感來源關係、憑證或受限制 Source Body 的資訊。

## 6. Machine-facing publication / 機器發布面

Machine-readable public metadata SHALL be intentionally minimal and stable. It may include public artifact identifiers, versions, typed lifecycle state, license, disclosure class, and public evidence pointers.

It SHALL NOT imply access to internal routing, private source pointers, privileged dependency topology, or restricted evidence bodies.

```yaml
artifact_id: <public-stable-id>
version: <version>
state: <typed-public-state>
disclosure_class: PUBLIC_CANDIDATE|PUBLIC_APPROVED
license: <license-id>
evidence_pointer: <public-pointer-or-null>
```

## 7. Semantic-drift control / 語義漂移控制

A material inconsistency between Human, External, and Canonical Machine profiles is classified as `SURFACE_DRIFT`.

When `SURFACE_DRIFT` is detected, publication of the affected artifact is suspended until the authoritative source, current evidence, and affected representation profiles are reconciled.

若三個表徵層在受治理語義上出現實質矛盾，視為 `SURFACE_DRIFT`；受影響 Artifact 的發布必須暫停，直到權威來源、現行證據與相關表徵完成調和。

## 8. Source boundary / 來源邊界

Publication, translation, serialization, or repository placement does not transfer source ownership or expand underlying rights.

發布、翻譯、序列化或放入 Repository 都不構成來源所有權移轉，也不會自動擴張原有權利。
