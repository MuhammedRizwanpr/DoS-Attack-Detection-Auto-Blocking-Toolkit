# 🛡️ DoS Attack Detection & Auto-Blocking Toolkit

This project is a **complete workflow tool** that demonstrates how a DoS attack is detected, blocked, logged, cleaned, and visualized using:

- **Suricata IDS** (Intrusion Detection System)
- **Fail2Ban** (Auto-block attacker IP)
- **Python Scripts** (Cleanup + Visualization)
- **Matplotlib** (Charts of attack traffic)

This tool is created for **educational and cybersecurity learning purposes**.

---

## 🔥 What This Tool Does

When you run the script:

1. **Suricata monitors your network traffic** in real-time.
2. When a **DoS attack happens**, Suricata raises alerts in `eve.json`.
3. **Fail2Ban reads those alerts** and automatically **blocks the attacker's IP**.
4. When you stop the script using **CTRL + C**, a Python cleanup script runs:
   - Cleans the `eve.json` file
   - Extracts DoS attack data
   - Generates a **visual report** using Matplotlib
5. You get charts like:
   - Number of attacks per IP
   - Attack duration
   - Attack direction
   - Ports targeted
   - Time of attack

A sample screenshot is added below (replace with your final screenshot).

---

## 📁 Project Structure

```
/DoS-Attack-Detection-&-Auto-Blocking-Toolkit
├── run_ids.sh             # Shell script to run Suricata + Fail2Ban
├── cleanup_visualize.py   # Python script to clean eve.json + visualize
├── sample_report.png      # Screenshot of the tool running
└── README.md              # This file
```

---

## ⚙️ Requirements

### **1. Suricata**
Install Suricata on Linux:
```bash
sudo apt install suricata
```

### **2. Fail2Ban**
```bash
sudo apt install fail2ban
```

### **3. Python Libraries**
```bash
pip install pandas matplotlib
```

---

## 🚀 How to Use

### **1. Clone the Repository**
```bash
git clone /home/rizwan/scripts/suricata-ids.sh
/home/rizwan/scripts/suricata-ips.sh
/home/rizwan/scripts/visualize_dos.py
cd yourrepo
```

### **2. Start the Monitoring Tool**
```bash
sudo bash run_ids.sh
```

Now Suricata starts watching your network.
Fail2Ban monitors Suricata alerts.

If a DoS attack happens:
- Suricata logs it
- Fail2Ban automatically blocks the attacker

### **3. Stop the Tool**
Press:
```
CTRL + C
```

When you stop it:
- The Python script runs automatically
- Cleans eve.json
- Creates charts
- Saves the visualization as an image

### **4. View the Report**
Your report will be saved as:
```
report.png
```
Open it to see the attack summary.

---

## 🖼️ Screenshot Example

Replace the image with your final screenshot:

![Sample Report](sample_report.png)

---

## 📊 Output You Will See

- Bar chart of attacks per IP
- Time series of attack timestamps
- Attack duration calculation
- Ports targeted
- Direction: inbound/outbound

---

## ✨ Why This Tool Is Useful

- Helps beginners understand Suricata
- Shows real DoS detection workflow
- Auto-blocks attackers using Fail2Ban
- Generates easy-to-read graphs
- Great for cybersecurity learning and portfolio projects

---

## 📜 License
This tool is for **educational purposes** only. Do not use it for illegal activities.

---

## 📩 Contribution
Want to improve it? Feel free to send a pull request.

---


## 📷 Final Output Screenshot
*(Add your running-tool screenshot here)*

