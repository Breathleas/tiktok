# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 上午11:47
# @Author  : Wang Junling
# @File    : run.py
# @Software: PyCharm
# from test_celery import add
# result = add.delay(4,5)
# print(result.ready())

# from doyin_api import openDouyin

# params = {'cursor': 0,
#           'count': 20,
#           'open_id': 'fd7953f6-a3ac-450c-b0b5-feae26cfc337',
#           'access_token': 'act.67b913f6cefe0bc54bca274f2d3f2790W9FxXuHNSXUsDYoBSJO8lXooLEfH'
#           }
#
# result=openDouyin.delay(r'https://open.douyin.com/video/list/', params)
# print(result.ready())
# import logging
# LOGGING_FORMAT = '%(asctime)-15s:%(levelname)s: %(message)s'
# logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO,
#                     filename='TikTok.log', filemode='a', )
#
# x=[
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# logging.info(x)
# with open('xxx.txt','a+',encoding='utf8')as f:
#     f.write(str(x)+'\n')
#
words = ["", "cbcdfiagbbhfbdb", "iaebjjchhegdcih", "fjaecjijdcdbdbfdb", "gacchccbiejeheddbdji", "ggachhhj", "j",
         "dbhgiee", "i", "fdg", "dagbfdj", "aejbed", "dcibjcebgj", "d", "ajefedadiageeae", "hfcbjec", "eahbc", "hggeb",
         "cghbeaahjifgejah", "hafgjacjadcehj", "fifacef", "dffg", "hiabiic", "facdabebbiadaa", "hacabfcgaagaddac",
         "eijeejhhggccfccfd", "caighh", "cahifhjdaachhjfbehj", "bijgfgbfjaejgccehh", "fjaehiidie", "bbdefedcdgdfjihic",
         "dggecieeec", "ieaibdhfgfbfhafci", "jhghjfjdebehdjahjcd", "gafhcja", "gdbbgihjgjjgb", "digedajahe", "ef",
         "fjidaejffhach", "bdi", "ifdj", "hfbbjichhfg", "efdcfbiefjjgadafhfji", "eiibeceiie", "bbefbeidiahid",
         "hihijecbjghhafjh", "aibjjdd", "hhgagfbhfdcjcebfdig", "fdfefiaeccdfihgab", "jhadeddd", "ijghgbdejdhgi",
         "heiecgh", "daefjjhehjhcdecja", "jdhfgdedf", "bgfi", "dh", "ciifefgie", "ceibbhabaigdcdihfd",
         "ijaeaghaacijeeh", "dihaideibcdbdaadeibg", "cghjeeaabegcfhb", "fhigjdfccbbebfhjccfb", "ifcbjcjijhefbechhige",
         "cacbcgfdfieciijbj", "bjjefhbdbfb", "jbibahe", "djhfagbedaihegcdefa", "fhdgbicifdagahchahg",
         "afgfhgjdiebeecegjgh", "cdcfafdibjhccdhbjf", "gddhahggjbdj", "efcgbg", "cihgefjfe", "edafdhddbbgdhebj",
         "bjjhhafbffbea", "fgeafdcde", "babdihifchh", "f", "effeedhdeh", "ejfaeffddfgiedfahbf", "fdjcffaaffhgaef",
         "ccedddaajf", "jbhfhhefja", "hbidebajchhihhf", "hfbjigbcfbg", "baabc", "ccccd", "dahigffgb", "agfbjadh",
         "jjafjddhhadeeabajef", "iibegj", "eddgjgg", "afdheeedjbbf", "dijhefbbihf", "chehadgbfagdebbcbh", "cje", "ca",
         "fdedhchcbajhibc", "ebjadhjacchbejh", "gcjihgbcffjj", "cejhcghiiiicibcebc", "ajjgfchfjbiibfajb", "jfdfh",
         "jbhgcf", "hdbhbcgeb", "ijc", "hfjhajeecijfbgabhd", "hijhjhdgggiceigjgi", "eahiga", "cdjigcaej",
         "cehhffcbhhgfdaf", "hgf", "iiifghee", "jbbjbdeihdcchjjda", "jjfdeabe", "jiehbfcijfahafgibf",
         "jebdfgefbdchejdcbe", "ba", "fhijejhbbjjc", "diacjghgdj", "hgfabcc", "icjhjaedafbi", "dejbbfa",
         "cfhgjjccjebeijga", "abfbgijfgade", "fhegfiehhe", "jehdejfegfcigeid", "gdfibijdeh", "jej", "cdgicbabfg", "afa",
         "bbjcfcaefe", "bcjdchejhdfegadda", "ebacafg", "bggefc", "jfcec", "gibfigb", "dgjfcahaecjhhbeg", "geccgfjgfh",
         "gjghcfejdgeea", "gfai", "hhbjiajegaga", "fffdgebajcgjf", "cjcdfbjfe", "eaedjf", "ihagdidagggddcgiajc",
         "efccfgejjegbiag", "jdjcd", "geg", "bddjjbedadcdcgj", "beea", "bafdgceghjffgfedcdhj", "jd", "eeabggi",
         "dbjhfgjcffd", "ddcabdfcigbdgbbjdgf", "geghjdiifabbbed", "dabd", "ce", "hcjhhefdeffiiiicchf", "eea",
         "bjcajgeieb", "fgcabh", "agbjb", "hfiajfjdbiddg", "dgii", "feijfai", "cgcbbiici", "hgchffa", "hdefjdhccfcei",
         "gddeadhhehhdbabhi", "eehajcgjdcf", "jh", "djecdicjf", "chadcdejaj", "egebia", "bejibijc", "ccgabfgachjj",
         "ffhibei", "bhh", "hc", "chdbcejhiabfcbifachc", "ibjfhai", "dabibgcahafebhbchge", "jadhjabhaceaaceg",
         "dcgbbjhigihaejfb", "dfhbigaeacgfgagfdege", "hjjfddadgeeedhfifjd", "di", "dgifja", "ghjeehbhge", "fejicig",
         "fabibcedehe", "fjighjfiiiaig", "eba", "gjjaifgjedgccabbf", "adje", "aa", "ijcjjdihdfbcah", "edaiifiica",
         "jiabebeejifbdaai", "iacjjidfegfheh", "if", "bgc", "hjeeggegidcfhfafc", "ghg", "cajdbbe", "aj", "aidjhiie",
         "fcgdcdcbgjddccdi", "aaafghgefiaggjdeif", "bfdegiefgbcjecdbg", "adabha", "ihg", "ffedjh",
         "edhajcfidicehifjcghf", "ajbfichedejeggiace", "ibjabjfejfbchcaibdbg", "ifiichf", "b", "aeaedgibggah", "igdf",
         "djecdfcfebci", "bgigfbcidaecic", "e", "bccf", "hdiggbccaec", "djcegbdga", "iibddcfdiigg", "gfieg",
         "bbjefefjgda", "eibgeccfhicffjaajhbe", "ahe", "gcfggegdggjgjga", "ifhcbefaebcghae", "jhd", "ebeddibg",
         "dfcefebgcbjghieee", "hfcdihdeaiaaig", "ajhgafebabjjhhhh", "icbjeadgfeijbjjje", "jigahffbffcihgdjaehc",
         "fcijicdfc", "hgahgabihdbgaghadeja", "ccjdfgaghiadcicegdhb", "djdidehcbhbaabejdeac", "g",
         "bjejaachfffjgcjcgah", "abfecdjdhdih", "bjbaae", "dfcej", "gjfeacgfabjfhded", "jigdbiiaidacgghg",
         "ecdjgajdjiedjfghadai", "ddgfjefbgbgfadajde", "geahgchd", "dac", "eafbdahifhgidjahhdc", "jdchideabfabgidbcaf",
         "iaddfedjigdhfeb", "fhi", "hjcc", "dehefdcdf", "acdchdfgf", "eghhffgbfgibeehdi", "cfefcihgdafjadc",
         "eefegfiaaaeae", "gbgcjiffgbeagd", "ceagbigehd", "jafajgadehdiecdejff", "eahaahadddhia",
         "igbdfgjcghhabebebiaf", "effciadaj", "adcgeh", "feecgbgbhegeh", "fddhibhd", "dghchfghdgcdjdajjhaa",
         "jfjhfjgeegjf", "dcaheadhfhciicf", "dc", "jbcfggai", "ihc", "ghfea", "idg", "aidgcgaigddjgec", "fbgi",
         "djgbhhjbbigcj", "fheaibh", "gggifgfcebigeehicfaa", "aihjefggahifeffdjdd", "cbafidfdagiegdjhdbj",
         "eebfiifjgedfa", "bfihcdac", "ejaahfjhajegajfadcda", "bbe", "fhbdia", "hdgdahgifjbdic", "jiaacaifijfegjdfjgf",
         "gihbhd", "gdaffjiece", "aegdagdaaagjfhhb", "ieiefddafjbidb", "bdhffdcff", "hjfgeb", "agiagbjaigfde",
         "ajaghahibgbagabd", "jgadddfgig", "gbdcahjidjai", "chge", "iabbecaifd", "ecde", "ehdidcchacaeiaccf",
         "ecbjbjficdji", "jgdjcgbchbdfag", "cfhbjg", "fgjca", "geeihfadeh", "dhijieccibai", "efdbgcidddgdehdeai",
         "djia", "ffaacihcfbagijgga", "gicehdghhgdcda", "bgg", "aiddfdfihbh", "dbhafchafajcj", "hjhdaeabb", "bb", "ej",
         "cifhcafdjahcgf", "aabgigjefd", "cfibiaagehgafaicfid", "edbhgeh", "haec", "ecibgighfdcbie", "efg",
         "adhbeehcfhdhde", "ji", "gfjcdaidcefabjfi", "ghdabahbgabjcbffaa", "gibiha", "dcj", "iecc", "aaaciidihbaiacefi",
         "cfhfacabcfhdb", "ehccjffddhaiidej", "ajehfce", "jdfahahcdb", "jbca", "hfhcjaeaaebijj", "dheicebeijafahbafjb",
         "jiidcidabcijhc", "iegbhcjd", "bai", "hhbica", "fcchfhafeib", "gjiici", "dieaggifhdbjbfebaidi",
         "hcahiadcibafddi", "acgfgjgccjdhdgagacb", "fhfiiiadfbdjichhejd", "dhcgeaeagidcbbihb", "gdbjbebbgc", "hdfieh",
         "agifaebibhjggbah", "hafgaaaicdaaabjfj", "ahjbdfihg", "fijbdidjjjedcjb", "ggeejbjbhcd", "fghhca",
         "feajdigehdibag", "ebjjdhdhajhdcgfeid", "jgbhfgaajffd", "dcgi", "gifjcfbgbjhbcbh", "bihafhccaihh",
         "djdjbciagebjgfgcbcid", "gdajchficfajcggdddgh", "gffihac", "ijhgacdhi", "adebabfjgcdcihbhcbdh",
         "bhffaiijhcediebfif", "ccijfejheidfdgf", "fiafc", "dabdfgiieb", "hdfjbghejbf", "ejfbc", "ieh", "jdfjih",
         "checj", "aaahihejidiiiffijdhh", "ddfighfdcghiegjid", "agbejigicdbfgjbiff", "hfa", "ihfhcg",
         "fhicgjfjcffibddhj", "eajhacigijfiiajbfaah", "hh", "adff", "jicedff", "gd", "jfgbjhijchegadcf", "biha",
         "acgeaehfhjciaeje", "gghdjcihhcdgcb", "feg", "adfdfaa", "bccdejhhjgcbj", "jgfcj", "ifa", "cccif",
         "ihaaiadfhahah", "hciefifdajdaeibbji", "cibgjjchfibfbfghie", "fg", "jggibh", "achgf", "hiag", "adajjedbhf",
         "cge", "ighfebfghdg", "dggjhgec", "jcfbcccibhcbacf", "beieg", "jigijagefjdijjggida", "jbcefgbdfjbeaicbhh",
         "fjfjeaedbfhgedaecch", "jdfgbcgceecdjdbbac", "ibehcfcacd", "dbi", "bdfjdhcfbjbhadajjjj", "hfahcfihbhdaafgcffe",
         "chahbf", "fdhijcecahheej", "jiciadh", "ebcbahbecc", "eggf", "cjheaic", "abhie", "cicbj", "bdjjagcabfja",
         "eeeajiajaa", "cccjijbfd", "gbhggdbebjacgh", "ciddgjijeafiabebbjf", "hdgaehfbfdecabagadd",
         "ajbhdhghiaefbcdegch", "ge", "cjbfiaefghjhjebihag", "eeh", "igffiiihbefidc", "fbejegfgeaahgghebjj", "cfidj",
         "ejjadab", "ggfjiffia", "ggddcijihjajgjahia", "bfaegcjbidgdi", "fa", "baccaadid", "effaheaeegf", "deahhgfddb",
         "fbbigafijahigahef", "cccbihejifdi", "gbbgiadjfjbffejfd", "gedjigbgidbhbeii", "ejaeehaejddcahhgabd",
         "iiidjhfci", "biibebdjcgijijfiaji", "ciaf", "bhiihaihcefjehf", "dajfegjd", "ejif", "dbddiichf", "eh",
         "bfdfdcdfcfh", "ghdhfjaccabhdddi", "bhfjiahiffaddde", "ehihahabhfbhjieg", "egdh", "faje", "gdceaegiha",
         "ghhjiadeb", "hidfecjaahc", "bdf", "jdcejjhbdachhhdbh", "gihgcjjijg", "ghfag", "cddgejjgafjcgdhie", "c",
         "bcjccijgccegehid", "fcgdghjbjdjccebgaj", "jaehdjdddbgaaihbef", "gdichbcdgacafee", "hcacjeieahgjecdhhia", "hj",
         "aachbibdib", "igdejbfdbchgeeg", "ejae", "hicjfhicjhfiaccfjhb", "hebeaf", "abdjhcaeaffebiehidf",
         "ecighbhbjdgaggfdcccf", "hgfddcd", "dcaieafbfb", "hfghdbacdheaeaejg", "cjaejagjedaiehh", "eid", "giij",
         "babhjgdhfcch", "jjdi", "fcbhiiejgedfidigd", "gbjiacgghceehggdhe", "cdbdabcggiihgc", "agdacjejgdg",
         "gjcabceciidiejadj", "hdcegbaej", "aafh", "feij", "iicefb", "gbchd", "ifbabfb", "jijcaigbdehdedacgjgh",
         "fbeebegbad", "agdhijabhabifd", "hbjfjfigjebehabif", "cj", "eidhjc", "fhac", "h", "eiciica",
         "fbggeiifddchaicddcgj", "ejggjbjefbfejacgi", "egc", "edgjfaegajhifj", "cicehjehf", "eeibjdhjeghbff",
         "fjghjeejccbidhchdcaj", "didgjfj", "feh", "fibbiid", "ghdfhieiheefbfh", "ifbjfaah", "cjfaiieccgjgdggae",
         "ddbhjicbgfgjifd", "gdeccggd", "dgjaeabdjecfdcfaag", "ihjcdggbffbgeihfaefd", "fbeijhj", "fbdjdbghdjfh",
         "ghaaijgifagccijeh", "dhaaccbbgaedeehcfe", "ficegih", "ibbecegifjhhbefjcdfh", "ejafcbejiceahjjabjgg", "igg",
         "ahgabd", "gjcfiefgafhedf", "achfjg", "eebdh", "bbbjeafbegc", "fciaacgcbebhgbhchb", "ahhigje",
         "ddfcjjbfcfafiif", "cghc", "jbibgjbhg", "iggjihbbgcidjhai", "idjcbag", "bdjahgccgeihcc", "edhfidajecjadii",
         "ifggbc", "iiafdf", "hgih", "dbiejiiaedhgbdhf", "ffedehceach", "hbjibiiibadfbgjjhf", "dfaibfhjjddehc",
         "ijbidcahah", "bbb", "hhbbgf", "ibgidhhjgddejfjba", "gegcebabbhbd", "caffeebgajbcb", "ifdgfegehj", "hiaae",
         "iehbccfegih", "ibgjejib", "fjfjgcciifgccah", "fchfajjcjcdbjc", "djejidabejb", "ifahfiaabdjgadgjc", "fhbbidab",
         "dbahbfg", "bcciabbhjicibaaabge", "fcafa", "ga", "gfjaabfaagbhaddce", "dheeaahabfceijc", "hcjffhf",
         "efiicjjbgbchaieeag", "hdfjhabbagfdgci", "iebiddjcdcd", "ccfhcijecbjgadjj", "ed", "eebac", "hhffcf", "ejh",
         "cibhbcgcfgi", "daabe", "ajhijeggfa", "iihfbggchdaji", "hf", "agadedba", "gcjiaaaiggagg", "a", "bjajj",
         "gccgiaifhadgg", "gjccjfhccji", "jdcecgjfdbfeiaefeddi", "ccbhdhiffiibb", "iagghdcbffchiegggii",
         "iddieddgahebed", "cdhaecg", "cadegbjbhhge", "ddhaiccjafhagff", "daaddbefhh", "fijjgdfeffeaecgjdgg", "bif",
         "faij", "ecfcbabaajdidaghech", "hiiaibccgbjjfbjbai", "cafidfdjccecbcg", "iebhhheaaaeafbcgi", "bdbjjijbagic",
         "gfghejbjfhhhfcfaeb", "ecagbi", "bacfbffdcdhbhgb", "ehghdbehhjdjhec", "ghdjgbddihafeebg", "ihdfaidfccgccdjd",
         "fgegddhejcbafjec", "fdh", "ejhfbdceeicedbdififg"]
list1 = []
list2 = []
for j in range(1, len(words)):
    for i in range(len(words) - j):
        list2.append(str([i, j]))
        a = words[i] + words[i + j]
        b = words[i + j] + words[i]
        if a == a[::-1]:
            list1.append([i, i + j])
        if b == b[::-1]:
            list1.append([i + j, i])
print(len(set(list2)))
print(len(list1))
# if words[i][0] in words[i+1] or words[i][-1] in words[i+1]:
#     print(words[i])

lookup = {w: i for i, w in enumerate(words)}
res = []
for i, w in enumerate(words):
    for j in range(len(w) + 1):
        pre, suf = w[:j], w[j:]
        if pre[::-1] == pre and suf[::-1] != w and suf[::-1] in lookup:
            res.append([lookup[suf[::-1]], i])
        if suf[::-1] == suf and pre[::-1] != w and pre[::-1] in lookup and j != len(w):
            res.append([i, lookup[pre[::-1]]])

print(len(res))
