#   Make a class BinaryCounter which consists of 4 Leds, and define methods to represent the value it represents in binary,
#   as a decimal and as a hexadecimal. Also provide a method to increment and decrement the value of the BinaryCounter.

#   For example the value 7 is represented by led3: 0, led2: 1, led1: 1, led0: 1
import math
class BinaryCounter():

  led = [0,0,0,0]
  def __init__(self):
    pass

  def numberToBinary(self, x):
    led = self.led
    
    if x >= 16:
      print("Need number lower than 16")
      return [0]
    else:
      for i in range(4): 
        if x % 2 == 1:
          led.insert(0, 1)
        else:
          led.insert(0, 0)
        x = math.floor(x/2)
    return led

counter = BinaryCounter()

x = counter.numberToBinary(5)
output = ""
for i in range(0, 4):
  output += str(x[i])
print(output)