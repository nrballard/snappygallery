#!/usr/bin/python

import os
from os import path
import glob
import sys

def directory_separator():
    if os.name == 'nt':
        return '\\'
    else:
        return '/'

def generate_gallery(img_dir, gallery_file):
    tab = "    "
    file_list = []
    file_names = []
  
    counter = 0
    for x in glob.glob(img_dir + '*.jpg'):
        rel_dir = path.join(path.relpath(path.dirname(x), path.dirname(gallery_file)), path.basename(x))
        file_list.append(rel_dir)

    for x in file_list:
        file_names.append(x.split(directory_separator())[-1])

    with open(gallery_file, "w") as outfile:
        outfile.write("""<html>
{}<head>
{}<title>Gallery</title>
{}<head>
{}<body>
{}<table>\n""".format(tab, tab*2, tab, tab, tab*2))
        for x in range(7):
            outfile.write(tab*3 + "<tr>\n")
            for y in range(3):
                outfile.write(tab*4 + "<td><a href=\"javascript:showImg('" + file_list[counter] + 
                    "')\">" + "<img width=\"240\" height=\"180\" src=\"" + file_list[counter] + "\"" +
                    " alt=\"" + file_names[counter] + "\" /></a></td>\n")
                counter += 1
            outfile.write(tab*3 + "</tr>\n")
        outfile.write("""{}</table>
{}</body>
</html>""".format(tab*2, tab))

if len(sys.argv) < 3:
    print "Usage: pygallery <IMAGE_DIRECTORY> <GALLERY_FILE>"
else:
    img_dir = sys.argv[1]
    gallery_file = sys.argv[2]
    generate_gallery(img_dir, gallery_file)


