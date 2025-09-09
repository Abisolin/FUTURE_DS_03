
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Task 3 dataset.csv")

if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

print("\n✅ Dataset Loaded & Cleaned")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

print("\n📊 Dataset Info:")
print(df.info())

print("\n📊 Summary Statistics:\n", df.describe())

avg_scores = df.drop(columns=["Student ID"]).mean().sort_values(ascending=False)

fig, axes = plt.subplots(2, 2, figsize=(14,10))  # 2x2 grid

sns.barplot(x=avg_scores.values, y=avg_scores.index, palette="Blues_r", ax=axes[0,0])
axes[0,0].set_title("Average Feedback Scores (1–10)", fontsize=12)
axes[0,0].set_xlabel("Average Rating")
axes[0,0].set_ylabel("Survey Question")

for col in df.columns[1:]:
    sns.kdeplot(df[col], fill=True, alpha=0.3, ax=axes[0,1], label=col)
axes[0,1].set_title("Distribution of Ratings", fontsize=12)
axes[0,1].set_xlabel("Rating")
axes[0,1].legend(fontsize=7)

sns.heatmap(df.drop(columns=["Student ID"]).corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=axes[1,0])
axes[1,0].set_title("Correlation Heatmap", fontsize=12)

lowest = avg_scores.tail(3)
axes[1,1].barh(lowest.index, lowest.values, color="red")
axes[1,1].set_title("Lowest Rated Aspects", fontsize=12)
axes[1,1].set_xlabel("Average Rating")

plt.tight_layout()
plt.show()

print("\n⚠️ Lowest Rated Aspects (Need Improvement):\n", lowest)

print("\n💡 Suggestions for Improvement:")
for aspect in lowest.index:
    if "presentation" in aspect.lower():
        print(f"- {aspect}: Use more visuals, animations, and interactive slides.")
    elif "difficulty" in aspect.lower():
        print(f"- {aspect}: Adjust assignment complexity or provide more guidance.")
    elif "support" in aspect.lower():
        print(f"- {aspect}: Offer mentoring, office hours, or extra resources.")
    elif "structuring" in aspect.lower():
        print(f"- {aspect}: Break course into clear modules with objectives.")
    else:
        print(f"- {aspect}: Gather detailed feedback to address student concerns.")
