\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  48.49660523763335 a_max_00 + 58.68544600938965 a_max_01
   + 3030.30303030303 a_max_10 + 884.9557522123894 a_max_11 + 2500 a_max_20
   + 6250 a_max_21 + 2500 a_max_30 + 2222.222222222222 a_max_31
   + 1030.927835051546 a_max_40 + 1818.181818181818 a_max_41
   + 1136.363636363636 a_max_50 + 1639.344262295081 a_max_51
   + 41.0172272354389 a_min_00 + 35.76537911301861 a_min_01
   + 854.7008547008547 a_min_10 + 2702.702702702702 a_min_11
   + 10000 a_min_20 + 2941.176470588235 a_min_21 + 10000 a_min_30
   + 20000 a_min_31 + 33333.33333333334 a_min_40
   + 2222.222222222222 a_min_41 + 1612.903225806451 a_min_50
   + 1123.595505617978 a_min_51 + 0.0484966052376334 b_min_00
   + 0.0586854460093897 b_min_01 + 3.03030303030303 b_min_10
   + 2.702702702702703 b_min_11 + 10 b_min_20 + 6.25 b_min_21 + 10 b_min_30
   + 20 b_min_31 + 33.33333333333334 b_min_40 + 2.222222222222222 b_min_41
   + 1.612903225806451 b_min_50 + 1.639344262295081 b_min_51
   + 0.0484966052376334 b_max_00 + 0.0586854460093897 b_max_01
   + 3.03030303030303 b_max_10 + 2.702702702702703 b_max_11 + 10 b_max_20
   + 6.25 b_max_21 + 10 b_max_30 + 20 b_max_31 + 33.33333333333334 b_max_40
   + 2.222222222222222 b_max_41 + 1.612903225806451 b_max_50
   + 1.639344262295081 b_max_51
Subject To
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1162.1
 capacity_constr_00: x_00 <= 270.6
 capacity_constr_10: x_10 <= 410
 capacity_constr_20: x_20 <= 385.4
 capacity_constr_30: x_30 <= 359.5
 min_quality_constr_00: 15.88 x_00 + 33.73 x_10 + 4.57 x_20 - 11.34 x_30
   + 1162.1 a_min_00 >= -0
 max_quality_constr_00: - 29.12 x_00 - 11.27 x_10 - 40.43 x_20 - 56.34 x_30
   - 1162.1 a_max_00 <= -0
 goal_quality_constr_00: - 8.5 x_00 + 9.35 x_10 - 19.81 x_20 - 35.72 x_30
   + b_min_00 - b_max_00 = -0
 min_quality_constr_10: 1.14 x_00 + 1.38 x_10 + 0.84 x_20 + 1.31 x_30
   + 1162.1 a_min_10 >= -0
 max_quality_constr_10: - 0.36 x_00 - 0.12 x_10 - 0.66 x_20 - 0.19 x_30
   - 1162.1 a_max_10 <= -0
 goal_quality_constr_10: - 0.03 x_00 + 0.21 x_10 - 0.33 x_20 + 0.14 x_30
   + b_min_10 - b_max_10 = -0
 min_quality_constr_20: 3.46 x_00 + 6.7 x_10 + 4.29 x_20 + 6.81 x_30
   + 1162.1 a_min_20 >= -0
 max_quality_constr_20: 2.96 x_00 + 6.2 x_10 + 3.79 x_20 + 6.31 x_30
   - 1162.1 a_max_20 <= -0
 goal_quality_constr_20: 3.36 x_00 + 6.6 x_10 + 4.19 x_20 + 6.71 x_30
   + b_min_20 - b_max_20 = -0
 min_quality_constr_30: 5.07 x_00 + 4.5 x_10 + 0.15 x_20 + 4.09 x_30
   + 1162.1 a_min_30 >= -0
 max_quality_constr_30: 4.57 x_00 + 4 x_10 - 0.35 x_20 + 3.59 x_30
   - 1162.1 a_max_30 <= -0
 goal_quality_constr_30: 4.97 x_00 + 4.4 x_10 + 0.05 x_20 + 3.99 x_30
   + b_min_30 - b_max_30 = -0
 min_quality_constr_40: 1.15 x_00 + 1.34 x_10 + 1.33 x_20 + 0.53 x_30
   + 1162.1 a_min_40 >= -0
 max_quality_constr_40: 0.15 x_00 + 0.34 x_10 + 0.33 x_20 - 0.47 x_30
   - 1162.1 a_max_40 <= -0
 goal_quality_constr_40: 1.12 x_00 + 1.31 x_10 + 1.3 x_20 + 0.5 x_30
   + b_min_40 - b_max_40 = -0
 min_quality_constr_50: 0.21 x_00 + 1.44 x_10 + 3.01 x_20 + 2.56 x_30
   + 1162.1 a_min_50 >= -0
 max_quality_constr_50: - 1.29 x_00 - 0.06 x_10 + 1.51 x_20 + 1.06 x_30
   - 1162.1 a_max_50 <= -0
 goal_quality_constr_50: - 0.41 x_00 + 0.82 x_10 + 2.39 x_20 + 1.94 x_30
   + b_min_50 - b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 1110.5
 capacity_constr_01: x_01 <= 270.6
 capacity_constr_11: x_11 <= 410
 capacity_constr_21: x_21 <= 385.4
 capacity_constr_31: x_31 <= 359.5
 min_quality_constr_01: 15.88 x_01 + 33.73 x_11 + 4.57 x_21 - 11.34 x_31
   + 1110.5 a_min_01 >= -0
 max_quality_constr_01: - 29.12 x_01 - 11.27 x_11 - 40.43 x_21 - 56.34 x_31
   - 1110.5 a_max_01 <= -0
 goal_quality_constr_01: - 12.08 x_01 + 5.77 x_11 - 23.39 x_21 - 39.3 x_31
   + b_min_01 - b_max_01 = -0
 min_quality_constr_11: 1.14 x_01 + 1.38 x_11 + 0.84 x_21 + 1.31 x_31
   + 1110.5 a_min_11 >= -0
 max_quality_constr_11: - 0.36 x_01 - 0.12 x_11 - 0.66 x_21 - 0.19 x_31
   - 1110.5 a_max_11 <= -0
 goal_quality_constr_11: 0.77 x_01 + 1.01 x_11 + 0.47 x_21 + 0.94 x_31
   + b_min_11 - b_max_11 = -0
 min_quality_constr_21: 3.46 x_01 + 6.7 x_11 + 4.29 x_21 + 6.81 x_31
   + 1110.5 a_min_21 >= -0
 max_quality_constr_21: 2.96 x_01 + 6.2 x_11 + 3.79 x_21 + 6.31 x_31
   - 1110.5 a_max_21 <= -0
 goal_quality_constr_21: 3.12 x_01 + 6.36 x_11 + 3.95 x_21 + 6.47 x_31
   + b_min_21 - b_max_21 = -0
 min_quality_constr_31: 5.07 x_01 + 4.5 x_11 + 0.15 x_21 + 4.09 x_31
   + 1110.5 a_min_31 >= -0
 max_quality_constr_31: 4.57 x_01 + 4 x_11 - 0.35 x_21 + 3.59 x_31
   - 1110.5 a_max_31 <= -0
 goal_quality_constr_31: 5.02 x_01 + 4.45 x_11 + 0.1 x_21 + 4.04 x_31
   + b_min_31 - b_max_31 = -0
 min_quality_constr_41: 1.15 x_01 + 1.34 x_11 + 1.33 x_21 + 0.53 x_31
   + 1110.5 a_min_41 >= -0
 max_quality_constr_41: 0.15 x_01 + 0.34 x_11 + 0.33 x_21 - 0.47 x_31
   - 1110.5 a_max_41 <= -0
 goal_quality_constr_41: 0.7 x_01 + 0.89 x_11 + 0.88 x_21 + 0.08 x_31
   + b_min_41 - b_max_41 = -0
 min_quality_constr_51: 0.21 x_01 + 1.44 x_11 + 3.01 x_21 + 2.56 x_31
   + 1110.5 a_min_51 >= -0
 max_quality_constr_51: - 1.29 x_01 - 0.06 x_11 + 1.51 x_21 + 1.06 x_31
   - 1110.5 a_max_51 <= -0
 goal_quality_constr_51: - 0.68 x_01 + 0.55 x_11 + 2.12 x_21 + 1.67 x_31
   + b_min_51 - b_max_51 = -0
Bounds
End
