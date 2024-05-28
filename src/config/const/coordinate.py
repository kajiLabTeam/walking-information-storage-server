from typing import List

# x, y, 歩幅, 進行方向, 角度の変化量
CORRECT_TRAJECTORY_COORDINATES1: List[List[int]] = [
    [1519, 1707, 0, 180, 0],
    [1496, 1683, 33, 316, 136],
    [1479, 1647, 39, 335, 19],
    [1480, 1604, 43, 1, 26],
    [1478, 1557, 47, 358, 357],
    [1480, 1507, 50, 2, 4],
    [1481, 1454, 53, 1, 359],
    [1486, 1403, 51, 6, 5],
    [1487, 1352, 51, 1, 355],
    [1491, 1304, 48, 5, 4],
    [1492, 1253, 51, 1, 356],
    [1495, 1204, 49, 4, 3],
    [1495, 1154, 50, 0, 356],
    [1496, 1106, 48, 1, 1],
    [1493, 1055, 51, 357, 356],
    [1495, 1001, 54, 2, 5],
    [1498, 947, 54, 3, 1],
    [1501, 894, 53, 3, 0],
    [1504, 842, 52, 3, 0],
    [1502, 791, 51, 358, 355],
    [1502, 741, 50, 0, 2],
    [1487, 698, 45, 341, 341],
    [1462, 665, 41, 323, 342],
    [1420, 645, 46, 295, 332],
    [1373, 631, 49, 287, 352],
    [1321, 628, 52, 273, 346],
    [1270, 624, 51, 274, 1],
    [1218, 621, 52, 273, 359],
    [1168, 614, 50, 278, 5],
    [1120, 601, 49, 285, 7],
    [1079, 587, 43, 289, 4],
    [1054, 563, 34, 314, 25],
    [1040, 532, 34, 336, 22],
    [1037, 497, 35, 355, 19],
    [1035, 460, 37, 357, 2],
    [1036, 434, 26, 2, 5],
    [1036, 418, 16, 0, 358],
    [1035, 414, 4, 346, 346],
    [1036, 414, 1, 90, 104],
    [1038, 412, 2, 45, 315],
    [1036, 408, 4, 333, 288],
    [1032, 405, 5, 307, 334],
    [1030, 401, 4, 333, 26],
    [1034, 390, 11, 20, 47],
    [1026, 374, 17, 333, 313],
    [1017, 361, 15, 325, 352],
    [998, 362, 19, 267, 302],
    [971, 357, 27, 280, 13],
    [939, 353, 32, 277, 357],
    [902, 354, 37, 268, 351],
    [867, 362, 35, 257, 349],
    [840, 375, 29, 244, 347],
    [830, 394, 21, 208, 324],
    [825, 412, 18, 196, 348],
    [826, 425, 13, 176, 340],
    [829, 435, 10, 163, 347],
    [827, 446, 11, 190, 27],
    [829, 449, 3, 146, 316],
    [828, 454, 5, 191, 45],
    [822, 463, 10, 214, 23],
    [820, 482, 19, 186, 332],
    [821, 516, 34, 178, 352],
    [813, 549, 33, 194, 16],
    [801, 581, 34, 201, 7],
    [776, 603, 33, 229, 28],
    [749, 622, 33, 235, 6],
    [714, 631, 36, 256, 21],
    [672, 648, 45, 248, 352],
    [634, 672, 44, 238, 350],
    [608, 710, 46, 214, 336],
    [592, 753, 45, 200, 346],
    [591, 804, 51, 181, 341],
    [590, 856, 52, 181, 0],
    [596, 907, 51, 173, 352],
    [595, 957, 50, 181, 8],
    [597, 1009, 52, 178, 357],
    [598, 1062, 53, 179, 1],
    [601, 1112, 50, 177, 358],
    [602, 1158, 46, 179, 2],
    [611, 1200, 42, 168, 349],
    [639, 1228, 39, 135, 327],
    [679, 1245, 43, 113, 338],
    [728, 1253, 49, 99, 346],
    [778, 1260, 50, 98, 359],
    [832, 1260, 54, 90, 352],
    [886, 1263, 54, 93, 3],
    [941, 1258, 55, 85, 352],
    [996, 1260, 55, 92, 7],
    [1050, 1259, 54, 89, 357],
    [1104, 1263, 54, 94, 5],
    [1155, 1265, 51, 92, 358],
    [1191, 1274, 37, 104, 12],
    [1208, 1276, 17, 97, 353],
    [1208, 1275, 1, 0, 263],
    [1212, 1272, 5, 53, 53],
    [1241, 1265, 29, 76, 23],
    [1285, 1263, 44, 87, 11],
    [1338, 1258, 53, 85, 358],
    [1387, 1262, 49, 95, 10],
    [1426, 1284, 44, 119, 24],
    [1449, 1322, 44, 149, 30],
    [1462, 1370, 49, 165, 16],
    [1470, 1421, 51, 171, 6],
    [1471, 1475, 54, 179, 8],
    [1474, 1531, 56, 177, 358],
    [1473, 1585, 54, 181, 4],
    [1472, 1638, 53, 181, 0],
    [1454, 1683, 48, 202, 21],
    [1421, 1713, 44, 228, 26],
    [1377, 1723, 45, 257, 29],
    [1326, 1729, 51, 263, 6],
    [1273, 1728, 53, 271, 8],
    [1217, 1728, 56, 270, 359],
    [1161, 1731, 56, 267, 357],
    [1109, 1732, 52, 269, 2],
    [1056, 1733, 53, 269, 0],
    [1008, 1722, 49, 283, 14],
    [969, 1697, 46, 303, 20],
    [949, 1660, 42, 332, 29],
    [933, 1617, 45, 340, 8],
    [930, 1570, 47, 356, 16],
    [926, 1520, 50, 355, 359],
    [929, 1471, 49, 4, 9],
    [929, 1420, 51, 0, 356],
    [932, 1370, 50, 3, 3],
    [931, 1318, 52, 359, 356],
    [934, 1267, 51, 3, 4],
    [935, 1217, 50, 1, 358],
    [937, 1168, 49, 2, 1],
    [934, 1118, 50, 357, 355],
    [934, 1065, 53, 0, 3],
    [936, 1012, 53, 2, 2],
    [938, 962, 50, 2, 0],
    [942, 912, 50, 5, 3],
    [945, 862, 50, 3, 358],
    [949, 812, 50, 5, 2],
    [944, 762, 50, 354, 349],
    [938, 714, 48, 353, 359],
    [917, 673, 46, 333, 340],
    [887, 641, 43, 317, 344],
    [845, 624, 45, 292, 335],
    [797, 615, 48, 281, 349],
    [748, 616, 49, 269, 348],
    [700, 618, 48, 268, 359],
    [656, 634, 46, 250, 342],
    [622, 666, 46, 227, 337],
    [602, 711, 49, 204, 337],
    [587, 757, 48, 198, 354],
    [583, 804, 47, 185, 347],
    [581, 852, 48, 182, 357],
    [585, 903, 51, 176, 354],
    [585, 954, 51, 180, 4],
    [590, 1005, 51, 174, 354],
    [592, 1054, 49, 178, 4],
    [601, 1105, 51, 170, 352],
    [614, 1152, 48, 165, 355],
    [645, 1188, 47, 139, 334],
    [682, 1211, 43, 122, 343],
    [726, 1222, 45, 104, 342],
    [774, 1230, 48, 99, 355],
    [824, 1232, 50, 92, 353],
    [875, 1236, 51, 94, 2],
    [926, 1239, 51, 93, 359],
    [978, 1243, 52, 94, 1],
    [1030, 1249, 52, 97, 3],
    [1083, 1251, 53, 92, 355],
    [1133, 1252, 50, 91, 359],
    [1182, 1249, 49, 86, 355],
    [1231, 1251, 49, 92, 6],
    [1280, 1247, 49, 85, 353],
    [1326, 1243, 46, 85, 0],
    [1370, 1223, 48, 66, 341],
    [1407, 1197, 45, 55, 349],
    [1430, 1157, 46, 30, 335],
    [1449, 1114, 47, 24, 354],
    [1459, 1065, 50, 12, 348],
    [1469, 1015, 50, 11, 359],
    [1475, 961, 54, 6, 355],
    [1482, 907, 54, 7, 1],
    [1486, 851, 56, 4, 357],
    [1492, 796, 55, 6, 2],
    [1501, 740, 56, 9, 3],
    [1518, 688, 54, 18, 9],
    [1551, 646, 53, 38, 20],
    [1591, 613, 51, 50, 12],
    [1639, 593, 52, 67, 17],
    [1690, 579, 52, 75, 8],
    [1741, 572, 51, 82, 7],
    [1789, 569, 48, 86, 4],
    [1830, 579, 42, 104, 18],
    [1860, 601, 37, 126, 22],
    [1874, 635, 36, 158, 32],
    [1879, 672, 37, 172, 14],
    [1878, 708, 36, 182, 10],
    [1882, 748, 40, 174, 352],
    [1895, 783, 37, 160, 346],
    [1922, 808, 36, 133, 333],
    [1955, 825, 37, 117, 344],
    [1994, 833, 39, 102, 345],
    [2036, 839, 42, 98, 356],
    [2079, 839, 43, 90, 352],
    [2122, 840, 43, 91, 1],
    [2167, 836, 45, 85, 354],
    [2211, 833, 44, 86, 1],
    [2256, 824, 45, 79, 353],
    [2300, 822, 44, 87, 8],
    [2343, 816, 43, 82, 355],
    [2390, 821, 47, 96, 14],
    [2437, 825, 47, 95, 359],
    [2483, 829, 46, 95, 0],
    [2533, 831, 50, 92, 357],
    [2583, 835, 50, 95, 3],
    [2632, 841, 49, 97, 2],
    [2679, 841, 47, 90, 353],
    [2721, 835, 42, 82, 352],
    [2751, 808, 40, 48, 326],
    [2770, 772, 40, 28, 340],
    [2777, 733, 39, 10, 342],
    [2785, 695, 38, 12, 2],
    [2786, 655, 40, 1, 349],
    [2789, 612, 43, 4, 3],
    [2787, 567, 45, 357, 353],
    [2783, 526, 41, 354, 357],
    [2763, 492, 39, 330, 336],
    [2735, 464, 39, 315, 345],
    [2696, 449, 41, 291, 336],
    [2659, 438, 38, 287, 356],
    [2623, 440, 36, 267, 340],
    [2584, 442, 39, 267, 0],
    [2538, 448, 46, 263, 356],
    [2493, 452, 45, 265, 2],
    [2453, 464, 41, 253, 348],
    [2417, 479, 39, 247, 354],
    [2395, 510, 38, 215, 328],
    [2379, 546, 39, 204, 349],
    [2378, 588, 42, 181, 337],
    [2374, 631, 43, 185, 4],
    [2379, 675, 44, 174, 349],
    [2378, 718, 43, 181, 7],
    [2373, 757, 39, 187, 6],
    [2359, 785, 31, 207, 20],
    [2343, 808, 28, 215, 8],
    [2316, 812, 27, 262, 47],
    [2279, 821, 38, 256, 354],
    [2236, 823, 43, 267, 11],
    [2192, 831, 44, 260, 353],
    [2148, 836, 44, 264, 4],
    [2104, 844, 44, 260, 356],
    [2062, 845, 42, 269, 9],
    [2025, 850, 37, 262, 353],
    [1990, 848, 35, 273, 11],
    [1960, 858, 31, 252, 339],
    [1932, 874, 32, 240, 348],
    [1907, 906, 40, 218, 338],
    [1884, 945, 45, 211, 353],
    [1867, 989, 47, 201, 350],
    [1850, 1035, 49, 200, 359],
    [1842, 1086, 51, 189, 349],
    [1832, 1131, 46, 193, 4],
    [1830, 1173, 42, 183, 350],
    [1826, 1219, 46, 185, 2],
    [1828, 1268, 49, 178, 353],
    [1824, 1319, 51, 184, 6],
    [1823, 1371, 52, 181, 357],
    [1820, 1424, 53, 183, 2],
    [1820, 1478, 54, 180, 357],
    [1815, 1534, 56, 185, 5],
    [1815, 1589, 55, 180, 355],
    [1808, 1640, 51, 188, 8],
    [1793, 1683, 45, 199, 11],
    [1763, 1709, 39, 229, 30],
    [1724, 1722, 41, 252, 23],
    [1688, 1726, 36, 264, 12],
    [1663, 1722, 25, 279, 15],
    [1655, 1723, 8, 263, 344],
    [1652, 1721, 3, 304, 41],
    [1652, 1722, 1, 180, 236],
]


# x, y, 歩幅, 進行方向, 角度の変化量
CORRECT_TRAJECTORY_COORDINATES2: List[List[int]] = [
    [461, 450, 0, 180, 0],
    [456, 486, 36, 188, 8],
    [457, 532, 46, 179, 351],
    [454, 582, 50, 183, 4],
    [452, 635, 53, 182, 359],
    [448, 692, 57, 184, 2],
    [449, 751, 59, 179, 355],
    [447, 807, 56, 182, 3],
    [446, 860, 53, 181, 359],
    [445, 914, 54, 181, 0],
    [446, 969, 55, 179, 358],
    [446, 1024, 55, 180, 1],
    [453, 1078, 54, 173, 353],
    [464, 1126, 49, 167, 354],
    [494, 1162, 46, 140, 333],
    [533, 1179, 42, 114, 334],
    [577, 1183, 44, 95, 341],
    [625, 1188, 48, 96, 1],
    [679, 1186, 54, 88, 352],
    [733, 1186, 54, 90, 2],
    [781, 1178, 48, 81, 351],
    [822, 1160, 44, 66, 345],
    [845, 1126, 41, 34, 328],
    [860, 1085, 43, 20, 346],
    [867, 1041, 44, 9, 349],
    [870, 990, 51, 3, 354],
    [872, 940, 50, 2, 359],
    [872, 885, 55, 0, 358],
    [873, 834, 51, 1, 1],
    [871, 780, 54, 358, 357],
    [872, 728, 52, 1, 3],
    [870, 672, 56, 358, 357],
    [873, 619, 53, 3, 5],
    [875, 563, 56, 2, 359],
    [890, 514, 51, 17, 15],
    [922, 474, 51, 39, 22],
    [964, 456, 45, 67, 28],
    [1012, 447, 48, 79, 12],
    [1062, 452, 50, 96, 17],
    [1114, 466, 53, 105, 9],
    [1150, 498, 48, 132, 27],
    [1175, 543, 51, 151, 19],
    [1182, 593, 50, 172, 21],
    [1185, 647, 54, 177, 5],
    [1184, 701, 54, 181, 4],
    [1186, 757, 56, 178, 357],
    [1186, 812, 55, 180, 2],
    [1200, 867, 56, 166, 346],
    [1229, 908, 50, 145, 339],
    [1275, 932, 51, 118, 333],
    [1327, 945, 53, 104, 346],
    [1378, 947, 51, 92, 348],
    [1417, 938, 40, 77, 345],
    [1443, 910, 38, 43, 326],
    [1456, 870, 42, 18, 335],
    [1457, 828, 42, 1, 343],
    [1457, 782, 46, 0, 359],
    [1462, 734, 48, 6, 6],
    [1465, 682, 52, 3, 357],
    [1469, 632, 50, 5, 2],
    [1472, 580, 52, 3, 358],
    [1465, 533, 47, 352, 349],
    [1441, 492, 47, 330, 338],
    [1407, 469, 41, 304, 334],
    [1368, 460, 40, 283, 339],
    [1327, 459, 41, 271, 348],
    [1280, 465, 47, 263, 352],
    [1238, 485, 46, 245, 342],
    [1212, 523, 46, 214, 329],
    [1197, 564, 43, 200, 346],
    [1193, 609, 45, 185, 345],
    [1188, 658, 49, 186, 1],
    [1189, 711, 53, 179, 353],
    [1186, 762, 51, 183, 4],
    [1190, 812, 50, 175, 352],
    [1192, 863, 51, 178, 3],
    [1199, 914, 51, 172, 354],
    [1202, 966, 52, 177, 5],
    [1204, 1018, 52, 178, 1],
    [1203, 1072, 54, 181, 3],
    [1190, 1120, 49, 195, 14],
    [1157, 1157, 49, 222, 27],
    [1115, 1179, 47, 242, 20],
    [1069, 1192, 47, 254, 12],
    [1021, 1195, 48, 266, 12],
    [975, 1191, 46, 275, 9],
    [935, 1167, 46, 301, 26],
    [905, 1128, 49, 322, 21],
    [890, 1083, 47, 342, 20],
    [878, 1034, 50, 346, 4],
    [875, 986, 48, 356, 10],
    [871, 935, 51, 356, 0],
    [872, 886, 49, 1, 5],
    [869, 835, 51, 357, 356],
    [871, 786, 49, 2, 5],
    [869, 733, 53, 358, 356],
    [871, 682, 51, 2, 4],
    [873, 629, 53, 2, 0],
    [879, 578, 51, 7, 5],
    [877, 525, 53, 358, 351],
    [871, 477, 48, 353, 355],
    [846, 433, 50, 330, 337],
    [815, 404, 42, 313, 343],
    [772, 389, 45, 289, 336],
    [726, 381, 46, 280, 351],
    [675, 383, 51, 268, 348],
    [623, 383, 52, 270, 2],
    [572, 388, 51, 264, 354],
    [526, 399, 47, 257, 353],
    [494, 429, 43, 227, 330],
    [472, 468, 44, 209, 342],
    [460, 511, 44, 196, 347],
    [453, 558, 47, 188, 352],
    [449, 604, 46, 185, 357],
    [449, 654, 50, 180, 355],
    [445, 704, 50, 185, 5],
    [445, 755, 51, 180, 355],
    [441, 802, 47, 185, 5],
    [444, 854, 52, 177, 352],
    [441, 904, 50, 183, 6],
    [441, 957, 53, 180, 357],
    [438, 1006, 49, 184, 4],
    [440, 1056, 50, 178, 354],
    [446, 1106, 50, 173, 355],
    [463, 1151, 48, 159, 346],
    [490, 1180, 39, 137, 338],
    [529, 1190, 40, 104, 327],
    [575, 1191, 46, 91, 347],
    [625, 1188, 50, 87, 356],
    [676, 1186, 51, 88, 1],
    [728, 1186, 52, 90, 2],
    [780, 1187, 52, 91, 1],
    [833, 1189, 53, 92, 1],
    [889, 1188, 56, 89, 357],
    [943, 1190, 54, 92, 3],
    [998, 1191, 55, 91, 359],
    [1053, 1190, 55, 89, 358],
    [1112, 1188, 59, 88, 359],
    [1168, 1189, 56, 91, 3],
    [1223, 1190, 55, 91, 0],
    [1278, 1194, 55, 94, 3],
    [1338, 1196, 60, 92, 358],
    [1395, 1200, 57, 94, 2],
    [1451, 1203, 56, 93, 359],
    [1506, 1205, 55, 92, 359],
    [1560, 1205, 54, 90, 358],
    [1609, 1211, 49, 97, 7],
    [1654, 1228, 48, 111, 14],
    [1678, 1265, 44, 147, 36],
    [1687, 1309, 44, 168, 21],
    [1679, 1348, 39, 192, 24],
    [1652, 1372, 36, 228, 36],
    [1613, 1374, 39, 267, 39],
    [1565, 1376, 48, 268, 1],
    [1517, 1368, 48, 279, 11],
    [1464, 1361, 53, 278, 359],
    [1418, 1343, 49, 291, 13],
    [1375, 1314, 51, 304, 13],
    [1345, 1272, 51, 324, 20],
    [1316, 1228, 52, 327, 3],
    [1290, 1179, 55, 332, 5],
    [1265, 1131, 54, 332, 0],
    [1240, 1080, 56, 334, 2],
    [1220, 1030, 53, 338, 4],
    [1202, 977, 55, 341, 3],
    [1193, 928, 49, 350, 9],
    [1187, 873, 55, 354, 4],
    [1184, 818, 55, 357, 3],
    [1183, 762, 56, 359, 2],
    [1182, 709, 53, 359, 0],
    [1180, 653, 56, 358, 359],
    [1178, 599, 54, 358, 0],
    [1170, 544, 55, 352, 354],
    [1152, 502, 45, 337, 345],
    [1121, 468, 46, 318, 341],
    [1083, 447, 43, 299, 341],
    [1033, 429, 53, 290, 351],
    [986, 416, 48, 285, 355],
    [936, 409, 50, 278, 353],
    [888, 404, 48, 276, 358],
    [836, 402, 52, 272, 356],
    [785, 397, 51, 276, 4],
    [729, 394, 56, 273, 357],
    [676, 391, 53, 273, 0],
    [617, 393, 59, 268, 355],
    [564, 394, 53, 269, 1],
    [515, 396, 49, 268, 359],
    [485, 399, 30, 264, 356],
    [472, 409, 16, 232, 328],
    [463, 415, 10, 236, 4],
    [461, 418, 3, 214, 338],
    [460, 419, 1, 225, 11],
    [460, 420, 1, 180, 315],
    [461, 421, 1, 135, 315],
    [462, 422, 1, 135, 0],
    [461, 422, 1, 270, 135],
    [459, 424, 2, 225, 315],
    [457, 426, 2, 225, 0],
]


# x, y, 歩幅, 進行方向, 角度の変化量
CORRECT_TRAJECTORY_COORDINATES3: List[List[int]] = [
    [4295, 1217, 0, 180, 0],
    [4274, 1193, 31, 319, 139],
    [4246, 1176, 32, 301, 342],
    [4217, 1164, 31, 292, 351],
    [4181, 1163, 36, 272, 340],
    [4144, 1154, 38, 284, 12],
    [4106, 1151, 38, 275, 351],
    [4070, 1138, 38, 290, 15],
    [4037, 1126, 35, 290, 0],
    [4001, 1110, 39, 294, 4],
    [3964, 1095, 39, 292, 358],
    [3924, 1089, 40, 279, 347],
    [3891, 1070, 38, 300, 21],
    [3853, 1052, 42, 295, 355],
    [3820, 1028, 40, 306, 11],
    [3778, 1013, 44, 290, 344],
    [3737, 1002, 42, 285, 355],
    [3698, 992, 40, 284, 359],
    [3657, 996, 41, 264, 340],
    [3614, 998, 43, 267, 3],
    [3587, 1026, 38, 224, 317],
    [3568, 1056, 35, 212, 348],
    [3565, 1103, 47, 184, 332],
    [3564, 1151, 48, 181, 357],
    [3563, 1201, 50, 181, 0],
    [3575, 1249, 49, 166, 345],
    [3574, 1292, 43, 181, 15],
    [3583, 1338, 46, 169, 348],
    [3585, 1392, 54, 178, 9],
    [3579, 1442, 50, 187, 9],
    [3579, 1493, 51, 180, 353],
    [3556, 1537, 49, 208, 28],
    [3520, 1560, 42, 237, 29],
    [3475, 1568, 45, 260, 23],
    [3431, 1562, 44, 278, 18],
    [3386, 1569, 45, 261, 343],
    [3337, 1567, 49, 272, 11],
    [3283, 1570, 54, 267, 355],
    [3231, 1573, 52, 267, 0],
    [3183, 1568, 48, 276, 9],
    [3129, 1571, 54, 267, 351],
    [3083, 1566, 46, 276, 9],
    [3032, 1559, 51, 278, 2],
    [2985, 1566, 47, 262, 344],
    [2945, 1546, 44, 297, 35],
    [2904, 1528, 44, 294, 357],
    [2876, 1492, 45, 322, 28],
    [2856, 1449, 47, 335, 13],
    [2836, 1411, 42, 332, 357],
    [2836, 1369, 42, 0, 28],
    [2825, 1329, 41, 345, 345],
    [2827, 1287, 42, 3, 18],
    [2828, 1241, 46, 1, 358],
    [2825, 1197, 44, 356, 355],
    [2826, 1147, 50, 1, 5],
    [2813, 1100, 48, 345, 344],
    [2793, 1057, 47, 335, 350],
    [2763, 1025, 43, 317, 342],
    [2724, 1012, 41, 288, 331],
    [2685, 992, 43, 297, 9],
    [2637, 991, 48, 271, 334],
    [2588, 981, 50, 282, 11],
    [2540, 977, 48, 275, 353],
    [2493, 981, 47, 265, 350],
    [2450, 974, 43, 279, 14],
    [2401, 981, 49, 262, 343],
    [2354, 988, 47, 262, 0],
    [2319, 1023, 49, 225, 323],
    [2305, 1062, 41, 200, 335],
    [2293, 1104, 43, 196, 356],
    [2287, 1154, 50, 187, 351],
    [2279, 1206, 52, 189, 2],
    [2274, 1256, 50, 186, 357],
    [2273, 1303, 47, 181, 355],
    [2267, 1351, 48, 187, 6],
    [2265, 1396, 45, 183, 356],
    [2237, 1440, 52, 212, 29],
    [2202, 1486, 57, 217, 5],
    [2166, 1522, 50, 225, 8],
    [2122, 1530, 44, 260, 35],
    [2074, 1541, 49, 257, 357],
    [2020, 1544, 54, 267, 10],
    [1969, 1550, 51, 263, 356],
    [1914, 1554, 55, 266, 3],
    [1861, 1540, 54, 285, 19],
    [1816, 1517, 50, 297, 12],
    [1781, 1477, 53, 319, 22],
    [1776, 1429, 48, 354, 35],
    [1770, 1375, 54, 354, 0],
    [1767, 1318, 57, 357, 3],
    [1773, 1262, 56, 6, 9],
    [1768, 1206, 56, 355, 349],
    [1772, 1146, 60, 4, 9],
    [1780, 1090, 56, 8, 4],
    [1783, 1034, 56, 3, 355],
    [1807, 1010, 33, 45, 42],
    [1862, 1002, 55, 82, 37],
    [1919, 995, 57, 83, 1],
    [1975, 984, 57, 79, 356],
    [2032, 981, 57, 87, 8],
    [2084, 979, 52, 88, 1],
    [2136, 966, 53, 76, 348],
    [2171, 936, 46, 49, 333],
    [2183, 885, 52, 13, 324],
    [2184, 832, 53, 1, 348],
    [2195, 785, 48, 13, 12],
    [2193, 728, 57, 358, 345],
    [2185, 675, 53, 351, 353],
    [2177, 633, 42, 349, 358],
    [2135, 601, 52, 307, 318],
    [2091, 598, 44, 274, 327],
    [2036, 598, 55, 270, 356],
    [1999, 623, 44, 236, 326],
    [1974, 657, 42, 216, 340],
    [1957, 661, 17, 257, 41],
    [1913, 633, 52, 302, 45],
    [1864, 620, 50, 285, 343],
    [1816, 625, 48, 264, 339],
    [1755, 626, 61, 269, 5],
    [1700, 614, 56, 282, 13],
    [1643, 598, 59, 286, 4],
    [1591, 594, 52, 274, 348],
    [1548, 626, 53, 233, 319],
    [1541, 675, 49, 188, 315],
    [1533, 734, 59, 188, 0],
    [1537, 791, 57, 176, 348],
    [1550, 839, 49, 165, 349],
    [1574, 881, 48, 150, 345],
    [1620, 906, 52, 119, 329],
    [1664, 931, 50, 120, 1],
    [1709, 957, 51, 120, 0],
    [1758, 967, 50, 102, 342],
    [1811, 980, 54, 104, 2],
    [1866, 981, 55, 91, 347],
    [1919, 984, 53, 93, 2],
    [1970, 994, 51, 101, 8],
    [2011, 1016, 46, 118, 17],
    [2032, 1070, 57, 159, 41],
    [2029, 1125, 55, 183, 24],
    [2028, 1186, 61, 181, 358],
    [2020, 1246, 60, 188, 7],
    [2011, 1300, 54, 189, 1],
    [2014, 1356, 56, 177, 348],
    [2014, 1413, 57, 180, 3],
    [2029, 1464, 53, 164, 344],
    [2072, 1486, 48, 117, 313],
    [2117, 1501, 47, 108, 351],
    [2165, 1502, 48, 91, 343],
    [2220, 1497, 55, 85, 354],
    [2268, 1507, 49, 102, 17],
    [2321, 1504, 53, 87, 345],
    [2379, 1508, 58, 94, 7],
    [2433, 1510, 54, 92, 358],
    [2484, 1489, 55, 68, 336],
    [2516, 1452, 48, 41, 333],
    [2532, 1407, 47, 20, 339],
    [2534, 1356, 51, 2, 342],
    [2541, 1302, 54, 7, 5],
    [2546, 1243, 59, 5, 358],
    [2542, 1186, 57, 356, 351],
    [2548, 1128, 58, 6, 10],
    [2557, 1076, 52, 10, 4],
    [2579, 1026, 54, 24, 14],
    [2628, 1003, 54, 65, 41],
    [2681, 981, 57, 67, 2],
    [2735, 969, 55, 77, 10],
    [2787, 970, 52, 91, 14],
    [2828, 987, 44, 113, 22],
    [2845, 1041, 56, 163, 50],
    [2835, 1102, 61, 189, 26],
    [2835, 1168, 66, 180, 351],
    [2839, 1227, 59, 176, 356],
    [2839, 1284, 57, 180, 4],
    [2843, 1348, 64, 176, 356],
    [2850, 1410, 62, 174, 358],
    [2864, 1459, 50, 164, 350],
    [2901, 1502, 56, 139, 335],
    [2951, 1533, 58, 122, 343],
    [3002, 1552, 54, 110, 348],
    [3060, 1560, 58, 98, 348],
    [3120, 1571, 61, 100, 2],
    [3175, 1579, 55, 98, 358],
    [3234, 1577, 59, 88, 350],
    [3292, 1564, 59, 77, 349],
    [3338, 1538, 52, 61, 344],
    [3353, 1490, 50, 17, 316],
    [3357, 1434, 56, 4, 347],
    [3361, 1377, 57, 4, 0],
    [3355, 1319, 58, 354, 350],
    [3349, 1266, 53, 354, 0],
    [3346, 1213, 53, 357, 3],
    [3339, 1160, 53, 352, 355],
    [3331, 1101, 59, 352, 0],
    [3336, 1045, 56, 5, 13],
    [3352, 998, 49, 19, 14],
    [3389, 967, 48, 50, 31],
    [3439, 962, 50, 84, 34],
    [3486, 958, 47, 85, 1],
    [3537, 957, 51, 89, 4],
    [3589, 969, 53, 103, 14],
    [3644, 964, 55, 85, 342],
    [3697, 972, 53, 99, 14],
    [3737, 1005, 51, 130, 31],
    [3779, 1044, 57, 133, 3],
    [3799, 1098, 57, 160, 27],
    [3803, 1147, 49, 175, 15],
    [3806, 1200, 53, 177, 2],
    [3782, 1246, 51, 208, 31],
    [3745, 1273, 45, 234, 26],
    [3694, 1284, 52, 258, 24],
    [3645, 1278, 49, 277, 19],
    [3603, 1302, 48, 240, 323],
    [3561, 1332, 51, 234, 354],
    [3512, 1364, 58, 237, 3],
    [3467, 1375, 46, 256, 19],
    [3421, 1379, 46, 265, 9],
    [3382, 1412, 51, 230, 325],
    [3369, 1457, 46, 196, 326],
    [3380, 1510, 54, 168, 332],
    [3417, 1540, 47, 129, 321],
    [3467, 1563, 55, 115, 346],
    [3525, 1562, 58, 89, 334],
    [3576, 1540, 55, 67, 338],
    [3634, 1528, 59, 78, 11],
    [3691, 1513, 58, 75, 357],
    [3748, 1497, 59, 74, 359],
    [3809, 1489, 61, 83, 9],
    [3871, 1477, 63, 79, 356],
    [3932, 1469, 61, 83, 4],
    [3990, 1477, 58, 98, 15],
    [4039, 1501, 54, 116, 18],
    [4098, 1525, 63, 112, 356],
    [4159, 1540, 62, 104, 352],
    [4220, 1540, 61, 90, 346],
    [4274, 1520, 57, 70, 340],
    [4312, 1482, 53, 45, 335],
    [4338, 1432, 56, 27, 342],
    [4343, 1367, 65, 4, 337],
    [4344, 1304, 63, 1, 357],
    [4329, 1253, 53, 344, 343],
    [4309, 1243, 22, 297, 313],
    [4313, 1261, 18, 167, 230],
    [4318, 1267, 7, 140, 333],
    [4320, 1269, 2, 135, 355],
]


# x, y, 歩幅, 進行方向, 角度の変化量
CORRECT_TRAJECTORY_COORDINATES4: List[List[int]] = (
    [[x, 300, 60, 90, 0] for _, x in enumerate(range(350, 2650, 60))]
    + [[2650, 350, 0, 180, 90]]
    + [[2650, y, 60, 180, 0] for _, y in enumerate(range(350, 1100, 60))]
    + [[2650, 1100, 0, 270, 90]]
    + [[x, 1100, 60, 270, 0] for _, x in enumerate(range(2650, 350, -60))]
    + [[350, 1100, 0, 180, -90]]
    + [[350, y, 60, 180, 0] for _, y in enumerate(range(1100, 1500, 60))]
    + [[350, 1500, 0, 90, -90]]
    + [[x, 1500, 60, 90, 0] for _, x in enumerate(range(350, 2650, 60))]
    + [[2650, 1500, 0, 180, 90]]
    + [[2650, y, 60, 180, 0] for _, y in enumerate(range(1500, 2700, 60))]
    + [[2650, 2700, 0, 270, 90]]
    + [[x, 2700, 60, 270, 0] for _, x in enumerate(range(2650, 400, -60))]
)


# x, y, 歩幅, 進行方向, 角度の変化量
CORRECT_TRAJECTORY_COORDINATES5: List[List[int]] = (
    [[x, 620, 60, 90, 0] for _, x in enumerate(range(620, 2390, 60))]
    + [[2380, 620, 60, 180, 90]]
    + [[2380, y, 60, 180, 0] for _, y in enumerate(range(660, 2390, 60))]
    + [[2380, 2390, 60, 270, 90]]
    + [[x, 2390, 60, 270, 0] for _, x in enumerate(range(2390, 620, -60))]
)
