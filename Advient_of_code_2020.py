# -*- coding: utf-8 -*-

################# Advent of Code 2020 #################
print("""
##### Advent of Code 2020 #####""")

      
### Day 1 - part one ###
print('''
--- Day 1 ---''')

values = """1753
1976
1574
308
1384
1191
1731
1829
1658
1908
1663
2001
1298
1888
1134
1213
965
2009
1071
1591
1402
1184
1836
1536
1038
1871
1354
1149
1863
1728
1896
1599
1556
1222
1909
1858
1754
1947
1907
1656
1135
1845
1504
1473
1401
1700
1067
1790
1783
1539
1087
1614
1856
1895
1564
1106
1204
1492
1361
1897
1977
1210
1867
1797
1232
1148
1520
1989
210
1259
570
1512
1894
1309
1154
1327
1817
1875
1702
1885
1664
1220
1208
2000
1178
1423
1454
1780
1710
1362
1816
1491
1363
1478
1648
1163
1554
1195
1500
1320
1698
1636
1097
1573
1846
1747
1138
1083
1505
1387
1900
1143
1905
1826
1735
1496
1687
1704
1916
1991
1750
1637
1742
691
1967
1272
1657
1140
1070
1985
1405
1959
1218
1878
1340
1722
2003
1258
1726
1766
1868
1714
1463
2006
1537
1570
1526
1578
1744
1734
1325
196
1935
1849
1424
1972
1602
1859
1341
1177
1901
1902
1247
2004
1350
1965
1407
836
1899
1804
975
1510
1898
1560
1777
1523
1822
1830
1855
1839
1482
1661
1835
1343
1278
1449
1136
1732
2008
1686
1775
1952
1444
1499
1680
1752
1597
1963
1117
776"""

values = values.split('\n')
values = [int(v) for v in values]


for v in values:
    complementary = 2020 - v
    if complementary in values:
        print (' 1 - part 1: ' + str(complementary * v))
        break
    

### Day 1 - part two ###    

for v in values: 
    condition = False
    for r in values: 
        complementary = 2020 - v - r
        if complementary in values:
            print(' 1 - part 2: ' + str(complementary * r * v))
            condition = True
            break
    if condition is True:
        break


### Day 2 - part one ###
print('''
--- Day 2 ---''')

values = """1-8 n: dpwpmhknmnlglhjtrbpx
11-12 n: frpknnndpntnncnnnnn
4-8 t: tmttdtnttkr
12-18 v: vvvvvvvqvvvvvqvvgf
3-4 c: cccc
17-18 z: zzzzzzzzdzzzzzzgzr
5-6 l: llltzl
4-5 g: fzfng
3-6 b: bjsbbxbb
4-5 b: dbbbl
1-4 t: tttcrt
8-11 t: tttwtttwttn
16-17 m: mmmmmmmmmmmmmmmbp
8-11 f: fffffffqfmzfff
10-12 n: nnnnnnnnnncvnnnf
5-15 b: ztmcfqsrbvbbbqbxw
12-13 m: mmmmmmrwmnmmr
5-6 d: sddddznddddkzdbpdv
14-15 l: lsllllskllllllllll
3-4 z: zvrz
2-8 h: fthhhqhghhtf
2-4 x: xhtxsp
6-10 q: qqlxqcvqwqqx
1-3 q: qqqqqqqqqqqq
6-15 l: qlllllllllllllghl
1-13 k: tkkkkkkkkkkklkk
8-12 k: kqkcqknklfkkvqp
15-16 f: hnjnmgfxdfrffdfff
3-11 k: ckkknpdlkkfkk
1-4 z: vzzz
4-7 c: gxgfcrcv
12-14 x: xxfxxxqxxxxxxq
4-19 g: gggwggggggggggggggxg
5-8 c: cdcqnmccxh
7-8 x: xxxxxxxcx
2-5 f: fmffjfff
2-3 w: wwbw
10-16 g: spbndcgjvnwbgcrvtg
4-5 t: ttttttt
6-10 d: dpdddddddl
1-4 s: ssszsss
8-12 f: ffffffffffffhfwffc
1-2 f: gmff
4-5 s: sssswss
12-17 v: vvvvjvvvfvvvvvvvvvv
3-5 n: tlndn
14-19 n: nnnnjjnnnnnnnwwlnnsn
17-18 d: dddcdddsdddddddddddd
5-17 x: zgsxphpttbdhqhxmxwms
1-3 f: ffffff
2-3 f: ffgf
8-11 r: dvrjxddrrgdrckrrxmp
9-12 n: nnrvnnnnxnhnnnnnnn
7-11 p: kxpsfsppppkplqxpmpfb
7-9 j: rjjjjjkjjjnj
3-4 g: lwng
9-10 h: lhzwfzlnhh
5-6 s: wlbdsfs
13-15 x: xgxqzxtpxgxqxjx
1-3 q: xqqq
15-17 d: ddfddtdddddhdfddddd
10-12 r: sgxrtkmwzrnrrgmscc
2-5 g: mggjg
7-9 t: trltttttt
7-13 b: bbbbbbqbbbbbgb
4-16 l: lllllllllllgllxjcll
14-15 v: vxvvvvtvvnvvwgv
8-9 m: xjmjklmfdnw
7-12 k: xhklkjhhwfrdkrlkkx
2-3 l: mlxfls
9-10 k: vhlgnkppkx
10-11 t: ttttktttttpt
1-3 q: qpkwvqb
6-7 k: kkvwjbkb
3-5 j: qpnmjjndh
8-12 z: zznzgzttvzzzzzg
8-11 n: wznmgnfnnfp
9-12 v: vvvvvvvvvvvvv
5-9 h: hhhhzhhhhhh
1-6 q: qsqqqdqqqqqqqq
2-5 c: cclfc
1-5 z: vwpzzzfzzzz
5-7 c: gcqcfcgzzcp
9-10 g: ggggggggszggggg
5-15 q: flqhqdqhqkqwcqqq
2-4 l: llpd
13-15 h: qbnzqnnfhchstbp
3-5 t: ttdttt
2-3 c: cccc
6-8 v: vvvvvdcvmv
6-7 n: bnnnnnn
10-16 t: tvztwtrbtttttqtt
2-5 m: zsvmmbbshz
3-13 f: xkfqfqrsmbjhj
3-5 c: cccjzjt
13-14 w: wwwwwwwwwwwwww
11-12 c: vcclpbccpqjgc
3-11 p: hqrlgpffspphvthb
3-12 z: zzjzzzzzzzzpz
3-10 s: ddqhwpqbxs
3-8 d: dddddddd
4-10 j: ktgsjzkqpjcjwcs
18-19 t: ttttdtttttttttttttf
6-11 s: jndthsskqbg
2-7 w: gpfhzwm
12-15 k: kkkkdkkkkkkckks
3-5 w: wdwnxw
2-4 w: wwtw
11-12 v: vvvvvvvvvvcfvv
12-15 h: wxlhgdxhhgttxhhnrgh
8-9 v: bptwkqvjxjdbhnzmbx
6-10 m: wrmmnqgmch
6-8 p: pppxcxprbcpppp
6-7 r: rrrrrkmrrrr
11-15 g: tpgkggggggvggfgtb
5-6 m: mmmmmmm
8-14 f: fkvwkmrfftmjczhf
12-13 q: rqqqqqqqqqqhqqqq
12-14 f: fffffffffffnffff
9-10 d: crsbdsddwdpddcpddd
1-4 b: gbjbx
2-3 n: nnnnnsnn
3-14 t: chtkhtdlddrztt
9-10 d: ldzdsdvxfmp
5-6 j: hrwjjj
1-4 l: lpllllblzll
10-12 l: glhnxlpdnlvq
5-6 q: jqzfqqt
3-11 z: npvzgdvpmnz
6-7 g: fgggrgg
4-10 f: xrtfnrcbgbkdf
1-14 f: ftvftwfxwmfmbftsd
3-6 s: scjsfcs
3-6 v: hvvvxvnvvvgtvgv
8-10 z: zzzzzzzzzszhfzzz
1-14 z: szzzwdzwzzqzzzz
8-14 f: wffhsjdfrslfpfnq
4-5 k: kckkkkkx
7-12 d: dddkkdkwddvhs
6-7 c: ckpmczj
1-15 h: hhjjhjhhhbhbhcckxh
2-4 n: xjhn
7-10 t: ttttttwttttttttttltt
1-5 v: vkbdvvgv
1-4 z: zzzlzzzzzzzzzzzz
3-5 f: fffffnc
1-2 c: pcfgl
8-12 m: mmmmmmmmrmmmm
10-14 l: lllllllllfvllblldlll
4-11 s: fwrbwnpttjpmnmsfnhs
9-11 m: zmmrrxcmsmmmqmgmmmmm
2-7 s: sqslsssj
18-19 p: ppppppppppmppdppwpz
6-8 k: qmfwhkkkd
7-8 v: vvvlsvhzgv
8-14 g: ggggggggggggggggg
3-4 r: rrrnr
7-8 m: kghmmmjm
3-5 g: ggtnbzggbxklprk
11-13 q: bqqqqqqqqqqfhqr
3-4 z: zzzz
17-18 b: bbbbbbbbbbbbbbbbsrb
2-4 f: wpff
5-6 z: zvrlwf
7-10 p: pppbdqwgwptpppp
2-12 v: vzvvvvvvvvvmv
3-11 f: fffqffffffcfff
7-10 v: vbsvvkgcwjxvdkvvv
18-19 l: lwmlllllllllvllfllll
13-17 s: gwssszsshssssstxs
2-3 k: kkdk
5-11 k: kkkkkkkkkkkkkkk
1-6 l: gllllll
1-5 c: jccccccccc
1-6 v: vdjvld
7-8 n: kjnknwnngnv
16-18 w: wwwwwwwwwwwkwtwwws
5-8 b: qbfjbcdg
13-14 d: ddddddddfdkdkddjd
7-8 w: nwwwcwwwkfwwjwwl
13-15 q: qqqqqqqqgqqqgqq
11-12 c: cmccjcqccknzcrcc
4-6 x: wvlnxbb
5-7 j: fmjffjj
3-5 q: xrqqnrhqjst
12-19 n: nnnqnnqnmbvnjnnqnnn
13-19 s: sqssvscdhssslsshwstt
15-17 k: kkkkkkkkkkhkkkcktkkj
3-5 s: cpsbs
10-12 b: bbbgbxhwsvbc
1-9 v: vjvdvdvlvkx
13-15 z: zzzzczzzzzzzgczzz
17-18 r: rrrrrrrrrrrrrrrrrr
3-8 z: tbmczfgz
9-11 h: dthhhhhhhhvhhhnhhh
11-13 l: qfzlnljldmllf
1-3 s: sscs
5-17 q: qfvrqphfjffckgmpj
2-6 f: rjfjvfgpf
5-6 h: hhghkh
12-17 s: ssssssssssssssssssrs
12-13 g: gggggggggggbl
12-13 m: mmmmmmmmmmmtcmmmm
16-17 x: rzcfxbdxxdstzdxmp
7-9 b: smbzgbbwzbzbb
11-13 f: ffskffvfgfflf
1-2 r: pmrwrmrbrrr
3-4 n: nnngnnnn
8-10 w: wcwwrptwwlcq
4-7 n: nnnpndn
1-4 l: lllpll
7-13 q: fqqfdqqqqxrlkq
6-7 f: fnrftkfffdf
8-10 s: cwtgnssstsmq
2-9 d: ddjkgsxkdsddgf
10-11 l: lwpjlpkzqlllltrln
4-20 n: sndnlnnnjpnncsjnrnnn
1-16 l: rltllllllllllllnllbl
15-19 w: gwtskpwwmnwnvmwrzmz
4-9 s: mxsssztlsslsmnbvwjdr
9-11 c: cccccdhcjckcccc
3-7 s: szsrrqjl
1-3 n: nnnnn
3-4 x: zcbj
16-18 s: sdsssssssssslsstsss
9-20 w: cnprwwnfdjlwqwswqwwz
16-17 v: vvvvvsvvvvvvvvvcvv
4-7 g: gxzgngg
5-6 s: sssssrs
11-13 q: qqqqqqqqqqjzq
8-10 x: xxxxxxxvxx
12-13 b: sbbbbbbbbbbbbbb
4-6 f: ffffff
7-8 d: ddtddddd
1-6 z: vzzzzzz
16-18 s: ssssssssssssssvssb
6-15 s: xbqsssxwsscsfbl
12-17 z: zzzzzzzzzzznzzzzvz
4-10 d: xwcdtdbpmtt
3-8 v: vjvjnxbw
4-11 q: fdflhjpvqmq
10-12 s: rqvjgslssssf
3-4 m: mmmmm
6-10 x: xxxxxxxxxxxx
4-5 g: ggggg
8-10 q: cwgbqqsxqgfqqz
9-19 l: lhzllnmlcgrbzrmzwln
5-14 x: xqqzxxnxxswwvxxxz
4-11 x: xxxlxxxxxxxx
13-17 d: ndrzwljrbcptswkfd
5-15 l: lnllhlllllllclpllll
1-2 s: cdsv
3-4 j: fpqj
4-7 r: rrrtrrxtr
9-11 h: hthhhhhhvkbhr
8-14 l: rllllllsllnlll
2-3 t: tvtt
8-18 h: hhhnhvhwhhhhphhhhwhl
1-3 d: ddmdd
14-18 q: nhqkrqdflknwbqvgph
3-4 z: zkzx
1-4 z: zfwgzzgrzcs
2-4 k: lkpxr
3-4 h: hhhhh
7-16 t: ltjttttftttttttdct
7-8 z: zlsxvwzxs
1-2 t: twtt
10-16 q: qqqqqqqqztqqqqwqqqqq
4-6 r: hgtrvrrfdwrgqw
3-6 z: bwzlzzzz
7-8 z: zzhzzcczqzzz
5-7 h: fjfhhphdc
13-16 p: tpnzmdbvwwpstpxprm
1-10 q: qqqdqqvqqfqqqqq
11-15 z: zzzmhtzzszbkzlz
2-4 x: hjhxkpmjwjkrsjdklzfc
1-2 m: kmgjnkwvfqxtmqc
9-10 j: kjlpjjjjxj
6-7 x: wxcxpxrxxx
17-18 k: kkkkkkkkkkkkkkkkkkk
5-7 d: pdddddd
2-4 p: pspp
2-11 n: nbnznnnnnnxnn
4-6 c: cxccdccgnf
13-14 c: cccccccccgdccccpf
1-3 q: qqrhsdcqqfbr
4-6 l: rqbrnjgmttlvbxjlrrh
15-18 k: kkkfkgkkkkkkkkckkz
13-15 r: rrrrrrrrrrrrrrrr
10-11 b: bbnbcrblhpb
2-7 z: znlzklzc
5-11 f: bfzcdfxmljrmnw
1-4 k: kkkkkckckkkk
3-4 w: wzww
2-4 l: vlllll
14-15 w: rzvrjrqgkcxhwwp
6-7 k: kkkkkldm
5-7 l: hbhllbn
8-11 x: xxxxxxxmxxxx
1-12 d: jddvddvddddqdddd
1-17 n: jnndrnnnsqnnwnnnmnnn
11-14 n: kgzqtdnqbbvmqj
2-3 d: hvkd
11-15 k: kkkdkkkkkkkkkwwk
4-5 v: vvvvk
2-3 x: bgbh
3-6 q: vqvmnp
1-4 n: nnnn
6-10 x: xxxxxxxxxhxlsxxx
1-16 x: xxdxxxxxxxxxxxxb
4-7 j: jnwdsjzr
5-6 g: bglmhg
2-4 p: pppp
7-17 h: hhhhhhfhhhhhhhhhfhh
8-16 h: hhxthhhhchqqhhhhh
3-6 k: kkkkkpkkkkrkk
3-4 z: gqzs
10-12 f: fffffffffzfsfffffff
9-11 f: fcgpwqfxnvf
8-10 j: jxjjjjjjjrjjnjbjzjj
6-7 h: bkttbhkzcmmnqs
1-13 w: kwwwwwwwwwwwnww
2-8 p: pspqpppzpjhp
1-13 n: nnnznnlnnnnfvnnnnnnn
2-3 n: nnqpnn
5-6 n: nmbdnn
13-15 d: jrdsdkddjvddsdsrh
6-9 n: ntnwnnknnncnnnnl
2-6 z: zzzzzznvz
9-13 c: ccccccccqcccw
5-7 x: qxxfxhmt
8-10 z: zzzzzzzltz
12-14 k: kkkkkkkkktkjknkkgd
6-9 z: jxjszgwzx
5-16 c: cccgscjpcccccccxd
6-7 g: lggjvgjghbtgggg
8-14 r: vtpbpwrcdqlrrfrrrrrs
6-14 w: twcwwnwwwqxwrwwmwf
3-6 s: mssbzssstgtmlw
1-12 m: mmwmmmmmmmmmmmmr
5-11 l: lclgllllclll
7-9 j: jjjjjjjjjj
2-14 n: wntdjqhtcqvnknjlfq
3-5 v: vvvvvn
7-8 p: hjcphnpm
2-7 w: wwwwwwswwwww
13-14 q: qqqqqqqqqqqqqqqq
4-5 d: kddmxcqqgzpddwddd
1-7 b: bfrhwgjtbchbzpcqmt
3-4 k: nkkk
6-7 q: qqsqqwqqq
1-10 g: gggggggggwgggg
1-4 k: kkkkkk
2-8 m: mtmmmmmnmmm
1-5 d: ldddd
5-8 s: szsssbqqsssssfsscsps
5-10 m: rljqkbcmbmxqsnbmzp
1-4 w: wfwwcrwnxxwwwdwh
9-12 v: wvqwvbvpsvvlvvvvvv
3-4 l: lljx
7-8 r: fzxvcbrmh
3-4 z: bvng
4-8 r: cskrnqrrjkvdtfv
13-14 q: qlqqxqqqqhqqqqqqm
14-20 n: zknbnnbnnznkhcnpnnzn
6-8 m: mmmmsmmn
8-15 x: xhxcxxxxfxhxwxt
11-12 b: wfmnwdltwjcb
3-13 t: rgjpbdbmdjhmx
1-2 x: hgrhrwxzwzdx
1-3 v: pvxvvdrvvv
3-13 q: qjqmvqkcbbqhqfqqq
4-8 h: vvzmthcpwrlnwhst
2-10 b: bphlmgjftzrwm
1-9 h: fhhhhhhhl
14-15 c: wrtccjwcccwvhcv
2-3 f: nftrf
1-8 l: ljcklkbllsb
1-7 w: zwwwbwwwwww
10-11 m: hkmfghpvhzm
8-19 r: szrrwmrrrbrrrrtrrhxl
3-4 j: jprp
4-10 h: hmbhqncmxft
8-12 d: dddddddtddddd
9-10 l: llllllllll
7-10 x: xxxnkxxxxxxxnxxxf
10-13 b: nbzzkzwjxbbwbgtsk
11-16 l: llllldllllllllwllll
4-5 d: ljzdlxwxmzxldwfwmqd
1-13 d: dgfddmwsghdsdnddd
15-16 j: bnfcxqjjjsdpznjprbjj
2-11 w: wlwwwwwwwwwwwwwwwww
5-8 z: zzlkzfzt
5-7 x: nqpjxxs
5-9 j: jgjjbjjjm
2-5 h: jvbhf
11-14 b: kqxfgwbbpnrjrjb
6-7 h: zjhhnhrr
2-7 c: crjcccgcc
4-5 z: gzczx
4-6 k: kkkrkkkxrtk
9-10 j: jjjjjjjjmj
8-12 b: bzdmbbbbbbcbdbmbdbh
2-6 t: wtjtptrptstx
1-11 w: wlmqwzkzmtwkd
11-12 h: khrbhmxhkbbh
10-18 x: sbttcdvmcxjxnjfjrkn
11-12 w: wwwsnwwwwcwz
5-18 g: zmgggvgmtrghhfwgbgjz
12-16 d: clxdsflvkpcsdmtqdwbd
15-17 p: ppppppppppspppxpzpp
4-5 k: kgrfk
2-4 l: lhfl
10-15 x: wdlvcxwtpjfflvzl
3-4 m: jwmmcjdxhkgbmtblmgfr
18-19 d: dqdjdqhddtdffddkmgd
5-9 h: hfngbhhchhkhkqmqgf
17-20 m: kmfmzrmmnmclsmthmfmt
7-12 p: ppppppppppphp
19-20 h: hhhhhhhhhhhhhxhjfghf
1-7 n: wkjsncn
1-6 x: xxxxxxxx
14-19 q: qwqgqqqqqrqqqqqqqqqq
7-16 n: nnnnnnzjnnmknnnqnnn
8-9 s: ssbssssbss
4-5 k: ckxvkhz
3-4 s: ssss
3-4 d: hwdsd
1-15 f: jfffffffffffffq
2-5 p: jppgpwwvhv
15-16 f: pllnmftdbzxhfkxf
5-10 w: vbwgswxwlwwwkwlw
1-2 g: glgg
10-15 c: cchccccclctcccdcc
4-5 r: rrgrrhmwrsrr
3-10 k: rwkcnwknkk
2-15 t: ttttttttttttttttt
11-12 l: lllllllllllql
4-6 m: jqdlzxvmv
10-12 l: lllwlmslllljflwll
1-2 s: mssss
3-7 h: plhgfjhchm
15-16 q: qqqqqqqqqqqjqqhsqqq
11-14 p: shpzpcmvscpccprdmmp
2-4 w: lgjn
5-7 q: vqkcstq
8-17 b: hbbbpbbtbbxbbbbjmb
8-15 b: bbbbbbbbbbbbbbr
14-16 s: sssjssssssssspsssss
9-13 w: wwwwwwkwkwwwxwww
4-7 k: xkkkkkwkkkkjkkkkk
4-6 m: bmvmnl
6-12 r: qrxvfrhcrtrrrm
2-8 t: rttwgtztkddbzbdd
1-4 x: sxbxxxd
1-2 b: bxqbqh
2-5 w: glmnxmlcmwkphwmxfk
12-13 n: nnhfnrnnsnfnnnmn
3-4 b: bqbbbbx
4-5 v: vvvgj
6-7 m: mmmmmsb
3-4 z: qqblwc
15-16 t: tttqdtttttttttmt
2-3 f: fffl
2-11 x: xpkxxxxbwrmxxvmx
11-15 p: lsxpjkwqjxqgwkpp
4-7 h: mvkszlvhkrfqpzfhdwbm
8-13 j: jjjjjjjjjjjjjjjjj
7-8 z: bdzzzzrz
3-6 v: vvvvvvv
10-12 f: ffxxffbfmnffffj
9-12 t: tjttwhtxtttttt
4-5 n: pdnnn
3-4 p: phprxnv
11-13 j: jjjjjjjjjjjjzj
7-10 g: ggggjgggdwggmgjvg
2-3 q: jxqqfqz
4-7 t: rghbdhgt
5-6 c: xrfcxcccctsp
2-4 j: ljpjspjbfkbmhzwbxmzc
7-8 s: ssssssvm
1-6 r: srrrrrwv
1-17 k: lkkkkkkkkkkkkzkkqkkk
10-13 j: xjjjhjjfjjjfljzmjbjm
8-9 q: qztvqqwqbv
3-4 v: vbvc
2-11 g: nwhdjzrvwxgngsh
8-13 k: kkztkkkxkkkgkclrrkk
9-10 n: tnnknzlsbnnn
5-6 v: vlvvpv
9-11 d: ddddddsddpvddddd
17-18 x: blxxxlkvxxpxftmjxxwp
6-9 z: zztzzkzzzh
3-5 j: sjkjq
4-11 k: kkkdkkvkkkkkkck
5-7 n: nnnnvsjn
5-7 k: kkkknkk
7-10 m: qdbmmmmtrvxggmmqlss
10-12 t: tttttttttrtvttttt
3-6 l: lsljmcgv
8-10 j: tjhnmwrjrtjmj
15-16 l: cllllrhwllzlnlll
12-14 m: mmmmmmmmmmmlmqm
3-4 m: mmrmmmmmm
2-6 p: psglpp
1-3 f: ffwwffffzf
3-4 z: zjzz
13-14 m: bzmmpmvclmzkmf
1-2 s: sssp
12-15 q: qqqqqqqqqqqgqqhqq
6-8 q: qhldnvqb
1-4 n: nnnn
9-10 t: rgzqzlndrtlzzdbtcrxh
15-16 w: wwwwwwwwwwwwwwwwww
2-4 h: hghhf
1-3 x: twhx
13-15 l: zhlsnvjllxqlqdq
1-3 b: jbzbjrfbjfrgsml
2-12 t: znskzrlnbjktpftd
3-12 b: grbvbwjbbsbgbpb
6-18 t: tttttztttttttttttttt
9-11 j: jjjsjjhjjqjjjrjnl
1-16 w: tgrwwwwwwwwwfkww
1-5 d: ddfdqdd
8-18 w: wwwwwwwwwwwwwwwwwww
5-16 s: rvlmcczcgbxbtxxqxm
1-4 z: zzqznzwtkg
2-6 j: zqpcvv
6-7 t: zttmtth
3-5 g: gggggg
8-9 j: jjjjjjjpjjjjjjjjj
11-19 k: ndlbdtjkdhgfrrvmtrk
5-6 s: ssnssss
6-7 f: zgzfqfg
16-18 k: kkkkkdzckbjmcjdfkkk
1-7 c: cccchmv
6-8 h: hkhhhhhhhhw
3-4 m: mmgm
3-4 j: jwjwj
1-2 t: jtttz
3-5 n: nnnns
2-9 l: wdpwdpcqlkrrt
6-11 d: ddddddddddpdsv
9-11 v: vvhqvpnvglvvvxv
3-8 v: dlvvkvmk
8-11 f: fmdfmcffsfdng
9-10 q: tqqqjqqqgqqqq
3-17 m: mzmxdgwfrgjjkrbjmvv
2-4 d: xwtdpd
10-11 v: vvvvvvvvvvn
6-8 l: fxcllfhl
17-18 n: nnnnnnnnnnnnnnnnjz
1-2 n: lnnsn
2-3 v: vvlj
11-12 s: ssssvssshsvc
7-8 n: njnnnnssn
1-8 h: hhhhhhhhthh
11-12 j: jfjjjjbbgjjj
5-7 n: cltwnfn
4-9 c: wgcccmxxr
10-13 n: xnnnszfnndhcnmnzc
7-8 n: nnnrnnrkqzn
7-10 f: ffffffbffff
2-16 z: zzzzzzzzzzzzzzzrz
13-14 q: qqqqqqqqqqqqnb
4-9 q: qcqkvlqgqdqnq
11-17 l: ppvjfgvhnxvzpdphlcxg
4-5 j: qjqpmjpj
3-4 n: mnqq
4-7 w: wwwbwww
3-9 n: mbpgnnfzn
10-13 j: jjwjjhjjjwjjj
2-6 f: zcdrsgqszfn
1-7 x: xmzkwtx
1-5 q: jzfqgdqrsqqqqgq
4-17 p: npvpppcljpcgjfbhpppp
5-11 g: grgggfggggggg
8-12 n: hdcnbplfnnmn
2-4 j: jnfw
13-14 d: mfgvkdrkzggddd
5-7 k: kkkkfkpkk
7-9 q: tqqrgqqjwqfpg
1-2 g: rdgxg
18-19 w: wwwwwwwwwswwwwwwwwz
8-12 q: qqqqcqzkvdqqqqspqf
12-16 p: xfzcfvpdrpnlpppmpq
4-5 q: qdqkb
6-12 p: glpppnpsppppppgnpp
1-18 g: ggggggggggggggggggg
1-7 h: hfhwsjxmnhd
1-8 h: hhjhphhchhhdh
8-11 z: zzzzkzzzzcr
13-18 w: qwhwvxwwbtdwlqwwww
4-11 n: nntnsnnngnnknnnptpn
1-8 c: cmccflmjccc
12-14 d: qgdrdhjddddddd
1-10 r: xrbmrrrwbcrrr
4-8 t: pjsfzxsst
3-6 h: hhfhdhl
5-6 m: mmmmmmmmmmm
8-9 c: jfrkcrrrccqcqsh
8-9 w: wwwwwwwbww
3-6 w: tvwpkvwwgwwqlcwzg
11-13 n: qnvnknfnccnngnnn
11-17 q: qqqqqqqqqqqqqqqqlq
5-9 k: whkkkkkkmmkkclkfjl
8-13 d: dddddddcdddddd
6-7 c: cckccckcc
6-9 n: nnnnkvnzn
2-10 x: fxdtdbbfpxfcdd
3-9 r: rrrxrrrrrrrlrrjr
3-10 d: ddgkdqdrfwdd
3-12 p: pppqpppphcppp
10-12 r: frrrrrwrrlrrrrrf
14-19 x: vxxzxqtxjgpxxxxvjxxx
1-12 v: vvvvvvvvvvvrvvv
11-13 c: cccccccccchmcccc
4-10 t: tmbpgnmtwksfwcmttbwt
3-5 c: mdcncrcj
9-10 f: ffffgsfqfmf
8-9 t: dzpdqtttqtptltttm
8-9 h: wwpqhshhhbv
12-17 s: sssssmsztqtbspssds
11-13 n: pnndnbnnvwznnnxsnnnn
6-10 n: nmxsvjlfnd
2-7 h: thlghzhf
6-9 s: rshshxpvlstdsd
16-17 c: ccccccbcccphccvcqc
6-11 q: jqqqqwsbqxqq
7-9 b: bbfjbbcbmsbvpglbh
1-11 m: mmmmmmmmmmmmmmm
15-17 x: xxxxxxxxxxxxxxxxvx
9-11 l: lllsldlllllljp
3-5 g: jgjnq
2-3 w: wgwz
4-5 h: jhfdpqqhsh
1-4 s: hrfxfxlx
3-5 r: kxrnsr
3-10 p: fpjppptppvpppp
5-12 m: dmclmfrmgbhlms
4-6 g: kdmmtgnxrgmgxggwmfd
4-10 f: xfshwrfrvx
1-3 v: dvmznrksd
7-18 n: xnsnnnnngnsnqjglwln
6-10 f: lffftlmfbfp
7-8 t: twjmbttjthpt
4-6 j: gjjltn
4-5 c: vfflxckkdh
10-15 b: kwcwcjtlsbbtfvbldglk
7-13 d: ddddddqddxddddd
1-4 w: wwwmw
4-8 d: lvddtrwzt
4-9 t: ttttztttt
5-6 k: kkrpkkkqtkffkwkk
1-3 f: kqfxxfb
3-6 g: ksgqlggb
11-12 f: ffffffdrffzf
10-11 b: jbbbbbbbbbbbb
16-17 s: sssssdssssssssskn
17-18 d: dmddddddddddddddrzdd
1-12 j: jvjjjqjcjtjj
2-4 b: npbbbkx
4-14 n: tnntfngpnbknnnnnrn
4-13 n: mnfsnnnnnnnnznn
6-10 s: sssssnssszsvs
8-9 m: mmxzpmhjj
2-4 k: pkgf
2-7 k: nkbtszkfzp
11-12 f: nxpbhffpzrff
5-14 x: czhvltwfxbxzsxzjtwxx
16-19 r: rrrrrrrrrrrrrrrrrrwr
2-4 m: mmmmvm
4-5 r: qrdrw
13-14 b: bbbhbbbbckbbpb
5-7 j: nwppmqkjxhtjf
8-11 z: zzwfwzbszzxzg
3-11 x: bxlfxjqxxgbwxxzcx
5-7 x: xxxxpxq
1-4 s: sssss
2-3 r: rvrr
6-7 b: bbbblkbzbbbnbbbbbj
1-3 g: gxgv
13-15 w: wwwwwwwwwwwwxwhww
3-4 c: rccc
4-15 p: cflwnhwfvntlxppmbg
7-12 m: xhmpvvmmmxhm
8-11 w: wmwwlwwcwdw
8-10 f: ghfcwzfffkfp
7-8 f: ffqcmdfww
3-4 z: qzjz
4-5 k: kkbqk
1-2 x: xqxczjtkfjt
2-17 h: hxhhhhhhhhhhhhhhhhhh
2-5 r: rrrmclqkcvkztr
10-13 q: fqgqqrgdxqfqq
8-9 j: jjjjjjdhjjj
6-7 q: sqqqhqvn
3-4 r: rrxw
13-15 j: jjjjjjjpjjjjjjx
4-6 v: rpvvvvrcfvqgfmsj
12-18 z: zzzzzzzzzdzjzzzdzn
8-10 n: ncnnnnmnnbhw
11-13 v: vvvvvvvvvvvvv
4-8 p: pdtpxpzw
5-10 z: zzqwxzmmfr
2-4 n: nknnn
3-4 c: dchb
10-17 h: lrpvfmmpwhgqphjphhhv
5-8 v: vrvmvvvnmvv
10-11 z: zzhzzzzzzzp
2-4 p: ppfpfp
4-7 z: zzzzzzjz
9-12 j: jjbwxjjjfjjwzmjc
12-17 f: fffffffffffdffffffff
5-7 t: dtlttvh
3-4 c: cmmnccv
1-8 j: tcjrqxjjk
10-14 h: vhhchthrhhhhhvhqhp
4-11 c: njrqmwpznxqtcc
1-15 g: xgdpwcqghrglgcgtggg
2-7 n: nkngnrnnqt
9-15 x: xxxxxsrxnxxfxxxxxxx
3-4 s: dsmf
4-5 r: rrrrcr
10-13 q: mqqqkqqqqzqqg
1-2 m: grtml
6-15 m: mmmmmfxmmftmmqm
15-18 g: ggjghfggvwgnhdggtb
1-5 k: ckkkfkqckqzk
4-5 h: kdllpjbn
2-4 b: jbgbf
5-8 v: vcvvqvvnhsz
8-9 m: fmmjmmmtm
4-6 l: lvhxdl
1-7 j: wjjjjjj
1-12 k: kkkkkkkkfkkpkkkkkj
3-5 r: rrrrr
3-4 x: vsqg
3-5 m: bszmmmcmnbdmhx
5-7 j: jjhfjjjk
9-12 v: nshvfvvwxvqv
10-15 v: dnthqhrpvsbznqdllwmg
8-9 g: jkgfzjgbcch
3-4 q: qqqw
2-3 m: mrcmmm
5-11 z: wzqzztfwzrz
1-4 p: zppf
3-4 l: dcvq
2-6 n: ngnnnnn
6-7 z: zczzznz
2-3 k: kglkkkjk
5-7 v: vvvgsbtfwk
2-12 q: qkgbwqjzqqqfqqqqqqqq
2-4 f: fpcq
17-18 b: bxtmblftbfbgbxbfdb
4-5 q: gqqjjz
10-11 l: llqllllllgl
2-4 r: jjrn
3-17 p: wfplgttzpngcvfzppw
2-3 v: vvmvt
10-17 k: kkkkkkktkxkkkkkkjkkk
8-9 z: pzdbjgbpzrxhhzc
3-12 z: blzpzxcqhvrsnvgml
14-15 q: qcffbpwbfqgxsqtrf
4-9 m: tthmftsxwrrmxx
2-3 r: zrrrr
7-14 l: blvhllgflllhcp
3-18 x: lplsnpshxmhsgmqdnr
12-15 f: rffdjffxfmffcfkff
11-12 q: qqqqqqqqqqqxq
7-9 b: bhbzrjfbvbbmgbbpkb
1-2 p: pppp
11-15 g: gtzgrghgwqgpqglx
1-7 t: tpttkxtptkgh
1-5 k: kkkkx
10-16 w: rthbwwqvcwggwpds
10-12 g: rpxxnxptslrgrpktg
5-8 h: hhhhhhhhhh
2-4 t: lthtsgbs
11-17 z: zzzzzzzzzzfzztzzzz
3-14 t: jttzstslpnvfftwmqqlq
4-10 l: tstfqpvlcl
6-16 t: cdtvtttrttwhmtvt
4-7 b: lbbwbbm
3-9 z: zrqbqzkdz
4-5 f: zlfsfzfgfzffpffff
1-4 m: jhmr
2-3 n: nnnvnnn
3-5 k: ktkjk
14-15 z: zzzzzzzzzzzzzzfn
12-13 m: mmmmmmmmmmmpmmm
3-4 s: spmssqbmnl
1-3 g: sgggggggfg
5-6 n: hnwnnd
7-11 r: rrrcrrvrrrrrrrrr
11-12 s: ssssssssssmw
2-4 n: rnvv
4-10 l: lmhplmllvdlnblmd
2-12 q: rbqwfbbqmsqfqfqqq
16-17 q: zqqqqqqqqqqqqqqnqq
18-19 p: dspfknrkgfxjdxvflbp
2-5 b: bbldb
3-4 k: kkfk
2-13 f: wfjhbcfrjfwxs
11-15 r: rrjrrrrrrrrrrrvrrrr
9-10 f: fffffffffhf
13-16 j: hsjjbjjpvvjsjrjsjz
6-8 l: ghlllffll
15-16 m: mvtxqmkfmfmbmvndm
4-5 h: zhhhhhh
3-4 x: mfzfnpcwxjxkhrrsszfc
17-18 d: qwdkqdsddddhdsxxwk
6-8 n: ngqnnnnzn
14-15 w: qwdbpsnwwwqwwww
10-13 h: hsrhnfxdhhxqb
2-4 k: kpjqgbpsq
12-13 x: xxxxxxxxxxxzrxxxxxx
7-10 j: jjjjjjbjjgk
11-15 q: mwqnxtrhwjqdqpz
2-9 b: cvcbxgxntx
5-7 x: xxdxxxc
4-7 d: dddtddkd
6-8 f: cnrfgfjn
3-4 h: ghhhh
12-15 z: mnqsvtxzclhzkzjz
5-6 m: gmdcmm
3-4 h: hhph
16-20 k: kkkkkkkkkkknkkkkkkkk
9-10 h: hhhhhhhhhhkhh
4-5 c: ccpcdf
6-11 l: lllllqlrljcl
9-12 z: zzzdzszzfzzn
9-10 b: bbbbbbbbfb
4-13 v: vvvcbvrvnvvvw
4-5 f: ffffv
4-6 m: mdmzdf
1-13 f: ffffffdffffsf
4-5 t: jttbtpttrttt
5-6 x: kxxxqb
3-5 t: twttpt
1-3 f: tfbd
1-7 w: fprwwwwwwwwwwzw
6-7 h: hhmhnkhhjhn
6-7 c: cpcwddc
6-8 q: ltsqwdqf
2-3 j: jjbjj
4-10 t: gtztntwkmt
5-6 d: xdwddddd
13-18 n: nnnnmnhzjrnnnlnnnrn
5-6 q: qqqqqqq
3-9 v: wvznrqpvvmhh
1-2 n: nbln
10-11 j: fsrjsvjjjwljzljsjpkj
1-4 n: cfnnf
13-16 j: qvlgjwhmsspdjgfxcl
2-6 k: kkkqkzh
1-6 f: ftcfff
12-16 g: ggggggggggggghgwg
4-14 w: hwwwpwwwbwwwww
3-14 c: cccccccccxccbwcccc
7-8 x: xxxxczsc
18-19 l: cplmllplhzbddwjlpvf
2-4 x: dxxxqr
5-8 w: vpxjwqwlfmzhbwwflj
3-6 v: vjlvvvvqqd
8-11 n: znnznnnnwnnn
9-10 c: ccccccccchc
3-12 l: hpljmhqcgfslm
4-5 s: dcqvxjczbxgxcrhksmvt
9-11 d: dddrnbfrfdhpndd
3-4 n: nssj
1-8 w: vwwwwwwww
7-12 h: hhhhhhhhhhhdhh
4-5 t: twtst
6-7 q: qrwqqqq
6-7 h: hghhnmbh
12-18 p: jvkpcjdkjssppmppjpp
4-5 s: ssslks
2-9 c: ccccccccccccccc
2-3 c: dvcvxcgpzjck
4-6 w: zmwnwlw
8-11 q: qqqqgqqqqqq
13-14 n: xfgnpvcwxmwfnrgnp
6-10 h: hhhhhhhhhhhh
3-6 z: gzcfwpkz
5-6 t: wtvhtttkmtttjt
7-16 f: fffwffffmfffffvf
6-10 d: lddddddddqg
3-5 t: dttttxlzlmwhd
8-12 w: wwwwwwwrwwwnw
6-7 v: spvcvvvpj
4-6 z: zzkzdzcwpzh
5-8 j: jjjjjjjzj
7-11 z: fxvhznzvzzz
9-12 s: sslksssscssrssvsvl
3-6 t: qtlwfw
10-11 l: vwssgxtszll
16-18 w: jvqrpdxlmjhwvdndtw
19-20 s: sssssssssxssssssssss
2-6 c: dzncll
15-17 f: qtlwcgtffxfrgflfcnv
3-4 p: qsjwvpbtjzpppqp
2-8 h: hzhhhhhth
3-4 g: rgdgggg
3-5 g: czzgkgbpns
6-7 t: tttttth
3-5 m: mvnmmmxzml
15-18 s: sswsssssszzssssssp
2-7 k: kzcrwpdjrtkkrgd
3-4 h: hshn
5-17 h: hrhhhhhhhhhhhhhhhhh
1-4 g: gcggglpfzgljnpstkngl
2-16 d: wbvwfvtdtjjnthkd
4-5 c: cmbccqtzjmnmcpjpwbkn
2-4 v: vjnvwnh
4-11 l: lllllllrllhllll
1-2 m: ltmmm
7-9 l: lslmlrbcsqll
16-19 q: qqqlqqqgqqqqrqqxtqfq
10-15 z: zwdzzdrsztsztrlz
11-12 g: ggvfgbgggmgg
8-9 d: dvjddddldd
4-5 g: wjrgmb
2-4 q: mqgq
4-6 j: jxjmjjfjxzx
1-2 l: ltvckkmlpkkll
4-7 v: djftvvdmv
4-5 p: ppppppp
6-12 z: jjxfvzzbmwmz
2-5 b: vpbnd
3-8 t: tttlthtntttt
4-6 r: xrrrrf
1-2 j: jjzqjjjjgs
3-4 c: ccczc
1-7 j: jjjjhdjjjj
3-6 k: jkfkkk
3-5 s: smssssnsl
5-11 d: tkqddsqhppmdkwwqvtdm
10-12 w: khrwhqwpcwww
15-19 t: ttttttttttttttpttttt
2-3 z: zrgz
14-17 p: gpzppppvjppppppppfp
15-17 p: ppvppppppppqppdpppzp
3-9 b: cbbpcbbbhbbbbnbbb
2-8 k: lvkstqvhssd
2-6 c: clcccccc
6-9 s: cgsssgsdw
1-4 p: pgpppp
9-16 z: zzzpmzzzxzzztzfz
14-15 j: jjjjjjjjjjjjjjtjj
5-9 b: rkctbdgbkcwvjxtz
13-16 d: dddddzddddkddddddddd
1-6 x: xlxxxhbgxfbmxzx
3-17 m: lbbsnfclmmctgfkvf
2-4 s: ssspss
8-12 w: wwwwwtwwgwwdww
2-4 t: ttgt
1-3 m: dmwjcbhlv
1-13 g: gggpghgcrggggntg
11-17 x: wxxxzxxtxxxxxxjxxxxx
14-15 j: jxjjhvxcdpbvjhknjrf
13-17 t: ttttttttttttttttpt
13-16 j: jjjjjjjjjjjjwjjjjj
7-9 w: wwwwwwhwm
3-5 w: rwwwc
4-5 l: zlltpl
2-4 j: nmbjjj
13-14 b: bqhbvsxbjvhchnnzbtb
2-3 k: cgtn
4-6 h: sfmjhnm
10-11 r: nrmcvgbdldn
2-6 r: rqrrrrr
14-18 r: rrrrrrrrrvrrrdrrrrr
10-11 g: jdgggcctgsg
9-14 f: stfflfrpjfffhxff
4-6 c: cccxcjcwc
13-17 w: rwwwwkwwwgwgswxfpwwc
7-9 g: ggggggcgrg
6-10 j: fjmjjjjdjkjmj
10-12 h: qswhkndjhqkh
4-12 z: zfzzzzzzzzkzzzzzzz
1-9 t: tqtttwtbxtgtzp
13-14 p: bppppppvpkpbppppp
7-11 m: phxfmmwmmwm
4-14 d: ddddddhdddddcbddd
1-6 l: mlllllll
6-13 z: nzzzztzznjcckznz
3-8 p: pppppppppppp
10-17 r: rrrrrrrrrdrrrrrrrr
15-18 j: bvswjgxvwdjcgdjqjjr
5-6 q: rqqkqq
7-15 k: kfkjsqlkzngkkvrmkzkv
2-6 p: gpwhqpbpgdrprbbp
1-7 x: rxxwxxxxxxrfxxfxqxx
14-15 x: xxxxxxfxxxxxxxxxgxxx
9-10 f: frskkfnffh
1-11 s: qsssssspsssss
4-11 g: zkxvrprgzxjcbg
11-14 g: ggggggggggggggggg
6-7 q: qqqqvqhq"""

values = values.split('\n')
correct_password = 0

for v in values:
    limits, letter, password = v.split(' ')
    min_lim, max_lim = limits.split('-')
    min_lim = int(min_lim)
    max_lim = int(max_lim)
    letter = letter[0]
    inside = password.count(letter)
    
    if inside >= min_lim and inside <= max_lim:
        correct_password += 1
        
print (' 2 - part 1: ' + str(correct_password))


### Day 2 - part two ###  
count = 0

for v in values:
    index, letter, password = v.split(' ')
    index1, index2 = index.split('-')
    index1 = int(index1) - 1
    index2 = int(index2) - 1
    letter = letter[0]
    if bool(password[index1] == letter) != bool(password[index2] == letter):
        count += 1
print(' 2 - part 2: ' + str(count))


### Day 3 - part one ###
print('''
--- Day 3 ---''')



# Repasar un Bool True != True/False, ¿por que tenemos que forzar a que sea bool?
# Devuelve 0 si no usamos bool, y devuelve otro valor si utilizamos or



values = '''...#..............#.#....#..#..
...#..#..#..............#..#...
....#.#.......#............#...
..##.....##.........#........##
...#...........#...##.#...#.##.
..#.#...#....#.....#........#..
....##.###.....#..#.......#....
.#..##...#.....#......#..#.....
............##.#...#.#.....#.#.
..........#....#....#.#...#...#
..##....#.#.#......#.........#.
#.#.........#..............##..
....##.##......................
....##..#...........#..........
..#..#.#........##....#......#.
..............#..#....#.....#..
.............#...#.....#...#...
.#...........#..........#...#..
.#......#.......#......#.......
#..#.............#..#....##.###
........#.#...........##.#...#.
......#..#.....##......#.......
.....#.....#....#..............
#...##.#......#......#...#.....
...........................#...
...#....................#.....#
..#.....#...#.....##.....#.....
....................#......#..#
.......#.....##......##....#...
#........##...#.....##..#...#..
........#..#.#......#..###..#.#
##.....#.............#.#....#..
..#.................#....######
.#.#..#.....#.#..........#.#...
.........#....#...#............
........#..#.....#.............
............#.#.............##.
...#....#..#......#............
.##....#.....#...#.#...........
..#..............#...........##
.....#.#.##...#................
..........#..#.#..........##..#
..#....#...#...#.....######....
....#.#..#........#....#.###...
.......................#.......
..#.....#.##................#..
.....#......#..#.....#........#
.#...###.......#.#.........#..#
............#..................
..#.........##.........##......
#...........#.#.......###.#....
.#...#.....#.........###.....#.
.#............#........#..#....
...##.#......##................
........#...#...#...#..........
.......#.##......##.#..........
....##.......#..#....#....#....
......#.........###........#...
#....#....####....##......#....
......................#....#.#.
...#.#.#....#.#...#...#......#.
......#.....##.#...........###.
#........#.........##......#.#.
....##.....#.....#..#..........
......#...#...#.........#...##.
..#........#..................#
.........#..##.#..#..#...#.#..#
.....#.....#...#.....###.....##
.............#....#...#........
..........#.#.#...#..#...#....#
#...............##.......#.....
#...#.............#..#...#....#
..#...#...##...##...#..#.......
..#..#........#.#...........#..
.....#.....#..................#
....#....##....###..###...##...
..#......###.........##....#.##
.......#.##...#.......#..#.....
...#.#.#.#.....##..#..#........
................##....#.#......
..#...#...#...#.....##.#...#..#
..#..#.....#..##....#....#.....
.###...#......#........#.....##
##......#..#........#..........
....#...#..#....##..#......####
.#.....##....#..........#......
.#...#....#.........#...#....#.
.....#..#.#..#......#..##....#.
...#.##...#...#........#......#
.#..#...#.#..#.........#...#...
#....#......##.....#.......#...
..##............##..#.#.#...#..
##.......#.......##............
#......#.##........#...#...#...
.#.#.......##.........#..#.#...
.............##.#........#.....
.#..#...###...#..#.............
.....#...#..#....#.......#.....
#.#.........#.#.#...#...#.#....
.....#.......#.##.##...#....#..
.#.##..#.....#...#.#.#.#.#..#..
..........#...................#
.....#.#.#...##.........#..#..#
.#..#....##......#...#.........
.##......#......#...#........#.
.....##.#......#............#.#
.#.....##..#...........##......
.....#......#.......##....#....
..#..##..........#.#..........#
#.#.......##..#..##.#....#.....
.......#..#.#.......##......#.#
....#...##...#..............#..
.....#.........#......#...##...
#.........#........##..#.....#.
.#.#..#.....##.......#......#..
........#..#....#.....###..#...
#.#..#.#..........#............
..#......##..#....#.........#..
#..............................
.......#............#..#..#.#..
.#.....#.#....#..#.##.#........
.......#.###.#........##.#..#..
..............#....#.....##.#..
#..............#....#.###......
.#..#..#...###............#...#
.#.##...#....#..#...#...#......
......##..#..#......#..#....#..
.........#.......##............
...........##...#..#....####...
.#..................#..........
#...#..#..................#....
..............#.....##.....#...
..#.#..#...##..#.....#.....#..#
....#....#.#.........#.....#...
.#.......#...#....#...#.#..#..#
#.........##.....##.......#...#
#..#............#....#........#
..........##...#......#....#...
.......#..##...............#...
#............#.#.#.....#.......
.#........##...#...............
..##....#.....#..#.##.#......#.
.#...#.............#...#.....#.
...##....#.......#......#.#..#.
#......................#..#.##.
...#..........#..#.........#...
..#......#.......#.#....#......
....#............#...#......#..
.....#..#..##...#...#.........#
.....#......#....#....#........
.............#..#..........#...
....#..............#.....#.#...
....#.................#.#...#.#
.........#.#...........###.#.##
#...........#..##.#....#.##.#..
#.#.....#......................
##.#.........#....##.#.#..#.#..
#..........#.#.#.#.#..#..##..#.
..#...#..###.........#......#..
.....#......#..#.#............#
...........#...#.#.#.###....#..
#....#..#.......##.#.......##..
..............#.....##.#.......
.#.....#.#..#.........#.#.#..#.
..#..#..#..#................#..
...........#..#.#...#.........#
.#..#..#...#........#...#.#..#.
...#.#..#......#..#............
........#......##.....#....#...
#...#......##.#.#..............
.#........................#....
#.#.....#.##.....#..#.#........
#..........##.#.......#....#..#
#...#..#..#.....#....#....#....
#...........#..#.#....##.##....
##......#..#........#.......##.
#........#..#...#..........#...
...#...#......##....#.#........
...##..#..#.##....#...#........
#.#..#....#...#........#.......
..........#.......#..........#.
......##...#....###...#....#...
........#..#.....#......#......
....#.........##...#..##......#
....#...........#.#..#.#.#.#..#
..#......#..#......#........#.#
#..#....#.....#.............#..
............................#..
#...#.#.....#...#....#....#....
........#...#...#...#...#......
.###........#....#.##.....##.#.
.........#.....#..........#....
.#.........#....##.#.....#.....
#..#....................##.#...
..##.#.............#....#.#....
..#.#........#............##.#.
#........#...##.....#...#.....#
.........#.#..........#....#..#
...###.#..#.#......#.#.....#...
......#.....#..#...#........#..
.......#...#.....#....#....#..#
.#.#........#......##.......#..
#.................###..........
#........#.#..#....#..#........
..##....#.#...##...#...##....#.
...#.#......##...#.....#..#....
#..#........#...###....#.......
##.#....#..#.#..........#......
....#...###...#.....#........#.
..#.#........#....##.#.........
......##.##.................##.
.#....##...#.#..#.#............
.#...###........#......#.......
##..#.#......#..#..#...#.......
.......##..#....#........#....#
......#..........#.............
....##..##..#......#.#.........
.....#....................##...
...###.....#.....#...#.#.##.#..
....#.#..#.......#..#......##..
.......#.#..#.##.#...#......#..
...#.#....#.#...#..##...#...#..
#.##...#....#..#.............#.
...#...#...#.......#..........#
.#..#.............#..##.#......
....#.......#..............#.#.
..................#..#.....##.#
.#...#..#......#..........#...#
..#.#.....#..#....#....#####.#.
.......###.......#....#....#...
......#.#........#...#.........
......#..#.#.#....#.#.#....##..
.#...#.#...##.#......#.........
#....#..##....#.#.......#....#.
..##.#.....#.....#.........#...
......#......#....#....#.....#.
...##.....#....#......#......#.
......#......##............#.#.
.##.#.......#....#...#....#....
....#..#..#...##.......#..#....
....#....#...#.#........#..#...
....#.....#..........#..#......
....#....#...#.....#..##.....#.
##...#..##......#....##..#..#..
.....##.##..............##.....
#.#....#.##..#....#...##.......
..#.....##.....#.....######...#
...#.....#.#.#......#......##.#
...........##.............#....
...##......#..#......#...#.....
....#.##......#..#....#.#..#...
.#..#....#...#..#.....##.......
.....#..#.................#..#.
................#..#...#......#
...##....#.....#..#....##......
....##...............##...#....
......#..........#..##.........
.......###.......#.........#..#
......................#....#.#.
#.#.....#...##............#....
........#......##......#.....#.
...#....#....#.#..##.#..#.#.#..
..#.#....#.##...#..#.....#.#...
............#....#..#.......#..
#...#...#.#......#...##.....#.#
......#....#....#.......#......
....#.......#..........#....#..
........#####........#....#....
......#....##..............#.#.
....#....#.......#.......#.....
.##.#....##....#...............
#.....##........#..#.#...#.#...
...#......##....#..............
.#.....#.....#.......##....##..
#....#..........#.#..#.........
......##..........##.......#...
.##......##.....#.#....#......#
....#......................#...
.#...........###........#...#..
#.#..#..#..#...##.#....#.#..#..
...##...........#.#..........#.
......#.#..#....#....#.........
....#....#.#......#.........##.
.#..#...#...##....#...#......#.
#.#......#...#.#.#...........#.
##.....#..........##....##..##.
...#.#.....#..##........#......
..#........##........#..#......
.......#...............##..#...
.......#.#....#..###...........
.............#........#...#....
#.................#......#..#..
...#....#..#..............#...#
.............#....##....#..##..
#........#..........##...##...#
............#....#.....#.#....#
.....#..............##..#...#..
..#....#......###....#.#...##..
....##......#.....#....#.......
.....#...............#.....#...
.#.....#.....#..............#..
#................#..#..........
.##....#....#.....#............
#.####...#..#..#....#..........
..##........##.....##......#..#
......#.....#...##.........##..
....##..#.....#.#.........#...#
.....##..#....#....#.#...#..#..
...#............#...........#..
.......#.#..#.#.#..#........#.#
....#.#........#.#.#..#...#...#
..#....#....#..#......#........
.#...........................#.
.#..#....####........##......#.
.#.....#..#.#.................#
.#..#...........#...#....#...#.
......##..#........#..#....#...
..#.............#....#........#
#.#..........#.##.......#.#..#.
..#....#...#...............#...
..............#..........#..#..
..#.....#.#.....#...#...#..#...
.........#...###.#...#........#'''

values = values.split('\n')

col = 0
tree = 0

for i in range(len(values)):
    if values[i][col] == '#':
        tree += 1
    col = (col + 3) % len(values[0])

print(' 3 - part 1: ' + str(tree))


### Day 3 - part two ###  

def slope(right, down):
    col = 0
    tree = 0
    for i in range(len(values)):
        if i % down != 0:
            continue
        if values[i][col] == '#':
            tree += 1
        col = (col + right) % len(values[0])
    return tree

tree = slope(1,1) * slope(3,1) * slope(5,1) * slope(7,1) * slope(1,2)
print(' 3 - part 2: ' + str(tree))
    

### Day 4 - part one ###
print('''
--- Day 4 ---''')

values ='''ecl:hzl byr:1926 iyr:2010
pid:221225902 cid:61 hgt:186cm eyr:2021 hcl:#7d3b0c

hcl:#efcc98 hgt:178 pid:433543520
eyr:2020 byr:1926
ecl:blu cid:92
iyr:2010

iyr:2018
eyr:2026
byr:1946 ecl:brn
hcl:#b6652a hgt:158cm
pid:822320101

iyr:2010
hgt:138 ecl:grn pid:21019503 eyr:1937 byr:2008 hcl:z

byr:2018 hcl:z eyr:1990 ecl:#d06796 iyr:2019
hgt:176in cid:75 pid:153cm

byr:1994
hcl:#ceb3a1 hgt:176cm cid:80 pid:665071929 eyr:2024 iyr:2020 ecl:grn

cid:280 byr:1955 ecl:blu hgt:155cm hcl:#733820
eyr:2013 iyr:2011 pid:2346820632

hcl:#4a5917 hgt:61cm
pid:4772651050
iyr:2026 ecl:brn byr:2015 eyr:2026

iyr:2019 hcl:#a97842 hgt:182cm eyr:2024 ecl:gry pid:917294399 byr:1974

ecl:#9c635c pid:830491851 hgt:175cm cid:141
iyr:2010
hcl:z
byr:2026 eyr:1998

byr:1927 iyr:2011 pid:055176954 ecl:gry hcl:#7d3b0c eyr:2025 hgt:166cm

hcl:#733820 byr:2008 ecl:utc eyr:1920 pid:159cm hgt:66cm iyr:2030

pid:027609878
eyr:2022 iyr:2012
byr:1960 hgt:157cm
hcl:#b6652a
cid:117
ecl:grn

iyr:2025 pid:7190749793 ecl:grn byr:1984 hgt:71in hcl:c41681
cid:259 eyr:1928

eyr:2029 pid:141655389 cid:52 hcl:#cfa07d iyr:2019
ecl:blu hgt:69in byr:1938

eyr:2020 hgt:166cm
ecl:gry
pid:611660309 iyr:2011
hcl:#623a2f byr:1943

hgt:190cm eyr:2022 byr:2000 cid:210 pid:728418346 hcl:#a97842 ecl:xry iyr:2015

byr:1973 eyr:2028 iyr:2012
hcl:#ff0ec8 pid:740554599 ecl:amb cid:58 hgt:155cm

iyr:2016 pid:922938570 ecl:oth hcl:#fffffd hgt:154cm eyr:2021 byr:1966

ecl:amb
byr:1929
hcl:#c3bbea pid:511876219
iyr:2019
hgt:191cm
eyr:2026

ecl:utc hgt:155cm pid:#9f0a41 iyr:2012 hcl:#bd4141
byr:1998 eyr:2020

ecl:grn hgt:173cm cid:321 pid:851120816 byr:1968 hcl:#a97842 eyr:2027
iyr:2014

hgt:155cm hcl:#f40d77 pid:038224056 byr:1953 ecl:brn iyr:2014
eyr:2022

pid:181869721
iyr:2011 hgt:151cm hcl:#733820 cid:110 ecl:blu
byr:1931 eyr:2024

byr:1948
hcl:#888785
hgt:74in
cid:112 ecl:hzl pid:921761213 eyr:2028
iyr:2015

ecl:gry
byr:1931
pid:600127430 hcl:#341e13 eyr:2027
iyr:2013 hgt:173cm

hgt:178cm pid:530791289 hcl:#6b5442
eyr:2022 byr:1979 iyr:2014 ecl:hzl

pid:412193170 hcl:#cfa07d hgt:186cm iyr:2012 cid:284 eyr:2020 byr:1967
ecl:grn

hcl:#6b5442
iyr:2015 pid:808448466 ecl:blu eyr:2022 hgt:159cm byr:1969

eyr:2020
iyr:2019 hgt:170cm pid:8964201562 hcl:#6b5442 byr:1947 ecl:amb

eyr:2029 ecl:hzl hcl:#866857 byr:1961
iyr:2017

ecl:#3456ba eyr:2013 iyr:2020 pid:378280953
hcl:z hgt:174cm

hgt:172cm
cid:202 ecl:oth eyr:2021 byr:1980
iyr:2012
hcl:#cfa07d pid:605707698

cid:281 hgt:161cm iyr:2017 pid:122936432 hcl:#602927 byr:1981 ecl:gry eyr:2021

byr:1959 hgt:193cm pid:083900241 iyr:2020 eyr:2037 hcl:#623a2f
ecl:hzl

iyr:2030 hgt:153cm eyr:2022 hcl:#efcc98 cid:131
byr:2016 ecl:hzl pid:64053944

hgt:172cm eyr:2025
hcl:#866857
byr:1938 ecl:dne
pid:192cm iyr:2014

pid:016297574 cid:152 iyr:2015
eyr:2024 hcl:#341e13 byr:1965 hgt:175cm
ecl:oth

pid:604330171 cid:125 byr:1974 hgt:160cm iyr:2014
eyr:2022 ecl:oth hcl:#6b5442

pid:59747275
byr:2027
hgt:145
hcl:1fd71f iyr:1944 eyr:2037 ecl:brn

iyr:2010
eyr:2021 byr:1953
pid:7098774146 ecl:brn hcl:98737d hgt:158cm

hcl:#602927 eyr:2039 pid:#81a5a1 iyr:2012 cid:67 byr:1951
ecl:#6551f5 hgt:76cm

hgt:170cm ecl:oth
cid:235 eyr:2022
byr:1929 iyr:2019
hcl:#341e13 pid:797557745

iyr:2011
hcl:#733820
eyr:2022 pid:830183476 ecl:blu byr:1976 cid:157 hgt:75in

hgt:164cm ecl:amb pid:653425455 hcl:#623a2f byr:1977 eyr:2020
iyr:2013

byr:2009 eyr:1953 hgt:178cm pid:#5d02f0
hcl:#a97842 iyr:2016
ecl:amb

pid:009643210 eyr:2036 ecl:zzz
cid:97 hcl:32e540 byr:2005 hgt:187cm iyr:2021

pid:155cm
iyr:2022 byr:2024 eyr:2031 ecl:amb cid:79
hcl:#cfa07d hgt:69cm

cid:176 ecl:oth
pid:688645779 byr:1933 eyr:2026 hgt:69cm
iyr:2016 hcl:#888785

hcl:#888785
eyr:2027
iyr:2020 pid:802243213 ecl:brn
hgt:179cm byr:1976

hcl:#6cad3e hgt:164cm byr:1982 iyr:2020
ecl:gry
pid:142160687 eyr:2023

hcl:#18171d
hgt:153cm
iyr:2014 ecl:hzl cid:231 pid:167809118 byr:1997 eyr:2028

byr:1940
ecl:hzl iyr:2016 cid:67 hcl:#c800da
pid:563956960 eyr:2021
hgt:189cm

pid:133094996 eyr:2032 hgt:60cm hcl:#623a2f byr:2030 ecl:dne iyr:2023

pid:65195409 hcl:d0d492
iyr:1956
byr:2019 ecl:#bb043f eyr:2031 hgt:167in

iyr:2016 byr:2006 ecl:#35d62f eyr:2029
hgt:186cm
hcl:1d8307

eyr:1935 iyr:1960 pid:346667344 ecl:grn hgt:170cm hcl:cfcc36

ecl:oth byr:1979 pid:165581192
hgt:177cm
hcl:#c0946f
iyr:2011

iyr:2011 eyr:2030 pid:250840477
byr:1934 cid:174 hgt:179cm hcl:#866857
ecl:blu

hgt:157cm hcl:#7d3b0c eyr:2027 pid:979510046
ecl:oth

iyr:2025
hgt:69
ecl:grt byr:1935
eyr:1928 pid:168cm
cid:271 hcl:z

pid:998166233
iyr:2020 hgt:166cm ecl:amb byr:1995 hcl:#fffffd

hcl:#ceb3a1 ecl:amb
iyr:2019
eyr:2024 hgt:184cm byr:1980 pid:839215481
cid:146

byr:1967
pid:444303019 ecl:oth hgt:150cm eyr:2024

eyr:2023 byr:1960 iyr:2010
cid:236 hcl:#733820 pid:900635506
hgt:69in
ecl:hzl

eyr:2029 pid:969574247
hgt:150cm byr:1967
iyr:2010 ecl:blu

pid:575879605 iyr:2010
ecl:hzl
byr:1963
hgt:151cm
hcl:#c0946f cid:277

byr:1998 pid:621374275
ecl:brn hcl:z iyr:2029
eyr:2024
hgt:68cm

pid:365407169 ecl:amb hcl:#87f433 iyr:2011 eyr:2021 byr:1987
hgt:175cm cid:201

hgt:175cm iyr:2020
ecl:gry
eyr:2029 pid:806927384 cid:59
byr:1932 hcl:#888785

pid:589898274 cid:113 hcl:z hgt:184cm eyr:2000
ecl:lzr iyr:2016 byr:2016

ecl:#2bafbb
eyr:2038 iyr:2027
hcl:#fffffd
hgt:174 byr:2007
pid:093750113

eyr:2022 hgt:59in
hcl:#ceb3a1
pid:159921662 ecl:gry
byr:1948 iyr:2014
cid:50

hgt:190cm
iyr:2014 pid:480507618 hcl:#fffffd byr:1945 eyr:2029

byr:1951 hgt:152cm ecl:brn iyr:2016 eyr:2029 cid:179 pid:027575942
hcl:#fffffd

cid:198 pid:728480773 eyr:2028 hgt:153cm iyr:2018
hcl:#888785 ecl:amb byr:1983

byr:1968 hcl:#c0946f ecl:grn eyr:2027
iyr:2013 pid:269749807
cid:227
hgt:178cm

eyr:2024 hgt:185cm ecl:oth
hcl:#448ace byr:1987 iyr:2018 pid:454243136

byr:1930 ecl:grn iyr:2018 hgt:158cm
hcl:#341e13 eyr:2021

eyr:2024 cid:194 pid:425431271
hgt:169cm ecl:grn byr:1973
iyr:2014 hcl:#fffffd

ecl:grn cid:110 iyr:2013 hcl:#18171d
hgt:155cm eyr:2024 byr:1962 pid:522435225

byr:1934 ecl:hzl hgt:152cm iyr:2018
eyr:2024 pid:079740520

ecl:grn eyr:2023 hcl:c3f119 pid:468039715 iyr:2013 hgt:150cm byr:1955

pid:809357582 eyr:2025 byr:1958
hcl:#6b5442 iyr:2013
hgt:161cm ecl:hzl

hcl:#b6652a pid:068979430 byr:1960 iyr:2010 ecl:grn hgt:159cm eyr:2021

cid:105 pid:495292692 byr:1965
hcl:#ceb3a1 hgt:160cm ecl:amb
iyr:2020

iyr:2010
eyr:2024 byr:1941 ecl:grn hcl:#b35770 hgt:171cm cid:132 pid:975699036

pid:767448421 hgt:186cm hcl:#733820
byr:1972 iyr:2020 eyr:2026 ecl:grn

pid:036236909 iyr:2012
hgt:181cm hcl:#888785
eyr:2026
ecl:hzl byr:1936

hgt:173cm
byr:1923 ecl:blu
eyr:2026 pid:570818321
hcl:#733820 iyr:2016
cid:59

pid:2711059768
byr:2024
cid:139 ecl:blu hcl:z hgt:60cm

eyr:2025
pid:671193016
byr:1950 hcl:#6b4b25 iyr:2017 hgt:158cm ecl:blu

hgt:175cm iyr:2015 ecl:amb
byr:1984 eyr:2026 pid:342782894
cid:140

iyr:2019 eyr:2027 byr:1972
pid:196266458
hgt:158cm hcl:#7d3b0c cid:69

pid:604018034 iyr:2016 ecl:brn eyr:2028 hgt:172cm hcl:#6b5442 byr:1922
cid:238

eyr:2024 ecl:gry byr:1970 pid:356551266 cid:340 hgt:162cm iyr:2013

ecl:amb
hgt:151cm hcl:#18171d byr:1921 pid:187276410 eyr:2030 iyr:2015

eyr:2030 pid:056372924 hcl:#d236d9 hgt:156cm
iyr:2014 ecl:blu

iyr:2014 eyr:2028 byr:1991
hcl:#b6652a pid:119231378 hgt:155cm ecl:blu
cid:77

hcl:#341e13
eyr:2027
iyr:2012 ecl:grn hgt:152cm pid:405955710 byr:1970

iyr:2013 hgt:180cm eyr:1978 ecl:amb byr:1929 pid:3198111997 hcl:z

pid:32872520 ecl:#8a0dd4 iyr:1955 eyr:2036
byr:2027 cid:133 hcl:z hgt:184in

hgt:152cm pid:402361044
hcl:#efcc98 eyr:2029 ecl:grn iyr:2014
byr:1960

byr:1972 eyr:2026 pid:411187543 iyr:2014
hgt:184cm cid:211 hcl:#866857 ecl:brn

ecl:brn
hcl:#efcc98
pid:311916712
byr:1957 hgt:151cm eyr:2020 iyr:2020

iyr:1968
hcl:a28220
pid:#ed250d cid:240 eyr:2031
hgt:181cm ecl:xry

ecl:grn byr:1946 hgt:172cm iyr:2010 hcl:#b6652a pid:372011640 eyr:2026

ecl:brn
eyr:2026 byr:1980 hcl:#c0946f
hgt:151cm pid:153076317 iyr:2012

byr:1966 pid:852999809 ecl:oth
hgt:163cm
iyr:2014 eyr:2029 hcl:#341e13

ecl:blu
byr:1959 hgt:191cm pid:195095631 iyr:2016 hcl:#ceb3a1 eyr:2028

byr:2001 ecl:gry hcl:#888785 iyr:2018 hgt:177cm pid:576714115

iyr:2017
byr:1949
ecl:blu hgt:186cm cid:289 pid:859016371
hcl:#ceb3a1 eyr:2021

byr:1999 hcl:#b6652a eyr:2023
hgt:175cm
ecl:gry iyr:2013 cid:165 pid:194927609

hgt:70in eyr:2027 ecl:brn iyr:2012 pid:162238378 hcl:#ceb3a1 byr:1986

hgt:63in ecl:xry
byr:2011 iyr:2024
hcl:5337b0

hcl:#341e13 eyr:2029
hgt:184cm ecl:amb iyr:2012
byr:1970

byr:1920 pid:472914751
eyr:2028
hgt:187cm hcl:#cfa07d cid:290 ecl:gry

byr:1948 ecl:gry eyr:2025 hgt:151cm cid:276 hcl:#6b5442 pid:937979267
iyr:2016

byr:1934
pid:626915978 hcl:#623a2f hgt:167cm ecl:gry
iyr:2020 eyr:2023

byr:1949
hgt:68in eyr:2027 iyr:2019 hcl:#733820 ecl:brn cid:237
pid:057797826

pid:155cm
hgt:68cm ecl:lzr hcl:z cid:344 eyr:2028 iyr:2020 byr:2017

byr:1959
hcl:#341e13 eyr:2022
iyr:2019 pid:728703569
hgt:167cm
ecl:oth

ecl:grn
eyr:2024 byr:1999
pid:566956828
iyr:2015 cid:293 hcl:#602927 hgt:192cm

byr:1939
ecl:xry pid:929512270 hgt:66in iyr:1939 eyr:2030 hcl:#efcc98

eyr:2026
iyr:2014
pid:176cm hcl:#fffffd
ecl:gry
hgt:151cm byr:1933
cid:256

ecl:oth eyr:2025 iyr:2017 hgt:159cm pid:055267863 cid:55 byr:2001 hcl:#cfa07d

eyr:2029 byr:1954 ecl:hzl cid:123 iyr:2020 hgt:192cm hcl:#866857
pid:225593536

pid:320274514 cid:289 byr:1963
eyr:1942
ecl:gmt hcl:z hgt:167in iyr:2022

byr:2013
ecl:gmt
iyr:2011
hcl:#733820 pid:#e7962f
hgt:178cm eyr:2029

pid:154cm ecl:hzl
eyr:2035 byr:2023 cid:104 iyr:2026

eyr:2024 ecl:hzl hcl:#7d3b0c iyr:2010
pid:105864164
byr:1955
hgt:163cm

eyr:2021 hgt:151cm
iyr:2017 hcl:#c0946f
ecl:amb
cid:150
pid:296798563
byr:1953

iyr:2012
byr:1990 hcl:#341e13
pid:189449931 eyr:2024 hgt:64in

hcl:z cid:79 byr:2028
eyr:2028 pid:886152432
ecl:#ce0596 hgt:178cm
iyr:2029

ecl:brn
iyr:2019 hgt:151cm
hcl:#341e13
byr:1969
pid:468846056
eyr:2022

ecl:grn hgt:157cm iyr:2012
eyr:2020
hcl:#b6652a cid:338
byr:1954 pid:153867580

iyr:2011
eyr:2027
byr:1935
hgt:151cm
ecl:blu pid:802665934 cid:276 hcl:#623a2f

hcl:#efcc98 eyr:2026 ecl:amb
iyr:2014 pid:320160032
hgt:157cm
byr:1976

eyr:2021 cid:172
iyr:2012 ecl:oth hgt:187cm
pid:432856831 byr:2001 hcl:#733820

eyr:2028 ecl:amb hcl:#efcc98
iyr:2020 byr:1954 hgt:153cm

byr:1930 ecl:brn hcl:#fffffd
pid:458840035 hgt:178cm eyr:2021
iyr:2011 cid:336

pid:216876576 hcl:#341e13
eyr:2028 iyr:2018 hgt:177cm byr:1938
ecl:brn cid:214

byr:2029 eyr:1987
hgt:75cm pid:193cm hcl:#b6652a cid:246 iyr:2028

ecl:hzl hgt:151cm hcl:#7d3b0c
eyr:2030 pid:910999919
iyr:2019 byr:1956

byr:1950
cid:95 iyr:2013 ecl:grn
eyr:2020 hcl:#623a2f
pid:603817559 hgt:159cm

pid:913791667
iyr:2018 byr:1959 hcl:#a97842 hgt:179cm eyr:2029 ecl:gry

hgt:71in
ecl:blu eyr:2028
hcl:#18171d byr:1937 iyr:2011 pid:951572571

hcl:#b6652a iyr:2015 hgt:170cm ecl:blu cid:292
byr:1977 pid:475457579 eyr:2020

ecl:amb eyr:2029
pid:530769382 iyr:2018 cid:53
hgt:63in
byr:1954 hcl:#07de91

hcl:#cfa07d hgt:185cm
byr:1929 iyr:2011
eyr:2027

iyr:2019 ecl:oth byr:2023 hcl:#341e13 pid:879919037
eyr:2030 hgt:174cm

hcl:z hgt:182cm ecl:grn iyr:2010 eyr:2020 pid:2063425865
cid:182
byr:2019

byr:1930 hgt:185cm pid:412694897 eyr:2025 ecl:brn iyr:2020
hcl:#a97842

hgt:150cm byr:1955 eyr:2020 cid:149 pid:597600808
hcl:#ceb3a1
ecl:hzl

pid:209568495
eyr:2026 byr:1928 hcl:#341e13 hgt:183cm ecl:brn iyr:2011

pid:723789670 ecl:blu iyr:2013 byr:1933
cid:239 hcl:#7d3b0c eyr:2026 hgt:151cm

byr:1978 eyr:2027 hgt:164cm
pid:009071063
hcl:#602927 iyr:2014 ecl:blu

hcl:#18171d ecl:grn hgt:154cm cid:154 iyr:2016
byr:1952 pid:730027149 eyr:2024

eyr:2025 hcl:#888785 iyr:2013 cid:90
byr:1975 ecl:grn
pid:619198428 hgt:161cm

ecl:gry iyr:2013 pid:795604673 cid:198 byr:1962
hcl:#6b5442 hgt:64in eyr:2021

hcl:#ceb3a1 ecl:oth iyr:2015
eyr:2021 pid:920586799 cid:302 hgt:60in
byr:1964

eyr:2021 ecl:gry iyr:2019
hcl:#6b5442 hgt:192cm
byr:1996
pid:692698177

ecl:grn pid:141369492 byr:1956 eyr:2028 hcl:#6b5442 hgt:190cm iyr:2014

hcl:#6b5442
ecl:grn iyr:2020 hgt:153cm
pid:312738382 eyr:2028
byr:1985

byr:1979
eyr:2021 ecl:gry hgt:175cm pid:787676021 cid:81 hcl:#b6652a iyr:2012

cid:80 hgt:188cm byr:1964 pid:105773060 iyr:2014 hcl:#733820 ecl:gry eyr:2028

byr:1960 pid:251870522 iyr:2018 hgt:168cm ecl:blu hcl:#c0946f eyr:2026

cid:270
pid:#5661f0 hgt:182in
ecl:dne
byr:1930
hcl:z iyr:2026

hcl:#888785 byr:1954 pid:170544716 eyr:2028 hgt:162cm cid:244
iyr:2014
ecl:grn

iyr:2017
hgt:69in
ecl:hzl
pid:544135985 hcl:#ceb3a1 eyr:2020

hcl:92d4a1 iyr:2018 pid:178cm
cid:347
hgt:97 eyr:2017
ecl:gmt byr:2004

ecl:oth iyr:2018 hcl:#fffffd byr:1999 pid:853396129
cid:119 eyr:2026 hgt:178cm

hgt:69in
hcl:#fffffd eyr:2026 byr:1922
iyr:2010 ecl:oth pid:664840386

hgt:178cm
byr:2000
iyr:2013 hcl:#cfa07d
eyr:2028 pid:842454291
ecl:amb

ecl:hzl
hcl:#733820 pid:316835287 byr:1998
eyr:2024
iyr:2015 hgt:165cm

pid:684064750 byr:1928 ecl:gry iyr:2015 cid:343
hgt:189cm
hcl:#4c6cb4 eyr:2020

byr:1923 hcl:#a97842 eyr:2024 ecl:gry
pid:095911913
hgt:185cm iyr:2010

ecl:hzl
byr:1996
eyr:2023
hgt:177cm
hcl:#b6652a pid:011541746
iyr:2011

hcl:#efcc98
iyr:2014 ecl:oth byr:1942 pid:730960830
hgt:183cm
eyr:2025

byr:1939 eyr:2029 ecl:amb hcl:#fffffd
hgt:188cm pid:732730418 iyr:2013 cid:313

hgt:164cm cid:217 byr:1985 hcl:#888785 eyr:2020
iyr:2014 ecl:oth
pid:071172789

eyr:2024 pid:215897274 ecl:#c67898
byr:1972 hcl:#866857 iyr:2010 hgt:170cm cid:310

ecl:hzl pid:030118892 byr:1941 hgt:158cm hcl:#b6652a
eyr:2029 iyr:2012

ecl:gry hcl:#c0946f hgt:166cm pid:604313781
byr:1924 eyr:2023 iyr:2020

hcl:#602927 hgt:168cm eyr:2027 ecl:brn
pid:764635418 byr:1968 iyr:2010

pid:157933284
ecl:grn
eyr:2030 byr:2000
hgt:81 hcl:z

hcl:#ec24d1
pid:647881680 byr:1922
hgt:178cm iyr:2020 ecl:amb eyr:2021 cid:94

ecl:hzl byr:1971 iyr:2018 pid:975690657 eyr:2027
hgt:192in
cid:202 hcl:#c0946f

pid:678999378
hgt:61in
byr:1981 hcl:#cfa07d eyr:2029 iyr:2014
ecl:oth

eyr:2022 iyr:2012 ecl:grn pid:883419125
hcl:#ceb3a1
cid:136 hgt:75in
byr:1952

iyr:2018 hgt:185cm
byr:1985 pid:119464380 eyr:2028 hcl:#623a2f ecl:gry

eyr:2025 hcl:#ceb3a1 byr:1953
cid:277 hgt:164cm iyr:2010 pid:574253234

cid:252 ecl:amb pid:594663323
hgt:75in hcl:#cfa07d iyr:2019
eyr:2026 byr:1964

iyr:2026 hcl:z pid:60117235 ecl:lzr
byr:2016 hgt:156in eyr:1994

pid:448392350
eyr:2022 hcl:#a97842
hgt:157cm
ecl:hzl
iyr:2018 byr:1973

ecl:brn
byr:1951
eyr:2028
hcl:#7d3b0c iyr:2018 hgt:164cm

hgt:156cm
byr:1963
iyr:2014 eyr:2020 ecl:blu hcl:#ceb3a1
pid:#a87d16

pid:447170366 ecl:blu hcl:#888785
iyr:2012 cid:236
hgt:167cm
eyr:2022 byr:1942

hcl:#623a2f
eyr:2020 iyr:2017 cid:128 ecl:amb pid:279550425
byr:1983 hgt:154cm

byr:2014 eyr:2034 hgt:176in hcl:z
ecl:#d4e521
pid:3629053477 cid:177
iyr:1970

pid:30370825 byr:1966 eyr:2026
iyr:2026 hcl:#866857
cid:346 ecl:#f7c189

iyr:2010 pid:271066119 eyr:2023 hcl:#efcc98 hgt:179cm byr:1956

byr:1966 hgt:156cm pid:977897485 cid:287 iyr:2011 hcl:#b6652a ecl:amb eyr:2029

cid:211 ecl:gmt byr:2017
hcl:z eyr:2029 hgt:180in iyr:2021 pid:81920053

byr:2019
pid:5229927737 hcl:75b4f1 hgt:146 iyr:2026 ecl:#92cf7d eyr:2032

eyr:2027 pid:604671573
ecl:hzl
hgt:189cm byr:1979
hcl:#efcc98 iyr:2020

iyr:2018 cid:192
eyr:2029 ecl:grn
pid:653764645 hgt:179cm
hcl:#341e13 byr:1927

byr:2012
iyr:2015
hcl:#b6652a
pid:168500059 eyr:2038 cid:234 hgt:191cm ecl:zzz

ecl:gry hcl:#623a2f byr:1925
iyr:2016
eyr:2028 cid:157
hgt:154cm
pid:196280865

cid:319 pid:928322396 ecl:gry
byr:1949
eyr:2028
hcl:#341e13 hgt:171cm
iyr:2018

byr:2023
iyr:1953 hgt:154cm ecl:dne
hcl:#888785
pid:066246061 eyr:1983

hcl:z
iyr:2016 byr:1986 ecl:utc
hgt:179cm eyr:2019 pid:583251408

ecl:amb iyr:2014 pid:499004360
byr:1927 eyr:2021 hgt:193cm hcl:#ceb3a1

pid:631303194 ecl:gry
hcl:#18171d cid:216 iyr:2019
eyr:2024 hgt:178cm

hcl:#341e13 cid:201
byr:1949 iyr:2019 ecl:gry pid:372356205
eyr:2024

hcl:#18171d
pid:867489359
hgt:185cm
iyr:2020 ecl:amb
eyr:2030
byr:1955

byr:1991
ecl:brn eyr:2025 hgt:184cm iyr:2016 pid:202216365

ecl:xry pid:#524139 hgt:151cm hcl:z eyr:2031 byr:2030 iyr:2005

byr:1971 hgt:178cm ecl:amb hcl:#ceb3a1
iyr:2010
eyr:2026 pid:396974525

iyr:2014
hgt:177cm pid:928522073
eyr:2022
ecl:hzl
hcl:#c0946f byr:1983

hgt:167cm hcl:#ceb3a1 iyr:2014
pid:172415447
eyr:2020 byr:1956

iyr:2011 hgt:188cm byr:1947 eyr:2020 pid:667108134 ecl:amb hcl:#44a86b

cid:302 ecl:brn pid:292483175 hgt:154cm
byr:1997
eyr:2026
iyr:2014 hcl:#623a2f

hgt:171cm
iyr:2014 hcl:z ecl:hzl pid:321513523 eyr:2027 cid:146
byr:2001

eyr:1956 ecl:dne hgt:75cm hcl:82e1fa
iyr:2030 byr:2027

eyr:2020
iyr:2011 pid:656669479 ecl:oth hgt:151cm hcl:#efcc98 byr:1981

iyr:2013
byr:1934
pid:142890410 hgt:62in
eyr:2022
hcl:#87cca4
ecl:hzl

pid:006232726
hgt:173cm ecl:hzl cid:110
eyr:2026 hcl:#866857 iyr:2017 byr:1992

cid:208
iyr:2014 ecl:brn eyr:2024 byr:1935 hgt:187cm
hcl:#b6652a
pid:770836724

iyr:2014 cid:144 hgt:169cm
eyr:2022
ecl:oth
pid:117575716 hcl:#fffffd byr:1926

byr:1971 ecl:brn
hcl:#733820 eyr:1942 iyr:2013
pid:606274259 hgt:163cm cid:196

byr:1964
pid:997828217 eyr:2029 iyr:2017 ecl:blu hcl:#341e13
hgt:158cm

pid:568202531 hcl:#efcc98 hgt:154cm eyr:2029 iyr:2010
byr:1946
ecl:blu

iyr:2011
pid:619355919
byr:1955
ecl:brn hcl:#888785 eyr:2030 hgt:155cm

ecl:hzl pid:367152545
hgt:162cm
cid:221 hcl:#866857
eyr:2024
byr:1997 iyr:2019

hgt:157in
cid:268 hcl:32371d byr:2020
ecl:zzz pid:1081234390

ecl:hzl eyr:2026
byr:1969 pid:850482906 cid:166 hcl:#602927 hgt:60in
iyr:2019

hcl:#c0946f
hgt:176cm
ecl:brn eyr:2026 iyr:2018 cid:172 byr:1986 pid:172963254

ecl:grn iyr:2016
hgt:187cm
byr:1983
hcl:#efcc98
pid:722084344 eyr:2025

ecl:oth hcl:#341e13 pid:130312766 hgt:171cm iyr:2018 byr:1927 eyr:2024

byr:2021 hgt:152cm hcl:74dda6
eyr:1984 cid:216
iyr:2018 pid:95283942

hcl:#b6652a pid:924778815 iyr:2017 ecl:gry
eyr:2035
hgt:68cm

iyr:2010
hcl:#efcc98 ecl:brn eyr:2020 pid:801894599 hgt:163cm byr:1959

pid:798701070 eyr:2030
hcl:#866857 ecl:hzl hgt:169cm byr:1994 cid:219 iyr:2010

pid:#e9b41b
hcl:#341e13 byr:1970
iyr:2014
ecl:oth cid:266 hgt:68cm eyr:2023

byr:1931 pid:929960843 hgt:187cm hcl:#6b5442 cid:52 iyr:2010 eyr:2024 ecl:brn

iyr:2017 byr:1974
ecl:hzl cid:243 pid:66053995 hgt:147 eyr:1920 hcl:z

iyr:2012 byr:1962 ecl:brn pid:773399437 hcl:#341e13
eyr:2026

pid:738442771 hgt:186cm eyr:2027 hcl:#efcc98 iyr:2013
ecl:brn byr:1928

pid:855794198
ecl:oth
hgt:67in
cid:81
iyr:2011 hcl:#b6652a eyr:2020
byr:1921

hcl:176abf hgt:161in
byr:2002 iyr:2016 eyr:2027 pid:639047770 ecl:brn
cid:178

pid:335686451
hcl:#86c240 iyr:2017 hgt:190cm byr:1968 ecl:amb

hgt:150cm
hcl:094a87 ecl:#09c463 eyr:1926 pid:537511570 byr:2009
iyr:1998

hgt:74in
pid:927963411
eyr:2026 ecl:gry cid:323 iyr:2012 hcl:#fffffd byr:1959

iyr:2018 byr:1978
hcl:#ff1829 eyr:2023
pid:823129853 ecl:hzl
hgt:65in

pid:189cm
ecl:#00391e hgt:72cm hcl:11050f
byr:2029
eyr:1994
iyr:1935
cid:186

ecl:grn byr:1942 pid:217290710 hgt:181cm eyr:2021 hcl:#7d3b0c iyr:2019 cid:320

byr:1983 iyr:2013 cid:122 hcl:#ceb3a1 eyr:2030 hgt:59in ecl:grn pid:946451564

ecl:amb
cid:236 hgt:184cm
hcl:#cfa07d iyr:2017 pid:934730535 eyr:2021 byr:2002

byr:1950 ecl:hzl eyr:2030 hcl:#623a2f pid:742249321
hgt:158cm iyr:2018

byr:1946 eyr:2021 hcl:#a97842 pid:204671558 ecl:grn
iyr:2010 hgt:187cm

hcl:#b6652a pid:528124882 hgt:162cm byr:1924 ecl:amb iyr:2027 cid:157
eyr:2028

hgt:180cm iyr:2013 byr:1926 pid:232265934 hcl:#602927 ecl:oth

byr:1984 ecl:brn
iyr:2016 pid:756596443 eyr:2030 hcl:#7d3b0c hgt:183cm

hgt:185cm
hcl:#fffffd byr:1991 eyr:2023 iyr:2014
ecl:amb
pid:759105859

cid:82 iyr:2012 hgt:160cm eyr:2022 pid:593798464 ecl:gry hcl:#4e7571 byr:1983

pid:478427550
iyr:2010
ecl:amb byr:1969 hgt:68in cid:94 eyr:2021 hcl:#866857

ecl:amb iyr:2019 byr:1986 hgt:170cm
hcl:#c0946f
pid:779205106 eyr:2027

ecl:brn eyr:2025 byr:1925
hcl:#7d3b0c hgt:76in pid:576353079 iyr:2010

hgt:175cm hcl:4bf5ae ecl:amb
eyr:2029 pid:173cm cid:329
iyr:1952 byr:1972

ecl:grn
eyr:2030
iyr:2015 hcl:#c0946f
byr:1989
hgt:178cm
pid:287209519

pid:834505198 byr:1985 ecl:gry eyr:2024
cid:295 hgt:169cm iyr:2017

hgt:170cm
pid:054644831 eyr:2023 iyr:1949 ecl:amb
hcl:#888785
byr:1955

hgt:171cm
pid:947263309 iyr:2015 byr:1944 eyr:2027 ecl:grn cid:79 hcl:#341e13

eyr:1982
cid:147
iyr:2015
hgt:70cm hcl:a77c10 ecl:zzz byr:2007
pid:161cm

ecl:gry byr:1933
hcl:#c0946f pid:483275512 iyr:2012 eyr:2025 hgt:161cm

eyr:1985 hgt:176cm hcl:7b6ddc iyr:2012 cid:326 byr:1973 pid:929418396 ecl:gmt

ecl:gry
byr:1971
hgt:184cm
eyr:2027 hcl:#3adf2c iyr:2017 cid:210
pid:693561862

eyr:2021 pid:779298835 byr:1921 hgt:193cm ecl:amb
iyr:2016 hcl:#ceb3a1

hcl:4a1444
byr:2019 iyr:2024 hgt:182in
cid:87 ecl:#122264
pid:181cm
eyr:1927

cid:267 ecl:amb eyr:2020 byr:2000
hcl:#18171d iyr:2012 hgt:190cm pid:18525759

ecl:oth byr:1988
iyr:2019 pid:660570833
hcl:#866857 hgt:176cm

eyr:2030 hcl:#866857
byr:1967 cid:316 pid:560346474 iyr:2015
hgt:160cm
ecl:gry

ecl:hzl
iyr:2014 hgt:164cm hcl:#733820 eyr:2025
pid:106302413 byr:1920

iyr:2016 pid:515066491
ecl:grn eyr:2026 hgt:179cm hcl:#b6652a byr:1982

ecl:#7de6a0
iyr:2004 eyr:1955 hgt:154cm cid:138 byr:2004
pid:758934555
hcl:a21980

pid:#2a21e0 ecl:#1b9b27 hgt:165in
byr:1998 iyr:2014 eyr:2032

eyr:2021 hgt:184cm pid:431054313 hcl:#ceb3a1 cid:109 byr:1977 ecl:blu
iyr:2011

pid:006339126 hgt:177cm
cid:188 hcl:#a97842
iyr:1959
ecl:xry

byr:2000
ecl:hzl eyr:2029
iyr:2011 hcl:#866857 hgt:74in'''
    
values = values.split('\n')

count = 0
recuento = 0
passport_valid = 0

for v in values:
    individual = v.split(' ')
                
    for i in range(len(individual)):
        name = individual[i].split(':')
        if name[0] == '':
            count = 0
            
        if (name[0] == 'byr' or name[0] == 'iyr' or name[0] == 'eyr' or name[0] == 'hgt' or 
        name[0] == 'hcl' or name[0] == 'ecl' or name[0] == 'pid'):
            count += 1
            
        if count == 7:
            recuento += 1
            count = 0
            
print(' 4 - part 1: ' + str(recuento))


### Day 3 - part two ###  

count = 0
recuento = 0
passport_valid = 0

for v in values:
    individual = v.split(' ')
 
    for i in range(len(individual)):
        name = individual[i].split(':')
        if name[0] == '':
            count = 0
            
        if (name[0] == 'byr' and len(name[1]) == 4 and 1920 <= int(name[1]) <= 2002
            ) or (name[0] == 'iyr' and len(name[1]) == 4 and 2010 <= int(name[1]) <= 2020
                 ) or (name[0] == 'eyr' and len(name[1]) == 4 and 2020 <= int(name[1]) <= 2030
                      ) or (name[0] == 'hgt' and (name[1][-2:] == 'cm' and 150 <= int(name[1][:-2]
                      ) <= 193 or name[1][-2:] == 'in' and 59 <= int(name[1][:-2]) <= 76)
                      ) or (name[0] == 'hcl' and name[1][0] == '#' and len(name[1][1:]) == 6 and name[1][1:].isalnum()
                      ) or (name[0] == 'ecl' and (name[1] in ['amb', 'blu', 'name', 'brn', 'gry', 'grn', 'hzl', 'oth'])
                      ) or (name[0] == 'pid' and len(name[1]) == 9 and name[1].isnumeric()):
                          count += 1
            
        if count == 7:
            recuento += 1
            count = 0           
            
print(' 4 - part 2: ' + str(recuento))


### Day 5 - part one ###
print('''
--- Day 5 ---''')

values = '''BFFFFFFRLL
FFBFBBBRLL
FBBFBFBRLR
BBFBBBBLLL
BBFBBBBLLR
BBBFBBBLLR
FFBBBFBRLR
BBFBFBFLRL
FBBFFBBLRL
BBBFBBFRRL
BBFBBFFRRL
BFBBFBFLRL
BBFFFBBRLL
FBFFFBBLLR
FBFBFBFLRR
FBBFBFFRLL
FFBBFFFRRR
BFBFBFBRLL
FBBFFBBRLL
BBBFFBBRLL
BFBFFFFLLR
FBBBBFBRRR
BBFBBFFLRR
BFFBFBFRRR
FBFBBBBRLR
BFBFBFFRLL
BFFFFFBRLL
FBBBFBFLLR
BFFBFBBRRR
BFFBBFBLLR
FBBBFFBLLL
BFFFBFBLRR
FFFFBFFLRR
BBFFFBFLLR
FBFBFFFLLR
FBFFFFFLLL
FFFFFFBRLL
BFFBFBBLRR
BFBFFBBLRR
BFFBFFBRLR
FFBFBBBLLR
FBFFFBFRRR
BFBFBFFRLR
BBBBFFBRRR
FBBFBBBLLL
FBBBBFBLRR
BFBBFFFRRL
FBBBBBBLRL
FBBFFFFLLL
FFBBBFFLLR
FBBBBBBRRR
BBBBFFBRLR
BBBFBFBLRL
FFBFFBFLLL
FBBBBBFLLL
FFBBBBBRLR
FBBFFFFLRL
BBFBBFBLLR
FFFBBFFRLR
FFFBBBFLLL
BFFFFFFLRL
BFFFBFFLRL
FBBFFFFRLR
FBFFFBBLLL
FFFFFBFRLR
BBBBFBFLLL
FBFBFFBLLR
FFBFBFBRLR
FBBBFBBLLR
FFBBBBFRLR
FBBBFBBRLL
FFFBFBFLLL
FFFFFBFRRL
FFFBFFBLRR
BFBFBBFRLL
BFBFFFBLLL
FFFBFBFRLL
FBFBBBFRLL
FFFBFBFLLR
BFBBFBFRRL
BBFFBFFRLR
FFFBBFFRLL
BBBBFFFLRL
BFFBFBBLLL
BBFFFFFLRL
BBFFBBBRLL
FFBFFFFLRR
FFBBFFFRLR
BBFFBBBRLR
FBFBFFBRRL
FFFFBBBLRL
BBFBFFFRRL
BFBBBFBRRL
FFBFBFBLRR
BBBFBFFRLR
BFBBBBBRRL
FBFFFFFLRR
BFFFFFBLRR
FFBBBFBLLL
FBBBFFFLRL
BBFFBBFRRL
FBFFFFBRRR
BFBFBBBRRL
BBFFBBBLRL
FBBFBFBRLL
FBFBBBFLLL
FFFFBBBLRR
FBBFBBFLLR
FBFFBBFLRL
FFBBFBFRRR
BFFBBBFLRL
FFFBBBFRRL
FFBBBFFLRL
BFBBFFBRLL
BFFBFFFLLL
FBFFFFBLRR
BFBFFBFLRL
FBBFFBFLLR
FBBFBBBRRL
BBFBFFFLLL
FBBBBFFLRR
FBBBFBBRRR
FFFBFFFLLR
BBFFBBFLRL
FFFFBFFRLL
BFBBBFFRRR
BFFFFBFRRL
BBFFBBBLLR
BFBBBBFRRR
BFBBBFFLLL
BBFBFFFLRL
BBBFFFBRRL
BBBBFFBRLL
FBFFFFFLRL
BFFFBBFLLR
FFFFBBFRRL
BBFFBFBLLR
BFFBBFFRRL
BBBFFBBLLL
BFFBFBFLLL
BFBFBFBRRL
BBFFFFBRRL
FBBBFBFRRR
FFBFBBFRLR
FFFBBBBLRR
FFBBFBBRRL
BBFBBFBRLL
FFBBBBBRLL
BFBBBBFLRR
FBFBBFBLLL
FBBFFFFRLL
BFFBFFFLRL
BBBFBBFLLL
BFBFBBBRRR
FBFBBFFLRL
FBBBFFFLLR
FBBBFFBLLR
BBFFBBFRLL
FBBFFBFLRL
BFFBBBFRRR
BFBBBBBRLL
FFBBBBFRLL
BBBFFFFLLL
BBFBFFBRRR
FBBBBFFLLL
BBBFFFFRRR
FBBFBFBLLL
BBBFBBFLRR
FFBFFBBRLL
FFBBFBFLLL
FBFFFFFRLL
FBFBFFBLRR
BBFFBBBRRL
BFFBBBFRRL
FFBBBFBRLL
FBBBBFBRRL
BBFBBBBRLR
BFFBFFBRRL
BBFBFBBRRL
FFFBFBFRLR
FFBBFBFRLR
FFFBBFBRLL
BFFFFBBRLL
FBFBBFBLLR
FBFFBBFLLL
BBFBFBBRLR
BBFBFBBLLL
FBBBFBBRRL
BFFFBBBRLR
BBFFBBBRRR
BFFBFFBLRL
BBFBFFBLLR
FFFFFFBRRL
BFBFBFFLLR
BBBBFFBLLL
FBBBFBFRRL
FBBFFBFLLL
FFBFBFFRLL
BFBBFFFLLL
FBFFFBBLRL
FFFBFFBLRL
BFFFBBBLRR
BBBFFBFRRL
FBBBFFFRLR
FFBBFFBRRR
FBBBBBBLLL
BFFBBFFLLR
FFFFFBBLLR
FBBFBFBRRR
BBBFBFFLLL
FFFFBBFRRR
FBFFFFBRLL
FFBBFFFLRR
FFFFFBBLRL
BBBBFFFLLL
FFFFBFBLLR
BBBBFFFRRR
FBBFBBFRRR
BFFBFFFRLR
FBFFBBFLRR
BFBBFBBRLR
BFFBBBFLLL
BFBFBBBLLL
BBFBBBFRRL
FBBFBBFRRL
FFFBFFFLRL
FBFFBFBLRR
FFBFFFFRLL
FFFFBBFLRR
BFBFFBFLRR
FBBFBBBRLR
BFBBBFFLRL
BBFBFBFRLR
FFFFFBBRRL
BBFFBFFLRR
FBBBFFBRLR
BBBFFBBRRL
FFFFFBBRLR
FFFBBFFRRL
FFBFFFFRLR
BFFBFBBLLR
BFBFBFFLLL
FFBFBBBLRL
BBFBBBBLRR
BFFFFFBRLR
BBFBFBBLLR
FBBBBFBRLL
BBFFBFBLRR
BBFBFBBRRR
BBBFBBBLLL
FBFBBBBRLL
BFFBFBBRLL
BFBBBBBRLR
BBFFFFBRLL
FBFBBBBRRR
FBBFFFBRRL
BFFBBFFLLL
BBFBBFBLRL
FBBFBBBLRR
FBBFBBFLLL
FFFFBBFLRL
BFFFBBBRLL
FFFBBBFLRL
BFFFBBFRLR
FFFFBBBLLR
FFFFBFFRLR
FFFFBBBRRR
BFBFBFBRRR
BBFFBBFRRR
FBBFBFFLLR
BFBBBFBRLL
BFBFFFFRLR
BFBFFFBLLR
BFBBBFBRRR
BFFBBBFRLL
FBFFBBFRLR
FBFBBFFLLL
FBFBFFFRLR
FFFBFBBLRR
FFBBBFFRRL
BBFBFFBLRL
FBBBBBFRLR
BBBFBFBLLR
FFFBBFFLRL
BFFBBFFLRR
BBFBFFFLRR
FFBFFFBRRR
BFFBBFBLRL
FFBBFFBRLL
BFBFFBFRLL
FFBFBFFRLR
FBFFFBFRLR
BFBBFBFRLL
BFFBFBFRRL
FFBBFFBRRL
FBFFFFBLLL
BFFFBBBLLL
FBBFBFFRRL
BFBFBBBRLL
FFFBFFFLLL
BFFFBFFRRL
FBBBBBFRLL
FFBFBBFRRR
FBFBFFFLLL
FFFBFBBRRR
BFBBFFFLRR
FFFFFBFLRR
FBFBFFBRLR
FBFFBBFLLR
BBBFFFBLLR
FBFFFBBRLL
BFFBFBBLRL
FFFFFFBRRR
FFBFBFBRLL
BBFBBFFLLR
BBBFFFFRLR
BFBFBFBLRL
FBFFBFBRLR
FBBFFFBRRR
BBFFFFFLRR
BFBFBFBLRR
BFBBBBBLLR
FFBFFBFRRR
FFFFBBBRLL
FBBBBBFLRR
FFBBFBFRLL
FBFBBFFLRR
FFBFBBBLLL
FBFFBFFRRL
BBBFFBBLRR
BFFFFFFRRL
FBFFBFFRLL
FBBBBFBRLR
FBBBFBFLRL
FBBBFFBLRL
FFBBFBBLLR
BBFFFBBRLR
BBBBFFBLLR
BFFFFBFLRR
BBFFBFFRLL
FFBFBFFRRR
BFFFFFFRLR
FFFFBFFLRL
BFBBFFFRLR
BBFFBFFLLL
FFFFFBFRRR
FFFBFBBLRL
BFFBBBBRRL
FBFBBFFLLR
FFFBBFFLLL
FFFFBFBLRL
BBFBFBBLRR
BBFFBFFLRL
BBBFFFBLRL
BFFBFBFRLL
FFFBFFFLRR
FBFFFBBRLR
BFFFBBFRRR
FBBBBBFLRL
BFFFBBBLLR
BFFFBBFLRL
BFFFFBFLLR
FBFFFBBLRR
FBBFFFBRLR
BBFFBFBLRL
BBFBFBFLLR
FBBBFBFRLR
FBFFFBFRRL
BFFFBFFLRR
FFFFBFBLRR
FBFFBFFLLL
FFBFFBBRLR
BBFBBBFLLL
FBFFBFBRRL
BFFBFFBRLL
BFBFFFFLRR
FFBFBBBRLR
BFFBFBBRRL
FBFBBBBLRR
BFFFFFBLLL
FBFFBFBRRR
FBFBBFFRLR
BFBFBBFLLL
BFBBBFFRRL
FFBBBFBLLR
FBBFFFBLRL
BFFFFFFLLR
FBFFFFBLRL
FFBBFFFLRL
FFBBBFBLRL
BFFFBFBLLR
BFFBBBFLRR
FBFFFBBRRR
FFBFFFBRLL
FBFBFBBLLR
BFBBBBFRLL
FBBBBFFRLL
BFBFFBFRRL
FBBBBFFRLR
FFBFFFFRRR
BFFFBBFLRR
BBFBFBFRLL
BFFBFFBRRR
FFFFFBFLLL
BFBFFFBRRL
BFFBBFBRRL
BFBBFFBRRL
FFFBBBBRLR
FFFBBBBLRL
BFBBBFFLLR
BFBFFFFRRR
BBBFBFFRRR
FFFBFFFRRR
FFFBFBBLLR
BBBFBFFRRL
BBFFBFFLLR
FFFBBFFLLR
FFFBFBBLLL
FBFBFBFLRL
FFFFFBBLLL
FBBBBBBRLR
FFBBFBFLRL
BFFFFBBRLR
BFFFBFBLLL
BBFBBBFRRR
FBBBFFBRRL
FFBFFBFLRL
FFBFFFFLRL
BBFFFFBLLL
BFBBFBBRLL
FFFFBFFRRR
BFFBFBBRLR
BFFBFBFLRR
BFFBBFBRLL
FBBBFBBLRR
FBFBFFFRLL
BFBFFFBRLL
FBBBBBFRRL
FBFBFBBRLL
FBBFFBBRRR
BFFFBBFRRL
BBFFFFFRRR
BFFBFBFLRL
BBBFFBBLRL
FFBFBBFLRR
BBFFFBFRLR
FBFBBBFRRR
BBFBBBBRLL
FBFFBFFRLR
BFBBBFFRLR
FBFFBBBLRR
BFBFFBFRRR
FFBFFBFRRL
FFBBBBBLLL
BBFBBBFRLL
BFBBFBBLLL
BFBBBFBLRL
FBBBFBFLLL
FBBFBFFLRL
FBFBFBFLLL
BBFFBBFRLR
FBFBBBFLRL
BBFBBFBLRR
FFFFBFFLLL
FFFBBBBRRL
BBBFBBBRLL
BBFFFFFLLR
FBBFFBBRLR
FBBFBBFRLR
BFFFBFBLRL
BFFFFBBRRR
FBFFFFFLLR
FBBFBBFLRL
BBFFFBFRRR
BBBFFBFLLR
BFFBBFBRLR
BBFBFFFRLL
FFFBBFBLRR
BBBFBFFLLR
FBFFBFBLRL
FBBFBFFLRR
FBBBFFFLRR
FBBFBBBRRR
BBFFFBFRLL
FFBFBBFLRL
FBBFFFBLLR
BFFFFBFRRR
BBFBBFFRLL
FFBFBBBLRR
BFBFFFBLRL
FBBFFBFRRL
FFFFBBBRRL
FFFBBFBRRR
FFFBBBFRLL
BBFFBBFLLR
FFBFBFFRRL
BFBFFFBRLR
FFBBBFFRLL
FFFFBBFLLL
BFFFFFBLLR
FBBFFFFRRR
FFFFFFBLRL
BBFBFFFLLR
BBBFBFFLRL
BBBFFFFRLL
BBFFFFBRLR
FBFBBFFRRL
FFFFFBFLLR
BFFFBFBRLR
BFFFFFFRRR
FBFBFBBRLR
BBBBFFFRLR
FBBFBFBLRL
BBFFBFFRRR
BFFBBBBRLR
BBBBFFBLRR
BFBBFBBRRL
BFFFFBBLLL
BFFFBFBRLL
FBBFFFFLLR
BFBBFFFRLL
BBFBBBFRLR
FBFBFBFRRR
BFBFBFFLRR
BBFBBBBRRL
BFFFBFFRLR
BBBFBFBLLL
FBFBFFFRRL
FBBBFFFRLL
FBFBBFBRRR
FBFFFFFRRR
FBBBBBBRRL
BBBBFFFLLR
BFFFBFFLLR
BFBBFBBLRL
BBBFFFBRLR
FFFBBFBLRL
BFBFBFFRRR
BBFFFBBLLR
FBFBBFFRLL
FFFBBBFRLR
BFFFFBFRLL
FFBBFBBRLL
FFFBFFBRRL
BBBBFFFRLL
FBFFBBBRLL
FFBFBFFLLL
BBBFBBFLRL
FBFBBFBLRL
FFBFBFFLRR
FFFBFFBLLR
FBBFBFFRRR
FFBFBFBLLR
FFFFFFBLLR
BBBFFFFLRR
BBFBBFFRLR
FFFFBBBLLL
FBBFFFBLRR
BFFFFBFLLL
BFBBBFBLRR
FBFFFBFLLR
FBFBBFBRRL
BFBFBBFRRR
FBFBFFFLRR
FFBFFBFLLR
FBFBFBFRRL
FFFBBBFLRR
FFFBBBBLLR
BBBFBBFRRR
BFFBBBBLRR
BBBFFBFLRR
FFBBBFFRRR
FBFFBFFRRR
BFFFFBBLRR
BFFBFFFRLL
BFFBFFBLRR
FBBBFBBRLR
BFBFFBBRLR
FBFFBBFRRR
FFBBBFFRLR
BBFFFFFRRL
BFFBBBBLRL
FBBFFFFLRR
FFBFBBFLLL
BFFFBBBRRR
BBFFFFBLRR
FFFFBFBLLL
FBFFBFFLRR
BFBFBFFLRL
BBFFFFFRLR
BBBFFBBRLR
BBFFBFBRRR
FBFFBBBLLR
BBFBFBFRRR
BFBBFBFRRR
BFFFBBBLRL
BFBBFBBLRR
BBBFBBBRRR
FFFBBFBRRL
FFBFFFBRRL
FFBFBFBLRL
BFFFFFBRRR
BFBFBBBLLR
BFFFBFFRRR
FBFBFFFLRL
BFBBBBBRRR
FFFBFBFLRL
FFFFBFFRRL
FBFBFBBLLL
FFFFBBBRLR
FBBFBBBLRL
BFBBFBBRRR
FFFBFBFLRR
BBBBFFBRRL
FFBBFBFLLR
FFFBFBBRLR
BBFFFBFLRL
FFBBBFBRRL
FFBFBBBRRR
BFBBBBFLLR
BBFBBBFLRL
BFBBFBBLLR
BBFFFBBLRR
FFBBFFBLRL
BBBFFFFRRL
BFFFBFFRLL
BBBBFFFLRR
FFBBBBFLRR
FBBFFBFLRR
BBBFFFFLLR
BFFBFFFRRL
FBFBFBBLRL
BFBFFBFLLR
BFFBFBFLLR
BFBFFFBRRR
FFBBFFFRRL
BBFBBFBLLL
FBBBFBFRLL
BBFBBBFLRR
BBBFFFBLRR
BBFFFFBLLR
FBBFBFFRLR
FBFBFFBLLL
BFFBBBFRLR
BFFFFBBRRL
BBBFFBFLLL
FFFBFBFRRR
FBFFBFFLRL
FFBBBBBLLR
BFFBBFBRRR
FBBBBFBLRL
BFBFBBBRLR
BBFBBFFLLL
BFFFFFBLRL
FBBFBFBRRL
FBBBFFFLLL
BFFFBFBRRR
FFBFBFFLRL
FFBFBFBRRL
FFBBBBBRRR
FFFFBFBRLR
BFBBFFBLLL
BFFBBBFLLR
FBBBFFBRLL
FBFFBBBLRL
BFFBBBBRRR
FFBFFBBRRL
BFBFFBBRLL
FFFFFBFLRL
FFBBBBFRRR
FFBFFFFLLR
BBBFBBBRRL
FFFFFBBRLL
FBFBBBBRRL
FBBBFBFLRR
FFFBBFFLRR
FBFFFBFLRL
FFBFFBFRLL
FFFBFFFRRL
FFFFBFBRLL
BBFBFBBRLL
FFBBBBFLLR
FBFFFBBRRL
BFBBBBBLLL
BFBFFBBLLL
FFFFBFBRRL
FFBBFFBLRR
BFBBFFFRRR
FFBFFBFRLR
BBFBBBBLRL
FBBFBBBLLR
BFFFBBFLLL
FFFFBFFLLR
BFFFFBFRLR
FBBFBFBLRR
BBBFFFFLRL
BBFFFBBLRL
BBFBFFBRLL
FBBBBFBLLR
FBFFBBFRLL
BBFFBFBLLL
FBBFFFBRLL
BBBFBFBRRL
FBFBBFBRLR
BFBBBBFLLL
FBFBFBFRLL
FBFBBBFLLR
BBFBFBFLLL
BBFFFBFLLL
BBBFFFBLLL
BFBBBFBLLL
FFBBBFFLLL
FFBFFFFRRL
FBBBBBFLLR
FBBFFBBLRR
BBFFFFFRLL
FFFFFBBLRR
BFBBFFBLRL
BFFFFFBRRL
BFBBFFFLLR
FFFBFBBRRL
FFBFFBBLRL
BFFFFBBLRL
FBFBBBBLRL
FBBBFFBRRR
FFBBFBBRLR
BFBBFFBLRR
FBBBFFBLRR
FBFBFFBRLL
FBFBFBFLLR
BBFFFBBRRL
BBBFBFBRLL
BBFBBFFRRR
BFBBFFFLRL
BFBFBFFRRL
BBFBBFFLRL
BBFBFBFLRR
BBFBFFFRRR
BBBFFBFRLR
BFFBBFFLRL
FBBBBBBRLL
BBFFFBBLLL
FFFBBBBLLL
BBFFFFBLRL
FFBBFFBRLR
BFBBBBBLRR
BBFBBFBRRR
FFFFFFBRLR
FFFFBBFRLL
FFFFBBFRLR
FBFBBFFRRR
FFFFBFBRRR
FBFBFBBRRR
FFFFFBBRRR
BFBBBBBLRL
BBBFBBFLLR
BFBFFBBRRL
BBBFFFBRLL
BBFBBBBRRR
FBFBBBFRRL
BFBBFBFLLL
FFFBBFBLLL
BBFFBFBRRL
FFBFFBBLLR
FFBFBBFLLR
BBBFBBFRLL
FBBFFFFRRL
FBBFFBFRRR
BFFBFFBLLL
FBFBFFBLRL
BBBFBBFRLR
FFBFBBBRRL
FFBBBBFLLL
FBFBBBFLRR
FFBBFBFLRR
FBFFBBFRRL
FFBBFFFLLR
FBFBFBBLRR
BBBFBBBRLR
BFFBFFFLLR
BFFFBFBRRL
FFBBBFBRRR
BFFBFFFRRR
BBBFBFFLRR
FFFFFFBLRR
BFBFBBFRRL
FBFBBFBRLL
FBBBBFFLLR
BFBBBBFLRL
FBBBBFBLLL
FFBBFFBLLR
BBBFFBBRRR
BFBFFFFRRL
FFBFFBBRRR
BFFBBFFRRR
FBFFBFFLLR
BBFFFFFLLL
BBBBFFBLRL
BFBBBBFRRL
FBBFBFFLLL
FFFFFBFRLL
FBBBBBFRRR
BBBFBFFRLL
BFBBBFFRLL
FFBBBFFLRR
BBFFFBFLRR
BBFFFBFRRL
BBFBFFBRLR
FFBFFFBLRR
FBFBFBBRRL
FFFBBFFRRR
FBBBBBBLLR
FBBFFBBLLL
FBBBBFFRRL
BFBFFFFLRL
BFBBBFBLLR
FFFBFFBRLL
FBFBBFBLRR
FFBBFBBLRR
BBBFBBBLRR
BBFBBBFLLR
BFBFBBBLRR
BFBFBBFLRL
FFFBBBBRRR
BFBFFBBRRR
FBBBBFFRRR
FFFBBFBRLR
FBFFFBFRLL
BFBFFBBLRL
FFBFBBFRRL
BFFFFFFLLL
BFBFFFFLLL
BBFFBFFRRL
BFFBBFFRLR
FFFBFFBLLL
BBFBFFBLLL
FBFFBBBRLR
FBBBBFFLRL
FBFFBBBRRR
BFFBBFBLLL
BFBFBFBLLR
FBFFFFBRLR
BBFFFBBRRR
BFBBFFBLLR
FFFBFBBRLL
BBFFFFBRRR
BFFBBFBLRR
FBFBFBFRLR
FBFFFBFLRR
FFBBBBBRRL
FBFFBBBRRL
BBBFFFBRRR
FBFFFFBLLR
BBFBFBFRRL
BBFBFFFRLR
BFFFFBFLRL
BBBBFFFRRL
FBBFBBFRLL
BFBFBFBLLL
FBBBBBBLRR
FFBBBBBLRR
BFFBBFFRLL
FFFFBBFLLR
FFBBFFBLLL
FFBFBBFRLL
BBBFBFBRRR
BFBBFBFRLR
FFBBFFFRLL
FBFFFBFLLL
FFBFFBBLRR
BFBFBBFLRR
FBBFFBFRLR
BBBFBFBLRR
BBFFBBBLLL
FFFBBBFRRR
BFFBBBBLLL
FFFBBFBLLR
BFBBBBFRLR
FBFFBFBRLL
FFBFFBFLRR
FFFBFFBRLR
BFBFFBFRLR
BFBBBFFLRR
BFBBFBFLLR
BBFBBFBRRL
FBFBFFBRRR
BFBBFFBRRR
BBFBFFBLRR
FBFFFFBRRL
FFFBBBBRLL
FFBBFFFLLL
BFBFBBFLLR
FBBBFBBLLL
BBFFBBFLRR
FBFFFFFRRL
BFBFFBBLLR
FBBFFBBLLR
BBBFBFBRLR
BFFFFFFLRR
BBFFBFBRLR
FBBFFBBRRL
BFFFFBBLLR
BBFBBFBRLR
FFBBBBFRRL
BFFBBBBLLR
FFBBFBBLRL
BFBFFFFRLL
BFFFBBFRLL
BFBFBBFRLR
BBFFBBFLLL
FFBBBFBLRR
FBFFBBBLLL
FFBFFFBLLL
FBBFFFBLLL
FFBBBBBLRL
FBBFFBFRLL
FFFBBBFLLR
BBBFBBBLRL
BFFBFFBLLR
BFBFBBBLRL
FFBFFFBRLR
BBBFFBFRRR
BFFBFBFRLR
FFBBBBFLRL
FBBFBBFLRR
FBBBFFFRRR
FBFBFFFRRR
FFFBFFFRLR
BFBBFBFLRR
FFBFFBBLLL
FFBFFFFLLL
FBFFBFBLLL
BFBFFFBLRR
FBFFFFFRLR
BBFBFBBLRL
FFBFBFBRRR
FFBFFFBLRL
FFBBFBBRRR
BBFFBFBRLL
FFFBFBFRRL
FFBFFFBLLR
FFFBFFFRLL
FFBFBFBLLL
FFFBFFBRRR
BBBFFBFRLL
FFBFBFFLLR
BBBFFBFLRL
FBFBBBBLLR
FBBFBFBLLR
FFBBFBBLLL
BFFBFFFLRR
BBFFBBBLRR
FBBFBBBRLL
FBFBBBFRLR
BFFFBBBRRL
BFBBFFBRLR
FBBBFFFRRL
BFBFFBFLLL
FBBBFBBLRL
FBFBBBBLLL
FBFFBFBLLR
FFBBFBFRRL
BFFBBBBRLL
BBBFFBBLLR
BBFBFFBRRL
FFFFFFBLLL
BFBBBFBRLR
BFFFBFFLLL'''


values = values.split('\n')

min_row = 0
max_row = 127
min_col = 0
max_col = 7
l = []

for v in values:
    for i, val in enumerate(v):
        if v[i] == 'F':
            max_row = (min_row + max_row + 1 ) / 2 - 1
        if v[i] == 'B':
            min_row = (min_row + max_row + 1 ) / 2
        if v[i] == 'L':
            max_col = (min_col + max_col + 1) / 2 - 1
        if v[i] == 'R':
            min_col = (min_col + max_col + 1) / 2

    ID = int(max_row * 8 + max_col)
    l.append(ID)
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7

print(' 5 - part 1: ' + str(max(l)))


### Day 5 - part two ###  

for element in range(min(l), max(l)):
    if element not in l:
        my_seat = element

print(' 5 - part 2: ' + str(my_seat))



### Day 6 - part one ###
print('''
--- Day 6 ---''')

values = '''elmcifawqgkp
dynwslejfcrkpv

pagrovuzscemqiy
paxomsgyuvc

hcoljgiraqvs
hgrvxqcojal
arjhqclogv
jlrvackhogq

bagctysnmhodfe
tfchsdoeagmnby
csdhnotbfgayme

rksnmhbxi
dyhavkcjrp

t
tx
t

fd
of
wejznfa
f
fs

lmz
ml
lm

zsidpewbu
uziwpbsed
dpzwbuise
uiebdpswz
dsuwzeibp

lpsk
srgk

xdktfapvyqmsgnzl
nmgqvxjzdlayrspf

reydlgxzvsokpi
sexvyokldpgr
yrqnkuixselvod
rylcshwxtefbadmokjv

qhxfn
hqfx
xifhq
fqhx

oqvjyepsdlmagcixutb
ebxgoqytzujdpvcma
nxrjofuytqpwdahkcgbv

gfwnlcbvuk
kqfnoucvgibw
pfsthrgmavun

aiejncxrvbwfgqyulz
vlzgrnxqfuacybweis
cvkqrezlxbiagyuwfsn

j
j
j
j

oxumbipdk
kmuoxditbp
bkpxmqioud

tsfjaiqdwexbonpvr
peuisyawojtxbr
utewromzksapjixb
klbrwmeahxistpgjco

izepslcjydnrxm
afedhyzbsmvlirtjncx

mbsuxzjkwaoclgr
sjcmlribkwgazx
zbwmxgcstearjlk
klcabsjxzgwrm

cuiexkrvhj
okijtbmqdu
znafslk

eyqvtziobjcgsp
mqjezigkycobpnsvw

wmhza
wazsh
fazhw

yqcwloght
wygdqmot
tgdybsoufwpq
rwjoqyagtbe

sdmjqln
mjqdibcleksw
oqsldmj
fxjpsmdlvatq
fdslomzuqj

zlfm
zfmnl
ufzlqm

oahgbpdmqwriuxzcyksfj
kcszyjxptoduhfrbmgawqi
hjkwbpogufscqzryxamid
ghkjxpozqsauycwimrbdf
rqywuxbgokjfzacihmsdp

otysqx
xsfyotq
tsxqyo

z
ua
vz
s

w
j

drn
pbetfc
lna

lfg
hvsinjd

jr
orj
jr

huarfp
forhwguxp
uhiprf
fhrupn
hrfup

zbndtlwehxku
uqbtwnxymkl

dfzbqrtenscjplvkaumwx
wtbeclnmkzsqyfajdpuvrx

uxmjrbdnhfoqgys
ymgjdosanq
dnjqwcsgoyem
oqdengmsyja
jynsmdtqgoe

odhjyxwncrt
ndehcmjwxytrio
cjydnrowxht

bgijpxv
qbnvmxguj
xqjgmuvzb

gcs
ep

idpzuvjseoqnck
mwdfyiacpklbjnheuorvszgx

fozderigtmcsjk
mubhxldvez

cobw
wobc
bwoc
baowmcr

mbka
w

izpceoqsglfv
zsqglfvecoi

eufkyohpwq
pyqhfeuok
noyqfpeukrh

zwjkfayco
lhcwf
hclrwf
fwnbtc

hfym
hfym
hyfm
myhf
yhmf

jbntrwuqkv
utxjiayq
thcqupxjdl

voxr
ogvxr
rvox

ukltspqnmirezyxj
ubxmpteqynocizjr
dzjfykwsxivumtreqpn

edyhapqtzcowf
isdawoqgzytfpech
wafdnqrzoelycmhtp
hatufwpdqcyoez

qolmhyg
hblygmo
yogmlh

bqoym
yqnoebm
byqom

b
b
ir
o
hb

cgikybplfujswhx
plguhjmkbfwxyic
xwjyhlmkcgubpif
kyiwgcfxhjmplbu
xgpuhvikblfjwcy

ljgdtkuaqwyvcfpx
cuqnjyvsbrlfai

gbnodyhuvxr
rpgaqs
zgsfpclr
rgs

iyqnvafsuzjxcodltghwkp
vihygqjntpldufxscwaokz
iqdhlngzfysaxopvukjcbtw
uldtisoknyzaqjpcgwvhfx

ztrfwlagshexiob
eafoigstrbzxwhn
gsaoufnbherxilwtz
iabgwxotzerhfs
kxyriswahgtezcdvobf

hwzsodnb
dzohwsb
zdwhsbno
ondwhxzsb
islzbdwhof

gcurdsepvakxzymo
wufbtpgqncjakoyems

hxectqimn
fetxchnkm
ncexth
brytxscnpgejoh
akufcendxht

qelcfbkwrxthnzoaj
mxkrqzwflijnbctdh
brhglkdmcxqjntfzw

newydrilgcqptjsfzmkoabh
fidvctrzkmsojnleaxqpywgh

umbrlcdhagvizfnw
webljuvic
buiyvlcsjwk

bw
bw
wb
bw
bw

opuyxbvwdk
bxodywpuvk
pdkyovubxw

z
q
i
z
z

swvpmuzdhnroikxg
shgkmwindxvpzoru
pgrmkzvdhonwixsu
knwopgiszrumxhdv

bjqlainyetm
kajmbqnteil
ajneqbytkplmi
domhaiqselcbtjn
ielqjmbntga

rlsntciqodgjwxbp
oanxipdc
yxicndfpome
pinvfhdoxcy
pdecixvkmnoy

rdngeljxkzwyfbhot
tmbxojfgwedrkyzn
rtopjxydkgwnevfzb
drbzofetqjyxwakng

wd
w
w
w
w

viseyncokafpwl
qjeygvwpdfbzlkou
ovikflerypw

sdpxiwage
esfgkuxh
grksexh

wqv
vq
kvq
qv
qv

btxyedokhlmpauwgq
gpdxuhvofysqamntez

fcwymjbnulsp
rhzjvwqde

rnsgbcdytpfz
spcrtybzgnf
sgncyztrpbf
csbtzfnygpr

lgioemjbdkf
bmokjilhedf
pblsdrtfeiomkj
iomxekgbjlfnd
mzdfjokbile

dnua
bsaurnxqc
aun
gayun

ryjkfxnmvphstw
icgwozqxtkbev

wprgenuj
xnrgmtej
otjvnzwelgru
zgrjenf
jdbiskyeanrcq

yag
ryga
yia
ayg
ya

brfjtowysu
ukyfbtjws
bfwgyustjvk
wfjxbhlpmnusqiacyzt

ktuqeysb

ecrjuyp
ycpawejr
ejyzrgvo

p
p
p
p
p

uyevxojtswflbdknp
tavljczymgnxqpbskd

tnrjqdaeu
yiowqlpk

sczbe
czesb
ceszb
zscqgeb
ebzsc

smyewnxtjoiurbclhf
htoenkbfwxursclmjip
juaflnrhosbmixewtc
wljbrincmsoexhfut

zklm
xfsmerpvkq
mki

zomlcxbevyukisjqp
dqhmnkfitjaprce

azemjicynpbwrhgduqtkloxfs
foheycqpuanskgdztiwlmrbx
pzwamfgdnkbrltsqheocxuyi

fgisklmbdwuaovcxntzjqypr
wrugpbntmcfljqikdovyxsza

qwgyu
tzfqbdjpxin
kaq
mqwa
gyqa

juevoildyfwqrpch
juovpelyqfid
ufgvoyldjeipq

pt
t

uiwcpryldjo
htwirdqcpuj
iqstpjrdyouv
ejnbrgzapfikudx
puvrmdjil

ayunwfjq
fnqwyja
ayjqfwn
wqajnfy

bho
hb

xeciotqasmblvghjk
ehoaicd

aibsmhznrkv
havsbirnkm
mvhriaknsbz
ynjbmshavdcekir

kd
vcwkdq
kd
kd

desol
egvspodlzk
redosl
dreslo

sywvarhcmlztiq
orqyclwmhizxsavgtd
mswlviqcyrtahz
qtmjazvcsirlwnpyh

fes
kdefns

poubdzithfq
douvaehxcl
dmohnu
eouhrdck

ympojnsevrc
corspkimven
pvzmeocnhtasbql
vcpokrxmjnes
nspgvmjocer

xgqvbohjlzpnymrusfc
xytjzfgpslbkruove
blopxszhgvumywjfr

nacjwslpxki
sjlmkacgniwyx
kilxgnajwsc
xwagtnckiljs
vlawnchrfbixskjd

icfqnuwxrhg
vnirqgxcmufbh
ghcrtfyloudix

jrouy
uyroj
juory
rjyou
kuotryj

fmnkioscvhtzdljuy
excjkilmywdsgunb
curdqnplmkejiays

cqwgdpihyoleb
qghlcteoydibp
pqoghecdilyb
rfbgcoqplehyiad
yldceuhqpgibo

twzxq
qnw

qcvhwkreoit
tvrqwchiuoke
oqktivrchwe
tqeihorcwvk
ikochwtvreq

rpwmlio
irqkofu
ieubo
tiopa
dzjscgxvionh

nzmeaqycg
zefliwdyg
gyzwrde

clmotbvhr
lmhtcwvigerb
zvufasbhtdymcjlr
cevxbltgrmh

kjvsgouatqxd
dxyajsgoqrt
tagwxqdjsco

pu
c
gc

mckf
kgqmf
fmk
odkmptf

vkqeigoc
kgqcvoei
gkiveqoc
coveiqgk
cgqoveik

pelbqxgnsicvut
vqsbngtpuxi
suxcnvbqpgit
wqubitsnghoxmyvp

xqymo
qmxoy
mxqyo
qoxym

bpey
ygdstpob
pbkhy
hbczyp

ebkpjsxvganulfohiqdtw
rlpjnfwdisogkhaqtxb
sdbqngowhlktfaxpij
cfngosajqikxpbtdlhw

pcno
op
co
o
roikw

nfogth
ochfdpe
lyarougfbx
sifwzvkqo

byzwnuk
voeqkzhrw
gwjcaekzvhx
zdimwkvc

hrqitmcukga
aosdujpcnmtqke

ux
ux
unx

vt
svt

pmulitndqgovfjebw
durbtgwjempxon
xsueoprmgkjnbdwt

ygzrdsxni
gwszyxriqnd

powyvtg
wvtpoyg
tovgpyw

ejnqu
jqne
reojq

fm
mf
mf
mf
xnfm

px
px

zakqlib
xaik

esgdvwxk
devwgkx
eqgxkwvd
evwxdkg
wdgvekx

jrv
vjr
jrv
jdrv
vjhr

wgazdye
ywga
gqway
gwvarhy

v
v
v

rofbzixqhlpakgndvj
gxphdvzfnoyuqrjke
fvqpnxgozhjrldk
gqphlxkfcnvtzodjrwi

uzyoinm
zyma
zynmixs
kndmruyz
fhmzqlyw

fl
fnl
fl

jgk
kjg
ljgk

orizljkcpeg
gpcirj
iebcdrj
crjaxfuiqtnv

hbxktsgyavoufm
xvskgyhutf
sthgzkvfxuyp
ktsguxyfhv

gxrtjozic
oznjtrxgi
irgztqxkj
gxztrji
irtgvuxzjwysh

rbskyeqldponazjucmxigh
qnecyzbgaorskjixmvhdl
nhrjoqcsyliwemakxbdtgz

gpyoakd
ydokpqsba
xudavkfpormnjz
eqkpoda
ciqpogdkba

ntsgzkpfi
buckqrmpxozevijwlgn

o
i
o
o

a
a
a

jhkdypm
pdn
pefzcv
agsbpuxoqrw
lpf

w
xw

xqsflmuzdpcrnhjgtwbvie
mxtcnpglidzqhbrjsufvew
amtbqulhdgirpwxvszjcnfe

evdrpj
tevpmrj
yiwheupjozvsgrklc
epfqbrvaj
ejpnqrv

lezukstv
sxvdcueapkb
ewujkrnvsz

s
li
s
xs

zmornlsckyb
mwblyhercogzsnkd
mbknzyrocsl

xfpbhqnejgazmvdwtuio
qohwtpidbfjmeguanxv
davwopnqfceltjisgumhrb
beqjmuhivfntgpdawo
dtuvpehyiqbgmjonwfa

fevqjnuhgsy
chlkrxgbs

bzevx
k
cif
k
r

tls
lnty
lt
ltcs
otlf

yxhftspr
xsfhytrp
xpsrythfqw
srptfxyhu
prtsxyfh

zanmupcyirdx
yfqpubdamrcknhx
eradnwlxpuvysmj

p
pb
hp

hy
hy
yh
ymh
hy

usocgzpjkfvqniltrxdbhw
yogvrkjxlpnamszudqtwb

exulnmgbfcjzk
fcexjudknzbl

ynmtqjve
jveynmq
jnqmvey
eyqnjmv
qnjymve

ziclnydugfqjretwhv
hljtrbqnwuvcyedfi
lxfyqcvrnhsjiuwtzed
wnvhfditlyrcusqej

kpaieqjdflocy
ciqpdoklyjaef
qpceifoljakyd
edkfliaqjpocy
kqjoylicpeadf

sd
shdo
igskvq

htwfobiycmpdxnzlrujk
uwzrcfxtnmbpyohlidj
zvqwdcoipfxmerusbajlhnyt

hzwv
whyv
hwvz
bvhlrwuj

u
tf
sbrc
y

slbfguyrjqhx
rygfqlsuhx
ygxsqhrluf

xsrjiu
uweprjg
pjru
yjhmcfunvrqk
irjuw

zdrjswcaik
tcikawjuzvdxrn
zcrihjwakd
radzyickjw
wadjkecizr

kvdeitchowuyxljqmabr
klqymaidcxojvwhuebrt
cmurhebtxwkoavqiyjdl
wvabixhqeoydktmrujcl
ajemidblvtycqhkrwxuo

ufhiespvlbrcqygjakz
cfsphiegkvzjaqyrblu
iaruqfsepgylkzcbjhv
bgfpashzvljqkuicyer

vjrmlnwzohcyfdxuatqgbpkie
bnqdyilruvescagwkxmthfojzp
xufzhqwciplbronmjtdavkyeg
whmrckbzdgfauqlyjeiotpxvn

i
ik
i

omtzex
yiwu
rhmnkgtj

yu
yu
yu
ucy
yu

lfbtyapow
ly
cvly

mxyphzlcgdjobawi
dzkcsjltapygoqufh

tycelnwdrvoubimhk
mdbivklcetyrwunoh

o
o
o
o

v
x
v
zv

cjavufbmswohnldpgrkt
phbmwjtofsgxckul
lyuhgmfjoswpxbctk
wlokhucbgsmejztfp

ovuitnkzey
gxhapflrb

qzd
zdjq

dqnbfjustlizexkgymr
gfrziynmkdtsjeql
tfayqdlrsizkngemj
tfyrnesizmgqjlkd
lgadikzmernwfsjtqy

reklgsoxbfwmqanvu
uolmkbanfyqgxpsrwv
khoswagrvxfqblmtnu
udlngfvmkqoxyrwbas

gzjqcoa
qt
bdtqlp

ih
hyi
hi
hif

yhisc
htxsaujicm
ishc
klhcies

gimjckpobfq
qogcmipbf

diqbsenjz
yakmchngwfpj
qxoernzdjvli

rlnbsqgfx
qsfnxlreb
fxlsgbqnrt
fszxqdgltnbre
qrbcxlpasfn

kczwo
ckdwoz
kqocuwz
wozckd

nlqgxw
xgnlqw
wqxngl
qwnxlg

rwxhuogzcjpfev
pixrgosatwhcbfzvj
hgvoyqwfpzxcnrj
pjrzhfqcgwxov

pvier
mripe
ipvbr
shcjiwoargp

aigpjvwdmyrlxsohkecut
ylinsgxukmcpwdetrjahv

ps
q
r

cm
mc
mc
mc

c
c
c
c
c

astrzjgc
arsz
szar
rszai
ayrzsl

gpjaqzvdtouxrmlciyefkb
gowrpcndejqiztuykvfsam

axbeqi
kexaqbi
xeaqbi
axbeqi
qaeibx

vazjticxqo
aqtjzvioc
iozcajvt
zcoitajgv
ibjlncovzta

gaz
g
gef

xbg
bgx
xbg
bgx

sm
sm
sm
ksm

rjmktglu
rjbfuc
juhri
jur

wxkrupn
ydzxbclvegnptrsu
nurxpa
nruphx
uxmrjnqp

fibazcjq
iqzabcfj
fqzibjacg
czjfqiba
abczjfiq

aqehugzcosv
imwnfcjk
dtyrlpxknbic

m
m
m
m
m

xwi
xwi
wix
xwi

ikyrwtsjo
sntyi
tyis

fjlt
jflt
tlfj
tlfj
ljtf

upzaxnkvohebcw
meqitclwfsrhkyj

bhi
bihvd
ewihub

tzxswligejqkn
pktiwcexzluvnhj

hkip
chp
g

ojnqulc
nupjmcleikyb

izbtdsufmjpewkrlyg
kwrfpusdimlzgebj
ilgcmrhbvkjduwspefqz

zouqmp
muq
mqu
mutcq
muozqp

yfncdoza
zdonyfjac
yadcfnzo
agodcyzfn
zndyocfa

s
s
s

fdylvisp
crzytblojaunei
yclgkqtwui

mo
mz
dnm

hbd
h
ct

gloqe
leog
exlo
oe
ejwor

byznh
rueczpmxo

rdtnicsag
xswrgiaqucn
gsericaqn
zcauinrwgfs

zmwekqucjobahgvsypx
okqmveubjwaxthcpygsz
shvofekzxqmaucpdjywbg
qwcefjzmkghsxaybuopv
cpwhsqkanjzlmouvgbxey

b
b
b
os
b

fgdkrtovwxmcqau
xlhutvowmgfacp
ysbegzuwnfoacxvt
fmalxitohjcgwvu

kufdawncqr
ftcnsuraxwbok
qupfncdwkraz

ujembfoqtlhkxnipz
mqkzehnupijbofxtl
fezkqiolpjmhtuxbn
ukpftihomblnxzjeq
fekoztlbipmnjuqhx

wuantesoxgzlkdyv
aeonwtksudylxgzv
vxogzenswdtculaky
eadntklvowxsyzgu
ktzeogldvuysxnaw

t
qt

hyanftqlru
faqnyurlht
lhtaryfqun
lashwuftqnyrk

ujekx
aep

fnhzwlpbktujeqds
nfbzhjeksgqlowxp

us
jbcao
xkp
mp
zkpl

baesofy
oyesf
seqyh
stapey
uesy

vtp
vtp
vpt
pvt
tpv

fploymws
wyfosmpl
wlopfysm
owmylpsf

az
za
za
az
az

wjrv
vjubnr
qdtjvys
jvp
jcuv

qrhynskzmxlduoftcwg
xwnzchoylfgdrmkqtu
kcmnwfxhqdrylousgzt
qusjzclktfmgwrhdxyon
bxwhmyqzdfoilnutckrg

aqp
l
z
c
c

hdlofpgw
wpchuflo

dxrezotclpb
eplobcxtdzry
rpzxboltcde
deobtupzvcxlr
cvnboptxrlzde

uja
uja
aujx

z
gmw

escljbdgo
tdoyqghj
chdtjugo
ohdjug
pfjwnmrogadvi

bl
lcb
lb
klb
bl

vyrtk
hvaitkry
nyerqtvlkx
jrvytku

wyjvfpqsxiotg
swjotvxqgy
sbcaotgrhqjvyexlw
toygjqxvwis
ytvxjwgqso

b
jb
b
b
b

hmoiwxluftbvyekj
fkvteiyojwbmlxh
ciqtkfvjgymenoxwldbp

uvsfb
vf
gefdojtv
vfm
mfpv

xrzvt
xtrv
hxtvr
vxrdbnt
rtxvz

hctgpj
vctpeqgkrmloyhj
cpghzdtj
thcjgp

oxd
xod
xod
xomdr
dxo

no
a

erjmoxdywnilqhtf
iuqjlmswzreoxfvphny

gqlyohipcdnsmfvwjaxkbe
wsqholxbkaegijyvfmdpnc
laqkcdhpwgsvojeybmfinx

mnec
mnc
cnm
mnc

ympar
gcjhp
dqvxznwbueilkotfs

retqbluxmovzcjpysia
xsqlpyfjmeztocunvirba
pozeqluyjscmibtarxv

tj
htj
jt
tj
tj

xhvictnm
kwpqvufoylb

ksecubljnawx
uxnfkeljbrpsdz

kcljaxwtopmqg
xktwagqponmjl

bqemuordtawylnivpchx
cpwgotxmnjrbdliqaev
iqtwpacxebmlnsdrov

ze
bhnrk

quranol
roulaqvy
aulqroi

btl
fbtu
dabkth
bts

czq
cq
cq
qc

rpwdmgqfxuhesynkl
jknhxtigcays
ghnyoixjazsk

ovrhfpykmdctusixzlaew
hcodefmtvbgsxruqiwlpkjn

w
w
w

vbwxs
bxvws
mkbfwxsv

rcksmaoz
lvu
pq
ht

tzsvfeapbxlmcri
mbtplrfexvcszai
axmpszicltfvrbed
clamxvbezsprift

kyglmxchpiw
ukcmpjwygxhli
wkygixhlczpm

xvrcmntzgheu
dbjkwlpqcix

rgmusakc
msgurca
uxgscaomkr
gjwfudczbrmtnas
magcusr

rtlsbvnimh
bclehvunx
hqjvpyabdf
ovbhex
nhkbv

achivfdsgwbmxjoez
fahrgmbnuqeztpvoc

yjimzdhsbrtxocvkulanegfpwq
fwhkrjxpbqmvyiasduetncolgz

oybpwzaumf
ypfoaedmzuxw
mawpfuzoy
wfapyoulzm
wmlyuafzoqp

qamnfijrbzwduocvleyxshtpkg
udwjyghpmlqoczrbxfsekt
xrblgfoyedsmqwctzukpjh

ctjumdkwfyvlrep
ckjqfwsauytzo

vflnuezdymakghjs
dgczlrueyfkmqj
yjzkwgludmef
glfmjykiudez
zjobfutkpmydelrg

ral
lgear
lra
lra

ljytdae
ladujtef
jdptlaoxe
jdyaelt

hwgkadmsnr
hrdakwgcsm
ramhslwdgk
yahlgscdmwkur

spj
sj
jstc

tpfjr
nyrfdlis
fjthr

l
g
g
g

awyvnf
vynaf
yavfn
nfavy

jsycn
qsymphni

wgnpjmtsvyh
wjgvspnyh
spjvgnywh
ygwnsvjph

ghwey
zupo
bd
xvub
rmu

ko
ok
ok

xqchrioeazbkvdygtsl
ahqcdbgkvtzoeysxilr

xjpykfoh
tfkcxopjh

zslnekgdtvyxo
ovxzyedktfngws
ovtxyqednsrkzg
yvkdqsztogxne
lgesztknqcxdymuhov

slhzwtiq
ziwhqtls
qzitsjxlwh

typdxr
urxtpy
tyrxp
txyrp
xrypt

oetyznfr
fntozyrx
hwaryotncfzvkj
inftzyor

lmqxngr
zgrelxqa
pkjgvdqtyclforx
suiqrgxlb
hlwxbgrq

pi
pci
thiyjpw
lmjpfti
pri

cykj
cjlkg
zjvkc

udihpjmfytbeskzv
zihutbpeysmvkjdf
kyhmpibtzuedfvsj

upc
ud
otmuy
ul

zlyfivurdqckmbjh
edmlbyjfvhuk
mlndjsagvfbwptxhy

ryenbvawhdqpkmf
owkehyranzvbmdfqp

pv
vp
pv

yfuz
yzuf
zfuy
zfuy
fzyu

abntu
nojuhst
tbfu
gvirxum

owgmci
ycoxmagw
qmowhcv

sgrmtfonvwlyi
wsyktlrnfihmv
lrftbaqwmnsyie
tpfylnrkwmis
nfowgyrilutms

siw
stg
s
sg

gswpatobqz
tqgdyzbopsaw
optaqszgfvwb
wzspagbotiqy
gpwbzstqoa

hpmeifxjwlzsadrytuc
fjrhvyacxuwodpet
pxcwitdhfeuyraj

nucleq
nqucel
uneqvcl
ceulnq
nlucqe

hrz
qprg
rzxm
rj

ltudnjkyxrae
ovljzxudgktr
kjilsumrdtxw

mg
gm
mg
gm
mg

vdrhzfaijp
ijprxvwt
rtpcixvj

cudpsrbgjvtw
mwbtjpscudr
fpjywbontrzcs
bcwsijrpt
dctrwplbjs

hgmjplf
hmlxgp
lgmpxh

duyj
wjcmd
fapbqvjdh

wrysjfdplgov
deznmktc

jairuwz
juoaib
jkiouya

yudqfn
zfqundy
uqdynf
qfdukyn

vqwido
qviado
qdivo
kgodqvhi

vrzysiwfmucdhnlxbtpe
nphxzelrmcyvituba
uebmctvxyjzlirphn
iqxobnuhrtckeyvpmlz

mb
a
stzg
mp
mk

pc
c
c
c
c

byacjmdq
dcbqymaj

sbvfp
bxsoqpwuvide

scjmloprtyexdaufhgn
qzthrdveixogscmbpfj

ixlesvzjnrfwtpgqkabyd
zktsfxadvpbgwrnlyjq
jadfmrxvtgykpbznslqw

wiscjd
qscjwid
swdcij
jwcdsi
siwjdc

mafcigperqutny
rhtdceaxnijzlvq
xlsqckadbvnwetir

ginltobkcuyvxdewmpa
gwbpmcytzvilkeujad
mqsyvgwdteiauclfbkp

ryzscdbevj
wayrbivcmtnuo
gervcbyqjd

uvdg
ugvqwmd
svugd
cgyhudfnv
vugd

i
i
i
oi
sid

nyulf
unylf
lufyn

mqsgtywlexjvib
tejyvxblgimwqs
bwtdeymxgslijkqvc
ygwtxqjvlsebmi

zufj
zuf

tf
v
ova
o
o

sxkcngriqjopeulybdfh
ykdgelruhxnpoicbqsjf

fwypdk
yfwdk

gqkp
qkpg
qpkg
qpgk
pgqk

khfnscbly
zfhbclsynk
lkybcqsnh
lkbynhsc
hbskycln

fevoigpcwtbzy
nleyjchafqkz

reowqgsjyxn
tijopa
zajfholi
pzjodcal

eujmvws
tzegmsiuj
hubnmwsjxe

zotxy
ytox
yxto
toxny
yxot

jnqzdpsmraikwfoghtxue
mthgnwpizudkraeqfsvx
zqxiasmpkrwegufnvydht
wraftbkmnilshugzedqxp
myfszgdxwnatupihrqek

d
id

vgit
tigv
tgvi

yghsexuowr
hjwpfrn
nrdtazwfh

ulzscyvhbedmkrpaoxjq
kfmlpzqwvuyrjntdabochi
kjldbrhzvmgyoaqepcu

lbedykfihuwrqjga
tzdaycqijxvnofpms

sjaxwn
asnxj
jasnx
xjsna

ynuefovwlzkjrhtadqbcmpx
alsrtouvejnzkpghimq
sgjrzluknaetvmpqohi

xptglvrwmnqeday
dgmwcevqraylntpx
awxgsypldervmqtz

kxjcwuhgd
luikjwxna

eypfmkhltigbqjr
lgqkyrhfjmpe
vlkpdyhenjzqg

yhomsubzwtanxieglfcpr
tsmfaobhuwrxgclpizeyn
amyrsibwhfuelcgzoxpnt

audfoqglzwbmxi
atezlmidbukqsxo
iubndahyxmvoqjrz
czstqouxbamdki

vxcym
jxypngvm

vcjqyfwarnpse
cznywqpraletsvuj
epknqavjywgcrs

zcasgw
zhgwm

q
j
gy
j
j

x
y
x

g
rg
g
g

uqtbyxnprvsmoziw
hgrosbuwndt
sbgownrtdu

tnmpvryj
boyvpjqinzrmct
rvyptmjn
nrmpytvj
hjpytrvnm

tohzgmpsbd
agzhdstmbo

rjoxmsunfz
dpualvqbhfwejo
xcyujfkrgo

oknfcvwdehsyp
chdykwzeasovnfpt
opemfhcbdvsnywk

bqksxvplr
jkyeqbczfwrl
ukqrlbo

xmjfswhtepvilu
uvietwmjzlxfsh
mwfjsuotihlvexc

rcmgbjyuwknhqfxazpi
rfixclqeagwpyukm
gowulqdpxracfysmki
furqvmasypwxckig

qocmhepgrsadk
hotakpeqcgsnvmrdj

hsadgzu
dakwghtlosfz
ipyjaqnxbvcm

iyzxjgwpn
azgw
wzg
zwg
gwzt

kd
kd
dk
dk
uwqdfbnrk

qgevndtsowlmbpuyca
fsgrdkhcixbtqeyzju

v
jbiq

d
d
bld
qd
d

bupgemxrocniwhltyj
bnrhvefuqitwxpadjzg

ulz
wkpnzsr

du
jut
ujp

vjomkthxbwezfaq
fqzhkovtejbwmxa
evfwkjxaqhbztmo
afojmbxehtsqzvwk
azxfhjqbokwvemt

skbeotiuaqpfzvcr
fuaopcrzviesbtq
eqtsouizcvfapbr
tuzifcpqreoasbv

vbaexcuwtzi
tvhabzwgux
etazxbvu
lakqvuxzbnto

akmuwnefdzoi
lfbnetdxagwzcu

cgut
cgt
gcut
tgc
tjcog

meswxbkv
kxqdacuysmjeb
mbdsecryjkxa

uczsvyqhn
zvshjyncxur
mchaunybvsz
nvhzyscu
vczyhnus

rwufbi
iucbf
ifub
ibuf
ubfoi

herxnv
hnxrev
hrevnx
nihverx

oarje
eaojr
earjomt
ajiroe
eauokrj

i
v

hfizv
mzsigcojf
fzia

p
p
p

sduajrytgfeqipmclwvnhzox
pldgorsanitxuhzjqevwymcf
afpxlwzsimtcryhnujqdegov
scjtheoaynidugrvwzmqlpfx

ubxzioenaqhvdfj
qbpxnwufaihevjyo
qznuhbfjovaxei
ibeuaovxqznfjh

gvynpistahco
xaipcvthnoy
tiocvnakhyp

jdz
mvrzdi
hbtzlodnyc
pdz

z
ge
yonxvl

ikuebtopyx
uxtbkiehpo
bidqkezluoxwt

axiklvqhebtf
vfgxrhdi

aicedpvysfhrw
wfdcsyehavrip
tvdicyrspfeahw

ogdnu
ywpnlodb
hdnorw

sclvgamkurpwzdbyqoien
wqgxeutjonpziklbma
lqinmbgekaowzup
webzlumakoigqnp

s
b
b
b

kiry
arm
sqtxclu

qbkl
ekwjlfxq
qkl
lqkv
qklc

ygzincjhtdlvxqwuosb
hngptjwzxislvcbdoyuq

rvoxnejykzscfudtgi
jdkoentifrzvcygsux
kryitcznsdujogefxv
xiygudzeovsfnjtcrk
fknotuvcdexsygjzir

xq
xt
x

xdkrwqputigyajze
swnbfomjclvh

w
lhrt
cj
u
nxcb

qk
q
q

mjafwbpvoklt
ojavmbwplkf
blvaokmjwfp
ovjmdpbfwktla
kpalobujvfwm

o
o
o

eva
qcv
rsloxgdwnmfi
zcb

konzxcldaw
nzwsouarxlf
onqlzwbvxa
owaxqlzn

vornwcbd
odeacqur
pcfkxshogt

bzyiswgjaplqrmucnt
mrwqcdzytsgpaniljb
qpstmlrunbwcgyijaz
wtklbrsaicnjqpmgzy

lixqjmvwscabofzgekhr
bewcrfvozxtjiqkaslmgh
fxvrgmlibozceqhjsawk

dnzcarkvpwmbjqyit
bezpcaiyfkwnmtjrdq
bxjtqmakndwyrisczp
dpiymvtjzcbkqanlrwe
gdyctfvnmkjowqhprbazi

fhr
hrf
yunrfh
rhf

baehycmkjovgnpi
vnokepjcmbhiya

xvltzoednwuq
bsnwprxvdulyzqeat
lijmhvnuzexdqwt
zjdlvtunwxeq
zmnlwxtuqevd

rspkajy
pskra
fkepatrs
sprka

ltvzbjgh
albhtjyvzk
zvjbtelh
lhjbvtzk
hdvtzlkjb

czvmwjaghquxslrkteib
qxrahpukngbmwejzcsy

xhfsuorb
volzamjey

pgendrayv
urctvbdy
fpqndkvy
oidsvwh
gydvck

wferdzc
cdfzewr

a
lx
a
a
a

kncvymsgfa
cfqanuydkg
fktnycago
xgkerpcfyna
anwuhtfikgcy

cpeh
dpqiksmzwr

wbzokycijumplxrfhvnq
vqonfwreaidkxbhsp

kmlnw
klmn
mklng
lknmg

ojbykxcefdshgrwimtqp
gmqedbfxpwntkrcjho
tkexprjngfwdmcohqb
mepqwjrxkbgdtcfho

avtklxnmujiwr
tknaprujwiv
aywvgfnitrck

nizxaebqrkcwvjut
mrgodaztnipsjbxlq
rhbqntaiuxzj

kfjwgmlyr
notbhxdicavqs

vaqidgkolexjcnbys
itwlxyesqocjprdunb
ncoyelzfsmbhqxji

w
q

myhultgvxew
obcsfrklqaxpij

tujq
uqztxbj
ajgumtqlvsewrc
tqjnou

wvlxdsajnc
ajvrwhkspn

gz
gez
ze
yxz

luyj
ljduny
ljyu
yjul
juyl

gbpfexukwdljnvaromisqhc
ezsaumkfvxpnchdtlborqjwgi

gzklpuaqehvio
sijxncbmwfy

vkwnrcyth
vectwfk

sg
s
s

az
caz
zfta
caz

jlrifchmk
irkjhmcfl
ifqmpklchjrb
kcjmlfhri
ilmkhfcjr

tjnqf
ncyzf
f
fo
lxdrgsfihbew

ntirwquhv
qwvhyuintr

gvunymbitk
dsbywnmzk
qjanlhbxmroc

pxsdylnmfhq
pyduhnqmfxl
dpmqchxtnlbyf
hnpqlxydfm'''


values = '''ggggttbitk
dsbywnmzk
pjanlhbxmroc

pxsdylnmfhq
pyduhnqmfxl
dpmqchxtnlbyf
hnpqlxydfm'''

#values = values.split('\n')
#print(values)
letter = []
letters = []

for v in values:
    if v == '':
        letter.append(values.split('\n')[0])
    else:
        letters.append(letter)
        letter = []
letters.append(letter)       
print(letters)
    


 




