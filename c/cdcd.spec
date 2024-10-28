Summary:        Command line based cd player with cddb support
Name:           cdcd
Version:        0.6.6
Release:        25.1
License:        GPL
Group:          Sound
Source0:        https://sourceforge.net/projects/libcdaudio/files/cdcd/0.6.6/%{name}-%{version}.tar.bz2
Patch0:         cdcd-0.6.6-drop-glib1.patch
BuildRequires:  libcdaudio-devel readline-devel
URL:            https://libcdaudio.sourceforge.net/

%description
cdcd takes a different approach from conventional console(or X) based CD
players, in that it doesn't keep with the display-oriented paradigm.
Conventional computer-based CD players resemble traditional physical CD
players.  This is fine, if your user interface consists of 10 buttons.
However, computers have keyboards, so why not use them? Besides, it's
certainly a waste of a console or an xterm to have a traditional CD player
open anyway.

%prep
%setup -q
%patch 0 -p0
sed -i -e 's/sparc64)/sparc64 | x86_64)/' -e 's/sparc64-\*/sparc64-* | x86_64-*/' config.sub

%build
%configure
make

%install
rm -rf %{buildroot}
%make_install
rm %{buildroot}%{_infodir}/dir

%files
%doc README AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*

%changelog
* Sat Nov 24 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.6
- Rebuilt for Fedora
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-10mdv2011.0
+ Revision: 616976
- the mass rebuild of 2010.0 packages
* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.6.6-9mdv2010.0
+ Revision: 436956
- rebuild
* Fri Apr 03 2009 Funda Wang <fwang@mandriva.org> 0.6.6-8mdv2009.1
+ Revision: 363653
- drop glib1 detection
  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild
  + Guillaume Rousse <guillomovitch@mandriva.org>
    - regenerate autotools suite to fix x86_64 build
    - rebuild for latest readline
* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.6.6-5mdv2009.0
+ Revision: 243461
- rebuild
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.6-3mdv2008.1
+ Revision: 136289
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cdcd
* Thu Aug 03 2006 Lenny Cartier <lenny@mandriva.com> 0.6.6-3mdv2007.0
- rebuild
* Sat Jan 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.6-2mdk
- wipe out buildroot in %%install, not %%prep
- quiet setup
- fix summary-ended-with-dot
- cosmetics
* Wed Aug 04 2004 Jerome Soyer <jeromesoyer@yahoo.fr> 0.6.6-1mdk
- 0.6.6
* Wed Jul 23 2003 Michael Scherer <scherer.michael@free.fr> 0.6.4-3mdk
- Buildrequires 
* Sun Apr 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6.4-2mdk
- adjust buildrequires
* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6.4-1mdk
- 0.6.4
* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6.3-3mdk
- rebuild
* Wed Jul 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.3-2mdk
- rebuild for new readline
* Tue Mar 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.6.3-1mdk
- 0.6.3
* Thu Jun 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-4mdk
- rebuild
* Wed Sep 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-3mdk
- build release
* Tue Apr 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-2mdk
- fix group, files section
- fix permission on sources
* Thu Feb 08 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build
- v0.5.0
* Sat Jul 31 1999 Adrian Likins <alikins@redhat.com>
-updated to 0.4.6
-readded the man page
* Sun Jun  6 1999 Adrian Likins <alikins@redhat.com>
-first release as rpm
