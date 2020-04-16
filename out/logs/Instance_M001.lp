\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  5882.352941176411 a_max_00 + 63.69426751592356 a_max_01
   + 1086.95652173913 a_max_10 + 5555.555555555557 a_max_11
   + 9090.909090909092 a_max_20 + 7142.857142857142 a_max_21
   + 50000 a_max_30 + 16666.66666666667 a_max_31
   + 1333.333333333333 a_max_40 + 1315.789473684211 a_max_41
   + 1851.851851851852 a_max_50 + 980.3921568627451 a_max_51
   + 22.30649118893598 a_min_00 + 34.1296928327645 a_min_01
   + 1724.137931034483 a_min_10 + 757.5757575757576 a_min_11
   + 2564.102564102564 a_min_20 + 2777.777777777778 a_min_21
   + 2083.333333333333 a_min_30 + 2272.727272727273 a_min_31
   + 4000 a_min_40 + 4166.666666666667 a_min_41
   + 1041.666666666667 a_min_50 + 2083.333333333333 a_min_51
   + 5.882352941176411 b_min_00 + 0.0636942675159236 b_min_01
   + 1.724137931034483 b_min_10 + 5.555555555555557 b_min_11
   + 9.090909090909092 b_min_20 + 7.142857142857142 b_min_21 + 50 b_min_30
   + 16.66666666666667 b_min_31 + 4 b_min_40 + 4.166666666666667 b_min_41
   + 1.851851851851852 b_min_50 + 2.083333333333333 b_min_51
   + 5.882352941176411 b_max_00 + 0.0636942675159236 b_max_01
   + 1.724137931034483 b_max_10 + 5.555555555555557 b_max_11
   + 9.090909090909092 b_max_20 + 7.142857142857142 b_max_21 + 50 b_max_30
   + 16.66666666666667 b_max_31 + 4 b_max_40 + 4.166666666666667 b_max_41
   + 1.851851851851852 b_max_50 + 2.083333333333333 b_max_51
Subject To
 capacity_constr_0: x_00 + x_01 <= 612.9
 capacity_constr_1: x_10 + x_11 <= 635.7
 capacity_constr_2: x_20 + x_21 <= 578.1
 capacity_constr_3: x_30 + x_31 <= 477.5
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 987.3
 min_quality_constr_00: 43.66 x_00 + 10.65 x_10 + 23.76 x_20 + 6.55 x_30
   + 987.3 a_min_00 >= -0
 max_quality_constr_00: - 1.34 x_00 - 34.35 x_10 - 21.24 x_20 - 38.45 x_30
   - 987.3 a_max_00 <= -0
 goal_quality_constr_00: - 1.17 x_00 - 34.18 x_10 - 21.07 x_20 - 38.28 x_30
   + b_min_00 - b_max_00 = -0
 min_quality_constr_10: 0.74 x_00 + 1.34 x_10 + 0.72 x_20 + 0.1 x_30
   + 987.3 a_min_10 >= -0
 max_quality_constr_10: - 0.76 x_00 - 0.16 x_10 - 0.78 x_20 - 1.4 x_30
   - 987.3 a_max_10 <= -0
 goal_quality_constr_10: 0.16 x_00 + 0.76 x_10 + 0.14 x_20 - 0.48 x_30
   + b_min_10 - b_max_10 = -0
 min_quality_constr_20: 0.3 x_00 + 5.7 x_10 + 4.52 x_20 + 3.43 x_30
   + 987.3 a_min_20 >= -0
 max_quality_constr_20: - 0.2 x_00 + 5.2 x_10 + 4.02 x_20 + 2.93 x_30
   - 987.3 a_max_20 <= -0
 goal_quality_constr_20: - 0.09 x_00 + 5.31 x_10 + 4.13 x_20 + 3.04 x_30
   + b_min_20 - b_max_20 = -0
 min_quality_constr_30: 3.33 x_00 + 0.95 x_10 + 4.02 x_20 + 4.22 x_30
   + 987.3 a_min_30 >= -0
 max_quality_constr_30: 2.83 x_00 + 0.45 x_10 + 3.52 x_20 + 3.72 x_30
   - 987.3 a_max_30 <= -0
 goal_quality_constr_30: 2.85 x_00 + 0.47 x_10 + 3.54 x_20 + 3.74 x_30
   + b_min_30 - b_max_30 = -0
 min_quality_constr_40: 0.42 x_00 + 0.73 x_10 + 0.71 x_20 + 0.87 x_30
   + 987.3 a_min_40 >= -0
 max_quality_constr_40: - 0.58 x_00 - 0.27 x_10 - 0.29 x_20 - 0.13 x_30
   - 987.3 a_max_40 <= -0
 goal_quality_constr_40: 0.17 x_00 + 0.48 x_10 + 0.46 x_20 + 0.62 x_30
   + b_min_40 - b_max_40 = -0
 min_quality_constr_50: - 0.05 x_00 + 1.07 x_10 + 0.78 x_20 + 2.15 x_30
   + 987.3 a_min_50 >= -0
 max_quality_constr_50: - 1.55 x_00 - 0.43 x_10 - 0.72 x_20 + 0.65 x_30
   - 987.3 a_max_50 <= -0
 goal_quality_constr_50: - 1.01 x_00 + 0.11 x_10 - 0.18 x_20 + 1.19 x_30
   + b_min_50 - b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 942.8
 min_quality_constr_01: 43.66 x_01 + 10.65 x_11 + 23.76 x_21 + 6.55 x_31
   + 942.8 a_min_01 >= -0
 max_quality_constr_01: - 1.34 x_01 - 34.35 x_11 - 21.24 x_21 - 38.45 x_31
   - 942.8 a_max_01 <= -0
 goal_quality_constr_01: 14.36 x_01 - 18.65 x_11 - 5.54 x_21 - 22.75 x_31
   + b_min_01 - b_max_01 = -0
 min_quality_constr_11: 0.74 x_01 + 1.34 x_11 + 0.72 x_21 + 0.1 x_31
   + 942.8 a_min_11 >= -0
 max_quality_constr_11: - 0.76 x_01 - 0.16 x_11 - 0.78 x_21 - 1.4 x_31
   - 942.8 a_max_11 <= -0
 goal_quality_constr_11: - 0.58 x_01 + 0.02 x_11 - 0.6 x_21 - 1.22 x_31
   + b_min_11 - b_max_11 = -0
 min_quality_constr_21: 0.3 x_01 + 5.7 x_11 + 4.52 x_21 + 3.43 x_31
   + 942.8 a_min_21 >= -0
 max_quality_constr_21: - 0.2 x_01 + 5.2 x_11 + 4.02 x_21 + 2.93 x_31
   - 942.8 a_max_21 <= -0
 goal_quality_constr_21: - 0.06 x_01 + 5.34 x_11 + 4.16 x_21 + 3.07 x_31
   + b_min_21 - b_max_21 = -0
 min_quality_constr_31: 3.33 x_01 + 0.95 x_11 + 4.02 x_21 + 4.22 x_31
   + 942.8 a_min_31 >= -0
 max_quality_constr_31: 2.83 x_01 + 0.45 x_11 + 3.52 x_21 + 3.72 x_31
   - 942.8 a_max_31 <= -0
 goal_quality_constr_31: 2.89 x_01 + 0.51 x_11 + 3.58 x_21 + 3.78 x_31
   + b_min_31 - b_max_31 = -0
 min_quality_constr_41: 0.42 x_01 + 0.73 x_11 + 0.71 x_21 + 0.87 x_31
   + 942.8 a_min_41 >= -0
 max_quality_constr_41: - 0.58 x_01 - 0.27 x_11 - 0.29 x_21 - 0.13 x_31
   - 942.8 a_max_41 <= -0
 goal_quality_constr_41: 0.18 x_01 + 0.49 x_11 + 0.47 x_21 + 0.63 x_31
   + b_min_41 - b_max_41 = -0
 min_quality_constr_51: - 0.05 x_01 + 1.07 x_11 + 0.78 x_21 + 2.15 x_31
   + 942.8 a_min_51 >= -0
 max_quality_constr_51: - 1.55 x_01 - 0.43 x_11 - 0.72 x_21 + 0.65 x_31
   - 942.8 a_max_51 <= -0
 goal_quality_constr_51: - 0.53 x_01 + 0.59 x_11 + 0.3 x_21 + 1.67 x_31
   + b_min_51 - b_max_51 = -0
Bounds
End
