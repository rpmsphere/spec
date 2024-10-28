Summary:        TV player
Name:           freetuxtv
Version:        0.6.8
Release:        1
License:        GPLv2+
Group:          Video
URL:            https://code.google.com/archive/p/freetuxtv/wikis/HomePage.wiki
Source0:        https://github.com/freetuxtv/freetuxtv/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  intltool
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(sqlite3)
Requires:       vlc

%description
freetuxtv is a player for Television on Internet with french Free
or SFR (ex-Neuf) Internet service providers, and a lot of WebTV in
French languages in the world (Canada, Switzerland, Belgium, etc...).

%prep
%setup -q

%build
autoreconf -fi
%configure --with-gtk=3.0
%make_build

%install
%make_install
%find_lang %{name}
rm -fr %{buildroot}%{_libdir}/*.a %{buildroot}%{_libdir}/*.la
rm -fr %{buildroot}%{_includedir}

%files -f %{name}.lang
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.8
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.6.8-3
- (10a1602) MassBuild#1257: Increase release tag
