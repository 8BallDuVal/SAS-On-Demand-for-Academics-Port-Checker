# SAS-On-Demand-for-Academics-Port-Checker
Checks the ports of the hostnames used by SAS OnDemand for Academics to see if any of the ports are being blocked. Can be used to check for connection issues, and is helpful for users to troubleshoot issues without needing to contact technical support.

Hostnames are initialized in the the self.states dictionary at the beginning of the program. These are the hostnames which we will check to see if they are open/closed.

The hostnames in the self.states dictionary depend on the selections made by the user.
  - The change_window() function decides whether or not they are using JMP/EG (User must choose Yes/No).
    - If they choose Yes, the program will include the Tier 2 hostnames of the corresponding region. 
    - If they choose No, the program will NOT include the Tier 2 hostnames of the corresponding region. 
      - If the user chose Yes, the region_select_using_EG() function decides which region they are in (User must choose US, EU, AP).
      - If the user chose No, the region_select_not_using_EG() function decides which region they are in (User must choose US, EU, AP).

- From there, the program skips ahead to one of the following functions: 
  - us_using_EG()
  - eu_using_EG()
  - ap_using_EG()
  - us_not_using_EG()
  - eu_not_using_EG()
  - ap_not_using_EG() 

- Finally, the program skips to the output_window() function to display the results. The user can choose to save the results as a text file to their desktop if they would like to. They can share the text file of the results with technical support.
