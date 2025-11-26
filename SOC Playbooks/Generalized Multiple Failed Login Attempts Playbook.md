# Generalized Multiple Failed Login Attempts Playbook

**Project Title:** Generalized Multiple Failed Login Attempts Playbook

**Alert Type:** Detection of repeated failed authentication attempts for a user, system, or source

**Version:** 1.0

**Date: 2025-11-26**

**Incident Type/Categorization:** Authentication Anomaly / Credential Access

**Severity/Priority by Default:** Medium to High (tune per environment)

**Source Platform:** SIEM Platform

---

### **Why does it matter? (business impact)**

Multiple failed login attempts may signal password spraying, credential stuffing, brute-force activity, or early-stage account compromise. Successful access following repeated failures can lead to unauthorized entry, privilege misuse, lateral movement, data exposure, or business disruption. Early detection reduces the risk of unauthorized access and protects critical systems and accounts.

---

## **Triage (Tier 1)**

### **Review Failed Login Pattern**

- Identify total number of failed attempts and the timeframe (e.g., 20 failures in 5 minutes).
- Determine if failures target a single account or multiple accounts.
- Identify whether attempts originate from one IP or several.

### **Review Source IP or Device**

- Collect `srcip`, device ID, or originating host.
- Determine internal vs. external network origin.
- Enrich with threat intelligence (AbuseIPDB, VirusTotal, GreyNoise).
- Check for known scanning, spray behavior, TOR exit nodes, or cloud-hosting providers.

### **Review Target User Account**

- Identify account type (`TargetUserName`): standard, admin, or service account.
- Check for recent password changes, lockouts, or help desk tickets.
- Confirm MFA enrollment status if applicable.

### **Review Timestamp and Behavior**

- Review timestamp for off-hours or abnormal login times.
- Look for patterns indicating password spraying (same source targeting many users).
- Identify whether failures are occurring across multiple systems.

### **Check for Related Alerts**

- Password spray alerts
- Impossible travel or login location anomalies
- Account lockouts
- MFA failure alerts
- Successful authentication events following failures

### **Escalate when:**

- Failures are coming from a suspicious or high-risk external IP.
- The account is privileged or sensitive.
- Multiple accounts are affected in a short timeframe (spray behavior).
- A successful login occurs following a cluster of failures.
- Data is incomplete or the event cannot be confidently triaged.

**Escalation targets:** SOC Tier 2 / Senior SOC Analyst / Lead SOC Analyst / IR Investigator

---

## **Investigation (Tier 2 / Senior SOC / IR)**

### **Correlate Authentication Activity**

- Review authentication attempts before and after failures.
- Identify whether a successful login occurred after failed attempts.
- Review MFA logs for failures, disablements, or unusual prompts.

### **Investigate Source Behavior**

- Review network logs, VPN logs, or firewall events from the source IP.
- Check whether the IP initiated attempts against multiple accounts.
- For internal sources, review EDR telemetry for suspicious processes or lateral movement.

### **Validate User and Role**

- Confirm with system owner or manager whether login attempts were expected.
- Determine whether the user recently traveled or changed devices.
- Verify that the account should be used interactively (service accounts often should not).

### **Historical Analysis**

- Compare login behavior to historical patterns for the user and device.
- Determine whether the user typically logs in from the observed location or time window.
- Review whether failed attempts have occurred previously from the same IP.

### **Escalate when:**

- A successful login appears suspicious or unrecognized.
- Attempts target admin accounts, service accounts, or critical business systems.
- The source IP shows malicious behavior or scanning activity.
- Additional indicators point toward account compromise, password spraying, or lateral movement.

**Escalation targets:** IR Lead, SOC Manager, Business Owner

---

## **Containment / Remediation**

- Reset the affected user’s credentials.
- Re-enforce MFA setup or re-registration if required.
- Temporarily disable the account if compromise is suspected.
- Block the malicious source IP or ranges at firewall, VPN, or identity provider.
- Invalidate existing sessions and authentication tokens where applicable (cloud environments).
- For internal sources: investigate and isolate host if needed.
- Notify IR Lead, system owner, and relevant stakeholders for coordination.

---

## **Recovery & Lessons Learned**

- Confirm access restoration for legitimate users only.
- Validate that no unauthorized access occurred following the failed attempts.
- Tune detection rules to reduce noise (thresholds, correlation logic).
- Add indicators, patterns, and behavioral insights from this incident to improve detection.
- Document timeline, actions taken, and recommendations for long-term controls.
- Identify root cause and control gaps (e.g., weak passwords, MFA gaps, external exposure).

---