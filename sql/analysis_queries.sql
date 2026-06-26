#qery-1
SELECT COUNT(*) AS Total_Rows
FROM logistics;

#query-2
SELECT SUM(On_Time) AS On_Time_Shipments,COUNT(*)-SUM(On_Time) AS Delayed_Shipments
FROM logistics;

#query-3
SELECT ROUND((SUM(On_Time)*100.0)/COUNT(*),2) AS On_Time_Percentage
FROM logistics;

#query-4
SELECT Shipment_Type,COUNT(*) AS Total_Shipments,ROUND(AVG(On_Time)*100,2) AS On_Time_Rate
FROM logistics
GROUP BY Shipment_Type
ORDER BY Total_Shipments DESC;

#query-5
SELECT Customer_Segment,COUNT(*) AS Total_Shipments,ROUND(AVG(On_Time)*100,2) AS On_Time_Rate
FROM logistics
GROUP BY Customer_Segment
ORDER BY Total_Shipments DESC;

#query-6
SELECT Origin_City,Destination_City,COUNT(*) AS Total_Shipments,ROUND(AVG(On_Time)*100,2) AS On_Time_Rate
FROM logistics
GROUP BY Origin_City,Destination_City
ORDER BY Total_Shipments DESC;

#query-7
SELECT Origin_City,Destination_City,COUNT(*) AS Shipments
FROM logistics
GROUP BY Origin_City,Destination_City
ORDER BY Shipments DESC
LIMIT 10;

#query-8
SELECT ROUND(AVG(Delivery_Time_Days),2) AS Avg_Delivery_Time
FROM logistics;

#query-9
SELECT Shipment_Type,ROUND(AVG(Delivery_Time_Days),2) AS Avg_Delivery_Time
FROM logistics
GROUP BY Shipment_Type;

#query-10
SELECT Origin_City,COUNT(*) AS Total_Shipments
FROM logistics
GROUP BY Origin_City
ORDER BY Total_Shipments DESC;