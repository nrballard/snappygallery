snappygallery
=============
Snappygallery is a utility for quickly generating simple, lightweight HTML galleries.

It works by iterating through the image files in a specified image directory and then creating a table of linked thumbnails to each image. The images themselves are not modified, nor are any new images created. The thumbnails and corresponding overlays are sized through simple manipulation of the HTML “width” and “height” attributes.

FEATURES:<br />
Snappygallery is run on the command line using the image directory and output file as the respective arguments<br />

Snappygallery depends on JQuery to provide the the gallery functionality of the output file. If it does not find JQuery in a directory with the output file at runtime, it will download the file or exit.


LIMITATIONS:<br />
—Snappygallery does not currently generate galleries spanning multiple pages. Consequently, large image directories will generate large HTML files that may load slowly in the browser.<br />
-Similarly, galleries with large image files may load slowly since Snappygallery does not resize the gallery images.
