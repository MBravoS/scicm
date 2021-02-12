
from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.04927454,0.17179195,0.02191863],
           [0.0509296 ,0.17514533,0.02269142],
           [0.0526154 ,0.17848605,0.02351003],
           [0.05429253,0.18182106,0.02433881],
           [0.0559539 ,0.18515188,0.02517044],
           [0.05760145,0.18847849,0.02600601],
           [0.05923509,0.19180121,0.02684469],
           [0.06084916,0.19512128,0.02767989],
           [0.06244941,0.198438  ,0.0285166 ],
           [0.06403417,0.20175192,0.02935231],
           [0.06560276,0.20506341,0.03018543],
           [0.06715557,0.20837266,0.03101552],
           [0.06869355,0.21167972,0.03184281],
           [0.07021699,0.2149848 ,0.03266687],
           [0.07172459,0.21828831,0.03348539],
           [0.07321536,0.22159065,0.03429635],
           [0.07469475,0.22489108,0.03510546],
           [0.07615483,0.22819117,0.0359024 ],
           [0.07760497,0.2314895 ,0.03669779],
           [0.07903547,0.2347879 ,0.03747893],
           [0.08045459,0.23808516,0.03825532],
           [0.08185861,0.24138207,0.03902158],
           [0.08324668,0.24467895,0.03977584],
           [0.08462309,0.24797524,0.04052166],
           [0.0859848 ,0.2512716 ,0.0412401 ],
           [0.08732952,0.25456857,0.04193605],
           [0.08866175,0.25786554,0.04261528],
           [0.08998052,0.26116282,0.04327639],
           [0.09128121,0.26446082,0.04393264],
           [0.09255122,0.26776146,0.04457953],
           [0.09379031,0.27106489,0.04521723],
           [0.09499921,0.27437112,0.04584537],
           [0.0961776 ,0.27768029,0.04646412],
           [0.09732518,0.28099255,0.04707371],
           [0.09844153,0.28430804,0.04767435],
           [0.09952431,0.2876271 ,0.04826748],
           [0.10057515,0.29094965,0.04885203],
           [0.10159367,0.29427579,0.04942822],
           [0.10257942,0.29760566,0.04999623],
           [0.10353195,0.30093938,0.05055624],
           [0.10444961,0.30427719,0.05110919],
           [0.10533202,0.30761921,0.05165516],
           [0.10617969,0.31096542,0.05219373],
           [0.10699206,0.31431595,0.05272509],
           [0.10776855,0.31767089,0.05324942],
           [0.10850854,0.32103037,0.05376693],
           [0.10920908,0.32439473,0.05427918],
           [0.10987179,0.32776384,0.05478498],
           [0.11049596,0.3311378 ,0.05528453],
           [0.11108087,0.33451671,0.05577802],
           [0.11162574,0.33790067,0.05626562],
           [0.11212878,0.34128988,0.05674811],
           [0.11258862,0.34468448,0.05722596],
           [0.11300581,0.34808444,0.0576985 ],
           [0.11337943,0.35148983,0.05816593],
           [0.11370847,0.35490075,0.05862843],
           [0.1139919 ,0.3583173 ,0.05908618],
           [0.11422685,0.36173973,0.05954039],
           [0.1144131 ,0.36516806,0.05999071],
           [0.11455022,0.36860227,0.06043686],
           [0.11463692,0.37204247,0.06087904],
           [0.11467186,0.37548873,0.06131744],
           [0.1146536 ,0.37894115,0.06175223],
           [0.11457836,0.38240001,0.06218487],
           [0.11444626,0.38586524,0.06261455],
           [0.11425605,0.38933687,0.06304122],
           [0.11400593,0.39281498,0.06346508],
           [0.11369393,0.39629966,0.0638863 ],
           [0.11331804,0.39979097,0.06430511],
           [0.11287376,0.40328921,0.06472283],
           [0.11236025,0.4067943 ,0.06513884],
           [0.11177565,0.41030627,0.06555302],
           [0.11111721,0.41382519,0.06596553],
           [0.11038203,0.41735114,0.0663766 ],
           [0.10956693,0.42088419,0.06678641],
           [0.10866703,0.42442453,0.06719583],
           [0.10767833,0.42797226,0.0676052 ],
           [0.1065984 ,0.43152731,0.06801389],
           [0.10542286,0.43508975,0.06842212],
           [0.10414685,0.43865967,0.06883007],
           [0.10276505,0.44223712,0.06923793],
           [0.10127165,0.44582218,0.06964594],
           [0.09966086,0.4494149 ,0.07005219],
           [0.09798545,0.45301135,0.07043343],
           [0.09622974,0.45661267,0.0707814 ],
           [0.09439038,0.46021886,0.07109488],
           [0.09246299,0.46382995,0.07137225],
           [0.09045041,0.46744548,0.0716136 ],
           [0.08835595,0.47106494,0.07181875],
           [0.08616081,0.47468933,0.07198256],
           [0.08386019,0.47831862,0.07210348],
           [0.08146582,0.48195167,0.07218315],
           [0.0789666 ,0.48558887,0.07221704],
           [0.07634662,0.48923075,0.07220214],
           [0.07361614,0.49287629,0.07213762],
           [0.07076774,0.49652549,0.0720213 ],
           [0.06777585,0.50017922,0.07184648],
           [0.06467566,0.50383518,0.07161644],
           [0.06140891,0.50749573,0.07131962],
           [0.05802668,0.51115789,0.07096092],
           [0.05446131,0.51482413,0.07052676],
           [0.05077059,0.51849136,0.07002142],
           [0.04689553,0.52216137,0.0694322 ],
           [0.04284775,0.52583301,0.06875484],
           [0.0386421 ,0.52950489,0.06798581],
           [0.03443984,0.53317761,0.067113  ],
           [0.03036408,0.53685022,0.06612848],
           [0.02645446,0.54052179,0.06502124],
           [0.02278136,0.54419045,0.06378393],
           [0.01936956,0.54785587,0.06239993],
           [0.01627576,0.55151679,0.06085148],
           [0.01358711,0.55517103,0.0591237 ],
           [0.01139932,0.5588163 ,0.0571951 ],
           [0.00979496,0.56245079,0.05503819],
           [0.00888283,0.56607203,0.05262053],
           [0.00889592,0.56967395,0.04991703],
           [0.00993995,0.57325448,0.04687565],
           [0.01230926,0.57680611,0.04345759],
           [0.01628381,0.58032194,0.03960273],
           [0.02218895,0.58379405,0.03537963],
           [0.03091348,0.58719881,0.03098207],
           [0.04486849,0.59046487,0.02662506],
           [0.06566544,0.59340714,0.02440263],
           [0.08782874,0.59605128,0.02849708],
           [0.10603197,0.59867374,0.03665714],
           [0.12136632,0.60132144,0.04631962],
           [0.13482884,0.60399234,0.05576215],
           [0.14698863,0.60668143,0.06477874],
           [0.15820485,0.60938303,0.07339957],
           [0.16867161,0.6120967 ,0.08163604],
           [0.17854255,0.61482024,0.08954169],
           [0.18792247,0.61755257,0.0971576 ],
           [0.19688995,0.62029291,0.10451849],
           [0.20552346,0.62303836,0.11167758],
           [0.21384909,0.62579102,0.11863519],
           [0.22191551,0.62854918,0.12542626],
           [0.22975014,0.63131302,0.13206521],
           [0.23738622,0.63408124,0.13857687],
           [0.24483091,0.63685571,0.14495882],
           [0.25212049,0.63963366,0.1512431 ],
           [0.25926248,0.64241613,0.15743116],
           [0.2662661 ,0.64520372,0.16352728],
           [0.27314609,0.64799594,0.16954242],
           [0.27991525,0.6507923 ,0.17548675],
           [0.28658706,0.653592  ,0.18137167],
           [0.29316316,0.65639608,0.1871953 ],
           [0.29965184,0.65920436,0.19296376],
           [0.30607008,0.66201524,0.19868076],
           [0.31242777,0.66482839,0.20433843],
           [0.31872897,0.66764385,0.20994174],
           [0.32497727,0.67046171,0.21549505],
           [0.33117548,0.67328213,0.22100187],
           [0.33732682,0.67610518,0.22646592],
           [0.34343425,0.6789309 ,0.23189053],
           [0.34950018,0.68175942,0.23727849],
           [0.3555267 ,0.68459088,0.24263219],
           [0.36151651,0.68742528,0.24795448],
           [0.36747134,0.69026277,0.25324731],
           [0.37339308,0.69310345,0.25851269],
           [0.37928387,0.69594733,0.26375281],
           [0.38514482,0.69879464,0.26896892],
           [0.39097794,0.70164536,0.27416302],
           [0.39678464,0.7044996 ,0.27933653],
           [0.40256606,0.70735751,0.28449064],
           [0.408324  ,0.71021906,0.28962707],
           [0.41405887,0.71308455,0.29474631],
           [0.41977271,0.71595384,0.29985025],
           [0.42546593,0.7188272 ,0.30493934],
           [0.43114012,0.72170459,0.31001504],
           [0.43679581,0.72458621,0.31507789],
           [0.44243432,0.72747206,0.32012909],
           [0.44805608,0.73036233,0.32516907],
           [0.45366251,0.73325699,0.33019907],
           [0.45925374,0.73615628,0.33521928],
           [0.46483122,0.73906013,0.34023093],
           [0.47039503,0.74196879,0.34523415],
           [0.47594642,0.74488222,0.35023   ],
           [0.48148568,0.7478006 ,0.35521875],
           [0.48701359,0.75072398,0.36020108],
           [0.49253169,0.75365222,0.36517804],
           [0.49803959,0.75658566,0.37014946],
           [0.50353812,0.75952432,0.37511613],
           [0.50902755,0.76246836,0.38007827],
           [0.51450837,0.76541787,0.3850363 ],
           [0.51998133,0.76837288,0.38999084],
           [0.52544654,0.77133359,0.39494197],
           [0.53090467,0.77430001,0.39989025],
           [0.53635628,0.77727222,0.40483613],
           [0.54180144,0.78025041,0.40977965],
           [0.54724147,0.78323442,0.41472169],
           [0.55267693,0.78622428,0.41966268],
           [0.55810729,0.78922034,0.4246024 ],
           [0.56353283,0.79222273,0.42954103],
           [0.56895417,0.79523145,0.43447909],
           [0.57437167,0.7982466 ,0.43941686],
           [0.57978536,0.80126836,0.44435432],
           [0.58519576,0.80429677,0.4492919 ],
           [0.59060432,0.80733158,0.45423045],
           [0.59601081,0.81037304,0.45916993],
           [0.60141481,0.81342146,0.46411009],
           [0.60681672,0.8164769 ,0.46905126],
           [0.61221691,0.81953941,0.47399371],
           [0.61761563,0.82260911,0.47893764],
           [0.62301317,0.82568608,0.48388324],
           [0.62841128,0.82876996,0.48883142],
           [0.63380871,0.83186129,0.49378164],
           [0.63920572,0.83496017,0.49873408],
           [0.64460256,0.83806669,0.50368891],
           [0.64999944,0.84118094,0.50864629],
           [0.65539667,0.84430301,0.51360641],
           [0.66079601,0.8474325 ,0.51857021],
           [0.66619611,0.85056999,0.52353704],
           [0.67159717,0.85371559,0.52850705],
           [0.6769994 ,0.85686938,0.5334804 ],
           [0.68240303,0.86003147,0.53845721],
           [0.68780934,0.86320159,0.54343822],
           [0.69322295,0.86637828,0.54842759],
           [0.69864088,0.86956258,0.55342473],
           [0.70406204,0.87275503,0.55842897],
           [0.70948587,0.87595596,0.56343974],
           [0.71491232,0.87916556,0.56845691],
           [0.72033816,0.88238516,0.57347748],
           [0.72576623,0.88561392,0.57850393],
           [0.73119794,0.88885148,0.58353744],
           [0.73663257,0.89209828,0.5885773 ],
           [0.74207117,0.89535408,0.59362436],
           [0.74751336,0.89861918,0.59867822],
           [0.75295892,0.90189384,0.60373859],
           [0.75840887,0.90517783,0.60880632],
           [0.7638625 ,0.90847158,0.61388069],
           [0.76932013,0.91177513,0.61896191],
           [0.77478273,0.91508828,0.62405079],
           [0.7802495 ,0.91841148,0.62914652],
           [0.7857211 ,0.92174466,0.63424964],
           [0.79119808,0.92508776,0.63936057],
           [0.79668121,0.92844063,0.64447994],
           [0.80217034,0.93180351,0.64960755],
           [0.80766495,0.93517673,0.65474285],
           [0.8131622 ,0.93856159,0.65988311],
           [0.81866701,0.94195632,0.66503283],
           [0.82418012,0.94536077,0.67019262],
           [0.82969924,0.94877602,0.67536027],
           [0.83522217,0.95220309,0.68053367],
           [0.84075764,0.95563867,0.68572087],
           [0.84629415,0.95908751,0.69091108],
           [0.85184461,0.9625446 ,0.69611627],
           [0.85739587,0.96601538,0.70132407],
           [0.86295874,0.96949566,0.70654452],
           [0.86853067,0.97298661,0.71177516],
           [0.87411107,0.97648864,0.71701535],
           [0.87969965,0.98000202,0.72226476],
           [0.88530121,0.98352494,0.72752781],
           [0.89091116,0.98705943,0.73280012],
           [0.89653667,0.99060269,0.73808835],
           [0.90218241,0.99415289,0.74339681],
           [0.90789699,0.99768979,0.74877117]]
test_cm = ListedColormap(cm_data, name="green")
