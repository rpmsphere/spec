Name: metacity-themes
Version: 1.0.12
Release: 2.1
Summary: Themes for the Gtk2 metacity window manager
License: GPL
Group: Graphical desktop/MATE
Source0: https://http.debian.net/debian/pool/main/m/metacity-themes/metacity-themes_%{version}.tar.gz
Buildarch: noarch

%description
This collection of themes for the metacity window manager has been carefully
compiled from a number of sources. Each one is publically available under a
license which complies with the Debian free software guidelines, most commonly
the GPL license. The themes have been individually checked to ensure that they
are all of high quality: they have a consistent design; include high quality
graphics; handle all types of window.

%prep
%setup -q
rm nodoka-theme-gnome-0.3.90.tar.gz

%build
for i in *.tar.*
do
tar xf $i
done
rm -f *.tar.*

%install
install -d $RPM_BUILD_ROOT%_datadir/doc/%{name}
install -m644 debian/changelog debian/GPL-1 debian/README.Debian $RPM_BUILD_ROOT%_datadir/doc/%{name}
rm -rf debian
install -d $RPM_BUILD_ROOT%_datadir/themes
cp -a * $RPM_BUILD_ROOT%_datadir/themes

%files
%_datadir/doc/%{name}
%_datadir/themes/*

%changelog
* Thu Aug 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.12
- Rebuilt for Fedora
