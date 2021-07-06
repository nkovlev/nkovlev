import random
Array = [random.randint(-100, 100) for i in range(30)]
MaxN = max(Array)

print(Array)
print("Максимальный елемент это  " + str(MaxN))
print("Этот елемент на  " + str(Array.index(MaxN)+1) + "месте")

for i in range(29):
  if Array[i]<0 and Array[i+1]<0:
    print("Номера : " + str(Array[i]) + " и " + str(Array[i+1]))