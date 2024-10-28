%undefine _debugsource_packages
%global _name anic

Summary: Faster than C, Safer than Java, Simpler than *sh
Name: anilang
Version: 0.74
Release: 3.1
License: GPLv3
Group: Development/Language
Source: %{_name}-%{version}.tar.gz
URL: https://code.google.com/p/anic/

%description
anic is the reference implementation compiler for the experimental,
high-performance, implicitly parallel, deadlock-free general-purpose
dataflow programming language ANI.

%prep
%setup -q -n %{_name}-%{version}
sed -i -e 's|VERSION_STRING|"0.74"|g' -e 's|VERSION_YEAR|"2010"|g' src/driver.h
sed -i 's|bool retVal = (in|bool retVal = bool(in|' src/lexer.cpp
sed -i 's|-Wall|-Wall -fpermissive|' Makefile
sed -i 's|gcc|gcc -Wl,--allow-multiple-definition|' bld/hyacc/makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{_name} $RPM_BUILD_ROOT%{_bindir}/%{_name}
install -Dm644 man/%{_name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{_name}.1

%files
%{_bindir}/%{_name}
%{_mandir}/man1/%{_name}.1.*

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.74
- Rebuilt for Fedora
