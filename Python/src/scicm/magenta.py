
from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.21234385,0.05935309,0.13016209],
           [0.21711452,0.06076701,0.13372493],
           [0.22185817,0.06219269,0.13727239],
           [0.22660002,0.06359695,0.14081699],
           [0.23134496,0.0649737 ,0.14436127],
           [0.23609315,0.06632326,0.14790547],
           [0.24084575,0.06764451,0.15145028],
           [0.24560388,0.06893629,0.1549964 ],
           [0.25036851,0.0701976 ,0.15854443],
           [0.25513922,0.07142935,0.1620943 ],
           [0.25991546,0.07263267,0.16564585],
           [0.26469972,0.0738042 ,0.16920045],
           [0.26949118,0.07494537,0.17275779],
           [0.27428981,0.07605641,0.17631798],
           [0.27909653,0.07713614,0.17988158],
           [0.28391164,0.07818422,0.18344884],
           [0.28873522,0.07920064,0.18701993],
           [0.29356762,0.08018492,0.1905951 ],
           [0.29840702,0.0811393 ,0.19417611],
           [0.30324735,0.08206825,0.19778082],
           [0.30809011,0.08296828,0.20141532],
           [0.31293514,0.08383994,0.20507868],
           [0.31778285,0.0846829 ,0.20876996],
           [0.32263317,0.08549746,0.21248867],
           [0.32748721,0.08628131,0.2162373 ],
           [0.33234451,0.08703575,0.22001342],
           [0.33720535,0.0877605 ,0.22381636],
           [0.34207063,0.08845338,0.22764872],
           [0.34694   ,0.08911544,0.23150824],
           [0.35181366,0.08974644,0.23539424],
           [0.3566927 ,0.09034356,0.23931002],
           [0.3615764 ,0.09090884,0.24325154],
           [0.36646575,0.09143966,0.24722169],
           [0.37136058,0.09193648,0.25121876],
           [0.37626123,0.09239833,0.25524315],
           [0.38116812,0.09282399,0.25929543],
           [0.38608122,0.09321347,0.26337439],
           [0.39100116,0.09356474,0.26748164],
           [0.39592778,0.09387812,0.27161553],
           [0.4008617 ,0.09415153,0.27577752],
           [0.40580294,0.0943846 ,0.27996674],
           [0.41075171,0.09457631,0.28418324],
           [0.41570846,0.09472478,0.28842805],
           [0.42067289,0.09483059,0.29269884],
           [0.42564637,0.09488889,0.29699987],
           [0.43062773,0.0949025 ,0.30132659],
           [0.43561821,0.09486699,0.30568222],
           [0.44061776,0.09478161,0.31006593],
           [0.44562599,0.09464664,0.3144759 ],
           [0.45064453,0.09445586,0.31891671],
           [0.45567218,0.09421176,0.32338432],
           [0.46070964,0.09391127,0.32787927],
           [0.46575768,0.09354973,0.33240506],
           [0.47081589,0.09312747,0.33695835],
           [0.4758842 ,0.09264282,0.34153905],
           [0.48096393,0.09208915,0.34615085],
           [0.48605459,0.09146623,0.3507912 ],
           [0.49115591,0.09077249,0.35545942],
           [0.49626885,0.09000208,0.36015738],
           [0.50139385,0.0891502 ,0.36488626],
           [0.5065303 ,0.08821601,0.36964376],
           [0.51167991,0.08719041,0.37443185],
           [0.51685543,0.08605912,0.37920199],
           [0.52206884,0.08479101,0.38394042],
           [0.5273238 ,0.08336523,0.38865197],
           [0.53262028,0.08177792,0.39332496],
           [0.5379582 ,0.08002609,0.39794489],
           [0.54334341,0.07807414,0.40252173],
           [0.54877062,0.0759443 ,0.40701864],
           [0.55424729,0.07358671,0.41145232],
           [0.55976832,0.0710218 ,0.41578453],
           [0.56533824,0.06821189,0.42001645],
           [0.57095576,0.06514779,0.42412956],
           [0.57661615,0.06184255,0.42809032],
           [0.58231757,0.05828586,0.43188299],
           [0.58805506,0.05448489,0.43548396],
           [0.59382026,0.05046863,0.43886532],
           [0.59960187,0.04628862,0.44199997],
           [0.60538565,0.04202507,0.44486382],
           [0.61115524,0.03779805,0.44743813],
           [0.61689217,0.03395708,0.4497121 ],
           [0.62257795,0.03067472,0.45168191],
           [0.6281961 ,0.02805979,0.45335381],
           [0.6337357 ,0.02617187,0.45475175],
           [0.63918916,0.02505185,0.45589976],
           [0.644553  ,0.02471239,0.45682558],
           [0.64982757,0.02514112,0.45755796],
           [0.65501603,0.02630758,0.45812505],
           [0.6601208 ,0.02820201,0.45853937],
           [0.66515064,0.03075156,0.45883274],
           [0.67011187,0.03390582,0.45902856],
           [0.67500937,0.03764187,0.45913233],
           [0.67984893,0.04188107,0.45915714],
           [0.68463831,0.04632131,0.45912371],
           [0.68937938,0.05091931,0.45902581],
           [0.69408002,0.05559119,0.45888414],
           [0.69874316,0.06031007,0.45870124],
           [0.70337155,0.06505927,0.45847416],
           [0.70797118,0.06979347,0.45822166],
           [0.71254635,0.07450713,0.4579291 ],
           [0.71706714,0.07932273,0.4576107 ],
           [0.72153813,0.08421825,0.45725435],
           [0.72595208,0.08921295,0.45686162],
           [0.73028721,0.09437045,0.45644691],
           [0.73455434,0.09963957,0.45599953],
           [0.73872678,0.10509109,0.4555394 ],
           [0.74281093,0.11068554,0.45506289],
           [0.74677981,0.11648354,0.45459233],
           [0.750641  ,0.12243952,0.45412743],
           [0.75436805,0.12860324,0.45369437],
           [0.75796183,0.13494467,0.45330417],
           [0.76141844,0.14144832,0.45297359],
           [0.764721  ,0.14813012,0.45273043],
           [0.76787409,0.15495332,0.45259034],
           [0.77088305,0.16188456,0.45256827],
           [0.77374867,0.16890461,0.45268224],
           [0.776469  ,0.17600263,0.45295096],
           [0.77906599,0.18312395,0.45337281],
           [0.78154684,0.19024986,0.45395369],
           [0.78391094,0.19737891,0.45470248],
           [0.78618712,0.20445957,0.45560369],
           [0.78836641,0.21151122,0.45666615],
           [0.7904763 ,0.21849194,0.45787041],
           [0.79250751,0.22542321,0.45922243],
           [0.79448586,0.23227083,0.46070009],
           [0.79639867,0.23906157,0.46230978],
           [0.79826553,0.24577245,0.46403497],
           [0.80009174,0.25240376,0.46586615],
           [0.8018704 ,0.25897192,0.46780517],
           [0.80361173,0.26546876,0.46984134],
           [0.80532172,0.27189271,0.47196583],
           [0.80700202,0.2782477 ,0.47417365],
           [0.80865436,0.28453705,0.47646017],
           [0.81027946,0.290765  ,0.47882177],
           [0.81187512,0.29693891,0.48125643],
           [0.81344896,0.30305381,0.48375667],
           [0.81500202,0.3091128 ,0.48631889],
           [0.81653439,0.31511986,0.48893962],
           [0.81804758,0.32107685,0.49161587],
           [0.81954369,0.32698471,0.49434488],
           [0.8210217 ,0.33284804,0.49712371],
           [0.8224848 ,0.33866611,0.49995004],
           [0.82393195,0.3444431 ,0.50282134],
           [0.82536218,0.35018244,0.50573741],
           [0.82677601,0.35588589,0.50869644],
           [0.82817574,0.36155358,0.51169475],
           [0.829563  ,0.36718595,0.51473046],
           [0.83093844,0.3727845 ,0.51780179],
           [0.83229878,0.37835641,0.52089615],
           [0.83365271,0.3838967 ,0.52399824],
           [0.83500044,0.38940683,0.52710812],
           [0.83634241,0.39488787,0.53022617],
           [0.83767853,0.40034149,0.5333521 ],
           [0.83900901,0.4057689 ,0.53648594],
           [0.84033403,0.41117128,0.53962776],
           [0.84165375,0.41654975,0.54277759],
           [0.84296829,0.42190541,0.54593548],
           [0.84427802,0.42723911,0.54910154],
           [0.84558332,0.43255156,0.55227603],
           [0.8468841 ,0.43784396,0.55545872],
           [0.84818045,0.44311726,0.55864966],
           [0.84947265,0.44837218,0.56184889],
           [0.8507609 ,0.45360947,0.56505646],
           [0.85204538,0.45882989,0.56827242],
           [0.85332626,0.46403415,0.57149686],
           [0.85460402,0.46922265,0.57473006],
           [0.85587858,0.4743963 ,0.57797179],
           [0.85715014,0.47955571,0.58122209],
           [0.85841881,0.48470153,0.58448102],
           [0.85968484,0.48983428,0.58774862],
           [0.86094844,0.49495448,0.59102494],
           [0.8622098 ,0.50006266,0.59431002],
           [0.86346928,0.50515916,0.59760416],
           [0.86472697,0.51024458,0.60090722],
           [0.86598301,0.51531942,0.60421918],
           [0.86723757,0.52038414,0.60754011],
           [0.86849076,0.52543925,0.61087004],
           [0.86974289,0.53048506,0.61420902],
           [0.87099416,0.53552198,0.6175571 ],
           [0.87224476,0.54055041,0.62091437],
           [0.87349505,0.54557055,0.62428108],
           [0.87474508,0.55058294,0.62765704],
           [0.87599504,0.5555879 ,0.63104229],
           [0.87724503,0.56058587,0.63443689],
           [0.87849533,0.5655771 ,0.63784088],
           [0.87974616,0.5705619 ,0.64125431],
           [0.88099768,0.57554061,0.64467724],
           [0.8822501 ,0.58051352,0.64810973],
           [0.88350392,0.58548071,0.65155205],
           [0.88475909,0.59044264,0.65500402],
           [0.88601571,0.59539968,0.65846567],
           [0.88727409,0.600352  ,0.66193707],
           [0.88853446,0.60529987,0.66541826],
           [0.88979693,0.6102436 ,0.66890929],
           [0.89106176,0.6151834 ,0.67241021],
           [0.89232922,0.62011947,0.67592108],
           [0.89359961,0.62505198,0.67944208],
           [0.89487308,0.6299812 ,0.68297324],
           [0.89614982,0.63490738,0.6865145 ],
           [0.89743002,0.63983076,0.6900659 ],
           [0.89871383,0.64475158,0.69362751],
           [0.90000158,0.64966999,0.69719937],
           [0.90129347,0.6545862 ,0.70078153],
           [0.90258963,0.65950046,0.70437406],
           [0.90389041,0.6644129 ,0.707977  ],
           [0.90519614,0.66932362,0.71159051],
           [0.90650693,0.67423288,0.71521466],
           [0.90782303,0.67914087,0.71884937],
           [0.90914468,0.68404775,0.72249471],
           [0.91047197,0.68895378,0.72615072],
           [0.91180528,0.69385905,0.72981747],
           [0.91314484,0.69876371,0.73349499],
           [0.9144908 ,0.703668  ,0.73718336],
           [0.91584353,0.708572  ,0.74088261],
           [0.91720322,0.71347589,0.74459281],
           [0.91857024,0.71837974,0.74831415],
           [0.91994483,0.72328371,0.75204661],
           [0.92132713,0.72818803,0.75579016],
           [0.92271739,0.73309283,0.75954488],
           [0.92411597,0.73799821,0.7633108 ],
           [0.9255218 ,0.74290498,0.76708806],
           [0.9269282 ,0.7478169 ,0.77087634],
           [0.92834466,0.75272945,0.77467415],
           [0.92976994,0.75764353,0.77848164],
           [0.93120665,0.76255809,0.78229875],
           [0.93265266,0.76747449,0.78612565],
           [0.9341107 ,0.77239161,0.78996227],
           [0.93557918,0.77731051,0.79380876],
           [0.9370593 ,0.78223087,0.79766513],
           [0.93855175,0.78715262,0.80153141],
           [0.94005638,0.79207609,0.80540766],
           [0.94157215,0.79700205,0.80929402],
           [0.94310058,0.80193001,0.81319045],
           [0.94464119,0.80686047,0.81709704],
           [0.94619401,0.81179367,0.82101384],
           [0.94775897,0.81672987,0.82494091],
           [0.94934423,0.82166554,0.82887782],
           [0.95094139,0.82660484,0.8328251 ],
           [0.95255012,0.8315482 ,0.8367828 ],
           [0.95417355,0.8364944 ,0.84075075],
           [0.95581674,0.84144138,0.84472871],
           [0.95746989,0.84639388,0.84871721],
           [0.95914367,0.85134731,0.85271566],
           [0.9608297 ,0.85630571,0.85672451],
           [0.96253557,0.86126593,0.86074329],
           [0.96425264,0.86623209,0.86477242],
           [0.96599181,0.87119958,0.86881123],
           [0.96774797,0.87617096,0.87285988],
           [0.96952014,0.88114692,0.87691829],
           [0.97130778,0.88612795,0.88098633],
           [0.97311137,0.89111409,0.88506373],
           [0.97493795,0.89610256,0.88914989],
           [0.9767757 ,0.90109875,0.89324511],
           [0.97862306,0.90610358,0.89734907],
           [0.98048222,0.91111633,0.90146125],
           [0.98226601,0.91617432,0.90558493]]
test_cm = ListedColormap(cm_data, name="magenta")
