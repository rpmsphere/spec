%define	fontdir     /usr/share/fonts/misc

Name:           cmatrix
Version:        1.2a
Release:        319.1
License:        GNU General Public License (GPL)
Summary:        The Console Screensaver in Accordance with Matrix
URL:            http://www.asty.org/cmatrix/
Group:          Applications/Terminal
Source:         cmatrix-%{version}.tar.bz2
Patch0:         cmatrix-%{version}-makefile.patch
Patch1:         cmatrix-no-TIME-DATE.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  kbd
BuildRequires:  ncurses-devel
BuildRequires:  libX11-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CMatrix is a program I wrote one evening because I didn't want to have
to run Wind*ws to see the cool scrolling lines from 'The Matrix', my
fave movie. If you haven't seen this movie and you are a fan of
computers or sci-fi in general, go see this movie!!!

%prep
%setup -q
%patch0
%patch1 -p1

%build
aclocal
autoconf
automake -a
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{fontdir}
mkdir -p $RPM_BUILD_ROOT/lib/kbd/consolefonts
make DESTDIR=$RPM_BUILD_ROOT install
# workaround for build with modular Xorg
install -m644 mtx.pcf $RPM_BUILD_ROOT%{fontdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_mandir}/man1/*
%{_bindir}/*
# workaround for build with modular Xorg
%{fontdir}/*
/lib/kbd/consolefonts/*

%changelog
* Thu May 19 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2a
- Rebuild for Fedora
* Mon Apr 11 2011 puzel@novell.com
- use spec-cleaner
- add cmatrix-no-TIME-DATE.patch (prevent unnecessary rebuilds)
* Wed Jan  7 2009 puzel@suse.cz
- fix rpmlint warnings
* Fri Mar 30 2007 rguenther@suse.de
- add ncurses-devel BuildRequires
* Thu Aug 10 2006 mfabian@suse.de
- move fonts to /usr/share/fonts/misc (because of X11R7).
* Mon Jul 24 2006 mmarek@suse.de
- workaround build with modular Xorg
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Sep 28 2004 uli@suse.de
- no consolefonts on s390*
* Fri Jul 23 2004 ro@suse.de
- added kbd to neededforbuild
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Mon Feb 10 2003 vbobek@suse.cz
- update to version 1.2a:
  * bugfixes
  * matrix size is now allocated dynamically
* Thu Feb 21 2002 pmladek@suse.cz
- fixed location of console fonts
- fixed file list
* Mon Nov  5 2001 pmladek@suse.cz
- fixed for automake 1.5
* Fri Mar 16 2001 pmladek@suse.cz
- new package
- added buildroot
