'''
Uruchomienie
python3 ./stats.py
'''

import matplotlib.pyplot as plt

filenames = ["matrix_{a}.txt".format(a= num) for num in range(2,13, 2 )] + ["matrix_seq.txt"]
print(filenames)
whole_results = []
for filename in filenames:
    file = open(filename)
    ns = []
    times= []
    to_trash = file.readline()
    while(1):
        line = file.readline()[:-2]
        if len(line)<=0:
            break
        line = list(map(float, line.split(';')))
        ns.append(line[0])
        times.append(line[1])
    whole_results.append(times)
    plt.plot(ns, times, label=filename)
print(whole_results)
ax = plt.gca()
ax.set_ylim([0, 20])
plt.legend()
plt.show()

# count acceleration
# E = Seq/Par
seq_times = whole_results[-1]
n = 2
print(''.join(['threads\\n:'.ljust(10)]+['|'+str(2**(3+a)).ljust(10) for a in range(1, 9)]))
for ind, par_time in enumerate(whole_results[:-1]):
    acceleration = []
    for i, time in enumerate(par_time):
        if time!=0:
            acceleration.append(round(seq_times[i]/time, 4))
        else:
            acceleration.append(0)

    acceleration.insert(0, n)
    acceleration = list(map(str, acceleration))
    acceleration = [a.ljust(10) for a in acceleration]
    print('|'.join(acceleration))
    n+=2

'''
Przyspieszenie:
threads\n:|16        |32        |64        |128       |256       |512       |1024      |2048
2         |0         |0         |0         |0         |200.3205  |164.992   |243.2533  |216.8267
4         |0         |0         |0         |24.96     |0         |137.4933  |255.416   |218.2964
6         |0         |0         |0         |0         |200.3205  |150.0145  |211.3811  |190.2097
8         |0         |0         |0         |0         |50.0      |113.7939  |159.635   |139.3192
10        |0         |0         |0         |0         |40.0128   |91.6622   |125.8736  |109.6688
12        |0         |0         |0         |0         |0         |91.6622   |104.4299  |91.2197

'''
