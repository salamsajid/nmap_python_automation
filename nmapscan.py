import os

# Ask the user for the IP address to scan
ip_address = input("Enter the IP address to scan: ")

# Create the command to run nmap with the appropriate flags and arguments
command = "nmap -F -Pn -sV --stats-every 1s " + ip_address

# Run the nmap command and save the output
nmap_output = os.popen(command).read()

# Print the output
print(nmap_output)

# Save the output to a text file
with open("nmap_scan_results.txt", "w") as f:
  f.write(nmap_output)
