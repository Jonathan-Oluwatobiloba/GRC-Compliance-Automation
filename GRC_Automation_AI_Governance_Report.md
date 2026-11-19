# CONTINUOUS COMPLIANCE-AS-CODE & AI REGULATORY GOVERNANCE

## Project Report

**Project:** GRC Automation and AI Regulatory Governance  
**Prepared:** 19 November 2026  
**Project Folder:** GRC_Compliance_Automation

---

## 1. EXECUTIVE SUMMARY

This project demonstrates the practical implementation of Continuous Compliance-as-Code and AI Regulatory Governance by transforming selected Governance, Risk and Compliance (GRC) activities into repeatable, automated and evidence-based processes.

The solution combines five major components:

1. **Automated Third-Party Risk Management:** A Python-based vendor assessment engine that applies weighted risk scoring across eight security and governance domains, with critical-risk overrides for serious encryption, privacy and contractual failures.
2. **Compliance-as-Code:** Automated Python rules that assess data protection, encryption, cross-border data transfers, backup resilience and Recovery Point Objective (RPO) requirements.
3. **Enterprise AI Governance:** Three governance documents establishing AI oversight, risk assessment, privacy safeguards and acceptable-use requirements for generative AI and autonomous agents.
4. **Remediation Tracking:** A consolidated register that records audit findings, corrective actions, priorities, ownership and target dates.
5. **Empirical Validation:** Demonstration tests using three vendor profiles and structured compliance datasets to verify the implemented controls.

The vendor risk engine assessed three demonstration vendors. SecureCloud Demonstration Ltd scored 88/100 and was approved. DataBridge Demonstration Ltd scored 84/100 but was rejected because of critical control failures, including unencrypted sensitive data at rest and a missing signed Data Processing Agreement. QuickServe Demonstration Ltd scored 68/100 and received conditional approval.

The compliance auditor assessed eight assets and generated 32 backup findings: 29 PASS and 3 FAIL. Its data protection assessment generated 11 findings: 6 PASS, 4 FAIL and 1 REVIEW. The remediation register tracks eight findings, including outstanding and overdue corrective actions.

These results demonstrate the system's ability to identify control weaknesses, enforce critical-risk decisions and support prioritised remediation. The project establishes a practical foundation for continuous compliance monitoring, automated risk assessment and responsible AI governance.

The results are based on demonstration datasets. They are not evidence of independent certification or complete regulatory compliance. Organisational adoption would require validation against actual business systems, and appropriate management, legal, privacy and security review.

## 2. PROJECT OBJECTIVES

The objectives were to:

- Operationalise a weighted third-party risk assessment methodology.
- Enforce critical security and privacy requirements through automated rules.
- Test backup resilience against 3-2-1, Recovery Point Objective (RPO) and Recovery Time Objective (RTO) requirements.
- Identify encryption and cross-border data protection gaps.
- Establish governance requirements for generative AI, large language models and autonomous AI agents.
- Generate audit evidence and track corrective actions.

## 3. SYSTEM ARCHITECTURE

The project is organised into four functional directories.

### 3.1 Third-Party Risk Management Engine

Directory: `01_TPRM_Engine`

Main components:

- `tprm_risk_engine.py` â€” vendor scoring and decision engine.
- `vendor_profiles/vendor_a.json` â€” compliant demonstration vendor.
- `vendor_profiles/vendor_b.json` â€” critical-risk override demonstration.
- `vendor_profiles/vendor_c.json` â€” medium-risk demonstration.
- `vendor_risk_register.csv` â€” generated vendor assessment register.
- `audit_summary.md` â€” generated assessment summary.

### 3.2 Compliance-as-Code Auditor

Directory: `02_Compliance_Auditor`

Main components:

- `compliance_auditor.py` â€” automated compliance rules and audit execution.
- `backup_manifest_test.csv` â€” backup configuration test data.
- `data_protection_test.csv` â€” data protection test data.

The auditor evaluates backup resilience, RPO requirements, encryption, cross-border transfers and remediation status.

### 3.3 AI Governance

Directory: `03_AI_Governance`

Policy documents:

- `01_Enterprise_AI_Governance_Policy.md`
- `02_AI_Risk_Assessment_Questionnaire.md`
- `03_AI_Privacy_and_Acceptable_Use_Controls.md`

These documents establish governance, risk assessment, privacy safeguards, acceptable-use requirements, autonomous-agent restrictions, monitoring and policy review.

### 3.4 Validation Evidence

Directory: `04_Validation_Evidence`

This directory contains generated audit exports, vendor assessment evidence, screenshots, remediation records and validation summaries.

## 4. AUTOMATED THIRD-PARTY RISK MANAGEMENT

### 4.1 Weighted Risk Scoring

The vendor risk engine assesses eight security and governance domains.

| Assessment domain | Weight |
|---|---:|
| SOC 2 | 15% |
| Encryption | 15% |
| Data Handling | 20% |
| Incident Response | 15% |
| Identity and Access | 10% |
| Business Continuity | 10% |
| Subcontractor Management | 5% |
| Legal and Regulatory | 10% |
| **Total** | **100%** |

The engine calculates a weighted score using the vendor's assessment ratings.

### 4.2 Critical-Risk Override

The engine checks for critical conditions that must override a favourable numerical score:

- Encryption at rest is disabled.
- A required Data Processing Agreement (DPA) is not signed.
- An unapproved cross-border transfer is identified.

A vendor triggering a critical override is classified as HIGH RISK and REJECTED regardless of its numerical score.

### 4.3 Vendor Validation Results

| Vendor | Score | Risk classification | Decision |
|---|---:|---|---|
| SecureCloud Demonstration Ltd | 88/100 | Low | Approved |
| DataBridge Demonstration Ltd | 84/100 | High | Rejected |
| QuickServe Demonstration Ltd | 68/100 | Medium | Conditional Approval |

**Validation interpretation:**

- Vendor A achieved 88/100 and was approved without a critical override.
- Vendor B achieved 84/100 but was rejected because critical controls failed, including encryption at rest and the signed DPA requirement.
- Vendor C achieved 68/100 and received conditional approval with remediation requirements.

The results demonstrate that a high numerical score does not automatically override critical privacy and security failures.

## 5. COMPLIANCE-AS-CODE POLICY GUARDRAILS

The compliance auditor implements Python-based rules to evaluate sample organisational control data.

### 5.1 Data Protection and Cross-Border Transfers

The data protection checks assess:

- Encryption at rest.
- Encryption in transit.
- Cross-border data transfers.
- Approval and documented safeguards for applicable transfers.
- Protection of Nigerian personal data and sensitive personal data.

The rules are intended to support the organisation's obligations under the Nigeria Data Protection Act (NDPA) 2023 and GDPR where applicable.

### 5.2 Data Protection Validation Results

Five systems were assessed, producing eleven findings.

| Result | Count |
|---|---:|
| PASS | 6 |
| FAIL | 4 |
| REVIEW | 1 |
| **Total** | **11** |

Identified issues included:

- Payment Processing System: encryption in transit failure.
- Employee Records: encryption at rest failure.
- Cloud Analytics Platform: cross-border transfer safeguards and approval failures.
- Public Website: review required because sensitive-data applicability was not established.

These results are recorded in `Data_Protection_Audit_Evidence.csv`.

### 5.3 BCDR 3-2-1 and RPO Validation

The backup compliance rule evaluates:

- At least three backup copies.
- At least two different storage types.
- At least one offline or immutable backup.
- Whether actual RPO values meet the applicable system targets.

The demonstration uses a 15-minute RPO target for relevant critical systems, including Identity and Financial databases.

The audit assessed eight assets and generated 32 findings.

| Result | Count |
|---|---:|
| PASS | 29 |
| FAIL | 3 |
| **Total** | **32** |

Three identified failures were:

1. Customer Database: actual RPO of 20 minutes against a 15-minute target.
2. Security Monitoring and Logging: no offline or immutable backup documented.
3. Public Website: fewer than three backup copies documented.

The latest recorded BCDR export is `BCDR_Backup_Audit_20261119_091455.csv`.

### 5.4 Remediation Tracking

The remediation register combines the BCDR and data-protection findings.

The latest recorded tracking summary reports:

- Total findings: 8.
- Open: 7.
- Under Review: 1.
- Critical: 1.
- High: 5.
- Medium: 1.
- Review: 1.
- Outstanding findings: 8.
- Outstanding Critical/High findings: 6.
- Overdue findings: 1.

The overdue demonstration item is BCDR-002, relating to Security Monitoring and Logging.

The register and tracking summary are:

- `GRC_Remediation_Register.csv`
- `Remediation_Tracking_Summary.txt`

The dates in the demonstration remediation register are test tracking dates, not confirmed organisational commitments.

## 6. ENTERPRISE AI GOVERNANCE

Three governance documents were prepared to establish responsible AI use and risk management.

### 6.1 Enterprise AI Governance Policy

The policy establishes:

- AI governance responsibilities and accountability.
- AI system inventory and approval.
- AI risk assessment and classification.
- NIST AI Risk Management Framework (AI RMF 1.0) alignment.
- Govern, Map, Measure and Manage control mapping.
- Privacy and security requirements.
- Human oversight and output validation.
- Third-party AI governance.
- Monitoring, incident management and policy review.

### 6.2 AI Risk Assessment Questionnaire

The questionnaire supports structured evaluation of AI systems.

Its assessment areas include:

- System purpose and governance.
- Data privacy.
- Training data provenance and model integrity.
- Cybersecurity and prompt injection.
- Fairness, accuracy and human oversight.
- Third-party AI provider risk.
- Risk classification, evidence and remediation.

It also addresses prompt injection defences, output logging, human review and approval.

### 6.3 AI Privacy and Acceptable-Use Controls

The acceptable-use controls establish restrictions on the disclosure of personal, sensitive and confidential information to AI services.

Key safeguards include:

- No unauthorised submission of customer PII or sensitive personal data to external AI services.
- Appropriate vendor assessment and contractual privacy safeguards.
- Data minimisation and anonymisation where appropriate.
- Verification of AI-generated information.
- Human approval for consequential decisions.
- Least-privilege access for autonomous agents.
- Restrictions on high-impact or irreversible agent actions.
- Activity logging, monitoring and the ability to suspend unsafe agents.

The policies support alignment with NDPA requirements and NIST AI RMF 1.0.

## 7. VALIDATION AND TESTING APPROACH

The project used sample vendor JSON profiles and CSV-based compliance datasets to test the implemented controls.

### 7.1 Vendor Risk Engine

Execution from the `02_Compliance_Auditor` directory:

`py ..\01_TPRM_Engine\tprm_risk_engine.py`

Expected validation scenarios:

- A compliant vendor is approved.
- A high-scoring vendor with critical control failures is rejected.
- A medium-risk vendor receives conditional approval.

### 7.2 Compliance Auditor

Execution from the `02_Compliance_Auditor` directory:

`py .\compliance_auditor.py`

The auditor executes the backup, data-protection and remediation checks against the configured test datasets and evidence register.

### 7.3 Code Validation

The Python auditor was syntax-checked using:

`py -m py_compile .\compliance_auditor.py`

No syntax errors were reported during the recorded validation.

## 8. EVIDENCE AND PROJECT OUTPUTS

The following evidence is retained in `04_Validation_Evidence`:

| Evidence | Purpose |
|---|---|
| `01_TPRM_Engine_Validation.png.png` | Vendor engine validation screenshot |
| `02_TPRM_Audit_Summary.png.png` | TPRM audit summary screenshot |
| `03_Vendor_Risk_Register.csv` | Vendor risk register export |
| `04_TPRM_Vendor_Register_Output.png` | Vendor register output screenshot |
| `BCDR_Validation_Summary.txt` | Backup compliance validation |
| `BCDR_Backup_Audit_20261119_091455.csv` | Latest recorded BCDR audit export |
| `Data_Protection_Audit_Evidence.csv` | Data-protection audit results |
| `GRC_Remediation_Register.csv` | Consolidated remediation register |
| `Remediation_Tracking_Summary.txt` | Remediation status summary |

Earlier audit exports and screenshots are retained as historical evidence.

## 9. LIMITATIONS AND FURTHER IMPROVEMENTS

The current implementation is a working demonstration, with the following limitations and recommended next steps:

1. **Input formats:** The vendor engine currently uses JSON profiles. YAML ingestion remains a future enhancement.
2. **Export naming:** The generated audit files contain audit timestamps, but the current output filenames are fixed. Timestamped filenames should be added to support retaining multiple independent runs.
3. **Policy engine:** Compliance guardrails are implemented in Python rather than OPA/Rego. Rego integration could be considered for a future policy-as-code deployment.
4. **Test data:** The results are based on demonstration datasets and should be replaced with verified organisational records before operational use.
5. **Regulatory review:** The policies and rules should be reviewed by qualified legal, privacy and compliance personnel before formal adoption.
6. **Operational deployment:** Production use would require access controls, protected audit storage, change management, scheduled execution and monitoring.

## 10. CONCLUSION

The project demonstrates a practical implementation of Continuous Compliance-as-Code and AI Regulatory Governance.

The vendor risk engine automates weighted assessments and critical-risk overrides. The compliance auditor evaluates backup resilience, encryption, cross-border transfer safeguards and remediation status. The AI governance documents establish a structured framework for responsible use of generative AI and autonomous agents.

The validation results demonstrate both successful control checks and meaningful control failures. The remediation register provides a basis for prioritising and tracking corrective actions.

The implementation provides a foundation for extending GRC activities towards continuous, measurable and evidence-based compliance.

---

**End of Project Report**


