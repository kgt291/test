# -*- coding: cp949 -*-
import os
import sys
import krr
import start
import visualize

if __name__ == "__main__" : 
  while True:
    batteryNum = input("���͸��� ����(4, 8 �� �ϳ�): ")
    k = input("kRR �� k��(1, 2, 4, 8 �� �ϳ�) ����: ")
    
    
    if int(batteryNum) < int(k):
      print("�ٽ� �Է����ּ���.")
      continue
    if int(batteryNum) != 4 and int(batteryNum) != 8:
      print("�ٽ� �Է����ּ���.")
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
      print("�ٽ� �Է����ּ���.")

    

      




