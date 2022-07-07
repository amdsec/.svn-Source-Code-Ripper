# .svn-Source-Code-Ripper
Apache Subversion Source Code Ripper


Apache SVN exposes /.svn/wc.db SQLite file which contains checksums for each file in the repository, the source code can be accessed by accessing `/.svn/pristine/(first two letters of checksum)/(checksum).svn-base`, this scripts scrapes all of the checksums and recompiles the source code from the site. 
