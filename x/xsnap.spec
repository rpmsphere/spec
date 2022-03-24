%undefine _debugsource_packages

Name:		xsnap
Version:	1.5.15
Release:	1
Summary:	Program to interactively take a snapshot of a region of the screen
Group:		Graphics
License:	BSD
URL:		ftp://ftp.ac-grenoble.fr/ge/Xutils/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:  libX11-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel

%description
xsnap is a program that allows one to interactively take a snapshot of a
region of the screen.  This snapshot is then saved to a window. Press "p" 
to create a pixmap of this snapshot.

%prep
%setup -q

%build
xmkmf -a
%make_build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%clean
rm -fr $RPM_BUILD_ROOT

%files
%doc README INSTALL AUTHORS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/locale/fr/LC_MESSAGES/xsnap.mo
#/usr/X11R6/lib/X11/doc/html/*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.15
- Rebuilt for Fedora
* Wed Nov 08 2006 JP Demailly <demailly@fourier.ujf-grenoble.fr> 1.5.1-1mdk
- new upstream version
* Mon Apr 18 2005 Franck Villaume <fvill@mandriva.org> 1.4.3-4mdk
- more buildRequires
* Sun Mar 20 2005 Franck Villaume <fvill@mandrake.org> 1.4.3-3mdk
- fix BuildRequires
* Sat Dec 04 2004 Franck Villaume <fvill@freesurf.fr> 1.4.3-2mdk
- add BuildRequires
- missing file
* Tue Oct 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.4.3-1mdk
- 1.4.3
* Tue Sep 21 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.4.2-1mdk
- 1.4.2
* Tue Sep 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.4-2mdk
- update to rev1
* Wed Sep 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4
* Fri Apr 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3-3mdk
- fixed buildrequires
* Fri Apr 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3-2mdk 
- from Pierre-Michel Theveny <pmth@free.fr> :
	- Correction in description
* Sat Mar 27 2004  Pierre-Michel Theveny <pmth@free.fr> 1.3-1mdk
- First build on 9.2
