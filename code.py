import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")

print(df.head())


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")


sns.lineplot(
    data=df,
    x="Level",
    y="Attack",
    hue="Name",
    marker="o"
)

plt.title("Attack Growth by Level")
# plt.show()

sns.boxplot(
    data=df,
    x="Name",
    y="Attack"
)

plt.xticks(rotation=45)
# plt.show()



stats = df[[
    "HP",
    "Attack",
    "Defense",
    "Sp. Atk",
    "Sp. Def",
    "Speed"
]]

corr = stats.corr()

sns.heatmap(
    corr,
    annot=True
)

# plt.show()


sns.pairplot(
    df,
    hue="Name"
)

# plt.show()


sns.lineplot(
    data=df,
    x="Level",
    y="Attack",
    hue="Name",
    marker="o"
)

plt.title("Pokemon Attack Growth")
plt.grid(True)
plt.show()