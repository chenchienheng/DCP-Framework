# Gemini to Google Sheet Bridge Spec

- Department: Adapter Layer
- Node ID: ADP-GBS-01
- Version: v0.1
- Status: Engineering Draft

---

## 1. Overview

This spec defines a safe bridge for ingesting point-cloud delta data from Gemini
into Google Sheets via Google Apps Script (GAS). It prioritizes data integrity
and non-destructive updates.

## 2. Safety Boundaries

- **No Deletion:** The script must never delete rows or clear the sheet.
- **Report-Only by Default:** Live writes require `AUTHORIZED_WRITE = true`.
- **Strength-Based Update:** Only update fields if the new data is "stronger"
  (e.g., Fact > Radar) or more recent.
- **No Private Data:** Payloads must not contain company-sensitive information.

## 3. GAS Code Draft

```javascript
/**
 * Gemini to Google Sheet Bridge (GAS)
 * Safety: Report-only until AUTHORIZED_WRITE = true
 */

const AUTHORIZED_WRITE = false; // Set to true to enable live writes

function doPost(e) {
  try {
    const payload = JSON.parse(e.postData.contents);
    const result = processPayload(payload);
    return ContentService.createTextOutput(JSON.stringify(result))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      error: err.toString(),
      status: "failed"
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function processPayload(payload) {
  const stats = { added: 0, updated: 0, skipped: 0, errors: [] };
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  let data = sheet.getDataRange().getValues();
  const headers = data[0];

  const entityNameIdx = headers.indexOf("Entity_Name");
  const statusIdx = headers.indexOf("Evidence_Status");

  payload.rows.forEach(newRow => {
    try {
      let existingRowIdx = -1;
      for (let i = 1; i < data.length; i++) {
        if (data[i][entityNameIdx] === newRow["Entity_Name"]) {
          existingRowIdx = i;
          break;
        }
      }

      if (existingRowIdx === -1) {
        const rowData = headers.map(h => {
          if (h === "Payload_ID") return payload.payload_id;
          if (h === "Source_Batch") return payload.source_batch;
          return newRow[h] || "";
        });
        data.push(rowData);
        stats.added++;
      } else {
        const existingStatus = data[existingRowIdx][statusIdx];
        const newStatus = newRow["Evidence_Status"];

        if (shouldUpdate(existingStatus, newStatus)) {
          headers.forEach((h, colIdx) => {
            let newVal = newRow[h];
            if (h === "Payload_ID") newVal = payload.payload_id;
            if (h === "Source_Batch") newVal = payload.source_batch;

            if (newVal && newVal !== data[existingRowIdx][colIdx]) {
              data[existingRowIdx][colIdx] = newVal;
            }
          });
          stats.updated++;
        } else {
          stats.skipped++;
        }
      }
    } catch (err) {
      stats.errors.push(`Row failed: ${newRow["Entity_Name"]} - ${err}`);
    }
  });

  if (AUTHORIZED_WRITE) {
    sheet.getRange(1, 1, data.length, headers.length).setValues(data);
  }

  return {
    status: stats.errors.length > 0 ? "partial_success" : "success",
    Asset_ID: "TBD",
    Location_Link: sheet.getParent() ? sheet.getParent().getUrl() : "Local",
    Return_Path: "AXIS-05",
    stats: stats,
    legion_log: {
      Round_ID: payload.payload_id,
      Node: payload.updated_by,
      Action: AUTHORIZED_WRITE ? "LIVE_WRITE" : "DRY_RUN_REPORT",
      Output: `Added: ${stats.added}, Updated: ${stats.updated}, ` +
              `Skipped: ${stats.skipped}, Errors: ${stats.errors.length}`,
      Next_Action: "Review report and authorize live write if needed",
      Risk_or_Blocker: stats.errors.length > 0 ?
          "Row processing errors" : "None",
      Return_Path: "AXIS-05"
    }
  };
}

function shouldUpdate(oldStatus, newStatus) {
  const weights = { "Fact": 3, "Signal": 2, "Radar": 1, "Pending": 0 };
  // Update if stronger OR same (to capture newer data/fields)
  return (weights[newStatus] || 0) >= (weights[oldStatus] || 0);
}
```

## 4. Test Payload Format

Aligned with `Writeback Packet Contract` (v0.1).

```json
{
  "payload_id": "PCD-TEST-001",
  "source_batch": "Gemini_Batch_001",
  "updated_by": "Gemini_Scout_Node",
  "rows": [
    {
      "Entity_Name": "Example Entity",
      "Entity_Type": "Owner / Demand Node",
      "Chain_Position": "Owner",
      "Region": "North",
      "Possible_Facility_Link": "Data Center",
      "Evidence_Status": "Radar",
      "Source_or_Search_Lead": "public search lead only",
      "Can_Support": "May be relevant to market point-cloud",
      "Cannot_Support": "Does not prove project opportunity",
      "Next_Verification_Needed": "official source / filing"
    }
  ]
}
```

## 5. Return Contract

The GAS bridge returns a JSON object with:

- **stats:** counts for added, updated, skipped, errors.
- **legion_log:**
  - **Round_ID:** from payload.
  - **Node:** from payload.
  - **Action:** LIVE_WRITE or DRY_RUN_REPORT.
  - **Output:** summary string.
  - **Next_Action:** instructions for next step.
  - **Risk_or_Blocker:** row processing errors or None.
  - **Return_Path:** AXIS-05 (Review Chain).

## 6. GitHub Action Plan (Optional)

A workflow to validate the bridge logic using a mock spreadsheet service.

1. **Trigger:** Push to `04_adapter-layer/`.
2. **Setup:** Install Node.js dependencies (e.g., `jest`).
3. **Test:**
   - Validate payload schema.
   - Run unit tests for `shouldUpdate` logic.
   - Mock GAS `SpreadsheetApp` to verify append/update behavior.

## 7. Status & Tracking

- design_complete: true
- gas_draft_included: true
- report_only_enabled: true
- registered_in_corpus: true
