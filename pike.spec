Name: pike
Version: 7.8.866
#Version: 8.0.610
Release: 39.1
Summary: Powerful Interpreted Programming Language
URL: http://pike.lysator.liu.se/
License: GPL 2, LGPL 2.1, MPL 1.1
Group: Development/Languages/Other
Source: http://pike.lysator.liu.se/pub/pike/latest-stable/Pike-v%{version}.tar.gz
BuildRequires: bison, autoconf, automake, m4
BuildRequires: zlib-devel, bzip2, libxml2-devel, gmp-devel, gdbm-devel, pcre-devel
BuildRequires: libjpeg-devel libpng-devel giflib-devel libtiff-devel freetype freetype-devel
# mDNSResponder-lib needed to clarify dependency for librsvg
#BuildRequires: mDNSResponder-lib librsvg-devel
#BuildRequires: avahi-compat-mDNSResponder-devel mysql-devel
BuildRequires: libpq-devel, unixODBC-devel
BuildRequires: openssl-devel, krb5-devel
BuildRequires: libglade2-devel, SDL-devel, gtk2-devel, libglade2, libgnome-devel, libgnomeui-devel, libgnomecanvas-devel
BuildRequires: freeglut-devel
BuildRequires: fuse-devel
BuildRequires: sqlite-devel
BuildRequires: librsvg2-devel
BuildRequires: SDL_mixer-devel
BuildRequires: fftw-devel
BuildRequires: nettle-devel
BuildRequires: w3m udisks2

%description
Pike is an interpreted, object-oriented, dynamic programming language
with a syntax similar to C. It includes many powerful data types and
a module system that, for instance, provides image manipulation with
support for graphics formats like SVG, JPG, PNG, GIF, XCF and many
others,  database connectivity, advanced cryptography, XML and HTML parsers
and others.

%package bzip2
Summary: Bzip2 Module for Pike
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description bzip2
This Pike module provides bzip2 compression.


%package devel
Summary: Development Files for C Modules for Pike
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description devel
This package contains files you will need to develop C extension modules
for Pike. The package depends on  the recommended set of packages for the
Pike  environment.


#%package doc
#Summary: Pike Developer Documentation
#Group: Documentation/Other
#Requires: %{name} = %{version}
#BuildArch: noarch

#%description doc
#Developer documentation (API reference and manual) for Pike.


%package gdbm
Summary: Pike gdbm Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description gdbm
This Pike module provides access to gdbm databases.


#%package gl
#Summary: Pike OpenGL Module
#Group: Development/Languages/Other
#Requires: %{name} = %{version}
#
#%description gl
#This Pike module provides OpenGL and freeglut suppport for Pike.


%package gtk2
Summary: Pike GTK2 Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description gtk2
This Pike module provides access to the GTK+ framework.


%package image
Summary: Pike Image Support Modules
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description image
These modules provide many powerful image processing functions to Pike
programs.


%package mysql
Summary: Pike MySQL Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description mysql
This Pike module provides access to MySQL databases.


%package odbc
Summary: Pike ODBC Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description odbc
This Pike module provides ODBC-based database access.


%package pcre
Summary: Pike PCRE Regular Expression Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description pcre
This Pike module provides PCRE regular expression support.


#%package pdf
#Summary: Pike PDF Module
#Group: Development/Languages/Other
#Requires: %{name} = %{version}
#
#%description pdf
#This Pike module provides support for the PDF portable document format.


#%package perl
#Summary: Pike Module for Perl Support
#Group: Development/Languages/Other
#Requires: %{name} = %{version}
#
#%description perl
#This Pike module provides support for the Perl programming language in Pike.


%package postgres
Summary: Pike Postgres Database Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description postgres
This Pike module provides access to Postgres databases.


%package sane
Summary: Pike SANE Scanner Access Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description sane
This Pike module provides support for the SANE scan solution.


%package sdl
Summary: Pike SDL Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description sdl
This Pike module provides support for the SDL programming framework and mixer.


%package svg
Summary: Pike Support for SVG Vector Graphics
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description svg
This Pike module provides support for SVG vector graphics.


%package gssapi
Summary: Pike GSSAPI Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description gssapi
This Pike module provides support for the MIT Kerberos5 Implementation.



%package sqlite
Summary: Pike SQLite Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description sqlite
This Pike module provides support for the SQLite.


%package fuse
Summary: Pike Fuse Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description fuse
This Pike module provides support for the Fuse.


%package search
Summary: Pike Search Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description search
This Pike module provides support for the integrated Search.


%package zxid
Summary: Pike ZXID Module
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description zxid
This Pike module provides support for the ZXID.


%prep
%setup -q -n Pike-v%{version}
# fix pike binary path in scripts:
for USRLOCALBINPIKE_FILE in `grep -Rl "/usr/local/bin/pike" *` ; do
  cp $USRLOCALBINPIKE_FILE $USRLOCALBINPIKE_FILE.bak
  cat $USRLOCALBINPIKE_FILE.bak | sed -e "s|/usr/local/bin/pike|%{_bindir}/pike|g" > $USRLOCALBINPIKE_FILE
  rm -f $USRLOCALBINPIKE_FILE.bak
done

%build
%define machine_code --with-machine-code
make CONFIGUREARGS="--prefix=%{_prefix} --with-freetype --with-ttflib --with-gif --with-jpeglib --with-tifflib --with-svg --with-gmp --with-bignums --without-mysql --without-gdbm --with-odbc --with-postgres --with-zlib --with-pdflib --with-gtk2 --with-libpcre --without-GL --with-GLUT --with-sane --with-SDL --with-Fuse --with-sqlite %{machine_code}" all
#make doc

%install
rm -rf $RPM_BUILD_ROOT
make buildroot=$RPM_BUILD_ROOT INSTALLARGS="--traditional" install_nodoc

# remove pike.syms:
rm -f $RPM_BUILD_ROOT%{_bindir}/pike.syms

# remove build specs from include directory:
rm -f $RPM_BUILD_ROOT%{_includedir}/pike/specs

# move manpage to correct location:
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
if [ -d $RPM_BUILD_ROOT%{_prefix}/man/man1 ]; then
    [ -e $RPM_BUILD_ROOT%{_prefix}/man/man1/pike.1 ] && mv $RPM_BUILD_ROOT%{_prefix}/man/man1/pike.1 $RPM_BUILD_ROOT%{_mandir}/man1/
    [ -e $RPM_BUILD_ROOT%{_prefix}/man/man1/pike.1.gz ] && mv $RPM_BUILD_ROOT%{_prefix}/man/man1/pike.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/
fi

# remove documentation sources that shouldn't have been installed:
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/pike

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING COPYRIGHT ANNOUNCE COMMITTERS
%{_bindir}/pike
%{_bindir}/hilfe
%{_bindir}/rsif
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/0.6
%dir %{_libdir}/%{name}/0.6/modules
%dir %{_libdir}/%{name}/7.0
%dir %{_libdir}/%{name}/7.0/include
%dir %{_libdir}/%{name}/7.0/modules
%dir %{_libdir}/%{name}/7.0/modules/Calendar.pmod
%dir %{_libdir}/%{name}/7.0/modules/Stdio.pmod
%dir %{_libdir}/%{name}/7.2
%dir %{_libdir}/%{name}/7.2/modules
%dir %{_libdir}/%{name}/7.2/modules/LR.pmod
%dir %{_libdir}/%{name}/7.2/modules/Parser.pmod
%dir %{_libdir}/%{name}/7.2/modules/Parser.pmod/XML.pmod
%dir %{_libdir}/%{name}/7.2/modules/Protocols.pmod
%dir %{_libdir}/%{name}/7.2/modules/Protocols.pmod/LDAP.pmod
%dir %{_libdir}/%{name}/7.4
%dir %{_libdir}/%{name}/7.4/include
%dir %{_libdir}/%{name}/7.4/modules
%dir %{_libdir}/%{name}/7.4/modules/ADT.pmod
%dir %{_libdir}/%{name}/7.4/modules/Locale.pmod
%dir %{_libdir}/%{name}/7.4/modules/Protocols.pmod
%dir %{_libdir}/%{name}/7.4/modules/SSL.pmod
%dir %{_libdir}/%{name}/7.4/modules/Sql.pmod
%dir %{_libdir}/%{name}/7.4/modules/Standards.pmod
%dir %{_libdir}/%{name}/7.4/modules/Standards.pmod/ASN1.pmod
%dir %{_libdir}/%{name}/7.4/modules/Standards.pmod/PKCS.pmod
%dir %{_libdir}/%{name}/7.4/modules/Stdio.pmod
%dir %{_libdir}/%{name}/7.4/modules/Tools.pmod
%dir %{_libdir}/%{name}/7.4/modules/Tools.pmod/Standalone.pmod
%dir %{_libdir}/%{name}/7.6
%dir %{_libdir}/%{name}/include
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/Audio.pmod
%dir %{_libdir}/%{name}/modules/Audio.pmod/Format.pmod
%dir %{_libdir}/%{name}/modules/Cache.pmod
%dir %{_libdir}/%{name}/modules/Cache.pmod/Policy.pmod
%dir %{_libdir}/%{name}/modules/Cache.pmod/Storage.pmod
%dir %{_libdir}/%{name}/modules/Calendar_I.pmod
%dir %{_libdir}/%{name}/modules/Filesystem.pmod
%dir %{_libdir}/%{name}/modules/GLUE.pmod
%dir %{_libdir}/%{name}/modules/GLUE.pmod/Driver.pmod
%dir %{_libdir}/%{name}/modules/Geography.pmod
%dir %{_libdir}/%{name}/modules/Graphics.pmod
%dir %{_libdir}/%{name}/modules/Graphics.pmod/Graph.pmod
%dir %{_libdir}/%{name}/modules/Languages.pmod
%dir %{_libdir}/%{name}/modules/Locale.pmod
%dir %{_libdir}/%{name}/modules/Locale.pmod/Language.pmod
%dir %{_libdir}/%{name}/modules/MIME.pmod
%dir %{_libdir}/%{name}/modules/Pike.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Server.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/IMAP.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/IRC.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/LDAP.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/SMTP.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/SNMP.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/X.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/db
%dir %{_libdir}/%{name}/modules/Protocols.pmod/XMLRPC.pmod
%dir %{_libdir}/%{name}/modules/Remote.pmod
%dir %{_libdir}/%{name}/modules/SSL.pmod
%dir %{_libdir}/%{name}/modules/Sql.pmod
%dir %{_libdir}/%{name}/modules/Stdio.pmod
%dir %{_libdir}/%{name}/modules/String.pmod
%dir %{_libdir}/%{name}/modules/Tools.pmod
%dir %{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod
%dir %{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod
%dir %{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/License.pmod
%dir %{_libdir}/%{name}/modules/Tools.pmod/Monger.pmod
%dir %{_libdir}/%{name}/modules/Yabu.pmod
%{_libdir}/%{name}/0.6/modules/.autodoc
%{_libdir}/%{name}/0.6/modules/Array.pmod
%{_libdir}/%{name}/0.6/modules/Regexp.pike
%{_libdir}/%{name}/0.6/modules/__default.pmod
%{_libdir}/%{name}/0.6/modules/readline.pmod
%{_libdir}/%{name}/7.0/include/simulate.h
%{_libdir}/%{name}/7.0/modules/.autodoc
%{_libdir}/%{name}/7.0/modules/Calendar.pmod/Austrian.pmod
%{_libdir}/%{name}/7.0/modules/Calendar.pmod/Gregorian.pmod
%{_libdir}/%{name}/7.0/modules/Calendar.pmod/ISO.pmod
%{_libdir}/%{name}/7.0/modules/Calendar.pmod/Julian.pmod
%{_libdir}/%{name}/7.0/modules/Calendar.pmod/Orthodox.pmod
%{_libdir}/%{name}/7.0/modules/Calendar.pmod/Stardate.pmod
%{_libdir}/%{name}/7.0/modules/Calendar.pmod/Swedish.pmod
%{_libdir}/%{name}/7.0/modules/Calendar.pmod/module.pmod
%{_libdir}/%{name}/7.0/modules/Colors.pmod
%{_libdir}/%{name}/7.0/modules/Simulate.pmod
%{_libdir}/%{name}/7.0/modules/Stack.pmod
%{_libdir}/%{name}/7.0/modules/Stdio.pmod/module.pmod
%{_libdir}/%{name}/7.0/modules/__default.pmod
%{_libdir}/%{name}/7.2/modules/.autodoc
%{_libdir}/%{name}/7.2/modules/Gmp.pmod
%{_libdir}/%{name}/7.2/modules/LR.pmod/Grammar_parser.pmod
%{_libdir}/%{name}/7.2/modules/LR.pmod/item.pike
%{_libdir}/%{name}/7.2/modules/LR.pmod/lr.pike
%{_libdir}/%{name}/7.2/modules/LR.pmod/parser.pike
%{_libdir}/%{name}/7.2/modules/LR.pmod/priority.pike
%{_libdir}/%{name}/7.2/modules/LR.pmod/rule.pike
%{_libdir}/%{name}/7.2/modules/LR.pmod/scanner.pike
%{_libdir}/%{name}/7.2/modules/Parser.pmod/XML.pmod/Tree.pmod
%{_libdir}/%{name}/7.2/modules/Parser.pmod/XML.pmod/module.pmod
%{_libdir}/%{name}/7.2/modules/Protocols.pmod/LDAP.pmod/client.pike
%{_libdir}/%{name}/7.2/modules/String.pmod
%{_libdir}/%{name}/7.2/modules/Thread.pmod
%{_libdir}/%{name}/7.2/modules/__default.pmod
%{_libdir}/%{name}/7.2/modules/system.pmod
%{_libdir}/%{name}/7.4/include/msql.h
%{_libdir}/%{name}/7.4/include/simulate.h
%{_libdir}/%{name}/7.4/modules/.autodoc
%{_libdir}/%{name}/7.4/modules/ADT.pmod/Heap.pike
%{_libdir}/%{name}/7.4/modules/Array.pmod
%{_libdir}/%{name}/7.4/modules/_Crypto.pmod
%{_libdir}/%{name}/7.4/modules/Crypto.pmod
%{_libdir}/%{name}/7.4/modules/Locale.pmod/Charset.pmod
%{_libdir}/%{name}/7.4/modules/Protocols.pmod/SMTP.pmod
%{_libdir}/%{name}/7.4/modules/Regexp.pmod
%{_libdir}/%{name}/7.4/modules/SSL.pmod/cipher.pike
%{_libdir}/%{name}/7.4/modules/SSL.pmod/constants.pike
%{_libdir}/%{name}/7.4/modules/SSL.pmod/sslfile.pike
%{_libdir}/%{name}/7.4/modules/Sql.pmod/sql.pike
%{_libdir}/%{name}/7.4/modules/Standards.pmod/ASN1.pmod/Encode.pmod
%{_libdir}/%{name}/7.4/modules/Standards.pmod/PKCS.pmod/Signature.pmod
%{_libdir}/%{name}/7.4/modules/Stdio.pmod/module.pmod
%{_libdir}/%{name}/7.4/modules/Thread.pmod
%{_libdir}/%{name}/7.4/modules/Tools.pmod/Standalone.pmod/extract_autodoc.pike
%{_libdir}/%{name}/7.4/modules/__default.pmod
%{_libdir}/%{name}/7.6/modules/
%{_libdir}/%{name}/include/array.h
%{_libdir}/%{name}/include/fifo.h
%{_libdir}/%{name}/include/getopt.h
%{_libdir}/%{name}/include/opengl.h
%{_libdir}/%{name}/include/process.h
%{_libdir}/%{name}/include/profiling.h
%{_libdir}/%{name}/include/regexp.h
%{_libdir}/%{name}/include/sql.h
%{_libdir}/%{name}/include/stack.h
%{_libdir}/%{name}/include/stdio.h
%{_libdir}/%{name}/include/string.h
%{_libdir}/%{name}/include/syslog.h
%{_libdir}/%{name}/master.pike
%{_libdir}/%{name}/master.pike.in
%{_libdir}/%{name}/master.pike.o
%{_libdir}/%{name}/modules/.autodoc
%{_libdir}/%{name}/modules/ADT.pmod
%{_libdir}/%{name}/modules/Arg.pmod
%{_libdir}/%{name}/modules/Array.pmod
%{_libdir}/%{name}/modules/Audio.pmod/Codec.pmod
%{_libdir}/%{name}/modules/Audio.pmod/Format.pmod/MP3.pike
%{_libdir}/%{name}/modules/Audio.pmod/Format.pmod/module.pmod
%{_libdir}/%{name}/modules/COM.so
%{_libdir}/%{name}/modules/Cache.pmod/Data.pike
%{_libdir}/%{name}/modules/Cache.pmod/Policy.pmod/Base.pike
%{_libdir}/%{name}/modules/Cache.pmod/Policy.pmod/Multiple.pike
%{_libdir}/%{name}/modules/Cache.pmod/Policy.pmod/Null.pike
%{_libdir}/%{name}/modules/Cache.pmod/Policy.pmod/Sized.pike
%{_libdir}/%{name}/modules/Cache.pmod/Policy.pmod/Timed.pike
%{_libdir}/%{name}/modules/Cache.pmod/Storage.pmod/Base.pike
%{_libdir}/%{name}/modules/Cache.pmod/Storage.pmod/Memory.pike
%{_libdir}/%{name}/modules/Cache.pmod/Storage.pmod/Yabu.pike
%{_libdir}/%{name}/modules/Cache.pmod/cache.pike
%{_libdir}/%{name}/modules/Calendar.pmod
%{_libdir}/%{name}/modules/Calendar_I.pmod/Austrian.pmod
%{_libdir}/%{name}/modules/Calendar_I.pmod/Gregorian.pmod
%{_libdir}/%{name}/modules/Calendar_I.pmod/ISO.pmod
%{_libdir}/%{name}/modules/Calendar_I.pmod/Julian.pmod
%{_libdir}/%{name}/modules/Calendar_I.pmod/Orthodox.pmod
%{_libdir}/%{name}/modules/Calendar_I.pmod/Stardate.pmod
%{_libdir}/%{name}/modules/Calendar_I.pmod/Swedish.pmod
%{_libdir}/%{name}/modules/Calendar_I.pmod/module.pmod
%{_libdir}/%{name}/modules/Colors.pmod
%{_libdir}/%{name}/modules/CommonLog.so
%{_libdir}/%{name}/modules/Crypto.pmod
%{_libdir}/%{name}/modules/DVB.so
%{_libdir}/%{name}/modules/Debug.pmod
%{_libdir}/%{name}/modules/Error.pmod
%{_libdir}/%{name}/modules/Filesystem.pmod/System.pike
%{_libdir}/%{name}/modules/Filesystem.pmod/Tar.pmod
%{_libdir}/%{name}/modules/Filesystem.pmod/module.pmod
%{_libdir}/%{name}/modules/Float.pmod
%{_libdir}/%{name}/modules/Function.pmod
%{_libdir}/%{name}/modules/GDK.pmod
%{_libdir}/%{name}/modules/GLU.pmod
%{_libdir}/%{name}/modules/GLUE.pmod/Driver.pmod/Interface.pike
%{_libdir}/%{name}/modules/GLUE.pmod/Events.pmod
%{_libdir}/%{name}/modules/GLUE.pmod/module.pmod
%{_libdir}/%{name}/modules/GLUT.so
%{_libdir}/%{name}/modules/Geography.pmod/Countries.pmod
%{_libdir}/%{name}/modules/Geography.pmod/Position.pike
%{_libdir}/%{name}/modules/Geography.pmod/module.pmod
%{_libdir}/%{name}/modules/Getopt.pmod
%{_libdir}/%{name}/modules/Gettext.so
%{_libdir}/%{name}/modules/Gnome.pmod
%{_libdir}/%{name}/modules/Graphics.pmod/Graph.pmod/create_bars.pike
%{_libdir}/%{name}/modules/Graphics.pmod/Graph.pmod/create_graph.pike
%{_libdir}/%{name}/modules/Graphics.pmod/Graph.pmod/create_pie.pike
%{_libdir}/%{name}/modules/Graphics.pmod/Graph.pmod/doc.txt
%{_libdir}/%{name}/modules/Graphics.pmod/Graph.pmod/graph.h
%{_libdir}/%{name}/modules/Graphics.pmod/Graph.pmod/module.pmod
%{_libdir}/%{name}/modules/Graphics.pmod/Graph.pmod/polyline.pike
%{_libdir}/%{name}/modules/Gz.pmod
%{_libdir}/%{name}/modules/HTTPAccept.so
%{_libdir}/%{name}/modules/Int.pmod
%{_libdir}/%{name}/modules/Java.pmod
%{_libdir}/%{name}/modules/Kerberos.so
%{_libdir}/%{name}/modules/Languages.pmod/PLIS.pmod
%{_libdir}/%{name}/modules/Local.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Charset.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Gettext.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/abstract.pike
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/cat.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/ces.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/deu.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/eng.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/fin.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/fra.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/hrv.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/hun.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/ita.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/jpn.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/mri.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/nld.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/nor.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/pol.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/por.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/rus.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/slv.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/spa.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/srp.pmod
%{_libdir}/%{name}/modules/Locale.pmod/Language.pmod/swe.pmod
%{_libdir}/%{name}/modules/Locale.pmod/module.pmod
%{_libdir}/%{name}/modules/MIME.pmod/ext_to_media_type.pmod
%{_libdir}/%{name}/modules/MIME.pmod/module.pmod
%{_libdir}/%{name}/modules/Mapping.pmod
%{_libdir}/%{name}/modules/Math.pmod
%{_libdir}/%{name}/modules/Msql.so
%{_libdir}/%{name}/modules/Multiset.pmod
%{_libdir}/%{name}/modules/Nettle.so
%{_libdir}/%{name}/modules/Object.pmod
%{_libdir}/%{name}/modules/Oracle.pmod
%{_libdir}/%{name}/modules/PDF.so
%{_libdir}/%{name}/modules/Parser.pmod
%{_libdir}/%{name}/modules/Pike.pmod/Security.pmod
%{_libdir}/%{name}/modules/Pike.pmod/module.pmod
%{_libdir}/%{name}/modules/Pipe.so
%{_libdir}/%{name}/modules/Process.pmod
%{_libdir}/%{name}/modules/Program.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod/Bencoding.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod/Generator.pike
%{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod/Peer.pike
%{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod/PeerID.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod/Port.pike
%{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod/Tracker.pike
%{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod/Torrent.pike
%{_libdir}/%{name}/modules/Protocols.pmod/Bittorrent.pmod/module.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/DNS.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/DNS_SD.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Query.pike
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Server.pmod/Chained.pike
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Server.pmod/Filesystem.pike
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Server.pmod/Port.pike
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Server.pmod/Proxy.pike
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Server.pmod/Request.pike
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Server.pmod/SSLPort.pike
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Server.pmod/module.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/Session.pike
%{_libdir}/%{name}/modules/Protocols.pmod/HTTP.pmod/module.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/IMAP.pmod/imap_server.pike
%{_libdir}/%{name}/modules/Protocols.pmod/IMAP.pmod/parse_line.pike
%{_libdir}/%{name}/modules/Protocols.pmod/IMAP.pmod/parser.pike
%{_libdir}/%{name}/modules/Protocols.pmod/IMAP.pmod/requests.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/IMAP.pmod/server.pike
%{_libdir}/%{name}/modules/Protocols.pmod/IMAP.pmod/types.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/IPv6.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/IRC.pmod/Client.pike
%{_libdir}/%{name}/modules/Protocols.pmod/IRC.pmod/Error.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/IRC.pmod/Raw.pike
%{_libdir}/%{name}/modules/Protocols.pmod/IRC.pmod/Requests.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/IRC.pmod/module.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/Ident.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/LDAP.pmod/*.pike
%{_libdir}/%{name}/modules/Protocols.pmod/LDAP.pmod/*.h
%{_libdir}/%{name}/modules/Protocols.pmod/LDAP.pmod/*.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/LMTP.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/LPD.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/Line.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod/ASync.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod/Connection.pike
%{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod/Helper.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod/ProtocolTypes.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod/Raw.pike
%{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod/Request.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod/Session.pike
%{_libdir}/%{name}/modules/Protocols.pmod/LysKOM.pmod/Threads.pike
%{_libdir}/%{name}/modules/Protocols.pmod/NNTP.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/OBEX.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/Ports.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/SMTP.pmod/module.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/SNMP.pmod/agent.pike
%{_libdir}/%{name}/modules/Protocols.pmod/SNMP.pmod/getcmd.pike
%{_libdir}/%{name}/modules/Protocols.pmod/SNMP.pmod/module.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/SNMP.pmod/protocol.pike
%{_libdir}/%{name}/modules/Protocols.pmod/SNMP.pmod/snmp_errors.h
%{_libdir}/%{name}/modules/Protocols.pmod/SNMP.pmod/snmp_globals.h
%{_libdir}/%{name}/modules/Protocols.pmod/TELNET.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/AUTHORS
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/Atom.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/Auth.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/Extensions.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/KeySyms.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/Requests.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/Types.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/XTools.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/Xlib.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/_Types.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/_Xlib.pmod
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/db/compose
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/db/compose.db
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/db/convert_compose.pike
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/db/keysyms
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/keysyms.h
%{_libdir}/%{name}/modules/Protocols.pmod/XMLRPC.pmod/module.pmod
%{_libdir}/%{name}/modules/Regexp.pmod
%{_libdir}/%{name}/modules/Remote.pmod/Client.pike
%{_libdir}/%{name}/modules/Remote.pmod/Server.pike
%{_libdir}/%{name}/modules/Remote.pmod/module.pmod
%{_libdir}/%{name}/modules/Remote.pmod/remote.h
%{_libdir}/%{name}/modules/SSL.pmod/*.pmod
%{_libdir}/%{name}/modules/SSL.pmod/*.pike
%{_libdir}/%{name}/modules/Shuffler.so
%{_libdir}/%{name}/modules/Sql.pmod/Sql.pike
%{_libdir}/%{name}/modules/Sql.pmod/null.pike
%{_libdir}/%{name}/modules/Sql.pmod/module.pmod
%{_libdir}/%{name}/modules/Sql.pmod/msql.pike
%{_libdir}/%{name}/modules/Sql.pmod/oracle.pike
%{_libdir}/%{name}/modules/Sql.pmod/pgsql.h
%{_libdir}/%{name}/modules/Sql.pmod/pgsql.pike
%{_libdir}/%{name}/modules/Sql.pmod/pgsql_util.pmod
%{_libdir}/%{name}/modules/Sql.pmod/pgsqls.pike
%{_libdir}/%{name}/modules/Sql.pmod/rsql.pike
%{_libdir}/%{name}/modules/Sql.pmod/sql_array_result.pike
%{_libdir}/%{name}/modules/Sql.pmod/sql_object_result.pike
%{_libdir}/%{name}/modules/Sql.pmod/sql_result.pike
%{_libdir}/%{name}/modules/Sql.pmod/sql_util.pmod
%{_libdir}/%{name}/modules/Sql.pmod/sybase.pike
%{_libdir}/%{name}/modules/Sql.pmod/tds.pike
%{_libdir}/%{name}/modules/Standards.pmod
%{_libdir}/%{name}/modules/Stdio.pmod/FakeFile.pike
%{_libdir}/%{name}/modules/Stdio.pmod/Readline.pike
%{_libdir}/%{name}/modules/Stdio.pmod/Terminfo.pmod
%{_libdir}/%{name}/modules/Stdio.pmod/module.pmod
%{_libdir}/%{name}/modules/String.pmod/Elite.pmod
%{_libdir}/%{name}/modules/String.pmod/HTML.pmod
%{_libdir}/%{name}/modules/String.pmod/module.pmod
%{_libdir}/%{name}/modules/System.pmod
%{_libdir}/%{name}/modules/Thread.pmod
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/CExtractor.pmod
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/DocParser.pmod
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/MirarDocParser.pike
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/PikeExtractor.pmod
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/PikeObjects.pmod
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/PikeParser.pike
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/ProcessXML.pmod
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/debug.h
%{_libdir}/%{name}/modules/Tools.pmod/AutoDoc.pmod/module.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Hilfe.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Install.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/Copyright.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/License.pmod/GPL.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/License.pmod/LGPL.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/License.pmod/MPL.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/License.pmod/gpl.txt
%{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/License.pmod/lgpl.txt
%{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/License.pmod/module.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Legal.pmod/License.pmod/mpl.txt
%{_libdir}/%{name}/modules/Tools.pmod/MasterHelp.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Monger.pmod/MongerDeveloper.pike
%{_libdir}/%{name}/modules/Tools.pmod/Monger.pmod/MongerUser.pike
%{_libdir}/%{name}/modules/Tools.pmod/Monger.pmod/module.pmod
%{_libdir}/%{name}/modules/Tools.pmod/PEM.pmod
%{_libdir}/%{name}/modules/Tools.pmod/PV.pike
%{_libdir}/%{name}/modules/Tools.pmod/Shoot.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Standalone.pmod
%{_libdir}/%{name}/modules/Tools.pmod/Testsuite.pmod
%{_libdir}/%{name}/modules/Tools.pmod/X509.pmod
%{_libdir}/%{name}/modules/Tools.pmod/sed.pmod
%{_libdir}/%{name}/modules/Unicode.so
%{_libdir}/%{name}/modules/Web.pmod
%{_libdir}/%{name}/modules/Val.pmod
%{_libdir}/%{name}/modules/Yabu.pmod/module.pmod
%{_libdir}/%{name}/modules/Yp.pmod
%{_libdir}/%{name}/modules/_ADT.so
%{_libdir}/%{name}/modules/_Charset.so
%{_libdir}/%{name}/modules/_Ffmpeg.so
%{_libdir}/%{name}/modules/_PGsql.so
%{_libdir}/%{name}/modules/_Protocols_DNS_SD.so
%{_libdir}/%{name}/modules/_Roxen.so
%{_libdir}/%{name}/modules/___Gz.so
%{_libdir}/%{name}/modules/___Java.so
%{_libdir}/%{name}/modules/___MIME.so
%{_libdir}/%{name}/modules/___Math.so
%{_libdir}/%{name}/modules/___Oracle.so
%{_libdir}/%{name}/modules/___Regexp.so
%{_libdir}/%{name}/modules/___Yp.so
%{_libdir}/%{name}/modules/__builtin.pmod
%{_libdir}/%{name}/modules/__builtin_dirnode.pmod
%{_libdir}/%{name}/modules/spider.so
%{_libdir}/%{name}/modules/sybase.so
%{_libdir}/%{name}/modules/_WhiteFish.so
%{_mandir}/man1/pike.1*

%files bzip2
%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/Bz2.so

%files devel
%{_includedir}/%{name}

#%files doc
#%doc refdoc/modref
#%doc refdoc/traditional_manual

%files gdbm
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/Cache.pmod
%dir %{_libdir}/%{name}/modules/Cache.pmod/Storage.pmod
%{_libdir}/%{name}/modules/Cache.pmod/Storage.pmod/Gdbm.pike
%{_libdir}/%{name}/modules/Gdbm.so

#%files gl
#%dir %{_libdir}/%{name}/modules
#%{_libdir}/%{name}/modules/GL.so

%files gtk2
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/GLUE.pmod
%dir %{_libdir}/%{name}/modules/GLUE.pmod/Driver.pmod
%{_libdir}/%{name}/modules/GLUE.pmod/Driver.pmod/GTK.pike
%{_libdir}/%{name}/modules/GTK.pmod
%{_libdir}/%{name}/modules/GTK2.pmod
%{_libdir}/%{name}/modules/GTKSupport.pmod
%{_libdir}/%{name}/modules/___GTK.so
%{_libdir}/%{name}/modules/___GTK2.so

%files image
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/Protocols.pmod
%dir %{_libdir}/%{name}/modules/Protocols.pmod/X.pmod
%dir %{_libdir}/%{name}/modules/_Image.pmod
%{_libdir}/%{name}/modules/Image.so
%{_libdir}/%{name}/modules/Protocols.pmod/X.pmod/XImage.pmod
%{_libdir}/%{name}/modules/_Image.pmod/Dims.pmod
%{_libdir}/%{name}/modules/_Image.pmod/Fonts.pmod
%{_libdir}/%{name}/modules/_Image.pmod/module.pmod
%{_libdir}/%{name}/modules/_Image_DWG.pmod
%{_libdir}/%{name}/modules/_Image_FreeType.so
%{_libdir}/%{name}/modules/_Image_GIF.so
%{_libdir}/%{name}/modules/_Image_JPEG.pmod
%{_libdir}/%{name}/modules/____Image_JPEG.so
%{_libdir}/%{name}/modules/_Image_PS.pmod
%{_libdir}/%{name}/modules/_Image_PSD.pmod
%{_libdir}/%{name}/modules/____Image_TIFF.so
%{_libdir}/%{name}/modules/_Image_TIFF.pmod
%{_libdir}/%{name}/modules/_Image_TTF.so
%{_libdir}/%{name}/modules/_Image_XCF.pmod
%{_libdir}/%{name}/modules/_Image_XFace.so
%{_libdir}/%{name}/modules/_Image_XPM.pmod

%files mysql
%dir %{_libdir}/%{name}/7.4
%dir %{_libdir}/%{name}/7.4/include
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/Cache.pmod
%dir %{_libdir}/%{name}/modules/Cache.pmod/Storage.pmod
%dir %{_libdir}/%{name}/modules/Sql.pmod
%{_libdir}/%{name}/7.4/include/mysql.h
%{_libdir}/%{name}/modules/Cache.pmod/Storage.pmod/MySQL.pike
%{_libdir}/%{name}/modules/Mysql.so
%{_libdir}/%{name}/modules/Sql.pmod/mysql.pike
%{_libdir}/%{name}/modules/Sql.pmod/mysql_result.pike
%{_libdir}/%{name}/modules/Sql.pmod/mysqls.pike
%{_libdir}/%{name}/modules/Sql.pmod/mysqls_result.pike

%files odbc
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/Sql.pmod
%{_libdir}/%{name}/modules/Odbc.so
%{_libdir}/%{name}/modules/Sql.pmod/odbc.pike
%{_libdir}/%{name}/modules/Sql.pmod/odbc_result.pike
%{_libdir}/%{name}/modules/Sql.pmod/dsn.pike
%{_libdir}/%{name}/modules/Sql.pmod/dsn_result.pike

%files pcre
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/modules/_Regexp_PCRE.pmod
%{_libdir}/%{name}/modules/____Regexp_PCRE.so

#%files pdf

#%files perl

%files postgres
%dir %{_libdir}/%{name}/7.4
%dir %{_libdir}/%{name}/7.4/include
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/Sql.pmod
%{_libdir}/%{name}/7.4/include/postgres.h
%{_libdir}/%{name}/modules/Postgres.so
%{_libdir}/%{name}/modules/Sql.pmod/postgres.pike
%{_libdir}/%{name}/modules/Sql.pmod/postgres_result.pike

%files sqlite
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/Sql.pmod
%{_libdir}/%{name}/modules/SQLite.so
%{_libdir}/%{name}/modules/Sql.pmod/sqlite.pike

%files sane
%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/SANE.so

%files sdl
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/GLUE.pmod
%dir %{_libdir}/%{name}/modules/GLUE.pmod/Driver.pmod
%{_libdir}/%{name}/modules/GLUE.pmod/Driver.pmod/SDL.pike
%{_libdir}/%{name}/modules/SDL.so

%files svg
%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/_Image_SVG.so

%files gssapi
%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/GSSAPI.so

%files fuse
%{_libdir}/%{name}/modules/Fuse.pmod
%{_libdir}/%{name}/modules/___Fuse.so

%files search
%{_libdir}/%{name}/modules/Search.pmod

%files zxid
%{_libdir}/%{name}/modules/ZXID.pmod
%{_libdir}/%{name}/modules/___ZXID.so

%changelog
* Wed Jan 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 7.8.866
- Rebuild for Fedora
* Fri Jun 29 2012 oleksii.prudkyi.pike@gmail.com
- update to 7.8.686
* Sun May 13 2012 oleksii.prudkyi.pike@gmail.com
-  try to hide error about RCS under SLE11
* Sun May 13 2012 oleksii.prudkyi.pike@gmail.com
- avoid problems with machine-code at sles > 10 and openSUSE > 11.4
* Sun May 13 2012 oleksii.prudkyi.pike@gmail.com
-  try to enable CentOS
* Sat May  5 2012 oleksii.prudkyi.pike@gmail.com
- support of x86_64 in rpmlint
* Sat May  5 2012 oleksii.prudkyi.pike@gmail.com
- switch to 7.8.680
* Fri May  4 2012 oleksii.prudkyi.pike@gmail.com
- removed fdupes from buildrequires
* Fri May  4 2012 oleksii.prudkyi.pike@gmail.com
- hide some warnings from rpmlint
* Fri May  4 2012 oleksii.prudkyi.pike@gmail.com
-  updated to pike 7.8.352
