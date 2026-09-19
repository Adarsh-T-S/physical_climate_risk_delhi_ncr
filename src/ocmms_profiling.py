from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
excel_file = PROJECT_ROOT / "data" / "raw" / "OCMMS_Central_Delhi.xlsx"

raw_df = pd.read_excel(
    excel_file,
    sheet_name="raw_1421",
    header=23
)

pilot_df = pd.read_excel(
    excel_file,
    sheet_name="pilot_100"
)

metadata_df = pd.read_excel(
    excel_file,
    sheet_name= "metadata"
)


print("\n=== INDUSTRY TYPE VALUES ===")
print(raw_df["Industry Type"].value_counts(dropna=False))

print("\n=== CATEGORY VALUES ===")
print(raw_df["Category"].value_counts(dropna=False))

print("\n=== FIRST 30 INDUSTRY NAMES ===")
print(raw_df["Industry Name"].head(30).to_string(index=False))

print("\n=== S.NO. CHECK ===")
print("Total records:", len(raw_df))
print("Unique S.No.: ", raw_df["S.No."].nunique())
print("Missing S.No.: ", raw_df["S.No."].isna().sum())

print("\n=== REPEATED INDUSTRY NAMES ===")
name_counts = raw_df["Industry Name"].value_counts()
print(
    name_counts[name_counts>1]
    .head(30)
)

print("\n=== ADDRESS SAMPLES ===")
print(raw_df["Industry Address"].head(30).to_string(index=False))
address_counts = raw_df["Industry Address"].value_counts()

print("\n=== REPEATED ADDRESSES ===")
print(address_counts[address_counts>1].head(30))

print("\n=== REGISTRATION DATE RANGE ===")
print("Earliest:", raw_df["Registration Date"].min())
print("Latest:", raw_df["Registration Date"].max())

print("\n=== RECORDS BY YEAR ===")
print(
    raw_df["Registration Date"]
    .dt.year
    .value_counts()
    .sort_index()
)

print("\n=== RECORDS WITH MISSING VALUES ===")
missing_records = raw_df[raw_df.isna().any(axis=1)]
print(missing_records.to_string(index=False))

print("\n=== PILOT ↔ RAW CHECK ===")
raw_names = set(raw_df["Industry Name"].dropna())
pilot_names = set(pilot_df["Industry Name"].dropna())

print("Pilot names:", len(pilot_names))
print("Pilot names found in raw: ", len(pilot_names.intersection(raw_names)))
print("Pilot names not found in raw: ", len(pilot_names - raw_names))