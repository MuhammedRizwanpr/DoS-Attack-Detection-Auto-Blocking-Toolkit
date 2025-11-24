#!/bin/bash

# When you press CTRL+C, run cleanup()
cleanup() {
    echo ""
    echo "-----------------------------------------"
    echo "Stopping Fail2ban and Suricata..."
    sudo systemctl stop fail2ban

    python3 /home/rizwan/scripts/visualize_dos.py
    echo "Done."
    echo "-----------------------------------------"
    exit 0
}

trap cleanup SIGINT

echo "-----------------------------------------"
echo ". . . . .  SURICATA IDS STARTING  . . . ."
echo "-----------------------------------------"

sudo systemctl start fail2ban 
sudo suricata -c /etc/suricata/suricata.yaml -i wlp0s20f3 &

sleep 2

echo "[✓] IDS + Fail2ban active"

tail -Fn0 /var/log/suricata/fast.log | while read line; do
    notify-send "🚨 Suricata Alert" "$line"
done 

