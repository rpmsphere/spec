%undefine _debugsource_packages
%define up_name DisplayCAL

Name:           displaycal
Version:        3.9.11
Release:        1
Summary:        A graphical user interface for the Argyll CMS display calibration utilities
Group:          Graphics/Utilities
License:        GPLv3
URL:            https://displaycal.net/
Source0:        https://sourceforge.net/projects/dispcalgui/files/release/%{version}/%{up_name}-%{version}.tar.gz
Patch0:         displaycal-3.5.1.0-udev-dir.patch
BuildRequires:  python3-setuptools
#BuildRequires: wxGTK
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
#Requires:      wxGTK
Requires:       argyllcms
Requires:       python3-setuptools
Requires:       pygobject3
Requires:       numpy
Provides:       %{up_name} = %{version}-%{release}
Provides:       dispcalGUI = %{version}-%{release}
Obsoletes:      dispcalGUI < 1.2.7.0-10

%description
DisplayCAL (formerly known as dispcalGUI) is a graphical user interface for
the display calibration and profiling tools of Argyll CMS, an open source
color management system.

%files
%doc %{_docdir}/%{up_name}-%{version}/LICENSE.txt
%doc %{_docdir}/%{up_name}-%{version}/CHANGES*.html
%doc %{_docdir}/%{up_name}-%{version}/README*.html
%doc %{_docdir}/%{up_name}-%{version}/screenshots
%doc %{_docdir}/%{up_name}-%{version}/theme
#{_udevrulesdir}/*-Argyll.rules
%{_bindir}/*
%{_datadir}/%{up_name}/
%{_datadir}/icons/hicolor/*/*
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/net.displaycal.%{up_name}.appdata.xml
%{_sysconfdir}/xdg/autostart/z-displaycal-apply-profiles.desktop
%{python3_sitearch}/%{up_name}/
%{python3_sitearch}/%{up_name}-%{version}-py%{python3_version}.egg-info
%{_mandir}/man1/*

%prep
%setup -q -n %{up_name}-%{version}
#autopatch -p1
touch misc/debian.rules

%build
%py3_build

%install
%py3_install -- --no-compile --prefix=%{_prefix} --skip-postinstall

%changelog
* Sun Nov 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.9.11
- Rebuilt for Fedora
* Mon Apr 30 2018 daviddavid <daviddavid> 3.5.3.0-1.mga7
  (not released yet)
+ Revision: 1223902
- new version: 3.5.3.0
* Sat Apr 07 2018 daviddavid <daviddavid> 3.5.2.0-1.mga7
+ Revision: 1215879
- new version: 3.5.2.0
* Fri Mar 23 2018 daviddavid <daviddavid> 3.5.1.0-1.mga7
+ Revision: 1211431
- new version: 3.5.1.0
- rename and rediff udev-dir patch
* Mon Feb 26 2018 daviddavid <daviddavid> 3.5.0.0-1.mga7
+ Revision: 1205245
- new version: 3.5.0.0
* Thu Jan 04 2018 daviddavid <daviddavid> 3.4.0.0-1.mga7
+ Revision: 1190081
- new version: 3.4.0.0
* Thu Nov 09 2017 daviddavid <daviddavid> 3.3.5.0-1.mga7
+ Revision: 1176692
- new version: 3.3.5.0
* Sat Sep 23 2017 daviddavid <daviddavid> 3.3.4.1-1.mga7
+ Revision: 1157787
- new version: 3.3.4.1
* Sat Sep 02 2017 daviddavid <daviddavid> 3.3.3.0-1.mga7
+ Revision: 1150723
- new version: 3.3.3.0
* Sun Jul 02 2017 daviddavid <daviddavid> 3.3.2.0-1.mga6
+ Revision: 1108913
- new version: 3.3.2.0
* Sun Jan 15 2017 daviddavid <daviddavid> 3.2.3.0-1.mga6
+ Revision: 1081884
- new version: 3.2.3.0
* Sun Dec 11 2016 daviddavid <daviddavid> 3.2.1.0-1.mga6
+ Revision: 1074203
- new version: 3.2.1.0
* Sun Oct 30 2016 daviddavid <daviddavid> 3.1.7.3-1.mga6
+ Revision: 1064156
- new version: 3.1.7.3
* Fri Oct 14 2016 daviddavid <daviddavid> 3.1.7.0-1.mga6
+ Revision: 1060737
- new version: 3.1.7.0
* Sun Aug 28 2016 daviddavid <daviddavid> 3.1.6.0-1.mga6
+ Revision: 1049349
- new version: 3.1.6.0
* Sat Aug 20 2016 daviddavid <daviddavid> 3.1.5.0-1.mga6
+ Revision: 1047143
- new version: 3.1.5.0
* Sun Jul 24 2016 daviddavid <daviddavid> 3.1.4.0-1.mga6
+ Revision: 1043512
- new version: 3.1.4.0
* Tue May 10 2016 daviddavid <daviddavid> 3.1.3.1-1.mga6
+ Revision: 1012317
- new version: 3.1.3.1
* Mon Feb 22 2016 daviddavid <daviddavid> 3.1.0.0-1.mga6
+ Revision: 976005
- new version: 3.1.0.0 (fixes mga#17803)
- new upstream URL and Source URL
- rename and rediff udev-dir patch
- use new python macros
- requires python-numpy
- obsoletes/provides old upstream name on dispcalGUI
- update files list
- move to new upstream name on displaycal
* Fri Feb 05 2016 umeabot <umeabot> 1.2.7.0-9.mga6
+ Revision: 938821
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 1.2.7.0-8.mga5
+ Revision: 744682
- Second Mageia 5 Mass Rebuild
* Sat Sep 27 2014 tv <tv> 1.2.7.0-7.mga5
+ Revision: 726130
- rebuild for missing pythoneggs deps
* Tue Sep 16 2014 umeabot <umeabot> 1.2.7.0-6.mga5
+ Revision: 678756
- Mageia 5 Mass Rebuild
+ ovitters <ovitters>
- add gobject-introspection BR for typelib auto BR
* Sat May 31 2014 pterjan <pterjan> 1.2.7.0-5.mga5
+ Revision: 628160
- Rebuild for new Python
* Sat Nov 02 2013 fwang <fwang> 1.2.7.0-4.mga4
+ Revision: 548862
- add requires on python-gi
* Tue Oct 22 2013 umeabot <umeabot> 1.2.7.0-3.mga4
+ Revision: 542551
- Mageia 4 Mass Rebuild
* Mon Oct 14 2013 pterjan <pterjan> 1.2.7.0-2.mga4
+ Revision: 497727
- Rebuild to add different pythonegg provides for python 2 and 3
* Wed Jul 31 2013 fwang <fwang> 1.2.7.0-1.mga4
+ Revision: 461407
- update file list
- new version 1.2.7.0
* Sun Feb 10 2013 neoclust <neoclust> 0.8.9.3-1.mga3
+ Revision: 397779
- imported package dispcalGUI
