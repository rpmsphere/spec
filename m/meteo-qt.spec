%define aname meteo_qt

Name:           meteo-qt
Version:        1.0.0
Release:        1
Group:          Graphical desktop/Other
Summary:        Weather status system tray application
License:        GPLv3
URL:            https://github.com/dglent/meteo-qt
Source0:        https://github.com/dglent/meteo-qt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-qt5-devel
BuildRequires:  python3
BuildRequires:  qt5-qttools
BuildRequires:  qt5-linguist
BuildRequires:  ImageMagick
Requires:       python3-qt5
Requires:       python3-sip
Requires:       python3-urllib3
Requires:       python3-lxml

%description
A Qt system tray application for the weather status
Weather data from: http://openweathermap.org/

%prep
%setup -q
sed -i 's|lrelease|lrelease-qt5|' setup.py

%build
%py3_build

%install
%py3_install
%__mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32}/apps
convert -scale 16x16 meteo_qt/images/meteo-qt.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/meteo-qt.png
convert -scale 32x32 meteo_qt/images/meteo-qt.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/meteo-qt.png

%files
%doc TODO CHANGELOG README.md
%exclude %_defaultdocdir/%{name}/LICENSE
#{_datadir}/%{aname}/images/
%{_bindir}/%{name}
%{_datadir}/icons/%{name}.png
%{python3_sitelib}/%{aname}-%{version}-py%python3_version.egg-info
%{python3_sitelib}/%{aname}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/meteo-qt.png
%{_datadir}/meteo_qt/translations/

%changelog
* Thu Mar 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
* Thu Mar 09 2017 dglent <dglent> 0.9.5-1.mga6
+ Revision: 1090520
- New version 0.9.5
* Sun Jul 03 2016 dglent <dglent> 0.9.4-1.mga6
+ Revision: 1038408
- Version 0.9.4
* Mon Jun 27 2016 akien <akien> 0.9.3-3.mga6
+ Revision: 1037870
- Rebuild in core/release
* Sat Jun 25 2016 akien <akien> 0.9.3-2.mga6
+ Revision: 1037542
- Rebuild for python-sip 4.18
* Thu May 19 2016 dglent <dglent> 0.9.3-1.mga6
+ Revision: 1016936
- Version 0.9.3
* Sun May 15 2016 dglent <dglent> 0.9.2-1.mga6
+ Revision: 1015739
- Version 0.9.2
* Tue Apr 19 2016 dglent <dglent> 0.9.1-1.mga6
+ Revision: 1003556
- Version 0.9.1
* Sun Apr 17 2016 dglent <dglent> 0.9.0-1.mga6
+ Revision: 1003228
- Version 0.9.0
* Sat Dec 19 2015 dglent <dglent> 0.8.8-1.mga6
+ Revision: 912079
- Version 0.8.8
* Thu Dec 03 2015 dglent <dglent> 0.8.7-1.mga6
+ Revision: 907816
- Version 0.8.7
* Mon Nov 30 2015 dglent <dglent> 0.8.6-1.mga6
+ Revision: 907271
- Version 0.8.6
* Sun Nov 29 2015 dglent <dglent> 0.8.5-1.mga6
+ Revision: 907041
- Version 0.8.5
* Wed Nov 04 2015 dglent <dglent> 0.8.4-1.mga6
+ Revision: 897817
- Version 0.8.4
* Sat Oct 31 2015 dglent <dglent> 0.8.3-1.mga6
+ Revision: 896842
- Version 0.8.3
* Sun Oct 25 2015 dglent <dglent> 0.8.2-1.mga6
+ Revision: 895177
- Verison 0.8.2
- Use new python macros
- Version 0.8.1
* Thu Oct 08 2015 daviddavid <daviddavid> 0.8.0-2.mga6
+ Revision: 887839
- rebuild for python 3.5
- use new python macros
* Sun Aug 23 2015 dglent <dglent> 0.8.0-1.mga6
+ Revision: 868208
- Version 0.8.0
* Sat Aug 08 2015 dglent <dglent> 0.7.1-1.mga6
+ Revision: 861644
- Version 0.7.1
* Sat Jul 04 2015 dglent <dglent> 0.7.0-1.mga6
+ Revision: 849866
- Version 0.7.0
* Mon May 11 2015 dglent <dglent> 0.6.0-1.mga5
+ Revision: 821718
- Version 0.6.0
* Mon Feb 09 2015 dglent <dglent> 0.5.0-1.mga5
+ Revision: 814230
- Version 0.5.0
* Sun Jan 25 2015 dglent <dglent> 0.4.3-1.mga5
+ Revision: 812172
- Version 0.4.3
* Sun Nov 30 2014 dglent <dglent> 0.3.4-1.mga5
+ Revision: 800018
- Version 0.3.4
- Version 0.3.3
- Version 0.3.1
- Version 0.2.0 (Qt5)
* Sat Oct 25 2014 dglent <dglent> 0.1.0-1.mga5
+ Revision: 793157
- imported package meteo-qt
