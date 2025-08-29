# Industrial-Scale Production & Distribution Optimization

## Scenario
A company produces 10 products (P1–P10) in 3 factories (F1–F3), ships them to 5 warehouses (W1–W5), and distributes to 5 stores (S1–S5). The goal is to maximize net profit while respecting resource limits, transportation costs, and minimum store demands.

## Key Data & Constraints
- Product sale price, production cost, machine & labor hours per unit
- Factory: max production, machine & labor hours (overtime possible)
- Warehouse handling capacities
- Transport costs (Factory→Warehouse, Warehouse→Store)
- Each store has max capacity per product and minimum demand = 50% of capacity per product per store

## Objective
Maximize: Revenue − Transportation cost − Overtime cost − Penalty for unmet demand
