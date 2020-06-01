\ Model Ore Mixing Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  324.7807729782396 a_max_00 + 984.2519685039374 a_max_01
   + 3.333333333333333e+06 a_max_10 + 4.5454545454545459e+06 a_max_11
   + 1.1111111111111108e+06 a_max_20 + 222222.2222222222 a_max_21
   + 222222.2222222222 a_max_30 + 263157.8947368421 a_max_31
   + 322580.6451612902 a_max_40 + 833333.3333333334 a_max_41
   + 90909.09090909091 a_max_50 + 1.6666666666666775e+06 a_max_51
   + 703.729767769177 a_min_00 + 287.0264064293915 a_min_01
   + 833333.3333333334 a_min_10 + 781250 a_min_11
   + 243902.4390243902 a_min_20 + 2e+06 a_min_21 + 2e+06 a_min_30
   + 833333.3333333334 a_min_31 + 144927.5362318841 a_min_40
   + 113636.3636363636 a_min_41 + 250000 a_min_50
   + 69444.44444444442 a_min_51 + 0.0703729767769177 b_min_00
   + 0.0984251968503937 b_min_01 + 3.333333333333333 b_min_10
   + 4.545454545454546 b_min_11 + 11.11111111111111 b_min_20 + 20 b_min_21
   + 20 b_min_30 + 8.333333333333334 b_min_31 + 3.225806451612903 b_min_40
   + 8.333333333333334 b_min_41 + 2.5 b_min_50 + 16.66666666666677 b_min_51
   + 0.0703729767769177 b_max_00 + 0.0984251968503937 b_max_01
   + 3.333333333333333 b_max_10 + 4.545454545454546 b_max_11
   + 11.11111111111111 b_max_20 + 20 b_max_21 + 20 b_max_30
   + 8.333333333333334 b_max_31 + 3.225806451612903 b_max_40
   + 8.333333333333334 b_max_41 + 2.5 b_max_50 + 16.66666666666677 b_max_51
Subject To
 input_weight_constr_0: y_00 + y_01 + y_02 + y_03 <= 72.7
 capacity_constr_0: y_00 <= 223.2
 weight_constr_00: x_00 + x_01 - y_00 <= 604
 capacity_constr_1: y_01 <= 77.4
 weight_constr_10: x_10 + x_11 - y_01 <= 649.6
 capacity_constr_2: y_02 <= 2.9
 weight_constr_20: x_20 + x_21 - y_02 <= 1009.7
 capacity_constr_3: y_03 <= 325.7
 weight_constr_30: x_30 + x_31 - y_03 <= 596.3
 demand_constr_0: x_00 + x_10 + x_20 + x_30 = 1146.6
 min_quality_constr_00: 28.75 x_00 + 20.17 x_10 + 30.13 x_20 + 3.09 x_30
   + 1146.6 a_min_00 >= -0
 max_quality_constr_00: - 16.25 x_00 - 24.83 x_10 - 14.87 x_20 - 41.91 x_30
   - 1146.6 a_max_00 <= -0
 goal_quality_constr_00: 14.54 x_00 + 5.96 x_10 + 15.92 x_20 - 11.12 x_30
   + 1146.6 b_min_00 - 1146.6 b_max_00 = -0
 min_quality_constr_10: 0.05 x_00 + 0.72 x_10 + 2.08 x_20 + 1.34 x_30
   + 1146.6 a_min_10 >= -0
 max_quality_constr_10: - 1.45 x_00 - 0.78 x_10 + 0.58 x_20 - 0.16 x_30
   - 1146.6 a_max_10 <= -0
 goal_quality_constr_10: - 1.15 x_00 - 0.48 x_10 + 0.88 x_20 + 0.14 x_30
   + 1146.6 b_min_10 - 1146.6 b_max_10 = -0
 min_quality_constr_20: 5.44 x_00 + 6.54 x_10 + 1.38 x_20 + 2.89 x_30
   + 1146.6 a_min_20 >= -0
 max_quality_constr_20: 4.94 x_00 + 6.04 x_10 + 0.88 x_20 + 2.39 x_30
   - 1146.6 a_max_20 <= -0
 goal_quality_constr_20: 5.03 x_00 + 6.13 x_10 + 0.97 x_20 + 2.48 x_30
   + 1146.6 b_min_20 - 1146.6 b_max_20 = -0
 min_quality_constr_30: 6.02 x_00 + 4.35 x_10 + 0.85 x_20 + 0.56 x_30
   + 1146.6 a_min_30 >= -0
 max_quality_constr_30: 5.52 x_00 + 3.85 x_10 + 0.35 x_20 + 0.06 x_30
   - 1146.6 a_max_30 <= -0
 goal_quality_constr_30: 5.97 x_00 + 4.3 x_10 + 0.8 x_20 + 0.51 x_30
   + 1146.6 b_min_30 - 1146.6 b_max_30 = -0
 min_quality_constr_40: 0.87 x_00 + 0.41 x_10 + 0.17 x_20 + 0.55 x_30
   + 1146.6 a_min_40 >= -0
 max_quality_constr_40: - 0.13 x_00 - 0.59 x_10 - 0.83 x_20 - 0.45 x_30
   - 1146.6 a_max_40 <= -0
 goal_quality_constr_40: 0.18 x_00 - 0.28 x_10 - 0.52 x_20 - 0.14 x_30
   + 1146.6 b_min_40 - 1146.6 b_max_40 = -0
 min_quality_constr_50: - 0.88 x_00 + 1.26 x_10 - 0.88 x_20 - 1.01 x_30
   + 1146.6 a_min_50 >= -0
 max_quality_constr_50: - 2.38 x_00 - 0.24 x_10 - 2.38 x_20 - 2.51 x_30
   - 1146.6 a_max_50 <= -0
 goal_quality_constr_50: - 1.28 x_00 + 0.86 x_10 - 1.28 x_20 - 1.41 x_30
   + 1146.6 b_min_50 - 1146.6 b_max_50 = -0
 demand_constr_1: x_01 + x_11 + x_21 + x_31 = 755.7
 min_quality_constr_01: 28.75 x_01 + 20.17 x_11 + 30.13 x_21 + 3.09 x_31
   + 755.7 a_min_01 >= -0
 max_quality_constr_01: - 16.25 x_01 - 24.83 x_11 - 14.87 x_21 - 41.91 x_31
   - 755.7 a_max_01 <= -0
 goal_quality_constr_01: - 6.09 x_01 - 14.67 x_11 - 4.71 x_21 - 31.75 x_31
   + 755.7 b_min_01 - 755.7 b_max_01 = -0
 min_quality_constr_11: 0.05 x_01 + 0.72 x_11 + 2.08 x_21 + 1.34 x_31
   + 755.7 a_min_11 >= -0
 max_quality_constr_11: - 1.45 x_01 - 0.78 x_11 + 0.58 x_21 - 0.16 x_31
   - 755.7 a_max_11 <= -0
 goal_quality_constr_11: - 1.23 x_01 - 0.56 x_11 + 0.8 x_21 + 0.06 x_31
   + 755.7 b_min_11 - 755.7 b_max_11 = -0
 min_quality_constr_21: 5.44 x_01 + 6.54 x_11 + 1.38 x_21 + 2.89 x_31
   + 755.7 a_min_21 >= -0
 max_quality_constr_21: 4.94 x_01 + 6.04 x_11 + 0.88 x_21 + 2.39 x_31
   - 755.7 a_max_21 <= -0
 goal_quality_constr_21: 5.39 x_01 + 6.49 x_11 + 1.33 x_21 + 2.84 x_31
   + 755.7 b_min_21 - 755.7 b_max_21 = -0
 min_quality_constr_31: 6.02 x_01 + 4.35 x_11 + 0.85 x_21 + 0.56 x_31
   + 755.7 a_min_31 >= -0
 max_quality_constr_31: 5.52 x_01 + 3.85 x_11 + 0.35 x_21 + 0.06 x_31
   - 755.7 a_max_31 <= -0
 goal_quality_constr_31: 5.9 x_01 + 4.23 x_11 + 0.73 x_21 + 0.44 x_31
   + 755.7 b_min_31 - 755.7 b_max_31 = -0
 min_quality_constr_41: 0.87 x_01 + 0.41 x_11 + 0.17 x_21 + 0.55 x_31
   + 755.7 a_min_41 >= -0
 max_quality_constr_41: - 0.13 x_01 - 0.59 x_11 - 0.83 x_21 - 0.45 x_31
   - 755.7 a_max_41 <= -0
 goal_quality_constr_41: - 0.01 x_01 - 0.47 x_11 - 0.71 x_21 - 0.33 x_31
   + 755.7 b_min_41 - 755.7 b_max_41 = -0
 min_quality_constr_51: - 0.88 x_01 + 1.26 x_11 - 0.88 x_21 - 1.01 x_31
   + 755.7 a_min_51 >= -0
 max_quality_constr_51: - 2.38 x_01 - 0.24 x_11 - 2.38 x_21 - 2.51 x_31
   - 755.7 a_max_51 <= -0
 goal_quality_constr_51: - 2.32 x_01 - 0.18 x_11 - 2.32 x_21 - 2.45 x_31
   + 755.7 b_min_51 - 755.7 b_max_51 = -0
Bounds
End
