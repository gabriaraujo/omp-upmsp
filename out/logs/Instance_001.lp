\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  285.7142857142857 a_max_00 + 1e+12 a_max_10 + 1e+11 a_max_20
   + 1e+11 a_max_30 + 2e+06 a_max_40 + 100000 a_max_50 + 1000 a_min_00
   + 666666.6666666666 a_min_10 + 200000 a_min_20 + 200000 a_min_30
   + 2.5e+06 a_min_40 + 200000 a_min_50 + 0.1 b_min_00 + 1e+06 b_min_10
   + 1e+06 b_min_20 + 1e+06 b_min_30 + 25 b_min_40 + 2 b_min_50
   + 0.1 b_max_00 + 1e+06 b_max_10 + 1e+06 b_max_20 + 1e+06 b_max_30
   + 25 b_max_40 + 2 b_max_50
Subject To
 input_weight_constr_0: y_00 + y_01 + y_02 + y_03 <= 100
 capacity_constr_0: y_00 <= -0
 weight_constr_00: x_00 - y_00 <= 400
 capacity_constr_1: y_01 <= 100
 weight_constr_10: x_10 - y_01 <= 300
 capacity_constr_2: y_02 <= 100
 weight_constr_20: x_20 - y_02 <= 300
 capacity_constr_3: y_03 <= 100
 weight_constr_30: x_30 - y_03 <= 300
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1000
 min_quality_constr_00: 5 x_00 - 5 x_10 + 15 x_20 + 15 x_30 + 1000 a_min_00
   >= -0
 max_quality_constr_00: - 40 x_00 - 50 x_10 - 30 x_20 - 30 x_30
   - 1000 a_max_00 <= -0
 goal_quality_constr_00: - 5 x_00 - 15 x_10 + 5 x_20 + 5 x_30
   + 1000 b_min_00 - 1000 b_max_00 = -0
 min_quality_constr_10: x_00 + 0.5 x_10 + x_20 + 2 x_30 + 1000 a_min_10
   >= -0
 max_quality_constr_10: - 0.5 x_00 - x_10 - 0.5 x_20 + 0.5 x_30
   - 1000 a_max_10 <= -0
 goal_quality_constr_10: - 0.5 x_00 - x_10 - 0.5 x_20 + 0.5 x_30
   + 1000 b_min_10 - 1000 b_max_10 = -0
 min_quality_constr_20: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   + 1000 a_min_20 >= -0
 max_quality_constr_20: - 1000 a_max_20 <= -0
 goal_quality_constr_20: 1000 b_min_20 - 1000 b_max_20 = -0
 min_quality_constr_30: x_00 + x_10 + x_20 + x_30 + 1000 a_min_30 >= -0
 max_quality_constr_30: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   - 1000 a_max_30 <= -0
 goal_quality_constr_30: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   + 1000 b_min_30 - 1000 b_max_30 = -0
 min_quality_constr_40: 0.05 x_00 + 0.05 x_10 + 0.05 x_20 + 0.05 x_30
   + 1000 a_min_40 >= -0
 max_quality_constr_40: - 0.04 x_00 - 0.04 x_10 - 0.04 x_20 - 0.04 x_30
   - 1000 a_max_40 <= -0
 goal_quality_constr_40: 0.01 x_00 + 0.01 x_10 + 0.01 x_20 + 0.01 x_30
   + 1000 b_min_40 - 1000 b_max_40 = -0
 min_quality_constr_50: 0.5 x_00 + 0.5 x_10 - 0.5 x_20 + 1.5 x_30
   + 1000 a_min_50 >= -0
 max_quality_constr_50: - x_00 - x_10 - 2 x_20 - 1000 a_max_50 <= -0
 goal_quality_constr_50: - x_20 + x_30 + 1000 b_min_50 - 1000 b_max_50
   = -0
Bounds
End
