Name: gfloatbg
Version: 0.2
Release: 10.1
Summary:  A tool to manipulate the background colors
URL: http://sourceforge.net/projects/%name/ 
License: GPLv2
Group: Graphical desktop/GNOME
Source:  http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source1: %name.desktop
Source5: poltava1trnsp.png
Patch: gfloatbg-0.2-link.patch
BuildRequires: gtk2-devel
BuildRequires: GConf2-devel

%description
GFloatbg is a little application that slowly modifies the color of the
GNOME's desktop. You won't be able to see the color change, but after
a quarter of an hour, you'll notice that it did change, however.

%prep
%setup -q
%patch

%build
autoreconf
%configure
make

%install
%make_install
mkdir -p %buildroot%_datadir/gnome/autostart
install -m644 %SOURCE1 %buildroot%_datadir/gnome/autostart/%name.desktop

# A sample background with transparency
mkdir -p %buildroot%_datadir/design/backgrounds
cp %SOURCE5 %buildroot%_datadir/design/backgrounds

%files
%doc README AUTHORS INSTALL NEWS COPYING ChangeLog 
%_bindir/%name
%_datadir/gnome/autostart/%name.desktop
%_datadir/design/backgrounds/*

%changelog
* Tue Feb 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Sat Jun 09 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2
* Tue Aug 14 2007 Alexey Rusakov <ktirf@altlinux.org> 0.1-alt3
- added a desktop file that makes gfloatbg run on session start.
- made the license tag more exact (GPL version 2)
* Wed Jul 25 2007 Alexey Rusakov <ktirf@altlinux.org> 0.1-alt2
- thanks to Andrii for the prepared specfile.
- added dependencies
- added an example background with transparency (again many thanks to Andrii).
* Wed Jul 18 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 0.1-alt1
- build with minimal documentations
* Wed Jul 18 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 0.1-alt0
- initial build for ALT Linux (Sisyphus)
