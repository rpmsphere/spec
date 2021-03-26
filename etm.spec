%global debug_package %{nil}
Name: etm
Summary: Event and Task Manager
Version: 696
Release: 1
License: GPL
Group: Applications/Editors
Source0: %{name}-%{version}.tar.gz
URL: http://www.duke.edu/~dgraham/ETM/
BuildArch: noarch
Requires: python2-wxpython

%description
etm provides a simple, intuitive format for using plain text files
to store data, a command line interface for viewing stored information
in a variety of convenient ways and a cross-platform, wx(python)-based
GUI for creating and modifying items as well as viewing them.
Displayed items can be grouped by date, context, keyword or project and
can be filtered in various ways. A display of busy and free times is also
supported as is a ledger view of time spent that is suitable for client
billing. Alarms are supported for events and repetition for both events
and tasks in a powerful and flexible manner.

%prep
%setup -q
sed -i -e "63i 'Asia/Taipei'," etm/etmRC.py

%build
python2 setup.py build

%install
%__rm -rf %{buildroot}
python2 setup.py install --root $RPM_BUILD_ROOT --prefix /usr

mv %{buildroot}%{_bindir}/e.py %{buildroot}%{_bindir}/etm
rm -f %{buildroot}%{_bindir}/e.pyw

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=ETM
Comment=%{summary}
Icon=%{python2_sitelib}/%{name}/etmlogo_128x128x32.png
Exec=%{name} w
Terminal=false
Type=Application
Categories=Application;Utility;Editor;
StartupNotify=false
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
%__rm -rf %{buildroot}

%files
%doc README PKG-INFO
%attr(755,root,root) %{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Feb 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 696
- Rebuild for Fedora
