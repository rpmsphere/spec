Name: pyboids
Summary: Python implemenation of the boids flocking (herding, schooling, swarming) simulation
Version: 0.3.0
Release: 5.1
Group: X11/Amusements
License: GPL
URL: http://www.pobox.com/~taw/pyboids
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}-1.tar.gz
BuildArch: noarch
Requires: tkinter

%description
pyBoids simulates the flocking behavior of animals found in nature.
This nifty program was written in order to learn Python. Some nice features
include multhreading operation, GUI programming, self-organizing systems, etc.
It can always be approved and I gladly accept feedback.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
install -m644 %{name}_main.py taw_*.py %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec python %{name}_main.py
EOF

%files
%doc %{name}_CHANGES %{name}_README *.asc
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Apr 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuild for Fedora
