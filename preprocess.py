import pandas as pd

# 1. Paths
input_path  = 'trace_data/run0_0.csv'
output_path = 'trace_data/preprocessed_run0_0.csv'

# 2. Load the data
df = pd.read_csv(input_path)

# 3. Drop unwanted columns (errors='ignore' skips any missing ones)
cols_to_drop = [
    'Trace Packet Header',
    'Packet Context',
    'Stream Context',
    'Event Context'
]
df = df.drop(columns=cols_to_drop, errors='ignore')

# 4. Filter rows by Event type prefix
df = df[df['Event type']
        .str.startswith(('syscall', 'sched'), na=False)]

# 5. Save to new CSV
df.to_csv(output_path, index=False)

print(f"Filtered CSV saved to: {output_path}")
