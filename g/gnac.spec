Name:           gnac
Version:        0.2.4.1
Release:        6.1
Summary:        Easy to use audio conversion program for the Gnome desktop
Group:          Sound/Editors and Converters
License:        GPLv3
URL:            https://gnac.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/gnac/gnac/gnac-0.2.4.1/%{name}-%{version}.tar.bz2
Patch1:         gnac-0.2.4.1-nofaac.patch
Patch2:         gnac-0.2.4.1-cflags.patch
BuildRequires:  gnome-doc-utils
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  gnome-common
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-pbutils-0.10)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  pkgconfig(gstreamer-tag-0.10)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(unique-3.0)
BuildRequires:  python
Patch3: gnac-stdc11.patch

%description
Gnac is an easy to use audio conversion program for the GNOME desktop.
It is designed to be powerful but simple! It provides easy audio files
conversion between all GStreamer supported audio formats.

%prep
%setup -q
%patch 1 -p1 -b .nofaac
%patch 2 -p1 -b .cflags
%patch 3 -p1

%build
export AUTOPOINT='intltoolize --automake --copy'
./autogen.sh
%configure
make

%install
%make_install

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/%{name}/
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}
%{_datadir}/applications/gnac.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/gnome/help/%{name}/*/*
%{_datadir}/locale/*/*/%{name}.mo

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4.1
- Rebuilt for Fedora
* Sat Jan 12 2013 umeabot <umeabot> 0.2.4.1-5.mga3
+ Revision: 351925
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Dec 06 2012 cjw <cjw> 0.2.4.1-4.mga3
+ Revision: 327089
- add BuildRequires: gnome-common for gnome-autogen.sh
- patch1: use voaacenc instead of faac which we don't have
- patch2: use our cflags so debug package can be used
- add dependencies on flac and speex streamer plugins
* Wed Dec 05 2012 barjac <barjac> 0.2.4.1-3.mga3
+ Revision: 327003
- change group to new policy
- minor spec clean
* Wed Aug 01 2012 juancho <juancho> 0.2.4.1-2.mga3
+ Revision: 277214
+ rebuild (emptylog)
* Mon Jul 30 2012 juancho <juancho> 0.2.4.1-1.mga3
+ Revision: 275891
- imported package gnac
