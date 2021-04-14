Name:           evilvte
Version:        0.5.2~pre1
Release:        5.1
License:        GPL-2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  vte-devel
BuildRequires:  pkgconfig
URL:            http://www.calno.com/evilvte/
Requires:       vte
Source0:        %{name}-%{version}.tar.gz
Source1:        evilvte.desktop
Patch0:         customization.patch
Group:          System/X11/Terminals
Summary:        VTE based, super lightweight terminal emulator

%description
Features:
 * tabs
 * tabbar autohide
 * right click to switch encoding
 * supports almost all VTE features (option list) (changelog)
 * build-time configuration

%prep
%setup -q
#patch0 -p1

%build
%{__mv} gpl-2.0.txt COPYING
%{configure} --prefix=/usr
%{__make}

%install
DESTDIR=%{buildroot} make install
%{__mkdir} -p %{buildroot}%{_datadir}/applications
%{__install} -m 644 %{S:1} %{buildroot}%{_datadir}/applications/evilvte.desktop

%files
%defattr(-,root,root)
%doc ChangeLog COPYING
%{_bindir}/evilvte
%{_bindir}/showvte
%{_datadir}/pixmaps/evilvte.*
%{_datadir}/applications/evilvte.desktop
%{_mandir}/man1/evilvte.1.gz
%{_mandir}/man1/showvte.1.gz
%{_datadir}/gnome-control-center/default-apps/evilvte.xml
%{_datadir}/icons/hicolor/*/*/evilvte.png
%{_datadir}/icons/hicolor/*/*/evilvte.svg
%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/default-apps
%dir %{_datadir}/icons/hicolor/20x20
%dir %{_datadir}/icons/hicolor/20x20/apps
%dir %{_datadir}/icons/hicolor/40x40
%dir %{_datadir}/icons/hicolor/40x40/apps

%changelog
* Sat Aug 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2~pre1
- Rebuilt for Fedora
* Wed Jul  3 2013 seiler@b1-systems.de
- changed to configuration to fit needs for a common window manager
* Wed Jul  3 2013 seiler@b1-systems.de
- initial commit (copied package from home:swyear and updated it)
