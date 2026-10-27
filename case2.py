# Case Study 02 (PDF #2): Progressive Electricity Billing & Spike Analysis


**Assigned Syllabus Concepts Used:** Multi-Slab Conditionals, Arithmetic Operators, Lists & Tuples, Trend Loops

---

## 1. Problem Statement

> **PDF Prompt (#2):** 2. Progressive Electricity Billing: Calculate household bills using multiple consumption slabs, fixed charges, surcharges, and rebates, then compare bills across several months and identify unusual increases.

Utility providers compute domestic electricity bills using progressive telescopic tariff slabs to encourage conservation while applying fixed meter charges, low-usage rebates, and high-load surcharges. Beyond single-month billing, households need longitudinal comparison across consecutive billing cycles to flag abnormal bill surges (>25% month-over-month rise) caused by faulty meters, seasonal HVAC loads, or appliance leakage.

---

## 2. Objectives

1. Compute accurate piecewise-linear energy charges across four progressive consumption slabs using `if-elif-else` branching.
2. Incorporate statutory fixed charges, conditional conservation rebates, and high-consumption surcharges into net payable bills.
3. Store multi-month billing summaries in a list of tuples and compute month-over-month percentage variations.
4. Detect and highlight unusual billing spikes exceeding 25.0% over the immediately preceding month.

---

## 3. Assumptions

- Tariff slabs are telescopic: 0–100 units @ Rs. 3.00/unit, 101–200 @ Rs. 5.00/unit, 201–400 @ Rs. 7.00/unit, and >400 @ Rs. 9.00/unit.
- Every monthly bill includes a fixed meter charge of Rs. 75.00.
- Households consuming <= 50 units receive a Rs. 25.00 green conservation rebate; consumption > 350 units attracts a 10% energy surcharge.
- Negative unit inputs, if entered erroneously, are sanitized to 0.0 units before slab computation.
- A month-over-month net bill increase strictly greater than 25.0% is classified as an UNUSUAL INCREASE.

---

## 4. Algorithm

- **Step 1:** Start the program.
- **Step 2:** Read `household_id` and number of billing months `num_months`. Set `fixed_charge = 75.0`.
- **Step 3:** Loop `num_months` times to read `month_name` and `units` consumed; clamp negative `units` to `0.0`.
- **Step 4:** Compute `energy_charge` using progressive slabs (`<=100`, `<=200`, `<=400`, `>400`).
- **Step 5:** Apply `rebate = 25.0` if `units <= 50`, or `surcharge = 0.10 * energy_charge` if `units > 350`.
- **Step 6:** Compute `net_bill = energy_charge + fixed_charge + surcharge - rebate` and store `(month_name, units, energy_charge, surcharge, rebate, net_bill)` in `monthly_records`.
- **Step 7:** Traverse `monthly_records` by index; accumulate `total_units` and `total_billed`.
- **Step 8:** For `idx > 0`, compare current `net_bill` against previous month `prev_bill` to compute `pct_change`. If `pct_change > 25.0`, append spike tuple to `unusual_spikes`.
- **Step 9:** Print itemized monthly statements, cumulative totals, monthly average, and all detected unusual spike alerts.
- **Step 10:** Stop the program.

---

## 5. Flowchart

![Flowchart - Progressive Electricity Billing & Spike Analysis](./flowchart.svg)

---

## 6. Pseudocode

```text
BEGIN
    INPUT household_id, num_months
    SET fixed_charge = 75.0, monthly_records = [], unusual_spikes = []

    FOR i = 1 TO num_months DO
        INPUT month_name, units
        IF units < 0 THEN SET units = 0.0 END IF

        IF units <= 100 THEN
            energy_charge = units * 3.0
        ELSE IF units <= 200 THEN
            energy_charge = 300.0 + (units - 100) * 5.0
        ELSE IF units <= 400 THEN
            energy_charge = 800.0 + (units - 200) * 7.0
        ELSE
            energy_charge = 2200.0 + (units - 400) * 9.0
        END IF

        SET rebate = 0.0, surcharge = 0.0
        IF units <= 50 THEN SET rebate = 25.0
        ELSE IF units > 350 THEN SET surcharge = 0.10 * energy_charge END IF

        SET net_bill = energy_charge + fixed_charge + surcharge - rebate
        APPEND (month_name, units, energy_charge, surcharge, rebate, net_bill) TO monthly_records
    END FOR

    FOR idx = 0 TO LENGTH(monthly_records) - 1 DO
        IF idx > 0 THEN
            pct_change = ((net_bill[idx] - net_bill[idx - 1]) / net_bill[idx - 1]) * 100
            IF pct_change > 25.0 THEN
                APPEND (month[idx - 1], month[idx], pct_change) TO unusual_spikes
            END IF
        END IF
        PRINT monthly_records[idx]
    END FOR
    PRINT totals, average, unusual_spikes
END
```

---

## 7. Python Source Code (`solution.py`)

```python
# Case Study 2 (PDF #2): Progressive Electricity Billing
# Syllabus Concepts: Variables, Operators, Multi-Slab Conditionals, Loops, Lists, Tuples, Unpacking

household_id = input("Enter Household Consumer ID: ").strip()
num_months = int(input("Enter number of months to analyse: "))

monthly_records = []
fixed_charge = 75.0

for i in range(num_months):
    raw = input("Enter MonthName,UnitsConsumed: ").strip()
    parts = raw.split(",")
    month_name = parts[0].strip()
    units = float(parts[1].strip())

    # Validate non-negative consumption
    if units < 0:
        units = 0.0

    # Progressive Consumption Slabs:
    # 0 - 100 units   : Rs. 3.00 / unit
    # 101 - 200 units : Rs. 5.00 / unit
    # 201 - 400 units : Rs. 7.00 / unit
    # Above 400 units : Rs. 9.00 / unit
    if units <= 100:
        energy_charge = units * 3.0
    elif units <= 200:
        energy_charge = (100 * 3.0) + ((units - 100) * 5.0)
    elif units <= 400:
        energy_charge = (100 * 3.0) + (100 * 5.0) + ((units - 200) * 7.0)
    else:
        energy_charge = (100 * 3.0) + (100 * 5.0) + (200 * 7.0) + ((units - 400) * 9.0)

    # Low-consumption rebate and high-load surcharge rules
    rebate = 0.0
    surcharge = 0.0
    if units <= 50:
        rebate = 25.0
    elif units > 350:
        surcharge = 0.10 * energy_charge

    net_bill = energy_charge + fixed_charge + surcharge - rebate
    if net_bill < 0:
        net_bill = 0.0

    monthly_records.append((month_name, units, energy_charge, surcharge, rebate, net_bill))

print("\n======================================================================")
print("         PROGRESSIVE ELECTRICITY BILLING & SPIKE ANALYSIS             ")
print("======================================================================")
print("Consumer ID:", household_id, "| Fixed Charge: Rs.", format(fixed_charge, ".2f"))
print("----------------------------------------------------------------------")

total_units = 0.0
total_billed = 0.0
unusual_spikes = []

for idx in range(len(monthly_records)):
    m_name, u_val, e_chg, sur, reb, net = monthly_records[idx]
    total_units = total_units + u_val
    total_billed = total_billed + net

    trend_note = "Baseline"
    if idx > 0:
        prev_month, prev_units, prev_e, prev_s, prev_r, prev_bill = monthly_records[idx - 1]
        if prev_bill > 0:
            pct_change = ((net - prev_bill) / prev_bill) * 100.0
        else:
            pct_change = 0.0

        if pct_change > 25.0:
            trend_note = "UNUSUAL INCREASE (+" + format(pct_change, ".1f") + "%)"
            unusual_spikes.append((prev_month, m_name, pct_change, net - prev_bill))
        elif pct_change >= 0:
            trend_note = "Normal (+" + format(pct_change, ".1f") + "%)"
        else:
            trend_note = "Decrease (" + format(pct_change, ".1f") + "%)"

    print(m_name, "| Units:", format(u_val, ".1f"), "| Energy:", format(e_chg, ".2f"), "| Sur:", format(sur, ".2f"), "| Reb:", format(reb, ".2f"), "| Net: Rs.", format(net, ".2f"), "|", trend_note)

avg_bill = 0.0
if num_months > 0:
    avg_bill = total_billed / num_months

print("----------------------------------------------------------------------")
print("Total Units:", format(total_units, ".1f"), "| Total Billed: Rs.", format(total_billed, ".2f"), "| Monthly Avg: Rs.", format(avg_bill, ".2f"))
if len(unusual_spikes) == 0:
    print("Spike Alert: No unusual bill increases (>25%) detected.")
else:
    for spike in unusual_spikes:
        from_m, to_m, pct, diff = spike
        print("Spike Alert:", to_m, "increased by", format(pct, ".1f") + "% (+Rs.", format(diff, ".2f") + ") compared to", from_m)
print("======================================================================")
```

---

## 8. Test Cases

| Test ID | Scenario | Sample Input (`stdin`) | Expected Behaviour | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** (Normal) | Four-month domestic profile spanning rebate, mid-slab, and summer surcharge spike | `HH-4092<br>4<br>Jan,45<br>Feb,160<br>Mar,175<br>Apr,420` | Applies Rs. 25 rebate in Jan (Rs. 185), flags Feb (+264.9%) and Apr (+259.1% with 10% surcharge) as unusual increases. | PASS |
| **TC-02** (Boundary / Tie) | Exact slab boundaries (50, 100, 200, 350 units) with steady controlled growth | `HH-1088<br>3<br>Jun,100<br>Jul,120<br>Aug,110` | Jun = Rs. 375.00, Jul = Rs. 475.00 (+26.7% flagged), Aug = Rs. 425.00 (-10.5% decrease). | PASS |
| **TC-03** (Edge / Validation) | Zero/vacant house usage and negative sensor reading sanitization | `HH-0019<br>2<br>Sep,-10<br>Oct,0` | Clamps -10 to 0.0 units, applies Rs. 25 rebate against Rs. 75 fixed fee = Rs. 50.00 net bill with zero spikes. | PASS |

---

## 9. Output Screenshots

### TC-01: Four-month domestic profile spanning rebate, mid-slab, and summer surcharge spike (Normal)

![Output Screenshot TC-01](./screenshots/output_TC-01.png)

<details>
<summary>View Raw Terminal Transcript (TC-01)</summary>

```text
Enter Household Consumer ID: HH-4092
Enter number of months to analyse: 4
Enter MonthName,UnitsConsumed: Jan,45
Enter MonthName,UnitsConsumed: Feb,160
Enter MonthName,UnitsConsumed: Mar,175
Enter MonthName,UnitsConsumed: Apr,420

======================================================================
         PROGRESSIVE ELECTRICITY BILLING & SPIKE ANALYSIS             
======================================================================
Consumer ID: HH-4092 | Fixed Charge: Rs. 75.00
----------------------------------------------------------------------
Jan | Units: 45.0 | Energy: 135.00 | Sur: 0.00 | Reb: 25.00 | Net: Rs. 185.00 | Baseline
Feb | Units: 160.0 | Energy: 600.00 | Sur: 0.00 | Reb: 0.00 | Net: Rs. 675.00 | UNUSUAL INCREASE (+264.9%)
Mar | Units: 175.0 | Energy: 675.00 | Sur: 0.00 | Reb: 0.00 | Net: Rs. 750.00 | Normal (+11.1%)
Apr | Units: 420.0 | Energy: 2380.00 | Sur: 238.00 | Reb: 0.00 | Net: Rs. 2693.00 | UNUSUAL INCREASE (+259.1%)
----------------------------------------------------------------------
Total Units: 800.0 | Total Billed: Rs. 4303.00 | Monthly Avg: Rs. 1075.75
Spike Alert: Feb increased by 264.9% (+Rs. 490.00) compared to Jan
Spike Alert: Apr increased by 259.1% (+Rs. 1943.00) compared to Mar
======================================================================
```
</details>

### TC-02: Exact slab boundaries (50, 100, 200, 350 units) with steady controlled growth (Boundary / Tie)

![Output Screenshot TC-02](./screenshots/output_TC-02.png)

<details>
<summary>View Raw Terminal Transcript (TC-02)</summary>

```text
Enter Household Consumer ID: HH-1088
Enter number of months to analyse: 3
Enter MonthName,UnitsConsumed: Jun,100
Enter MonthName,UnitsConsumed: Jul,120
Enter MonthName,UnitsConsumed: Aug,110

======================================================================
         PROGRESSIVE ELECTRICITY BILLING & SPIKE ANALYSIS             
======================================================================
Consumer ID: HH-1088 | Fixed Charge: Rs. 75.00
----------------------------------------------------------------------
Jun | Units: 100.0 | Energy: 300.00 | Sur: 0.00 | Reb: 0.00 | Net: Rs. 375.00 | Baseline
Jul | Units: 120.0 | Energy: 400.00 | Sur: 0.00 | Reb: 0.00 | Net: Rs. 475.00 | UNUSUAL INCREASE (+26.7%)
Aug | Units: 110.0 | Energy: 350.00 | Sur: 0.00 | Reb: 0.00 | Net: Rs. 425.00 | Decrease (-10.5%)
----------------------------------------------------------------------
Total Units: 330.0 | Total Billed: Rs. 1275.00 | Monthly Avg: Rs. 425.00
Spike Alert: Jul increased by 26.7% (+Rs. 100.00) compared to Jun
======================================================================
```
</details>

### TC-03: Zero/vacant house usage and negative sensor reading sanitization (Edge / Validation)

![Output Screenshot TC-03](./screenshots/output_TC-03.png)

<details>
<summary>View Raw Terminal Transcript (TC-03)</summary>

```text
Enter Household Consumer ID: HH-0019
Enter number of months to analyse: 2
Enter MonthName,UnitsConsumed: Sep,-10
Enter MonthName,UnitsConsumed: Oct,0

======================================================================
         PROGRESSIVE ELECTRICITY BILLING & SPIKE ANALYSIS             
======================================================================
Consumer ID: HH-0019 | Fixed Charge: Rs. 75.00
----------------------------------------------------------------------
Sep | Units: 0.0 | Energy: 0.00 | Sur: 0.00 | Reb: 25.00 | Net: Rs. 50.00 | Baseline
Oct | Units: 0.0 | Energy: 0.00 | Sur: 0.00 | Reb: 25.00 | Net: Rs. 50.00 | Normal (+0.0%)
----------------------------------------------------------------------
Total Units: 0.0 | Total Billed: Rs. 100.00 | Monthly Avg: Rs. 50.00
Spike Alert: No unusual bill increases (>25%) detected.
======================================================================
```
</details>

---

## 10. Conclusion

Progressive Electricity Billing demonstrates how multi-branch conditional statements and tuple-based longitudinal records accurately model real-world utility tariffs while automatically surfacing abnormal consumption spikes.
