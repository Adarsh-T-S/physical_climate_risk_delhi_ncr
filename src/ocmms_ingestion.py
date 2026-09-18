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

print("Excel successfully loaded!")

print("Raw records: ", len(raw_df))
print("Pilot records: ", len(pilot_df))

print("\nRaw columns: ")
print(raw_df.columns.to_list())

print("\nRaw shape: ", raw_df.shape)
print("Pilot shape: ", pilot_df.shape)
print("Metadata shape: ", metadata_df.shape)

print("\nRaw data types: ")
print(raw_df.dtypes)
print("\nPilot data types: ")
print(pilot_df.dtypes)
print("\nMetadata data types: ")
print(metadata_df.dtypes)

print("\nRaw missing values: ")
print(raw_df.isna().sum())
print("\nPilot missing values: ")
print(pilot_df.isna().sum())
print("\n Metadata missing values: ")
print(metadata_df.isna().sum())


print("\nINGESTION CHECKPOINT PASSED")