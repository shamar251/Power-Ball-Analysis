Powerball Analysis

This project performs a statistical analysis of Powerball lottery data, identifying patterns in recurring winning numbers and visualizing them for better understanding. It utilizes Python libraries such as Pandas, Seaborn, and Matplotlib to process the data and generate insights.

Features

- Data Extraction & Preparation: 
  - The notebook starts by loading Powerball lottery data from historical records, cleaning, and preparing it for analysis.
  
- Top Recurring Numbers: 
  - The project identifies the most recurring winning numbers across all Powerball draws and visualizes them using bar charts.
  
- Section-wise Analysis: 
  - Further, the analysis divides the lottery numbers into sections and examines the top recurring numbers within each section, providing insights into which numbers tend to appear more frequently in specific ranges.

Visualizations

- Most Recurring Winning Numbers: 
  - A bar chart visualizes the top 10 most frequent winning numbers in the Powerball game.
  
- Section-wise Top Numbers**: 
  - Another grouped bar chart highlights the top recurring numbers in different sections of the Powerball number range.

Setup

Prerequisites

- Python 3.x
- Required Python packages:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  
Install the required packages using:
```bash
pip install pandas matplotlib seaborn
```

Running the Analysis

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/powerball-analysis.git
   ```
2. Navigate into the project directory:
   ```bash
   cd powerball-analysis
   ```
3. Open the Jupyter notebook:
   ```bash
   jupyter notebook power_ball_analysis.ipynb
   ```

4. Run the notebook to see the data analysis and visualizations.

## Functions Overview

- `get_most_recurring_winning_numbers()`: Extracts the top recurring winning numbers from the data.
- `visualize_top_recurring_winning_numbers()`: Plots the most frequent numbers using a bar chart.
- `visualize_top_recurring_numbers_by_section()`: Creates a grouped bar chart to show the frequency of numbers by section.
