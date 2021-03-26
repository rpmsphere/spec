Name: jobp2012
Summary: Go playing computer program
Version: 0.4
Release: 2.1
Group: Amusements/Games
License: GPLv2
URL: https://code.google.com/p/jobp2012/
Source0: https://jobp2012.googlecode.com/files/Final.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: python

%description
This program is meant to play the ancient Chinese strategy game of Go
utilizing deterministic algorithms. The program calculates proper moves
based on recognition of "shapes" on the board. Machine learning and the
Monte Carlo method are possible additions to the program.

Created by Justin Oh and Ben Parks for their Senior Thesis Project for
Manlius Pebble Hill School.

%prep
%setup -q

%build
cat > %{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec python humvscomp.py
EOF

%install
install -d %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -m644 *.py *.cray %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Fri Nov 01 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
