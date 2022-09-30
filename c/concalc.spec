Summary:	Scientific Calculator for the Terminal
Name:		concalc
Version:	0.9.3
Release:	22.1
License:	GPL-2.0+
Group:		Applications/Engineering
URL:		http://sourceforge.net/projects/extcalc-linux/
Source0:	http://sourceforge.net/projects/extcalc-linux/files/extcalc-linux/%{version}/concalc-%{version}.tar.gz
BuildRequires:  gcc-c++, cmake

%description
Concalc is the console version of the Extcalc calculator.

%prep
%setup -q
sed -i -e 's|/usr/local|/usr|' CMakeLists.txt

%build
%cmake .
cd *-linux-build
sed -i -e 's|-O3||' -e 's|-Werror=format-security||' CMakeCache.txt CMakeFiles/concalc.dir/link.txt CMakeFiles/concalc.dir/flags.make
cd ..
%cmake_build
										
%install
rm -rf $RPM_BUILD_ROOT
#make DESTDIR=$RPM_BUILD_ROOT install
%cmake_install

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.3
- Rebuilt for Fedora
