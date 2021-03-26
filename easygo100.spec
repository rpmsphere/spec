Summary: IQChinese go100
Name: easygo100
Version: 3.0demo
Release: 1%{?dist}.bin
License: Commercial
Group: Applications/Education
Source: EasyGo_L2_L3_demo.tar.gz
Source1: go100-icons.zip
URL: http://www.iqchinese.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: gnash
BuildArch: noarch

%description
Educational tutor for learning Chinese:
- Familiar with Chinese sounds & intonations using chants and karaoke.
- Pratical conversation and sentence pattern.
- Word and phrase building via listening & recognition typing practices.

%prep
%setup -q -n "Easy Go_L2_L3_demo"

%build
%install
rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -R Menu.swf images Sound sw %{buildroot}%{_datadir}/%{name}
unzip %{SOURCE1} iqchinese.png -d %{buildroot}%{_datadir}/%{name}

%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
gnash Menu.swf
EOF

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Easy Go 100
Comment=IQChinese go100
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/iqchinese.png
Categories=Application;Education;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Feb 14 2008 Wei-Lun Chao <bluebat@member.fsf.org> 3.0demo-1.ossii
- Initial package for M6(CentOS5)
