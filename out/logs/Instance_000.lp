\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  28.57142857142857 a_max_0 + 1e+09 a_max_1 + 1e+09 a_max_2 + 1e+09 a_max_3
   + 20000 a_max_4 + 1000 a_max_5 + 100 a_min_0 + 666.6666666666666 a_min_1
   + 2000 a_min_2 + 2000 a_min_3 + 25000 a_min_4 + 2000 a_min_5
   + 0.1 b_min_0 + 1e+06 b_min_1 + 1e+06 b_min_2 + 1e+06 b_min_3
   + 25 b_min_4 + 2 b_min_5 + 0.1 b_max_0 + 1e+06 b_max_1 + 1e+06 b_max_2
   + 1e+06 b_max_3 + 25 b_max_4 + 2 b_max_5
Subject To
 demand_constr: x_0 + x_1 + x_2 + x_3 = 1000
 capacity_constr_0: x_0 <= 400
 capacity_constr_1: x_1 <= 400
 capacity_constr_2: x_2 <= 400
 capacity_constr_3: x_3 <= 400
 min_quality_constr_0: 5 x_0 - 5 x_1 + 15 x_2 + 15 x_3 + 1000 a_min_0
   >= -0
 max_quality_constr_0: - 40 x_0 - 50 x_1 - 30 x_2 - 30 x_3 - 1000 a_max_0
   <= -0
 goal_quality_constr_0: - 5 x_0 - 15 x_1 + 5 x_2 + 5 x_3 + b_min_0
   - b_max_0 = -0
 min_quality_constr_1: x_0 + 0.5 x_1 + x_2 + 2 x_3 + 1000 a_min_1 >= -0
 max_quality_constr_1: - 0.5 x_0 - x_1 - 0.5 x_2 + 0.5 x_3 - 1000 a_max_1
   <= -0
 goal_quality_constr_1: - 0.5 x_0 - x_1 - 0.5 x_2 + 0.5 x_3 + b_min_1
   - b_max_1 = -0
 min_quality_constr_2: 0.5 x_0 + 0.5 x_1 + 0.5 x_2 + 0.5 x_3 + 1000 a_min_2
   >= -0
 max_quality_constr_2: - 1000 a_max_2 <= -0
 goal_quality_constr_2: b_min_2 - b_max_2 = -0
 min_quality_constr_3: x_0 + x_1 + x_2 + x_3 + 1000 a_min_3 >= -0
 max_quality_constr_3: 0.5 x_0 + 0.5 x_1 + 0.5 x_2 + 0.5 x_3 - 1000 a_max_3
   <= -0
 goal_quality_constr_3: 0.5 x_0 + 0.5 x_1 + 0.5 x_2 + 0.5 x_3 + b_min_3
   - b_max_3 = -0
 min_quality_constr_4: 0.05 x_0 + 0.05 x_1 + 0.05 x_2 + 0.05 x_3
   + 1000 a_min_4 >= -0
 max_quality_constr_4: - 0.04 x_0 - 0.04 x_1 - 0.04 x_2 - 0.04 x_3
   - 1000 a_max_4 <= -0
 goal_quality_constr_4: 0.01 x_0 + 0.01 x_1 + 0.01 x_2 + 0.01 x_3 + b_min_4
   - b_max_4 = -0
 min_quality_constr_5: 0.5 x_0 + 0.5 x_1 - 0.5 x_2 + 1.5 x_3 + 1000 a_min_5
   >= -0
 max_quality_constr_5: - x_0 - x_1 - 2 x_2 - 1000 a_max_5 <= -0
 goal_quality_constr_5: - x_2 + x_3 + b_min_5 - b_max_5 = -0
Bounds
End
