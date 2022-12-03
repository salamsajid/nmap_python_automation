# nmap_python_automation
A simple nmap automation python script
This script performs a fast nmap scan by using the -F flag, which tells nmap to only scan the most common ports. It also uses the -Pn flag, which tells nmap to treat all hosts as online, even if they don't respond to ping requests. Finally, it uses the -sV flag to enable service version detection, which tells nmap to try to determine the version of the services running on the target host.

After running the nmap command, the script saves the output to a variable and prints it to the screen. It also saves the output to a text file called "nmap_scan_results.txt".
