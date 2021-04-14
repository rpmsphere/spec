Name:       conkyweather
Version:    0.3.1
Release:    7.1
Summary:    Display weather information and forecast in conky
License:    GPLv3
URL:        http://hardikmehta.wordpress.com/2009/08/04/a-script-to-display-weather-forecast-for-conkyconky-screen-shot
Source0:    %{name}-%{version}.tar.bz2
Patch1:     weather.sh.patch
Patch2:     fcConditions.xslt.patch
Patch3:     conditionsInclude.xslt.patch   
BuildArch:  noarch
Requires:   conky
Group:	    User Interface/X
Requires:   xorg-x11-font-utils
Requires:   libxslt
%define fontdir	%{_datadir}/fonts/%{name}

%description
weather.sh is a simple bash script which is supposed to be called from conky.
The script downloads weather information from www.google.com  in xml format.
The xml file is processed by different stylesheets.

Authors:
--------
	Hardik Mehta <hard.mehta@gmail.com>

%prep
%setup -q
%patch1 -p0
%patch2 -p0
%patch3 -p0
echo %{fontdir}

%build

%install
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{fontdir}
install -m 0755 weather.sh $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 0644 *.xslt $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 0644 weather.ttf $RPM_BUILD_ROOT%{fontdir}

%post
/usr/bin/mkfontdir %{fontdir}
/usr/bin/mkfontscale %{fontdir}
/usr/bin/fc-cache -f %{fontdir} 

%postun
/usr/bin/mkfontdir %{fontdir}
/usr/bin/mkfontscale %{fontdir}
/usr/bin/fc-cache -f %{fontdir} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING gpl.txt ChangeLog weatherInfo.xml
%dir %{_datadir}/%{name}
%dir %{fontdir}
%{_bindir}/conkyweather
%{_datadir}/%{name}/*
%{fontdir}/weather.ttf

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora

* Wed Aug 31 2011 Agnelo de la Crotche <agnelo@unixversal.com> 0.3.1
- fixed Google UTF-8 output 

* Wed Jun 1 2011 Agnelo de la Crotche <agnelo@unixversal.com> 0.3
- added cuurentHumidity.xslt and currentWind.xslt

* Tue May 24 2011 Agnelo de la Crotche <agnelo@unixversal.com> 0.2
- original built
- some changes applied to the original script weather.sh by Hardik Meta to match rpm package standards:
- rename weather.sh to conkyweather and put in /usr/bin
- set RUNDIR to /usr/share/conkyweather
- set weather_xml to $HOME/weatherInfo.xml instead of ${RUNDIR}/weatherInfo.xml
