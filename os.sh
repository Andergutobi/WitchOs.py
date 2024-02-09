# Function to add to your .bashrc or .zshrc
# Usage: os <ip>

function os(){
        if [[ "$(ping -c 1 $1 | grep 'ttl' | awk '{print $6}' | tr '=' ' ' | awk '{print $2}')" -le 64 ]]; then
            echo "[+] Linux"
        elif [[ "$(ping -c 1 $1 | grep 'ttl' | awk '{print $6}' | tr '=' ' ' | awk '{print $2}')" -ge 65 && "$(ping -c 1 $1 | grep 'ttl' | awk '{print $6}' | tr '=' ' ' | awk '{print $2}')" -le 128 ]]; then
            echo "[+] Windows"
        elif [[ "$(ping -c 1 $1 | grep 'ttl' | awk '{print $6}' | tr '=' ' ' | awk '{print $2}')" -gt 128 ]]; then
            echo "[+] Solaris/AIX"
        else
            echo "[!] Not reached"
        fi
}
