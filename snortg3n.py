#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#General Params
id_change = ""
initialSID = 0

#Rule structure
ruleHeader = {'action':'alert', 'protocol':'udp', 'srcIP':'any', 'srcPort':'any'
              , 'direction':'->', 'dstIP':'any', 'dstPort':'53'}

header = ruleHeader['action']+" "+ruleHeader['protocol']+" "+ruleHeader['srcIP']+" "+ruleHeader['srcPort']+" "+ruleHeader['direction']+" "+ruleHeader['dstIP']+" "+ruleHeader['dstPort']
print(header)

#Rule Options
msg = 'msg:\"LOCAL-RULES' + str(id_change) +"\"; "
content = "content:" + "; "
nocase = "nocase" + "; "
sid = initialSID
rev = "rev:1" + ";"