\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  57.47126436781607 a_max_00 + 64.14368184733803 a_max_01
   + 724.6376811594204 a_max_10 + 7692.307692307699 a_max_11
   + 4166.666666666667 a_max_20 + 2127.659574468085 a_max_21
   + 2222.222222222222 a_max_30 + 4545.454545454546 a_max_31
   + 3448.275862068965 a_max_40 + 50000 a_max_41
   + 3703.703703703709 a_max_50 + 1315.789473684211 a_max_51
   + 36.23188405797102 a_min_00 + 34.00204012240734 a_min_01
   + 8333.333333333334 a_min_10 + 729.92700729927 a_min_11
   + 3846.153846153846 a_min_20 + 33333.33333333334 a_min_21
   + 20000 a_min_30 + 3571.428571428571 a_min_31
   + 1408.450704225352 a_min_40 + 1020.408163265306 a_min_41
   + 813.0081300813006 a_min_50 + 1351.351351351351 a_min_51
   + 0.0574712643678161 b_min_00 + 0.064143681847338 b_min_01
   + 8.333333333333334 b_min_10 + 7.692307692307699 b_min_11
   + 4.166666666666667 b_min_20 + 33.33333333333334 b_min_21 + 20 b_min_30
   + 4.545454545454546 b_min_31 + 3.448275862068965 b_min_40 + 50 b_min_41
   + 3.703703703703709 b_min_50 + 1.351351351351351 b_min_51
   + 0.0574712643678161 b_max_00 + 0.064143681847338 b_max_01
   + 8.333333333333334 b_max_10 + 7.692307692307699 b_max_11
   + 4.166666666666667 b_max_20 + 33.33333333333334 b_max_21 + 20 b_max_30
   + 4.545454545454546 b_max_31 + 3.448275862068965 b_max_40 + 50 b_max_41
   + 3.703703703703709 b_max_50 + 1.351351351351351 b_max_51
Subject To
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1176.8
 capacity_constr_00: x_00 <= 381.7
 capacity_constr_10: x_10 <= 314.5
 capacity_constr_20: x_20 <= 468.9
 capacity_constr_30: x_30 <= 436.4
 min_quality_constr_00: 30.75 x_00 + 36.95 x_10 + 19.74 x_20 + 41.49 x_30
   + 1176.8 a_min_00 >= -0
 max_quality_constr_00: - 14.25 x_00 - 8.05 x_10 - 25.26 x_20 - 3.51 x_30
   - 1176.8 a_max_00 <= -0
 goal_quality_constr_00: 3.15 x_00 + 9.35 x_10 - 7.86 x_20 + 13.89 x_30
   + b_min_00 - b_max_00 = -0
 min_quality_constr_10: 1.34 x_00 + 0.64 x_10 + 0.13 x_20 + 1.71 x_30
   + 1176.8 a_min_10 >= -0
 max_quality_constr_10: - 0.16 x_00 - 0.86 x_10 - 1.37 x_20 + 0.21 x_30
   - 1176.8 a_max_10 <= -0
 goal_quality_constr_10: 1.22 x_00 + 0.52 x_10 + 0.01 x_20 + 1.59 x_30
   + b_min_10 - b_max_10 = -0
 min_quality_constr_20: 0.69 x_00 + 4.94 x_10 + 4.7 x_20 + 4.47 x_30
   + 1176.8 a_min_20 >= -0
 max_quality_constr_20: 0.19 x_00 + 4.44 x_10 + 4.2 x_20 + 3.97 x_30
   - 1176.8 a_max_20 <= -0
 goal_quality_constr_20: 0.43 x_00 + 4.68 x_10 + 4.44 x_20 + 4.21 x_30
   + b_min_20 - b_max_20 = -0
 min_quality_constr_30: 2.86 x_00 + 2.09 x_10 + 5.13 x_20 + 1.06 x_30
   + 1176.8 a_min_30 >= -0
 max_quality_constr_30: 2.36 x_00 + 1.59 x_10 + 4.63 x_20 + 0.56 x_30
   - 1176.8 a_max_30 <= -0
 goal_quality_constr_30: 2.81 x_00 + 2.04 x_10 + 5.08 x_20 + 1.01 x_30
   + b_min_30 - b_max_30 = -0
 min_quality_constr_40: 1.16 x_00 + 0.22 x_10 + 0.64 x_20 + 0.69 x_30
   + 1176.8 a_min_40 >= -0
 max_quality_constr_40: 0.16 x_00 - 0.78 x_10 - 0.36 x_20 - 0.31 x_30
   - 1176.8 a_max_40 <= -0
 goal_quality_constr_40: 0.45 x_00 - 0.49 x_10 - 0.07 x_20 - 0.02 x_30
   + b_min_40 - b_max_40 = -0
 min_quality_constr_50: - 0.63 x_00 - 0.45 x_10 + 0.1 x_20 + 0.05 x_30
   + 1176.8 a_min_50 >= -0
 max_quality_constr_50: - 2.13 x_00 - 1.95 x_10 - 1.4 x_20 - 1.45 x_30
   - 1176.8 a_max_50 <= -0
 goal_quality_constr_50: - 1.86 x_00 - 1.68 x_10 - 1.13 x_20 - 1.18 x_30
   + b_min_50 - b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 880.1
 capacity_constr_01: x_01 <= 381.7
 capacity_constr_11: x_11 <= 314.5
 capacity_constr_21: x_21 <= 468.9
 capacity_constr_31: x_31 <= 436.4
 min_quality_constr_01: 30.75 x_01 + 36.95 x_11 + 19.74 x_21 + 41.49 x_31
   + 880.1 a_min_01 >= -0
 max_quality_constr_01: - 14.25 x_01 - 8.05 x_11 - 25.26 x_21 - 3.51 x_31
   - 880.1 a_max_01 <= -0
 goal_quality_constr_01: 1.34 x_01 + 7.54 x_11 - 9.67 x_21 + 12.08 x_31
   + b_min_01 - b_max_01 = -0
 min_quality_constr_11: 1.34 x_01 + 0.64 x_11 + 0.13 x_21 + 1.71 x_31
   + 880.1 a_min_11 >= -0
 max_quality_constr_11: - 0.16 x_01 - 0.86 x_11 - 1.37 x_21 + 0.21 x_31
   - 880.1 a_max_11 <= -0
 goal_quality_constr_11: - 0.03 x_01 - 0.73 x_11 - 1.24 x_21 + 0.34 x_31
   + b_min_11 - b_max_11 = -0
 min_quality_constr_21: 0.69 x_01 + 4.94 x_11 + 4.7 x_21 + 4.47 x_31
   + 880.1 a_min_21 >= -0
 max_quality_constr_21: 0.19 x_01 + 4.44 x_11 + 4.2 x_21 + 3.97 x_31
   - 880.1 a_max_21 <= -0
 goal_quality_constr_21: 0.66 x_01 + 4.91 x_11 + 4.67 x_21 + 4.44 x_31
   + b_min_21 - b_max_21 = -0
 min_quality_constr_31: 2.86 x_01 + 2.09 x_11 + 5.13 x_21 + 1.06 x_31
   + 880.1 a_min_31 >= -0
 max_quality_constr_31: 2.36 x_01 + 1.59 x_11 + 4.63 x_21 + 0.56 x_31
   - 880.1 a_max_31 <= -0
 goal_quality_constr_31: 2.58 x_01 + 1.81 x_11 + 4.85 x_21 + 0.78 x_31
   + b_min_31 - b_max_31 = -0
 min_quality_constr_41: 1.16 x_01 + 0.22 x_11 + 0.64 x_21 + 0.69 x_31
   + 880.1 a_min_41 >= -0
 max_quality_constr_41: 0.16 x_01 - 0.78 x_11 - 0.36 x_21 - 0.31 x_31
   - 880.1 a_max_41 <= -0
 goal_quality_constr_41: 0.18 x_01 - 0.76 x_11 - 0.34 x_21 - 0.29 x_31
   + b_min_41 - b_max_41 = -0
 min_quality_constr_51: - 0.63 x_01 - 0.45 x_11 + 0.1 x_21 + 0.05 x_31
   + 880.1 a_min_51 >= -0
 max_quality_constr_51: - 2.13 x_01 - 1.95 x_11 - 1.4 x_21 - 1.45 x_31
   - 880.1 a_max_51 <= -0
 goal_quality_constr_51: - 1.37 x_01 - 1.19 x_11 - 0.64 x_21 - 0.69 x_31
   + b_min_51 - b_max_51 = -0
Bounds
End
