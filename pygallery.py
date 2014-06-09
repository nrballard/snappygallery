#!/usr/bin/python

import glob

tab = "    "
filelist = []
filenames = []
counter = 0

for x in glob.glob("nbnet/imgs/*"):
    filelist.append(x)

for x in filelist:
    filenames.append(x.split("/")[2])

with open("gallery.html", "w") as outfile:
    outfile.write("""<html>
{}<head>
{}<title>Gallery</title>
{}<head>
{}<body>
{}<table>\n""".format(tab, tab*2, tab, tab, tab*2))
    for x in range(7):
        outfile.write(tab*3 + "<tr>\n")
        for y in range(3):
            outfile.write(tab*4 + "<td><a href=\"" + filelist[counter] + 
                "\">" + "<img src=\"" + filelist[counter] + "\"" +
                " " + "alt=\"" + filenames[counter] + "\" /></a></td>\n")
            counter += 1
        outfile.write(tab*3 + "</tr>\n")
    outfile.write("""{}</table>
{}</body>
</html>""".format(tab*2, tab))

