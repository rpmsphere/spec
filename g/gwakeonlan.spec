%define oname gWakeOnLan

Name:           gwakeonlan
Version:        0.6.3
Release:        7.1
Summary:        A GTK+ utility to awake machines using the Wake on LAN
Group:          Networking/Other
License:        GPLv2
URL:            https://www.muflone.com/gwakeonlan/
Source0:        https://codeload.github.com/muflone/gwakeonlan/tar.gz/%{version}#/%{name}-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  python2-pyxdg
BuildArch:      noarch
Requires:       pygtk2

%description
gWakeOnLan is a GTK+ utility to awake turned off machines using
the Wake On LAN feature.
It allows to turn on machines in the local network or throught
Internet using a destination host and a specified UDP port number.
The machines to turn on need to be shut off with the Wake on LAN
magic packet enabled.
If WOL is available on your computer, do not forget to enable it
on the BIOS.

%prep
%setup -q

%build

%install
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot}
#%{__install} -D -m644 data/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_mandir}/man1/%{name}.1*
%{python2_sitelib}/*

%changelog
* Tue Dec 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.3
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 0.5.1-8.mga5
+ Revision: 748764
- Second Mageia 5 Mass Rebuild
* Sat Sep 27 2014 tv <tv> 0.5.1-7.mga5
+ Revision: 726456
- rebuild for missing pythoneggs deps
* Tue Sep 16 2014 umeabot <umeabot> 0.5.1-6.mga5
+ Revision: 680058
- Mageia 5 Mass Rebuild
* Sat May 31 2014 pterjan <pterjan> 0.5.1-5.mga5
+ Revision: 628247
- Rebuild for new Python
* Tue Oct 22 2013 umeabot <umeabot> 0.5.1-4.mga4
+ Revision: 542683
- Mageia 4 Mass Rebuild
* Mon Oct 14 2013 pterjan <pterjan> 0.5.1-3.mga4
+ Revision: 497771
- Rebuild to add different pythonegg provides for python 2 and 3
* Sat Jan 12 2013 umeabot <umeabot> 0.5.1-2.mga3
+ Revision: 353057
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Mar 06 2012 dams <dams> 0.5.1-1.mga2
+ Revision: 220221
- imported package gwakeonlan
