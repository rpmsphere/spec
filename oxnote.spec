Name:           oxnote
Version:        0.1
Release:        2
Summary:        OxNote Clinet for School Base On OxZilla.
Group:          Applications/Education
License:        Commercial
URL:            http://www.ossii.com.tw/
Source0:			%{name}.tar.gz
Source1:			%{name}.png
BuildArch:      noarch
Requires:       oxzilla >= 0.1.1-20


%description
OxNote Clinet for School Base On OxZilla.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
# 安裝
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a config data images inc oxnote.htm $RPM_BUILD_ROOT%{_datadir}/%{name}/

# 安裝小圖示
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# 安裝 desktop 檔
%__mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=OxNote
Name[zh_TW]=OxNote
Comment=OxNote Client base on OxZilla
Comment[zh_TW]=電子聯絡簿
Categories=Application;Education;
Exec=%{name}
Terminal=false
Type=Application
Hidden=false
Icon=%{name}
EOF

# 安裝執行檔
%__mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd /usr/share/oxnote
if [ ! -f /home/$USER/.config/oxnote/mydialog.xml ]; then 
	cp /usr/share/oxnote/data/mydialog.xml.sample  /home/$USER/.config/oxnote/mydialog.xml
	chmod 755 /home/$USER/.config/oxnote/mydialog.xml
fi
oxzilla -s 800x480 -r oxnote.htm
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Thu Dec 15 2010 Sean <sean@ossii.com.tw> 1.0-2.ossii
- 同步功能修改完成
- 修復家長留言檔上傳的漏字問題
- OSSII LOGO增加

* Thu Dec 09 2010 Sean <sean@ossii.com.tw> 1.0-1.ossii
- First Release 
- Resolution 800x480 for Demo use.


