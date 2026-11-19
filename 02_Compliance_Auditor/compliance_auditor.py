import json
import csv
from pathlib import Path
from datetime import datetime

# Compliance auditor project directory
BASE_DIR = Path(__file__).parent

# Evidence output directory
EVIDENCE_DIR = BASE_DIR.parent / "04_Validation_Evidence"

# Compliance assessment results
AUDIT_RESULTS = []
def check_data_encryption(system):
    """
    Check encryption of sensitive data at rest and in transit.
    """
    findings = []

    if system.get("handles_sensitive_data", False):
        if system.get("encryption_at_rest") is not True:
            findings.append(
                "FAIL: Sensitive data is not encrypted at rest."
            )

        if system.get("encryption_in_transit") is not True:
            findings.append(
                "FAIL: Sensitive data is not encrypted in transit."
            )

        if not findings:
            findings.append(
                "PASS: Sensitive data is encrypted at rest and in transit."
            )
    else:
        findings.append(
            "REVIEW: System is not identified as handling sensitive data."
        )

    return findings

  
def check_cross_border_transfer(system):
    """
    Check whether cross-border data transfers have documented safeguards.
    """
    findings = []

    if system.get("cross_border_transfer", False):
        if system.get("transfer_safeguards_documented") is not True:
            findings.append(
                "FAIL: Cross-border transfer lacks documented safeguards."
            )

        if system.get("transfer_approved") is not True:
            findings.append(
                "FAIL: Cross-border transfer lacks documented approval."
            )

        if not findings:
            findings.append(
                "PASS: Cross-border transfer has documented safeguards and approval."
            )
    else:
        findings.append(
            "PASS: No cross-border data transfer reported."
        )

    return findings

# Section 4.3: Approved planning RPO targets (minutes)
RECOVERY_TARGETS = {
    "Identity and Authentication Services": 15,
    "Customer Database": 15,
    "Core Business Applications": 60,
    "Email and Communication Systems": 240,
    "Financial and Payment Systems": 15,
    "File Storage and Document Systems": 240,
    "Security Monitoring and Logging": 60,
    "Public Website": 240
}




def check_backup_compliance(system):
    """
    Check 3-2-1 backup compliance and Section 4.3 RPO targets.
    """
    findings = []

    # Check the 3-2-1 backup rule
    if system.get("backup_copies", 0) < 3:
        findings.append(
            "FAIL: Fewer than 3 backup copies are maintained."
        )
    else:
        findings.append("PASS: At least 3 backup copies maintained.")

    if system.get("storage_types", 0) < 2:
        findings.append(
            "FAIL: Backups are not maintained across 2 storage types."
        )
    else:
        findings.append("PASS: At least 2 storage types maintained.")

    if system.get("offline_or_immutable_backup") is not True:
        findings.append(
            "FAIL: No offline or immutable backup is documented."
        )
    else:
        findings.append(
            "PASS: Offline or immutable backup documented."
        )

    # Check the Section 4.3 RPO target
    asset_name = system.get("asset_name")
    actual_rpo = system.get("actual_rpo_minutes")
    target_rpo = RECOVERY_TARGETS.get(asset_name)

    if target_rpo is None:
        findings.append(
            "REVIEW: Asset is missing from the Section 4.3 RPO register."
        )
    elif actual_rpo is None:
        findings.append(
            f"REVIEW: Actual RPO evidence missing for {asset_name}."
        )
    elif not isinstance(actual_rpo, (int, float)) or actual_rpo < 0:
        findings.append(
            "FAIL: Actual RPO must be a valid non-negative number."
        )
    elif actual_rpo <= target_rpo:
        findings.append(
            f"PASS: Actual RPO of {actual_rpo} minutes "
            f"meets the {target_rpo}-minute target."
        )
    else:
        findings.append(
            f"FAIL: Actual RPO of {actual_rpo} minutes "
            f"exceeds the {target_rpo}-minute target."
        )

    return findings



def audit_backup_manifest():
    """
    Audit the backup manifest and save detailed CSV evidence.
    """
    manifest_path = BASE_DIR / "backup_manifest_test.csv"

    if not manifest_path.exists():
        print(f"ERROR: Backup manifest not found: {manifest_path}")
        return

    # Ensure the evidence directory exists
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    audit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    report_path = EVIDENCE_DIR / f"BCDR_Backup_Audit_{timestamp}.csv"

    print("\nBCDR 3-2-1 and RPO Compliance Audit")
    print("===================================")

    evidence_rows = []

    with open(manifest_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            system = {
                "asset_name": row["asset_name"].strip(),
                "backup_copies": int(row["backup_copies"]),
                "storage_types": int(row["storage_types"]),
                "offline_or_immutable_backup":
                    row["offline_or_immutable_backup"].strip().lower() == "true",
                "actual_rpo_minutes": int(row["actual_rpo_minutes"])
            }

            findings = check_backup_compliance(system)

            print(f"\nAsset: {system['asset_name']}")

            for finding in findings:
                print(f"  {finding}")

                status = finding.split(":", 1)[0]

                evidence_rows.append({
                    "audit_timestamp": audit_time,
                    "asset_name": system["asset_name"],
                    "status": status,
                    "finding": finding
                })

    # Save all findings to the evidence CSV
    with open(report_path, "w", newline="", encoding="utf-8-sig") as file:
        fieldnames = [
            "audit_timestamp",
            "asset_name",
            "status",
            "finding"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(evidence_rows)

    print("\nAudit evidence saved successfully.")
    print(f"Evidence report: {report_path}")


def audit_data_protection():
    """
    Audit data encryption and cross-border transfer compliance.
    """
    audit_time = datetime.now().isoformat(timespec="seconds")

    test_file = BASE_DIR / "data_protection_test.csv"
    report_path = EVIDENCE_DIR / "Data_Protection_Audit_Evidence.csv"

    evidence_rows = []

    if not test_file.exists():
        print(f"ERROR: Test file not found: {test_file}")
        return

    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    print("\nDATA PROTECTION COMPLIANCE AUDIT")
    print("================================")

    with open(test_file, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            system = {
                "system_name": row["system_name"].strip(),
                "handles_sensitive_data":
                    row["handles_sensitive_data"].strip().lower() == "true",
                "encryption_at_rest":
                    row["encryption_at_rest"].strip().lower() == "true",
                "encryption_in_transit":
                    row["encryption_in_transit"].strip().lower() == "true",
                "cross_border_transfer":
                    row["cross_border_transfer"].strip().lower() == "true",
                "transfer_safeguards_documented":
                    row["transfer_safeguards_documented"].strip().lower() == "true",
                "transfer_approved":
                    row["transfer_approved"].strip().lower() == "true"
            }

            findings = (
                check_data_encryption(system)
                + check_cross_border_transfer(system)
            )

            print(f"\nSystem: {system['system_name']}")

            for finding in findings:
                print(f"  {finding}")

                status = finding.split(":", 1)[0]

                evidence_rows.append({
                    "audit_timestamp": audit_time,
                    "system_name": system["system_name"],
                    "status": status,
                    "finding": finding
                })

    with open(report_path, "w", newline="", encoding="utf-8-sig") as file:
        fieldnames = [
            "audit_timestamp",
            "system_name",
            "status",
            "finding"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(evidence_rows)

    print("\nData Protection Audit completed.")
    print(f"Evidence report: {report_path}")


def audit_remediation_register():
    """Audit and summarize the GRC remediation register."""

    register_path = EVIDENCE_DIR / "GRC_Remediation_Register.csv"

    if not register_path.exists():
        print("\nERROR: Remediation register not found.")
        return

    with open(register_path, "r", newline="", encoding="utf-8-sig") as file:
        records = list(csv.DictReader(file))

    if not records:
        print("\nERROR: Remediation register is empty.")
        return

    total = len(records)

    status_counts = {}
    priority_counts = {}

    for record in records:
        status = record["Status"].strip()
        priority = record["Priority"].strip()

        status_counts[status] = status_counts.get(status, 0) + 1
        priority_counts[priority] = priority_counts.get(priority, 0) + 1

    outstanding = [
        record for record in records
        if record["Status"].strip().lower() in ("open", "under review")
    ]

    critical_high = [
        record for record in outstanding
        if record["Priority"].strip().lower() in ("critical", "high")
    ]


    today = datetime.now().date()
    overdue = []

    for record in outstanding:
        target_date_text = record["Target_Date"].strip()

        try:
            target_date = datetime.strptime(
                target_date_text, "%Y-%m-%d"
            ).date()

            if target_date < today:
                overdue.append(record)

        except ValueError:
            print(
                f"WARNING: Invalid target date for "
                f"{record['Finding_ID']}: {target_date_text}"
            )


    print("\nREMEDIATION TRACKING SUMMARY")
    print("============================")
    print(f"Total findings: {total}")

    print("\nStatus breakdown:")
    for status, count in sorted(status_counts.items()):
        print(f"{status}: {count}")

    print("\nPriority breakdown:")
    for priority, count in sorted(priority_counts.items()):
        print(f"{priority}: {count}")

    print(f"\nOutstanding findings: {len(outstanding)}")
    print(f"Outstanding Critical/High findings: {len(critical_high)}")

    print(f"Overdue findings: {len(overdue)}")

    for record in overdue:
        print(
            f"OVERDUE: {record['Finding_ID']} | "
            f"{record['System']} | "
            f"Deadline: {record['Target_Date']}"
        )

    report_path = EVIDENCE_DIR / "Remediation_Tracking_Summary.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("GRC REMEDIATION TRACKING SUMMARY\n")
        file.write("================================\n")
        file.write(f"Total findings: {total}\n\n")

        file.write("Status breakdown:\n")
        for status, count in sorted(status_counts.items()):
            file.write(f"{status}: {count}\n")

        file.write("\nPriority breakdown:\n")
        for priority, count in sorted(priority_counts.items()):
            file.write(f"{priority}: {count}\n")

        file.write(f"\nOutstanding findings: {len(outstanding)}\n")
        file.write(
            f"Outstanding Critical/High findings: {len(critical_high)}\n"
        )

        file.write(f"Overdue findings: {len(overdue)}\n")

        file.write("\nOverdue finding details:\n")
        for record in overdue:
            file.write(
                f"{record['Finding_ID']} | "
                f"{record['System']} | "
                f"Deadline: {record['Target_Date']}\n"
            )

        file.write("\nOutstanding Critical/High details:\n")
        for record in critical_high:
            file.write(
                f"{record['Finding_ID']} | {record['System']} | "
                f"{record['Priority']} | {record['Status']}\n"
            )

    print(f"\nRemediation summary saved: {report_path}")


print("GRC Compliance Auditor")
print("======================")
print("Auditor initialized successfully.")
print(f"Evidence directory: {EVIDENCE_DIR}")

audit_backup_manifest()
audit_data_protection()
audit_remediation_register()