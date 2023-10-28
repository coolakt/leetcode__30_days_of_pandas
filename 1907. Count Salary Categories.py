import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    
    # Creating 'conditional count' columns using apply and lambda
    accounts['low_sal'] = accounts['income'].apply(lambda x: 1 if x < 20000 else 0)
    accounts['av_sal'] = accounts['income'].apply(lambda x: 1 if (x >= 20000 and x <= 50000) else 0)
    accounts['high_sal'] = accounts['income'].apply(lambda x: 1 if x > 50000 else 0)
    
    # taking a sneak peek at our data
    print(accounts.head())
    
    # Summing values for each conditional count column
    low_count = accounts['low_sal'].sum()
    av_count = accounts['av_sal'].sum()
    high_count = accounts['high_sal'].sum()

    # Creating a dictionary to put inside of dataframe
    data = {
        # These are values for "category" column
        'category' : ['Low Salary', 'Average Salary', 'High Salary'],
        # These are our values for 'accounts_count' column
        'accounts_count' : [low_count, av_count, high_count]
    }
    # Creating a result dataframe
    result = pd.DataFrame(data)

    # Outputting result
    return result
