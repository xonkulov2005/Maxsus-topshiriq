# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_RlnVhuFGEufhVhCTybxOSUHhOz0fCOf
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('sin(x) funksiyasining grafigi')
plt.grid(True)
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Tasodifiy nuqtalar grafigi')
plt.grid(True)
plt.show()

# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DBDYEH4rafHFx7HN5VxeIqGKrZB8E7op
"""

# prompt: from google.colab.patches import cv2_imshow

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("gul.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("Akam.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("Sayohat.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)