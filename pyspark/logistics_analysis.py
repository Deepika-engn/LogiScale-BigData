import pandas as pd

df = pd.read_csv("data/data.csv")

print(df.head())

print("Total Rows:", len(df))

print(df.info())

print(df.describe())

# Total shipments
total_shipments = len(df)

# On-time shipments
on_time = df["On_Time"].sum()

# Delayed shipments
delayed = total_shipments - on_time

# On-time percentage
on_time_percent = round((on_time / total_shipments) * 100, 2)

print("\n----- Shipment KPI -----")
print("Total Shipments:", total_shipments)
print("On-Time Shipments:", on_time)
print("Delayed Shipments:", delayed)
print("On-Time %:", on_time_percent)

# Route Analysis
route_analysis = df.groupby(
    ["Origin_City", "Destination_City"]
).agg(
    Total_Shipments=("Shipment_ID", "count"),
    On_Time_Rate=("On_Time", "mean")
)

print("\n----- Route Analysis -----")
print(route_analysis.head())

route_analysis.to_csv("data/route_analysis.csv")
# Shipment Type Analysis

shipment_analysis = df.groupby(
    "Shipment_Type"
).agg(
    Total_Shipments=("Shipment_ID", "count"),
    On_Time_Rate=("On_Time", "mean")
)

print("\n----- Shipment Type Analysis -----")
print(shipment_analysis)

shipment_analysis.to_csv(
    "data/shipment_analysis.csv"
)
# Customer Segment Analysis

customer_analysis = df.groupby(
    "Customer_Segment"
).agg(
    Total_Shipments=("Shipment_ID", "count"),
    On_Time_Rate=("On_Time", "mean")
)

print("\n----- Customer Segment Analysis -----")
print(customer_analysis)

customer_analysis.to_csv(
    "data/customer_analysis.csv"
)