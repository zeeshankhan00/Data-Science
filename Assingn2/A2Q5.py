from collections import Counter
import random
import matplotlib.pyplot as plt

num_friends = [random.randint(1,100) for _ in range(100)]
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]  # height is just number of friends
plt.bar(xs,ys)
plt.axis([0,101,0,10])
plt.title("Histogram of friends count")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()
