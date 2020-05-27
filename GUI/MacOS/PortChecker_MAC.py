'''
Created on April 29th, 2020

@author: daduva
'''
from tkinter import *
from tkinter.messagebox import showinfo
import base64
import os
class ODAPortChecker:
    def __init__(self, window):  
    #-------------------------- Initializing hostnames ------------------------------------#
    #------ US Hostnames ------#
        self.global_hostnames_us = {'welcome.oda.sas.com':443,									# Welcome Page (Global)
						              'status.oda.sas.com':443,										# Status Page (Global)
                                      'odamid-usw2.oda.sas.com':443,								# odamid (US)
                                     }
        self.tier3_hostnames_us = {'odaomr-usw2.oda.sas.com':8561,									# odamr (US)
                                   'odaws01-usw2.oda.sas.com':8591,									# odaws01 (US)
	                               'odaws02-usw2.oda.sas.com':8591,									# odaws02 (US)
                                   'odaws03-usw2.oda.sas.com':8591,									# odaws03 (US)
                                   'odaws04-usw2.oda.sas.com':8591,									# odaws04 (US)
                                  }
    #------ EU Hostnames ------#
        self.global_hostnames_eu = {'welcome.oda.sas.com':443,										# Welcome Page (Global)
						             'status.oda.sas.com':443,										# Status Page (Global)
                                     'odamid-euw1.oda.sas.com':443,									# odamid (EU)
                                    }
        self.tier3_hostnames_eu = {'odaomr-euw1.oda.sas.com':8561,									# odamr (EU)
                                   'odaws01-euw1.oda.sas.com':8591,									# odaws01 (EU)
                                   'odaws02-euw1.oda.sas.com':8591,									# odaws02 (EU)
                                  }
    #------ AP Hostnames ------#
        self.global_hostnames_ap = {'welcome.oda.sas.com':443,								        # Welcome Page (Global)
						             'status.oda.sas.com':443,										# Status Page (Global)
                                     'odamid-apse1.oda.sas.com':443,								# odamid (AP)
                                    }
        self.tier3_hostnames_ap = {'odaomr-apse1.oda.sas.com':8561,									# odamr (AP)
                                   'odaws01-apse1.oda.sas.com':8591,								# odaws01 (AP)
						           'odaws02-apse1.oda.sas.com':8591									# odaws02 (AP)
                                  }
    #-------------------------- Build the GUI window ------------------------------------#
        self.window = window
        self.window.title("SAS OnDemand Port Checker")
        self.window.geometry("815x600")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
    
        ### Build Frames ###
        self.top_frame = Frame(self.window, padx=5,pady=5)
        self.top_frame.rowconfigure(0, weight=1)
        self.top_frame.columnconfigure(0, weight=1)
        
        self.bottom_frame= Frame(self.window, padx=5, pady=5)
        self.bottom_frame.rowconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(0, weight=1)       

        self.center_frame = LabelFrame(self.window, padx=5, pady=5)
        self.center_frame.rowconfigure(0, weight=1)
        self.center_frame.columnconfigure(0, weight=1)
        
        ### Layout frames ###
        self.top_frame.grid(row=0, sticky=N)
        self.center_frame.grid(row=1,sticky=N+S+E+W)
        self.bottom_frame.grid(row=2, sticky=S)
        
        ### add logo photo ###
        base64_image = b'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'
        analyticsphoto = PhotoImage(data=base64.b64decode(base64_image))
        self.analytics_u_photo = Label(self.top_frame, image=analyticsphoto, justify=RIGHT)
        self.analytics_u_photo.image = analyticsphoto
        self.analytics_u_photo.pack()
        
        ### Add welcome label ### 
        self.welcome_label = Label(self.center_frame,
                                   text='Welcome! The SAS OnDemand Port Checker will help you identify blocked connections to the\n SAS OnDemand servers.\n\n'+
                                        'Click next to continue.',
                                        font=("Arial", 12))
        self.welcome_label.grid(row=0,padx=10, pady=10, sticky=E+W+N+S)

        ### Add "Next" Button ###
        self.next_button = Button(self.bottom_frame, text="Next", width=10, height=2, command=self.change_window)
        self.next_button.grid(row=1, column=3, sticky=E)
        
        ### Add "Exit" Button ###
        self.exit_button = Button(self.bottom_frame, text="Exit", width=10, height=2, command=self.quit)
        self.exit_button.grid(row=1, column=0, sticky=W)
#------------- Main logic for the program --------------#
    def scanports(self):
        from socket import socket, AF_INET, SOCK_STREAM                                     # importing socket package (needs to be done here to avoid errors in ns_lookup)
        server_state = {}
        
        for hostname, port in self.states.items():                                # Testing the hostnames/ports to see if they are open are closed
            socket_obj = socket(AF_INET, SOCK_STREAM)                             # Create socket object
            location = (hostname, port)                                           # set location (Host Name, Port)
            try:                                                                  
                result = socket_obj.connect_ex(location)                          # Try to connect to hostname/port, store result.
            except:                                                               
                server_state[hostname] = 'Port {}: Error - Not Available'.format(port)            # If the lookup fails, return "Port ####: ERROR"
            if result == 0:                                                       # if result = 0, connection was successful.
                server_state[hostname] = 'Port {}: OPEN'.format(port)
            else:                                                                 # Else, the port is closed. 
                server_state[hostname] = 'Port {}: CLOSED'.format(port)
        self.server_state = server_state
        return self.server_state

    def quit(self):
        self.window.destroy()
    
    def change_window(self):
        self.welcome_label.config(text = 'Are you having issues using SAS OnDemand for Academics: Enterprise Guide,\n or SAS OnDemand for Academics: JMP?')    
        self.yes_button = Button(self.bottom_frame, text="Yes", width=10, height=2, command=self.region_select_using_EG)
        self.yes_button.grid(row=1, column=3, sticky=E)

        self.no_button = Button(self.bottom_frame, text="No", width=10, height=2, command=self.region_select_not_using_EG)
        self.no_button.grid(row=1, column=0, sticky=W)

    def region_select_using_EG(self):
        self.welcome_label.config(text = "Select the SAS OnDemand for Academics region that your profile is associated with below.")
        self.US_button = Button(self.bottom_frame, text="US", width=10, height=2, command=self.us_using_EG)
        self.US_button.grid(row=1, column=3, sticky=E)

        self.EU_button = Button(self.bottom_frame, text="EU", width=10, height=2, command=self.eu_using_EG)
        self.EU_button.grid(row=1, column=0, sticky=W)

        self.AP_button = Button(self.bottom_frame, text="AP", width=10, height=2, command=self.ap_using_EG)
        self.AP_button.grid(row=1, column=6, sticky=W)
    def region_select_not_using_EG(self):
        self.welcome_label.config(text = "Select the SAS OnDemand for Academics region that your profile is associated with below.")
        self.US_button = Button(self.bottom_frame, text="US", width=10, height=2, command=self.us_not_using_EG)
        self.US_button.grid(row=1, column=3, sticky=E)

        self.EU_button = Button(self.bottom_frame, text="EU", width=10, height=2, command=self.eu_not_using_EG)
        self.EU_button.grid(row=1, column=0, sticky=W)

        self.AP_button = Button(self.bottom_frame, text="AP", width=10, height=2, command=self.ap_not_using_EG)
        self.AP_button.grid(row=1, column=6, sticky=W)
        
# ------------------------------- If a user chooses 'Yes' to the question asking if they are using EG ------------------------- #
    def us_using_EG(self):
        self.states = {**self.global_hostnames_us , **self.tier3_hostnames_us}
        # after the user makes a selection, bring them to output window
        self.output_window() 
    def eu_using_EG(self):
        self.states = {**self.global_hostnames_eu , **self.tier3_hostnames_eu}
        # after the user makes a selection, bring them to output window
        self.output_window()
    def ap_using_EG(self):
        self.states = {**self.global_hostnames_ap , **self.tier3_hostnames_ap}
        # after the user makes a selection, bring them to output window
        self.output_window()
# ------------------------------- If a user chooses 'No' to the question asking if they are using EG ------------------------- #    
    def us_not_using_EG(self):
        self.states = {**self.global_hostnames_us}
        # after the user makes a selection, bring them to output window
        self.output_window()
    def eu_not_using_EG(self):
        self.states = {**self.global_hostnames_eu}
        # after the user makes a selection, bring them to output window
        self.output_window()
    def ap_not_using_EG(self):
        self.states = {**self.global_hostnames_ap}
        # after the user makes a selection, bring them to output window
        self.output_window()
#-------------------------- Output PortCheck results on to GUI window after Ports are checked ------------------------------------#
    def output_window(self):
        # destroy remaining buttons and labels from previous windows
        self.US_button.destroy()
        self.AP_button.destroy()
        self.EU_button.destroy()
        self.next_button.destroy()
        self.welcome_label.destroy()
        self.no_button.destroy()
        # change the size of the window to accomodate the output results
        self.window.geometry("815x600")
        ### Creating a save button
        self.save_button = Button(self.bottom_frame, text="Save", width=10, height=2, command=self.output)
        self.save_button.grid(row=1, column=3, sticky=E)
        ### Include instructions about save button
        self.instructions = Label(self.center_frame, text="\nUse the 'Save' button below to save the output to a text file on your desktop.\n", font=("Arial", 12))
        self.instructions.grid(row=1, column=0, sticky=W)
        ### create an output text box
        self.output_textbox = Text(self.center_frame, relief=SUNKEN, width=100, height=20, wrap=WORD, background="white")
        self.output_textbox.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)
        ### using the scanports_dict dictionary to create output ####
        self.scanports_dict = self.scanports()
        self.portstatus_output(self.scanports_dict)
#-------------------------- Logic to output results to a text file on user's desktop ------------------------------------#
    def output(self):
        try:
            Desktop_path = os.path.expanduser("~/Desktop/") + "SAS OnDemand for Academics PortChecker Output.txt"
            output_txt_file = open(Desktop_path, 'w')
            output_txt_file.write(self.output_textbox.get("1.0","end-1c"))
            showinfo("File Saved", "A text file containing the output has been saved to the Desktop.\n")
        except:
            showinfo("Permissions Error","You do not have permission to save a file to the Desktop. Try to copy/paste the information into a new text file instead.")
#-------------------------- Logic to output results to GUI window after Ports are checked ------------------------------------#       
    def portstatus_output(self, scanports_dict):
        import pprint
        pprint.pprint(self.scanports_dict)
        self.output_textbox.config(state=NORMAL)
        ######### Port Open/Closed Information output code #########
        results = []
        closed = []
        for key, value in self.scanports_dict.items():
            ### the first 4 if statements must be checked each time ###
            ### time due to the list in the value of the dictionary ###
            if 'OPEN' in value:
                results.append(value+ ' (successfully connected to '+key+')')
            elif 'CLOSED' in value:
                closed.append(value+ ' (did not successfully connect to '+key+
                                        '. You may need to unblock this port to connect.)')
            ### labelling the (US ONLY) servers ###
            elif 'odaws03.oda.sas.com' in key or 'odaws04.oda.sas.com' in key:
                if 'OPEN' in value:
                    results.append(value+ ' (successfully connected to '+key+' (US ONLY))')
                elif 'CLOSED' in value:
                    closed.append(value+ ' (did not successfully connect to '+key+
                                         ' (US ONLY). You may need to unblock this port to connect.)')

        #### IF ALL PORTS ARE OPEN: ###
        if len(closed) == 0:
            self.output_textbox.insert(END,'Congratulations! The SAS OnDemand Port Checker did not detect'+
                                   ' any blockages in your connection.\n\nAll tests performed on '+
                                   'your machine have been successful. While open ports are one of '+
                                   'the most common causes of connection failures, this does not '+
                                   'guarantee that other issues may be present on your system. If '+
                                   'you are still having issues connecting to the SAS Analytics U '+
                                   'servers, you are encouraged to contact SAS Technical Support for'+
                                   ' further investigation. Below is a summary of the ports that were'+
                                   ' tested.')
            self.output_textbox.insert(END, '\n\nThe following ports tested as successful. No further action '+
                                    'is required for these ports:\n\n')
            self.output_textbox.config(state=DISABLED)                     
        ### IF ANY OF THE PORTS ARE CLOSED: ###
        else:
            self.output_textbox.insert(END,'Unfortunately, we discovered that there were some network ports being'+
                                   ' blocked on your system.\n\nWhile closed ports are one of the most '+
                                   'common causes of connection failures, this does not guarantee that'+
                                   ' other issues may be present on your system. If you are still having '+
                                   'issues connecting to the SAS Analytics U servers, you are encouraged '+
                                   'to contact SAS Technical Support for further investigation. Below is a'+
                                   ' summary of the ports that were tested.')
            self.output_textbox.insert(END, '\n\nThe following ports tested as follows. No further action is required'+
                                    ' for any OPEN ports:\n\n')
            
        ### Output the OPEN/CLOSED port results ###   
        for result in results:
            self.output_textbox.config(state=NORMAL)
            self.output_textbox.insert(END, result)
            self.output_textbox.insert(END, '\n')
        self.output_textbox.insert(END, '\n\n')
        self.output_textbox.config(state=DISABLED)
#-------------------------- Main Event Listener Loop for the GUI window ------------------------------------#
if __name__ == "__main__":
    root = Tk()
    PortcheckerGUI = ODAPortChecker(root)
    root.mainloop()
