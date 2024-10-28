Summary: Battery level indicator for the GNOME panel
Name:    batterymon
Version: 1.2.4
Release: 2.1
License: LGPLv2+
Group:   Applications/System
URL:     https://code.google.com/p/batterymon
Source0: %{name}-%{version}.tar.gz
Requires: notify-python
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: python2-devel
BuildRequires: python2-distutils-extra
BuildArch: noarch

%description
This package contains a simple battery level indicator applet for GNOME.
It can be useful for scenarios which do not have GNOME Power Manager installed
for some reason.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT
%find_lang %{name}

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files -f %{name}.lang
%{python2_sitelib}/*
%{_datadir}/batterymon
%{_bindir}/batterymon

%changelog
* Fri Oct 18 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.4
- Rebuilt for Fedora
* Tue Jan 26 2010 Sayamindu Dasgupta <sayamindu@laptop.org>
- Initial packaging.
