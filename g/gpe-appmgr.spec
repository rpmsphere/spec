%undefine _debugsource_packages

Name: gpe-appmgr
License: GPL
Group: User Interface/Desktops
Summary: An application launcher and desktop
Version: 2.8
Release: 7.3
Source: https://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.gz
URL: https://gpe.linuxtogo.org/projects/GPE-appmgr.shtml
BuildRequires: libpng-devel
BuildRequires: libgpewidget-devel, libgpelaunch-devel, libxsettings-client-devel
Patch0: gpe-appmgr-2.8-cairo.patch

%description
GPE-Appmgr uses freedesktop.org-style desktop files like known
from Gnome and KDE. It allows to start-up applications and offers
a kind of start-menu.

%prep
%setup -q
%patch 0 -p1
sed -i '/render.h/d' *.c
sed -i 's/-lXsettings-client/-Wl,--allow-multiple-definition -lX11 -lXsettings-client/' Makefile

%build
%__make

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc COPYING README todo
%{_bindir}/%{name}
%{_datadir}/pixmaps/*

%changelog
* Wed Apr 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.8
- Rebuilt for Fedora
