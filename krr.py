# -*- coding: cp949 -*-
import os
import sys
import write
import random
from heapq import *

def krr(a, k):
   chance = 1
   chance2 = 1
   item = 0
   time = 0.000
   cuv = [[0.0 for col in range(int(a))] for row in range(100)] # current �з� �۾� ���� ����
   tv = [[0.0 for t in range(int(a))] for tt in range(100)]
   stop = [0 for s in range(int(a))]
   cut = [0 for s in range(int(a))]
   duration = [0.0 for d in range(int(a))]
   timesw = 0
   fcu = 0.0
   loc = 0
   curr=[60.0, 110.0, 230.0, 90.0, 40.0, 200.0, 120.0, 170.0, 20.0, 80.0] #���� queue
   charge = [-80.0, -120.0, -40.0] #���� ť
   curr2=[60.0, 110.0, 50.0, 80.0, 60.0, 40.0, 100.0, 70.0, 90.0, 120.0] #���� queue
   for j in range(int(a)):
        if int(a) == 4:
           fcu = 80.0/float(k)
           tu = 5.0
        else:
           fcu = 120.0/float(k)
           tu = 5.0
        if j < int(k) :
           cuv[0][j] = fcu
           tv[0][j] = tu
        else :
           cuv[0][j] = 0.0
           tv[0][j] = tu
   for h in range(100):
     print('try' + str(h+1)) 
     check = [0 for i in range(int(a))] 
     flt = 0.0000 
     volt = []
     pretime = time
     if int(a) == 4:
        time = time + tv[chance-1][0]
     else:
        time = time + tv[chance-1][0]
     time = round(time, 3)
     if timesw == 0 or time == round(time):    
        endtime = str(time) + '00,'
     elif time == round(time, 2):
        endtime = str(time) + '0,'
     else:
        endtime = str(time) + ','

     for i in range(0,int(a)):
        chkvol = str(cuv[chance-1][i])+'0,'
        if stop[i] == 1: #���͸��� ���̻� �������� ���� ���
          print('battery' + str(i+1)) 
          print('x')
        else:   
          os.system('cp dualfoil'+ str(i+1) +'.txt dualfoil5.in') #input���� ����
          os.system('g77 dualfoil5.1.f -o a' + str(i+1) +'.exe') #dualfoil ������
          os.system('a'+ str(i+1)) #dualfoil ����
          print('battery' + str(i+1))
          f = open('dualfoil5.out', 'r')
          while True:
            line = f.readline()
            if not line: break
            cha = line.split(' ')
            if 'converged' in cha: stop[i] = 1 #���̻� �۾� �� �ϸ� ����
            if endtime in cha:
               if endtime == cha[4]:  key = cha[8]
               elif endtime == cha[3]:  key = cha[7]
               else: key = cha[6]
               vol = key.replace(',', '')
               cut[i] = 0
               check[i] = 1
               print('time: ' + str(time) +'min')
               print('volt: ' + str(vol) +'V')
               flt = float(vol)
               heappush(volt, (flt, i)) #heap queue�� (volt, �ش� volt�� ��ȣ�� Ʃ�� ���·�) ����
            if chkvol in cha: # ������ 5�� ���� �� �� ��� �� �۾��� �̾�ް� �ϱ� ���� ��ġ
               if cha[2] != '':
                 if float(cha[6].replace(',', '')) < 2.1:
                   duration[i] = float(cha[2].replace(',', '')) 
               elif cha[3] != '' and cha[2]=='':
                 if float(cha[7].replace(',', '')) < 2.1: 
                   duration[i] = float(cha[3].replace(',', ''))
               elif cha[4] != '' and cha[3]=='' and cha[2]=='':
                 if float(cha[8].replace(',', '')) < 2.1:  
                  duration[i] = float(cha[4].replace(',', ''))
          f.close()
          os.system('cp dualfoil5.out dualfoil'+ str(i+1) +'out.txt') #output���� ����


     
     if not volt: break #���̻� volt�� �ƹ��͵� ������ �۾� ���� ��
     
     stopnum = 0
     direction = 0
     for c in range(int(a)):
        if check[c] == 0: # 5�� ���� �����۾� ���� �ߴ��� check
          if cut[c] == 0: # cutoff ���� �۾��������� ���� check
             cut[c] = 1
             time = round(duration[c], 3)
             stopnum = 1
             timesw = 1
             direction = c

         
     m = int(k)    
     t = (0.000, 0)
     v = [0 for u in range(m)]
     num = [0 for nu in range(m)]
     vv=0
     nn=0
     length = len(volt)
     if int(a) == 4 and chance2%11 == 10 : #������ �� SOC���� ������� pop
       chance2 = chance2 + 1 
       for j in range(length):
         if j >= m: break
         t= heappop(volt)
         v[vv]=t[0]
         num[nn]=t[1]
         vv = vv+1
         nn = nn+1

     elif int(a) == 8 and chance2%11 == 10 :  #������ �� SOC���� ������� pop
        chance2 = chance2 + 1 
        for j in range(length):
          if j >= m: break
          t= heappop(volt)
          v[vv]=t[0]
          num[nn]=t[1]
          vv = vv+1
          nn = nn+1

     else: #������ �� SOC ū ������� pop
      if stopnum == 0: chance2 = chance2 + 1   
      for j in range(length):
        if j >= length-(m-1):
          vv = vv+1
          nn = nn+1
          t = heappop(volt) #heap queue���� volt�� ���� ���� ������ ���� pop��
          v[vv]=t[0]  #�ش� volt 
          num[nn]=t[1]  #���͸� ��ȣ
        else:
          t = heappop(volt) #heap queue���� volt�� ���� ���� ������ ���� pop��
          v[vv]=t[0]
          num[nn]=t[1]

     
     for l in range(int(a)):  
       if l in num:
         if int(a) == 4:
            if stopnum == 1:
                 cuv[chance][l]=cuv[chance-1][direction]
            else:
               if chance2%11 == 10:
                  cuv[chance][l] = charge[loc]/float(m)
               else:   
                  cuv[chance][l]=curr[item]/float(m) 
              
         else:
            if stopnum == 1:
               cuv[chance][l]=cuv[chance-1][direction]
            else:
               if chance2%11 == 10:
                  cuv[chance][l] = charge[loc]/float(m)
               else:   
                  cuv[chance][l]=curr2[item]/float(m)
       else:
         cuv[chance][l]=0.0 #rest

     if chance2%11 == 10: loc= loc+1 
     else: item = item + 1
     if item == 10: item = 0
     if loc == 3: loc = 0
                 
     for tm in range(int(a)):
       if stopnum==1:
          tv[chance-1][tm] = round(time - pretime, 3)
          if tv[chance-2][tm] == 5.0:
                pos = 5.000 - tv[chance-1][tm]
          elif tv[chance-3][tm] + tv[chance-2][tm] == 5.0:
             pos = 5.000 - tv[chance-1][tm]
          elif tv[chance-4][tm] + tv[chance-3][tm] + tv[chance-2][tm] == 5.0:
             pos = 5.000 - tv[chance-1][tm]   
          else:
             pos = 5.000 - (tv[chance-2][tm] + tv[chance-1][tm])
          tv[chance][tm] = round(pos, 3)
       else:
         if int(a) == 8:
          if (chance2-1)%11 == 10:
            tv[chance][tm]= 5.0
          else:
            tv[chance][tm]= 5.0
         else:
           tv[chance][tm]= 5.0

     if tv[chance-1][direction]+tv[chance-2][direction]+tv[chance-3][direction] < 5.000: break #5�� �ȿ� ���� ����� ��
     chance=chance+1 #���� Ƚ��
     write.write(a, num, chance, cuv, stop, tv) #����� �������� input���Ͽ� �Է�

   print("end\n")
