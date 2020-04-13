\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  29.6823983377857 a_max_00 + 25.0501002004008 a_max_01
   + 6666.666666666671 a_max_10 + 25000 a_max_11
   + 7142.857142857142 a_max_20 + 50000 a_max_21
   + 14285.71428571428 a_max_30 + 2040.816326530612 a_max_31
   + 1162.790697674419 a_max_40 + 2173.913043478261 a_max_41
   + 20000 a_max_50 + 671.1409395973153 a_max_51
   + 88.41732979664012 a_min_00 + 196.8503937007875 a_min_01
   + 740.7407407407406 a_min_10 + 684.931506849315 a_min_11
   + 2777.777777777778 a_min_20 + 2083.333333333333 a_min_21
   + 2325.581395348837 a_min_30 + 100000 a_min_31
   + 7142.857142857142 a_min_40 + 1851.851851851852 a_min_41
   + 689.655172413793 a_min_50 + 100000.0000000021 a_min_51
   + 0.0884173297966401 b_min_00 + 0.1968503937007875 b_min_01
   + 6.666666666666671 b_min_10 + 25 b_min_11 + 7.142857142857142 b_min_20
   + 50 b_min_21 + 14.28571428571428 b_min_30 + 100 b_min_31
   + 7.142857142857142 b_min_40 + 2.173913043478261 b_min_41 + 20 b_min_50
   + 100 b_min_51 + 0.0884173297966401 b_max_0 + 0.1968503937007875 b_max_0
   + 6.666666666666671 b_max_1 + 25 b_max_1 + 7.142857142857142 b_max_2
   + 50 b_max_2 + 14.28571428571428 b_max_3 + 100 b_max_3
   + 7.142857142857142 b_max_4 + 2.173913043478261 b_max_4 + 20 b_max_5
   + 100 b_max_5
Subject To
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1162
 capacity_constr_00: x_00 <= 431
 capacity_constr_10: x_10 <= 338
 capacity_constr_20: x_20 <= 424
 capacity_constr_30: x_30 <= 310
 min_quality_constr_00: 35.13 x_00 - 8.49 x_10 + 44.02 x_20 + 15.37 x_30
   + 1162 a_min_00 >= -0
 max_quality_constr_00: - 9.87 x_00 - 53.49 x_10 - 0.98 x_20 - 29.63 x_30
   - 1162 a_max_00 <= -0
 goal_quality_constr_00: 23.82 x_00 - 19.8 x_10 + 32.71 x_20 + 4.06 x_30
   + b_min_00 - b_max_0 = -0
 min_quality_constr_10: 0.61 x_00 + 1.41 x_10 + 0.46 x_20 + 0.59 x_30
   + 1162 a_min_10 >= -0
 max_quality_constr_10: - 0.89 x_00 - 0.09 x_10 - 1.04 x_20 - 0.91 x_30
   - 1162 a_max_10 <= -0
 goal_quality_constr_10: - 0.74 x_00 + 0.06 x_10 - 0.89 x_20 - 0.76 x_30
   + b_min_10 - b_max_1 = -0
 min_quality_constr_20: 5.87 x_00 + 4.94 x_10 + 5.52 x_20 + 3.48 x_30
   + 1162 a_min_20 >= -0
 max_quality_constr_20: 5.37 x_00 + 4.44 x_10 + 5.02 x_20 + 2.98 x_30
   - 1162 a_max_20 <= -0
 goal_quality_constr_20: 5.51 x_00 + 4.58 x_10 + 5.16 x_20 + 3.12 x_30
   + b_min_20 - b_max_2 = -0
 min_quality_constr_30: 1.62 x_00 + 4.43 x_10 + 4.26 x_20 + 2.49 x_30
   + 1162 a_min_30 >= -0
 max_quality_constr_30: 1.12 x_00 + 3.93 x_10 + 3.76 x_20 + 1.99 x_30
   - 1162 a_max_30 <= -0
 goal_quality_constr_30: 1.19 x_00 + 4 x_10 + 3.83 x_20 + 2.06 x_30
   + b_min_30 - b_max_3 = -0
 min_quality_constr_40: 0.54 x_00 + 1.18 x_10 + 0.18 x_20 + 0.69 x_30
   + 1162 a_min_40 >= -0
 max_quality_constr_40: - 0.46 x_00 + 0.18 x_10 - 0.82 x_20 - 0.31 x_30
   - 1162 a_max_40 <= -0
 goal_quality_constr_40: 0.4 x_00 + 1.04 x_10 + 0.04 x_20 + 0.55 x_30
   + b_min_40 - b_max_4 = -0
 min_quality_constr_50: 1.88 x_00 - 0.59 x_10 + 1.51 x_20 + 2.43 x_30
   + 1162 a_min_50 >= -0
 max_quality_constr_50: 0.38 x_00 - 2.09 x_10 + 0.01 x_20 + 0.93 x_30
   - 1162 a_max_50 <= -0
 goal_quality_constr_50: 0.43 x_00 - 2.04 x_10 + 0.06 x_20 + 0.98 x_30
   + b_min_50 - b_max_5 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 927
 capacity_constr_01: x_01 <= 431
 capacity_constr_11: x_11 <= 338
 capacity_constr_21: x_21 <= 424
 capacity_constr_31: x_31 <= 310
 min_quality_constr_01: 35.13 x_01 - 8.49 x_11 + 44.02 x_21 + 15.37 x_31
   + 927 a_min_01 >= -0
 max_quality_constr_01: - 9.87 x_01 - 53.49 x_11 - 0.98 x_21 - 29.63 x_31
   - 927 a_max_01 <= -0
 goal_quality_constr_01: 30.05 x_01 - 13.57 x_11 + 38.94 x_21 + 10.29 x_31
   + b_min_01 - b_max_0 = -0
 min_quality_constr_11: 0.61 x_01 + 1.41 x_11 + 0.46 x_21 + 0.59 x_31
   + 927 a_min_11 >= -0
 max_quality_constr_11: - 0.89 x_01 - 0.09 x_11 - 1.04 x_21 - 0.91 x_31
   - 927 a_max_11 <= -0
 goal_quality_constr_11: - 0.85 x_01 - 0.05 x_11 - x_21 - 0.87 x_31
   + b_min_11 - b_max_1 = -0
 min_quality_constr_21: 5.87 x_01 + 4.94 x_11 + 5.52 x_21 + 3.48 x_31
   + 927 a_min_21 >= -0
 max_quality_constr_21: 5.37 x_01 + 4.44 x_11 + 5.02 x_21 + 2.98 x_31
   - 927 a_max_21 <= -0
 goal_quality_constr_21: 5.39 x_01 + 4.46 x_11 + 5.04 x_21 + 3 x_31
   + b_min_21 - b_max_2 = -0
 min_quality_constr_31: 1.62 x_01 + 4.43 x_11 + 4.26 x_21 + 2.49 x_31
   + 927 a_min_31 >= -0
 max_quality_constr_31: 1.12 x_01 + 3.93 x_11 + 3.76 x_21 + 1.99 x_31
   - 927 a_max_31 <= -0
 goal_quality_constr_31: 1.61 x_01 + 4.42 x_11 + 4.25 x_21 + 2.48 x_31
   + b_min_31 - b_max_3 = -0
 min_quality_constr_41: 0.54 x_01 + 1.18 x_11 + 0.18 x_21 + 0.69 x_31
   + 927 a_min_41 >= -0
 max_quality_constr_41: - 0.46 x_01 + 0.18 x_11 - 0.82 x_21 - 0.31 x_31
   - 927 a_max_41 <= -0
 goal_quality_constr_41: 0.64 x_11 - 0.36 x_21 + 0.15 x_31 + b_min_41
   - b_max_4 = -0
 min_quality_constr_51: 1.88 x_01 - 0.59 x_11 + 1.51 x_21 + 2.43 x_31
   + 927 a_min_51 >= -0
 max_quality_constr_51: 0.38 x_01 - 2.09 x_11 + 0.01 x_21 + 0.93 x_31
   - 927 a_max_51 <= -0
 goal_quality_constr_51: 1.87 x_01 - 0.6 x_11 + 1.5 x_21 + 2.42 x_31
   + b_min_51 - b_max_5 = -0
Bounds
End
