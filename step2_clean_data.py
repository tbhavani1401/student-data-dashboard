# ============================================================
#  STEP 2 — Clean the Dataset
#  Fixes common data problems:
#    ✔ Removes duplicate rows
#    ✔ Fills in missing values
#    ✔ Fixes inconsistent text (spaces, CAPS, etc.)
#    ✔ Adds letter grade and performance columns
# ============================================================

import pandas as pd

# ── Load the raw data ─────────────────────────────────────
print("📂 Loading raw data...")
df = pd.read_csv("sample_student_data.csv")

print(f"   Rows before cleaning : {len(df)}")
print(f"   Missing values       : {df.isna().sum().sum()}")
print(f"   Duplicate rows       : {df.duplicated().sum()}")


# ────────────────────────────────────────────────────────────
#  FIX 1: Remove duplicate rows
# ────────────────────────────────────────────────────────────
df = df.drop_duplicates()
print(f"\n✅ Removed duplicates → {len(df)} rows remaining")


# ────────────────────────────────────────────────────────────
#  FIX 2: Fill missing student names with "Unknown"
# ────────────────────────────────────────────────────────────
df["name"] = df["name"].fillna("Unknown Student")
print("✅ Filled missing names")


# ────────────────────────────────────────────────────────────
#  FIX 3: Fill missing scores with the average score
# ────────────────────────────────────────────────────────────
average_score = round(df["score"].mean(), 1)
df["score"] = df["score"].fillna(average_score)
print(f"✅ Filled missing scores with average ({average_score})")


# ────────────────────────────────────────────────────────────
#  FIX 4: Fix text columns (strip spaces, title-case)
# ────────────────────────────────────────────────────────────
df["name"]        = df["name"].str.strip().str.title()
df["subject"]     = df["subject"].str.strip().str.title()
df["grade_level"] = df["grade_level"].str.strip().str.title()
print("✅ Fixed text formatting (spaces, capitalisation)")


# ────────────────────────────────────────────────────────────
#  FIX 5: Convert score to a whole number (integer)
# ────────────────────────────────────────────────────────────
df["score"] = df["score"].astype(int)


# ────────────────────────────────────────────────────────────
#  ADD: Letter grade column based on score
# ────────────────────────────────────────────────────────────
def assign_letter_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

df["letter_grade"] = df["score"].apply(assign_letter_grade)
print("✅ Added 'letter_grade' column")


# ────────────────────────────────────────────────────────────
#  ADD: Performance label column
# ────────────────────────────────────────────────────────────
def assign_performance(score):
    """Assign a human-readable performance label."""
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 55:
        return "Average"
    else:
        return "Needs Improvement"

df["performance"] = df["score"].apply(assign_performance)
print("✅ Added 'performance' column")


# ── Save the clean data ───────────────────────────────────
df.to_csv("clean_student_data.csv", index=False)

print(f"\n📊 Final dataset: {len(df)} rows, {len(df.columns)} columns")
print("💾 Saved → clean_student_data.csv")
