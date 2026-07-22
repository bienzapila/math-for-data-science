# Получение срдедневзвешанного значения
import numpy as np
sample = [1, 3, 7, 5, 4]
weights = [1, 1, 2, 2, 2]
print(np.average(sample, weights=weights))