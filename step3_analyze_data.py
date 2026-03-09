# ============================================================
#  STEP 3 — Analyse the Data & Generate Insights
#  Reads the clean data and prints key insights:
#    ✔ Overall statistics (average, highest, lowest)
#    ✔ Best and worst subjects
#    ✔ Grade-level performance
#    ✔ Attendance vs score relationship
#    ✔ Pass/Fail breakdown
# ============================================================

import pandas as pd

# ── Load clean data ───────────────────────────────────────
df = pd.read_csv("clean_student_data.csv")
print("=" * 55)
print("        📊  STUDENT DATA ANALYSIS REPORT")
print("=" * 55)


# ────────────────────────────────────────────────────────────
#  SECTION 1: Overall Statistics
# ────────────────────────────────────────────────────────────
print("\n📌 OVERALL STATISTICS")
print("-" * 40)
print(f"  Total students       : {df['student_id'].nunique()}")
print(f"  Total records        : {len(df)}")
print(f"  Average score        : {df['score'].mean():.1f}")
print(f"  Highest score        : {df['score'].max()}")
print(f"  Lowest score         : {df['score'].min()}")
print(f"  Average attendance   : {df['attendance_pct'].mean():.1f}%")


# ────────────────────────────────────────────────────────────
#  SECTION 2: Performance by Subject
# ────────────────────────────────────────────────────────────
print("\n📌 AVERAGE SCORE BY SUBJECT")
print("-" * 40)
subject_avg = df.groupby("subject")["score"].mean().sort_values(ascending=False)
for subject, avg in subject_avg.items():
    bar = "█" * int(avg // 5)   # simple text bar chart
    print(f"  {subject:<20} {avg:5.1f}  {bar}")

best_subject  = subject_avg.idxmax()
worst_subject = subject_avg.idxmin()
print(f"\n  🏆 Best subject   : {best_subject} ({subject_avg[best_subject]:.1f})")
print(f"  ⚠️  Weakest subject : {worst_subject} ({subject_avg[worst_subject]:.1f})")


# ────────────────────────────────────────────────────────────
#  SECTION 3: Performance by Grade Level
# ────────────────────────────────────────────────────────────
print("\n📌 AVERAGE SCORE BY GRADE LEVEL")
print("-" * 40)
grade_avg = df.groupby("grade_level")["score"].mean().sort_values(ascending=False)
for grade, avg in grade_avg.items():
    print(f"  {grade:<12} : {avg:.1f}")


# ────────────────────────────────────────────────────────────
#  SECTION 4: Grade Distribution (A / B / C / D / F)
# ────────────────────────────────────────────────────────────
print("\n📌 GRADE DISTRIBUTION")
print("-" * 40)
grade_counts = df["letter_grade"].value_counts().sort_index()
total = len(df)
for grade, count in grade_counts.items():
    pct = count / total * 100
    bar = "█" * int(pct // 3)
    print(f"  Grade {grade} : {count:>4} students  ({pct:.1f}%)  {bar}")


# ────────────────────────────────────────────────────────────
#  SECTION 5: Pass / Fail Rate
# ────────────────────────────────────────────────────────────
pass_count = (df["score"] >= 60).sum()
fail_count = (df["score"] <  60).sum()
pass_rate  = pass_count / len(df) * 100

print("\n📌 PASS / FAIL SUMMARY")
print("-" * 40)
print(f"  ✅ Passed : {pass_count} students ({pass_rate:.1f}%)")
print(f"  ❌ Failed : {fail_count} students ({100 - pass_rate:.1f}%)")


# ────────────────────────────────────────────────────────────
#  SECTION 6: Attendance Insight
# ────────────────────────────────────────────────────────────
high_att = df[df["attendance_pct"] >= 90]["score"].mean()
low_att  = df[df["attendance_pct"] <  75]["score"].mean()

print("\n📌 ATTENDANCE vs SCORE INSIGHT")
print("-" * 40)
print(f"  Students with ≥90% attendance → avg score : {high_att:.1f}")
print(f"  Students with <75% attendance → avg score : {low_att:.1f}")
print(f"  💡 Higher attendance correlates with "
      f"{abs(high_att - low_att):.1f} points difference on average.")


# ────────────────────────────────────────────────────────────
#  SECTION 7: Top 5 Students (by average score)
# ────────────────────────────────────────────────────────────
print("\n📌 TOP 5 STUDENTS (by average score)")
print("-" * 40)
top5 = (
    df.groupby("name")["score"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)
for rank, (name, avg) in enumerate(top5.items(), start=1):
    print(f"  {rank}. {name:<22} {avg:.1f}")

print("\n" + "=" * 55)
