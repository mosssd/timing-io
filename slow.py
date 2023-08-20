import time

start_time = time.time()
for i in range(100000):
  x = i
  print(x) 
end_time = time.time()

print("time taken in execution is :", end_time - start_time)