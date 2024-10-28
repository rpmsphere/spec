Name:           xstroke
BuildRequires:  libpng-devel
BuildRequires:  libXpm-devel, libXtst-devel, gtk2-devel
URL:            https://xstroke.org/
Version:        0.6
Release:        474.1
Summary:        Fullscreen gesture recognition for X
License:        GPL v2 or later
# PreReq:       %fillup_prereq %insserv_prereq 
Group:          Hardware/Mobile
Source:         xstroke-%{version}.tar.bz2
Source1:        xstroke.png
Source2:        xstroke.desktop
# please upstream it
Patch0:         xstroke-no-copy-dt-needed-entries.patch

%description
xstroke is a full-screen gesture recognition program for the X Window
System. It captures gestures performed with a pointer device, (such as
a mouse, a stylus, or a pen/tablet), recognizes the gestures and
performs actions based on the gestures.



Authors:
--------
    Carl Worth <cworth@east.isi.edu>

%prep
%setup -q
%patch 0 -p1
libtoolize --force
autoreconf -f --install 

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" ./configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=%{_sysconfdir} --with-libdir=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} libdir=%{_libdir} install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
cp -pr AUTHORS COPYING INSTALL ChangeLog NEWS README TODO $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/

%files
%{_bindir}/xstroke
%dir %{_sysconfdir}/xstroke
%config %{_sysconfdir}/xstroke/alphabet
%doc %{_defaultdocdir}/%{name}
##%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Wed Sep 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora

* Tue Aug 30 2011 pgajdos@suse.com
- build with --no-copy-dt-needed-entries
  * no-copy-dt-needed-entries.patch

* Sun Aug 12 2007 stbinner@suse.de
- disable start-up notification under KDE
- fix GenericName capitalization for after 10.3

* Mon Jan  8 2007 dkukawka@suse.de
- Fixed b.n.c #222484: added GenericName

* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires

* Wed Sep 28 2005 dmueller@suse.de
- add norootforbuild

* Sat May  7 2005 dkukawka@suse.de
- added desktopfile and icon for menu entry

* Wed Jan 19 2005 behlert@suse.de
- added various files into doc-dir

* Tue Jan 18 2005 behlert@suse.de
- initial version
