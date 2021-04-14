%global _name PLaunch

Name:           plaunch
Version:        1.1
Release:        1
Summary:        A shortcuts management and quickly running tool
Group:          System/Internationalization
License:        GPLv2
URL:            http://code.google.com/p/plaunch/
Source0:        http://plaunch.googlecode.com/files/%{_name}_V%{version}.tgz
BuildRequires:	ImageMagick
Requires:	pygtk2 python2-xlib python2
BuildArch:      noarch

%description
You can make a shortcut run with limited keystoke. PLaunch is developed with
Python and Pygtk, and it works under Linux and Windows. 

%prep
%setup -q -n %{_name}_V%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

#Desktop
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{name}
Name[zh_TW]=工具快捷列
Comment=PLaunch is shortcuts management and quickly running tool. You can make a shortcut run with limited keystoke.
Comment[zh_TW]=工具快捷列可以方便使用者在工具列上連結使用自定常用的工具，便於管理，操作簡便。
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=System;Internationalization;
EOF

#Exec
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd %{_datadir}/%{name}
python2 StatusIcon.py
EOF

#Icon
convert data/%{_name}.ico $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Mon Dec 01 2008 Feather Mountain <john@ossii.com.tw> 1.1-1.ossii
- Build for OSSII
