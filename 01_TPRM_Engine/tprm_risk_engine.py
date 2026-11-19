
"""
Continuous Compliance-as-Code
Third-Party Risk Management (TPRM) Engine

Project: Enterprise GRC Governance
"""

import json
import csv
import argparse
from datetime import datetime
from pathlib import Path

# ==========================================
# 1. TPRM ASSESSMENT CATEGORY WEIGHTS
# ==========================================

CATEGORY_WEIGHTS = {
    "soc2_assurance": 15,
    "encryption": 15,
    "data_handling_privacy": 20,
    "incident_response": 15,
    "identity_access_management": 10,
    "business_continuity": 10,
    "subcontractor_management": 5,
    "legal_regulatory_compliance": 10
}

# ==========================================
# 2. RISK CLASSIFICATION THRESHOLDS
# ==========================================

# Provisional thresholds based on the project
# validation examples. Confirm against Appendix A.

LOW_RISK_MINIMUM = 80
MEDIUM_RISK_MINIMUM = 60

# ==========================================
# 3. OUTPUT FILE LOCATIONS
# ==========================================

OUTPUT_DIRECTORY = Path(__file__).parent

REGISTER_FILE = OUTPUT_DIRECTORY / "vendor_risk_register.csv"
AUDIT_FILE = OUTPUT_DIRECTORY / "audit_summary.md"




# ==========================================
# 4. WEIGHTED VENDOR RISK CALCULATION
# ==========================================

def calculate_weighted_score(assessment):
    """
    Calculate the vendor's weighted score.

    Each category is scored from 0 to 5.
    The final result is converted to a score out of 100.
    """

    total_score = 0

    for category, weight in CATEGORY_WEIGHTS.items():

        if category not in assessment:
            raise ValueError(
                f"Missing assessment category: {category}"
            )

        rating = assessment[category]

        if isinstance(rating, bool) or not isinstance(rating, (int, float)):
            raise ValueError(
                f"{category} must have a numeric score."
            )

        if not 0 <= rating <= 5:
            raise ValueError(
                f"{category} must be between 0 and 5."
            )

        weighted_points = (rating / 5) * weight
        total_score += weighted_points

    return round(total_score, 2)


# ==========================================
# 5. CRITICAL-RISK OVERRIDE
# ==========================================

def check_critical_overrides(vendor):
    """
    Identify critical conditions that automatically
    make a vendor HIGH RISK and REJECTED.
    """

    overrides = []

    if vendor.get("encryption_at_rest") is False:
        overrides.append(
            "Sensitive data is not encrypted at rest."
        )

    if vendor.get("dpa_signed") is False:
        overrides.append(
            "A signed Data Processing Agreement is missing."
        )

    if vendor.get("unapproved_cross_border_transfer") is True:
        overrides.append(
            "Unapproved cross-border data transfer detected."
        )

    return overrides


# ==========================================
# 6. RISK CLASSIFICATION AND APPROVAL
# ==========================================

def classify_vendor(score, overrides):

    if overrides:
        return "HIGH RISK", "REJECTED"

    if score >= LOW_RISK_MINIMUM:
        return "LOW RISK", "APPROVED"

    if score >= MEDIUM_RISK_MINIMUM:
        return "MEDIUM RISK", "CONDITIONAL APPROVAL"

    return "HIGH RISK", "REJECTED"




# ==========================================
# 7. AUTOMATED REMEDIATION ACTION PLAN
# ==========================================

def generate_remediation_plan(vendor):

    actions = []

    if vendor.get("encryption_at_rest") is False:
        actions.append(
            "Implement AES-256 encryption at rest "
            "for all sensitive data."
        )

    if vendor.get("dpa_signed") is False:
        actions.append(
            "Execute and sign a Data Processing "
            "Agreement before processing personal data."
        )

    if vendor.get("unapproved_cross_border_transfer") is True:
        actions.append(
            "Suspend the unapproved transfer and "
            "implement documented lawful safeguards."
        )

    if vendor.get("incident_response") is not None:
        if vendor["incident_response"] < 3:
            actions.append(
                "Improve incident response procedures "
                "and contractual notification timelines."
            )

    if vendor.get("business_continuity") is not None:
        if vendor["business_continuity"] < 3:
            actions.append(
                "Strengthen business continuity and "
                "disaster recovery arrangements."
            )

    if not actions:
        actions.append(
            "No automatic remediation actions identified. "
            "Continue routine vendor monitoring."
        )

    return actions




# ==========================================
# 8. LOAD VENDOR ASSESSMENTS FROM JSON
# ==========================================

def load_vendor_assessment(file_path):
    """
    Read one vendor assessment from a JSON file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            vendor = json.load(file)

        required_fields = [
            "vendor_name",
            "soc2_assurance",
            "encryption",
            "data_handling_privacy",
            "incident_response",
            "identity_access_management",
            "business_continuity",
            "subcontractor_management",
            "legal_regulatory_compliance",
            "encryption_at_rest",
            "dpa_signed",
            "unapproved_cross_border_transfer"
        ]

        for field in required_fields:
            if field not in vendor:
                raise ValueError(
                    f"Missing required field: {field}"
                )

        return vendor

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in {file_path}: {error}"
        )


def load_all_vendor_assessments(input_directory):
    """
    Read every JSON vendor assessment in a folder.
    """

    input_directory = Path(input_directory)

    vendor_files = sorted(input_directory.glob("*.json"))

    if not vendor_files:
        raise FileNotFoundError(
            f"No JSON vendor profiles found in {input_directory}"
        )

    vendors = []

    for file_path in vendor_files:
        vendor = load_vendor_assessment(file_path)
        vendors.append(vendor)

    return vendors


# ==========================================
# 9. PROCESS EACH VENDOR
# ==========================================

def process_vendor(vendor):

    score = calculate_weighted_score(vendor)

    overrides = check_critical_overrides(vendor)

    risk_level, decision = classify_vendor(
        score, overrides
    )

    remediation = generate_remediation_plan(vendor)

    return {
        "vendor_name": vendor["vendor_name"],
        "risk_score": score,
        "risk_level": risk_level,
        "decision": decision,
        "critical_overrides": "; ".join(overrides) if overrides else "None",
        "remediation_actions": "; ".join(remediation)
    }



# ==========================================
# 10. EXPORT VENDOR RISK REGISTER TO CSV
# ==========================================

def export_vendor_register(results):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    fieldnames = [
        "vendor_name",
        "risk_score",
        "risk_level",
        "decision",
        "critical_overrides",
        "remediation_actions",
        "assessment_timestamp"
    ]

    with open(
        REGISTER_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for result in results:

            row = result.copy()
            row["assessment_timestamp"] = timestamp

            writer.writerow(row)

    print("\nVendor Risk Register exported:")
    print(REGISTER_FILE)



# ==========================================
# 11. GENERATE MARKDOWN AUDIT SUMMARY
# ==========================================

def generate_audit_summary(results):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    total_vendors = len(results)

    approved = sum(
        1 for item in results
        if item["decision"] == "APPROVED"
    )

    conditional = sum(
        1 for item in results
        if item["decision"] == "CONDITIONAL APPROVAL"
    )

    rejected = sum(
        1 for item in results
        if item["decision"] == "REJECTED"
    )

    report = [
        "# THIRD-PARTY RISK MANAGEMENT AUDIT SUMMARY",
        "",
        f"Assessment Date: {timestamp}",
        "",
        "## Executive Summary",
        "",
        f"- Total vendors assessed: {total_vendors}",
        f"- Approved vendors: {approved}",
        f"- Conditional approvals: {conditional}",
        f"- Rejected vendors: {rejected}",
        "",
        "## Vendor Assessment Results",
        ""
    ]

    for item in results:

        report.extend([
            f"### {item['vendor_name']}",
            "",
            f"- Risk Score: {item['risk_score']}/100",
            f"- Risk Level: {item['risk_level']}",
            f"- Decision: {item['decision']}",
            f"- Critical Overrides: {item['critical_overrides']}",
            "",
            "#### Remediation Actions",
            "",
            f"- {item['remediation_actions']}",
            ""
        ])

    report.extend([
        "## Audit Conclusion",
        "",
        "Vendor assessments were processed using the "
        "weighted TPRM scoring framework and critical-risk "
        "override controls.",
        "",
        "All decisions require appropriate GRC review, "
        "supporting evidence and management approval.",
        "",
        "---",
        "Generated automatically by the TPRM Risk Engine."
    ])

    with open(
        AUDIT_FILE,
        "w",
        encoding="utf-8"
    ) as report_file:

        report_file.write("\n".join(report))

    print("\nAudit summary generated:")
    print(AUDIT_FILE)



# ==========================================
# 12. MAIN COMMAND-LINE INTERFACE
# ==========================================

def main():

    parser = argparse.ArgumentParser(
        description="Automated Third-Party Risk Management Engine"
    )

    parser.add_argument(
        "--input-dir",
        default=str(OUTPUT_DIRECTORY / "vendor_profiles"),
        help="Folder containing vendor JSON assessment files"
    )

    args = parser.parse_args()

    print("\n====================================")
    print("      TPRM RISK ENGINE")
    print("====================================")

    try:

        print("\nLoading vendor assessments...")

        vendors = load_all_vendor_assessments(
            args.input_dir
        )

        print(f"Loaded {len(vendors)} vendor profiles.")

        results = []

        for vendor in vendors:

            result = process_vendor(vendor)
            results.append(result)

            print("\nVendor:", result["vendor_name"])
            print("Score:", result["risk_score"], "/100")
            print("Risk:", result["risk_level"])
            print("Decision:", result["decision"])

        export_vendor_register(results)

        generate_audit_summary(results)

        print("\n====================================")
        print("TPRM ASSESSMENT COMPLETED")
        print("====================================")

    except (ValueError, FileNotFoundError, OSError) as error:

        print("\nERROR:", error)
        raise SystemExit(1)


# ==========================================
# 13. START THE PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
