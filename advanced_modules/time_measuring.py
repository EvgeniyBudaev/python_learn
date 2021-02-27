import time

input('Press Enter to start')

# start_time = time.time() # deprecated
#start_time = time.monotonic()
start_time = time.perf_counter() # для более точных результатов чем monotonic
for i in range(1000000):
  x = i * i
# end_time = time.time() # deprecated
# end_time = time.monotonic()
end_time = time.perf_counter()
print(end_time-start_time)  
