#!/usr/bin/python
################################################################################
########################This will create Base Site Policies#####################
################################################################################

from pandevice import panorama
from pandevice import firewall
from pandevice import network
from pandevice import device
from pandevice import policies
import sys

#Top level variables populated by ansible playbook

panorama_name = sys.argv[3]
username = sys.argv[1]
password = sys.argv[2]

location_code = "TUKI"
closet_type = "MDF"
model = "PA-820"

############################################################################################
###############################Begin Configuration##########################################
############################################################################################
device_group = '{0}{1}'.format("DG-LOCAL-", location_code)

phl_pan = panorama.Panorama(panorama_name, username, password)

devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
devicegroup.create()


# Create Panorama Site Policies

#Create DNS policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_DNS_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "dns", \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create SSH policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_SSH_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "ssh", \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create RDP policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_RDP_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "ms-rdp", \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create ICMP policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_ICMP_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "ping", \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create VPN policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_VPN_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "ipsec", \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create HTTP8080 policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_HTTP8080_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "any", \
                service = "CUST-HTTP-8080", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create Teamviewer policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_TEAMVIEWER_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = [ "adobe-flash-socketpolicy-server", "ssl", "teamviewer", "web-browsing" ], \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()


#Create Apple Cloud policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_APPLE_CLOUD_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = [ "apple-push-notifications", "ssl",  "web-browsing" ], \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create Google Cloud policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_GOOGLE_CLOUD_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = [ "google-base", "ssl",  "web-browsing" ], \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create Web Access policy for Guest Wireless
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_WEB_ACCESS_GUESTWLAN", \
                fromzone = ["trust_guest_wlan"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "any", \
                service = ["service-http", "service-https" ], \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()




###############Trust Policies################

#Create SSH policy for trust
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_SSH", \
                fromzone = ["trust"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "ssh", \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create RDP policy for trust
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_RDP", \
                fromzone = ["trust"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "ms-rdp", \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create ICMP policy for trust
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_ICMP", \
                fromzone = ["trust"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = "ping", \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()


#Create Teamviewer policy for trust
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_TEAMVIEWER", \
                fromzone = ["trust"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = [ "adobe-flash-socketpolicy-server", "ssl", "teamviewer", "web-browsing" ], \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()


#Create Apple Cloud policy for trust
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_APPLE_CLOUD", \
                fromzone = ["trust"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = [ "apple-push-notifications", "ssl",  "web-browsing" ], \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()

#Create Google Cloud policy for trust
devicegroup = panorama.DeviceGroup(device_group)
phl_pan.add(devicegroup)
postrulebase = policies.PostRulebase()
devicegroup.add(postrulebase)
sec_rule = policies.SecurityRule("R_ALLOW_GOOGLE_CLOUD", \
                fromzone = ["trust"], \
                tozone = ["untrust"], \
                source = "any", \
                destination = "any", \
                application = [ "google-base", "ssl",  "web-browsing" ], \
                service = "application-default", \
                action = "allow", \
                log_setting = "LFP-POLICY1", \
                log_end = True, \
                group = "SPG-Default", \
                )
postrulebase.add(sec_rule)
sec_rule.create()
