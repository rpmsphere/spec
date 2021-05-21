Summary: OSSII Home screen upon oxzilla 
Name: oxhome
Version: 0.1
Release: 8
License: Commercial
Group: User Interface/Desktops
Source0: %{name}.tar.gz
Source1: %{name}.png
Requires:	oxzilla-jscollections
BuildArch:	noarch

%description
Home screen running on oxzilla.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n oxhome

%install
rm -rf $RPM_BUILD_ROOT
cd ..
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a %{name} $RPM_BUILD_ROOT%{_datadir}/${name}

%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
%{__mkdir_p} %{buildroot}%{_bindir}

# Install auto-launched file
%{__cat} > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
oxzilla %{_datadir}/%{name}/index.html --noresize
EOF

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=OX Home
Name[zh_TW]=OX 主畫面
Comment=Home screen written in OXZilla
Comment[zh_TW]=利用 OXZilla 編寫的主畫面 
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
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Fri Mar 12 2010 Wind <yc.yan@ossii.com.tw> 0.1-7
- Auto-launched file added.

* Fri Feb 5 2010 Wind <yc.yan@ossii.com.tw> 0.1-4
- Change content of .desktop file.

* Wed Jan 27 2010 Kami <kami@ossii.com.tw> 0.1-2
- Categories tag modified.

* Thu Nov 19 2009 Wind Win <yc.yan@ossii.com.tw> 0.1-1
- Building on first time.
