Name:		timeset-gui
Version:	2.2.1
Release:	2.1
Summary:	A GUI for managing system date and time
License:	GPLv3
Group:		System Environment/Base
URL:		https://github.com/aadityabagga/timeset-gui
Source0:	https://github.com/aadityabagga/timeset-gui/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	beesu
Requires:       python-gobject
Requires:       ntpdate
Requires:       timedatectl

%description
Its a graphical interface written in python for managing system date and time.

%prep
%setup -q
sed -i -e 's|share/icons|share/pixmaps|' -e '/makefile/d' makefile

%build
make

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/applications/*.desktop
%{_datadir}/doc/%{name}

%changelog
* Wed Sep 27 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.1
- Rebuilt for Fedora
