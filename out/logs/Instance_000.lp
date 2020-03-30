\ Model Mistura de Minérios
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.1 a_max_0 + 0.6666666666666666 a_max_1 + 2 a_max_2 + 2 a_max_3
   + 25 a_max_4 + 2 a_max_5 + 0.0285714285714286 a_min_0 + a_min_1
   + a_min_2 + a_min_3 + 20 a_min_4 + a_min_5
Subject To
 constr(0): x_0 + x_1 + x_2 + x_3 = 1000
 constr(1): x_0 <= 400
 constr(2): x_1 <= 400
 constr(3): x_2 <= 400
 constr(4): x_3 <= 400
 constr(5): 5 x_0 - 5 x_1 + 15 x_2 + 15 x_3 + 1000 a_min_0 >= -0
 constr(6): - 40 x_0 - 50 x_1 - 30 x_2 - 30 x_3 - 1000 a_max_0 <= -0
 constr(7): x_0 + 0.5 x_1 + x_2 + 2 x_3 + 1000 a_min_1 >= -0
 constr(8): - 0.5 x_0 - x_1 - 0.5 x_2 + 0.5 x_3 - 1000 a_max_1 <= -0
 constr(9): 0.5 x_0 + 0.5 x_1 + 0.5 x_2 + 0.5 x_3 + 1000 a_min_2 >= -0
 constr(10): - 1000 a_max_2 <= -0
 constr(11): x_0 + x_1 + x_2 + x_3 + 1000 a_min_3 >= -0
 constr(12): 0.5 x_0 + 0.5 x_1 + 0.5 x_2 + 0.5 x_3 - 1000 a_max_3 <= -0
 constr(13): 0.05 x_0 + 0.05 x_1 + 0.05 x_2 + 0.05 x_3 + 1000 a_min_4
   >= -0
 constr(14): - 0.04 x_0 - 0.04 x_1 - 0.04 x_2 - 0.04 x_3 - 1000 a_max_4
   <= -0
 constr(15): 0.5 x_0 + 0.5 x_1 - 0.5 x_2 + 1.5 x_3 + 1000 a_min_5 >= -0
 constr(16): - x_0 - x_1 - 2 x_2 - 1000 a_max_5 <= -0
Bounds
End
