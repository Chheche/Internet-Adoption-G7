import pandas as pd
import matplotlib.pyplot as plt

file_path = "Global_Internet_Users.xlsx"
df = pd.read_excel(file_path)

g7_countries = ["United States", "Canada", "Germany", "France", "United Kingdom", "Italy", "Japan"]
df_g7 = df[df["Entity"].isin(g7_countries)]

print(df_g7.head())

plt.figure(figsize=(10, 6))

for country in g7_countries:
    subset = df_g7[df_g7["Entity"] == country]
    plt.plot(subset["Year"], subset["Internet Users(%)"], label=country)

plt.title("Évolution de l'utilisation d'Internet dans les pays du G7")
plt.xlabel("Année")
plt.ylabel("Pourcentage d'utilisateurs d'Internet")
plt.legend(title="Pays du G7")
plt.grid(True)
plt.show()