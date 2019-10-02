# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:17:34 2019

@author: Marlon
"""
def fatorar(n):
  fat = []
  if ( n == 0):
    return fat
  elif(n==1):
      fat.append(1)
      return fat
  else:    
      
      for i in range(2,n+1):          
          while n % i == 0:
              n = n/i
              fat.append(i)
      return fat


if __name__ == '__main__':
    decompor = 198
    fatores = fatorar(decompor)
    fatoresTxt = str(decompor) + ' = ';
    for i in fatores:
        fatoresTxt = fatoresTxt + str(i) + ' x '
    
    print(fatoresTxt[:len(fatoresTxt)-3])
        
        