import time
import numpy as np


print("""



















# --------------
#   ATI - MUZ 
# --------------
# A Flood Early Warning System
# NASA Space Apps Challenge 2017.
# Buenos Aires People's Choice Winner.







""")
for i in range(10):
  print('Predicting with artificial neural networks...')
  time.sleep(0.35)
  noise = np.random.normal(0, 5)
  p = 30 + noise + i*3
  if (i > 5):
    p += i*4 + 5
    if (p > 99):
      p -= (p-97)
  print('Flood probability: {:.0f}%'.format(p))
  time.sleep(0.15)
  if (p >= 95):
    print('**************************')
    print('** {}% ** FLOOD ALERT! **'.format(p))
    print('**************************')
    print('-- Broadcasting SMS...')
    t = 0.1
    time.sleep(t)
    print('**')
    time.sleep(t)
    print('******')
    time.sleep(t)
    print('**********')
    time.sleep(t)
    print('**************')
    time.sleep(t)
    print('******************')
    time.sleep(t)
    print('**********************')
    time.sleep(t)
    print('**************************')
    print('DONE!')
    break

  print()