Summary:	OXStore Soft-Keyboard upon oxzilla 
Name:		oxkeyboard
Version:	0.1
Release:	1
License:	Commerical
Group:		Applications/File
URL:		http://www.opdesktop.org.tw/
Source0:	%{name}-%{version}.tar.gz
Requires:	oxzilla-jscollections oxzilla >= 0.1.2
BuildArch:	noarch

%description
A keyboard for OXStore running on oxzilla.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT datadir=%{_datadir} %{__make} install
%__install -Dm 644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__mkdir_p} %{buildroot}%{_bindir}

# Install auto-launched file
%{__cat} > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s800x160 -p --notitle %{_datadir}/%{name}/index.html
EOF

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=OXKeyboard
Name[zh_TW]=OXStore 小鍵盤
Comment=Keyboard written in OXZilla
Comment[zh_TW]=利用 OXZilla 編寫的小鍵盤
Icon=%{name}.png
Exec=%{_bindir}/%{name}
Terminal=false
Type=Application
Categories=Application;System;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Jan 4 2011 Wind Yan <yc.yan@ossii.com.tw> 0.1-1
- Build for first time.
