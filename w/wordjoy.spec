Name:		wordjoy
Version:	0.2.2
Release:	1
Summary:	English words memory for Linux
License:	GPL
Group:		Education
Source0:	%{name}_%{version}.tar.bz2
URL:		http://code.google.com/p/wordjoy/
BuildArch:	noarch
Requires:	pygtk2

%description
wordjoy is a Python script to help people memory english words.

%prep
%setup -q -n %{name}_%{version}

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}/src
python2 %{name}.py
EOF
%__mkdir_p %{buildroot}%{_datadir}/%{name}
cp -a glade README RELEASE sound src words %{buildroot}%{_datadir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=WordJoy
Name[zh_TW]=背單字
Name[zh_CN]=背单词
Comment=A tool for english words memory
Comment[zh_TW]=記憶英文單字的工具
Exec=wordjoy
Terminal=false
Type=Application
Categories=Application;Education;
Icon=/usr/share/wordjoy/glade/wordjoy.png
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/src/*.py

%clean
%__rm -rf %{buildroot}

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuild for Fedora
