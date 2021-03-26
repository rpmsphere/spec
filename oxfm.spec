Summary:	A lightweight filemanager built-on OXZilla.
Name:		oxfm
Version:	0.0.1
Release:	7
License:	Commerical
Group:		Applications/File
URL:		http://www.opdesktop.org.tw/
Source0:	%{name}-%{version}.tar.gz
Requires:	oxzilla-gio, oxzilla-jscollections
BuildArch:	noarch

%description
OXFM is A filemanager built on OXZilla enviornment.
This tool can help OXIM user to manage files on filesystem, 
just like some common filemanager programs.

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
oxzilla %{_datadir}/%{name}/index.html
EOF

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=OXFileManager
Name[zh_TW]=OXZilla 檔案總管
Comment=
Comment[zh_TW]=
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
* Tue Mar 16 2010 Wind <yc.yan@ossii.com.tw> 0.0.1-3
- fix some bugs.

* Tue Mar 16 2010 Wind <yc.yan@ossii.com.tw> 0.0.1-3
- Auto-launched file added.

* Fri Mar 5 2010 Wind Yan <yc.yan@ossii.com.tw> 0.0.1-2
- New abbility added.

* Thu Mar 4 2010 Wind Yan <yc.yan@ossii.com.tw> 0.0.1-1
- Build for first time.
