#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../../../dspplot/dspplot'))
sys.path.append(os.path.abspath(__file__ + '/../../../dspplot/dspplot'))
import dspplotting as dspplot

data = [
1.3218606489504897e-29,
6.0563710738903851e-28,
1.384560472321597e-26,
2.107631811466765e-25,
2.4054024507072286e-24,
2.1973202632045742e-23,
1.6749834222518031e-22,
1.0968253179127396e-21,
6.3035302739305299e-21,
3.2324543218154427e-20,
1.4986765527625694e-19,
6.3502318371304947e-19,
2.4812990309737065e-18,
9.0091257245218453e-18,
3.0594174785359719e-17,
9.7726195815204429e-17,
2.9509169014258683e-16,
8.4602012715795116e-16,
2.3119222808667908e-15,
6.0428932699561741e-15,
1.5154833448673883e-14,
3.6569028454616558e-14,
8.5120965207073379e-14,
1.9156810771209162e-13,
4.1772082204045625e-13,
8.842158807180344e-13,
1.820128193066413e-12,
3.6493551738237089e-12,
7.1374520580054411e-12,
1.3635616834225261e-11,
2.5477493998484414e-11,
4.661153885793174e-11,
8.3589561356623273e-11,
1.470840669004887e-10,
2.5417710668285447e-10,
4.3175619281963056e-10,
7.2147373081826998e-10,
1.1868812662318302e-09,
1.9235449843745794e-09,
3.073190953942534e-09,
4.8432241699368637e-09,
7.5333207711804005e-09,
1.1571213336349898e-08,
1.7560279059838645e-08,
2.6342102172822195e-08,
3.9077815023603054e-08,
5.7352723457265792e-08,
8.3309484459149089e-08,
1.198159159852664e-07,
1.7067436409931983e-07,
2.4088040920326967e-07,
3.3693953385761355e-07,
4.6725116624475065e-07,
6.425702168975942e-07,
8.7655679779719923e-07,
1.1864252036405598e-06,
1.5937033926619653e-06,
2.125114074163954e-06,
2.8135880363888443e-06,
3.6994194771060404e-06,
4.8315717790193825e-06,
6.2691403569660801e-06,
8.0829768558983157e-06,
1.0357476070166767e-05,
1.3192523470815733e-05,
1.6705597168738697e-05,
2.1034013525166795e-05,
2.6337300483653996e-05,
3.279967709649476e-05,
4.0632611731675562e-05,
5.007742517391779e-05,
6.140789839621402e-05,
7.4932838317705395e-05,
9.0998548539283439e-05,
0.00010999114603511309,
0.0001323386592639283,
0.00015851283834438177,
0.00018903060401360831,
0.00022445505925573821,
0.00026539598593863068,
0.00031250974871100881,
0.00036649852994809212,
0.00042810882282665942,
0.00049812911476477563,
0.00057738670054608126,
0.00066674357349216068,
0.00076709135403345817,
0.00087934522789667345,
0.0010044368807626196,
0.0011433064324913769,
0.0012968933916501072,
0.0014661266698544756,
0.0016519137150443164,
0.0018551288429151708,
0.0020766008659427013,
0.0023171001393626576,
0.0025773251626816612,
0.0028578888933597862,
0.0031593049457899901,
0.0034819738631761241,
0.0038261696619739504,
0.0041920268578310819,
0.0045795281881039355,
0.0049884932487531466,
0.0054185682624909234,
0.0058692171903065504,
0.0063397143898325523,
0.0068291390114124184,
0.0073363713062485686,
0.0078600910007842299,
0.0083987778677229504,
0.0089507145971105938,
0.0095139920410669387,
0.010086516873496114,
0.010666021671926857,
0.011250077393087201,
0.011836108177498089,
0.012421408381901833,
0.013003161702368289,
0.013578462216094069,
0.014144337136870636,
0.014697771048568066,
0.015235731353351639,
0.015755194647261453,
0.016253173715727202,
0.016726744825979533,
0.017173074982497923,
0.017589448805860206,
0.017973294694798296,
0.018322209935991551,
0.018633984436120757,
0.018906622765842901,
0.019138364225415969,
0.019327700666400584,
 0.01947339183280198,
0.019574478017725851,
0.019630289867570209,
0.019640455204369914,
0.019604902777511663,
0.019523862897971089,
0.019397864950795516,
0.019227731824062445,
 0.01901457133428738,
0.018759764768555474,
0.018464952701861236,
 0.01813201828365342,
0.017763068219846193,
0.017360411705083675,
0.016926537584416257,
0.016464090043424171,
0.015975843140951664,
0.015464674508824522,
0.014933538548134678,
0.014385439451895573,
0.013823404379195414,
0.013250457096579221,
0.012669592388529815,
0.012083751520918624,
0.011495799019549814,
0.010908501000870617,
0.010324505264057569,
0.0097463233235386797,
0.0091763145291257966,
0.0086166723878744675,
0.0080694131681281027,
0.0075363668325000082,
0.0070191703133441882,
0.0065192631120805479,
0.0060378851730539381,
0.0055760769538582044,
0.0051346815876356713,
0.0047143490091043627,
0.0043155418952459182,
0.0039385432539213658,
0.0035834654793212815,
0.0032502606821895657,
0.0029387320952118782,
0.0026485463497961646,
0.0023792464196019038,
0.0021302650284520004,
0.0019009383254938699,
0.001690519638429125,
0.0014981931260331764,
0.001323087163736475,
0.001164287310414994,
0.0010208487204004372,
0.00089180788172371237,
0.00077619357940002373,
0.00067303700080707416,
0.00058138091856700419,
0.00050028790450217257,
0.00042884754590075526,
0.00036618265223241272,
0.0003114544563585483,
0.00026386682897989701,
0.00022266953838469118,
0.00018716059936742455,
0.00015668776538135291,
0.00013064922650323467,
0.00010849358259722131,
8.9719166170324394e-05,
7.3872792849718536e-05,
6.0548019245975504e-05,
4.9382988285277639e-05,
4.0057941008898623e-05,
3.2292471479374614e-05,
2.5842597944117242e-05,
2.0497718943909252e-05,
1.6077517778024004e-05,
1.2428872815259583e-05,
9.4228247364857554e-06,
6.951645071459253e-06,
4.926043506349147e-06,
3.2725445352285319e-06,
1.9310572439556849e-06,
8.5265547033033792e-07,
-2.4206126665309948e-09,
-6.6653620205614147e-07,
-1.1662068147666301e-06,
-1.5234211118833117e-06,
-1.7567502875150609e-06,
-1.882256135583046e-06,
-1.9142126838594561e-06,
-1.865658418680931e-06,
-1.7487976342485887e-06,
-1.5752703573826735e-06,
-1.3563106622619693e-06,
-1.1028130487349802e-06,
-8.253259676195051e-07,
-5.3399059730195324e-07,
-2.3844167136647091e-07,
5.2314408130859588e-08,
3.3003069793556328e-07,
5.8734850083178555e-07,
8.1791419748974468e-07,
1.0164764884172668e-06,
1.1789583565517113e-06,
1.3024999245908711e-06,
1.3854701238857356e-06,
1.4274466809488637e-06,
1.4291653376123523e-06,
1.3924404327589154e-06,
1.3200599752796052e-06,
1.21565912389011e-06,
1.0835765601239448e-06,
9.2869860219071763e-07,
7.5629607030723569e-07,
5.7185889364236008e-07,
3.8093326368543784e-07,
1.8896580986933982e-07,
1.1588237945907764e-09,
-1.7765998727609298e-07,
-3.4315035409206593e-07,
-4.9155270670358712e-07,
-6.1976033102677193e-07,
-7.2536959647305658e-07,
-8.0670809902990766e-07,
-8.6284119505216469e-07,
-8.9355797851236773e-07,
-8.993382656536528e-07,
-8.8130258585050715e-07,
-8.4114752888061232e-07,
-7.810690624858071e-07,
-7.0367660855384974e-07,
-6.1190075257582496e-07,
-5.0889746267953929e-07,
-3.9795161705131911e-07,
-2.8238248926799476e-07,
-1.6545362875611735e-07,
-5.0289308180610658e-08,
6.0200598286840715e-08,
1.6338578105747198e-07,
2.5696954013430361e-07,
3.3903091206542833e-07,
4.0805444896344692e-07,
4.6294757566597186e-07,
5.0304578708927818e-07,
5.2810625610924089e-07,
5.3829069641487443e-07,
5.3413855957567282e-07,
5.1653183727860409e-07,
4.8665288594440808e-07,
4.4593679070338694e-07,
3.960198392704776e-07,
3.3868568508281758e-07,
2.7581074571006543e-07,
2.0931031052526879e-07,
1.4108672523251868e-07,
7.2980885016945797e-08,
6.7281082026548234e-09,
-5.6080715945770575e-08,
-1.1403200246067918e-07,
-1.6591586375119209e-07,
-2.107457141721214e-07,
-2.4777097453104777e-07,
-2.7648295091613702e-07,
-2.966141349960934e-07,
-3.0813132886227334e-07,
-3.1122313353317705e-07,
-3.0628245410841674e-07,
-2.9388476464696774e-07,
-2.7476294127223971e-07,
-2.4977951258642704e-07,
-2.1989719267520997e-07,
-1.8614855486903709e-07,
-1.4960567560296637e-07,
-1.1135052924876415e-07,
-7.2446849125418734e-08,
-3.3914089764944159e-08,
3.2959661390299842e-09,
3.8319512784462132e-08,
7.0397600487858934e-08,
9.8889359083454462e-08,
1.2328144274847915e-07,
1.431936774753735e-07,
1.5838099062368374e-07,
1.6873179227288288e-07,
1.7426305862977252e-07,
1.7511243704952044e-07,
1.7152774921402144e-07,
1.6385431296331911e-07,
1.5252053386011444e-07,
1.3802223481080748e-07,
1.2090619633509381e-07,
1.0175337204487144e-07,
8.1162224509901619e-08,
5.9732597131986067e-08,
3.8050499288651699e-08,
1.6674136349994601e-08,
-3.8785351788817972e-09,
-2.3140502532219546e-08,
-4.0704474502633319e-08,
-5.6229633695519691e-08,
-6.9446312514561073e-08,
-8.0158597798545185e-08,
-8.8244921192825884e-08,
-9.3656739925216916e-08,
-9.6415454734592049e-08,
-9.6607747535947811e-08,
-9.4379550466167386e-08,
-8.9928879912344172e-08,
-8.3497783851433182e-08,
-7.5363658389415869e-08,
-6.5830190021130933e-08,
-5.5218174240359093e-08,
-4.3856449256468447e-08,
-3.2073166380305173e-08,
-2.0187596884020506e-08,
-8.5026496428175296e-09,
2.7017544986135753e-09,
1.3174336035907565e-08,
2.2697053628107854e-08,
3.1088591939504288e-08,
3.8206719092771256e-08,
4.3949522081873212e-08,
4.8255556247304401e-08,
5.11029700890434e-08,
5.250768880496981e-08,
5.2520758621559566e-08,
5.1224968965856066e-08,
4.87308806586863e-08,
4.517239554105854e-08,
4.0702006332092765e-08,
3.5485865204895481e-08,
2.9698805788023088e-08,
2.351944635947047e-08,
1.712549226357036e-08,
1.0689343463145146e-08,
4.3740990889405118e-09,
-1.6699646635599593e-09,
-7.3083834344761689e-09,
-1.2424917544306577e-08,
-1.6923362982666211e-08,
-2.0728751410272498e-08,
-2.3787945934569207e-08,
-2.6069654179328551e-08,
-2.7563893494731014e-08,
-2.8280954798613416e-08,
-2.8249921311011992e-08,
-2.751680621072379e-08,
-2.6142378930736668e-08,
-2.4199753402154788e-08,
-2.17718130905138e-08,
-1.8948547230501803e-08,
-1.5824370385780102e-08,
-1.249549350888262e-08,
-9.0574092528777219e-09,
-5.6025476171937774e-09,
-2.2181503379279788e-09,
1.015595988324622e-09,
4.0271369715700241e-09,
6.7548157628480951e-09,
9.1478138785531296e-09,
1.1166763648263344e-08,
1.2784036886276411e-08,
1.3983722223634102e-08,
1.4761310585632869e-08,
1.5123114430720167e-08,
1.5085451482218197e-08,
1.467362771791593e-08,
1.3920757298867998e-08,
1.2866458912583454e-08,
1.1555468700521487e-08,
1.0036209584947552e-08,
8.3593554785857694e-09,
6.5764266450528627e-09,
4.7384494882160191e-09,
2.8947104065858126e-09,
1.0916291857553901e-09,
-6.2822714607203229e-10,
-2.2269738697144505e-09,
-3.6720703112937784e-09,
-4.9368074299515917e-09,
-6.0006196735780362e-09,
-6.8492240188263603e-09,
-7.4745932636839936e-09,
-7.8747743622698987e-09,
-8.0535658152870019e-09,
-8.0200708052172575e-09,
-7.7881448592772068e-09,
-7.3757583183738611e-09,
-6.8042947858916453e-09,
-6.0978070402763198e-09,
-5.2822516480575687e-09,
-4.3847227494364999e-09,
-3.4327042576385266e-09,
-2.4533580752715374e-09,
-1.4728639518892586e-09,
-5.1582435731798077e-10,
3.9525470198345928e-10,
1.2403985677447512e-09,
2.0025087837076583e-09,
2.6676147930321526e-09,
3.2250318794463842e-09,
3.6674271383483078e-09,
3.9907974592924129e-09,
4.194365462337872e-09,
4.280401022760062e-09,
4.2539774156805211e-09,
4.1226721972825749e-09,
3.8962237043447537e-09,
3.5861544992585143e-09,
3.2053732219079396e-09,
2.7677661484746991e-09,
2.2877893225393534e-09,
1.7800714434272852e-09,
1.2590368027103303e-09,
7.3855648762949161e-10,
2.3163485774715478e-10,
-2.4986301263094753e-10,
-6.9543860965223884e-10,
-1.0961390558987774e-09,
-1.444686457387817e-09,
-1.7355573321816881e-09,
-1.9650131940968729e-09,
-2.1310845235276047e-09,
-2.2335113889008981e-09,
-2.2736448686823054e-09,
-2.2543141518269946e-09,
-2.1796647555816404e-09,
-2.0549736897628197e-09,
-1.8864476167589004e-09,
-1.6810101114403082e-09,
-1.4460840236743122e-09,
-1.1893747003680522e-09,
-9.1865944892408456e-10,
-6.4158813702381733e-10,
-3.654992438369601e-10,
-9.7255025328619483e-11,
1.5690124788171208e-10,
3.9146375682345228e-10,
6.0175682713688909e-10,
7.8400110823078481e-10,
9.3535320852339918e-10,
1.053919424138544e-09,
1.1387448089361583e-09,
1.1897793754749946e-09,
1.2078236800701419e-09,
1.1944564236922493e-09,
1.1519469897811751e-09,
1.0831560383386929e-09,
9.9142738353956464e-10,
8.804744024047919e-10,
7.5426415968391067e-10,
6.1690229563926647e-10,
4.7252151705851905e-10,
3.2517626688997573e-10,
1.7874583464156158e-10,
3.6847818934324892e-11,
-9.7236523542898625e-11,
-2.2062390088759474e-10,
-3.3087683583965265e-10,
-4.2603738910590933e-10,
-5.0464677871826372e-10,
-5.6575127041175149e-10,
-6.0889503536654394e-10,
-6.3410095579832972e-10,
-6.4184060096329744e-10,
-6.3299479267786658e-10,
-6.088063283074016e-10,
-5.7082652954754444e-10,
-5.2085733766755927e-10,
-4.6089068184476618e-10,
-3.9304680949352089e-10,
-3.1951318971214307e-10,
-2.4248548754948181e-10,
-1.6411196276530577e-10,
-8.6442477619823496e-11,
-1.1383109764228013e-11,
5.9342835567605017e-11,
1.2422682925717024e-10,
1.8199976427443344e-10,
2.316490778990889e-10,
2.7242838315727879e-10,
3.0385982837669805e-10,
3.2572957277709773e-10,
3.3807691490478933e-10,
3.411777369894708e-10,
3.3552303017140816e-10,
3.2179334196009573e-10,
3.0083003788908554e-10,
2.7360429444213603e-10,
2.4118474087987456e-10,
2.0470464508911738e-10,
1.6532949499096999e-10,
1.2422576476810692e-10,
8.2531576917640855e-11,
4.1329879849511157e-11,
1.6246595231328373e-12,
-3.5679404401607837e-11,
-6.9793539101087061e-11,
-1.0005754932653195e-10,
-1.2594848194706246e-10,
-1.4708531313862563e-10,
-1.6322978510649861e-10,
-1.7428360806419269e-10,
-1.8028232115238969e-10,
-1.8138617177982868e-10,
-1.7786842560006984e-10,
-1.7010155848348546e-10,
-1.5854180725530146e-10,
-1.4371256785440168e-10,
-1.2618712845708664e-10,
-1.0657121183157246e-10,
-8.5485776823826988e-11,
-6.3550494716269978e-11,
-4.1368273707156395e-11,
-1.9511155508854639e-11,
1.4921462910111349e-12,
2.1166854242561289e-11,
3.9100729104738934e-11,
5.4950573368243395e-11,
6.8446601988241611e-11,
7.939470172110583e-11,
8.7676652139211273e-11,
9.3248428067163962e-11,
9.6136743978330813e-11,
9.6434035149304633e-11,
9.4292097633852264e-11,
8.9914629132568275e-11,
8.3548925543074683e-11,
7.5476993508212424e-11,
6.600633793842503e-11,
5.5460675725551429e-11,
4.4170813277686126e-11,
3.246590678787239e-11,
2.0665301088180791e-11,
9.0711163809974695e-12,
-2.0382770372589124e-12,
-1.2413786845117218e-11,
-2.1840052085425566e-11,
-3.0138776139120589e-11,
-3.717092448127088e-11,
-4.2837801821587496e-11,
-4.7081050462316879e-11,
-4.9881636213653451e-11,
-5.1257909542777049e-11,
-5.1262847456691219e-11,
-4.9980595699650732e-11,
-4.752244105974694e-11,
-4.4022349907432453e-11,
-3.9632211611353584e-11,
-3.451692436436921e-11,
-2.8849456456376684e-11,
-2.2806008471334708e-11,
-1.6561391641634021e-11,
-1.0284725085848277e-11,
-4.1355403388888582e-12,
1.7396340727328161e-12,
7.2101517781836862e-12,
1.2163552116399909e-11,
1.6507265645193948e-11,
2.0169715544770337e-11,
2.3100824391114013e-11,
2.5271950118254834e-11,
2.6675287852673015e-11,
2.7322785456094472e-11,
2.7244629879845287e-11,
2.6487368698082625e-11,
2.5111736389330222e-11,
2.3190258071953036e-11,
2.0804704517733657e-11,
1.8043471464469071e-11,
1.4998953661740302e-11,
1.1764979888241662e-11,
8.434369578474816e-12,
5.0966649181151886e-12,
1.836084553467078e-12,
-1.2702633377610803e-12,
-4.1538796967622756e-12,
-6.7560650503588464e-12,
-9.028790848249723e-12,
-1.0935249407903899e-11,
-1.2450088410524874e-11,
-1.3559343444386759e-11,
-1.4260088841865183e-11,
-1.4559832883556938e-11,
-1.4475688257449524e-11,
-1.4033352404529952e-11,
-1.3265935026364822e-11,
-1.2212671576216341e-11,
-1.091756203184772e-11,
-9.427973709064788e-12,
-7.7932453961786218e-12,
-6.0633277658191714e-12,
-4.2874919621228782e-12,
-2.513134590165575e-12,
-7.8470318041239905e-13,
8.572383021467086e-13,
2.3767890521400793e-12,
3.743326069765831e-12,
4.9319485649879818e-12,
5.9237514248552673e-12,
6.7059313821729523e-12,
7.2717334995385869e-12,
7.6202491231377348e-12,
7.7560795035711935e-12,
7.6888817805415265e-12,
7.4328159551061996e-12,
7.0059128142279326e-12,
6.4293835298557201e-12,
5.7268918455910545e-12,
4.9238094181612781e-12,
4.046474040089025e-12,
3.1214691856321478e-12,
2.1749416537573187e-12,
1.2319720950711394e-12,
3.1601097370645072e-13,
-5.5160989842464104e-13,
-1.3520826373480009e-12,
-2.0694403111933045e-12,
-2.6907831774248402e-12,
-3.2064140323246086e-12,
-3.6098848594361969e-12,
-3.8979590557663281e-12,
-4.0704953706919168e-12,
-4.1302612806398791e-12,
-4.0826848193003517e-12,
-3.935554873759205e-12,
-3.6986806354325417e-12,
-3.3835212632010013e-12,
-3.002796884470501e-12,
-2.5700918447569422e-12,
-2.0994606406207876e-12,
-1.6050462623191659e-12,
-1.1007197634769953e-12,
-5.9974880054770803e-13,
-1.1450168197561739e-13,
3.438078261376506e-13,
7.6533103641856295e-13,
1.1417476778428242e-12,
1.4663808345835501e-12,
1.7342635746276833e-12,
1.9421585638620505e-12,
2.0885330618014354e-12,
2.1734926678456117e-12,
2.1986780153443661e-12,
2.1671292828933749e-12,
2.0831239009081877e-12,
1.9519931739084623e-12,
1.7799237167096543e-12,
1.5737496215167776e-12,
1.3407411420396297e-12,
1.0883954126817613e-12,
8.2423433075395012e-13,
5.5561423481630753e-13,
2.8955143151758387e-13,
3.2566976529224493e-14,
-2.0944657734351304e-13,
-4.3133446985783763e-13,
-6.2876378984639808e-13,
-7.9828173899998814e-13,
-9.3734822515128825e-13,
-1.04434354411364e-12,
-1.1185524877736552e-12,
-1.1601267256537132e-12,
-1.1700277390082868e-12,
-1.1499529346290242e-12,
-1.1022478263147142e-12,
-1.0298073442334508e-12,
-9.3596941727944449e-13,
-8.2440397424511961e-13,
-6.990004313428908e-13,
-5.6375658313922615e-13,
-4.2267159951815984e-13,
-2.796455621853442e-13,
-1.3838766056991209e-13,
-2.3348193895354505e-15,
1.2541784057619284e-13,
2.4217369008148471e-13,
3.4567779410309988e-13,
4.3414637372487806e-13,
5.062826319370831e-13,
5.6127938390162051e-13,
5.9880923637532721e-13,
6.1900332774687273e-13,
6.2241986512903223e-13,
6.1000387507676971e-13,
5.8303971800746317e-13,
5.4309800279616313e-13,
4.9197857803178171e-13,
4.3165127189498619e-13,
3.6419600640526648e-13,
2.9174382760438645e-13,
2.16420275541779e-13,
1.4029237171822944e-13,
6.5320332348733454e-14,
-6.6850709085854637e-15,
-7.4098779486459969e-14,
-1.3551082677630185e-13,
-1.8974851321337189e-13,
-2.3589126357626925e-13,
-2.7327824317793364e-13,
-3.0150898666583174e-13,
-3.204374529440301e-13,
-3.3016005932813486e-13,
-3.3099836518255174e-13,
-3.2347716840792359e-13,
-3.0829884638343272e-13,
-2.8631481613986472e-13,
-2.5849500710132658e-13,
-2.2589623473235e-13,
-1.8963033643601547e-13,
-1.5083288409621292e-13,
-1.1063322314812411e-13,
-7.0126508693298053e-14,
-3.0348317854315987e-14,
7.7476826844085705e-15,
4.3308641113978763e-14,
7.559773303044979e-14,
1.0400552704972158e-13,
1.280574545819201e-13,
1.4741743563052146e-13,
1.618878057783825e-13,
1.7140577344413333e-13,
1.7603670950767115e-13,
1.7596463235014356e-13,
1.7148029944355341e-13,
1.6296735144081809e-13,
1.5088697620044942e-13,
1.3576156861087837e-13,
1.1815785804815237e-13,
9.86699596741252e-14,
7.7902779664975209e-14,
5.6456169152000239e-14,
3.4910178609039159e-14,
1.3811715189567435e-14,
-6.3371482828674892e-15,
-2.5089020703648087e-14,
-4.2059062557276957e-14,
-5.6930802232614871e-14,
-6.9459878962644866e-14,
-7.9475745827520222e-14,
-8.6881415407426395e-14,
-9.1651374727052591e-14,
-9.3827834303324365e-14,
-9.3515507796026182e-14,
-9.0875143569919323e-14,
-8.6116047206869434e-14,
-7.9487844647254031e-14,
-7.1271739359989762e-14,
-6.177151407173129e-14,
-5.13045186049667e-14,
-4.0192870882804941e-14,
-2.8755078857562194e-14,
-1.7298267790697638e-14,
-6.1111707863248021e-15,
4.5419883784391556e-15,
1.442662140789274e-14,
2.3341842848103111e-14,
3.1123441614259856e-14,
3.7645749427039846e-14,
4.282242703339635e-14,
4.6606214968125586e-14,
4.8987718729821049e-14,
4.9993318187957514e-14,
4.9682307501296806e-14,
4.8143384612134341e-14,
4.549061839126529e-14,
4.1859026750652348e-14,
3.7399900614565398e-14,
3.2276006731313712e-14,
2.6656797178467719e-14,
2.0713745391283316e-14,
1.4615918006080257e-14,
8.5258791765953108e-15,
2.5960097376986484e-15,
-3.0346918827853961e-15,
-8.2432763055734853e-15,
-1.2924943175398169e-14,
-1.6994556576800521e-14,
-2.0387573768345719e-14,
-2.3060399969388308e-14,
-2.4990195557167928e-14,
-2.6174174157065614e-14,
-2.6628440523031005e-14,
-2.6386425652221255e-14,
-2.549698315795962e-14,
-2.402221549391515e-14,
-2.2035101188819375e-14,
-1.961699487367918e-14,
-1.6855070666112783e-14,
-1.3839776562729243e-14,
-1.066236305774927e-14,
-7.412543458914139e-15,
-4.176336535160815e-15,
-1.0341344430853501e-15,
1.9409694138946467e-15,
4.6845665931664768e-15,
7.1420166611769614e-15,
9.2692185237911675e-15,
1.1033069830153086e-14,
1.2411622083590878e-14,
1.3393946261837277e-14,
1.3979730105586578e-14,
1.417863366951682e-14,
1.4009434163573522e-14,
1.3498994494782709e-14,
1.2681092230820952e-14,
1.1595146953846663e-14,
1.028488419073535e-14,
8.7969733516593626e-15,
7.1796754615496281e-15,
5.481534024599955e-15,
3.7501392309431786e-15,
2.0309920177186051e-15,
3.664903615213614e-16,
-1.2049442635997668e-15,
-2.6495869484357001e-15,
-3.9389672873820885e-15,
-5.0502611502140076e-15,
-5.966516662613831e-15,
-6.6767189094573208e-15,
-7.1757016455715336e-15,
-7.4639176297714375e-15,
-7.5470820328596081e-15,
-7.4357056682669462e-15,
-7.1445365304284514e-15,
-6.691929291745503e-15,
-6.0991630098854958e-15,
-5.3897273528328277e-15,
-4.5885971916340261e-15,
-3.721514483183258e-15,
-2.8142950198394192e-15,
-1.8921759186047798e-15,
-9.7921772482599067e-16,
-9.7772782090149117e-17,
7.3197085915831074e-16,
1.4923631874676627e-15,
2.1685793089559122e-15,
2.7488179777413957e-15,
3.2244120354647711e-15,
3.5898534001229013e-15,
3.8427372270275756e-15,
3.9836316094531396e-15,
4.0158806642665763e-15,
3.9453500378561183e-15,
3.7801247577971614e-15,
3.5301699420006175e-15,
3.2069651635290085e-15,
2.823123267073417e-15,
2.3920041600483227e-15,
1.9273335808749704e-15,
1.4428361075459412e-15,
9.5189074301569675e-16,
4.6721633509376736e-16,
5.9289376690864784e-19,
-4.3737640464817003e-16,
-8.3745905261379514e-16,
-1.1919407337000184e-15,
-1.4947256747582858e-15,
-1.7413902072092602e-15,
-1.9291910678597055e-15,
-2.0570310116702079e-15,
-2.1253852223145937e-15,
-2.1361927761768393e-15,
-2.092718031123527e-15,
-1.9993872669842345e-15,
-1.8616061985695887e-15,
-1.6855641168147889e-15,
-1.478030395650216e-15,
-1.2461489413062311e-15,
-9.9723586977506417e-16,
-7.3858529237509807e-16,
-4.7728758602967662e-16,
-2.2006394261117678e-16,
2.687965002449741e-17,
2.5797652411691995e-16,
4.6839977558697032e-16,
6.5413796842404542e-16,
8.1204571965893829e-16,
9.3986943856232341e-16,
1.0362491005236819e-15,
1.10069748349876e-15,
1.1335587728731145e-15,
1.1359488413466406e-15,
1.1096798286834509e-15,
1.0571718789751336e-15,
9.8135503983904648e-16,
8.8556439031846584e-16,
7.7343144579054351e-16,
6.4877479434909067e-16,
5.1549275689877767e-16,
3.7746064084929614e-16,
2.3843488410686842e-16,
1.0196607200706725e-16,
-2.8677534689519519e-17,
-1.50574687089187e-16,
-2.6120315114254517e-16,
-3.5847850035174562e-16,
-4.4077953614294381e-16,
-5.0696051944121192e-16,
-5.5635071674659152e-16,
-5.887420514927751e-16,
-6.0436590144140442e-16,
-6.0386029135557884e-16,
-5.8822889452133399e-16,
-5.5879337543452218e-16,
-5.1714067896230361e-16,
-4.6506689950253401e-16,
-4.0451934914363078e-16,
-3.3753838956209725e-16,
-2.6620050218871773e-16,
-1.9256394949984488e-16,
-1.1861823213461589e-16,
-4.623837724801433e-17,
2.2855091368824333e-17,
8.7129845737659446e-17,
1.4526865240068597e-16,
1.9618921963355089e-16,
2.3905692823899523e-16,
2.7329056360682638e-16,
2.9856133516311387e-16,
3.1478562023836663e-16,
3.2211200005028841e-16,
3.2090326388541473e-16,
3.1171414232364485e-16,
2.9526559080469119e-16,
2.7241648096161502e-16,
2.4413356953189017e-16,
2.1146060444858712e-16,
1.7548739655762069e-16,
1.3731963537066173e-16,
9.8050160763144367e-17,
5.873232224347743e-17,
2.0355966215025576e-17,
-1.6173507513118334e-17,
-5.0052682858926725e-17,
-8.0594027347108239e-17,
-1.0723602931988804e-16,
-1.2954954921130423e-16,
-1.4724045807370656e-16,
-1.6014872523818749e-16,
-1.6824419617126279e-16,
-1.7161936985526109e-16,
-1.7047954132676501e-16,
-1.6513071867748002e-16,
-1.5596575453537399e-16,
-1.4344914982596866e-16,
-1.2810099281244115e-16,
-1.104804896713297e-16,
-9.1169525080975176e-17,
-7.0756663606793087e-17,
-4.9821966365222341e-17,
-2.8922953976865816e-17,
-8.5819977105125861e-18,
1.0724632447593589e-17,
2.8575889706855258e-17,
4.4613125843390278e-17,
5.8545259521908482e-17,
7.0151931155543103e-17,
7.9284688822538297e-17,
8.5866296443816879e-17,
8.9888296953060243e-17,
9.1406998835559571e-17,
9.0538083640512467e-17,
8.745005454421775e-17,
8.2356761609760977e-17,
7.5509248085739199e-17,
6.7187164116215308e-17,
5.7689989955109472e-17,
4.7328300685627857e-17,
3.6415289149605934e-17,
2.5258743996401638e-17,
1.415365623951966e-17,
3.3756012808042866e-18,
-6.8249851312487398e-18,
-1.6227548258692527e-17,
-2.464511441454159e-17,
-3.1926920793399661e-17,
-3.7959974836659555e-17,
-4.2669569760943877e-17,
-4.6018807442636918e-17,
-4.8007201621397275e-17,
-4.8668452986680998e-17,
-4.8067502871354198e-17,
-4.6296983826333807e-17,
-4.3473193221772851e-17,
-3.9731720242016362e-17,
-3.5222857331677407e-17,
-3.0106924508375021e-17,
-2.4549629254958184e-17,
-1.8717576271610053e-17,
-1.277403058544949e-17,
]
dspplot.plot(data, phaseresp=True, log_freq=True, freq_dB_lim=(-160, 10), padwidth=8192, title='24th-order Bessel filter, lowpass 1 kHz', file='../svg/bessel_lowpass24.svg')
