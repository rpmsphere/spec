Name:           matchbox-keyboard
Version:        0.1.1
Release:        9.3
Summary:        On screen virtual keyboard
Group:          Accessibility
License:        GPLv2+
URL:            http://matchbox-project.org/
Source0:        http://git.yoctoproject.org/cgit.cgi/matchbox-keyboard/snapshot/%{name}-%{version}.tar.gz
Patch0:         matchbox-keyboard-0.1-fix-desktop.patch
Patch3:		    matchbox-keyboard-0.1-automake-1.13.patch
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libfakekey)
BuildRequires:  pkgconfig(xft)
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  expat-devel
BuildRequires:  desktop-file-utils
#BuildRequires:  matchbox-panel-devel

%description
Matchbox-keyboard is an on screen 'virtual' or 'software'
keyboard. It will hopefully work well on various touchscreen
devices from mobile phones to tablet PCs running X Windows.

It aims to 'just work' supporting localised, easy to write
XML layout configuration files.

%prep
%setup -q
%patch0 -p1 -b .fix-category
%patch3 -p1 -b .am

%build
autoreconf -fi
%configure --enable-gtk-im --enable-applet
%make_build

%install
%make_install
find %{buildroot} -name '*.la' | xargs rm

%files
%doc AUTHORS COPYING README
%{_bindir}/matchbox-keyboard
%{_datadir}/matchbox-keyboard
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_libdir}/gtk-2.0/2.10.0/immodules/libmb*-im-invoker.so
%{_libdir}/matchbox-panel/libkeyboard.so

%changelog
* Mon Aug 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuild for Fedora
* Sat Feb 06 2016 umeabot <umeabot> 0.1-10.mga6
+ Revision: 941592
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.1-9.mga5
+ Revision: 746385
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.1-8.mga5
+ Revision: 682177
- Mageia 5 Mass Rebuild
* Sat Oct 19 2013 umeabot <umeabot> 0.1-7.mga4
+ Revision: 526167
- Mageia 4 Mass Rebuild
* Mon Jun 03 2013 fwang <fwang> 0.1-6.mga4
+ Revision: 436010
- rebuild for new libpng
* Sat Jan 19 2013 fwang <fwang> 0.1-5.mga3
+ Revision: 389773
- fix build with latest automake
  + umeabot <umeabot>
    - Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sun Dec 16 2012 pterjan <pterjan> 0.1-4.mga3
+ Revision: 331328
- links with libXrender (fixes build)
* Thu Sep 15 2011 fwang <fwang> 0.1-3.mga2
+ Revision: 143669
- fix linkage
- force regenerate
- drop br
- add patch
- cleanup br
* Sun Apr 10 2011 dmorgan <dmorgan> 0.1-2.6.mga1
+ Revision: 82874
- imported package matchbox-keyboard
* Mon Mar 22 2010 Olivier Blin <oblin@mandriva.com> 0.1-2.6mdv2010.1
+ Revision: 526417
- buildrequire gtk+2-devel for IM
- remove empty dir
- enable gtk input method
- autoreconf for newer libtool
- do not build applet yet (it requires a new matchbox-panel)
- fix buildroot
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
* Thu Oct 16 2008 Thierry Vignaud <tv@mandriva.org> 0.1-2.5mdv2009.1
+ Revision: 294295
- import matchbox-keyboard
* Thu Oct 16 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-2.5mdv2009.1
- adapt to Mandriva
* Tue Sep 23 2008 Vivian zhang <vivian.zhang@intel.com> 0.1
- Add BuildRequires: libXi-devel
* Thu Sep 18 2008 Vivian zhang <vivian.zhang@intel.com> 0.1
- Add comments "specfile originally created for Fedora..." to the spec file
* Tue May 20 2008 Jon McCann <jmccann@redhat.com> 0.1-0.2008.05.19.1
- Initial package
