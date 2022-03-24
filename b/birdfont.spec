%undefine _debugsource_packages

Name:           birdfont
Version:        2.30.0
Release:        1
Summary:        Font editor
License:        GPLv3+
Group:          Multimedia/Graphics/Vector Editors 
URL:            http://birdfont.org/
Source0:        http://birdfont.org/releases/%{name}-%{version}.tar.xz
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  python3
BuildRequires:  vala
BuildRequires:  webkitgtk4-devel
BuildRequires:  libnotify-devel
BuildRequires:  libgee-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  sqlite-devel
BuildRequires:  xmlbird-devel
Requires:       unicode-ucd

%description
BirdFont is a free font editor that lets you create vector graphics and export
TTF, EOT & SVG fonts.

%prep
%setup -q

%build
./configure -p/usr
./scripts/linux_build.py -p/usr

%install
./install.py -d%{?buildroot} -l/%{_lib} -n/share/man/man1
chmod +x %{?buildroot}%{_libdir}/libbird*.*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libbird*
%{_bindir}/birdfont*
%{_datadir}/applications/birdfont.desktop
%{_datadir}/birdfont
%{_datadir}/locale/*/LC_MESSAGES/*
%{_mandir}/man1/birdfont*.1.*
%{_datadir}/icons/hicolor/*/apps/birdfont.png
%{_datadir}/metainfo/birdfont.appdata.xml
%{_datadir}/mime/packages/birdfont.xml

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.30.0
- Rebuilt for Fedora
