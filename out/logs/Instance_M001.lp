\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  15625 a_max_00 + 315.4574132492114 a_max_01
   + 4.7619047619047621e+06 a_max_10 + 826446.2809917355 a_max_11
   + 250000 a_max_20 + 909090.9090909093 a_max_21 + 250000 a_max_30
   + 357142.8571428571 a_max_31 + 108695.652173913 a_max_40
   + 370370.3703703703 a_max_41 + 102040.8163265306 a_max_50
   + 131578.9473684211 a_max_51 + 225.4283137962128 a_min_00
   + 751.8796992481205 a_min_01 + 775193.7984496123 a_min_10
   + 3.4482758620689656e+06 a_min_11 + 1e+06 a_min_20
   + 256410.2564102564 a_min_21 + 1e+06 a_min_30
   + 454545.4545454546 a_min_31 + 1.25e+06 a_min_40
   + 136986.301369863 a_min_41 + 192307.6923076925 a_min_50
   + 135135.1351351351 a_min_51 + 1.5625 b_min_00
   + 0.075187969924812 b_min_01 + 4.761904761904763 b_min_10
   + 3.448275862068966 b_min_11 + 10 b_min_20 + 9.090909090909092 b_min_21
   + 10 b_min_30 + 4.545454545454546 b_min_31 + 12.5 b_min_40
   + 3.703703703703703 b_min_41 + 1.923076923076925 b_min_50
   + 1.351351351351351 b_min_51 + 1.5625 b_max_00
   + 0.075187969924812 b_max_01 + 4.761904761904763 b_max_10
   + 3.448275862068966 b_max_11 + 10 b_max_20 + 9.090909090909092 b_max_21
   + 10 b_max_30 + 4.545454545454546 b_max_31 + 12.5 b_max_40
   + 3.703703703703703 b_max_41 + 1.923076923076925 b_max_50
   + 1.351351351351351 b_max_51
Subject To
 input_weight_constr_0: y_00 + y_01 + y_02 + y_03 <= 31.7
 capacity_constr_0: y_00 <= 112.2
 weight_constr_00: x_00 + x_01 - y_00 <= 526.6
 capacity_constr_1: y_01 <= 24.3
 weight_constr_10: x_10 + x_11 - y_01 <= 609.1
 capacity_constr_2: y_02 <= 125.9
 weight_constr_20: x_20 + x_21 - y_02 <= 554.3
 capacity_constr_3: y_03 <= 57.7
 weight_constr_30: x_30 + x_31 - y_03 <= 645.1
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1102.2
 min_quality_constr_00: 44.42 x_00 + 20.11 x_10 - 10.5 x_20 + 37.94 x_30
   + 1102.2 a_min_00 >= -0
 max_quality_constr_00: - 0.58 x_00 - 24.89 x_10 - 55.5 x_20 - 7.06 x_30
   - 1102.2 a_max_00 <= -0
 goal_quality_constr_00: 0.06 x_00 - 24.25 x_10 - 54.86 x_20 - 6.42 x_30
   + 1102.2 b_min_00 - 1102.2 b_max_00 = -0
 min_quality_constr_10: 0.89 x_00 + 0.34 x_10 + 0.35 x_20 + 0.2 x_30
   + 1102.2 a_min_10 >= -0
 max_quality_constr_10: - 0.61 x_00 - 1.16 x_10 - 1.15 x_20 - 1.3 x_30
   - 1102.2 a_max_10 <= -0
 goal_quality_constr_10: - 0.4 x_00 - 0.95 x_10 - 0.94 x_20 - 1.09 x_30
   + 1102.2 b_min_10 - 1102.2 b_max_10 = -0
 min_quality_constr_20: 1.26 x_00 + 2.37 x_10 + 2.03 x_20 + 4.53 x_30
   + 1102.2 a_min_20 >= -0
 max_quality_constr_20: 0.76 x_00 + 1.87 x_10 + 1.53 x_20 + 4.03 x_30
   - 1102.2 a_max_20 <= -0
 goal_quality_constr_20: 1.16 x_00 + 2.27 x_10 + 1.93 x_20 + 4.43 x_30
   + 1102.2 b_min_20 - 1102.2 b_max_20 = -0
 min_quality_constr_30: 2.29 x_00 + 4.71 x_10 + 3.29 x_20 + 3.98 x_30
   + 1102.2 a_min_30 >= -0
 max_quality_constr_30: 1.79 x_00 + 4.21 x_10 + 2.79 x_20 + 3.48 x_30
   - 1102.2 a_max_30 <= -0
 goal_quality_constr_30: 2.19 x_00 + 4.61 x_10 + 3.19 x_20 + 3.88 x_30
   + 1102.2 b_min_30 - 1102.2 b_max_30 = -0
 min_quality_constr_40: 0.21 x_00 + 0.67 x_10 + 0.94 x_20 + 0.31 x_30
   + 1102.2 a_min_40 >= -0
 max_quality_constr_40: - 0.79 x_00 - 0.33 x_10 - 0.06 x_20 - 0.69 x_30
   - 1102.2 a_max_40 <= -0
 goal_quality_constr_40: 0.13 x_00 + 0.59 x_10 + 0.86 x_20 + 0.23 x_30
   + 1102.2 b_min_40 - 1102.2 b_max_40 = -0
 min_quality_constr_50: - 0.5 x_00 + 0.93 x_10 + 0.68 x_20 + 2.13 x_30
   + 1102.2 a_min_50 >= -0
 max_quality_constr_50: - 2 x_00 - 0.57 x_10 - 0.82 x_20 + 0.63 x_30
   - 1102.2 a_max_50 <= -0
 goal_quality_constr_50: - 1.02 x_00 + 0.41 x_10 + 0.16 x_20 + 1.61 x_30
   + 1102.2 b_min_50 - 1102.2 b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 1005.5
 min_quality_constr_01: 44.42 x_01 + 20.11 x_11 - 10.5 x_21 + 37.94 x_31
   + 1005.5 a_min_01 >= -0
 max_quality_constr_01: - 0.58 x_01 - 24.89 x_11 - 55.5 x_21 - 7.06 x_31
   - 1005.5 a_max_01 <= -0
 goal_quality_constr_01: 31.12 x_01 + 6.81 x_11 - 23.8 x_21 + 24.64 x_31
   + 1005.5 b_min_01 - 1005.5 b_max_01 = -0
 min_quality_constr_11: 0.89 x_01 + 0.34 x_11 + 0.35 x_21 + 0.2 x_31
   + 1005.5 a_min_11 >= -0
 max_quality_constr_11: - 0.61 x_01 - 1.16 x_11 - 1.15 x_21 - 1.3 x_31
   - 1005.5 a_max_11 <= -0
 goal_quality_constr_11: 0.6 x_01 + 0.05 x_11 + 0.06 x_21 - 0.09 x_31
   + 1005.5 b_min_11 - 1005.5 b_max_11 = -0
 min_quality_constr_21: 1.26 x_01 + 2.37 x_11 + 2.03 x_21 + 4.53 x_31
   + 1005.5 a_min_21 >= -0
 max_quality_constr_21: 0.76 x_01 + 1.87 x_11 + 1.53 x_21 + 4.03 x_31
   - 1005.5 a_max_21 <= -0
 goal_quality_constr_21: 0.87 x_01 + 1.98 x_11 + 1.64 x_21 + 4.14 x_31
   + 1005.5 b_min_21 - 1005.5 b_max_21 = -0
 min_quality_constr_31: 2.29 x_01 + 4.71 x_11 + 3.29 x_21 + 3.98 x_31
   + 1005.5 a_min_31 >= -0
 max_quality_constr_31: 1.79 x_01 + 4.21 x_11 + 2.79 x_21 + 3.48 x_31
   - 1005.5 a_max_31 <= -0
 goal_quality_constr_31: 2.07 x_01 + 4.49 x_11 + 3.07 x_21 + 3.76 x_31
   + 1005.5 b_min_31 - 1005.5 b_max_31 = -0
 min_quality_constr_41: 0.21 x_01 + 0.67 x_11 + 0.94 x_21 + 0.31 x_31
   + 1005.5 a_min_41 >= -0
 max_quality_constr_41: - 0.79 x_01 - 0.33 x_11 - 0.06 x_21 - 0.69 x_31
   - 1005.5 a_max_41 <= -0
 goal_quality_constr_41: - 0.52 x_01 - 0.06 x_11 + 0.21 x_21 - 0.42 x_31
   + 1005.5 b_min_41 - 1005.5 b_max_41 = -0
 min_quality_constr_51: - 0.5 x_01 + 0.93 x_11 + 0.68 x_21 + 2.13 x_31
   + 1005.5 a_min_51 >= -0
 max_quality_constr_51: - 2 x_01 - 0.57 x_11 - 0.82 x_21 + 0.63 x_31
   - 1005.5 a_max_51 <= -0
 goal_quality_constr_51: - 1.24 x_01 + 0.19 x_11 - 0.06 x_21 + 1.39 x_31
   + 1005.5 b_min_51 - 1005.5 b_max_51 = -0
Bounds
End
