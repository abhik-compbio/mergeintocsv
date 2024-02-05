import pandas as pd
import glob

# Path to your .dat files
dat_files_path = '/home/abhikghosh/work_on_csi/all-atom-lowsalt-kx5-anton-traj/curve-canal-analysis/final_curve_canal/pca_tica-analysis/myDats/*.dat'

# List to store dataframes from each .dat file
dfs = []

# Iterate through all .dat files in the specified path
for file_path in glob.glob(dat_files_path):
    # Assuming the data in .dat file is tab-separated, you can adjust the delimiter as needed
    df = pd.read_csv(file_path, delimiter='\t')
    dfs.append(df)

# Concatenate all dataframes into a single dataframe
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged dataframe to a .csv file
merged_df.to_csv('/home/abhikghosh/work_on_csi/all-atom-lowsalt-kx5-anton-traj/curve-canal-analysis/final_curve_canal/pca_tica-analysis/myDats/merged_file.csv', index=False)

