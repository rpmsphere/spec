%define _name splashscreenmanager

Summary: Splash Screen Manager
Name: splash-screen-manager
Version: 1.2
Release: 6.1
Source0: https://s5.histats.com/stats/r.php?715549&100&14419&urlr=&zorin-os.webs.com/%{_name}_%{version}_i386.deb
License: GPLv3
Group: Applications/System
URL: https://zorin-os.webs.com/splashscreenmanager.htm
BuildArch: noarch
Requires: gnome-python2-gnome

%description
Splash Screen Manager makes it easy to change, install and remove Plymouth splash screen themes.

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
mkdir -p $RPM_BUILD_ROOT
tar xf data.tar.gz -C $RPM_BUILD_ROOT
sed -i 's|/lib/|/usr/share/|' $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -i 's|gksudo ||' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{_name}

%changelog
* Fri Jul 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
