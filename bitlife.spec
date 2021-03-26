Name: bitlife
Summary: A Bitwise Stack of Life Games
Version: 0.9.6.svn24
Release: 4.1
Group: Amusements/Graphics
License: GPL
URL: http://bitlife.sourceforge.net/
Source0: %{name}-code-24.zip
Requires: numpy, pygame
BuildArch: noarch

%description
It's a simple idea: implement Conway's Game of Life using boolean logic
operations (and, or, not, xor); do so by blits, thus running a Life game
in every bitplane in parallel.

%prep
%setup -q -n %{name}-code-24

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp python/* %{buildroot}%{_datadir}/%{name}
cat > %{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec python2 pygame3d.py
EOF
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
cd xscreensaver/hacks
install -Dm644 %{name}.man %{buildroot}%{_mandir}/man6/%{name}.6

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%doc README.*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.*

%changelog
* Wed Jan 04 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.6.svn24
- Rebuild for Fedora
