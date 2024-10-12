import requests

PROVIDERS = {
    "AT&T Mobility LLC": {"sms": "txt.att.net", "alt_sms": "", "mms": "mms.att.net", "mms_support": True, "level":1},
    "Boost Mobile": {
        "sms": "sms.myboostmobile.com",
        "alt_sms": "",
        "mms": "myboostmobile.com",
        "mms_support": True,
        "level": 2
    },
    "Cellular South Licenses LLC (C Spire Wireless)": {"sms": "cspire1.com", "alt_sms": "", "mms_support": False, "level": 3},
    "Cricket Wireless": {
        "sms": "sms.cricketwireless.net",
        "alt_sms": "",
        "mms": "mms.cricketwireless.net",
        "mms_support": True,
        "level": 2
    },
    "Consumer Cellular": {"sms": "mailmymobile.net", "alt_sms": "", "mms_support": False, "level": 3},
    "Google Project Fi": {"sms": "msg.fi.google.com", "alt_sms": "", "mms_support": True, "level": 3},
    "Metro PCS": {"sms": "mymetropcs.com", "alt_sms": "", "mms_support": True, "level": 2},
    "Mint Mobile": {"sms": "mailmymobile.net", "alt_sms": "", "mms_support": False, "level": 3},
    "Page Plus": {
        "sms": "vtext.com",
        "alt_sms": "",
        "mms": "mypixmessages.com",
        "mms_support": True,
        "level": 2
    },
    "Republic Wireless": {
        "sms": "text.republicwireless.com",
        "alt_sms": "",
        "mms_support": False,
        "level": 3
    },
    "Sprint": {
        "sms": "messaging.sprintpcs.com",
        "alt_sms": "",
        "mms": "pm.sprint.com",
        "mms_support": True,
        "level": 2
    },
    "Straight Talk": {
        "sms": "vtext.com",
        "alt_sms": "",
        "mms": "mypixmessages.com",
        "mms_support": True,
        "level": 2 
    },
    "T-Mobile USA Inc.": {"sms": "tmomail.net", "alt_sms": "", "mms_support": True, "level":1},
    "T-Mobile Puerto Rico LLC": {"sms": "tmomail.net", "alt_sms": "", "mms_support": True, "level":1},
    "Ting": {"sms": "message.ting.com", "alt_sms": "", "mms_support": False, "level":3},
    "Tracfone": {"sms": "", "alt_sms": "", "mms": "mmst5.tracfone.com", "mms_support": True, "level": 3},
    "United States Cellular Corp. (U.S. Cellular)": {
        "sms": "email.uscc.net",
        "alt_sms": "uscc.textmsg.com",
        "mms": "mms.uscc.net",
        "mms_support": True,
        "level":1,
    },
    "Cellco Partnership (Verizon Wireless)": {"sms": "vtext.com", "alt_sms": "", "mms": "vzwpix.com", "mms_support": True, "level":1},
    "Virgin Mobile": {
        "sms": "vmobl.com",
        "mms": "vmpix.com",
        "alt_sms": "",
        "mms_support": True,
        "level": 1
    },
    "Xfinity Mobile": {
        "sms": "vtext.com",
        "alt_sms": None,
        "mms": "mypixmessages.com",
        "mms_support": True,
        "level": 2
    },
}
# most_popular_providers
level_1_providers = [
    "AT&T",
    "Verizon",
    "T-Mobile",
    "U.S. Cellular",
    # top 4
    "Cricket Wireless",  # Parent: AT&T~
    "Page Plus",         # Uses Verizon network
    "Straight Talk",     # Uses Verizon network
    "Xfinity Mobile",    # Uses Verizon network
    "Metro PCS",         # Parent: T-Mobile
    "Boost Mobile",      # Parent: T-Mobile (formerly Sprint)
    "Sprint",            # Merged with T-Mobile
    "Virgin Mobile",
    "Consumer Cellular", # Uses AT&T and T-Mobile networks
    "Google Project Fi", # Uses T-Mobile and US Cellular networks
    "Mint Mobile",       # Uses T-Mobile network
    "Republic Wireless", # Uses T-Mobile network
    "Ting",              # Uses T-Mobile and Verizon networks
    "Tracfone",          # Uses AT&T, T-Mobile, Verizon, and Sprint networks
    "C-Spire"            # Uses its own network but also roams on other networks  
]
# providers_with_parent_companies
level_2_providers = [
   # Parent: T-Mobile
    "Cricket Wireless",  # Parent: AT&T
    "Page Plus",         # Uses Verizon network
    "Straight Talk",     # Uses Verizon network
    "Xfinity Mobile",    # Uses Verizon network
    "Metro PCS",         # Parent: T-Mobile
    "Boost Mobile",      # Parent: T-Mobile (formerly Sprint)
    "Sprint",            # Merged with T-Mobile
    "Virgin Mobile"   
]

# providers_using_same_network
level_3_providers = [
    "Consumer Cellular", # Uses AT&T and T-Mobile networks
    "Google Project Fi", # Uses T-Mobile and US Cellular networks
    "Mint Mobile",       # Uses T-Mobile network
    "Republic Wireless", # Uses T-Mobile network
    "Ting",              # Uses T-Mobile and Verizon networks
    "Tracfone",          # Uses AT&T, T-Mobile, Verizon, and Sprint networks
    "C-Spire"            # Uses its own network but also roams on other networks
]

def look_up(value):
    for provider, details in PROVIDERS.items():
        if details["level"] == 1:
            
            if details["sms"] == value or details["alt_sms"] == value:
                return provider
    for provider, details in PROVIDERS.items():
        if details["level"] == 2:
            
            if details["sms"] == value:
                return provider
    for provider, details in PROVIDERS.items():
        if details["level"] == 3:
            
            if details["sms"] == value:
                return provider
    return None
