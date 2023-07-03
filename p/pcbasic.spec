Name: pcbasic
Summary: An emulator for GW-BASIC
Version: 2.0.6
Release: 1
Group: Development/Languages
License: GPLv3
URL: https://sourceforge.net/projects/pcbasic/
Source0: https://github.com/robhagemans/pcbasic/releases/download/v%{version}/pcbasic-%{version}.tar.gz
BuildArch: noarch
Requires: pygame
Requires: numpy
Requires: pyserial
Requires: python2-pexpect
Requires: python2-pyxdg

%description
PC-BASIC can run and convert between ASCII, bytecode and 'protected'
(encrypted) .BAS files. It implements floating-point arithmetic in the
Microsoft Binary Format (MBF) and can therefore read and write binary
data files created by GW-BASIC.

%prep
%setup -q

%build
cat > %{name}.sh <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec ./run.py
EOF

%install
install -Dm755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}

%files
%doc *.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.6
- Rebuilt for Fedora
