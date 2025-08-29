# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 19:32:55 2025

@author: Ritikesh Dimri
"""

import pyomo.environ as pyo
from pyomo.environ import *
import pandas as pd


# Importing data from sheet
A=pd.read_excel('sheet02.xlsx',sheet_name='Production')
B=pd.read_excel('sheet02.xlsx',sheet_name='Transportation_F_W')
C=pd.read_excel('sheet02.xlsx',sheet_name='Factory')
D=pd.read_excel('sheet02.xlsx',sheet_name='Warehouse')
E=pd.read_excel('sheet02.xlsx',sheet_name='Transportation_W_S')
G=pd.read_excel('sheet02.xlsx',sheet_name='Store_capacity')

#==============================================================================

model=ConcreteModel(name="Production_project")

#==============================================================================

'''Decision Variables'''

# p(i,j) represent unit of product i produced at factory j
model.p=Var(range(1,11),range(1,4),within=NonNegativeIntegers)
p=model.p

# q(i,j,k) represents the unit of product i trasported from factory j to 
#   warehouse k
model.q=Var(range(1,11),range(1,4),range(1,6),within=NonNegativeIntegers)
q=model.q

#r(i,k,s) represents units of ith product shipped from warehouse k to Store s.
model.r=Var(range(1,11),range(1,6),range(1,6),within=NonNegativeIntegers)
r=model.r

#extra machine hours at each factory
model.mh=Var(range(1,4),within=NonNegativeReals)
#extra labor hours at each factory
model.lh=Var(range(1,4),within=NonNegativeReals)
mh=model.mh; lh=model.lh

#u[i,s] represents unmet demand of product i at store s to meet min demand
model.u=Var(range(1,11),range(1,6),within=NonNegativeIntegers)
u=model.u

#==============================================================================

# Cost matrix for factory to warehouse transportation
cost_F_W=B.iloc[:,1:].values.tolist()
# cost matrix for warehouse to store transportation
cost_W_S=E.iloc[:,1:].values.tolist()

#Stores max capacity matrix
## Store-level aggregate min demand (50% of total capacity)
stores_max_cap_matrix=G.iloc[:,1:].values.tolist()

# profit
profit=sum(sum(
    r[i,k,s] for k in range(1,6) for s in range(1,6))*A.profit[i-1] 
    for i in range(1,11))
# total cost of transportation from F to W
Tcost_F_W=sum(cost_F_W[j-1][k-1]*sum(q[i,j,k] for i in range(1,11))
              for j in range(1,4) for k in range(1,6)) 
# cost of transportation from W to S
Tcost_W_S=sum(cost_W_S[k-1][s-1]*sum(r[i,k,s] for i in range(1,11))
              for k in range(1,6) for s in range(1,6)) 

#==============================================================================

'''Objective function'''
model.obj=Objective(expr=profit-Tcost_F_W-Tcost_W_S-
                    sum(250*mh[j]+300*lh[j] for j in range(1,4))-
                    500*sum(u[i,s] for i in range(1,11) for s in range(1,6))
                    ,sense=maximize)

'''Constraints'''

#labor constraints
model.C_labor=ConstraintList()
for j in range(1,4):
    model.C_labor.add(expr=sum(
            p[i,j]*A.Labor_hours[i-1] for i in range(1,11))<=
        C.Labor_Hours_Available[j-1]+lh[j])
    model.C_labor.add(expr=lh[j]<=0.1*C.Labor_Hours_Available[j-1])

#Machine Constraints
model.C_machine=ConstraintList()
for j in range(1,4):
    model.C_machine.add(expr=sum(
            p[i,j]*A.Machine_hours[i-1] for i in range(1,11))<=
        C.Machine_Hours_Available[j-1]+mh[j])
    model.C_machine.add(expr=mh[j]<=0.1*C.Machine_Hours_Available[j-1])

#Factory max production capacity constraints
model.C_maxcap=ConstraintList()
for j in range(1,4):
    model.C_maxcap.add(expr=sum(
        p[i,j] for i in range(1,11))<=
        C.Max_Production_Capacity_unitsperweek[j-1])

#p and q relation constraints
model.C_pq=ConstraintList()
for i in range(1,11):
    for j in range(1,4):
        model.C_pq.add(expr=p[i,j]==sum(q[i,j,k] for k in range(1,6)))

#warehouse handeling per week
model.C_WH=ConstraintList()
for k in range(1,6):
    model.C_WH.add(expr=sum(q[i,j,k] for i in range(1,11) for j in range(1,4))
                   <=D.HandlingCap_per_week[k-1])

#q and r relation constraints
model.C_qr=ConstraintList()
for i in range(1,11):
    for k in range(1,6):
        model.C_qr.add(expr=sum(r[i,k,s] for s in range(1,6))==
                                 sum(q[i,j,k] for j in range(1,4)))

# store max cap and min demand constraints
model.C_store=ConstraintList()
for i in range(1,11):
    for s in range(1,6):
        model.C_store.add(expr=sum(r[i,k,s] for k in range(1,6))<=
                                   stores_max_cap_matrix[i-1][s-1])
for i in range(1,11):
    for s in range(1,6):
        model.C_store.add(expr=sum(r[i,k,s] for k in range(1,6))+u[i,s]>=
                                   0.5*stores_max_cap_matrix[i-1][s-1])
        
#==============================================================================

opt=SolverFactory('gurobi')
#model.pprint()
result=opt.solve(model)
print(result)
for i in range(1,11):
        print(value(sum(p[i,j] for j in range(1,4))))
for i in range(1,11):
    for j in range(1,4):
        print(f"{p[i,j].value:03.0f}", end='   ')
    print()

for i in range(1, 11):
    for s in range(1, 6):
        total = sum(value(r[i, k, s]) for k in range(1, 6))  
        print(f"{total:02.0f}", end="   ")  
    print()
for i in range(1,11):
    for s in range(1,6):
        print(value(u[i,s]), end="  ")
    print()
print(value(model.obj)+500*value(sum(u[i,s]for i in range(1,11) 
                                        for s in range(1,6))))
