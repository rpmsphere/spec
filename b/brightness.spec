Name: brightness
Summary: Brightness Controller
Version: 1.0.1
Release: 3.1
Group: Converted/extras
License: GPLv3
URL: https://github.com/lordamit/Brightness
Source0: Brightness-develop.zip
BuildArch: noarch
Requires: python-pyside

%description
Brightness Controller is the only GUI application for Linux that allows you to
control brightness of your primary and secondary display from the same place.

%prep
%setup -q -n Brightness-develop

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
cd %{_datadir}/%{name}
exec python2 init.py
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
cp -a src %{buildroot}%{_datadir}/%{name}
install -Dm644 img/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg 

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuild for Fedora
