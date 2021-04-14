Name: marquee-plugins
License: GPL
Group: User Interface/Desktops
Summary: Plugins for the Hildon marquee
Version: 0.22
Release: 1
Source: http://moblin.org/build-results/projects/marquee-plugins/lpia/marquee-plugins_%{version}.tar.gz
URL: http://www.moblin.org/projects/projects_ui.php
BuildRequires: gtk2-devel, hildon-desktop-devel
Requires: gtk2, hildon-desktop

%description
This package contains the marquee plugins for hildon, such as
the application menu, the clock and the close button.

%prep
%setup -q -n marquee-plugins
sed -i 's/-Werror / /' configure.ac

%build
./autogen.sh
%configure
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}

%files
%doc README AUTHORS ChangeLog COPYING
%{_libdir}/hildon-desktop/*
%{_datadir}/applications/hildon-marquee

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.22
- Rebuilt for Fedora
