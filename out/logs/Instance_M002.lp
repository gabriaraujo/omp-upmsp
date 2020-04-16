\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  26.5041081367612 a_max_00 + 43.14063848144951 a_max_01
   + 943.3962264150942 a_max_10 + 746.2686567164178 a_max_11
   + 2325.581395348837 a_max_20 + 5263.157894736843 a_max_21
   + 12500 a_max_30 + 2439.024390243902 a_max_31
   + 1851.851851851852 a_max_40 + 100000 a_max_41 + 4000 a_max_50
   + 8333.333333333327 a_max_51 + 137.5515818431911 a_min_00
   + 45.82951420714942 a_min_01 + 2272.727272727273 a_min_10
   + 6250 a_min_11 + 14285.71428571428 a_min_20
   + 3225.806451612903 a_min_21 + 2380.952380952381 a_min_30
   + 11111.11111111111 a_min_31 + 2173.913043478261 a_min_40
   + 1010.10101010101 a_min_41 + 800 a_min_50 + 724.6376811594204 a_min_51
   + 0.1375515818431911 b_min_00 + 0.0458295142071494 b_min_01
   + 2.272727272727273 b_min_10 + 6.25 b_min_11
   + 14.28571428571428 b_min_20 + 5.263157894736842 b_min_21
   + 12.5 b_min_30 + 11.11111111111111 b_min_31
   + 2.173913043478261 b_min_40 + 100 b_min_41 + 4 b_min_50
   + 8.333333333333327 b_min_51 + 0.1375515818431911 b_max_00
   + 0.0458295142071494 b_max_01 + 2.272727272727273 b_max_10
   + 6.25 b_max_11 + 14.28571428571428 b_max_20
   + 5.263157894736842 b_max_21 + 12.5 b_max_30
   + 11.11111111111111 b_max_31 + 2.173913043478261 b_max_40 + 100 b_max_41
   + 4 b_max_50 + 8.333333333333327 b_max_51
Subject To
 capacity_constr_0: x_00 + x_01 <= 554.6
 capacity_constr_1: x_10 + x_11 <= 615.1
 capacity_constr_2: x_20 + x_21 <= 616.8
 capacity_constr_3: x_30 + x_31 <= 499
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 995.7
 min_quality_constr_00: - 12.65 x_00 + 36.81 x_10 - 6.26 x_20 - 16.12 x_30
   + 995.7 a_min_00 >= -0
 max_quality_constr_00: - 57.65 x_00 - 8.19 x_10 - 51.26 x_20 - 61.12 x_30
   - 995.7 a_max_00 <= -0
 goal_quality_constr_00: - 19.92 x_00 + 29.54 x_10 - 13.53 x_20
   - 23.39 x_30 + b_min_00 - b_max_00 = -0
 min_quality_constr_10: 1.09 x_00 + 0.35 x_10 + 0.99 x_20 + 1.26 x_30
   + 995.7 a_min_10 >= -0
 max_quality_constr_10: - 0.41 x_00 - 1.15 x_10 - 0.51 x_20 - 0.24 x_30
   - 995.7 a_max_10 <= -0
 goal_quality_constr_10: 0.65 x_00 - 0.09 x_10 + 0.55 x_20 + 0.82 x_30
   + b_min_10 - b_max_10 = -0
 min_quality_constr_20: 2.49 x_00 + 5.85 x_10 + 5.95 x_20 + 3.21 x_30
   + 995.7 a_min_20 >= -0
 max_quality_constr_20: 1.99 x_00 + 5.35 x_10 + 5.45 x_20 + 2.71 x_30
   - 995.7 a_max_20 <= -0
 goal_quality_constr_20: 2.42 x_00 + 5.78 x_10 + 5.88 x_20 + 3.14 x_30
   + b_min_20 - b_max_20 = -0
 min_quality_constr_30: 5.97 x_00 + 0.63 x_10 + 3.72 x_20 + 4.05 x_30
   + 995.7 a_min_30 >= -0
 max_quality_constr_30: 5.47 x_00 + 0.13 x_10 + 3.22 x_20 + 3.55 x_30
   - 995.7 a_max_30 <= -0
 goal_quality_constr_30: 5.55 x_00 + 0.21 x_10 + 3.3 x_20 + 3.63 x_30
   + b_min_30 - b_max_30 = -0
 min_quality_constr_40: 0.44 x_00 + 0.27 x_10 + 0.46 x_20 + 1.11 x_30
   + 995.7 a_min_40 >= -0
 max_quality_constr_40: - 0.56 x_00 - 0.73 x_10 - 0.54 x_20 + 0.11 x_30
   - 995.7 a_max_40 <= -0
 goal_quality_constr_40: - 0.02 x_00 - 0.19 x_10 + 0.65 x_30 + b_min_40
   - b_max_40 = -0
 min_quality_constr_50: 0.55 x_00 + 0.66 x_10 + 1.12 x_20 + 2.08 x_30
   + 995.7 a_min_50 >= -0
 max_quality_constr_50: - 0.95 x_00 - 0.84 x_10 - 0.38 x_20 + 0.58 x_30
   - 995.7 a_max_50 <= -0
 goal_quality_constr_50: - 0.7 x_00 - 0.59 x_10 - 0.13 x_20 + 0.83 x_30
   + b_min_50 - b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 871.8
 min_quality_constr_01: - 12.65 x_01 + 36.81 x_11 - 6.26 x_21 - 16.12 x_31
   + 871.8 a_min_01 >= -0
 max_quality_constr_01: - 57.65 x_01 - 8.19 x_11 - 51.26 x_21 - 61.12 x_31
   - 871.8 a_max_01 <= -0
 goal_quality_constr_01: - 34.47 x_01 + 14.99 x_11 - 28.08 x_21
   - 37.94 x_31 + b_min_01 - b_max_01 = -0
 min_quality_constr_11: 1.09 x_01 + 0.35 x_11 + 0.99 x_21 + 1.26 x_31
   + 871.8 a_min_11 >= -0
 max_quality_constr_11: - 0.41 x_01 - 1.15 x_11 - 0.51 x_21 - 0.24 x_31
   - 871.8 a_max_11 <= -0
 goal_quality_constr_11: 0.93 x_01 + 0.19 x_11 + 0.83 x_21 + 1.1 x_31
   + b_min_11 - b_max_11 = -0
 min_quality_constr_21: 2.49 x_01 + 5.85 x_11 + 5.95 x_21 + 3.21 x_31
   + 871.8 a_min_21 >= -0
 max_quality_constr_21: 1.99 x_01 + 5.35 x_11 + 5.45 x_21 + 2.71 x_31
   - 871.8 a_max_21 <= -0
 goal_quality_constr_21: 2.18 x_01 + 5.54 x_11 + 5.64 x_21 + 2.9 x_31
   + b_min_21 - b_max_21 = -0
 min_quality_constr_31: 5.97 x_01 + 0.63 x_11 + 3.72 x_21 + 4.05 x_31
   + 871.8 a_min_31 >= -0
 max_quality_constr_31: 5.47 x_01 + 0.13 x_11 + 3.22 x_21 + 3.55 x_31
   - 871.8 a_max_31 <= -0
 goal_quality_constr_31: 5.88 x_01 + 0.54 x_11 + 3.63 x_21 + 3.96 x_31
   + b_min_31 - b_max_31 = -0
 min_quality_constr_41: 0.44 x_01 + 0.27 x_11 + 0.46 x_21 + 1.11 x_31
   + 871.8 a_min_41 >= -0
 max_quality_constr_41: - 0.56 x_01 - 0.73 x_11 - 0.54 x_21 + 0.11 x_31
   - 871.8 a_max_41 <= -0
 goal_quality_constr_41: - 0.55 x_01 - 0.72 x_11 - 0.53 x_21 + 0.12 x_31
   + b_min_41 - b_max_41 = -0
 min_quality_constr_51: 0.55 x_01 + 0.66 x_11 + 1.12 x_21 + 2.08 x_31
   + 871.8 a_min_51 >= -0
 max_quality_constr_51: - 0.95 x_01 - 0.84 x_11 - 0.38 x_21 + 0.58 x_31
   - 871.8 a_max_51 <= -0
 goal_quality_constr_51: - 0.83 x_01 - 0.72 x_11 - 0.26 x_21 + 0.7 x_31
   + b_min_51 - b_max_51 = -0
Bounds
End
