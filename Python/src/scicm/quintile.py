
from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.12792763,0.02229164,0.15670404],
           [0.13158307,0.02446874,0.1617488 ],
           [0.1352098 ,0.02675112,0.16673528],
           [0.13881477,0.02912008,0.17170859],
           [0.14240048,0.03157059,0.17668011],
           [0.14596831,0.03410096,0.18165317],
           [0.14951897,0.03671167,0.18662656],
           [0.15305388,0.03940033,0.19160476],
           [0.15657359,0.04211834,0.19658597],
           [0.160079  ,0.0447967 ,0.20157168],
           [0.16357078,0.04744725,0.20656166],
           [0.16705032,0.05006901,0.21156152],
           [0.17051781,0.05266522,0.21656815],
           [0.17397335,0.05523912,0.22157803],
           [0.17741917,0.05778594,0.22660367],
           [0.18085384,0.06031399,0.23163065],
           [0.18427999,0.06281678,0.23667469],
           [0.18769642,0.06530123,0.24172368],
           [0.19110428,0.06776583,0.24678276],
           [0.19450468,0.07020915,0.25185688],
           [0.19789718,0.07263493,0.25693993],
           [0.20128232,0.07504337,0.26203312],
           [0.20466097,0.07743348,0.26714008],
           [0.20803364,0.07980544,0.27226192],
           [0.2114003 ,0.08216115,0.27739596],
           [0.21476138,0.08450077,0.28254309],
           [0.21811722,0.08682485,0.28770335],
           [0.22146825,0.08913339,0.2928779 ],
           [0.22481486,0.09142658,0.29806734],
           [0.22815726,0.09370509,0.3032713 ],
           [0.2314959 ,0.09596877,0.30849103],
           [0.23483108,0.09821791,0.31372682],
           [0.23816306,0.10045279,0.31897892],
           [0.24149217,0.10267357,0.32424779],
           [0.24482684,0.1048771 ,0.32952055],
           [0.24817204,0.10705456,0.33481193],
           [0.25152875,0.10920556,0.34012238],
           [0.25489786,0.11132982,0.34545191],
           [0.25828032,0.11342706,0.35080049],
           [0.26167705,0.11549692,0.35616814],
           [0.26508903,0.11753901,0.36155481],
           [0.26851736,0.11955252,0.3669612 ],
           [0.27196311,0.12153731,0.37238603],
           [0.27542773,0.12349292,0.37782778],
           [0.27891193,0.12541838,0.38328857],
           [0.28241648,0.12731377,0.38876689],
           [0.28594278,0.12917773,0.3942639 ],
           [0.28949157,0.1310104 ,0.39977785],
           [0.29306415,0.13281064,0.40530919],
           [0.29666153,0.13457804,0.41085701],
           [0.3002858 ,0.13631217,0.41641724],
           [0.09959375,0.26472179,0.07610441],
           [0.10125382,0.26794378,0.07757651],
           [0.10290595,0.27116579,0.07904176],
           [0.10455384,0.27438726,0.08050496],
           [0.10619097,0.27760949,0.08195951],
           [0.10781943,0.28083224,0.08340802],
           [0.10943838,0.28405579,0.08484942],
           [0.11104709,0.28728042,0.0862828 ],
           [0.11264827,0.29050573,0.08771152],
           [0.11423917,0.29373238,0.08913215],
           [0.11582122,0.2969602 ,0.09054653],
           [0.11739485,0.30018925,0.09195511],
           [0.11895827,0.30341997,0.09335578],
           [0.12051436,0.30665193,0.09475201],
           [0.12206092,0.30988566,0.09614119],
           [0.12359808,0.31312125,0.09752344],
           [0.12512802,0.31635837,0.09890149],
           [0.12664816,0.31959764,0.10027217],
           [0.12815988,0.32283889,0.10163721],
           [0.12966365,0.32608212,0.10299722],
           [0.13115777,0.32932777,0.10435013],
           [0.1326443 ,0.33257552,0.10569851],
           [0.13412237,0.33582566,0.10704127],
           [0.13559071,0.33907849,0.10837699],
           [0.13705238,0.34233355,0.10970933],
           [0.13850488,0.34559138,0.11103537],
           [0.13994794,0.34885213,0.11235479],
           [0.14138469,0.3521153 ,0.11367141],
           [0.14281191,0.35538157,0.1149814 ],
           [0.14423018,0.35865091,0.11628547],
           [0.14564173,0.361923  ,0.11758643],
           [0.14704393,0.3651984 ,0.11888107],
           [0.14843729,0.36847709,0.1201701 ],
           [0.14982385,0.37175878,0.12145605],
           [0.15120114,0.375044  ,0.12273593],
           [0.15256943,0.37833277,0.12401023],
           [0.15393101,0.38162474,0.1252817 ],
           [0.15528315,0.3849205 ,0.12654714],
           [0.15662625,0.38822003,0.12780708],
           [0.1579629 ,0.39152294,0.12906464],
           [0.15929009,0.39482984,0.13031636],
           [0.16060798,0.39814077,0.13156244],
           [0.16191947,0.40145528,0.13280645],
           [0.16322163,0.40477396,0.13404497],
           [0.16451432,0.4080969 ,0.13527792],
           [0.16579982,0.41142375,0.13650808],
           [0.16707681,0.41475483,0.1377339 ],
           [0.1683443 ,0.41809036,0.13895435],
           [0.16960364,0.42143017,0.14017108],
           [0.17085516,0.42477426,0.14138461],
           [0.17209701,0.42812303,0.14259286],
           [0.04786536,0.37272284,0.75590611],
           [0.05002666,0.37680764,0.75569989],
           [0.05272689,0.38085822,0.75545101],
           [0.05585464,0.38487268,0.75519081],
           [0.05937034,0.38885523,0.75490344],
           [0.06318373,0.39280505,0.75461167],
           [0.06724377,0.3967233 ,0.75431971],
           [0.07152003,0.40061316,0.75401674],
           [0.07594886,0.40447357,0.75372483],
           [0.08049913,0.40830635,0.7534437 ],
           [0.08516   ,0.41211397,0.75316319],
           [0.08989877,0.41589648,0.75289445],
           [0.09469236,0.41965489,0.75264168],
           [0.09952679,0.42339045,0.75240509],
           [0.10439077,0.42710413,0.75218613],
           [0.10927483,0.43079707,0.75198493],
           [0.11417121,0.43447189,0.75179332],
           [0.11890151,0.43813634,0.75166239],
           [0.1234645 ,0.44179339,0.75158755],
           [0.12787263,0.44544394,0.75156766],
           [0.13213476,0.44908888,0.75160247],
           [0.13625834,0.45272901,0.75169192],
           [0.14024964,0.45636514,0.75183592],
           [0.1441139 ,0.45999811,0.7520342 ],
           [0.14785561,0.46362861,0.75228704],
           [0.15147236,0.46725758,0.75259732],
           [0.15496737,0.47088572,0.75296522],
           [0.15834873,0.47451362,0.75338813],
           [0.16161836,0.47814199,0.75386602],
           [0.16477791,0.48177146,0.75439928],
           [0.16782722,0.48540272,0.75498875],
           [0.17075511,0.48903679,0.75564109],
           [0.17357492,0.49267393,0.75634975],
           [0.17628675,0.49631477,0.75711499],
           [0.17889051,0.49995988,0.75793727],
           [0.18137346,0.50361026,0.75882373],
           [0.18374272,0.50726622,0.75977065],
           [0.18600147,0.51092824,0.760776  ],
           [0.18814881,0.51459676,0.76184056],
           [0.19016475,0.51827306,0.76297479],
           [0.19206564,0.52195705,0.76416913],
           [0.19385029,0.52564909,0.7654246 ],
           [0.19550324,0.52935028,0.76674846],
           [0.19702803,0.53306087,0.76813829],
           [0.19842979,0.53678093,0.76959114],
           [0.19969313,0.54051156,0.77111364],
           [0.2008182 ,0.54425297,0.77270541],
           [0.20181143,0.54800519,0.77436191],
           [0.2026542 ,0.55176928,0.7760917 ],
           [0.20335051,0.55554528,0.77789143],
           [0.20390501,0.55933312,0.7797578 ],
           [0.20429096,0.56313426,0.78170227],
           [0.5985492 ,0.51600768,0.11771216],
           [0.60161878,0.51927631,0.1180623 ],
           [0.60469201,0.52255133,0.11840346],
           [0.60776897,0.52583276,0.11873598],
           [0.61084966,0.52912066,0.11906   ],
           [0.61393413,0.53241506,0.11937645],
           [0.61702243,0.53571605,0.11968387],
           [0.62011461,0.53902368,0.11998217],
           [0.62321071,0.542338  ,0.12027146],
           [0.62631075,0.54565907,0.12055128],
           [0.62941479,0.54898693,0.12082256],
           [0.63252287,0.5523216 ,0.12108594],
           [0.63563501,0.55566319,0.12133969],
           [0.63875129,0.55901173,0.12158407],
           [0.64187172,0.56236729,0.12181896],
           [0.64499636,0.56572992,0.12204416],
           [0.64812524,0.56909966,0.12225976],
           [0.65125839,0.57247656,0.12246703],
           [0.65439586,0.57586069,0.12266478],
           [0.65753771,0.57925209,0.12285278],
           [0.66068395,0.58265084,0.1230308 ],
           [0.66383463,0.58605699,0.12319854],
           [0.6669898 ,0.58947059,0.12335627],
           [0.6701495 ,0.5928917 ,0.1235039 ],
           [0.67331375,0.59632036,0.12364197],
           [0.67648259,0.59975662,0.12377037],
           [0.67965607,0.60320056,0.12388839],
           [0.68283425,0.60665223,0.12399594],
           [0.68601714,0.61011169,0.12409266],
           [0.68920478,0.61357901,0.12417851],
           [0.69239723,0.61705423,0.12425355],
           [0.69559452,0.62053741,0.12431771],
           [0.69879668,0.6240286 ,0.1243709 ],
           [0.70200375,0.62752786,0.12441413],
           [0.70521576,0.63103525,0.12444604],
           [0.70843278,0.63455084,0.12446659],
           [0.71165483,0.63807467,0.12447566],
           [0.71488195,0.64160682,0.12447312],
           [0.71811417,0.64514735,0.12445851],
           [0.72135153,0.64869632,0.12443198],
           [0.72459408,0.65225378,0.12439346],
           [0.72784186,0.65581979,0.1243428 ],
           [0.7310949 ,0.65939441,0.12427983],
           [0.73435324,0.6629777 ,0.12420487],
           [0.73761691,0.66656971,0.12411799],
           [0.74088595,0.67017053,0.1240183 ],
           [0.7441604 ,0.6737802 ,0.1239056 ],
           [0.74744031,0.6773988 ,0.12377981],
           [0.7507257 ,0.68102639,0.12364074],
           [0.75401661,0.68466303,0.12348815],
           [0.75731309,0.68830878,0.12332197],
           [0.67200956,0.69385356,0.68644358],
           [0.67527584,0.69735628,0.68969976],
           [0.67854922,0.70086741,0.69296284],
           [0.68182979,0.70438699,0.69623288],
           [0.68511765,0.70791504,0.69950997],
           [0.68841279,0.71145166,0.70279411],
           [0.69171528,0.7149969 ,0.70608534],
           [0.69502516,0.71855083,0.70938371],
           [0.69834248,0.7221135 ,0.71268927],
           [0.70166731,0.72568497,0.71600205],
           [0.70499969,0.72926531,0.71932211],
           [0.70833985,0.73285449,0.72264964],
           [0.71168782,0.7364526 ,0.72598466],
           [0.71504351,0.74005974,0.7293271 ],
           [0.71840694,0.74367601,0.73267699],
           [0.72177821,0.74730145,0.73603439],
           [0.72515778,0.75093592,0.73939972],
           [0.72854527,0.7545797 ,0.74277264],
           [0.73194071,0.75823287,0.74615319],
           [0.73534451,0.7618953 ,0.74954172],
           [0.73875652,0.76556718,0.75293811],
           [0.74217668,0.76924862,0.75634229],
           [0.74560543,0.77293949,0.75975468],
           [0.74904248,0.77664004,0.76317499],
           [0.75248803,0.78035025,0.76660342],
           [0.75594226,0.78407014,0.77004013],
           [0.75940497,0.7877999 ,0.77348494],
           [0.7628765 ,0.79153945,0.77693816],
           [0.76635671,0.79528896,0.78039967],
           [0.76984569,0.79904847,0.78386953],
           [0.77334376,0.80281795,0.78734806],
           [0.77685063,0.80659761,0.79083499],
           [0.78036647,0.81038748,0.79433046],
           [0.78389165,0.81418747,0.79783483],
           [0.7874259 ,0.81799781,0.80134784],
           [0.79096931,0.82181856,0.80486959],
           [0.79452203,0.82564975,0.80840021],
           [0.79808409,0.82949146,0.81193972],
           [0.80165559,0.83334374,0.81548824],
           [0.80523651,0.8372067 ,0.81904573],
           [0.80882688,0.84108044,0.82261223],
           [0.81242722,0.84496481,0.82618821],
           [0.81603679,0.84886026,0.829773  ],
           [0.81965648,0.85276647,0.83336743],
           [0.8232858 ,0.85668377,0.83697104],
           [0.82692478,0.86061227,0.84058387],
           [0.83057374,0.86455191,0.8442062 ],
           [0.83423244,0.8685029 ,0.84783784],
           [0.83790061,0.8724655 ,0.85147852],
           [0.84157833,0.87643975,0.85512833],
           [0.84526012,0.88042833,0.85878224]]
test_cm = ListedColormap(cm_data, name="quintile")
