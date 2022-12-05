
"""
0 = rank
1 = team
2 = age
3 = W
4 = L
5 = PW
6 = PL
7 = MOV
8 = SOS
9 = SRS
10 = ORtg
11 = DRtg
12 = NRtg
13 = Pace 
14 = FTr
15 = 3PAr
16 = TS%
17 = eFG%
18 = TOV%
19 = ORB%
20 = FT/FGA
21 = D_eFG%
22 = D_TOV%
23 = D_RB%
24 = D_FT/FGA
25 = Arena
26 = Attend.
27 = Attend./game
"""
orArray = [4,'Memphis Grizzlies*',24,56,26,55,27,5.68,-0.32,5.37,114.6,109,+5.6,100.3,0.245,0.346,0.553,0.522,11.2,30,0.18,0.523,13.3,77.8,0.195,'FedEx Forum',646785,15775]

#anArr = [15,18,19,20,21, 22, 24]
#Reg Group 1

anArr = [2, 16, 18, 19, 20, 21, 22, 23, 24]
#Reg Group 3


finalArr=[]
for i in range(len(orArray)-1):
    if i in anArr:
        finalArr.append(orArray[i])

print(finalArr)