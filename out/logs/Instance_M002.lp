\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  22.76867030965391 a_max_00 + 27.18868950516585 a_max_01
   + 3703.703703703703 a_max_10 + 2173.913043478261 a_max_11
   + 5000 a_max_20 + 3333.333333333333 a_max_21 + 10000 a_max_30
   + 3571.428571428571 a_max_31 + 1818.181818181818 a_max_40
   + 1282.051282051282 a_max_41 + 862.0689655172413 a_max_50
   + 840.3361344537815 a_max_51 + 925.9259259259273 a_min_00
   + 121.654501216545 a_min_01 + 813.0081300813008 a_min_10
   + 961.5384615384614 a_min_11 + 3333.333333333333 a_min_20
   + 5000 a_min_21 + 2500 a_min_30 + 4545.454545454546 a_min_31
   + 2222.222222222222 a_min_40 + 4545.454545454546 a_min_41
   + 2941.176470588236 a_min_50 + 3225.806451612902 a_min_51
   + 0.9259259259259274 b_min_00 + 0.121654501216545 b_min_01
   + 3.703703703703703 b_min_10 + 2.173913043478261 b_min_11 + 5 b_min_20
   + 5 b_min_21 + 10 b_min_30 + 4.545454545454546 b_min_31
   + 2.222222222222222 b_min_40 + 4.545454545454546 b_min_41
   + 2.941176470588236 b_min_50 + 3.225806451612903 b_min_51
   + 0.9259259259259274 b_max_0 + 0.121654501216545 b_max_0
   + 3.703703703703703 b_max_1 + 2.173913043478261 b_max_1 + 5 b_max_2
   + 5 b_max_2 + 10 b_max_3 + 4.545454545454546 b_max_3
   + 2.222222222222222 b_max_4 + 4.545454545454546 b_max_4
   + 2.941176470588236 b_max_5 + 3.225806451612903 b_max_5
Subject To
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1106
 capacity_constr_00: x_00 <= 227
 capacity_constr_10: x_10 <= 372
 capacity_constr_20: x_20 <= 342
 capacity_constr_30: x_30 <= 272
 min_quality_constr_00: - 12.6 x_00 + 17.98 x_10 + 15.31 x_20 + 16.46 x_30
   + 1106 a_min_00 >= -0
 max_quality_constr_00: - 57.6 x_00 - 27.02 x_10 - 29.69 x_20 - 28.54 x_30
   - 1106 a_max_00 <= -0
 goal_quality_constr_00: - 13.68 x_00 + 16.9 x_10 + 14.23 x_20 + 15.38 x_30
   + b_min_00 - b_max_0 = -0
 min_quality_constr_10: 0.94 x_00 + 1.84 x_10 + 1.3 x_20 + 0.42 x_30
   + 1106 a_min_10 >= -0
 max_quality_constr_10: - 0.56 x_00 + 0.34 x_10 - 0.2 x_20 - 1.08 x_30
   - 1106 a_max_10 <= -0
 goal_quality_constr_10: - 0.29 x_00 + 0.61 x_10 + 0.07 x_20 - 0.81 x_30
   + b_min_10 - b_max_1 = -0
 min_quality_constr_20: 3.79 x_00 + 6.33 x_10 + 0.42 x_20 + 2.7 x_30
   + 1106 a_min_20 >= -0
 max_quality_constr_20: 3.29 x_00 + 5.83 x_10 - 0.08 x_20 + 2.2 x_30
   - 1106 a_max_20 <= -0
 goal_quality_constr_20: 3.49 x_00 + 6.03 x_10 + 0.12 x_20 + 2.4 x_30
   + b_min_20 - b_max_2 = -0
 min_quality_constr_30: 2.49 x_00 + 5.58 x_10 + 5.77 x_20 + 4.58 x_30
   + 1106 a_min_30 >= -0
 max_quality_constr_30: 1.99 x_00 + 5.08 x_10 + 5.27 x_20 + 4.08 x_30
   - 1106 a_max_30 <= -0
 goal_quality_constr_30: 2.09 x_00 + 5.18 x_10 + 5.37 x_20 + 4.18 x_30
   + b_min_30 - b_max_3 = -0
 min_quality_constr_40: 0.19 x_00 + 0.93 x_10 + 0.54 x_20 + 1.03 x_30
   + 1106 a_min_40 >= -0
 max_quality_constr_40: - 0.81 x_00 - 0.07 x_10 - 0.46 x_20 + 0.03 x_30
   - 1106 a_max_40 <= -0
 goal_quality_constr_40: - 0.26 x_00 + 0.48 x_10 + 0.09 x_20 + 0.58 x_30
   + b_min_40 - b_max_4 = -0
 min_quality_constr_50: 3.23 x_00 - 0.06 x_10 - 0.74 x_20 + 3.21 x_30
   + 1106 a_min_50 >= -0
 max_quality_constr_50: 1.73 x_00 - 1.56 x_10 - 2.24 x_20 + 1.71 x_30
   - 1106 a_max_50 <= -0
 goal_quality_constr_50: 2.89 x_00 - 0.4 x_10 - 1.08 x_20 + 2.87 x_30
   + b_min_50 - b_max_5 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 650
 capacity_constr_01: x_01 <= 227
 capacity_constr_11: x_11 <= 372
 capacity_constr_21: x_21 <= 342
 capacity_constr_31: x_31 <= 272
 min_quality_constr_01: - 12.6 x_01 + 17.98 x_11 + 15.31 x_21 + 16.46 x_31
   + 650 a_min_01 >= -0
 max_quality_constr_01: - 57.6 x_01 - 27.02 x_11 - 29.69 x_21 - 28.54 x_31
   - 650 a_max_01 <= -0
 goal_quality_constr_01: - 20.82 x_01 + 9.76 x_11 + 7.09 x_21 + 8.24 x_31
   + b_min_01 - b_max_0 = -0
 min_quality_constr_11: 0.94 x_01 + 1.84 x_11 + 1.3 x_21 + 0.42 x_31
   + 650 a_min_11 >= -0
 max_quality_constr_11: - 0.56 x_01 + 0.34 x_11 - 0.2 x_21 - 1.08 x_31
   - 650 a_max_11 <= -0
 goal_quality_constr_11: - 0.1 x_01 + 0.8 x_11 + 0.26 x_21 - 0.62 x_31
   + b_min_11 - b_max_1 = -0
 min_quality_constr_21: 3.79 x_01 + 6.33 x_11 + 0.42 x_21 + 2.7 x_31
   + 650 a_min_21 >= -0
 max_quality_constr_21: 3.29 x_01 + 5.83 x_11 - 0.08 x_21 + 2.2 x_31
   - 650 a_max_21 <= -0
 goal_quality_constr_21: 3.59 x_01 + 6.13 x_11 + 0.22 x_21 + 2.5 x_31
   + b_min_21 - b_max_2 = -0
 min_quality_constr_31: 2.49 x_01 + 5.58 x_11 + 5.77 x_21 + 4.58 x_31
   + 650 a_min_31 >= -0
 max_quality_constr_31: 1.99 x_01 + 5.08 x_11 + 5.27 x_21 + 4.08 x_31
   - 650 a_max_31 <= -0
 goal_quality_constr_31: 2.27 x_01 + 5.36 x_11 + 5.55 x_21 + 4.36 x_31
   + b_min_31 - b_max_3 = -0
 min_quality_constr_41: 0.19 x_01 + 0.93 x_11 + 0.54 x_21 + 1.03 x_31
   + 650 a_min_41 >= -0
 max_quality_constr_41: - 0.81 x_01 - 0.07 x_11 - 0.46 x_21 + 0.03 x_31
   - 650 a_max_41 <= -0
 goal_quality_constr_41: - 0.03 x_01 + 0.71 x_11 + 0.32 x_21 + 0.81 x_31
   + b_min_41 - b_max_4 = -0
 min_quality_constr_51: 3.23 x_01 - 0.06 x_11 - 0.74 x_21 + 3.21 x_31
   + 650 a_min_51 >= -0
 max_quality_constr_51: 1.73 x_01 - 1.56 x_11 - 2.24 x_21 + 1.71 x_31
   - 650 a_max_51 <= -0
 goal_quality_constr_51: 2.92 x_01 - 0.37 x_11 - 1.05 x_21 + 2.9 x_31
   + b_min_51 - b_max_5 = -0
Bounds
End
