#!/usr/bin/env python
''' Redner a template '''

from jinja2 import Template

template = Template("interface {{ intf }} \n    shutdown")

for eth in  [1, 2]:
    print template.render(intf="Ethernet%s", % eth)
