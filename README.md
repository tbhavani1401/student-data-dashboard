# 📊 Student Data Analysis Dashboard

A beginner-friendly Python project that cleans messy student data and builds a fully formatted Excel dashboard with charts and insights.

---

## 📸 What It Does

| Step | File | What Happens |
|------|------|--------------|
| 1 | `step1_create_sample_data.py` | Creates a messy CSV with missing values and duplicates |
| 2 | `step2_clean_data.py` | Cleans the data — removes duplicates, fills gaps, fixes text |
| 3 | `step3_analyze_data.py` | Prints insights in the terminal |
| 4 | `step4_build_dashboard.py` | Builds a formatted Excel dashboard with charts |
| ▶ | `run_all.py` | Runs all 4 steps at once |

---

## 📋 Excel Dashboard Preview

The output `student_dashboard.xlsx` has 4 sheets:

- 📋 **Student Records** — full data table with colour-coded grades and performance
- 📊 **Summary Statistics** — KPI cards (avg score, pass rate, attendance) + pie chart
- 📈 **Subject Analysis** — average score per subject + bar chart
- 🗓️ **Attendance Report** — students ranked by attendance with progress bars

---

## 🔍 Insights Generated

- Overall average score, highest and lowest
- Best and worst performing subjects
- Grade level comparison (Grade 9 to 12)
- Grade distribution (A / B / C / D / F)
- Pass vs fail rate
- How attendance affects scores
- Top 5 students by average score

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/tbhavani1401/student-data-dashboard.git
cd student-data-dashboard
```

**2. Install the required libraries**
```bash
pip install -r requirements.txt
```

**3. Run everything at once**
```bash
python run_all.py
```

**4. Open the output file**
```
student_dashboard.xlsx
```

---

## 🛠️ Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Loading, cleaning and analysing data |
| `openpyxl` | Creating and formatting the Excel dashboard |

---

## 📁 Project Structure

```
student-data-dashboard/
│
├── step1_create_sample_data.py   # Generates a messy sample CSV
├── step2_clean_data.py           # Cleans and prepares the data
├── step3_analyze_data.py         # Prints analysis and insights
├── step4_build_dashboard.py      # Builds the Excel dashboard
├── run_all.py                    # Runs all steps in one command
├── requirements.txt              # Required Python libraries
└── README.md                     # Project documentation
```

---

## 💡 Use Your Own Data

You can swap in your own CSV file:

1. Open `step2_clean_data.py`
2. Change this line:
```python
df = pd.read_csv("sample_student_data.csv")
```
to:
```python
df = pd.read_csv("your_file.csv")
```
3. Update the column names in steps 3 and 4 to match your file.

---

## 🙋 About

Built as a beginner data analysis project using Python and Excel with the help of AI Tools.
Feel free to fork it, use it, or build on top of it!
