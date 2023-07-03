Summary: An enhanced calculator for X11
Name: ycalc
Version: 1.09.1
Release: 4.1
Source:  https://www.sourcefiles.org/Productivity_Tools/Calculators/%{name}-%{version}.tar.gz
License: GPL
Group: X11/Utilities
BuildRequires: libX11-devel

%description
Ycalc is an enhanced calculator for X. It supports many more 
operations and has 99 memories. Especially nice is its binary 
mode.

%prep 
%setup -q
sed -i '/extern struct keydef calckd/d' Calc.h
sed -i '1i extern struct keydef *calckd;' main.c

%build
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Jun 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.09.1
- Rebuilt for Fedora
