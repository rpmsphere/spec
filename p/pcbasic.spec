Name: pcbasic
Summary: An emulator for GW-BASIC
Version: 1.2.14
Release: 1
Group: Development/Languages
License: GPLv3
URL: http://sourceforge.net/projects/pcbasic/
Source0: https://github.com/robhagemans/pcbasic/releases/download/v%{version}/pcbasic-v%{version}.tgz
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
%setup -q -n pcbasic-v%{version}

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
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.14
- Rebuilt for Fedora
