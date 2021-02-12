
from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.00873788,0.09620843,0.00483465],
           [0.00993292,0.09973443,0.00557508],
           [0.01121021,0.10323553,0.00637176],
           [0.01254413,0.10671898,0.00720983],
           [0.0139285 ,0.11018701,0.00808562],
           [0.01536573,0.11363982,0.00900058],
           [0.01685371,0.11707859,0.00995343],
           [0.01839315,0.12050379,0.01094457],
           [0.01997986,0.12391689,0.0119714 ],
           [0.02161573,0.12731803,0.01303507],
           [0.02330001,0.1307079 ,0.01413505],
           [0.02503401,0.13408676,0.01527216],
           [0.02681119,0.13745624,0.01644222],
           [0.0286372 ,0.14081577,0.01764876],
           [0.03051093,0.14416596,0.01889108],
           [0.03243097,0.14750746,0.02016823],
           [0.03439485,0.15084104,0.02147858],
           [0.03640287,0.15416699,0.02282227],
           [0.03845609,0.15748547,0.02419997],
           [0.04055174,0.16079694,0.02561103],
           [0.04262257,0.16410177,0.02705521],
           [0.04467403,0.16740028,0.02853225],
           [0.04670701,0.1706928 ,0.03004196],
           [0.04872233,0.17397963,0.0315841 ],
           [0.05071991,0.1772612 ,0.03315784],
           [0.05269871,0.18053808,0.03476151],
           [0.05466124,0.18381023,0.03639629],
           [0.05660898,0.18707777,0.0380627 ],
           [0.05854227,0.19034099,0.03976039],
           [0.0604614 ,0.19360017,0.04146394],
           [0.06236787,0.19685537,0.04314853],
           [0.06425656,0.20010774,0.04481783],
           [0.06613217,0.20335679,0.04647591],
           [0.06799539,0.20660269,0.04812335],
           [0.06984786,0.20984542,0.04976158],
           [0.07168731,0.21308561,0.05138861],
           [0.07351072,0.21632405,0.05300176],
           [0.07532474,0.21955982,0.05460685],
           [0.0771298 ,0.22279309,0.05620426],
           [0.07891964,0.22602515,0.05778847],
           [0.08069785,0.22925561,0.05936263],
           [0.08246797,0.23248405,0.06092984],
           [0.08422702,0.2357112 ,0.06248749],
           [0.08597246,0.23893768,0.06403333],
           [0.08771071,0.24216259,0.06557299],
           [0.08943897,0.24538658,0.06710402],
           [0.09115348,0.24861048,0.06862312],
           [0.0928622 ,0.25183309,0.07013726],
           [0.09455964,0.25505554,0.07164162],
           [0.0962457 ,0.25827798,0.07313613],
           [0.09792723,0.26149941,0.07462679],
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
           [0.10252479,0.3017172 ,0.72849187],
           [0.09800498,0.30543407,0.73332409],
           [0.09307268,0.30927926,0.7377108 ],
           [0.08777819,0.3132469 ,0.7416195 ],
           [0.08223719,0.31733283,0.74498971],
           [0.07659552,0.32151901,0.74781398],
           [0.07101805,0.32578035,0.75012131],
           [0.06569275,0.33009643,0.75193268],
           [0.06076092,0.3344378 ,0.75333659],
           [0.05636458,0.33878765,0.75438331],
           [0.05261344,0.3431309 ,0.75513331],
           [0.04958463,0.34745435,0.75565143],
           [0.0473318 ,0.35175141,0.75598057],
           [0.04588667,0.3560169 ,0.75615937],
           [0.04524985,0.36024755,0.75622068],
           [0.04539295,0.36444184,0.75619051],
           [0.0462977 ,0.36860113,0.75607351],
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
           [0.20452449,0.56694799,0.78371556],
           [0.20459773,0.57077474,0.78579993],
           [0.20449161,0.57461554,0.78796222],
           [0.20422185,0.57846953,0.79019344],
           [0.20376555,0.58233784,0.79250176],
           [0.20312412,0.58622028,0.79488413],
           [0.20230048,0.59011656,0.79733685],
           [0.20126192,0.59402814,0.79987117],
           [0.20002889,0.59795375,0.80247527],
           [0.19857893,0.60189422,0.80515523],
           [0.19690245,0.60584966,0.8079113 ],
           [0.19500582,0.60981938,0.81073691],
           [0.19285012,0.61380478,0.81364287],
           [0.19044855,0.61780469,0.81661916],
           [0.18779366,0.62181947,0.8196591 ],
           [0.18520013,0.62583603,0.82263323],
           [0.18270384,0.62985313,0.82553088],
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
           [0.76061518,0.6919637 ,0.123142  ],
           [0.7639229 ,0.69562787,0.12294806],
           [0.76723629,0.69930134,0.12273993],
           [0.7705554 ,0.70298418,0.12251739],
           [0.77388026,0.70667645,0.12228022],
           [0.7772109 ,0.71037823,0.12202824],
           [0.78054737,0.71408958,0.12176127],
           [0.78388969,0.71781055,0.12147906],
           [0.78723792,0.72154123,0.12118138],
           [0.79059207,0.72528168,0.12086795],
           [0.7939522 ,0.72903196,0.12053853],
           [0.79731833,0.73279215,0.12019285],
           [0.80069051,0.73656231,0.1198307 ],
           [0.80406876,0.7403425 ,0.11945187],
           [0.80745313,0.74413281,0.11905614],
           [0.81084365,0.7479333 ,0.11864283],
           [0.81424035,0.75174405,0.11821178],
           [0.81764327,0.75556512,0.1177626 ],
           [0.82105246,0.75939659,0.11729506],
           [0.82446708,0.76323916,0.11679231],
           [0.82788926,0.76709175,0.11627029],
           [0.83131894,0.7709545 ,0.11572595],
           [0.83475615,0.7748275 ,0.11515815],
           [0.83820101,0.77871079,0.11456734],
           [0.84165344,0.78260452,0.11395047],
           [0.84511356,0.78650871,0.11330811],
           [0.84858132,0.79042352,0.1126372 ],
           [0.85205683,0.79434897,0.11193801],
           [0.85553998,0.79828527,0.11120631],
           [0.85903151,0.80223197,0.11045538],
           [0.86253108,0.80618943,0.10967659],
           [0.8660384 ,0.810158  ,0.10886101],
           [0.86955347,0.81413779,0.10800635],
           [0.8730776 ,0.81812793,0.10713926],
           [0.87660923,0.8221297 ,0.10622281],
           [0.88014929,0.82614254,0.1052751 ],
           [0.88369776,0.83016656,0.1042933 ],
           [0.88725444,0.83420205,0.10326989],
           [0.89081947,0.83824901,0.10220545],
           [0.89439337,0.84230719,0.10110929],
           [0.8979754 ,0.84637724,0.09996073],
           [0.90156586,0.85045907,0.09876335],
           [0.90516506,0.85455256,0.0975217 ],
           [0.90877302,0.85865784,0.09623244],
           [0.91238981,0.86277497,0.09489379],
           [0.91601491,0.86690445,0.09348783],
           [0.91964875,0.8710461 ,0.09202129],
           [0.923291  ,0.87520028,0.09047998],
           [0.92694098,0.87936761,0.08883925],
           [0.93059887,0.88354808,0.08709612],
           [0.93425416,0.88774947,0.08492999]]
test_cm = ListedColormap(cm_data, name="tercile")
