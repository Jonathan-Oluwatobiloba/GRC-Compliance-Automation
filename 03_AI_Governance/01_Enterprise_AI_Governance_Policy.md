# ENTERPRISE AI GOVERNANCE POLICY



**Document Classification:** Internal — Governance and Compliance  

**Policy Owner:** Lead GRC & Compliance Analyst  

**Version:** 1.0  

**Status:** Draft for Management Review  

**Review Frequency:** Annually or following significant regulatory or technological changes



\---



## 1. PURPOSE



This policy establishes an enterprise-wide framework for the responsible, secure, transparent and lawful adoption and use of Artificial Intelligence (AI).



It defines governance responsibilities, risk management requirements, privacy safeguards, human oversight obligations and monitoring controls for AI systems used in organisational operations.



The objective is to ensure that AI technologies support business objectives without introducing unacceptable legal, ethical, operational, privacy or cybersecurity risks.



## 2. SCOPE



This policy applies to:



\- Employees, contractors, consultants and approved third-party service providers.

\- AI applications developed internally or acquired from external vendors.

\- Generative AI tools, large language models (LLMs), machine-learning systems, autonomous AI agents and automated decision-making tools.

\- AI systems that process organisational information, customer information, employee information or other personal data.



## 3. GOVERNANCE PRINCIPLES



All organisational AI systems must follow these principles:



1\. **Accountability:** Every AI system must have an assigned business owner.

2\. **Transparency:** AI use and significant automated decisions must be appropriately disclosed.

3\. **Fairness:** AI systems must be assessed for bias and discriminatory outcomes.

4\. **Privacy:** Personal information must be collected and processed lawfully.

5\. **Security:** AI systems must be protected against cyber threats and unauthorised access.

6\. **Human Oversight:** High-impact decisions must have appropriate human review.

7\. **Reliability:** AI outputs must be tested, monitored and validated before operational reliance.



## 4. AI SYSTEM APPROVAL AND INVENTORY



Before deployment, every AI system must undergo a documented approval process.



The organisation must maintain an AI inventory containing:



\- AI system name and business purpose.

\- System owner and responsible department.

\- AI vendor or developer.

\- Categories of data processed.

\- Intended users and affected individuals.

\- Risk classification.

\- Security and privacy assessment results.

\- Approval status and review date.



Unapproved AI systems must not be used to process confidential organisational information or personal data.



## 5. AI RISK ASSESSMENT



AI systems must undergo risk assessment before deployment and periodically thereafter.



Assessments must consider:



\- Data privacy and protection risks.

\- Cybersecurity vulnerabilities.

\- Algorithmic bias and discrimination.

\- Inaccurate or misleading AI outputs.

\- Prompt injection and malicious input manipulation.

\- Training-data quality and provenance.

\- Unauthorised access and data leakage.

\- Vendor dependency and third-party risks.

\- Inadequate human oversight.



High-risk AI systems must receive enhanced security and privacy reviews, documented management approval and ongoing monitoring before operational deployment.



## 6. NIST AI RISK MANAGEMENT FRAMEWORK ALIGNMENT



The organisation adopts the four functions of the NIST AI Risk Management Framework (AI RMF 1.0):



### 6.1 GOVERN



\- Establish AI governance roles and accountability.

\- Maintain an approved AI inventory.

\- Define acceptable-use requirements.

\- Assign responsibility for AI risk decisions.

\- Establish policies for third-party AI providers.

\- Provide relevant AI security and privacy awareness training.



### 6.2 MAP



\- Document the purpose and intended use of each AI system.

\- Identify affected individuals and business processes.

\- Identify data categories and processing locations.

\- Assess potential harm, misuse and operational impact.

\- Identify dependencies on external AI vendors and services.



### 6.3 MEASURE



\- Test AI systems for accuracy, reliability and security.

\- Evaluate bias and discriminatory outcomes.

\- Test prompt injection and data leakage protections.

\- Review training-data provenance and quality.

\- Maintain assessment records, test results and output logs where appropriate.



### 6.4 MANAGE



\- Apply controls to reduce identified AI risks.

\- Restrict or suspend systems presenting unacceptable risks.

\- Assign remediation actions and responsible owners.

\- Monitor deployed AI systems for performance and security changes.

\- Review incidents and update risk assessments.



## 7. DATA PRIVACY AND NDPA COMPLIANCE



AI systems processing personal data must comply with applicable Nigerian data protection requirements, including the Nigeria Data Protection Act (NDPA) 2023.



The organisation must:



\- Establish a lawful basis for personal data processing.

\- Apply data minimisation and purpose limitation.

\- Protect personal data against unauthorised disclosure.

\- Define retention and secure deletion requirements.

\- Assess third-party processors before sharing personal data.

\- Apply appropriate safeguards to international data transfers.

\- Maintain records of relevant privacy assessments and approvals.



Sensitive Personal Data (SPD) and other confidential information require enhanced protection.



Cross-border processing must be assessed against applicable NDPA transfer requirements. Where required, appropriate safeguards and documented transfer assessments must be maintained.



## 8. GENERATIVE AI AND LLM ACCEPTABLE USE



Employees and contractors must use only AI services approved by the organisation for business activities.



The following are prohibited unless specifically authorised through documented security and privacy approval:



\- Submitting customer PII or SPD to unapproved external LLM APIs.

\- Uploading confidential vendor records, credentials or internal documents to unapproved AI services.

\- Using AI-generated outputs as the sole basis for high-impact decisions.

\- Attempting to bypass AI security controls.

\- Using AI systems to generate malicious code, phishing content or unauthorised access instructions.

\- Connecting autonomous AI agents to business systems without documented approval and access restrictions.



Before an external AI provider processes personal data, the organisation must complete the necessary vendor security and privacy assessment and establish a signed Data Processing Agreement (DPA) where required.



Approved use of personal data must follow data minimisation and appropriate anonymisation or pseudonymisation safeguards.



## 9. AUTONOMOUS AI AGENT SECURITY



Autonomous AI agents must undergo additional security assessment before deployment.



Required safeguards include:



\- Least-privilege access to systems and data.

\- Human approval for sensitive or high-impact actions.

\- Restricted access to financial, identity and administrative functions.

\- Logging of agent actions and relevant decisions.

\- Monitoring of tool calls and external connections.

\- Protection against prompt injection and unauthorised instructions.

\- Ability to suspend or revoke agent access.

\- Testing in a controlled environment before production deployment.



Agents must not independently approve their own access permissions or override organisational security controls.



## 10. HUMAN OVERSIGHT AND OUTPUT VALIDATION



AI outputs must be reviewed before they are used for important business decisions.



Human review is mandatory for decisions involving:



\- Customer eligibility or access to essential services.

\- Employment and personnel decisions.

\- Financial approvals and transactions.

\- Legal, regulatory or compliance determinations.

\- Processing that could significantly affect an individual's rights.



Users remain accountable for decisions made using AI-generated information.



## 11. LOGGING, MONITORING AND INCIDENT MANAGEMENT



Approved AI systems must maintain appropriate records of:



\- User access and administrative activities.

\- Relevant prompts and AI outputs, subject to privacy and retention requirements.

\- Agent actions and connected tools.

\- Security events and policy violations.

\- Model changes and system updates.

\- Risk assessments and approval decisions.



AI-related incidents, including personal data exposure, prompt injection exploitation and unauthorised agent activity, must be reported through the organisation's incident response process.



The organisation must investigate incidents, document findings and implement corrective actions.



## 12. THIRD-PARTY AI VENDOR GOVERNANCE



AI vendors must undergo third-party risk assessment before approval.



Assessment areas include:



\- Security certifications and independent assurance.

\- Data encryption and access controls.

\- Data processing and retention practices.

\- Training-data provenance and use of customer data.

\- Incident notification obligations.

\- Subcontractor management.

\- Business continuity and disaster recovery.

\- Privacy compliance and international data transfers.



Vendor agreements must include appropriate confidentiality, security, privacy, incident notification and data deletion obligations.



## 13. POLICY VIOLATIONS AND ENFORCEMENT



Violations of this policy must be reported to the appropriate management, Information Security or GRC function.



The organisation may suspend access to AI systems where misuse, security weaknesses or unacceptable risks are identified.



Policy violations may result in corrective action in accordance with applicable organisational procedures and contractual obligations.



## 14. REVIEW AND CONTINUOUS IMPROVEMENT



This policy must be reviewed at least annually and whenever significant changes occur in:



\- Applicable data protection or AI regulations.

\- AI technologies and organisational use cases.

\- Cybersecurity threats.

\- Third-party AI services.

\- Organisational risk appetite.



The Lead GRC & Compliance Analyst is responsible for coordinating policy reviews and tracking approved changes.



## 15. APPROVAL



**Policy Owner:** Lead GRC & Compliance Analyst



**Management Approver:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



**Approval Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



**Next Review Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\---



*End of Enterprise AI Governance Policy.*


