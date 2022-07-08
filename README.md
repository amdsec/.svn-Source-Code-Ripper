# .svn-Source-Code-Ripper
Apache Subversion Source Code Ripper


Apache SVN exposes /.svn/wc.db SQLite file.
This file contains an index of files within SVN, filename, location and checksum.
SVN stores the source code for these files in  `/.svn/pristine/`.
You can access these files by using the sha1 checksum inside the SQLLite database file. 
`/.svn/pristine/(first two letters of checksum)/(checksum).svn-base`

This scripts iterates over all of the checksums and filenames within the database to recompile the source code of the target website.


Use responsibily.
