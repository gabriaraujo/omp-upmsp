\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  22.22222222222222 a_max_00 + 1e+09 a_max_10 + 1e+09 a_max_20
   + 1e+09 a_max_30 + 20000 a_max_40 + 1000 a_max_50 + 1e+09 a_min_00
   + 666.6666666666666 a_min_10 + 2000 a_min_20 + 2000 a_min_30
   + 25000 a_min_40 + 2000 a_min_50 + 1e+06 b_min_00 + 1e+06 b_min_10
   + 1e+06 b_min_20 + 1e+06 b_min_30 + 25 b_min_40 + 2 b_min_50
   + 1e+06 b_max_00 + 1e+06 b_max_10 + 1e+06 b_max_20 + 1e+06 b_max_30
   + 25 b_max_40 + 2 b_max_50
Subject To
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1000
 capacity_constr_00: x_00 <= 400
 capacity_constr_10: x_10 <= 300
 capacity_constr_20: x_20 <= 300
 capacity_constr_30: x_30 <= 300
 min_quality_constr_00: 5 x_00 + 10 x_10 + 15 x_20 - 5 x_30 + 1000 a_min_00
   >= -0
 max_quality_constr_00: - 40 x_00 - 35 x_10 - 30 x_20 - 50 x_30
   - 1000 a_max_00 <= -0
 goal_quality_constr_00: 5 x_00 + 10 x_10 + 15 x_20 - 5 x_30 + b_min_00
   - b_max_00 = -0
 min_quality_constr_10: x_00 + 0.5 x_10 + x_20 + 2 x_30 + 1000 a_min_10
   >= -0
 max_quality_constr_10: - 0.5 x_00 - x_10 - 0.5 x_20 + 0.5 x_30
   - 1000 a_max_10 <= -0
 goal_quality_constr_10: - 0.5 x_00 - x_10 - 0.5 x_20 + 0.5 x_30 + b_min_10
   - b_max_10 = -0
 min_quality_constr_20: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   + 1000 a_min_20 >= -0
 max_quality_constr_20: - 1000 a_max_20 <= -0
 goal_quality_constr_20: b_min_20 - b_max_20 = -0
 min_quality_constr_30: x_00 + x_10 + x_20 + x_30 + 1000 a_min_30 >= -0
 max_quality_constr_30: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   - 1000 a_max_30 <= -0
 goal_quality_constr_30: 0.5 x_00 + 0.5 x_10 + 0.5 x_20 + 0.5 x_30
   + b_min_30 - b_max_30 = -0
 min_quality_constr_40: 0.05 x_00 + 0.05 x_10 + 0.05 x_20 + 0.05 x_30
   + 1000 a_min_40 >= -0
 max_quality_constr_40: - 0.04 x_00 - 0.04 x_10 - 0.04 x_20 - 0.04 x_30
   - 1000 a_max_40 <= -0
 goal_quality_constr_40: 0.01 x_00 + 0.01 x_10 + 0.01 x_20 + 0.01 x_30
   + b_min_40 - b_max_40 = -0
 min_quality_constr_50: 0.5 x_00 + 0.5 x_10 - 0.5 x_20 + 1.5 x_30
   + 1000 a_min_50 >= -0
 max_quality_constr_50: - x_00 - x_10 - 2 x_20 - 1000 a_max_50 <= -0
 goal_quality_constr_50: - x_20 + x_30 + b_min_50 - b_max_50 = -0
Bounds
End
