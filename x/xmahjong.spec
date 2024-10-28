%undefine _debugsource_packages

Name:           xmahjong
BuildRequires:  freetype-devel
BuildRequires:  libX11-devel
#Conflicts:      xmahjongg
Version:        2010.11.8
Release:        1
Summary:        Mahjong for X
License:        MIT
Group:          Amusements/Games/Board/Other
Source:         xmahjong.tar.bz2
Patch0:         xmahjong.dif
Patch1:         xmahjong-missing-includes.patch

%description
Mahjong is a challenging Chinese game similar to domino. It is usually
played by four players. Xmahjong is the solitaire version designed for
the X Window System. More can be found in the appropriate manual page.
xmahjong is really xmahjongg ver. 2.

%prep
%setup -q -n xmahjong
%patch 0
%patch 1 -p1
sed -i 's|ahjongg|ahjong|' *
rename ahjongg ahjong *

%build
xmkmf -a
rm -f xmahjong.man; ln -sf xmahjong.6 xmahjong.man
make LIBDIR=%{_datadir} %{?_smp_mflags}

%install
chmod 644 copyright readme.1 readme.2
make install install.man DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_datadir} FONTDIR=%{_datadir}/fonts

%files
%doc copyright readme.1 readme.2
%{_datadir}/xmahjong
%{_bindir}/xmahjong
%{_datadir}/fonts/misc/xmahjong.pcf.gz
%{_mandir}/man1/xmahjong.1x.*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2010.11.8
- Rebuilt for Fedora
* Fri Jul  5 2013 dap.darkness@gmail.com
- Conflicts with xmahjongg package because xmahjong is really
  xmahjongg ver. 2.
* Mon Jan 14 2013 werner@suse.de
- Require bdftopcf at build time (bnc#798333)
* Mon Nov  5 2012 werner@suse.de
- Avoid errors due wrong permissions
* Fri Aug 10 2012 werner@suse.de
- Relocate %%reconfigure_fonts_prereq macro as osc source validator
  is not able to handle this before Version tag
* Mon Aug  6 2012 pgajdos@suse.com
- prepare spec file for dropping SuSEconfig.fonts (openFATE#313536)
* Thu May 10 2012 vuntz@opensuse.org
- Pass FONTDIR=%%{fontdir}/.. to "make install" so that the font is
  correctly installed in /usr/share/fonts/misc instead of
  /usr/share/fonts/X11/misc.
* Mon Feb 20 2012 jengelh@medozas.de
- Remove redundant tags/sections from specfile
- Parallel build with %%_smp_mflags
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Thu Aug 10 2006 mfabian@suse.de
- change paths for X11R7
- bzip2 source tarball
- add missing includes
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Dec  6 2004 mfabian@suse.de
- use new macro "%%run_suseconfig_fonts".
* Thu May 27 2004 sndirsch@suse.de
- added freetype2 to #neededforbuild; prevents from building empty
  xmahjong font (bdftopcf needs freetype2)
* Fri Mar 19 2004 mfabian@suse.de
- use %%suseconfig_fonts_prereq
- run SuSEconfig.fonts and SuSEconfig.pango in %%post and %%postun
* Sun Jan 11 2004 adrian@suse.de
- add %%defattr
* Fri Jun 13 2003 kukuk@suse.de
- Use BuildRoot
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Wed Jun 20 2001 ro@suse.de
- fix to build
* Thu Dec 14 2000 werner@suse.de
- Group tag
* Mon Jun  5 2000 ro@suse.de
- specfile cleanup , doc relocation
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Sep 24 1998 ro@suse.de
- fixed arguments for bind, connnect in initial.c
* Wed May 14 1997 werner@suse.de
- Move documentation to /usr/doc/packages/xmahjong
