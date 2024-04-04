import pandas as pd
from collections import defaultdict


def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here
    result = []
    for file_path in files:
        company_data = pd.read_csv(file_path, parse_dates=['date']) # convert date into datetime object
        
        # dicts to store the data. One per dataframe
        vol_by_year = defaultdict(list) 
        close_by_year = defaultdict(list)

        for _, row in company_data.iterrows():
            vol_by_year[row['date'].year].append((row['date'], row['vol']))
            close_by_year[row['date'].year].append((row['date'], row['close']))

        ##### First dataframe: highest trading volumn per year ##### 

        # Iterate over vol by year to find max per year
        max_vol_by_year = []
        for _, vol_dates in vol_by_year.items():
            max_vol_date = max(vol_dates, key=lambda x: x[1]) # Not sure about this lambda function, will test it later TODO
            max_vol_by_year.append({'date': max_vol_date[0], 'vol': max_vol_date[1]})
        
        max_vol_by_year_df = pd.DataFrame(max_vol_by_year) # Convert to panda df
        
        ##### Second dataframe:  Days of highest closing prices in individual years ##### 
        
        # Same, iterate to get max clousing but not grouping by max year
        max_close_by_year = []
        for _, close_dates in close_by_year.items():
            max_close_dates = [d for d in close_dates if d[1] == max(d[1] for d in close_dates)]
            max_close_by_year.extend([{'date': d[0], 'close': d[1]} for d in max_close_dates]) # not working, change to extend? TODO
        
        max_close_by_year_df = pd.DataFrame(max_close_by_year) # Convert to panda
        
        result.append([max_vol_by_year_df, max_close_by_year_df])
    
    return result
    pass

files = ["C:/csv_files/gnyned.csv", "C:/csv_files/framp.csv"]
print(solution(files))

"""
check lambda function: done
change from append to extend: done
performance not great
    refactor to single iterrow: done
    refactor to single defaultdict: 
edge scenarios:
??
"""