%undefine _debugsource_packages

Summary:        Touchpad service for KDE 4
Name:           synaptiks
Version:        0.8.1
Release:        12.4
Source0:        https://pypi.python.org/packages/source/s/synaptiks/synaptiks-%{version}.tar.bz2
License:        BSD
Group:          System/Configuration/Hardware
URL:            https://synaptiks.lunaryorn.de/
BuildRequires:  python2
BuildRequires:  python2-setuptools
BuildRequires:  kdelibs-devel
BuildRequires:  qca2 udisks2
Requires:       pykde4
Requires:       python-qt4
Requires:       python-pyudev
Requires:       libXi
Requires:       libXtst
Requires:       dbus-python
BuildArch:      noarch

%description
Synaptiks is a touchpad management service for KDE. It provides a simple
configuration interface and can automatically switch off your touchpad
on keyboard activity or if mouse devices are plugged.

%prep
%setup -q

%build
python2 setup.py build

%install
%__rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT --single-version-externally-managed

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

install -d %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/synaptiks.svgz %{buildroot}%{_datadir}/pixmaps/synaptiks.svg.gz
gunzip %{buildroot}%{_datadir}/pixmaps/synaptiks.svg.gz

%files
%{_sysconfdir}/xdg/autostart/*.desktop
%{_bindir}/*
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-%{version}*.egg-info
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/kde4/services/*.desktop
%{_datadir}/autostart/*.desktop
%{_datadir}/applications/kde4/*.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/kde4/apps/%{name}

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.1
- Rebuilt for Fedora
* Mon Feb 13 2012 fwang <fwang> 0.8.1-1.mga2
+ Revision: 208397
- new version 0.8.1
* Sat Oct 08 2011 fwang <fwang> 0.8.0-1.mga2
+ Revision: 152908
- br meinproc4
- br setup tools
- update file list for python based package
- new version 0.8.0
* Wed Mar 09 2011 mikala <mikala> 0.4.0-3.mga1
+ Revision: 66740
- Clean Spec
- Use synaptiks from kde playground
 (switched from hal to udev, & add some minors fix)
* Fri Feb 25 2011 ahmad <ahmad> 0.4.0-2.mga1
+ Revision: 59228
- imported package synaptiks
