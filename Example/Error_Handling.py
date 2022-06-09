#error
#we try to execute code under try block lines
try:
    #change w to r to get other outputs
  f=open('BlackHat.txt','w')
  f.write("kot")
#if we handle a input or output error we execute this code
except IOError:
  print("Error")
#if except isnt executed else is executed
else:
    print("dnd")
#finally is executed every time in the end
finally:
    print("ok")