# Generalized Command and Control (C2) Traffic Detected Playbook

**Project Title:** Generalized Command and Control (C2) Traffic Detected Playbook  
**Alert Type:** Detection of suspected command-and-control communication between an internal host and an external malicious system  
**Version:** 1.0  
**Date:**  2025-12-10

**Incident Type/Categorization:** Malware / External Threat / C2 Communication  
**Severity/Priority by Default:** High (tune per environment)  
**Source Platform:** SIEM Platform

---

## Why does it matter? (business impact)

Command-and-control traffic indicates that an internal system may already be compromised and communicating with an attacker-controlled server. Through C2 channels, attackers can issue commands, deploy additional malware, exfiltrate data, move laterally, or prepare ransomware attacks. Failure to contain C2 activity quickly can lead to widespread compromise, data loss, operational downtime, and regulatory or contractual impact.

---

## Triage (Tier 1)

### Review Source and Destination
- Identify internal source host (`srcip`, `host.name`, `agent.computer_name`).
- Identify external destination IP or domain (`dstip`, `destination.ip`, `destination.domain`).
- Confirm reputation using threat intelligence sources (VirusTotal, AbuseIPDB, GreyNoise, commercial TI feeds).
- Determine whether the destination is known malware, botnet, or C2 infrastructure.

### Review Network Characteristics
- Identify protocol and port (e.g., HTTP/S, DNS, TCP, UDP).
- Review session frequency, beaconing intervals, and connection persistence.
- Identify suspicious patterns such as low-and-slow periodic callbacks or unusual ports.

### Review Activity Type
- Determine whether activity is:
  - Blocked
  - Allowed
  - Partially successful
- Identify if data was transmitted outbound (possible exfiltration).

### Review Timestamp and Frequency
- Review initial detection time and recurrence.
- Identify whether communication is continuous or intermittent.
- Check whether activity coincides with suspicious user or process activity.

### Check for Related Alerts
- Suspicious PowerShell or script execution  
- Bad source reputation anomalies  
- Malware or EDR detections  
- Multiple failed logins  
- Data exfiltration or DNS tunneling alerts  

### Escalate when
- The C2 connection is allowed or partially successful.
- The destination is confirmed malicious.
- Repeated beaconing behavior is observed.
- The affected host is a critical business system.
- Additional host-based suspicious activity exists.

**Escalation targets:** SOC Tier 2 / Senior SOC Analyst / Lead SOC Analyst / IR Investigator

---

## Investigation (Tier 2 / Senior SOC / IR)

### Correlate Host and Network Activity
- Review EDR, firewall, proxy, and DNS logs for the affected host.
- Identify processes responsible for the network connections.
- Determine when the first C2 communication occurred.

### Investigate Malware Execution
- Identify suspicious processes, services, or scripts associated with the traffic.
- Review file creation, registry changes, scheduled tasks, or persistence indicators.
- Check for privilege escalation or lateral movement attempts.

### Assess Scope and Impact
- Identify whether other hosts are communicating with the same IP or domain.
- Determine if the infection is isolated or widespread.
- Review authentication logs for suspicious access from the infected host.

### Validate Asset and User Context
- Identify system owner and business function of the affected host.
- Determine whether sensitive data may reside on the system.
- Confirm whether the host is internet-facing or user-facing.

### Historical Analysis
- Review historical connections to the same IP/domain.
- Identify whether similar IOCs appeared in prior incidents.
- Compare with known threat campaigns.

### Escalate when
- Active malware infection is confirmed.
- Data exfiltration is suspected or observed.
- Multiple hosts are infected.
- Privileged systems or sensitive data are involved.

**Escalation targets:** IR Lead, SOC Manager, business owner

---

## Containment / Remediation

- Isolate the affected host from the network.
- Terminate malicious processes.
- Block C2 IPs, domains, and related infrastructure at firewall, DNS, proxy, and EDR controls.
- Remove malicious files, services, and persistence mechanisms.
- Reset credentials associated with the affected system and user.
- Patch vulnerable software exploited during the compromise.
- Conduct full malware scanning of the affected system.
- Notify IR Lead, IT operations, and system owner.

---

## Recovery & Lessons Learned

- Restore the system from a known-good backup if integrity cannot be guaranteed.
- Validate that no further C2 communication is observed.
- Confirm all persistence mechanisms have been removed.
- Update detection rules with new IOCs and beaconing patterns.
- Add blocked indicators to long-term deny lists.
- Perform root cause analysis:
  - How was the malware introduced?
  - What security control failed or was bypassed?
- Document full incident timeline, response actions, and required security improvements.
