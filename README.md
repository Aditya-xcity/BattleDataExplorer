# Pokemon Data Representation

This project explores a small Pokemon dataset with Python data analysis and visualization tools. It uses `pandas`, `matplotlib`, and `seaborn` to compare stats, visualize attack growth, and inspect relationships between core battle attributes.

## What’s Included

- `code.ipynb` - notebook version of the analysis
- `code.py` - script version of the same workflow
- `pokemon.csv` - dataset used for the charts and summaries
- `pokemon.xlsx` - alternate spreadsheet version of the data
- `blastoise_growth.mp4` - exported visual output

## Main Visualizations

- Line chart for Pokemon attack growth by level
- Box plot for comparing attack values across Pokemon
- Correlation heatmap for battle stats
- Pair plot for exploring relationships between features

## Requirements

- Python 3.9 or later
- pandas
- matplotlib
- seaborn

## Setup

Install the required packages:

```bash
pip install pandas matplotlib seaborn
```

If you want to work from the notebook, install Jupyter as well:

```bash
pip install notebook
```

## How to Run

### Notebook

Open `code.ipynb` in VS Code or Jupyter and run the cells top to bottom.

### Script

Run the Python file from the project folder:

```bash
python code.py
```

## Notes

- Make sure `pokemon.csv` stays in the same folder as the notebook or script so the relative file path works.
- The script displays the final line chart with `plt.show()`. Other plots are prepared in code and can be shown by uncommenting their `plt.show()` lines.

## Project Goal

The goal of the project is to make Pokemon stat data easier to understand through simple exploratory data analysis and visual storytelling.