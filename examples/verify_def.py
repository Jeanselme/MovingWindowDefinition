"""
    Simple example on data
    The data contains different space time
    And also time in the wring order
"""
import pandas as pd
import matplotlib.pyplot as plt
from analysis.movingWindowDef import verifyDef

data = pd.read_csv("examples/generated_data.csv", index_col="time")

# Transform Data in boolean
data = (data.f1 == data.f2)

plt.figure()
plt.scatter(data.index, data)

# Compute different defintions
full = verifyDef(data, duty_cycle = 1, min_length = 0, max_gap = 0)
for event in full:
    plt.scatter([event["begin"], event["end"]], [0.2,0.2], color="red")
    plt.plot([event["begin"], event["end"]], [0.2,0.2], alpha=event["density"], color="red")


semi = verifyDef(data, duty_cycle = 0.5, min_length = 0, max_gap = 2)
for event in semi:
    plt.scatter([event["begin"], event["end"]], [0.4,0.4], color="green")
    plt.plot([event["begin"], event["end"]], [0.4,0.4], alpha=event["density"], color="green")


minl = verifyDef(data, duty_cycle = 0.5, min_length = 3, max_gap = 5, only_first= True)
for event in minl:
    plt.scatter([event["begin"], event["end"]], [0.6,0.6], color="black")
    plt.plot([event["begin"], event["end"]], [0.6,0.6], alpha=event["density"], color="black")


maxl = verifyDef(data, duty_cycle = 0.5, min_length = 15, max_gap = 5)
for event in maxl:
    print(event["density"])
    plt.scatter([event["begin"], event["end"]], [0.8,0.8], color="yellow")
    plt.plot([event["begin"], event["end"]], [0.8,0.8], alpha=event["density"], color="yellow")


plt.show()