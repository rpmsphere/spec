Summary:	A GUI setup tool for Open X Input Method Server .
Name:		oxim-setup-oxzilla
Version:	0.0.1
Release:	6
License:	MIT
Group:		System/Internationalization
URL:		http://www.opdesktop.org.tw/
Source0:	oxim-setup-oxzilla-%{version}.tar.gz
Requires:	oxzilla, oxzilla-jscollections, oxim >= 1.4.3
BuildRequires:	oxzilla-devel

%description
OXIM-SETUP-OXZILLA is A GUI interface built on OXZilla enviornment.
This tool can help OXIM user to change common settings, download/Install
Input-Method tab files, and User-Defined pharse settings.

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT %{__make} install
%__install -Dm 644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__mkdir_p} %{buildroot}%{_bindir}

# Install auto-launched file
%{__cat} > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
oxzilla --notitle %{_libdir}/oxim-setup/%{name}/index.html
EOF

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=OXIM-Setup
Name[zh_TW]=OXIM-Setup on OXZilla
Comment=
Comment[zh_TW]=
Icon=%{name}.png
Exec=%{_bindir}/oxim-setup-oxzilla
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
%{_libdir}/oxim-setup/%{name}/*
%{_libdir}/oxzilla/jsplugins/*.so
%exclude %{_libdir}/oxzilla/jsplugins/*.la
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Mar 01 2011 Wind Yan <yc.yan@ossii.com.tw> 0.0.1-6
- Adjust font-size, layout.

* Mon Feb 23 2010 Wind Yan <yc.yan@ossii.com.tw> 0.0.1-1
- Build for first time.
