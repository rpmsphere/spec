%define xerces_ver 2.5.0
%define m1_xercesc_file %{_includedir}/xercesc/util/XercesVersion.hpp

Name: amberfish
Summary:  Text retrieval software
Version: 2.3.0
Release: 1
Vendor: Etymon Systems Inc.
Packager: Dimitri Tarassenko <mitka@mitka.us>
License: GPL
Group: Applications/Text
URL: https://github.com/nassibnassar/amberfish
Source0: %{name}-%{version}.tar.gz
#Source1: pdftex.map
BuildRequires: %{m1_xercesc_file}
BuildRequires: tetex texinfo sed automake gcc gcc-c++ make binutils libstdc++-devel
Requires: libstdc++
BuildRequires: xerces-c-devel >= %xerces_ver
Requires: xerces-c >= %xerces_ver

%description 
Amberfish is general purpose text retrieval and indexing software. 
Its distinguishing features are indexing/search of semi-structured 
text (i.e. both free text and multiply nested fields), built-in 
support for XML documents using the Xerces-C library, structured 
queries allowing generalized field/tag paths, hierarchical result 
sets (XML only), automatic searching across multiple databases 
(allowing modular indexing), efficient indexing, and relatively 
low memory requirements during indexing (and the ability to index 
documents larger than available memory). Other features include 
Boolean queries, right truncation, phrase searching, relevance 
ranking, support for multiple documents per file, incremental 
indexing, and easy integration with other UNIX tools. 

Please note that you need Xerces-c installed on your server for
Amberfish to work. On a RedHat/Fedora you can download the latest
source from http://xml.apache.org/xerces-c/download.cgi and follow
the steps at http://xml.apache.org/xerces-c/build-misc.html#RPMLinux

On SuSE, install Xerces-c (note capital X) package using yast or rpm.

%prep
%setup -q
#cp %{SOURCE1} ./doc/pdftex.map
#%patch0 -p1 -b .bindir

%build 
autoreconf -ifv ||:
%configure
sed -i 's|-Wall|-fPIC|' src/Makefile
make

%install 
rm -fr %{buildroot}
make DESTDIR=%{buildroot} install

%clean 
rm -fr %{buildroot}

%files 
%{_bindir}/* 
%{_mandir}/man1/* 
%doc doc/html/* doc/amberfish.pdf doc/amberfish.texi doc/version.texi NOTES README COPYING INSTALL CREDITS
	
%changelog 
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.0
- Rebuilt for Fedora
* Mon Mar 27 2006 Nassib Nassar <nassar@etymon.com> 1.6.2-1
- added "make html" and "make pdf" as suggested by Antoine Brenner
* Mon Jun 21 2004 Dimitri Tarassenko <mitka@mitka.us> 1.5.9-1
- pdftex.map added to resolve font mapping when pdf is built
- tetex is added as build requirement
- some cleanup done to prevent empty pre/postun scripts in RPM
* Wed Jun 16 2004 Joao Cruz <jalrnc@yahoo.com> 1.5.9-0
- upgrade to 1.5.9
- added mandrake flavor
* Tue Jun 15 2004 Dimitri Tarassenko <mitka@mitka.us>
- patch removed, added HTML docs and CREDITS file, install notes
* Mon Jun 14 2004 Dimitri Tarassenko <mitka@mitka.us>
- first 2 versions
