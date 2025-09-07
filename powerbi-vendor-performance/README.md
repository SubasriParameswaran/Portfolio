# Vendor Performance — Power BI Notes

Project outline & DAX snippets you can turn into a repo or blog post.

## Business KPIs
- On-Time Delivery %
- In-Full %
- Lead Time (avg, P90) & variability
- Defect rate / NCR count
- Cost of late delivery

## Example DAX
```DAX
OnTime % :=
DIVIDE(
    CALCULATE(COUNTROWS(Shipments), Shipments[DeliveredOnOrBeforeDue] = TRUE() ),
    COUNTROWS(Shipments)
)
```

```DAX
Lead Time (days) :=
AVERAGEX(
    Shipments,
    DATEDIFF(Shipments[PO_Date], Shipments[Delivery_Date], DAY)
)
```
