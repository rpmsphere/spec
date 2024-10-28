Name:           sleeptimer
Version:        0.64
Release:        2.1
License:        GPL
Group:          System/Configuration/Other
URL:            https://www.pclinuxos.com/
Source:         sleeptimer-%{version}.tar.xz
Summary:        To shutdown the computer automatically
Summary(de):    Zum automatischen Herunterfahren des Computers
BuildArch:      noarch

%description
Enter the minutes to wait for shutdown.

%description -l de
Geben Sie die Minuten ein zum abschalten.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -d -m 0755 %buildroot%_datadir/pixmaps
install -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/%{name}_64.png %buildroot%_datadir/pixmaps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=sleeptimer
Name[de]=Sleeptimer
Comment=automated system shutdown
Comment[de]=Automatisches Herunterfahren des Rechners 
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Infos;System;Monitor;
EOF

# i18n - Internationalization - Internationalisierung
mkdir -p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES
msgfmt -o %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo $RPM_BUILD_DIR/%{name}-%{version}/languages/%{name}-de_DE.po

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%doc README COPYING CHANGELOG

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.64
- Rebuilt for Fedora
* Fri May 08 2015 daniel <meisssw01 at gmail.com> 0.64-1free2015
- 0.64
- bugfix
* Fri Jun 27 2014 daniel <meisssw01 at gmail.com> 0.63-1free2014
- 0.63
+ add Hipernate
* Fri Jan 17 2014 daniel <meisssw01 at gmail.com> 0.62-1free2014
- 0.62
+ rewrite settings dialog
+ add function to choose shutdown or pm-suspend
* Tue Jun 04 2013 ghostbunny <hmhaase at pclinuxosusers dot de> 0.61-1pclos2013
- 0.61
* Sun Mar 11 2012 Neal <nealbrks0 at gmail dot com> 0.60-1pclos2012
- process
* Sat Mar 10 2012 leiche <meisssw01 at gmail.com> 0.60-1pclos2012
- fix bug by first start
- add variable to set your Distri name
* Thu Feb 23 2012 leiche <meisssw01 at gmail.com> 0.59-1pclos2012
- 0.59
- change progressbar (idea embi)
- add display last entry (idea embi)
- change input methode to scale, for a quick handle
  (idea Manfred) 
* Mon Dec 19 2011 leiche <meisssw01 at gmail.com> 0.58-1pclos2011
- add left click menu
* Wed Dec 07 2011 leiche <meisssw01 at gmail.com> 0.57-1pclos2011
- fix some bugs
* Thu Nov 17 2011 leiche <meisssw01 at gmail.com> 0.56-1pclos2011
- fix close bug 
- fix description
* Fri Sep 30 2011 leiche <meisssw01 at gmail.com> 0.55-1leiche2011
- add dialog to activate, or deactivate check for 
  running jobs
* Fri Sep 16 2011 leiche <meisssw01 at gmail.com> 0.54-1leiche2011
- add dialog to check for running players or encoders
* Wed Jul 13 2011 leiche <meisssw01 at gmail.com> 0.53-1leiche2011
- fix display in systray again, by using new version of yad
- add about window
* Sun Jul 10 2011 leiche <meisssw01 at gmail.com> 0.52-1pclos2011
- fix icon display in systray, by move zenity to yad
* Tue Mar 29 2011 leiche <meisssw01 at aol.com> 0.51-1pclos2011
- Progress bar changed from 10 to 20 seconds
- fix notification message, now will only display time.
- add requires for new glibc
* Sun Sep 26 2010 leiche <meisssw01 at aol.com> 0.50-1pclos2010
- change notification message 
* Sun Sep 12 2010 leiche <meisssw01 at aol.com> 0.45-2pclos2010
- fix notification message 
* Mon Sep 06 2010 leiche <meisssw01 at aol.com> 0.45-1pclos2010
- add notification for systray
* Tue Aug 03 2010 Texstar <texstar at gmail.com> 0.30-2pclos2010
- add X-MandrivaLinux-System-Monitoring to menu
 * Tue Aug 03 2010 leiche <meisssw01 at aol.com> 0.30-1pclos2010
- add german language
- fix specfile description
* Tue Aug 03 2010 leiche <meisssw01 at aol.com> 0.25-1pclos2010
- add warndialog 
- change input methode from seconds to minutes
 * Mon Aug 02 2010 leiche <meisssw01 at aol.com> 0.01pclos2010
- first build for pclinuxos
