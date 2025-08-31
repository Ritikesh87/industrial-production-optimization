# Industrial-Scale Production & Distribution Optimization
**Optimizing industrial production and supply chain operations with Pyomo & Python.**  
This project models a large-scale **production and distribution optimization** problem using **Pyomo** and **Gurobi**.

## Problem Overview
- 10 products produced in 3 factories
- Shipped through 5 warehouses to 5 stores
- Constraints: factory capacities, machine & labor hours, warehouse handling limits, transport costs
- Modeled variations: overtime allowed, unmet demand allowed, hybrid model

## Models
- `models/overtime_model.py` — allows overtime
- `models/unmet_model.py` — allows unmet demand with penalty
- `models/hybrid_model.py` — hybrid formulation

## How to run
overtime_model
```bash
pip install -r requirements.txt
python models/overtime_model.py
```
unmet_model
```bash
pip install -r requirements.txt
python models/unmet_model.py
```
hybrid_model
```bash
pip install -r requirements.txt
python models/hybrid_model.py
```

## Author
Ritikesh Dimri — Aspiring Operations Research Scientist

## License
This project is licensed under the [MIT License](LICENSE).

> ℹ️ Note: This project is still under development. Models and documentation are being updated frequently.



