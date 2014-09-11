#!/usr/bin/python

import os       
from os import path
import glob
import sys

def directory_separator():
    """Determine appropriate directory delimiter
    Based on the operating system
    (Assuming Windows or POSIX-Compatible systems)"""

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
        outfile.write("""
<html>
    <head>
        <title>Gallery</title>
	<style>
		body {
			z-index: 1;
			width: 100%;
		}
		table {
			margin-right: auto;
			margin-left: auto;
		}
		#imgView {
			height: 100%;
			width: 100%;
			background-color: black;
			text-align: center;
			position: fixed;
			z-index: 2;
			display: none;
		}
		#imgView img {
			left: auto;
			right: auto;
			margin-top: 100px;
		}

	</style>
        <script type="text/javascript" src="jquery-1.11.1.min.js"></script>
	<script>
		var closeImg = function() {
			$('#imgView img').remove();
			$('#imgView br').remove();
			$('#imgView a').remove();
			$('#imgView').toggle('fast');
			$('h1').toggle('fast');
		};
		var showImg = function(imgFile) {
			$('h1').toggle('fast');
			$('#imgView').toggle('fast');
			$('#imgView').append('<img src="' + imgFile + '"><br />');
			$('#imgView').append('<a href="javascript:closeImg()">Back to Gallery</a>');
		};
	</script>
    </head>
    <body>
    <div id="imgView"></div>
    <h1 style="text-align: center">Gallery</h1>
        <table>\n""")
        for x in range(7):
            outfile.write(tab*3 + "<tr>\n")
            for y in range(3):
                outfile.write(tab*4 + "<td><a href=\"javascript:showImg('" + file_list[counter] + 
                    "')\">" + "<img width=\"240\" height=\"180\" src=\"" + file_list[counter] + "\"" +
                    " alt=\"" + file_names[counter] + "\" /></a></td>\n")
                counter += 1
            outfile.write(tab*3 + "</tr>\n")
        outfile.write("""
        </table>
    </body>
</html>""")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: pygallery <IMAGE_DIRECTORY> <OUTPUT_FILE>"
    else:
        img_dir = sys.argv[1]
        gallery_file = sys.argv[2]
        generate_gallery(img_dir, gallery_file)

