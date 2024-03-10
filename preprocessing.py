import pandas as pd

# data sets
df = pd.read_csv("./athlete_events.csv")
region_df = pd.read_csv("./noc_regions.csv")


def preprocess(df, region_df):
    
    # Get Season == "Summer"
    df = df[df['Season'] == 'Summer']

    # Merge with region_df
    df = df.merge(region_df, on="NOC", how="left")

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Perform one hot encoding
    encoded_df = pd.get_dummies(df['Medal'])
    df = pd.concat([df, encoded_df], axis=1)
    
    return df

