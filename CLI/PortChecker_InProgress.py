class PortCheck:
    def __init__(self):
        self.teir1_hostnames = {'welcome.oda.sas.com':443,											# Welcome Page (Global)
						         'status.oda.sas.com':443,											# Status Page (Global)
                                }

        self.teir2_hostnames = {'odamid-usw2.oda.sas.com':443,										# odamid (US)
						        'odamid-euw1.oda.sas.com':443,										# odamid (EU)
						        'odamid-apse1.oda.sas.com':443,										# odamid (AP)
                               }

        self.teir3_hostnames = {'odaomr-usw2.oda.sas.com':8561,									    # odamr (US)
						        'odaomr-euw1.oda.sas.com':8561,										# odamr (EU)
						        'odaomr-apse1.oda.sas.com':8561,									# odamr (AP)
						        'odaws01-usw2.oda.sas.com':8591,									# odaws01 (US)
						        'odaws02-usw2.oda.sas.com':8591,									# odaws02 (US)
						        'odaws03-usw2.oda.sas.com':8591,									# odaws03 (US)
						        'odaws04-usw2.oda.sas.com':8591,									# odaws04 (US)
						        'odaws01-euw1.oda.sas.com':8591,									# odaws01 (EU)
						        'odaws02-euw1.oda.sas.com':8591,									# odaws02 (EU)
						        'odaws01-apse1.oda.sas.com':8591,									# odaws01 (AP)
						        'odaws02-apse1.oda.sas.com':8591									# odaws02 (AP)
                               }
        
        self.reverselookup = {}
        self.nslookup_results = {}
        
        # ---------------- Prompt the user if they are using SODA: EG/SODA: JMP and if they are, include tier 3 hostnames. -------------------------# 
        try:
            decision = input("Are you using SAS OnDemand for Academics: Enterprise Guide, or SAS OnDemand for Academics: JMP? (Enter Yes/No): \n")
            if decision == 'No' or decision == 'N' or decision == 'no' or decision == 'n':
                self.states = {**self.teir1_hostnames , **self.teir2_hostnames}
            elif decision == 'Yes' or decision == 'Y' or decision == 'yes' or decision == 'y':
                self.states = {**self.teir1_hostnames , **self.teir2_hostnames, **self.teir3_hostnames}
            else:
                print('input was invalid. please restart the program and try again.')
        except Exception as e:
            print(e)

    def scanports(self):
        from socket import socket, AF_INET, SOCK_STREAM                                     # importing socket package (needs to be done here to avoid errors in ns_lookup)
        server_state = {}
        
        for targetIP, port in self.states.items():                                # Testing the hostnames/ports to see if they are open are closed
            socket_obj = socket(AF_INET, SOCK_STREAM)                             # Create socket object
            location = (targetIP, port)                                           # set location (Host Name, Port)
            try:                                                                  
                result = socket_obj.connect_ex(location)                          # Try to connect to hostname/port, store result.
            except:                                                               
                server_state[targetIP] = 'Port {}: ERROR'.format(port)            # If the lookup fails, return "Port ####: ERROR"
            if result == 0:                                                       # if result = 0, connection was successful.
                server_state[targetIP] = 'Port {}: OPEN'.format(port)
            else:                                                                 # Else, the port is closed. 
                server_state[targetIP] = 'Port {}: CLOSED'.format(port)
        self.server_state = server_state
        return server_state

    def ns_lookup(self):
        import socket
        # Performing an 'nslookup' using the socket.gethostbyname() method to get the dns ip address 
        for key in self.states:
            try:
                self.nslookup_results[key] = socket.gethostbyname(key)          # Example of what is stored in self.nslookup_results: 
            except:                                                             # {'key':value} --> { 'odamid-apse1.oda.sas.com' : 54.251.250.199 }
                self.nslookup_results[key] = 'Error'                            # The value will be "Error" if the lookup fails
                continue

        # Using the dns ip address to get the dns hostname
        for key, value in self.nslookup_results.items():
            try:
                self.reverselookup[key] = socket.getfqdn(value)                 # Example of what is stored in self.reverselookup: 
            except:                                                             # {'key':value} --> { 'odamid-apse1.oda.sas.com' : 'ec2-54-251-250-199.ap-southeast-1.compute.amazonaws.com' }
                self.reverselookup[key] = 'Error'                               # The value will be "Error" if the lookup fails
                continue
        return self.reverselookup

#----------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------- Command-Line output -----------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#
print('''
#----------------------------------------------------------------------------------------------------------------------#
#--------------------------------- SAS OnDemand for Academics Port Checker: In-Progress Version -----------------------#
#----------------------------------------------------------------------------------------------------------------------#\n
''')
import pprint         # this python package prints lists in a much cleaner, more readable fashion.
                        # run the command "pip install pprint" on a command line if you have python installed to download the pprint package.

test = PortCheck()      # Create a PortCheck() object, initializing the tier1, 2 and 3 dictionaries

#-------------------------------- Scanports Method check (Checking for blocked ports) ---------------------------------#
print('\n#-------------------------------- Scanports Method check (Checking for blocked ports) ---------------------------------#\n')
ports = test.scanports()
pprint.pprint(ports)

#------------------------------------------------ nslookup method check -----------------------------------------------#
print('\n#------------------------------------------------ nslookup method check -----------------------------------------------#\n')
print('                 ~~~~~ Be patient, this method takes around 30-60 seconds (max) to complete... ~~~~~                      \n')
ns = test.ns_lookup()
pprint.pprint(ns)

#------------- Wait for user input, then close the program --------------#
a = input('\n#-------------------------------------- Press the Enter/Return key to exit --------------------------------------------#\n')
if a:
    exit(0)