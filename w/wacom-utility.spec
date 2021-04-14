Name: wacom-utility
Summary: Allows advanced controls and configuration options
Version: 1.21
Release: 4.1
Group: Applications/System
License: GPL
URL: https://launchpad.net/~hughescih/+archive/ppa/+packages
Source0: https://launchpadlibrarian.net/66164559/%{name}_%{version}-3.tar.gz
BuildArch: noarch
Requires: pygtk2-libglade

%description
For a wacom tablet through an easy to use utility. This can allow you to:
- Configure pressure curves
- Set shortcut keys to pad buttons
- Works with the new HAL hotplugging system

%prep
%setup -q -n %{name}

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a images *.py *.txt *.glade %{buildroot}%{_datadir}/%{name}
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec python wacom_utility.py
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.21
- Rebuilt for Fedora
