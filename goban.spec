%global __os_install_post %{nil}

Summary: xscreensaver hack, replays historical games of go
Name: goban
Version: 1.1
Release: 7.1
License: GPL
Group: Graphics
Source: http://draves.org/goban/goban-1.1.tar.gz
URL: http://draves.org/goban
BuildRequires: libX11-devel
Requires: xscreensaver

%description
Replays historical games of go (aka wei-chi and baduk) on the screen.
Designed to work with xscreensaver (http://www.jwz.org/xscreensaver).

%prep
%setup -q
sed -i 's|$(GNOME_DATADIR)/control-center/screensavers|$(DESTDIR)%{_datadir}/xscreensaver/config|' Makefile*
sed -i 's|$(pkgdatadir)|$(DESTDIR)$(pkgdatadir)|' Makefile*

%build
%configure
make

%install
mkdir -p %{buildroot}%{_datadir}/xscreensaver/config
%make_install

%files
%doc COPYING README* TODO
%{_bindir}/goban
%{_datadir}/goban
%{_datadir}/xscreensaver/config/goban.xml

%changelog
* Wed Mar 11 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Tue Jul 26 2005 Scott Draves <rpm@draves.org>
- Initial package
