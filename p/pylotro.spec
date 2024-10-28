%undefine _debugsource_packages
%define _name PyLotRO

Name:       pylotro
Version:    0.1.15
Release:    8.1
Summary:    Lord of the Rings Online Launcher
Group:      Game/Role Playing
License:    GPLv3
URL:        https://www.lotrolinux.com
Source0:    %{_name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires: python2-devel
Requires: python-4Suite-XML
Requires: python-qt4

%description
PyLotRO is a game launcher for Lord of the Rings Online.  It can also be used
to launch Dungeons & Dragons Online.

%prep
%setup -q -n %{_name}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.15
- Rebuilt for Fedora
