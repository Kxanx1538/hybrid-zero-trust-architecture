
# 🔐 Hybrid Multi-Cloud Zero Trust Architecture


Welcome to my cybersecurity engineering showcase—a real-world hybrid multi-cloud architecture I designed and implemented using Zero Trust principles across On-Prem, Azure, AWS, and SaaS ecosystem.  The design integrates identity, access control, monitoring, and secure remote access across cloud, on-premises, and SaaS environments.

---

## 🌐 Overview

This repository demonstrates how I built and secured a hybrid infrastructure spanning:

- 🏢 On-Premises  
- ☁️ Azure & AWS Cloud  
- 🧩 SaaS Platforms  

The architecture follows Zero Trust principles — ensuring **continuous identity verification**, **least privilege**, and **context-based access** across environments.

---

## 🧩 Architecture Diagram

🔽 Sanitized visual of the high-level architecture:

![Hybrid Architecture](./assets/Hybrid+Multi-cloud-sanitized.drawio.png)


## 🧭 Architecture Breakdown & Data Flow

🧩 Architecture Components Explained

This architecture enforces Zero Trust principles across a hybrid, multi-cloud ecosystem, integrating identity, access, monitoring, and secure access controls. Here's how the components interact:

|Zone / Layer                   |Component                            | Description
|-------------------------------|-------------------------------------|-----------------
|Federated Identity             |Federated Identity Management (FIM)  |Centralized access and identity federation using Microsoft Entra ID (SSO, MFA,PIM, SCIM, GPO, CA) to manage user access across SaaS, Azure, AWS, and on-prem resources.
|User Layer                     |👤 User Identity                     |Identities are verified and routed through Conditional Access policies and MFA enforced via Entra ID.
|On-Premises                    |AD, Legacy Travel Apps                |Legacy applications and infrastructure reside in a high-trust zone, integrated into Azure via AD Connect.
|Azure Cloud                    |Azure Resources, Defender XDR     |Azure hosts core apps, UEM, and SIEM; integrated with Microsoft Sentinel, Defender for Cloud, and Conditional Access enforcement.
|                               |Microsoft 365, Compliance Manager      |Compliance policies and threat monitoring configured in Microsoft Purview.
|AWS Cloud                      |IAM Identity Center, VPC, SecurityHub, CloudWatch, S3  |AWS apps and services reside in a medium trust zone, connected via ZTNA and monitored through AWS CloudTrail and SecurityHub.
|SaaS Layer                     |Travel apps, Email, ITSM, ITAM tools   |SaaS integrations (e.g., Zendesk, Gmail, Zoho) are federated via Entra ID and secured using Secure Web Gateway and VPN access.
|Network Security Tools         |Netbird VPN, Microsoft Global Secure Access (GSA), Suricata |Tunnels secure access between clouds and SaaS services, applying Zero Trust Network Access (ZTNA).
|Monitoring                     |Sentinel, Site24x7, Azure Monitor      |Central SIEM correlation, real-time alerts, endpoint, and network telemetry across environments.

## 🔄 Data & Trust Flow Summary

- Identity Flow: Authenticated users flow through Entra ID → Conditional Access → SCIM/MFA → Workload Access.

- Traffic Routing: Traffic is routed over Netbird VPN and Microsoft GSA for secure connectivity.

- Zone Enforcement:

  - 🔐 High Trust: On-Prem

  - 🔐 Medium Trust: Azure & AWS

  - 🔐 Low Trust: SaaS (external)

- Policy Controls: Conditional Access & RBAC differentiate user access across zones and services.

- Monitoring Layer: Logs from Azure, AWS, SaaS, and VPN are ingested into Microsoft Sentinel for correlation, alerting, and SOAR workflows.

---
## 🛡️ Security Highlights

- ✅ Hybrid identity and access control with **Microsoft Entra ID**, AWS IdentityCenter, AD
- ✅ Zero Trust Network Access using **Netbird VPN** + **Microsoft Global Secure Access**
- ✅ **Unified Endpoint Management** via Endpoint Central, integrated with Azure AD
- ✅ **SIEM integrations**: Microsoft Sentinel,AWS SecurityHub, AWS CloudWatch, Azure Monitor 
- ✅ **Conditional Access** for trusted zones and role-based access
- ✅ **TLS 1.2**, **disk encryption**, and **VPN-enforced SSO**

---

## 📸 SecOps in Action

| Description                                                    | Screenshot                                               |
|----------------------------------------------------------------|------------------------------------------------          |
|**🔎 Correlated attacks: Privilege escalation alert investigation**
This Sentinel investigation reflects my analysis of a high-severity incident involving unauthorized role elevation. Sentinel’s Fusion analytics automatically grouped related alerts — such as privileged role assignments and PowerShell activity — into a unified attack storyline.I examined the Investigation Graph to correlate IP addresses, user accounts, and affected resources. This accelerated my understanding of the attack path, validated the threat, and informed response decisions. The view demonstrates how I conducted cross-domain correlation analysis to drive evidence-based incident response in a hybrid environment.                                                     | ![Screenshot of Microsoft Sentinel Investigation Graph showing cross-domain correlated entities including IPs, users, and resources](./assets/Persistant_attack.png)           |
| **📊  SIEM Log Correlation in Microsoft Sentinel**
Continuing from the same incident, this view captures my analysis using the Timeline tab — which revealed how the attacker’s activities unfolded across services and time. I traced suspicious actions from initial access to privilege escalation across Entra ID, Defender for Cloud, and Azure Activity. By combining timeline mapping with graph-based entity analysis, I accelerated investigation and reinforced incident response accuracy. This demonstrates my ability to interpret correlated data across Microsoft’s XDR stack and convert it into actionable response steps using Microsoft Sentinel.                                                       | ![Screenshot of Microsoft Sentinel Timeline view showing sequence of attacker actions across cloud services](./assets/Correlated_story_telling.png) |
| **🎯 Conditional Access Policy enforcement(**80.21%** Identity Score)**
This screenshot reflects my implementation and continuous enforcement of Conditional Access policies in Microsoft Entra ID, achieving an 80.21% identity security score. Policies enforced include MFA for privileged roles, blocking legacy authentication, and device-based access restrictions. I aligned most configurations with Microsoft’s Zero Trust recommendations while testing custom policies in Report-Only mode for iterative evaluation. This demonstrates my capability to operationalize adaptive access control using identity posture metrics to assess effectiveness and gaps.| ![Screenshot of Microsoft Entra ID Conditional Access Policies configuration](./assets/Conditional_access_policies.png)<br>![Screenshot showing Microsoft Entra ID Identity Security Score of 80.21%](./assets/Identity_score.png)  |
|**🖥️ Device monitoring in Endpoint Central**
 This view illustrates my endpoint vulnerability and patch compliance monitoring across a hybrid fleet using Endpoint Central, integrated with Microsoft Entra ID for device identity governance. It shows how I maintain visibility into OS versions, patch levels, critical vulnerabilities, and compliance status across remote and on-prem devices. My configuration supports automated patch deployment, threat detection, and device health tracking—forming a foundational layer of defense for endpoint hardening.                                                        | ![Screenshot of Endpoint Central device monitoring dashboard showing vulnerability status and patch compliance](./assets/Device_monitoring.png)|
|**Microsoft Purview Compliance Score (**97%**)**  
This updated screenshot reflects a 97% compliance score in Microsoft Purview Compliance Manager, showcasing my proactive enforcement of security, privacy, and regulatory controls across Microsoft 365 and hybrid cloud environments. I aligned policies and technical configurations with key frameworks including SOX, NYDFS, GLBA, NIST, PCI-DSS, CIS Controls, ISO 27001, and Microsoft’s internal security benchmarks. This score reflects my hands-on work in implementing conditional access, data loss prevention, secure device configurations, auditing policies, and user risk controls — all tracked and measured through Purview’s continuous assessments.   | ![Screenshot of Microsoft Purview Compliance Manager showing compliance score of 97%](./assets/Compliance_score.png) |


> All screenshots are real, redacted, and timestamped. No identifying or sensitive data is shown.



---

## 🧰 Tooling Stack

| Category             | Tools / Platforms                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------------|
| Identity & Access    | Microsoft Entra ID, Active Directory, AWS Identity Center, Zoho Identity360, FIM, SCIM, MFA, SSO       |
| Zero Trust Network   | Netbird VPN, Microsoft Global Secure Access (GSA), NSGs, Security Groups, Suricata IDS                 |
| Cloud Infrastructure | Azure (VMs, VNets, NSGs, Azure Monitor), AWS (IAM, EC2, S3, CloudWatch), Terraform                     |
| Endpoint & UEM       | Zoho Endpoint Central (UEM), Microsoft Defender for Endpoint (ATP), integrated with Entra ID           |
| SIEM & Monitoring    | Microsoft Defender XDR, Microsoft Sentinel, Azure Monitor, Site24x7, AWS CloudWatch, Log360            |
| Compliance & Governance   | Microsoft Purview, Microsoft Defender for Cloud, AWS Security Hub, Log360                         |
| DevSecOps & Code Security | GitHub Actions, CodeQL, Dependabot, Burp suite 

---

## 🧱 Zero Trust Pillars & Capabilities

| Zero Trust Pillar        | Implementation & Tools                                                                          |
|--------------------------|--------------------------------------------------------------------------------------------------|
| **Identity**             | Microsoft Entra ID, MFA, Conditional Access, Identity360, SCIM, SSO, AWS Identity Center         |
| **Devices**              | Zoho Endpoint Central (UEM), Microsoft Intune (if applicable), Compliance policies via Entra ID  |
| **Network**              | Netbird VPN, Microsoft Global Secure Access (GSA), Azure NSGs, AWS Security Groups               |
| **Applications**         | Conditional Access App Controls, SSO integrations, OAuth Scopes, Application Registrations       |
| **Data**                 | Microsoft Purview (DLP, Insider Risk Mgmt, Compliance Manager), Sensitivity Labels, eDiscovery   |
| **Infrastructure**       | Azure & AWS infrastructure secured via Terraform IaC, Defender for Cloud, AWS Security Hub       |
| **Visibility & Analytics** |Mcrosoft Defender XDR,  Microsoft Sentinel (SIEM), Azure Monitor, Site24x7, AWS CloudWatch, Log360|
| **Automation & Response**| Sentinel SOAR playbooks, Azure Logic Apps, Auto-remediation policies, Compliance Manager insights|


---
## 🚧 Future Projects: ObsidianWall Platform Initiative (In progress)
Security Infrastructure-as-Code (SIaC) — Designing a secure-by-default IaC framework focused on compliant, multi-cloud deployments.

---

## 📁 Repository Contents

```
├── assets/           # Diagrams and redacted screenshots
├── scripts/          # Optional Python automation scripts
├── policies/         # Optional Conditional Access policy exports
├── README.md         # This file
└── LICENSE
```

---

## 🚀 Why This Project?

This project represents my real-world cybersecurity engineering work:  
✅ Hands-on with modern hybrid security stacks  
✅ Built using Zero Trust principles  
✅ Demonstrates SecOps, IAM, and cloud infrastructure security in action

---

> 🧭 Want to see this in action or talk shop? Let’s connect on [LinkedIn](https://linkedin.com/in/aisha-3136031a0i) or [GitHub Discussions](https://github.com)!
