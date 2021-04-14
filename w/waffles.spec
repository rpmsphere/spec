%undefine _debugsource_packages

Name: waffles
Summary: A collection of command-line tools for researchers in machine learning, data mining
Version: 1.0.0
Release: 1
Group: Development/Tools
URL: https://github.com/mikegashler/waffles
Source0: https://github.com/mikegashler/waffles/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
License: LGPL, Public Domain
BuildRequires: ncurses-devel, libpng-devel

%description
Waffles seeks to be the world's most comprehensive collection of command-line
tools for machine learning and data mining. Our native tools have minimal
dependencies (no interpreter, VM, or runtime environment is necessary),
and build cross-platform. If you have a useful data mining tool that meets
these criteria, we want it in Waffles.

%package        devel
Summary:        Development files for Waffles
Group:          Development/Libraries/C and C++
Requires:      %{name}

%description    devel
Development files for Waffles.

%prep
%setup -q
#sed -i '1i #include <unistd.h>' src/GClasses/GDirList.cpp
sed -i -e 's|; false; fi|; true; fi|' -e 's|@sudo -u $${SUDO_USER} ||' -e 's|/usr/local/lib|%{buildroot}%{_libdir}|' -e 's|/usr/local|%{buildroot}/usr|' -e 's|/etc|%{buildroot}/etc|' src/Makefile src/*/Makefile
sed -i 's|-Werror||' src/*/Makefile

%build
cd src
make opt

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cd src
make install

%files
%doc README.txt
%{_bindir}/%{name}*

%files devel
%{_includedir}/GClasses
%{_libdir}/lib*.a

%changelog
* Thu Jan 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
