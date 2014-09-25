snappygallery
=============
Snappygallery is a utility for quickly generating simple, lightweight HTML galleries.

It works by iterating through the image files in a specified image directory and then creating a table of linked thumbnails to each image. The images themselves are not modified, nor are any new images created. The thumbnails and corresponding overlays are sized through simple manipulation of the HTML “width” and “height” attributes.

FEATURES:
Snappygallery can be run in two ways:<br />
—Using traditional command-line argument passing, where the image directory and output file are passed in as the respective arguments<br />
—Without arguments in an interactive mode, in which the user is prompted to supply the location of the image directory and output file.

Snappygallery depends on JQuery to provide the the gallery functionality of the output file. If it does not find JQuery in a directory with the output file at runtime, it will download the file or exit.


LIMITATIONS:<br />
—Snappygallery does not currently generate galleries spanning multiple pages.
