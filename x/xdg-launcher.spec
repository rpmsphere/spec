%undefine _debugsource_packages
Summary: XDG Launcher Panel
Name: xdg-launcher
Version: 0.0.4
Release: 4.1
License: GPLv2
Group: Desktop/User Interface
Source: https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}_%{version}.tar.gz
URL: https://launchpad.net/xdg-launcher
BuildArch: noarch
BuildRequires: python3-devel
Requires: pygtk2, python-argparse, python-gmenu

%description
An X11 desktop panel that contains launchers for items in a given XDG Menu.
The goal is to provide a light-weight panel for launching a subset of
application defined by XDG menus.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 xdglauncher.py $RPM_BUILD_ROOT%{python3_sitelib}/xdglauncher.py

sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}%{_bindir}/%{name}

%files
%doc GPL-2
%{_bindir}/*
%{python3_sitelib}/*.py*
%{python3_sitelib}/__pycache__/*

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.4
- Rebuilt for Fedora
