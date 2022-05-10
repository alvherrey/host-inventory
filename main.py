import pandas as pd
import utils.connection as conn

# Create dataframe from json
df = pd.read_csv("host-inventory.csv")
# Set headers
df = df[['host', 'ip', 'os']]
# Filter by column value
df = df[df['os'].str.contains("linux")]
# Display the first 10 rows
#df = df.head(10)
# Export to csv
#df.to_csv('out.csv', index = False)
#print(df)

for ip in df['ip']:
    print(ip)
    conn.ssh(ip,"user","password","hostname")