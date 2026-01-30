# Daily Azure Security Briefing — SAMPLE
**Date:** YYYY-MM-DD  
**Scope:** Azure + Entra + Defender signals (export-first MVP)  
**Audience:** Exec / IT leadership (60-second read)

---

## 1) Top Risks (Today)
- **High:** Suspicious sign-in activity on privileged accounts (multiple IPs / impossible travel indicators).
- **Medium:** New firewall/NSG rule changes increasing exposure on a public endpoint.
- **Medium:** Defender alerts indicate malware-like behavior on one endpoint (investigating).

---

## 2) Detections / Incidents
- **Defender Incident:** “Potential credential access”  
  **Severity:** High  
  **Affected:** User: <user>, Device: <device>  
  **What happened:** Multiple failed logins followed by successful auth from new geo/IP.  
  **Next action:** Verify MFA, reset credentials, review conditional access.

---

## 3) Identity & Privilege Changes
- New role assignment detected: **<role>** granted to **<user/service principal>**  
  **Why it matters:** Privilege escalation risk  
  **Next action:** Confirm business justification + ticket reference.

---

## 4) Azure Control-Plane Changes
- NSG updated: inbound rule added **Allow 0.0.0.0/0 → <port>**  
  **Risk:** Public exposure  
  **Next action:** Restrict source IPs, confirm need, add approval workflow.

---

## 5) Recommended Actions (Owner + ETA)
- **Owner:** <name/team> — Review privileged sign-ins + enforce MFA policies — **ETA:** Today EOD  
- **Owner:** <name/team> — Roll back NSG change or narrow scope — **ETA:** Today  
- **Owner:** <name/team> — Validate Defender incident + isolate device if needed — **ETA:** 4 hours

---

### Notes
This is a sample output format. Real data will populate these sections from exports/API queries.

