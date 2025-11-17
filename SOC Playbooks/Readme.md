# SOC Playbooks – Professional Portfolio

This repository contains a collection of **generalized SOC alert playbooks** designed to support:

- New SOC analysts learning how to investigate common alerts  
- Startups or small teams needing lightweight playbooks to jump-start operations  
- Security researchers looking for structured, repeatable investigation approaches  

The playbooks are intentionally **compact, technology-agnostic, and vendor-neutral**. They are meant as quick-reference guides, not full incident response runbooks or formal policy documents.

This repository also serves as part of my **professional portfolio** as I continue developing toward roles such as **SOC Manager / Lead** and **GRC (Governance, Risk, and Compliance) Analyst**.

---

## Objectives

This repository is built with the following goals:

1. **Practical learning**  
   - Document real-world investigation logic for common alerts  
   - Reinforce good triage, investigation, escalation, and containment habits  

2. **Reusable starting point**  
   - Provide generalized playbooks that other teams can adapt to their own tools, environments, and risk profiles  

3. **Leadership and GRC development**  
   - Show how operational playbooks connect to business impact, governance, and risk  
   - Demonstrate thought process aligned with SOC leadership and GRC responsibilities  

---

## Audience

These playbooks are written for:

- **SOC Analysts (Tier 1 / Tier 2)**  
  Quick, structured guidance on how to triage and investigate alerts.

- **SOC Leads / Managers in smaller organizations or startups**  
  A baseline set of investigation flows that can be customized and built upon.

- **GRC / Risk practitioners**  
  Examples of how technical alerts tie back to business impact, risk, and control expectations.

- **Security Researchers / Blue Teamers**  
  Simple, repeatable frameworks for testing and documenting detection coverage.

---

## Repository Structure

> Note: Folder names may evolve over time as the content grows. The descriptions below explain the intent of each area.

### `playbooks/`

Core SOC alert playbooks, typically one file per alert type.

- Focused on **triage**, **investigation**, **escalation criteria**, **containment**, and **recovery / lessons learned**.
- Written to be **generalized** and **tool-agnostic** (e.g., “SIEM Platform” instead of a specific vendor).
- Examples:  
  - `rdp-suspicious-logon-attempt.md`  
  - `suspicious-powershell-execution.md`  
  - `cryptojacking-activity-detected.md`
---

## Playbook Structure

Most playbooks follow a consistent pattern:

- **Alert Type & Context** – What the alert represents and why it matters  
- **Incident Type / Severity** – High-level classification and default severity (with tuning notes)  
- **Business Impact** – What could go wrong from a business perspective if this alert is ignored  
- **Triage (Tier 1)** – Quick checks, data points to review, and clear escalation triggers  
- **Investigation (Tier 2 / IR)** – Deeper correlation steps, historical analysis, and behavior review  
- **Containment / Remediation** – High-level actions that should be tailored to each environment  
- **Recovery & Lessons Learned** – Root cause, improvements to controls, and documentation

The goal is to keep each playbook **short, structured, and immediately usable**.

---

## How to Use These Playbooks

- **As a new SOC analyst:**  
  Use the playbooks as a guide for how to think through alerts: what to check, when to escalate, and how to connect technical evidence to business risk.

- **As a small or new SOC team / startup:**  
  Clone or copy the playbooks and adapt them to your environment, tools, and policies. Replace generic field names with your actual log fields and platforms.

- **As a researcher / engineer:**  
  Use the playbooks as a baseline for building detection tests, lab scenarios, and documentation around coverage and tuning.

---

## Roadmap

Planned future enhancements include:

- Additional playbooks for common endpoint, network, and cloud alerts  
- More communication templates (internal and external)  
- Expanded GRC mappings to frameworks (NIST CSF, ISO 27001, etc.)  
- Example lab scenarios showing how to test and validate the playbooks

---

## Disclaimer

These materials are **for educational and reference purposes only**.  
They are generalized and **must be tailored** to the specific technologies, policies, legal requirements, and risk appetite of any organization before being used in production.

