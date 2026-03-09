# ============================================================
#  STEP 1 — Create a Sample Student Dataset
#  Creates a messy CSV file that looks like real-world data
#  (with missing values, duplicates, and formatting issues)
# ============================================================

import pandas as pd
import random

# Set a seed so we always get the same random data
random.seed(42)

# ── Student information ───────────────────────────────────
names = [
    "Alice Johnson", "Bob Smith", "Clara Davis", "David Lee",
    "Eva Martinez", "Frank Wilson", "Grace Kim", "Henry Brown",
    "Isla Clark", "Jack White", "Karen Hall", "Liam Young",
    "Mia Scott", "Noah Adams", "Olivia Baker", "Paul Carter",
    "Quinn Evans", "Rose Foster", "Sam Green", "Tina Harris",
    "Uma Patel", "Victor Nguyen", "Wendy Chen", "Xander Roy",
    "Yara Singh", "Zoe Turner"
]

subjects  = ["Math", "Science", "English", "History", "Computer Science"]
grades    = ["Grade 9", "Grade 10", "Grade 11", "Grade 12"]

# ── Build rows of data ────────────────────────────────────
rows = []
for i, name in enumerate(names):
    for subject in subjects:
        score = random.randint(40, 100)
        rows.append({
            "student_id":     f"S{i+1:03d}",
            "name":           name,
            "grade_level":    random.choice(grades),
            "subject":        subject,
            "score":          score,
            "attendance_pct": random.randint(55, 100),
            "test1":          random.randint(35, 100),
            "test2":          random.randint(35, 100),
            "test3":          random.randint(35, 100),
        })

df = pd.DataFrame(rows)

# ── Introduce messy data (like real-world datasets!) ──────

# Add some missing scores
for idx in random.sample(range(len(df)), 15):
    df.at[idx, "score"] = None

# Add some missing names
for idx in random.sample(range(len(df)), 5):
    df.at[idx, "name"] = None

# Add duplicate rows
duplicates = df.sample(8, random_state=1)
df = pd.concat([df, duplicates], ignore_index=True)

# Add inconsistent text formatting
df.loc[5,  "subject"]     = "  math "    # extra spaces
df.loc[10, "subject"]     = "SCIENCE"    # all caps
df.loc[20, "grade_level"] = "grade 9"   # lowercase

# Save to CSV
df.to_csv("sample_student_data.csv", index=False)

print("✅ sample_student_data.csv created!")
print(f"   Total rows    : {len(df)}")
print(f"   Missing scores: {df['score'].isna().sum()}")
print(f"   Duplicate rows: {duplicates.shape[0]}")
