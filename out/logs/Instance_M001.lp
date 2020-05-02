\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  917.4311926605476 a_max_00 + 100.2004008016032 a_max_01
   + 8333.333333333327 a_max_10 + 10000 a_max_11
   + 5555.555555555556 a_max_20 + 4347.826086956522 a_max_21
   + 2173.913043478261 a_max_30 + 3448.275862068965 a_max_31
   + 1176.470588235294 a_max_40 + 1388.888888888889 a_max_41
   + 14285.71428571423 a_max_50 + 900.900900900901 a_max_51
   + 22.77385561375541 a_min_00 + 28.55511136493433 a_min_01
   + 724.6376811594204 a_min_10 + 714.2857142857143 a_min_11
   + 3125 a_min_20 + 3703.703703703703 a_min_21 + 25000 a_min_30
   + 4761.904761904761 a_min_31 + 6666.666666666667 a_min_40
   + 3571.428571428571 a_min_41 + 699.3006993006995 a_min_50
   + 2564.102564102564 a_min_51 + 0.9174311926605476 b_min_00
   + 0.1002004008016032 b_min_01 + 8.333333333333327 b_min_10 + 10 b_min_11
   + 5.555555555555555 b_min_20 + 4.347826086956522 b_min_21 + 25 b_min_30
   + 4.761904761904762 b_min_31 + 6.666666666666667 b_min_40
   + 3.571428571428571 b_min_41 + 14.28571428571423 b_min_50
   + 2.564102564102563 b_min_51 + 0.9174311926605476 b_max_00
   + 0.1002004008016032 b_max_01 + 8.333333333333327 b_max_10 + 10 b_max_11
   + 5.555555555555555 b_max_20 + 4.347826086956522 b_max_21 + 25 b_max_30
   + 4.761904761904762 b_max_31 + 6.666666666666667 b_max_40
   + 3.571428571428571 b_max_41 + 14.28571428571423 b_max_50
   + 2.564102564102563 b_max_51
Subject To
 capacity_constr_0: x_00 + x_01 <= 509.4
 capacity_constr_1: x_10 + x_11 <= 580.2
 capacity_constr_2: x_20 + x_21 <= 455
 capacity_constr_3: x_30 + x_31 <= 553.4
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1078.5
 min_quality_constr_00: 18.09 x_00 + 26.31 x_10 + 18.57 x_20 + 38.78 x_30
   + 1078.5 a_min_00 >= -0
 max_quality_constr_00: - 26.91 x_00 - 18.69 x_10 - 26.43 x_20 - 6.22 x_30
   - 1078.5 a_max_00 <= -0
 goal_quality_constr_00: - 25.82 x_00 - 17.6 x_10 - 25.34 x_20 - 5.13 x_30
   + b_min_00 - b_max_00 = -0
 min_quality_constr_10: 0.16 x_00 + 0.83 x_10 + 0.3 x_20 + 0.16 x_30
   + 1078.5 a_min_10 >= -0
 max_quality_constr_10: - 1.34 x_00 - 0.67 x_10 - 1.2 x_20 - 1.34 x_30
   - 1078.5 a_max_10 <= -0
 goal_quality_constr_10: - 1.22 x_00 - 0.55 x_10 - 1.08 x_20 - 1.22 x_30
   + b_min_10 - b_max_10 = -0
 min_quality_constr_20: 4.93 x_00 + 4.34 x_10 + 1.02 x_20 + 5.9 x_30
   + 1078.5 a_min_20 >= -0
 max_quality_constr_20: 4.43 x_00 + 3.84 x_10 + 0.52 x_20 + 5.4 x_30
   - 1078.5 a_max_20 <= -0
 goal_quality_constr_20: 4.61 x_00 + 4.02 x_10 + 0.7 x_20 + 5.58 x_30
   + b_min_20 - b_max_20 = -0
 min_quality_constr_30: 1.36 x_00 + 4.12 x_10 + 1.06 x_20 + 4.92 x_30
   + 1078.5 a_min_30 >= -0
 max_quality_constr_30: 0.86 x_00 + 3.62 x_10 + 0.56 x_20 + 4.42 x_30
   - 1078.5 a_max_30 <= -0
 goal_quality_constr_30: 1.32 x_00 + 4.08 x_10 + 1.02 x_20 + 4.88 x_30
   + b_min_30 - b_max_30 = -0
 min_quality_constr_40: 0.73 x_00 + 0.83 x_10 + 0.7 x_20 + 0.08 x_30
   + 1078.5 a_min_40 >= -0
 max_quality_constr_40: - 0.27 x_00 - 0.17 x_10 - 0.3 x_20 - 0.92 x_30
   - 1078.5 a_max_40 <= -0
 goal_quality_constr_40: 0.58 x_00 + 0.68 x_10 + 0.55 x_20 - 0.07 x_30
   + b_min_40 - b_max_40 = -0
 min_quality_constr_50: 1.21 x_00 + 2.23 x_10 + 0.15 x_20 - 0.33 x_30
   + 1078.5 a_min_50 >= -0
 max_quality_constr_50: - 0.29 x_00 + 0.73 x_10 - 1.35 x_20 - 1.83 x_30
   - 1078.5 a_max_50 <= -0
 goal_quality_constr_50: - 0.22 x_00 + 0.8 x_10 - 1.28 x_20 - 1.76 x_30
   + b_min_50 - b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 841.8
 min_quality_constr_01: 18.09 x_01 + 26.31 x_11 + 18.57 x_21 + 38.78 x_31
   + 841.8 a_min_01 >= -0
 max_quality_constr_01: - 26.91 x_01 - 18.69 x_11 - 26.43 x_21 - 6.22 x_31
   - 841.8 a_max_01 <= -0
 goal_quality_constr_01: - 16.93 x_01 - 8.71 x_11 - 16.45 x_21 + 3.76 x_31
   + b_min_01 - b_max_01 = -0
 min_quality_constr_11: 0.16 x_01 + 0.83 x_11 + 0.3 x_21 + 0.16 x_31
   + 841.8 a_min_11 >= -0
 max_quality_constr_11: - 1.34 x_01 - 0.67 x_11 - 1.2 x_21 - 1.34 x_31
   - 841.8 a_max_11 <= -0
 goal_quality_constr_11: - 1.24 x_01 - 0.57 x_11 - 1.1 x_21 - 1.24 x_31
   + b_min_11 - b_max_11 = -0
 min_quality_constr_21: 4.93 x_01 + 4.34 x_11 + 1.02 x_21 + 5.9 x_31
   + 841.8 a_min_21 >= -0
 max_quality_constr_21: 4.43 x_01 + 3.84 x_11 + 0.52 x_21 + 5.4 x_31
   - 841.8 a_max_21 <= -0
 goal_quality_constr_21: 4.66 x_01 + 4.07 x_11 + 0.75 x_21 + 5.63 x_31
   + b_min_21 - b_max_21 = -0
 min_quality_constr_31: 1.36 x_01 + 4.12 x_11 + 1.06 x_21 + 4.92 x_31
   + 841.8 a_min_31 >= -0
 max_quality_constr_31: 0.86 x_01 + 3.62 x_11 + 0.56 x_21 + 4.42 x_31
   - 841.8 a_max_31 <= -0
 goal_quality_constr_31: 1.15 x_01 + 3.91 x_11 + 0.85 x_21 + 4.71 x_31
   + b_min_31 - b_max_31 = -0
 min_quality_constr_41: 0.73 x_01 + 0.83 x_11 + 0.7 x_21 + 0.08 x_31
   + 841.8 a_min_41 >= -0
 max_quality_constr_41: - 0.27 x_01 - 0.17 x_11 - 0.3 x_21 - 0.92 x_31
   - 841.8 a_max_41 <= -0
 goal_quality_constr_41: 0.45 x_01 + 0.55 x_11 + 0.42 x_21 - 0.2 x_31
   + b_min_41 - b_max_41 = -0
 min_quality_constr_51: 1.21 x_01 + 2.23 x_11 + 0.15 x_21 - 0.33 x_31
   + 841.8 a_min_51 >= -0
 max_quality_constr_51: - 0.29 x_01 + 0.73 x_11 - 1.35 x_21 - 1.83 x_31
   - 841.8 a_max_51 <= -0
 goal_quality_constr_51: 0.82 x_01 + 1.84 x_11 - 0.24 x_21 - 0.72 x_31
   + b_min_51 - b_max_51 = -0
Bounds
End
