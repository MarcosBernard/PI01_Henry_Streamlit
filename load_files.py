import pandas as pd

def load_and_normalize():
    # Savin 'qualifying' dataframes
    lap_times_split1_df = pd.read_csv('./Datasets/lap_times/lap_times_split_1.csv',encoding='UTF-8',header=None)
    lap_times_split2_df = pd.read_csv('./Datasets/lap_times/lap_times_split_2.csv',encoding='UTF-8',header=None)
    lap_times_split3_df = pd.read_csv('./Datasets/lap_times/lap_times_split_3.csv',encoding='UTF-8',header=None)
    lap_times_split4_df = pd.read_csv('./Datasets/lap_times/lap_times_split_4.csv',encoding='UTF-8',header=None)
    lap_times_split5_df = pd.read_csv('./Datasets/lap_times/lap_times_split_5.csv',encoding='UTF-8',header=None)
    # Concatenate dataframes, ignoring their respective indexes (create a new restarted index)
    lap_times_df = pd.concat([lap_times_split1_df, lap_times_split2_df,lap_times_split3_df,lap_times_split4_df,lap_times_split5_df],ignore_index=True)
    # Change colums name
    lap_times_df.rename(columns = {0:'raceId',1:'driverId',2:'lap',3:'position',4:'time',5:'miliseconds'}, inplace = True)

    # Savin 'qualifying' dataframes
    qualifying_df1 = pd.read_json('./Datasets/Qualifying/qualifying_split_1.json')
    qualifying_df2 = pd.read_json('./Datasets/Qualifying/qualifying_split_2.json')
    #Concatenate dataframes
    qualifying_df = pd.concat([qualifying_df1,qualifying_df2],ignore_index=True)

    # Savin 'constructors' dataframe
    constructors_df = pd.read_json('./Datasets/constructors.json', lines = True)

    # Savin 'drivers' dataframe
    drivers_df = pd.read_json('./Datasets/drivers.json', lines = True)
    # Combining the new columns with the original dataframe
    drivers_df = pd.concat([drivers_df.drop(['name'], axis=1), drivers_df['name'].apply(pd.Series)], axis=1)
    # Reordering columns (forename and surname)
    drivers_df = drivers_df[['driverId','driverRef','number','code','forename','surname','dob','nationality','url']]

    # Savin 'pit_stops' dataframe
    pit_stops_df = pd.read_json('./Datasets/pit_stops.json')

    # Savin 'races' dataframe
    races_df = pd.read_csv('./Datasets/races.csv', encoding='UTF-8')

    # Savin 'results' dataframe
    races_df = pd.read_json('./Datasets/results.json', lines=True)
    return None