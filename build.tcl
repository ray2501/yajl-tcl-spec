#!/usr/bin/tclsh

set arch "x86_64"
set base "yajl-tcl-1.6.2"
set fileurl "https://github.com/flightaware/yajl-tcl/archive/v1.6.2.tar.gz"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb yajl-tcl.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base.tar.gz
