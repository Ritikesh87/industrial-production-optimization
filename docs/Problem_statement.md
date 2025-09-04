# Industrial-Scale Production & Distribution Optimization

## Scenario

A company produces **10 products (P1–P10)** in **3 factories (F1–F3)**, ships them to **5 warehouses (W1–W5)**, and distributes to **5 stores (S1–S5)**. The goal is to **maximize net profit** while respecting resource limits, transportation costs, and minimum store demands.

> **Unit conventions**: All quantities are **per week**. Currency: **₹ (INR)**.

---

## Objectives (three models)

1. [**Hybrid model**](../models/hybrid_model.py)  
   Maximize: **Revenue − Transportation cost − Overtime cost − Penalty for unmet demand**
2. [**Overtime model**](../models/overtime_model.py)    
   Maximize: **Revenue − Transportation cost − Overtime cost**
3. [**Unmet demand model**](../models/unmet_model.py)   
   Maximize: **Revenue − Transportation cost − Penalty for unmet demand**

---

## Data — Production

| Product | Selling Price (₹) | Production Cost (₹) | **Profit / unit (₹)** | Machine hrs / unit | Labor hrs / unit |
| :-----: | ----------------: | ------------------: | --------------------: | -----------------: | ---------------: |
|    P1   |              2500 |                1500 |              **1000** |                1.5 |              1.0 |
|    P2   |              2200 |                1500 |               **700** |                1.0 |              1.0 |
|    P3   |              2800 |                1600 |              **1200** |                2.0 |              0.5 |
|    P4   |              2000 |                1400 |               **600** |                1.0 |              0.5 |
|    P5   |              3200 |                2000 |              **1200** |                2.0 |              1.0 |
|    P6   |              2400 |                1700 |               **700** |                1.0 |              1.0 |
|    P7   |              3000 |                1800 |              **1200** |                1.5 |              1.0 |
|    P8   |              2700 |                1600 |              **1100** |                1.5 |              1.0 |
|    P9   |              2100 |                1400 |               **700** |                1.0 |              0.5 |
|   P10   |              2600 |                1900 |               **700** |                1.0 |              1.0 |

---

## Data — Factories

| Factory | Max production (units/week) | Machine hrs available | Labor hrs available |
| :-----: | --------------------------: | --------------------: | ------------------: |
|    F1   |                         800 |                   800 |                 600 |
|    F2   |                        1200 |                  1000 |                 700 |
|    F3   |                        1000 |                   600 |                 500 |

**Overtime (optional):** Cost = **₹250 / extra machine-hour**, **₹300 / extra labor-hour**.
**Overtime cap:** up to **20%** of available hours at each factory.

---

## Data — Warehouses

| Warehouse | Handling cap (units/week) |
| :-------: | ------------------------: |
|     W1    |                       800 |
|     W2    |                       500 |
|     W3    |                      1000 |
|     W4    |                       500 |
|     W5    |                       600 |

**Flow balance:** For each warehouse and product, **Inflows = Outflows** (no inventory holding across weeks).

---

## Data — Transport costs (Factory → Warehouse)

*All costs are in ₹/unit*

| Factory → Warehouse |  W1 |  W2 |  W3 |  W4 |  W5 |
| :------------------ | --: | --: | --: | --: | --: |
| **F1**              | 120 | 140 | 100 | 150 | 130 |
| **F2**              | 100 | 120 | 110 | 140 | 120 |
| **F3**              | 130 | 110 | 100 | 135 | 115 |

---

## Data — Transport costs (Warehouse → Store)

*All costs are in ₹/unit*

| Warehouse → Store | S1 | S2 | S3 | S4 | S5 |
| :---------------- | -: | -: | -: | -: | -: |
| **W1**            | 60 | 55 | 65 | 50 | 58 |
| **W2**            | 52 | 60 | 70 | 62 | 55 |
| **W3**            | 48 | 50 | 45 | 55 | 60 |
| **W4**            | 70 | 65 | 60 | 48 | 52 |
| **W5**            | 55 | 50 | 58 | 45 | 62 |

---

## Data — Store capacities (Max) and Min-demand rule

Each store has a **maximum capacity per product (Max)**. The model enforces a **minimum demand** equal to **50% of Max** for **each product per store**.

| Product |  S1 |  S2 | S3 |  S4 |  S5 |
| :-----: | --: | --: | -: | --: | --: |
|  **P1** |  80 |  75 | 60 |  95 |  70 |
|  **P2** |  70 |  85 | 90 | 100 |  65 |
|  **P3** |  90 |  95 | 70 |  85 |  80 |
|  **P4** | 100 |  70 | 80 |  75 |  85 |
|  **P5** |  60 | 100 | 95 |  80 |  90 |
|  **P6** |  50 |  65 | 75 |  90 |  60 |
|  **P7** |  85 |  90 | 85 |  70 |  95 |
|  **P8** |  95 |  80 | 65 |  85 | 100 |
|  **P9** |  75 |  85 | 70 |  95 |  85 |
| **P10** |  65 |  60 | 55 | 100 |  75 |

**Min-demand rule:** Each store must receive at least 50% of its listed capacity for each product. 

---

**Links**:  
1. Problem document (ODT): [Problem.odt](../docs/Problem.odt)  
2. Updated tables and data in Excel: [input.xlsx](../data/input.xlsx), used as input for the [models](../models).
