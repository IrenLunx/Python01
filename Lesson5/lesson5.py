from isOdd import isOdd

print(isOdd(1))
print(isOdd(4))
#

from progress.bar import Bar
import time

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(0.5)
    bar.next()
bar.finish()

#
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
#

import matplotlib.pyplot as plt
import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()

lis = [1,2,3,2,7]
plt.plot(lis)
plt.show()