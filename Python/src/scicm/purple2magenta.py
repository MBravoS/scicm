
from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.12205587,0.01850877,0.18590411],
           [0.12659391,0.01974823,0.19081584],
           [0.13108308,0.0210641 ,0.19566539],
           [0.1355639 ,0.02239963,0.20050612],
           [0.1400436 ,0.02374326,0.20534739],
           [0.14452075,0.02509624,0.21018709],
           [0.14899967,0.02645047,0.21503077],
           [0.15348173,0.0278022 ,0.21988008],
           [0.15796612,0.02915132,0.22473381],
           [0.16245599,0.03049071,0.22959598],
           [0.16694765,0.03182546,0.23446162],
           [0.17144125,0.03315407,0.23933081],
           [0.1759447 ,0.03445969,0.24421393],
           [0.18044798,0.0357603 ,0.24909763],
           [0.18496157,0.03703325,0.25399571],
           [0.18947882,0.03829036,0.2588993 ],
           [0.19399994,0.03952982,0.26380862],
           [0.19853251,0.04072797,0.26873366],
           [0.20307085,0.04187196,0.27366684],
           [0.20761524,0.04297108,0.27860849],
           [0.21216639,0.04402425,0.2835595 ],
           [0.21672554,0.04502901,0.28852151],
           [0.22129439,0.04598176,0.29349673],
           [0.2258727 ,0.04688306,0.29848482],
           [0.23045907,0.04773613,0.30348391],
           [0.23505429,0.04853915,0.30849502],
           [0.23965891,0.04929062,0.31351889],
           [0.24427296,0.04999025,0.31855552],
           [0.24889675,0.05063693,0.32360532],
           [0.25353048,0.0512297 ,0.32866855],
           [0.25817435,0.05176753,0.33374549],
           [0.26282851,0.05224936,0.33883632],
           [0.26749311,0.05267403,0.34394124],
           [0.27217099,0.05303323,0.34906406],
           [0.27686029,0.05333059,0.3542023 ],
           [0.28156104,0.0535647 ,0.35935601],
           [0.28627251,0.05373627,0.3645242 ],
           [0.29099543,0.05384175,0.36970787],
           [0.29573004,0.05387885,0.37490734],
           [0.30047713,0.05384611,0.38011944],
           [0.30523358,0.05379346,0.38527603],
           [0.3100115 ,0.05368407,0.39039487],
           [0.31481229,0.0535128 ,0.39547687],
           [0.3196349 ,0.05328478,0.40051528],
           [0.3244791 ,0.05300306,0.40550418],
           [0.32934474,0.05267103,0.41043736],
           [0.33423086,0.0522949 ,0.41530753],
           [0.33913651,0.05188164,0.42010716],
           [0.34406046,0.05143969,0.42482831],
           [0.34900126,0.05097915,0.42946264],
           [0.35395707,0.05051208,0.43400149],
           [0.35892586,0.05005227,0.438436  ],
           [0.36390491,0.04961656,0.44275694],
           [0.36889208,0.04922102,0.44695568],
           [0.37388371,0.04888735,0.45102298],
           [0.37887604,0.04863835,0.45495015],
           [0.38386585,0.04849538,0.45872949],
           [0.38884827,0.04848499,0.46235344],
           [0.39381944,0.04862983,0.46581602],
           [0.39877456,0.04895416,0.4691122 ],
           [0.40370597,0.04950228,0.4722238 ],
           [0.408612  ,0.05027376,0.47516031],
           [0.41348957,0.05127569,0.47792527],
           [0.41833536,0.05251528,0.48052053],
           [0.42314636,0.05399509,0.48294958],
           [0.42792044,0.05571163,0.4852172 ],
           [0.43265567,0.05765785,0.48732959],
           [0.43735141,0.05982095,0.48929352],
           [0.44200663,0.06218733,0.49111713],
           [0.44662074,0.0647458 ,0.49280357],
           [0.45119536,0.06747118,0.49436569],
           [0.45573187,0.07034115,0.49581505],
           [0.46023147,0.07333733,0.49716041],
           [0.46469581,0.07644179,0.49841   ],
           [0.46912666,0.0796378 ,0.49957184],
           [0.47352581,0.08291017,0.50065371],
           [0.47789326,0.08625559,0.50165388],
           [0.48223257,0.08965271,0.50258594],
           [0.48654549,0.09309038,0.50345693],
           [0.49083389,0.09655863,0.50427338],
           [0.49510002,0.10004835,0.50504038],
           [0.49934598,0.10355178,0.50576272],
           [0.50357282,0.10706285,0.50644744],
           [0.50778274,0.11057651,0.50709628],
           [0.51197214,0.11410995,0.50769216],
           [0.51614784,0.11763614,0.5082602 ],
           [0.52031096,0.1211517 ,0.50880546],
           [0.5244633 ,0.12465346,0.50933039],
           [0.52860273,0.12815178,0.50982533],
           [0.53273051,0.13164611,0.51028853],
           [0.53685114,0.13512006,0.51073991],
           [0.54096554,0.13857225,0.51118316],
           [0.54506951,0.14202301,0.51159315],
           [0.5491678 ,0.14545662,0.51198892],
           [0.55326327,0.14886514,0.51238133],
           [0.5573527 ,0.15226239,0.51275476],
           [0.56143714,0.15564827,0.51310798],
           [0.56552089,0.1590074 ,0.51346477],
           [0.56960098,0.16235472,0.51380386],
           [0.57367832,0.165689  ,0.51412742],
           [0.57775737,0.16899582,0.51445807],
           [0.58183297,0.17229702,0.51476303],
           [0.58590933,0.17557809,0.51506645],
           [0.5899884 ,0.17883535,0.515374  ],
           [0.59406422,0.1820906 ,0.51565317],
           [0.598145  ,0.1853184 ,0.51594374],
           [0.60222569,0.18853718,0.51621775],
           [0.60630924,0.19173942,0.51648703],
           [0.61039697,0.19492143,0.51676015],
           [0.61448505,0.19809847,0.51701029],
           [0.61857985,0.2012491 ,0.5172783 ],
           [0.62267474,0.20439903,0.5175158 ],
           [0.62677674,0.20752532,0.51776668],
           [0.63088179,0.21064429,0.51799942],
           [0.63499301,0.21374444,0.51824013],
           [0.63911056,0.21682963,0.51847804],
           [0.64323189,0.21990371,0.51871478],
           [0.64736514,0.22295945,0.51893843],
           [0.65149545,0.2260128 ,0.51916806],
           [0.65564008,0.22904706,0.5193803 ],
           [0.65978124,0.23208081,0.51959841],
           [0.66393155,0.23510219,0.51980475],
           [0.66808686,0.23811634,0.52000313],
           [0.67224113,0.24112967,0.52020174],
           [0.676407  ,0.24413069,0.52038164],
           [0.68056624,0.24713756,0.52056798],
           [0.68473225,0.25013798,0.52074093],
           [0.68890387,0.25313368,0.52090128],
           [0.69306755,0.25613821,0.52106692],
           [0.6972389 ,0.25913728,0.52121476],
           [0.70140976,0.26213902,0.521356  ],
           [0.70557436,0.26514969,0.52149633],
           [0.70974345,0.26815928,0.52162108],
           [0.7139102 ,0.27117508,0.52173723],
           [0.71806763,0.27420405,0.52185339],
           [0.72222617,0.27723659,0.52195505],
           [0.72638448,0.28027456,0.52204214],
           [0.73052504,0.28333466,0.52213771],
           [0.73466304,0.28640338,0.52221835],
           [0.73879663,0.28948265,0.52228599],
           [0.74292114,0.29257696,0.52234668],
           [0.74702689,0.29569616,0.52240936],
           [0.75112311,0.2988316 ,0.52246185],
           [0.75520787,0.30198556,0.52250447],
           [0.75927884,0.30516037,0.52253921],
           [0.7633297 ,0.30836242,0.52257111],
           [0.76735614,0.31159541,0.5226062 ],
           [0.77136228,0.31485627,0.52263483],
           [0.7753451 ,0.31814764,0.5226604 ],
           [0.77930164,0.3214724 ,0.52268465],
           [0.78322869,0.32483358,0.52270955],
           [0.78712287,0.32823438,0.52273705],
           [0.79098051,0.33167799,0.52277015],
           [0.79479774,0.33516776,0.52281199],
           [0.79857048,0.33870721,0.52286558],
           [0.80229438,0.34230003,0.52293398],
           [0.80596487,0.3459497 ,0.52302222],
           [0.80957722,0.34965979,0.52313518],
           [0.81312652,0.35343385,0.5232783 ],
           [0.81660751,0.3572759 ,0.52345579],
           [0.82001526,0.36118865,0.52367644],
           [0.82334431,0.36517587,0.52394552],
           [0.82658982,0.36923974,0.52427276],
           [0.82974688,0.37338266,0.52466644],
           [0.83279774,0.37761724,0.52515309],
           [0.83574953,0.38193481,0.52572925],
           [0.83860013,0.3863343 ,0.52640415],
           [0.8413475 ,0.39081433,0.52718841],
           [0.84397635,0.39538382,0.52811137],
           [0.8464967 ,0.40003108,0.5291702 ],
           [0.84891442,0.40474797,0.53036824],
           [0.85122852,0.40953182,0.53171798],
           [0.853432  ,0.41438466,0.53323929],
           [0.85554528,0.41928767,0.53491575],
           [0.8575741 ,0.4242339 ,0.53674892],
           [0.8595177 ,0.42922168,0.5387473 ],
           [0.86138036,0.43424591,0.54091126],
           [0.86317835,0.43929306,0.54322477],
           [0.86491784,0.44435769,0.54568328],
           [0.86660366,0.44943585,0.54828111],
           [0.8682419 ,0.45452274,0.55101252],
           [0.86982972,0.45962033,0.5538797 ],
           [0.87137984,0.46471973,0.55686638],
           [0.87289614,0.46981873,0.55996488],
           [0.87438502,0.47491633,0.56314374],
           [0.87587254,0.48000079,0.56633064],
           [0.87735805,0.48507334,0.56952564],
           [0.87884157,0.49013464,0.57272879],
           [0.88032321,0.49518521,0.57594015],
           [0.88180335,0.50022537,0.57915978],
           [0.88328188,0.50525582,0.58238772],
           [0.88475912,0.51027687,0.58562405],
           [0.88623525,0.51528896,0.58886881],
           [0.88771022,0.52029266,0.59212206],
           [0.8891856 ,0.5252873 ,0.59538393],
           [0.89066019,0.53027432,0.59865441],
           [0.8921345 ,0.53525385,0.60193357],
           [0.89360822,0.54022662,0.60522145],
           [0.89508189,0.54519268,0.60851811],
           [0.89655535,0.55015262,0.61182363],
           [0.8980289 ,0.55510667,0.61513804],
           [0.89950334,0.5600547 ,0.61846145],
           [0.90097913,0.56499682,0.62179396],
           [0.90245559,0.56993395,0.62513556],
           [0.90393278,0.57486645,0.6284863 ],
           [0.90541056,0.57979483,0.63184625],
           [0.90688932,0.58471919,0.63521547],
           [0.90837102,0.58963858,0.63859413],
           [0.90985444,0.59455425,0.64198221],
           [0.91133906,0.59946689,0.64537976],
           [0.91282515,0.6043767 ,0.64878682],
           [0.91431368,0.60928337,0.65220353],
           [0.91580581,0.61418652,0.65562999],
           [0.91729977,0.61908763,0.65906617],
           [0.91879569,0.62398698,0.66251214],
           [0.92029512,0.62888388,0.66596805],
           [0.92179836,0.63377848,0.66943397],
           [0.92330391,0.63867207,0.67290987],
           [0.92481226,0.64356462,0.67639586],
           [0.92632624,0.64845471,0.67989214],
           [0.92784286,0.6533445 ,0.68339862],
           [0.92936231,0.65823416,0.6869154 ],
           [0.930888  ,0.66312191,0.69044271],
           [0.93241664,0.66801005,0.69398043],
           [0.93394987,0.67289789,0.69752873],
           [0.93548849,0.67778521,0.70108774],
           [0.93703027,0.68267366,0.70465738],
           [0.93857908,0.68756119,0.70823797],
           [0.94013166,0.69245002,0.71182938],
           [0.94169016,0.69733915,0.71543183],
           [0.94325402,0.7022292 ,0.71904534],
           [0.94482317,0.70712045,0.72267003],
           [0.94639873,0.71201254,0.726306  ],
           [0.94797985,0.7169062 ,0.72995331],
           [0.94956724,0.7218013 ,0.73361211],
           [0.95115828,0.72669955,0.73728227],
           [0.95275335,0.73160118,0.74096196],
           [0.9543592 ,0.73650279,0.74465073],
           [0.95596982,0.74140792,0.74834881],
           [0.95758753,0.74631553,0.75205614],
           [0.95921649,0.75122368,0.75577259],
           [0.96085204,0.75613512,0.75949836],
           [0.96249526,0.76104951,0.76323341],
           [0.96414706,0.76596663,0.76697772],
           [0.96580689,0.770887  ,0.77073132],
           [0.96747513,0.77581067,0.77449421],
           [0.96915005,0.78073879,0.77826644],
           [0.9708387 ,0.78566796,0.78204779],
           [0.97253085,0.79060368,0.78583855],
           [0.97423563,0.79554151,0.78963846],
           [0.97594704,0.80048475,0.79344766],
           [0.97766378,0.80543425,0.79726617],
           [0.97939138,0.81038748,0.8010938 ],
           [0.98112239,0.81534836,0.80493072],
           [0.9828509 ,0.82031998,0.80877703],
           [0.98452112,0.8253298 ,0.81263402]]
test_cm = ListedColormap(cm_data, name="purple2magenta")
