# -*- coding: utf-8 -*-
"""20230213_3_광운대.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1njMtk6CejPf1xx419hSiRWbh1NRAZz1b
"""

#Stack
box = [1,3,5,4,2]
box.append(10) #push
box

box.pop()
box

box[-1]

#Queue
from collections import deque

que = deque()
que

que.append(3)
que.append(5)
que

que.popleft()
que