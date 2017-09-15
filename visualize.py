# -*- coding: cp949 -*-
import matplotlib.pyplot as plt

def visualize(a, k):
  for i in range(int(a)):  
    file = open("C:\dualfoil5\df5.1\dualfoil"+str(i+1)+"out.txt", "r")

    sw=0
    time=[]
    volt=[]
    while True:
        fline = file.readline()
        if not fline: break
        ch = fline.split(' ')
        if len(ch)>14 and not('heat' in ch) and not('energy' in ch) and not('mass' in ch):   
           if '0.000,' in ch or sw == 1:
                sw=1
                if ch[2] != '':
                   t=ch[2] #시간 저장
                   v=ch[6] #vol 저장
                elif ch[3] != '' and ch[2] == '':
                  t=ch[3] #시간 저장
                  v=ch[7] #vol 저장
                elif ch[4] != '' and ch[2] == '' and ch[3] == '':
                  t=ch[4] #시간 저장
                  v=ch[8] #vol 저장  
                t = t.replace(',', '')
                v = v.replace(',', '')
                time.append(float(t))
                volt.append(float(v))


    plt.figure()
    plt.plot(time, volt)
    plt.grid()
    plt.xlabel('time(sec)')
    plt.ylabel('volt(V)')
    plt.show()
