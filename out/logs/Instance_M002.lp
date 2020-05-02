\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  54.17118093174433 a_max_00 + 24.98750624687656 a_max_01 + 4000 a_max_10
   + 877.1929824561403 a_max_11 + 2083.333333333333 a_max_20
   + 100000 a_max_21 + 2083.333333333333 a_max_30
   + 2272.727272727273 a_max_31 + 4166.666666666667 a_max_40
   + 3846.153846153846 a_max_41 + 862.0689655172413 a_max_50
   + 3030.30303030303 a_max_51 + 37.6789751318764 a_min_00
   + 200.8032128514058 a_min_01 + 800 a_min_10 + 2777.777777777778 a_min_11
   + 50000 a_min_20 + 2040.816326530612 a_min_21 + 50000 a_min_30
   + 16666.66666666667 a_min_31 + 1315.789473684211 a_min_40
   + 1351.351351351351 a_min_41 + 2941.176470588236 a_min_50
   + 854.7008547008547 a_min_51 + 0.0541711809317443 b_min_00
   + 0.2008032128514058 b_min_01 + 4 b_min_10 + 2.777777777777778 b_min_11
   + 50 b_min_20 + 100 b_min_21 + 50 b_min_30 + 16.66666666666667 b_min_31
   + 4.166666666666667 b_min_40 + 3.846153846153846 b_min_41
   + 2.941176470588236 b_min_50 + 3.03030303030303 b_min_51
   + 0.0541711809317443 b_max_00 + 0.2008032128514058 b_max_01 + 4 b_max_10
   + 2.777777777777778 b_max_11 + 50 b_max_20 + 100 b_max_21 + 50 b_max_30
   + 16.66666666666667 b_max_31 + 4.166666666666667 b_max_40
   + 3.846153846153846 b_max_41 + 2.941176470588236 b_max_50
   + 3.03030303030303 b_max_51
Subject To
 capacity_constr_0: x_00 + x_01 <= 609
 capacity_constr_1: x_10 + x_11 <= 339.3
 capacity_constr_2: x_20 + x_21 <= 998.3
 capacity_constr_3: x_30 + x_31 <= 647.9
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 628.4
 min_quality_constr_00: 28.18 x_00 + 25.71 x_10 + 19.91 x_20 + 7.96 x_30
   + 628.4 a_min_00 >= -0
 max_quality_constr_00: - 16.82 x_00 - 19.29 x_10 - 25.09 x_20 - 37.04 x_30
   - 628.4 a_max_00 <= -0
 goal_quality_constr_00: 1.64 x_00 - 0.83 x_10 - 6.63 x_20 - 18.58 x_30
   + b_min_00 - b_max_00 = -0
 min_quality_constr_10: 0.43 x_00 + 0.38 x_10 + 0.1 x_20 + 0.91 x_30
   + 628.4 a_min_10 >= -0
 max_quality_constr_10: - 1.07 x_00 - 1.12 x_10 - 1.4 x_20 - 0.59 x_30
   - 628.4 a_max_10 <= -0
 goal_quality_constr_10: - 0.82 x_00 - 0.87 x_10 - 1.15 x_20 - 0.34 x_30
   + b_min_10 - b_max_10 = -0
 min_quality_constr_20: 4.7 x_00 + 2.96 x_10 + 0.01 x_20 + 3.75 x_30
   + 628.4 a_min_20 >= -0
 max_quality_constr_20: 4.2 x_00 + 2.46 x_10 - 0.49 x_20 + 3.25 x_30
   - 628.4 a_max_20 <= -0
 goal_quality_constr_20: 4.68 x_00 + 2.94 x_10 - 0.01 x_20 + 3.73 x_30
   + b_min_20 - b_max_20 = -0
 min_quality_constr_30: 1.06 x_00 + 3.4 x_10 + 6.18 x_20 + 5.47 x_30
   + 628.4 a_min_30 >= -0
 max_quality_constr_30: 0.56 x_00 + 2.9 x_10 + 5.68 x_20 + 4.97 x_30
   - 628.4 a_max_30 <= -0
 goal_quality_constr_30: 1.04 x_00 + 3.38 x_10 + 6.16 x_20 + 5.45 x_30
   + b_min_30 - b_max_30 = -0
 min_quality_constr_40: 0.17 x_00 + 0.94 x_10 + 0.12 x_20 + 0.08 x_30
   + 628.4 a_min_40 >= -0
 max_quality_constr_40: - 0.83 x_00 - 0.06 x_10 - 0.88 x_20 - 0.92 x_30
   - 628.4 a_max_40 <= -0
 goal_quality_constr_40: - 0.59 x_00 + 0.18 x_10 - 0.64 x_20 - 0.68 x_30
   + b_min_40 - b_max_40 = -0
 min_quality_constr_50: 3 x_00 + 3.05 x_10 + 2.9 x_20 + 0.15 x_30
   + 628.4 a_min_50 >= -0
 max_quality_constr_50: 1.5 x_00 + 1.55 x_10 + 1.4 x_20 - 1.35 x_30
   - 628.4 a_max_50 <= -0
 goal_quality_constr_50: 2.66 x_00 + 2.71 x_10 + 2.56 x_20 - 0.19 x_30
   + b_min_50 - b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 1165.8
 min_quality_constr_01: 28.18 x_01 + 25.71 x_11 + 19.91 x_21 + 7.96 x_31
   + 1165.8 a_min_01 >= -0
 max_quality_constr_01: - 16.82 x_01 - 19.29 x_11 - 25.09 x_21 - 37.04 x_31
   - 1165.8 a_max_01 <= -0
 goal_quality_constr_01: 23.2 x_01 + 20.73 x_11 + 14.93 x_21 + 2.98 x_31
   + b_min_01 - b_max_01 = -0
 min_quality_constr_11: 0.43 x_01 + 0.38 x_11 + 0.1 x_21 + 0.91 x_31
   + 1165.8 a_min_11 >= -0
 max_quality_constr_11: - 1.07 x_01 - 1.12 x_11 - 1.4 x_21 - 0.59 x_31
   - 1165.8 a_max_11 <= -0
 goal_quality_constr_11: 0.07 x_01 + 0.02 x_11 - 0.26 x_21 + 0.55 x_31
   + b_min_11 - b_max_11 = -0
 min_quality_constr_21: 4.7 x_01 + 2.96 x_11 + 0.01 x_21 + 3.75 x_31
   + 1165.8 a_min_21 >= -0
 max_quality_constr_21: 4.2 x_01 + 2.46 x_11 - 0.49 x_21 + 3.25 x_31
   - 1165.8 a_max_21 <= -0
 goal_quality_constr_21: 4.21 x_01 + 2.47 x_11 - 0.48 x_21 + 3.26 x_31
   + b_min_21 - b_max_21 = -0
 min_quality_constr_31: 1.06 x_01 + 3.4 x_11 + 6.18 x_21 + 5.47 x_31
   + 1165.8 a_min_31 >= -0
 max_quality_constr_31: 0.56 x_01 + 2.9 x_11 + 5.68 x_21 + 4.97 x_31
   - 1165.8 a_max_31 <= -0
 goal_quality_constr_31: x_01 + 3.34 x_11 + 6.12 x_21 + 5.41 x_31
   + b_min_31 - b_max_31 = -0
 min_quality_constr_41: 0.17 x_01 + 0.94 x_11 + 0.12 x_21 + 0.08 x_31
   + 1165.8 a_min_41 >= -0
 max_quality_constr_41: - 0.83 x_01 - 0.06 x_11 - 0.88 x_21 - 0.92 x_31
   - 1165.8 a_max_41 <= -0
 goal_quality_constr_41: - 0.57 x_01 + 0.2 x_11 - 0.62 x_21 - 0.66 x_31
   + b_min_41 - b_max_41 = -0
 min_quality_constr_51: 3 x_01 + 3.05 x_11 + 2.9 x_21 + 0.15 x_31
   + 1165.8 a_min_51 >= -0
 max_quality_constr_51: 1.5 x_01 + 1.55 x_11 + 1.4 x_21 - 1.35 x_31
   - 1165.8 a_max_51 <= -0
 goal_quality_constr_51: 1.83 x_01 + 1.88 x_11 + 1.73 x_21 - 1.02 x_31
   + b_min_51 - b_max_51 = -0
Bounds
End
