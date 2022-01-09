#Cálculo de humedad relativa partiendo de la temperatura del aire
#y del punto de rocío, usando tablas I y II.
#Fuente tablas SMN: www.youtube.com/watch?v=FdKqiPnqDCg&ab_channel=DtoCapacitacionSMN

#Versión funcional.
#Faltan cargar valores de temperatura inferiores a 10 grados y todas las negativas.
#Revisar índices de tablas
#Verificar funcionalidad de rangos de humedad mínimos
#Correción de impresión doble de valores a tabla II
#Sebastián Damiano 09/01/2022 03.45 hs.

#Importo la librería MATH PARA poder separar un float en entero y decimal
import math

#TABLA I - Índice para las decenas
cero = [000,858,729,653,600,558,524,495,471,449]
diez = [429,411,395,380,366,353,341,330,319,310]
veinte = [300,291,282,274,266,253,251,244,237,231]
treinta = [224,218,212,207,201,196,190,185,180,175]
cuarenta = [171,166,162,157,153,149,145,141,137,133]
cincuenta = [129,125,122,118,115,111,108,105,101,98]
sesenta = [95,92,89,86,83,80,77,74,72,69]
setenta = [68,64,61,59,56,54,51,49,46,44]
ochenta = [42,39,37,35,32,30,28,26,24,22]
noventa = [20,18,16,14,12,10,8,6,4,2]

"""
cero = [0,1,2,3,4,5,6,7,8,9]
diez = [10,11,12,13,14,15,16,17,18,19]
veinte = [20,21,22,23,24,25,26,27,28,29]
treinta = [30,31,32,33,34,35,36,37,38,39]
cuarenta = [40,41,42,43,44,45,46,47,48,49]
cincuenta = [50,51,52,53,54,55,56,57,58,59]
sesenta = [60,61,62,63,64,65,66,67,68,69]
setenta = [70,71,72,73,74,75,76,77,78,79]
ochenta = [80,81,82,83,84,85,86,87,88,89]
noventa = [90,91,92,93,94,95,96,97,98,99]
"""

# TABLA II
m49 = [1389,1391,1393,1396,1398,1400,1402,1404,1406,1408]
m48 = [1368,1370,1372,1374,1377,1379,1381,1386,1388,1390]
m47 = [1347,1349,1351,1354,1356,1358,1360,1362,1364,1366]
m46 = [1327,1329,1331,1333,1335,1337,1339,1341,1343,1345]
m45 = [1306,1308,1310,1313,1315,1317,1319,1321,1323,1325]
m44 = [1286,1288,1290,1292,1294,1296,1298,1300,1302,1304]
m43 = [1266,1268,1270,1272,1274,1276,1278,1280,1282,1284]
m42 = [1246,1248,1250,1252,1254,1256,1258,1260,1262,1264]
m41 = [1227,1229,1231,1233,1235,1236,1238,1240,1242,1244]
m40 = [1207,1209,1211,1213,1215,1217,1219,1221,1223,1225]
m39 = [1188,1190,1192,1194,1196,1198,1200,1201,1203,1205]
m38 = [1169,1171,1173,1175,1177,1179,1180,1182,1184,1186]
m37 = [1150,1152,1154,1156,1158,1160,1161,1163,1165,1167]
m36 = [1131,1133,1135,1137,1139,1141,1143,1144,1148,1148]
m35 = [1113,1115,1117,1118,1120,1122,1124,1126,1128,1130]
m34 = [1095,1096,1098,1100,1102,1104,1106,1107,1109,1111]
m33 = [1076,1078,1080,1082,1084,1085,1087,1089,1091,1093]
m32 = [1058,1060,1062,1064,1066,1067,1069,1071,1073,1075]
m31 = [1041,1042,1044,1046,1048,1049,1051,1053,1055,1057]
m30 = [1023,1025,1026,1028,1030,1032,1033,1035,1037,1039]
m29 = [1005,1007,1009,1011,1012,1014,1016,1018,1019,1021]
m28 = [988,990,992,993,995,997,998,1000,1002,1004]
m27 = [971,973,974,976,978,979,981,983,985,986]
m26 = [954,956,957,959,961,962,964,966,967,969]
m25 = [937,939,940,942,944,945,947,949,950,952]
m24 = [920,922,924,925,927,929,930,932,934,935]
m23 = [904,905,907,909,910,912,914,915,917,919]
m22 = [887,889,891,892,894,895,897,899,900,902]
m21 = [871,873,874,876,877,879,881,882,884,885]
m20 = [855,850,858,860,861,863,864,866,868,869]
m19 = [839,840,842,844,845,847,848,850,852,853]
m18 = [823,825,826,828,829,831,832,834,836,837]
m17 = [807,809,810,812,814,815,817,818,820,821]
m16 = [792,793,795,796,798,799,801,803,804,806]
m15 = [776,778,779,781,782,784,786,787,789,790]
m14 = [761,763,764,766,767,769,770,772,773,775]
m13 = [746,747,749,750,752,753,755,756,758,759]
m12 = [731,732,734,735,737,738,749,741,743,744]
m11 = [716,717,718,719,721,722,724,725,727,728]
m10 = [701,703,704,705,707,708,710,711,713,714]
m9 = [686,688,689,691,692,694,695,697,698,700]
m8 = [672,673,675,676,678,679,681,682,683,685]
m7 = [657,659,660,662,663,665,666,668,669,670]
m6 = [643,645,646,647,648,650,651,653,654,658]
m5 = [629,630,632,633,635,636,637,639,640,642]
m4 = [615,617,618,619,621,622,623,625,626,628]
m3 = [601,602,604,605,607,608,609,611,612,614]
m2 = [587,589,590,591,593,594,595,597,598,600]
m1 = [573,575,576,578,579,580,582,583,584,586]
m0 = [560,561,563,564,565,567,568,569,571,572]

t0  = [560,559,557,556,554,553,552,550,549,548]
t1 = [546,545,544,542,541,540,538,537,536,534]
t2 = [533,532,530,529,528,526,525,524,522,521]
t3 = [520,518,517,516,514,513,512,511,509,508]
t4 = [507,505,504,503,501,500,499,497,496,495]
t5 = [494,492,491,490,488,487,486,484,483,482]
t6 = [480,479,478,477,475,474,473,472,470,469]
t7 = [468,466,465,464,463,461,460,459,458,456]
t8 = [455,454,452,451,450,449,447,446,445,444]
t9 = [442,441,440,439,437,436,435,434,432,431]
t10 = [430,429,427,426,425,424,422,421,420,419]
t11 = [417,416,415,414,412,411,410,409,408,406]
t12 = [405,404,403,401,400,399,398,396,395,394]
t13 = [393,392,390,389,388,387,386,384,383,382]
t14 = [381,379,378,377,376,375,373,372,371,370]
t15 = [369,367,366,365,364,363,361,360,359,358]
t16 = [357,356,354,353,352,351,350,348,347,346]
t17 = [345,344,342,341,340,339,338,337,335,334]
t18 = [333,332,331,330,328,327,326,325,324,323]
t19 = [322,321,320,319,317,316,314,313,312,311]
t20 = [310,309,307,306,305,304,303,302,301,299]
t21 = [298,297,296,295,294,293,291,290,289,288]
t22 = [287,286,285,284,282,281,280,279,278,277]
t23 = [276,274,273,272,271,270,269,268,267,265]
t24 = [264,263,262,261,260,259,258,257,255,254]
t25 = [253,252,251,250,249,248,247,245,244,243]
t26 = [242,241,240,239,238,237,236,234,233,232]
t27 = [231,230,229,228,227,226,225,224,222,221]
t28 = [220,219,218,217,216,215,214,213,212,211]
t29 = [209,208,207,206,205,204,203,202,201,200]
t30 = [199,198,197,196,194,193,192,191,190,189]
t31 = [188,187,186,185,184,183,182,181,180,179]
t32 = [177,176,175,174,173,172,171,170,169,168]
t33 = [167,166,165,164,163,162,161,160,159,158]
t34 = [157,156,155,153,152,151,150,149,148,147]
t35 = [146,145,144,143,142,141,140,139,138,137]
t36 = [136,135,134,133,132,131,130,129,128,127]
t37 = [126,125,124,123,122,121,120,119,118,117]
t38 = [116,115,114,113,112,111,110,109,108,107]
t39 = [106,105,104,103,102,101,100,99,98,97]
t40 = [96,95,94,93,92,91,90,89,88,87]

def calcular_temperatura():
    
    if entero == 10:
        print("el valor a tabla II es: ", t10[xdecimal])
        temp_fix = t10[xdecimal]
        return temp_fix
    elif entero == 11:
        print("el valor a tabla II es: ", t11[xdecimal])
        temp_fix = t11[xdecimal]
        return temp_fix
    elif entero == 12:
        print("el valor a tabla II es: ", t12[xdecimal])
        temp_fix = t12[xdecimal]
        return temp_fix
    elif entero == 13:
        print("el valor a tabla II es: ", t13[xdecimal])
        temp_fix = t13[xdecimal]
        return temp_fix
    elif entero == 14:
        print("el valor a tabla II es: ", t14[xdecimal])
        temp_fix = t14[xdecimal]
        return temp_fix
    elif entero == 15:
        print("el valor a tabla II es: ", t15[xdecimal])
        temp_fix = t15[xdecimal]
        return temp_fix
    elif entero == 16:
        print("el valor a tabla II es: ", t16[xdecimal])
        temp_fix = t16[xdecimal]
        return temp_fix
    elif entero == 17:
        print("el valor a tabla II es: ", t17[xdecimal])
        temp_fix = t17[xdecimal]
        return temp_fix
    elif entero == 18:
        print("el valor a tabla II es: ", t18[xdecimal])
        temp_fix = t18[xdecimal]
        return temp_fix
    elif entero == 19:
        print("el valor a tabla II es: ", t19[xdecimal])
        temp_fix = t19[xdecimal]
        return temp_fix
    elif entero == 20:
        print("el valor a tabla II es: ", t20[xdecimal])
        temp_fix = t20[xdecimal]
        return temp_fix
    elif entero == 21:
        print("el valor a tabla II es: ", t21[xdecimal])
        temp_fix = t21[xdecimal]
        return temp_fix
    if entero == 22:
        print("el valor a tabla II es: ", t22[xdecimal])
        temp_fix = t22[xdecimal]
        return temp_fix
    elif entero == 23:
        print("el valor a tabla II es: ", t23[xdecimal])
        temp_fix = t23[xdecimal]
        return temp_fix
    elif entero == 24:
        print("el valor a tabla II es: ", t24[xdecimal])
        temp_fix = t24[xdecimal]
        return temp_fix
    elif entero == 25:
        print("el valor a tabla II es: ", t25[xdecimal])
        temp_fix = t25[xdecimal]
        return temp_fix
    elif entero == 26:
        print("el valor a tabla II es: ", t26[xdecimal])
        temp_fix = t26[xdecimal]
        return temp_fix
    elif entero == 27:
        print("el valor a tabla II es: ", t27[xdecimal])
        temp_fix = t27[xdecimal]
        return temp_fix
    elif entero == 28:
        print("el valor a tabla II es: ", t28[xdecimal])
        temp_fix = t28[xdecimal]
        return temp_fix
    elif entero == 29:
        print("el valor a tabla II es: ", t29[xdecimal])
        temp_fix = t29[xdecimal]
        return temp_fix
    elif entero == 30:
        print("el valor a tabla II es: ", t30[xdecimal])
        temp_fix = t30[xdecimal]
        return temp_fix
    elif entero == 31:
        print("el valor a tabla II es: ", t31[xdecimal])
        temp_fix = t31[xdecimal]
        return temp_fix
    elif entero == 32:
        print("el valor a tabla II es: ", t32[xdecimal])
        temp_fix = t32[xdecimal]
        return temp_fix
    elif entero == 33:
        print("el valor a tabla II es: ", t33[xdecimal])
        temp_fix = t33[xdecimal]
        return temp_fix
# ------------------------------------------------------------------------
def humedad_relativa():
    if resta == 2 or resta == 3:
        print("La humedad relativa es del 99%")
    elif resta == 4 or resta == 5:
        print("La humedad relativa es del 98%")
    elif resta == 6 or resta == 7:
        print("La humedad relativa es del 97%")
    elif resta == 8 or resta == 9:
        print("La humedad relativa es del 96%")    
    elif resta == 10 or resta == 11:
        print("La humedad relativa es del 95%")
    elif resta == 12 or resta == 13:
        print("La humedad relativa es del 94%")    
    elif resta == 14 or resta == 15:
        print("La humedad relativa es del 93%")
    elif resta == 16 or resta == 17:
        print("La humedad relativa es del 92%")    
    elif resta == 18 or resta == 19:
        print("La humedad relativa es del 91%")
    elif resta == 20 or resta == 21:
        print("La humedad relativa es del 90%")
    elif resta == 22 or resta ==23:
        print("La humedad relativa es del 89%")
    elif resta == 24 or resta ==25:
        print("La humedad relativa es del 88%")
    elif resta == 26 or resta ==27:
        print("La humedad relativa es del 87%")
    elif resta == 28 or resta ==29:
        print("La humedad relativa es del 66%")    
    elif resta == 30 or resta ==31:
        print("La humedad relativa es del 85%")
    elif resta == 32 or resta ==33:
        print("La humedad relativa es del 84%")    
    elif resta == 34 or resta ==35 or resta ==36:
        print("La humedad relativa es del 83%")
    elif resta == 37 or resta ==38:
        print("La humedad relativa es del 82%")    
    elif resta == 39 or resta ==40 or resta ==41:
        print("La humedad relativa es del 81%")
    elif resta == 42:
        print("La humedad relativa es del 80%")
    elif resta == 43 or resta ==44:
        print("La humedad relativa es del 79%")
    elif resta == 45 or resta ==46 or resta ==47:
        print("La humedad relativa es del 78%")
    elif resta == 48 or resta ==49 or resta ==50:
        print("La humedad relativa es del 77%")
    elif resta == 51 or resta == 52 or resta == 53:
        print("La humedad relativa es del 76%")    
    elif resta == 54 or resta == 55:
        print("La humedad relativa es del 75%")
    elif resta == 56 or resta == 57 or resta == 58:
        print("La humedad relativa es del 74%")    
    elif resta == 59 or resta == 60:
        print("La humedad relativa es del 73%")
    elif resta == 61 or resta == 62 or resta == 63:
        print("La humedad relativa es del 72%")    
    elif resta == 64 or resta == 65 or resta == 66 or resta == 67:
        print("La humedad relativa es del 71%")
    elif resta == 68:
        print("La humedad relativa es del 70%")
    elif resta == 69 or resta == 70 or resta == 71:
        print("La humedad relativa es del 69%")
    elif resta == 72 or resta == 73:
        print("La humedad relativa es del 68%")
    elif resta == 74 or resta == 75 or resta == 76:
        print("La humedad relativa es del 67%")
    elif resta == 77 or resta == 78 or resta == 79:
        print("La humedad relativa es del 66%")    
    elif resta == 80 or resta == 81 or resta == 82:
        print("La humedad relativa es del 65%")
    elif resta == 83 or resta == 84 or resta == 85:
        print("La humedad relativa es del 64%")    
    elif resta == 86 or resta == 87 or resta == 88:
        print("La humedad relativa es del 63%")
    elif resta == 89 or resta == 90 or resta == 91:
        print("La humedad relativa es del 62%")    
    elif resta == 92 or resta == 93 or resta == 94:
        print("La humedad relativa es del 61%")
    elif resta == 95 or resta == 96 or resta == 97:
        print("La humedad relativa es del 60%")
    elif resta == 98 or resta == 99 or resta == 100:
        print("La humedad relativa es del 59%")
    elif resta == 101 or resta == 101 or resta == 101 or resta == 103 or resta == 104:
        print("La humedad relativa es del 58%")
    elif resta == 105 or resta == 106 or resta == 107:
        print("La humedad relativa es del 57%")
    elif resta == 108 or resta == 109 or resta == 110:
        print("La humedad relativa es del 56%")    
    elif resta == 111 or resta == 112 or resta == 113 or resta == 114:
        print("La humedad relativa es del 55%")
    elif resta == 115 or resta == 116 or resta == 117 or resta == 118:
        print("La humedad relativa es del 54%")    
    elif resta == 118 or resta == 119 or resta == 120 or resta == 121:
        print("La humedad relativa es del 53%")
    elif resta == 122 or resta == 123 or resta == 124:
        print("La humedad relativa es del 52%")    
    elif resta == 125 or resta == 126 or resta == 127 or resta == 128:
        print("La humedad relativa es del 51%")
    elif resta == 129 or resta == 130 or resta == 131 or resta == 132:
        print("La humedad relativa es del 50%")
    elif resta == 133 or resta == 134 or resta == 135 or resta == 136:
        print("La humedad relativa es del 49%")
    elif resta == 137 or resta == 138 or resta == 139 or resta == 140:
        print("La humedad relativa es del 48%")
    elif resta == 141 or resta == 142 or resta == 143 or resta == 144:
        print("La humedad relativa es del 47%")
    elif resta == 145 or resta == 146 or resta == 147 or resta == 148:
        print("La humedad relativa es del 46%")    
    elif resta == 149 or resta == 150 or resta == 151 or resta == 152:
        print("La humedad relativa es del 45%")
    elif resta == 153 or resta == 154 or resta == 155 or resta == 156:
        print("La humedad relativa es del 44%")    
    elif resta == 157 or resta == 158 or resta == 159 or resta == 161:
        print("La humedad relativa es del 43%")
    elif resta == 162 or resta == 163 or resta == 164 or resta == 165:
        print("La humedad relativa es del 42%")    
    elif resta == 166 or resta == 167 or resta == 168 or resta == 169 or resta == 170:
        print("La humedad relativa es del 41%")
    elif resta == 171 or resta == 172 or resta == 173 or resta == 174:
        print("La humedad relativa es del 40%")
    elif resta == 175 or resta == 176 or resta == 177 or resta == 178 or resta == 179:
        print("La humedad relativa es del 39%")
    elif resta == 180 or resta == 181 or resta == 182 or resta == 183 or resta == 184:
        print("La humedad relativa es del 38%")
    elif resta == 185 or resta == 186 or resta == 187 or resta == 188 or resta == 189:
        print("La humedad relativa es del 37%")
    elif resta == 190 or resta == 191 or resta == 192 or resta == 193 or resta == 194 or resta == 195:
        print("La humedad relativa es del 36%")    
    elif resta == 196 or resta == 197 or resta == 198 or resta == 199 or resta == 200:
        print("La humedad relativa es del 35%")
    elif resta == 201 or resta == 202 or resta == 203 or resta == 204 or resta == 205 or resta == 206:
        print("La humedad relativa es del 34%")    
    elif resta == 207 or resta == 208 or resta == 209 or resta == 210 or resta == 211:
        print("La humedad relativa es del 33%")
    elif resta == 212 or resta == 213 or resta == 214 or resta == 215 or resta == 216 or resta == 217:
        print("La humedad relativa es del 32%")    
    elif resta == 218 or resta == 219 or resta == 220 or resta == 221 or resta == 222 or resta == 223:
        print("La humedad relativa es del 31%")
    elif resta == 224 or resta == 225 or resta == 226 or resta == 227 or resta == 228 or resta == 229 or resta == 230:
        print("La humedad relativa es del 30%")
    elif resta == 231 or resta == 232 or resta == 233 or resta == 234 or resta == 235 or resta == 236:
        print("La humedad relativa es del 29%")
    elif resta == 237 or resta == 238 or resta == 239 or resta == 240 or resta == 241 or resta == 242 or resta == 243:
        print("La humedad relativa es del 28%")
    elif resta == 244 or resta == 245 or resta == 246 or resta == 247 or resta == 248 or resta == 249 or resta == 250:
        print("La humedad relativa es del 27%")
    elif resta == 251 or resta == 252:
        print("La humedad relativa es del 26%")    
    elif resta == 253 or resta == 254 or resta == 255 or resta == 256 or resta == 257 or resta == 258 or resta == 259 or resta == 260 or resta == 261 or resta == 262 or resta == 263 or resta == 264 or resta == 265:
        print("La humedad relativa es del 25%")
    elif resta == 266 or resta <= 273:
        print("La humedad relativa es del 24%")    
    elif resta == 274 or resta <= 281:
        print("La humedad relativa es del 23%")
    elif resta == 282 or resta <= 290:
        print("La humedad relativa es del 22%")    
    elif resta == 291 or resta <=299:
        print("La humedad relativa es del 21%")
    elif resta == 300 or resta <= 309:
        print("La humedad relativa es del 20%")
    elif resta == 310 or resta <= 318:
        print("La humedad relativa es del 19%")
    elif resta == 319 or resta <= 329:
        print("La humedad relativa es del 18%")
    elif resta == 330 or resta <= 340:
        print("La humedad relativa es del 17%")
    elif resta == 341 or resta <= 352:
        print("La humedad relativa es del 16%")    
    elif resta == 353 or resta <= 365:
        print("La humedad relativa es del 15%")
    elif resta == 366 or resta <= 379:
        print("La humedad relativa es del 14%")    
    elif resta == 380 or resta <= 394:
        print("La humedad relativa es del 13%")
    elif resta == 395 or resta <= 410:
        print("La humedad relativa es del 12%")    
    elif resta == 411 or resta <= 428:
        print("La humedad relativa es del 11%")
    elif resta == 429 or resta <= 448:
        print("La humedad relativa es del 10%")
    elif resta == 449 or resta <= 470:
        print("La humedad relativa es del 0.9%")
    elif resta == 471 or resta <= 494:
        print("La humedad relativa es del 0.8%")
    elif resta == 495 or resta <= 523:
        print("La humedad relativa es del 0.7%")
    elif resta == 524 or resta <= 557:
        print("La humedad relativa es del 0.6%")    
    elif resta == 558 or resta <= 599:
        print("La humedad relativa es del 0.5%")
    elif resta == 600 or resta <= 652:
        print("La humedad relativa es del 0.4%")    
    elif resta == 653 or resta <= 728:
        print("La humedad relativa es del 0.3%")
    elif resta == 729 or resta <= 857:
        print("La humedad relativa es del 0.2%")    
    elif resta == 858:
        print("La humedad relativa es del 0.1%")
    elif resta == none:
        print("La humedad relativa es del ---%")
    else:
        pass

temperatura = float(input("Ingrese temperatura del aire, con decimales: "))
     
#Se toma el primer dato y se separa la parte entera de la decimal
print("La temperatura ingresada: ", temperatura)
decimal, entero = math.modf(temperatura)

print("Valor entero a tabla II: ", entero)
print("Valor decimal a tabla II: ", decimal)

#multiplico por 10 para hacer entero el valor decimal y entrar a la tabla
xdecimal = int(decimal *10)

#llamo a la función
calcular_temperatura()

#Vuelvo de la función y asigno el valor devuelto a primer_valor de tabla
primer_valor = calcular_temperatura()

#print("Primer valor:", calcular_temperatura())
#print(primer_valor)

temp_rocio = float(input("Ingrese temperatura del punto de rocío, con decimales: "))

print("El punto de rocío ingresado: ", temp_rocio)
decimal, entero = math.modf(temp_rocio)

print("Valor entero a tabla II: ", entero)
print("Valor decimal a tabla II: ", decimal)

xdecimal = int(decimal *10)

calcular_temperatura()

segundo_valor = calcular_temperatura()

resta = segundo_valor - primer_valor

print(">>>>>> Valor a ingresar a tabla I: ", resta)

#Llamo a la función para acceder al valor de la humedad mediante el valor de la resta de temp. de rocío y temp. de termómetro seco.
humedad_relativa()
