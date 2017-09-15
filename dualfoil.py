# -*- coding: cp949 -*-
import os
import sys
import krr
import start
import visualize

if __name__ == "__main__" : 
  while True:
    batteryNum = input("배터리의 개수(4, 8 중 하나): ")
    k = input("kRR 중 k값(1, 2, 4, 8 중 하나) 선택: ")
    
    
    if int(batteryNum) < int(k):
      print("다시 입력해주세요.")
      continue
    if int(batteryNum) != 4 and int(batteryNum) != 8:
      print("다시 입력해주세요.")
      continue

    if int(k) == 1:
      start.startkrr(batteryNum,k)
      krr.krr(batteryNum, k)
      visualize.visualize(batteryNum, k)
      
    elif int(k) == 2 :
      start.startkrr(batteryNum,k)
      krr.krr(batteryNum, k)
      visualize.visualize(batteryNum, k)
      
    elif int(k) == 4 :
      start.startkrr(batteryNum,k)
      krr.krr(batteryNum, k)
      visualize.visualize(batteryNum, k)
      
    elif int(k) == 8 :
      start.startkrr(batteryNum,k)
      krr.krr(batteryNum, k)
      visualize.visualize(batteryNum, k)
      
    else :
      print("다시 입력해주세요.")

    

      




