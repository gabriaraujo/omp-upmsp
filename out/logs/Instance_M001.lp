\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  52.41090146750525 a_max_00 + 27.26281352235551 a_max_01
   + 1204.819277108434 a_max_10 + 680.2721088435374 a_max_11
   + 2222.222222222222 a_max_20 + 8333.333333333334 a_max_21
   + 3030.303030303031 a_max_30 + 3703.703703703703 a_max_31
   + 2272.727272727273 a_max_40 + 1562.5 a_max_41
   + 2439.024390243902 a_max_50 + 2380.952380952381 a_max_51
   + 38.58024691358025 a_min_00 + 120.1923076923077 a_min_01
   + 1492.537313432836 a_min_10 + 33333.33333333334 a_min_11
   + 20000 a_min_20 + 2631.578947368421 a_min_21
   + 5882.35294117647 a_min_30 + 4347.826086956521 a_min_31
   + 1785.714285714286 a_min_40 + 2777.777777777778 a_min_41
   + 917.4311926605507 a_min_50 + 925.9259259259259 a_min_51
   + 0.0524109014675052 b_min_00 + 0.1201923076923077 b_min_01
   + 1.492537313432836 b_min_10 + 33.33333333333334 b_min_11 + 20 b_min_20
   + 8.333333333333334 b_min_21 + 5.88235294117647 b_min_30
   + 4.347826086956522 b_min_31 + 2.272727272727273 b_min_40
   + 2.777777777777778 b_min_41 + 2.439024390243901 b_min_50
   + 2.380952380952381 b_min_51 + 0.0524109014675052 b_max_00
   + 0.1201923076923077 b_max_01 + 1.492537313432836 b_max_10
   + 33.33333333333334 b_max_11 + 20 b_max_20 + 8.333333333333334 b_max_21
   + 5.88235294117647 b_max_30 + 4.347826086956522 b_max_31
   + 2.272727272727273 b_max_40 + 2.777777777777778 b_max_41
   + 2.439024390243901 b_max_50 + 2.380952380952381 b_max_51
Subject To
 capacity_constr_0: x_00 + x_01 <= 506.9
 capacity_constr_1: x_10 + x_11 <= 599.9
 capacity_constr_2: x_20 + x_21 <= 579.3
 capacity_constr_3: x_30 + x_31 <= 563.8
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1028.7
 min_quality_constr_00: 12.62 x_00 - 2.32 x_10 + 16.04 x_20 + 41.46 x_30
   + 1028.7 a_min_00 >= -0
 max_quality_constr_00: - 32.38 x_00 - 47.32 x_10 - 28.96 x_20 - 3.54 x_30
   - 1028.7 a_max_00 <= -0
 goal_quality_constr_00: - 13.3 x_00 - 28.24 x_10 - 9.88 x_20 + 15.54 x_30
   + b_min_00 - b_max_00 = -0
 min_quality_constr_10: 1.7 x_00 + 0.48 x_10 + 1.05 x_20 + 0.44 x_30
   + 1028.7 a_min_10 >= -0
 max_quality_constr_10: 0.2 x_00 - 1.02 x_10 - 0.45 x_20 - 1.06 x_30
   - 1028.7 a_max_10 <= -0
 goal_quality_constr_10: 1.03 x_00 - 0.19 x_10 + 0.38 x_20 - 0.23 x_30
   + b_min_10 - b_max_10 = -0
 min_quality_constr_20: 0.35 x_00 + 5.78 x_10 + 2.43 x_20 + 5.5 x_30
   + 1028.7 a_min_20 >= -0
 max_quality_constr_20: - 0.15 x_00 + 5.28 x_10 + 1.93 x_20 + 5 x_30
   - 1028.7 a_max_20 <= -0
 goal_quality_constr_20: 0.3 x_00 + 5.73 x_10 + 2.38 x_20 + 5.45 x_30
   + b_min_20 - b_max_20 = -0
 min_quality_constr_30: 0.67 x_00 + 4.65 x_10 + 2.28 x_20 + 4 x_30
   + 1028.7 a_min_30 >= -0
 max_quality_constr_30: 0.17 x_00 + 4.15 x_10 + 1.78 x_20 + 3.5 x_30
   - 1028.7 a_max_30 <= -0
 goal_quality_constr_30: 0.5 x_00 + 4.48 x_10 + 2.11 x_20 + 3.83 x_30
   + b_min_30 - b_max_30 = -0
 min_quality_constr_40: 0.34 x_00 + 0.36 x_10 + 0.18 x_20 + 0.95 x_30
   + 1028.7 a_min_40 >= -0
 max_quality_constr_40: - 0.66 x_00 - 0.64 x_10 - 0.82 x_20 - 0.05 x_30
   - 1028.7 a_max_40 <= -0
 goal_quality_constr_40: - 0.22 x_00 - 0.2 x_10 - 0.38 x_20 + 0.39 x_30
   + b_min_40 - b_max_40 = -0
 min_quality_constr_50: - 0.53 x_00 + 1.03 x_10 + 0.12 x_20 + 2.19 x_30
   + 1028.7 a_min_50 >= -0
 max_quality_constr_50: - 2.03 x_00 - 0.47 x_10 - 1.38 x_20 + 0.69 x_30
   - 1028.7 a_max_50 <= -0
 goal_quality_constr_50: - 1.62 x_00 - 0.06 x_10 - 0.97 x_20 + 1.1 x_30
   + b_min_50 - b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 1019.3
 min_quality_constr_01: 12.62 x_01 - 2.32 x_11 + 16.04 x_21 + 41.46 x_31
   + 1019.3 a_min_01 >= -0
 max_quality_constr_01: - 32.38 x_01 - 47.32 x_11 - 28.96 x_21 - 3.54 x_31
   - 1019.3 a_max_01 <= -0
 goal_quality_constr_01: 4.3 x_01 - 10.64 x_11 + 7.72 x_21 + 33.14 x_31
   + b_min_01 - b_max_01 = -0
 min_quality_constr_11: 1.7 x_01 + 0.48 x_11 + 1.05 x_21 + 0.44 x_31
   + 1019.3 a_min_11 >= -0
 max_quality_constr_11: 0.2 x_01 - 1.02 x_11 - 0.45 x_21 - 1.06 x_31
   - 1019.3 a_max_11 <= -0
 goal_quality_constr_11: 1.67 x_01 + 0.45 x_11 + 1.02 x_21 + 0.41 x_31
   + b_min_11 - b_max_11 = -0
 min_quality_constr_21: 0.35 x_01 + 5.78 x_11 + 2.43 x_21 + 5.5 x_31
   + 1019.3 a_min_21 >= -0
 max_quality_constr_21: - 0.15 x_01 + 5.28 x_11 + 1.93 x_21 + 5 x_31
   - 1019.3 a_max_21 <= -0
 goal_quality_constr_21: - 0.03 x_01 + 5.4 x_11 + 2.05 x_21 + 5.12 x_31
   + b_min_21 - b_max_21 = -0
 min_quality_constr_31: 0.67 x_01 + 4.65 x_11 + 2.28 x_21 + 4 x_31
   + 1019.3 a_min_31 >= -0
 max_quality_constr_31: 0.17 x_01 + 4.15 x_11 + 1.78 x_21 + 3.5 x_31
   - 1019.3 a_max_31 <= -0
 goal_quality_constr_31: 0.44 x_01 + 4.42 x_11 + 2.05 x_21 + 3.77 x_31
   + b_min_31 - b_max_31 = -0
 min_quality_constr_41: 0.34 x_01 + 0.36 x_11 + 0.18 x_21 + 0.95 x_31
   + 1019.3 a_min_41 >= -0
 max_quality_constr_41: - 0.66 x_01 - 0.64 x_11 - 0.82 x_21 - 0.05 x_31
   - 1019.3 a_max_41 <= -0
 goal_quality_constr_41: - 0.02 x_01 - 0.18 x_21 + 0.59 x_31 + b_min_41
   - b_max_41 = -0
 min_quality_constr_51: - 0.53 x_01 + 1.03 x_11 + 0.12 x_21 + 2.19 x_31
   + 1019.3 a_min_51 >= -0
 max_quality_constr_51: - 2.03 x_01 - 0.47 x_11 - 1.38 x_21 + 0.69 x_31
   - 1019.3 a_max_51 <= -0
 goal_quality_constr_51: - 1.61 x_01 - 0.05 x_11 - 0.96 x_21 + 1.11 x_31
   + b_min_51 - b_max_51 = -0
Bounds
End
