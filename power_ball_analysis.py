import csv
from matplotlib import pyplot as plt
import pandas as pd
from typing import Counter
import seaborn as sns
from scipy.stats import chisquare



def get_most_recurring_winning_numbers(top_n):
    '''
    Returns the top n most recurring numbers.
    

    Return:
    - Dictionary of the top n most recurring numbers and their counts within the given section.
    '''
    winning_numbers = []
    with open('Lottery_Powerball_Winning_Numbers__Beginning_2010.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row

        for row in reader:
            # Split the 'Winning Numbers' column (index 1) into individual numbers
            numbers = row[1].split()  # Assuming numbers are separated by spaces
            winning_numbers.extend(numbers)  # Add numbers to the list

    # After the file is closed, process the data
    return dict(Counter(winning_numbers).most_common(top_n))
        
def get_most_recurring_winning_number_by_section(section, top_n):
    ''' 
    Returns the top n most recurring numbers within the given section.
    Example winning number: 11 21 27 36 62 24
    Section 1 = 11
    Section 2 = 21
    Section 3 = 27
    Section 4 = 36
    Section 5 = 62
    Section 6 = 24

    Return:
    - Dictionary of the top n most recurring numbers and their counts within the given section.
    '''
    winning_number_by_section = {}

    with open('Lottery_Powerball_Winning_Numbers__Beginning_2010.csv', 'r') as csv_file:
        df = pd.read_csv(csv_file)
        winning_numbers = df['Winning Numbers'].values.tolist()

    for winning_number in winning_numbers:
        
        numbers = winning_number.split()
        
        if section > 0 and section <= len(numbers):
            # Convert to integer and access the correct section
            section_number = int(numbers[section - 1])
            winning_number_by_section[section_number] = winning_number_by_section.get(section_number, 0) + 1

    # Return the top_n most common numbers
    return dict(Counter(winning_number_by_section).most_common(top_n))
    


def visualize_top_recurring_winning_numbers(winning_numbers_dict):
    '''
    Visualizes top n most recurring numbers in a bar chart with improved visuals.
    '''
    # Set the figure size
    plt.figure(figsize=(10, 6))
    
    sorted_dict = dict(sorted(winning_numbers_dict.items(), key=lambda item: item[1], reverse=True))
    sns.barplot(x=list(sorted_dict.keys()), y=list(sorted_dict.values()), palette='viridis')
    
    plt.title('Top Recurring Winning Numbers', fontsize=16)
    plt.xlabel('Winning Numbers', fontsize=12)
    plt.ylabel('Frequency of Occurrence', fontsize=12)
    
    for index, value in enumerate(sorted_dict.values()):
        plt.text(index, value + 0.5, str(value), ha='center', va='bottom', fontsize=10)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_top_recurring_numbers_by_section(section_data_dict):
    '''
    Visualizes top recurring winning numbers by section in a grouped bar chart.
    
    section_data_dict: A dictionary where each key is a section number, 
    and the value is another dictionary with top recurring numbers and their frequencies.
    '''

    data = []
    for section, top_numbers in section_data_dict.items():
        for number, count in top_numbers.items():
            data.append({'Section': f'Section {section}', 'Number': number, 'Frequency': count})
    
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Number', y='Frequency', hue='Section', data=df, palette='Set2')
    
    
    plt.title('Top Recurring Winning Numbers by Section', fontsize=16)
    plt.xlabel('Winning Numbers', fontsize=12)
    plt.ylabel('Frequency of Occurrence', fontsize=12)
    
    plt.tight_layout()
    plt.show()

def chi_square_test_lottery(data_path, section):
    '''
    Performs a Chi-Square Goodness-of-Fit Test for lottery numbers in a given section.
    
    Parameters:
    - data_path: path to the CSV file containing lottery data.
    - section: the section of the lottery numbers to analyze (1-6).
    
    Returns:
    - chi-square statistic and p-value.
    '''
    
    # Read the dataset
    df = pd.read_csv(data_path)
    
    # Extract the winning numbers column
    winning_numbers = df['Winning Numbers'].values.tolist()
    
    # Split the winning numbers by spaces and select the chosen section
    section_numbers = [int(num.split()[section - 1]) for num in winning_numbers]
    
    # Get observed frequencies
    observed_frequencies = Counter(section_numbers)
    
    # Number of unique possible numbers (assuming lottery numbers range from 1-69)
    total_numbers = 69
    
    # Total number of draws
    total_draws = len(section_numbers)
    
    # Expected frequency: uniform distribution, i.e., each number should appear equally often
    expected_frequency = total_draws / total_numbers
    
    # Create lists of observed and expected frequencies for each number from 1 to 69
    observed = []
    expected = []
    
    for num in range(1, total_numbers + 1):
        observed.append(observed_frequencies.get(num, 0))
        expected.append(expected_frequency)
    
    # Perform the Chi-Square Goodness-of-Fit Test
    chi_statistic, p_value = chisquare(f_obs=observed, f_exp=expected)

    chi_statistic = round(chi_statistic, 2)
    #p_value = round(p_value, 1)

    print(f'Chi-Square Statistic: {chi_statistic}')
    print(f'P-Value: {p_value}')

    if p_value < 0.05:
        pass #print("The lottery numbers in this section deviate from a random distribution (p < 0.05).")
    else:
        pass #print("The lottery numbers in this section do not significantly deviate from a random distribution (p >= 0.05).")
    
    chi_statistic = f'Chi-Square Statistic: {chi_statistic}'
    p_value = f'P-Value: {p_value}'
    
    
    return chi_statistic, p_value




def main():
    
    # top_recurring_numbers = get_most_recurring_winning_numbers(10)
    # visualize_top_recurring_winning_numbers(top_recurring_numbers)

    # section_data = {}

    # for section in range(1, 7):
    #     top_recurring_numbers = get_most_recurring_winning_number_by_section(section, 5)
    #     section_data[section] = top_recurring_numbers
    
    # visualize_top_recurring_numbers_by_section(section_data)

    chi_square_results = {}

    for section in range(1, 7):
        chi_square_results[section] = chi_square_test_lottery('Lottery_Powerball_Winning_Numbers__Beginning_2010.csv', section)

    print(chi_square_results)



if __name__ == '__main__':
    main()