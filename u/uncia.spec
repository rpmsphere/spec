Name:		uncia
Version:	1.3
Release:	1
Summary:	Text File Manipulation Command Line Tool
Source:		http://uncia.sourceforge.net/uncia-%{version}.tar.gz
Patch1:		uncia-fix_headers.patch
URL:		http://uncia.sourceforge.net/
Group:		Productivity/Text/Utilities
License:	GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:	bison flex boost-devel zlib-devel curl-devel
BuildRequires:	gcc-c++ libstdc++-devel
BuildRequires:	glibc-devel automake libtool
BuildRequires:  libexplain-devel

%description
uncia can do zillions of different things to text files. The subtlety lies in
uncia's implementation: each different filter that uncia(1) implements is a
separate class, and all of these classes can be chained together, much like
commands being piped together on the command line. The implementation uses the
C++ <iostream> interface, allowing the various classes to be re-used in other
C++ programs. This is still the Unix philosophy, but it's implemented as a
library at the <iostream> level, rather than a directory full of executables. 

%package devel
Summary:        Development files for uncia
License:        GNU General Public License version 2 or later (GPL v2 or later)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files for the package uncia.

%prep
%setup -q
#patch1
sed -i 's|return deeper.get(c);|return bool(deeper.get(c));|' libuncia/input/filter.h
sed -i 's|bison -y|byacc|' configure etc/yacc.cook

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
%{_mandir}/man1/*
%{_includedir}/libuncia
%{_libdir}/libuncia.so.*

%files devel
%{_libdir}/libuncia.a
%{_libdir}/libuncia.so
%{_libdir}/pkgconfig/uncia.pc

%changelog
* Sun Sep 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
