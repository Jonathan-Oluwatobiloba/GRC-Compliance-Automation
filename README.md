\# GRC Compliance Automation



**Project:** Continuous Compliance-as-Code and AI Regulatory Governance



## Project Overview



This project demonstrates how Python-based automation can support third-party risk management (TPRM), continuous compliance monitoring, business continuity and disaster recovery (BCDR), and enterprise AI governance.



## Project Components



### 1. Third-Party Risk Management

- Automated vendor risk scoring across eight weighted security and compliance domains.

- Critical-risk overrides for missing Data Processing Agreements, unencrypted data at rest, and unapproved cross-border transfers.

- CSV vendor risk register and Markdown audit summary.



### 2. Compliance-as-Code

- Automated data protection checks.

- Cross-border data transfer safeguards.

- Backup compliance validation against the 3-2-1 rule.

- Recovery Point Objective (RPO) and Recovery Time Objective (RTO) checks.

- Remediation tracking.



### 3. AI Governance

- Enterprise AI Governance Policy.

- AI Risk Assessment Questionnaire.

- AI Privacy and Acceptable Use Controls.

- Alignment with the NIST AI Risk Management Framework and Nigeria Data Protection Act (NDPA).



### 4. Validation Evidence

The project includes demonstration vendor profiles, generated audit outputs, compliance findings, remediation records, and validation screenshots.



## Project Structure

- `01_TPRM_Engine/` â€” vendor risk scoring engine and vendor profiles.
- `02_Compliance_Auditor/` â€” compliance and backup audit scripts and test data.
- `03_AI_Governance/` â€” AI governance and privacy policy documents.
- `04_Validation_Evidence/` â€” audit exports, validation results, and evidence.



## Technology



- Python 3

- PowerShell

- CSV and JSON

- Git and GitHub

- Markdown



## Important Notes



All vendor profiles and assessment records are demonstration data created for this project. The scripts are educational prototypes and should be reviewed, tested, and adapted before production use.



The current implementation uses JSON input and Python-based compliance checks. YAML support and OPA/Rego implementation are potential future enhancements.



## Author



Jonathan David Oluwatobiloba


## Demonstration Results

### Third-Party Risk Management (TPRM)

Three demonstration vendors were assessed:

| Vendor | Risk Score | Decision |
|---|---:|---|
| SecureCloud Demonstration Ltd | 88/100 | Approved |
| DataBridge Demonstration Ltd | 84/100 | Rejected |
| QuickServe Demonstration Ltd | 68/100 | Conditional Approval |

**Critical-risk validation:** DataBridge was rejected despite its score of 84/100 because of missing contractual data protection safeguards and unencrypted sensitive data at rest.

### Compliance-as-Code and BCDR

- 8 assets assessed against backup compliance requirements.
- 29 checks passed and 3 failed.
- Identified RPO, offline/immutable backup, and backup-copy weaknesses.
- Generated a remediation register for tracking corrective actions.

### Data Protection Monitoring

- 5 systems assessed.
- 6 checks passed, 4 failed, and 1 required review.
- Identified encryption and cross-border data transfer control weaknesses.

### Remediation Tracking

- 8 findings recorded.
- 7 Open and 1 Under Review.
- Critical, High, Medium, and Review priorities represented in the register.

### AI Governance

Developed three governance documents:

1. Enterprise AI Governance Policy.
2. AI Risk Assessment Questionnaire.
3. AI Privacy and Acceptable Use Controls.

The documents address the NIST AI Risk Management Framework and Nigeria Data Protection Act (NDPA).

**Disclaimer:** All assessment results are based on demonstration data and are not evidence of an actual organisation's regulatory compliance.

