markdown
# 🧹 CSV Cleaner

A lightweight Python script to clean and sanitize CSV files by removing empty rows, duplicates, and standardizing missing data. Built for freelancers, analysts, and anyone working with messy data files.

## 🚀 Features

- Strips whitespace from column names
- Converts empty strings and whitespace-only cells to `NaN`
- Removes:
  - Duplicate rows
  - Completely empty rows
  - Rows missing key information (e.g., Age and Email)
- Fills remaining missing values with `"MISSING"`
- Outputs a cleaned CSV file

## 📂 Input & Output

- **Input:** `sample.csv` (or any CSV file with basic data)
- **Output:** `cleaned_sample.csv` (overwrites if exists)

## 🛠 How to Use

1. Clone this repo or copy the script locally  
2. Place your CSV file in the same directory (e.g., `sample.csv`)  
3. Run the script:

   ```bash
   python clean_csv.py
   ```

4. The cleaned CSV will be saved as `cleaned_sample.csv`

## 🧪 Sample Workflow

```python
# Load original CSV
df = pd.read_csv("sample.csv")

# Clean the data
# (strip headers, remove duplicates, drop blanks, etc.)

# Save to new file
df.to_csv("cleaned_sample.csv", index=False)
```

## 📌 Requirements

- Python 3.x  
- `pandas`  
- `numpy`

Install dependencies:

```bash
pip install -r requirements.txt
```

## 📄 Example Use Case

- Cleaning scraped form submissions  
- Prepping messy survey results  
- Sanitizing exported user records

## 🤖 Author

**Geoff Jensen**  
Freelance Python Developer | Automation & Data Tools  
📧 jensen.geoff87@gmail.com

---

> 💡 *This project is part of a freelancing journey to build efficient, AI-assisted data tools. Follow along for updates and new releases!*
