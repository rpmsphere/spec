Name:		oxmanual
Version:	1.0
Release:	8
Summary:	oxzilla document editor.
Group:		Applications/Editors
License:	Commercial
URL:		http://www.ossii.com.tw/
Source0:	%{name}.tar.gz
Source1:	%{name}.png
Requires:	oxzilla, sqlite
Buildarch:	noarch

%description
oxzilla document editor. Made by pure htm and javascript(jQuery,phpjs,and OSSII custom methods).

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
# 安裝
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a css db images js manual.htm $RPM_BUILD_ROOT%{_datadir}/%{name}/

# 安裝小圖示
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# 安裝 desktop 檔
%__mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=OX Manual
Name[zh_TW]=OX 程式手冊
Comment=Programm Manual written in OXZilla
Comment[zh_TW]=利用 OXZilla 編寫的程式手冊
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Development;
EOF

# 安裝執行檔
%__mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd /usr/share/oxmanual
oxzilla manual.htm
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Mon Mar 08 2010 Kami <kami@ossii.com.tw> 1.0-8.ossii
- OXZilla plugins replaced.

* Tue Feb 23 2010 Kami <kami@ossii.com.tw> 1.0-7.ossii
- Change Requires.

* Thu Feb 05 2010 Kami <kami@ossii.com.tw> 1.0-6.ossii
- Change content of .desktop file.

* Thu Feb 04 2010 Kami <kami@ossii.com.tw> 1.0-5.ossii
- SQLite, MySQL, Zip Functions' comment finished

* Wed Feb 03 2010 Kami <kami@ossii.com.tw> 1.0-4.ossii
- PHP Functions' comment finished

* Fri Jan 29 2010 Kami <kami@ossii.com.tw> 1.0-3.ossii
- FileSystem Functions' comment finished
- Function List Box sort by name

* Fri Jan 22 2010 Kami <kami@ossii.com.tw> 1.0-2.ossii
- String Functions' comment finished
- Function List sort by name

* Wed Dec 02 2009 Feather Mountain <john@ossii.com.tw> 1.0-1.ossii
- Build for OSSII
