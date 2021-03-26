Summary: Stroke exercise in Flash
Name: flash-stroke_exercise
Version: 100.3.1
Release: 1
License: freeware
Group: Applications/Internet
Source0: http://163.22.168.6/%7Enirc010/tpet/stroke/download/stroke-KH-100-3-1.zip
URL: http://163.22.168.6/~nirc010/tpet/stroke/stroke-KH-100-3-1/
Requires: oxzilla, flash-plugin
BuildArch: noarch

%description
Stroke exercise in Flash.
Material with KH-100-3-1

%description -l zh_TW
教育部有一個【常用標準字體筆順學習網】，透過這個網站，我們可以自己輸入想要學習的國字，
然後跟著動畫一起學習那個字的寫法，如果點選「筆順練習」，甚至可以利用滑鼠在字上面寫，
筆順錯了，電腦會提醒我們重寫。

%prep
%setup -q -n stroke-KH-100-3-1

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp * $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Flash Stroke Exercise
Comment=Stroke Exercise in Flash
Categories=Application;Education;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/tpet_300.jpg
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 920x640 index.htm
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Thu Sep 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> 100.3.1
- Initial build
