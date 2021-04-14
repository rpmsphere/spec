%undefine _debugsource_packages

Name: conkycolors
Summary: An easier way to configure Conky
Version: 9.0
Release: 6.1
License: GPL
Source: conky_colors-%{version}.zip
Group: User Interface/X

%description
This conky script by helmuthdu supports multilanguages.

%prep
%setup -q -n conky_colors

%build
sed -i 's|-Wall|-Wall -Wl,--allow-multiple-definition|' Makefile
make

%install
%make_install
mv %{buildroot}%{_bindir}/conky-colors %{buildroot}%{_bindir}/conkycolors
ln -fs ../share/conkycolors/bin/conkyTask %{buildroot}%{_bindir}/ct

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/scripts/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README ChangeLog AUTHORS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/fonts/*

%changelog
* Wed Apr 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 9.0
- Rebuilt for Fedora
