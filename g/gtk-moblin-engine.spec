Summary: GTK Moblin engine
Name: gtk-moblin-engine
Version: 1.1.1
Release: 7.1
License: GPL
Group: User Interface/Desktops
Source0: https://launchpadlibrarian.net/48138297/moblin-gtk-engine_%{version}.orig.tar.gz
Source1: Moblin-index.theme
URL: https://launchpad.net/ubuntu/+source/moblin-gtk-engine/
BuildRequires: gtk2-devel
Requires: moblin-icon-theme
Requires: moblin-cursor-theme

%description
This package contains gtk2 engines for moblin.

%prep
%setup -q -n moblin-gtk-engine-%{version}
cp %{SOURCE1} data/index.theme

%build
autoreconf -ifv
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING.LIB README NEWS ChangeLog
%{_datadir}/themes/Moblin-Netbook
%{_libdir}/gtk-2.0/*/engines/*.*

%changelog
* Wed Sep 07 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
* Thu Jun 10 2010 awafaa@opensuse.org
- Initial import for openSUSE version 1.0.0
