Name: brightness-controller
Summary: Brightness Controller
Version: 2.4
Release: 1
Group: Converted/extras
License: GPLv3
URL: https://github.com/lordamit/Brightness
Source0: Brightness-%{version}.tar.gz
BuildArch: noarch
Requires: python3-pyside2

%description
Brightness Controller is the only GUI application for Linux that allows you to
control brightness of your primary and secondary display from the same place.

%prep
%setup -q -n Brightness-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
cd %{_datadir}/%{name}
exec python3 init.py
EOF
chmod +x %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Brightness
Comment=Brightness Controller
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
EOF

mkdir -p %{buildroot}%{_datadir}/%{name}
cd brightness-controller-linux/brightness_controller_linux
cp -a * %{buildroot}%{_datadir}/%{name}
install -Dm644 icons/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg 

sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora
