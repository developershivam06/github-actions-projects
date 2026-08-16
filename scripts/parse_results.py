import xml.etree.ElementTree as ET
import os

REPORT = "reports/test-results.xml"

tree = ET.parse(REPORT)
root = tree.getroot()

total = int(root.find("testsuite").get("tests", 0))
failed = int(root.find("testsuite").get("failures", 0))
skipped = int(root.find("testsuite").get("skipped", 0))
errors = int(root.find("testsuite").get("errors", 0))

passed = total - failed - skipped - errors

print(f"Total: {total}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Skipped: {skipped}")
print(f"Errors: {errors}")

summary_file = os.getenv("GITHUB_STEP_SUMMARY")

if summary_file:
    with open(summary_file, "a") as f:
        f.write("## Test Summary ##\n\n")
        f.write("| Metric | Result |\n")
        f.write("|---|---:|\n")
        f.write(f"| Total | {total} |\n")
        f.write(f"| Passed | {passed} |\n")
        f.write(f"| Failed | {failed} |\n")
        f.write(f"| Skipped | {skipped} |\n")
        f.write(f"| Errors | {errors} |\n\n")

        if failed == 0 and errors == 0:
            f.write("### Status: ✅ PASSED\n")
        else:
            f.write("### Status: ❌ FAILED\n")