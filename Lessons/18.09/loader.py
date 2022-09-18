
import timer

timer.finish()
timer.start()

for i in range(10000000):
    i = i*i

res = timer.finish()

print(res)