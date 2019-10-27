#!/usr/bin/python
#

import os

output = 'css/icons_list.css'
css = ''

for icon in os.listdir('./icons'):
	[name, ext] = icon.split('.')
	css += 'i[data-feather="{}"]:after {{ background-image: url(../icons/{}); }}\n'.format(name, icon);

f = open(output, 'w+')
f.write(css)
f.close()

print 'Output: ' + output
print 'Done!'