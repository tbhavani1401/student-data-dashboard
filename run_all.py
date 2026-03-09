# ============================================================
#  run_all.py — Run the entire pipeline in one go
#  Runs all 4 steps back to back:
#    1. Create sample data
#    2. Clean the data
#    3. Analyse and print insights
#    4. Build the Excel dashboard
# ============================================================

import subprocess
import sys

steps = [
    "step1_create_sample_data.py",
    "step2_clean_data.py",
    "step3_analyze_data.py",
    "step4_build_dashboard.py",
]

print("=" * 50)
print("   🚀  DATA ANALYSIS DASHBOARD PIPELINE")
print("=" * 50)

for script in steps:
    print(f"\n▶  Running {script} ...")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"\n❌ Error in {script}. Please check above.")
        sys.exit(1)

print("\n" + "=" * 50)
print("🎉  Done! Open student_dashboard.xlsx to view.")
print("=" * 50)
