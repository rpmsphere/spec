Name:            xml-coreutils
Version:         0.8a
Release:         3.1
Summary:         Command Line Tools for Reading and Writing XML Files
# http://prdownloads.sourceforge.net/xml-coreutils/xml-coreutils-%{version}.tar.gz
Source:          xml-coreutils-%{version}.tar.bz2
Patch1:          xml-coreutils-fix_buffer_overflow.patch
URL:             http://xml-coreutils.sourceforge.net/
Group:           Productivity/Text/Utilities
License:         GNU General Public License version 3 (GPL v3)
BuildRequires:   bison flex ncurses-devel slang-devel
BuildRequires:   expat-devel
BuildRequires:   gcc make glibc-devel
BuildRequires:   autoconf automake libtool

%description
The xml-coreutils are a set of command line tools for reading and writing XML
files in a Unix/POSIX type shell environment. The tools try to be as close as
possible to the traditional text processing tools... cat, echo, sed, etc.

%prep
%setup -q
%patch1
sed -i 's|slang.h||' configure
sed -i 's|slang.h|slang/slang.h|' src/lessui.c src/lessdisp.c src/lessrend.c

%build
%configure
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install
%__rm -rf "$RPM_BUILD_ROOT%{_datadir}/xml-coreutils"
%__rm doc/Makefile*

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc ChangeLog COPYING NEWS README SFX THANKS
%doc doc/*
%{_bindir}/xml-*                                                      
%doc %{_mandir}/man1/xml-*.1.*
%doc %{_mandir}/man7/xml-coreutils.7.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8a
- Rebuilt for Fedora

* Mon May 17 2010 pascal.bleser@opensuse.org
- initial package
