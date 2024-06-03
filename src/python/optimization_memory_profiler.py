import pandas as pd
from memory_profiler import profile

df = pd.read_csv("/Users/farshid/Downloads/Ex_Files_Hands_On_Data_Sci_3/Exercise Files/MonthlyProductSales.csv", encoding = "ISO-8859-1")
# bad: it may hinder readability for those who are not familiar with the specific chaining of methods. Additionally, if an error occurs during execution, it can be more challenging to pinpoint the exact method that caused the issue.
@profile
def single_line_approach():
    final_df_single = df.groupby(df['Month of Order Date'].str[:4]).describe().reset_index().rename(columns={"Month of Order Date": "Year"})
    return final_df_single
# best: enhances readability, as each line of code represents a single action, making it easier to follow and understand. Furthermore, it improves maintainability, as updating or modifying a specific step can be done without having to change the entire chain of methods. Lastly, in the event of an error, debugging is more straightforward, as you can quickly identify which step is causing the problem.
@profile
def step_by_step_approach():
    year_series = df['Month of Order Date'].str[:4]
    grouped_df = df.groupby(year_series)
    descriptive_stats = grouped_df.describe()
    reset_df = descriptive_stats.reset_index()
    final_df_step = reset_df.rename(columns={"Month of Order Date": "Year"})
    return final_df_step

# Run these functions to see memory usage
step_by_step_approach()
single_line_approach()


