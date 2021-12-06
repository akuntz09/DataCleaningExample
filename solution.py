import pandas as pd

pd.set_option('display.max_columns', None)

# Loading the data and doing initial investigation
jeopardy_data = pd.read_csv("jeopardy.csv")
print(jeopardy_data.info())
print(jeopardy_data.head())
jeopardy_data[" Round"].value_counts()

# Looking at the possible values
print(jeopardy_data[" Value"].unique())

# Seeing which questions have a Value of None
print(jeopardy_data[jeopardy_data[" Value"] == "None"])

# Filtering out the None questions
no_final_jeopardy = jeopardy_data[jeopardy_data[" Value"] != "None"]
print(no_final_jeopardy[" Value"].unique())

# A function to convert the values to ints
def str_to_int(input_str):
    return int(input_str.replace("$","").replace(",",""))

# Applying the function to all rows of our filtered dataset
no_final_jeopardy["Int Value"] = no_final_jeopardy[' Value'].apply(str_to_int)
print(no_final_jeopardy["Int Value"])
print(no_final_jeopardy.describe())

# Filtering the questions by the word "computer"
contains_computer = no_final_jeopardy[" Question"].apply(lambda x: "computer" in x)
computer_rows = no_final_jeopardy[contains_computer]

# Finding the mean value of the filtered questions
print(computer_rows["Int Value"].mean())
print(computer_rows[" Answer"].value_counts())