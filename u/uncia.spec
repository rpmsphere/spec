Name:				 uncia
Version:			 1.0
Release:			 4.1
Summary:			 Text File Manipulation Command Line Tool
# http://uncia.sourceforge.net/uncia-%{version}.tar.gz
Source:			 uncia-%{version}.tar.bz2
Patch1:			 uncia-fix_headers.patch
URL:				 http://uncia.sourceforge.net/
Group:			 Productivity/Text/Utilities
License:			 GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:	 bison flex boost-devel zlib-devel curl-devel
BuildRequires:	 gcc-c++ libstdc++-devel
BuildRequires:	 gcc make glibc-devel
BuildRequires:	 autoconf automake libtool

%description
uncia can do zillions of different things to text files. The subtlety lies in
uncia's implementation: each different filter that uncia(1) implements is a
separate class, and all of these classes can be chained together, much like
commands being piped together on the command line. The implementation uses the
C++ <iostream> interface, allowing the various classes to be re-used in other
C++ programs. This is still the Unix philosophy, but it's implemented as a
library at the <iostream> level, rather than a directory full of executables. 

%prep
%setup -q
%patch1
sed -i 's|return deeper.get(c);|return bool(deeper.get(c));|' libuncia/input/filter.h

%build
%configure
# -j breaks build
%__make

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/uncia
%doc %{_mandir}/man1/uncia.1.*
%doc %{_mandir}/man1/uncia_license.1.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
