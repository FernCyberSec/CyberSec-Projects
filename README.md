# Cybersecurity Projects & Portfolio

Welcome to my cybersecurity project portfolio.  
This repository centralizes my work across:

- **SOC operations & playbooks**
- **Security policies and governance artifacts**
- **AWS security concepts and mini-labs**
- **Hands-on projects, experiments, and technical writeups**

All content is created for **educational and reference purposes only**.  
It is **generalized** and must be **tailored to your specific environment, risk profile, and policies** before use in production.

---

## Objectives

This repository exists to:

1. **Develop and demonstrate practical skills**  
   - Document how I think through alerts, incidents, cloud security, and governance.
   - Show repeatable workflows rather than just theoretical notes.

2. **Serve as a living notebook of my growth**  
   - Track my progression from SOC analyst toward **SOC Lead / Manager** and **GRC-focused roles**.
   - Capture lessons learned in a structured, reusable way.

3. **Provide value to others**  
   - Offer generalized playbooks, templates, and concepts that others can adapt.
   - Help new analysts, students, and small teams get a starting point for their own processes.

---

## Repository Structure

> Folder names may evolve as the repository grows. Below is the current intended structure and purpose.

### `soc-playbooks/`

Generalized SOC alert playbooks focused on:

- Triage and investigation logic
- Escalation criteria and decision points
- High-level containment and recovery steps
- Business impact context

Example:  
- `rdp-suspicious-logon-attempt.md`  
- `suspicious-powershell-execution.md`

These are designed to be **vendor-neutral** and usable as quick-reference guides.

---

### `policies/`

High-level **security policy and governance artifacts**, such as:

- Draft incident response policies
- Vulnerability management and patching concepts
- Access control and remote access guidelines
- Other governance-oriented documents

These are **not** meant to replace legal or formal corporate policies, but to demonstrate **GRC thinking** and how technical controls tie to written expectations.

---

### `aws-security/`

AWS-focused security notes, labs, and mini-projects, for example:

- IAM, identity and access control concepts
- Logging and monitoring (CloudTrail, CloudWatch, Security Hub, GuardDuty, etc.)
- Example architectures or small lab environments
- Detection and response ideas in AWS contexts

The goal is to combine **cloud security fundamentals** with **hands-on experimentation**.

---

### `projects/`

Standalone or small-scale projects, such as:

- Detection engineering or SOC lab exercises
- Scripts or small tools (e.g., log parsing, enrichment helpers)
- Experimental ideas or proofs-of-concept

These projects are meant to show **how I apply concepts end-to-end**, not just theory.

---

### `writeups/`

Written analysis and reflections, such as:

- Incident-style writeups based on lab scenarios
- Post-mortem style documents (what worked, what didn’t)
- Short essays on specific topics (e.g., RDP risk, MFA gaps, alert tuning approaches)

These writeups demonstrate **communication skills**, which are critical for SOC leadership and GRC roles.

---

## How to Use This Repository

- **For learners / junior analysts:**  
  Use the playbooks, policies, and notes as examples of how to structure your own documentation. Adapt them to your environment and tools.

- **For teams or startups:**  
  Treat this as a set of **starting templates**. Replace generalized terms with your actual platforms (e.g., your SIEM, your ticketing system, your cloud provider).

- **For reviewers / recruiters:**  
  This repo is intended to show:
  - How I structure technical and process documentation.
  - How I think about **business impact**, **risk**, and **operations**.
  - My progression toward **SOC leadership** and **GRC-oriented responsibilities**.

---

## Skills & Focus Areas Reflected Here

This repository touches on, but is not limited to:

- **Security Operations (SOC)**
  - Alert triage and investigation
  - Playbook design and escalation workflows
- **Incident Response Concepts**
  - Containment and recovery at a high level
  - Lessons learned and continuous improvement
- **Governance, Risk, and Compliance (GRC)**
  - Policy-style documents
  - Conceptual mapping to frameworks (e.g., NIST CSF, ISO-style controls)
- **Cloud Security (AWS)**
  - Identity and access management
  - Logging, monitoring, and basic detection ideas
- **General Blue Team / Defensive Security**
  - Remote access risks (e.g., RDP)
  - Authentication and account abuse scenarios

---

## Tools & Technologies (Referenced or Used)

Depending on the project, you may see references to:

- **SIEM / Logging platforms** (generalized, vendor-neutral)
- **EDR / Endpoint telemetry concepts**
- **AWS services** (e.g., IAM, CloudTrail, Security Hub, GuardDuty)
- **Common security tooling and Threat Intel sources** (e.g., AbuseIPDB, VirusTotal, GreyNoise)
- **Scripting / automation basics** (e.g., Python, shell) – as projects grow

This list will evolve as I add more hands-on examples.

---

## Certifications

These certifications inform the way I approach the material in this repository:

- CompTIA Security+  
- CompTIA CySA+  
- CISSP (Associate)  

(Additional certifications will be added here as I complete them.)

---

## About Me

I am a cybersecurity professional with a focus on:

- **Security Operations (SOC)** and incident handling  
- **Detection-oriented thinking** and practical playbooks  
- **Governance and risk** alignment rather than pure “tools-only” focus  

This repository is one of the ways I hold myself accountable to **continuous improvement** and build toward future roles such as **SOC Manager / Lead** and **GRC analyst**.

---

## Connect

If you would like to connect, discuss any of the material, or provide feedback:

- **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/fgj07/)  

You are welcome to open issues or pull requests with suggestions, corrections, or ideas.

---

## Disclaimer

All contents in this repository are:

- For **educational and reference use only**
- **Generalized** and not specific to any employer, client, or environment
- **Not legal, compliance, or formal policy advice**

You must assess, validate, and adapt any material here to your own **technical stack**, **regulatory requirements**, and **risk appetite** before using it in a production setting.
