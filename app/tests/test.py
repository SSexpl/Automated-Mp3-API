import numpy as np
from pandas import DataFrame
from scipy.spatial.distance import cdist
from Levenshtein import ratio
from pprint import pprint


arr1 = np.array(
    [
        "Coldplay",
        "Coldplay",
        "Coldplay",
        "Coldplay",
        "Coldplay",
        "Chris Brown",
        "sdfsdfsfdummyadasdasd",
        "Coldplay Chris",
        "Coldplay Guy Berryman Jonny Buckland Will Champion Chris Martin",
        "Guy Berryman Jonny Buckland Will Champion Chris Martin Coldplay",
    ]
)

matrix = cdist(arr1.reshape(-1, 1), arr1.reshape(-1, 1), lambda x, y: ratio(x[0], y[0]))
df = DataFrame(data=matrix, index=arr1, columns=arr1)
classifierOptions = df.sum().drop_duplicates().to_dict()

max_key = next(iter(classifierOptions))
for key in classifierOptions:
    if classifierOptions[key] > classifierOptions[max_key]:
        max_key = key
 
# Print the key with the maximum value
print(max_key)
pprint(classifierOptions)
