Name: bijinclock
Version: 1.1.0
Release: 1
BuildArch: noarch
Group: Applications/Internet
Summary: Clock with beautiful women photo
License: GPLv2
URL: https://github.com/adhisimon/bijinclock
Source0: %{name}-master.zip
Requires: python2 pygtk2

%description
Bijin Clock is a clock program. It display photos of beautiful women
every minute.

%prep
%setup -q -n %{name}-master

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT BINDIR=/usr/bin DATADIR=/usr/share install
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/bijinclock
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/bijinclock.png
%doc AUTHOR COPYING README

%changelog
* Tue Apr 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuild for Fedora
* Tue May 24 2011 Adhidarma Hadiwinoto <gua@adhisimon.or.id>
- Initial version
