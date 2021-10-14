#   Make a class BinaryCounter which consists of 4 Leds, and define methods to represent the value it represents in binary,
#   as a decimal and as a hexadecimal. Also provide a method to increment and decrement the value of the BinaryCounter.

#   For example the value 7 is represented by led3: 0, led2: 1, led1: 1, led0: 1
import math
class BinaryCounter:

  def __init__(self):
    self.__ledState =0
    pass

  def numberToBinary(self):
    return  bin(self.__ledState)

  def numberToHex(self):
    return hex(self.__ledState)

  def numberToDecimal(self):
    return self.__ledState

  def Increment(self):
    if self.__ledState < 16: #limit to 4 leds > 4^2 = 16
      self.__ledState +=1

  def Decrement(self):
    if self.__ledState > 0:
      self.__ledState -=1
    