import json
import os
import pandas as pd
import matplotlib.pyplot as plt

# Load eve.json

path = "/var/log/suricata/eve.json"

if os.path.getsize(path) == 0:
    print("eve.json file is empty. No attack happened.")
    exit()

with open("/var/log/suricata/eve.json") as f:
    data = [json.loads(line) for line in f if '"event_type":"alert"' in line]

if not data : 
    print("no alert event found")
    exit()

# Convert to pandas DataFrame
df = pd.json_normalize(data)

# Filter only DOS alerts
df = df[df["alert.signature"] == "HTTP DOS attack"]

if df.empty:
    print("No DoS alerts found.")
    exit()

# Count alerts per IP
ip_counts = df["src_ip"].value_counts()

print("\nDoS Alert Count per IP:")
print(ip_counts)

# Plot
plt.figure(figsize=(8,5))
ip_counts.plot(kind="bar")
plt.title("DoS Attacks by Source IP")
plt.xlabel("IP Address")
plt.ylabel("Alert Count")
plt.tight_layout()
print("Visualization saved as dos_visual.png")

plt.show()

# attack time and count of request 

df['timestamp'] = pd.to_datetime(df['timestamp'])
start = df['timestamp'].min()
end = df['timestamp'].max()
duration = end - start

print("\n-------- attack duration -------")
print(f"Start : {start}")
print(f"End : {end}")
print(f"Duration : {duration}")

# attack direction 
print("\n--- ATTACK DIRECTION ---")
print(df['direction'].value_counts())

# port of attack happens 
print("\n--- PORT INFORMATION ---")
print("Source Ports:")
print(df['src_port'].value_counts().head(5))

print("\nDestination Ports:")
print(df['dest_port'].value_counts().head(5))

# each 1 second how much request chat 
time_counts = df.resample('1S', on='timestamp').size()

if len(time_counts) <= 1:
    print("\nNot enough timeline data to plot DoS activity over time.")
else:
    plt.figure(figsize=(10,5))
    time_counts.plot(color='red')
    plt.title("DoS Attack Volume Over Time (per second)")
    plt.xlabel("Time")
    plt.ylabel("Number of Alerts")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("dos_timeline.png")
    print("Timeline graph saved as dos_timeline.png")
    plt.show()