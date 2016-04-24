#!/usr/bin/python

import os
import glob
import sys
import re
import urllib2
from os import path


def directory_separator():
    """Determines appropriate directory delimiter
    Based on the operating system
    (Assuming Windows or POSIX-Compatible systems)"""

    if os.name == 'nt':
        return '\\'
    else:
        return '/'


def get_jquery(gallery_file):
    jquery_found = False
    gallery_dir = path.dirname(path.abspath(gallery_file)) + directory_separator()
    for x in glob.glob(gallery_dir + "jquery*.js"):
        jquery_found = True
        break
    if jquery_found:
        print "Found", x
        return path.basename(x)

    if not jquery_found:
        ans = ""
        while not ans.lower() == "y" or "n":
            ans = raw_input("JQuery library not found. Download it now? [Y/n] ")
            if ans.lower() == "n":
                print "Exiting."
                sys.exit(0)
            elif ans.lower() == "y" or ans.lower() == "":
                print "Downloading..."
                dl_req = urllib2.Request("http://jquery.com/download", headers={"User-Agent": "lynx"})
                dl_page = urllib2.urlopen(dl_req).read()
                matches = re.findall("https://code\.jquery\.com/jquery-[0-9]*\.?[0-9]*\.?[0-9]*\.min\.js", dl_page)
                matches.sort()      # Sort source files by version number if not already done
                target = matches[0] # Download lowest version number to ensure we get a stable version
                with open(gallery_dir + path.basename(target), 'wb') as outfile:
                    for line in urllib2.urlopen(target).readlines():
                        outfile.write(line)
                print path.basename(target) + " downloaded successfully"
                return path.basename(target)
            else:
                ans = raw_input("Invalid input. Press Enter to continue.")


def make_link(img_loc):
    """Injects a given file path into a hyperlinked <img> tag
    and uses the filename as a generic 'alt' property."""

    return str("<a href=\"javascript:showImg('" + img_loc + 
                    "')\">" + "<img width=\"240\" height=\"180\" src=\"" + img_loc + "\"" +
                    " alt=\"" + img_loc.split(directory_separator())[-1] + "\" /></a>""")


def generate_gallery(img_dir, gallery_file, jquery_loc):
    tab = "    "
    file_list = []
    counter = 0

# Loop through all files in the image directory and make a list of all files with the appropriate extensions
    for x in glob.glob(img_dir + '*'):
        if (x.split('.')[-1]).lower() in ('jpg', 'jpeg', 'gif', 'png', 'svg'):
            rel_dir = path.join(path.relpath(path.dirname(x), path.dirname(gallery_file)), path.basename(x))
            file_list.append(rel_dir)

    for y in file_list:
        if os.name == 'nt' and '\\' in y:
            '\\'.replace('/')

# Boilerplate code for output file
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
                td {
                        text-align: center;
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
                        max-width: 640;
                        max-height: 480;
		}

	</style>
        <script type="text/javascript" src=""" + '"' +  jquery_loc + '"'  """></script>
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

# Create a table 3 columns wide and n rows long,
# where n is an even multiple of 3 and number of files in the list

        for x in range(len(file_list) / 3):
            outfile.write(tab*3 + "<tr>\n")
            for y in range(3):
                outfile.write(tab*4 + "<td>" + make_link(file_list[counter]) + "</td>\n")
                counter += 1
            outfile.write(tab*3 + "</tr>\n")
        outfile.write(tab*2 + "</table>\n")

# If the number of files was not an even multiple of 3, add the remaining files
# in a center-aligned row beneath the table.
        if len(file_list) % 3 != 0:
            outfile.write(tab*2 + "<div style=\"display: block; text-align: center\">\n")
            for x in range(len(file_list) % 3):
                outfile.write(tab*3 + make_link(file_list[counter]) + "\n")
                counter += 1
            outfile.write(tab*2 + "</div>")
        outfile.write("""
    </body>
</html>""")

def main(img_dir, gallery_file):
    img_count = 0

    if not path.exists(img_dir):
        print "Invalid image directory"
        return

    if not img_dir[-1] == directory_separator():
        img_dir += directory_separator()

    for x in glob.glob(img_dir + '*'):
        if (x.split('.')[-1]).lower() in ('jpg', 'jpeg', 'gif', 'png', 'svg'):
            img_count += 1

    if img_count == 0:
        print "No browser-compatible images in directory provided"
        return

    print "Looking for JQuery..."
    jquery = get_jquery(gallery_file)

    print "Generating gallery..."
    generate_gallery(img_dir, gallery_file, jquery)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "USAGE: snappygallery IMAGE_DIRECTORY OUTPUT_FILE/n"

    else:
        img_dir = sys.argv[1]
        gallery_file = sys.argv[2]

        main(img_dir, gallery_file)
