Summary: Password management program
Name: pwman
Version: 0.4.5
Release: 7.1
Group: Development/Libraries
Source: https://heanet.dl.sourceforge.net/sourceforge/pwman/%{name}-%{version}.tar.gz
URL: https://pwman.sourceforge.net/
License: GPL
BuildRequires: ncurses-devel libxml2-devel

%description
PWman is a text-based application for securely storing and managing passwords,
using a gpg encrypted xml file, based on the ui design of abook.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
autoreconf -fi
%configure --with-ncurses=%{_usr} --with-libxml2=%{_usr} --disable-rpath

%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%makeinstall

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%files
%{_bindir}/convert_pwdb
%{_bindir}/pwdb2csv
%{_bindir}/pwman
%{_mandir}/man1/pwman.1.*

%changelog
* Tue Aug 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.5
- Rebuilt for Fedora
* Sat Jan 20 2007 - judas_iscariote@shorewall.net
- update to 0.3.5 
