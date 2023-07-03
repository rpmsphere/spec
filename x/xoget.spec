Name:		xoget
Summary:	XO-Get with PyGTK User Interface
Version:	1.2.5
Release:	1
URL:		https://wiki.laptop.org/go/Xo-get
License:	GPL
BuildArch:	noarch
Source0:	https://xo-get.olpc.at/xoget.xo
Source1:	https://xo-get.olpc.at/xo-get.py
Group:		System Environment/Base
Requires:	pygtk2, sugar-toolkit

%description
XO-Get is a very simple package-installer/manager, used for installing,
testing and removing activities for / on the xo-laptop and emulators.
We are currently developing a Graphical User Interface with PyGTK.

%prep
%setup -q -n xoget.activity

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -f %{SOURCE1} xoget.py
%__sed -i 's/sqlite3/sqlite/' xoget.py
%__sed -i 's/700/600/' xogetgtk.glade
%__cp -a * %{buildroot}%{_datadir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# xoget script

cd /usr/share/%{name}
python2 xogetgtk.py
EOF

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=XO-Get
Name[zh_TW]=管理 XO 檔
Comment=xo-get with PyGTK User Interface
Comment[zh_TW]=XO 檔下載與安裝圖形介面
Exec=xoget
Icon=/usr/share/xoget/activity/activity-xoget.svg
Terminal=false
Categories=Application;System;
EOF

sed -i -e 's|/usr/bin/python$|/usr/bin/python2|' -e 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%clean
%__rm -rf %{buildroot}

%post
#/usr/bin/update-mime-database /usr/share/mime &> /dev/null

%postun
#/usr/bin/update-mime-database /usr/share/mime &> /dev/null

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.5
- Rebuilt for Fedora
