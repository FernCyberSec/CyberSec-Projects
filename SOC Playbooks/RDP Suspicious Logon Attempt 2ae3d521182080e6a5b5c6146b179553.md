# RDP Suspicious Logon Attempt

**Project Title:** Generalized ****RDP Suspicious Logon Attempt Playbook

**Alert Type:** Detection of a potentially unauthorized or abnormal attempt to access a system via Remote Desktop Protocol (RDP)

**Version:** 1.0 

**Date:** 2025-11-17

**Incident Type/Categorization:** Remote Access

**Severity/Priority by Default:** High (tune per environment).

**Source Platform:** SIEM Platform

**Why does it matter?** (business impact)

Unauthorized RDP access can lead to full system compromise, data theft, ransomware deployment, or lateral movement, particularly when privileged accounts or critical systems are involved. Early detection helps prevent breaches, business disruption, and potential regulatory or contractual impact.

---

### **Triage (Tier 1)**

**Review Source IP Address**:

- Check `srcip, source.ip`.
- Determine if the IP is internal or external.
- Use threat intelligence tools (AbuseIPDB, VirusTotal, GreyNoise) to assess if it’s associated with known scanning or brute-force behavior and get enriched Geo-IP location.

**Review Destination Host and IP**:

- Validate `agent.computer_name` or `host.name` and `dstip`.
- Confirm if the system is expected to accept RDP connections (jump servers, admin systems).
- Flag RDP access to workstations or servers where RDP should be disabled or tightly restricted, especially critical business systems.

**Review Logon Type and Event Data**:

- Confirm that the logon type is RDP-related (typically Logon Type 10).
- Check `TargetUserName` to identify the user account targeted.
- Review `ProcessName` or service that indicated the session if available for insights.

**Check Timestamp and Repetition**:

- Review the time and frequency of the logon attempts.
- Look for repeated failed RDP logins from the same IP or toward the same host.
- Consider whether activity occurs outside normal business hours for the user or system.

**Escalate when:**

- A successful RDP logon is observed and appears unusual (new source IP, new device, off-hours, external IP).
- The target system is a critical business asset (domain controller, jump server, finance system, etc.)
- The alert has incomplete or unclear data that prevents confident triage.
- You observe indicators of possible brute-force activity (multiple failures followed by a success).

**Escalation targets:** SOC Tier 2 / Senior SOC / Lead SOC Analyst / IR Investigator

---

### **Investigation (Tier 2 / Senior SOC / Lead SOC Analyst / IR Investigator)**

**Correlate with Other Authentication Alerts**:

- Look for related alerts like password spraying, login location anomalies, or brute-force indicators.

**Investigate Host Behavior**:

- Search for process execution, network traffic, or suspicious scripting activity following the logon attempt.
- Confirm if there was any data access or lateral movement after the RDP session started (if successful).

**User & Role Validation**:

- Check if the targeted user is an admin or service account.
- Investigate if RDP access is authorized for that user on the target system.

**Historical Analysis**:

- Review historical RDP login patterns for both the user and host to determine whether this attempt is abnormal.
- Confirm with the user’s manager or system owner whether the login is expected (especially for privileged accounts).

**Escalate when:**

- A successful RDP login is confirmed on a critical business system, **and**
- The user is:
    - Unknown or not recognized by the system owner, **or**
    - A privileged account (IT admin, service account) with no clear business justification for this access, and
- You observe suspicious post-login activity, such as unusual process execution, privilege escalation, lateral movement, or data staging/exfiltration.

**Escalation targets:** IR Lead, SOC Manager, business owner

---

### **Containment / Remediation**:

In practice, you usually first preserve evidence ****/ isolate, then reset.

- Isolate the affected host from the network if unauthorized access is confirmed or strongly suspected.
- Terminate active RDP sessions associated with the suspicious activity.
- Reset the user’s credentials and enforce strong password policy and MFA (where supported).
- Temporarily disable or lock the account if compromise is likely and operations allow.
- Block malicious source IPs or ranges at the firewall, VPN, or security gateway, as appropriate.
- Review and restrict RDP exposure, including:
    - Disabling direct external RDP access where possible.
    - Limiting RDP to jump hosts or VPN-only access.
- Notify relevant stakeholders (IR lead, system owner, business owner, IT operations) and coordinate any required downtime or change approvals.

---

### **Recovery & Lessons Learned**

- Restore normal access only after the affected systems are verified as clean, patched, and correctly configured.
- If unauthorized changes or damage were identified, restore from a known-good backup. Take a forensic snapshot or image before major remediation where feasible.
- Perform a brief root cause and gap analysis:
    - How was RDP accessed (internet-exposed, weak credentials, lack of MFA, stolen VPN credentials, etc.)?
    - What controls failed or were missing?
- Update detection rules, alert thresholds, and playbooks based on new IOCs, TTPs, and lessons learned (better tuning for failed/successful RDP combinations).
- Document the incident in the ticketing or IR system, including timeline, actions taken, and recommendations for long-term hardening.

---