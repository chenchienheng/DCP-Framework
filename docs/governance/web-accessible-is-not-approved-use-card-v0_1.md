# WEB_ACCESSIBLE_IS_NOT_APPROVED_USE Card v0.1

Status: Candidate / Red Door Card / No Runtime / No External Writeback
Use As: QHA/Aki red-door card for external web tools, community claims, and agent platform availability
Do Not Use As: company policy, vendor rejection, legal conclusion, tool ban, or final security decision

## Core

A tool being accessible on the web does not mean it is approved for company use. A community claim that a company can use it does not mean company IT, security, data owners, or management have approved it.

## Red Door Statement

```yaml
Web_Accessible_Is_Not_Approved_Use:
  web_can_open: "does not imply company approval"
  no_install_needed: "does not imply no security review"
  mobile_confirmation: "does not imply complete authorization chain"
  background_execution: "does not imply runtime approval"
  official_announcement: "does not imply internal approval"
  community_claim: "does not imply company policy"
```

## Candidate Gate

A tool may be listed as company-use candidate only if all are true:

```yaml
Company_Use_Candidate_Gate:
  official_enterprise_support: true
  company_it_security_allowed: true
  approved_account_or_tenant: true
  allowed_data_types_defined: true
  access_control_and_audit_visible: true
  human_responsibility_owner_visible: true
```

## Common False Equivalences

- Web 可用 != 公司允許.
- 免安裝 != 免資安審查.
- 手機確認 != 完整授權鏈.
- 背景執行 != 已授權 Runtime.
- 功能存在 != 公司資料可用.
- 社群說公司能用 != 公司 IT / 資安批准.

## Final Rule

If the approval chain is not visible, classify as Tool Available / Company Use Not Approved.