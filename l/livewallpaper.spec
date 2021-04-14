%undefine _debugsource_packages

Name:           livewallpaper
Version:        0.4.1
#Version:        0.5.0
Release:        1
Summary:        Animated wallpaper
License:        GPLv3
Group:          User Interface/X
URL:            https://launchpad.net/livewallpaper
Source0:        https://launchpad.net/livewallpaper/0.5/%{version}/+download/livewallpaper-%{version}.tar.gz
BuildRequires:  cmake, gettext, intltool, gtk-doc, libappstream-glib
BuildRequires:  pkgconfig(gobject-introspection-1.0), pkgconfig(libpeas-1.0), pkgconfig(glew), pkgconfig(upower-glib)
#BuildRequires:  xcftools

%description
Livewallpaper provides animated wallpaper for your desktop.

%package devel
Requires:      %{name} = %{version}-%{release}
Summary:       LiveWallpaper development files
Provides:      livewallpaper-devel

%description devel
Header files for Livewallpaper, required to develop new plugins or to
build existing plugins.
Developer documentation for the LiveWallpaper API

%package ui
BuildRequires: pkgconfig(gtk+-3.0), vala
Requires:      %{name} = %{version}-%{release}
Summary:       User interfaces to configure LiveWallpaper
Provides:      livewallpaper-config, livewallpaper-indicator

%description ui
This package contains an application to set up Livewallpaper, and an indicator
to access quickly to basic options of LiveWallpaper and that embeds a shortcut
to the configuration program.

%prep
%setup -q
sed -i 's|-Wall|-Wall -fPIC -lX11|' CMakeLists.txt

%build
%cmake . -DENABLE_OPTIMIZATION=ON -DENABLE_DOC=OFF
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
ln -fs liblivewallpaper-core.so.%{version} %{buildroot}%{_libdir}/liblivewallpaper-core.so
%find_lang %{name}

%files -f %{name}.lang
/etc/xdg/autostart/livewallpaper-autostart.desktop
%{_bindir}/livewallpaper
#%{_bindir}/livewallpaper-autostart
#%{_bindir}/lw-desktop-icons.default.sh
%{_libdir}/livewallpaper/*
%{_libdir}/liblivewallpaper-core.so.*
%{_datadir}/applications/livewallpaper.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/*/scalable/apps/*
%{_datadir}/livewallpaper/*

%files devel
/usr/include/livewallpaper/*
%{_libdir}/liblivewallpaper-core.so
%{_libdir}/pkgconfig/livewallpaper.pc
%{_datadir}/cmake/Modules/*
#%{_bindir}/lw-generate-schema
#%{_datadir}/gtk-doc/html/

%files ui
/etc/xdg/autostart/livewallpaper-indicator.desktop
#%{_datadir}/appdata/livewallpaper-config.appdata.xml
%{_bindir}/livewallpaper-config
%{_bindir}/livewallpaper-indicator
%{_datadir}/applications/livewallpaper-config.desktop
%{_datadir}/icons/*/scalable/status/livewallpaper-indicator.svg

%changelog
* Thu Jan 02 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
* Sat Dec 20 2014 Aurélien Rivière <aurelien.riv@gmail.com> 0.5.0-1
- Maybe Livewallpaper will join COPR soon ? :)
