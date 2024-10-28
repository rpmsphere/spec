%undefine _debugsource_packages
Name: nts
Summary: Note taking simplified
Version: 74
Release: 1
License: GPL
Group: Applications/Editors
Source0: %{name}-%{version}.tar.gz
URL: https://www.duke.edu/~dgraham/NTS/
BuildArch: noarch
Requires: python2-wxpython

%description
nts provides a simple, intuitive format for using plain text files
to store notes, a command line interface for viewing notes in a variety
of convenient ways and a cross-platform, wx(python)-based GUI for creating
and modifying notes as well as viewing them. Displayed items can be grouped
by path or tag and can be filtered in various ways.

%prep
%setup -q
sed -i -e '15,269s/d_encoding/encoding/' -e '/Press enter to continue/d' nts/ntsRC.py

%build
python2 setup.py build

%install
%__rm -rf %{buildroot}
python2 setup.py install --root $RPM_BUILD_ROOT --prefix /usr

mv %{buildroot}%{_bindir}/n.py %{buildroot}%{_bindir}/nts
rm -f %{buildroot}%{_bindir}/n.pyw

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=NTS
Comment=%{summary}
Icon=%{python2_sitelib}/%{name}/NTS_128.png
Exec=%{name} w
Terminal=false
Type=Application
Categories=Application;Utility;Editor;
StartupNotify=false
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc README PKG-INFO
%attr(755,root,root) %{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Mar 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 74
- Rebuilt for Fedora
