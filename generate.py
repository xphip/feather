#!/usr/bin/python
#

import os
import subprocess
import sys

def CSSMaker():
	output = 'css/icons_list.css'
	css = ''

	for icon in os.listdir('./icons'):
		[name, ext] = icon.split('.')
		css += 'i[data-feather="{}"]:after {{ background-image: url(../icons/{}); }}\n'.format(name, icon);

	f = open(output, 'w+')
	f.write(css)
	f.close()

	print 'Output: ' + output

def CSSUriMaker():
	output = 'css/icons_list_emb.css'
	css = ''

	for icon in os.listdir('./icons'):
		[name, ext] = icon.split('.')
		i = SVGMinify(icon, './icons', './icons-min')
		i = 'data:image/svg+xml;utf8,' + i
		css += """i[data-feather="{}"]:after {{ background-image: url('{}'); }}\n""".format(name, i);

	f = open(output, 'w+')
	f.write(css)
	f.close()

def SVGMinify(icon, icons_dir, icons_min_dir):
	# icons_dir = './icons'
	# icons_min_dir = './icons-min'

	[name, ext] = icon.split('.')
	icon_min = "{}/{}.min.{}".format(icons_min_dir, name, ext)
	i = "{}/{}.{}".format(icons_dir, name, ext)

	if os.path.exists(icon_min) == 0:
		subprocess.call(['svgo', '-q', i, '-o', icon_min])

	f = open(icon_min)
	i = f.read()
	f.close()

	return i

# # OLD
# def SVGMinify():
# 	icons_dir = './icons'
# 	icons_min_dir = './icons-min'
# 	total_icons = 0

# 	for icon in os.listdir(icons_dir):
# 		[name, ext] = icon.split('.')
# 		icon_min = "{}/{}.min.{}".format(icons_min_dir, name, ext)
# 		i = "{}/{}.{}".format(icons_dir, name, ext)
# 		if os.path.exists(icon_min) == 0:
# 			subprocess.call(['svgo', '-q', i, '-o', icon_min])
# 			total_icons += 1

# 	if total_icons > 0:
# 		print 'Total icons minified: ' + str(total_icons)

def Usage():
	print """
	[USAGE]
	./generate.py [OPTIONS]

	[OPTIONS]
	css 		Gera o arquivo CSS conforme os ./icones.
	cssuri 		Gera o arquivo CSS conforme os ./icones, inclusos no arquivo de estilo.
	"""
	pass

if __name__ == "__main__":
	if len(sys.argv) > 1:

		if sys.argv[1] == "css":
			CSSMaker()
			print 'Done!'

		elif sys.argv[1] == "cssuri":
			CSSUriMaker()
			print 'Done!'
	else:
		Usage()
