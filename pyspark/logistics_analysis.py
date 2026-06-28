import pandas as pd

# Load dataset
df = pd.read_csv("data/data.csv")

# -----------------------------
# Replace Turkish values with English
# -----------------------------

# Shipment Type
df["Shipment_Type"] = df["Shipment_Type"].replace({
    "Kara": "Road",
    "Hava": "Air",
    "Deniz": "Sea"
})

# Customer Segment
df["Customer_Segment"] = df["Customer_Segment"].replace({
    "Bireysel": "Individual",
    "Kurumsal": "Corporate"
})

# Shipment Status (only if this column exists)
if "Shipment_Status" in df.columns:
    df["Shipment_Status"] = df["Shipment_Status"].replace({
        "Zamanında": "On Time",
        "Gecikmeli": "Delayed"
    })

# Save updated dataset
df.to_csv("data/data.csv", index=False)

print("Turkish values replaced successfully.\n")

# -----------------------------
# Data Exploration
# -----------------------------

print(df.head())

print("\nTotal Rows:", len(df))

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Shipment KPIs
# -----------------------------

total_shipments = len(df)

on_time = df["On_Time"].sum()

delayed = total_shipments - on_time

on_time_percent = round((on_time / total_shipments) * 100, 2)

print("\n----- Shipment KPI -----")
print("Total Shipments:", total_shipments)
print("On-Time Shipments:", on_time)
print("Delayed Shipments:", delayed)
print("On-Time %:", on_time_percent)

# -----------------------------
# Route Analysis
# -----------------------------

route_analysis = (
    df.groupby(["Origin_City", "Destination_City"])
      .agg(
          Total_Shipments=("Shipment_ID", "count"),
          On_Time_Rate=("On_Time", "mean"),
          Delayed_Shipments=("On_Time", lambda x: (x == 0).sum())
      )
      .reset_index()
)

print("\n----- Route Analysis -----")
print(route_analysis.head())

route_analysis.to_csv(
    "data/route_analysis.csv",
    index=False
)

# -----------------------------
# Shipment Type Analysis
# -----------------------------

shipment_analysis = (
    df.groupby("Shipment_Type")
      .agg(
          Total_Shipments=("Shipment_ID", "count"),
          On_Time_Rate=("On_Time", "mean"),
          Delayed_Shipments=("On_Time", lambda x: (x == 0).sum())
      )
      .reset_index()
)

print("\n----- Shipment Type Analysis -----")
print(shipment_analysis)

shipment_analysis.to_csv(
    "data/shipment_analysis.csv",
    index=False
)

# -----------------------------
# Customer Segment Analysis
# -----------------------------

customer_analysis = (
    df.groupby("Customer_Segment")
      .agg(
          Total_Shipments=("Shipment_ID", "count"),
          On_Time_Rate=("On_Time", "mean"),
          Delayed_Shipments=("On_Time", lambda x: (x == 0).sum())
      )
      .reset_index()
)

print("\n----- Customer Segment Analysis -----")
print(customer_analysis)

customer_analysis.to_csv(
    "data/customer_analysis.csv",
    index=False
)

print("\nAll files generated successfully!")