# Industrial-Scale Production & Distribution Optimization

This project models a large-scale **production and distribution optimization** problem using **Pyomo** and **Gurobi**.

## Problem Overview
- 10 products produced in 3 factories
- Shipped through 5 warehouses to 5 stores
- Constraints: factory capacities, machine & labor hours, warehouse handling limits, transport costs
- Modeled variations: overtime allowed, unmet demand allowed, hybrid model

## Models
- `models/complete_sheet_02_extrahours.py` — allows overtime
- `models/Complete_sheet02_unmetdemand.py` — allows unmet demand with penalty
- `models/complete_sheet_02_hybrid.py` — hybrid formulation

## How to run
```bash
pip install -r requirements.txt
python models/complete_sheet_02_extrahours.py
```

## Author
Ritikesh Dimri — Aspiring Operations Research Scientist
