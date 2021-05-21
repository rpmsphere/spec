Name:           app-launcher
Version:        0.2
Release:        3
Summary:        The Moblin Application Launcher (app-launcher) 
Group:          Development/Languages
License:        LGPLv2+
URL:            http://www.moblin.org/projects/application-launcher
Source0:        %{name}.tar.bz2
Source1:        %{name}.png
Source2:	%{name}-po.tar.gz
Source3:	directories.deny
Patch0:		%{name}-0.2-main.c.patch
Patch1:		%{name}-0.2-fullscreen.patch
Patch2:	        %{name}-0.3-main.c-directories.deny.patch
BuildRequires:  cairo-devel >= 0.8, libwnck-devel
BuildRequires:  clutter-devel >= 0.8, clutter-box2d-devel, clutter-cairo-devel 
BuildRequires:	genesis
Requires:       libwnck 
Requires:       genesis 
Requires:       clutter >= 0.8 
Requires:       clutter-cairo >= 0.8
Requires:       clutter-box2d >= 0.8

%description
The Moblin Application Launcher (app-launcher) provides 
a platform mechanism for the user to launch applications.
Leveraging existing standards from freedesktop.org relating 
to application categories (currently parsed via Genesis),
the Moblin Application Launcher is able to present a view 
of the applications available using predefined application categories.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p1
%patch2 -p0
sed -i -e 's|clutter-0.8|clutter-1.0|' -e 's|clutter-box2d-0.8|clutter-box2d-0.10|' Makefile

%build
export CFLAGS="-I/usr/include/clutter-1.0 -I/usr/include/glib-2.0 -I%{_libdir}/glib-2.0/include"
make 

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp background.jpg %{buildroot}%{_datadir}/%{name}/
%__mkdir_p %{buildroot}%{_bindir}
%__cp app-launcher %{buildroot}%{_bindir}/

# deny.conf
%__cp %{SOURCE3} %{buildroot}%{_datadir}/%{name}/
# icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=app-launcher
Name[zh_TW]=應用程式執行介面
Comment=app-launcher The Moblin Application Launcher
Comment[zh_TW]=像手機一樣的應用程式執行介面
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=System;Internationalization;
EOF

#i18n
tar xvzf %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/zh_TW/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN/LC_MESSAGES
msgfmt zh_TW.po -o $RPM_BUILD_ROOT%{_datadir}/locale/zh_TW/LC_MESSAGES/%{name}.mo
msgfmt zh_CN.po -o $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.mo


%clean
%__rm -rf %{buildroot}

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_bindir}/%{name}/
%{_datadir}/%{name}/background.jpg
%{_datadir}/%{name}/directories.deny
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Jan 22 2009 Feather Mountain <john@ossii.com.tw> 0.2-3.ossii
- Add directories.deny for category list.

* Mon Jan 12 2009 Wind <yc.yan@ossii.com.tw> 0.2-2
- Modify the fullscreen bug.

* Fri Dec 05 2008 Feather Mountain <john@ossii.com.tw> 0.2-1.ossii
- Regit newer version
- Rebuild for M6(OSSII)
- Add i18n for menu

* Thu Sep 11 2008 Feather Mountain <john@ossii.com.tw> 0.1-1
- Add patch for icons and change default font to 文鼎PL新宋
- Add version for buildrequires and requires

* Wed Sep 10 2008 Feather Mountain <john@ossii.com.tw> 0.1-1
- Build for OSSII
