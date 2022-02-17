import os
    
os.system("clear")
print ('\033[1;97m \033[1;40m welcome')
but = 0
while but != 5:
    print ('\033[1;97m\033[1;40m===' * 10)
    print ('''\033[1;97m \033[1;40m 
    [ 1 ] calc resistance
    [ 2 ] calt voltagem
    [ 3 ] calc ampers
    [ 4 ] resistor
    [ 5 ] exit
    ''')
    print ('===' * 10)
    but = int(input('choose an option \n>>> '))
    os.system("clear")
    print ('===' * 10)
    os.system("clear")
    if but == 1:
      os.system("clear")
      vol = float(input('volt batt \n>>> '))
      vol2 = float(input('volt elet \n>>> '))
      cor = float(input('ampers \n>>> '))
      calc1 = vol-vol2
      calc2 = calc1/cor
      print('result =', calc2)
      print ('===' * 10)
      but = int(input('[ 0 ] back \n>>> '))
      os.system("clear")
    if but == 2:
      os.system("clear")
      print ('===' * 10)
      cor = float(input('amper \n>>> '))
      res = float(input('resistance \n>>> '))
      calc = cor*res 
      print ('result =', calc)
      print ('===' * 10)
      but = int(input('[ 0 ] back \n>>> '))
      os.system("clear")
    if but == 3:
      os.system("clear")
      print ('===' * 10)
      print ('current')
      vol = float(input('volt batt \n>>> '))
      res = float(input('resistance \n>>> '))
      calc = vol/res 
      print ('result =', calc)
      print ('===' * 10)
      but = int(input('[ 0 ] back \n>>> '))
      os.system("clear")
    if but == 4:
      os.system("clear")
      print ('===' * 11)
      print ('          band 1 | band 2 | mul. ')
      print ('negro    =   0       0      1Ω        ')
      print ('cafe     =   1       1      10Ω       ')
      print ('rojo     =   2       2      100Ω       ')
      print ('naranjab =   3       3      1KΩ       ')
      print ('amarillo =   4       4      10KΩ       ')
      print ('verde    =   5       5      100KΩ       ')
      print ('azul     =   6       6      1MΩ       ')
      print ('lila     =   7       7      10MΩ       ')
      print ('gris     =   8       8             ')
      print ('blanco   =   9       9             ')
      print ('===' * 11)
      but = int(input('[ 0 ] back \n>>> '))
      os.system("clear")
