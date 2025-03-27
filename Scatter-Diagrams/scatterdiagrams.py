import os
import pandas as pd
import matplotlib.pyplot as plt

# Construct the file path relative to the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, "..", "datas", "midwest_filter.csv")

# Load the data
df = pd.read_csv(path)
df.info()

# Create the figure and axis
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1)

# Iterate over each state and plot the points
for cat in sorted(list(df["state"].unique())):
    # Filter data for each category (state)
    ar = df[df["state"] == cat]["area"]
    pop = df[df["state"] == cat]["poptotal"]
    wht = df[df["state"] == cat]["popwhite"]
    
    # Plot population vs. area with symbol size proportional to white population
    ax.scatter(ar, pop, label=cat, s=wht/200)

# Customize the axes
ax.spines["top"].set_color("None")
ax.spines["right"].set_color("None")
ax.set_xlabel("Area")
ax.set_ylabel("Population")
ax.set_xlim(left=-0.01)
ax.set_title("Scatter plot of population vs area: Symbols size = White population")
ax.legend(loc="upper left", fontsize=10)

plt.grid()
plt.show()
