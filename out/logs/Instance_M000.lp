\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  28.57142857142857 a_max_00 + 25 a_max_01 + 1e+09 a_max_10 + 2000 a_max_11
   + 1e+09 a_max_20 + 5000 a_max_21 + 1e+09 a_max_30
   + 3333.333333333333 a_max_31 + 20000 a_max_40 + 50000 a_max_41
   + 1000 a_max_50 + 2000 a_max_51 + 100 a_min_00 + 200 a_min_01
   + 666.6666666666666 a_min_10 + 1000 a_min_11 + 2000 a_min_20
   + 3333.333333333333 a_min_21 + 2000 a_min_30 + 5000 a_min_31
   + 25000 a_min_40 + 14285.71428571428 a_min_41 + 2000 a_min_50
   + 1000 a_min_51 + 0.1 b_min_00 + 0.2 b_min_01 + 1e+06 b_min_10
   + 2 b_min_11 + 1e+06 b_min_20 + 5 b_min_21 + 1e+06 b_min_30 + 5 b_min_31
   + 25 b_min_40 + 50 b_min_41 + 2 b_min_50 + 2 b_min_51 + 0.1 b_max_0
   + 0.2 b_max_0 + 1e+06 b_max_1 + 2 b_max_1 + 1e+06 b_max_2 + 5 b_max_2
   + 1e+06 b_max_3 + 5 b_max_3 + 25 b_max_4 + 50 b_max_4 + 2 b_max_5
   + 2 b_max_5
Subject To
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1000
 capacity_constr_00: x_00 <= 400
 capacity_constr_10: x_10 <= 300
 capacity_constr_20: x_20 <= 300
 capacity_constr_30: x_30 <= 300
 min_quality_constr_00: 5 x_00 - 5 x_10 + 15 x_20 + 15 x_30 + 1000 a_min_00
   >= -0
 max_quality_constr_00: - 40 x_00 - 50 x_10 - 30 x_20 - 30 x_30
   - 1000 a_max_00 <= -0
 goal_quality_constr_00: - 5 x_00 - 15 x_10 + 5 x_20 + 5 x_30 + b_min_00
   - b_max_0 = -0
 min_quality_constr_10: x_00 + 0.5 x_10 + x_20 + 2 x_30 + 1000 a_min_10
   >= -0
 max_quality_constr_10: - 0.5 x_00 - x_10 - 0.5 x_20 + 0.5 x_30
   - 1000 a_max_10 <= -0
 goal_quality_constr_10: - 0.5 x_00 - x_10 - 0.5 x_20 + 0.5 x_30 + b_min_10
   - b_max_1 = -0
 min_quality_constr_20: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   + 1000 a_min_20 >= -0
 max_quality_constr_20: - 1000 a_max_20 <= -0
 goal_quality_constr_20: b_min_20 - b_max_2 = -0
 min_quality_constr_30: x_00 + x_10 + x_20 + x_30 + 1000 a_min_30 >= -0
 max_quality_constr_30: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   - 1000 a_max_30 <= -0
 goal_quality_constr_30: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   + b_min_30 - b_max_3 = -0
 min_quality_constr_40: 0.05 x_00 + 0.05 x_10 + 0.05 x_20 + 0.05 x_30
   + 1000 a_min_40 >= -0
 max_quality_constr_40: - 0.04 x_00 - 0.04 x_10 - 0.04 x_20 - 0.04 x_30
   - 1000 a_max_40 <= -0
 goal_quality_constr_40: 0.01 x_00 + 0.01 x_10 + 0.01 x_20 + 0.01 x_30
   + b_min_40 - b_max_4 = -0
 min_quality_constr_50: 0.5 x_00 + 0.5 x_10 - 0.5 x_20 + 1.5 x_30
   + 1000 a_min_50 >= -0
 max_quality_constr_50: - x_00 - x_10 - 2 x_20 - 1000 a_max_50 <= -0
 goal_quality_constr_50: - x_20 + x_30 + b_min_50 - b_max_5 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 800
 capacity_constr_01: x_01 <= 400
 capacity_constr_11: x_11 <= 300
 capacity_constr_21: x_21 <= 300
 capacity_constr_31: x_31 <= 300
 min_quality_constr_01: 5 x_01 - 5 x_11 + 15 x_21 + 15 x_31 + 800 a_min_01
   >= -0
 max_quality_constr_01: - 40 x_01 - 50 x_11 - 30 x_21 - 30 x_31
   - 800 a_max_01 <= -0
 goal_quality_constr_01: - 10 x_11 + 10 x_21 + 10 x_31 + b_min_01 - b_max_0
   = -0
 min_quality_constr_11: x_01 + 0.5 x_11 + x_21 + 2 x_31 + 800 a_min_11
   >= -0
 max_quality_constr_11: - 0.5 x_01 - x_11 - 0.5 x_21 + 0.5 x_31
   - 800 a_max_11 <= -0
 goal_quality_constr_11: - 0.5 x_11 + x_31 + b_min_11 - b_max_1 = -0
 min_quality_constr_21: 0.5 x_01 + 0.5 x_11 + 0.5 x_21 + 0.5 x_31
   + 800 a_min_21 >= -0
 max_quality_constr_21: - 800 a_max_21 <= -0
 goal_quality_constr_21: 0.2 x_01 + 0.2 x_11 + 0.2 x_21 + 0.2 x_31
   + b_min_21 - b_max_2 = -0
 min_quality_constr_31: x_01 + x_11 + x_21 + x_31 + 800 a_min_31 >= -0
 max_quality_constr_31: 0.5 x_01 + 0.5 x_11 + 0.5 x_21 + 0.5 x_31
   - 800 a_max_31 <= -0
 goal_quality_constr_31: 0.8 x_01 + 0.8 x_11 + 0.8 x_21 + 0.8 x_31
   + b_min_31 - b_max_3 = -0
 min_quality_constr_41: 0.05 x_01 + 0.05 x_11 + 0.05 x_21 + 0.05 x_31
   + 800 a_min_41 >= -0
 max_quality_constr_41: - 0.04 x_01 - 0.04 x_11 - 0.04 x_21 - 0.04 x_31
   - 800 a_max_41 <= -0
 goal_quality_constr_41: - 0.02 x_01 - 0.02 x_11 - 0.02 x_21 - 0.02 x_31
   + b_min_41 - b_max_4 = -0
 min_quality_constr_51: 0.5 x_01 + 0.5 x_11 - 0.5 x_21 + 1.5 x_31
   + 800 a_min_51 >= -0
 max_quality_constr_51: - x_01 - x_11 - 2 x_21 - 800 a_max_51 <= -0
 goal_quality_constr_51: - 0.5 x_01 - 0.5 x_11 - 1.5 x_21 + 0.5 x_31
   + b_min_51 - b_max_5 = -0
Bounds
End
