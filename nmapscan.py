import os

ip_address = input("Enter the IP address to scan: ")
command = "nmap -F -Pn -sV --stats-every 1s " + ip_address
nmap_output = os.popen(command).read()
print(nmap_output)
with open("nmap_scan_results.txt", "w") as f:
  f.write(nmap_output)
