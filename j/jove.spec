Summary: Jonathan's Own Version of Emacs
Name: jove
Version: 4.17.3.7
Release: 1
License: Copyright only
Group: Applications/Editors
URL: https://github.com/jonmacs/jove
Source: jove-%{version}.tar.gz
BuildRequires: ncurses-devel groff
%global configflags SYSDEFS="-DSYSVR4 -D_XOPEN_SOURCE=500 -DIPROC_TERM='\\"TERM=vanilla\\"'" NROFF="nroff -Tascii" TROFF=groff TROFFPOST=""

%description
Jove is a compact, powerful Emacs-style text-editor. It provides the common
emacs keyboard bindings, together with a reasonable assortment of the most
popular advanced features (e.g. interactive shell windows, compile-it,
language specific modes) while weighing in with CPU, memory, and disk
requirements comparable to vi(1).

%prep
%setup -q

%build
# Keep all three make commands consistent, except for JOVEHOME and targets.
# JOVEHOME must be the ultimate path since it will be compiled into JOVE.
make JOVEHOME=/usr LIBDIR=%{_libdir}/jove SHAREDIR=%{_datadir}/jove MANDIR=%{_mandir}/man1 OPTFLAGS="%{optflags}" %{configflags} all doc/jove.man doc/jove.man.ps
mv doc/jove.man doc/jove.man.txt

%install
# Keep all three make commands consistent, except for JOVEHOME and targets.
# JOVEHOME is a temporary home under $RPM_BUILD_ROOT/.
# This can be different from JOVEHOME for the build phase's make.
#mkdir -p $RPM_BUILD_ROOT%{_bindir}
#mkdir -p $RPM_BUILD_ROOT%{_libdir}
#mkdir -p $RPM_BUILD_ROOT%{_datadir}
#mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
#make JOVEHOME=$RPM_BUILD_ROOT/usr LIBDIR=$RPM_BUILD_ROOT%{_libdir}/jove SHAREDIR=$RPM_BUILD_ROOT%{_datadir}/jove MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 OPTFLAGS="%{optflags}" %{configflags} install
%make_install JOVEHOME=/usr LIBDIR=%{_libdir}/jove SHAREDIR=%{_datadir}/jove MANDIR=%{_mandir}/man1 OPTFLAGS="%{optflags}" %{configflags}
mv doc/README doc/README.doc
# although we build jovetool.1 and xjove.1, we don't install them
#rm $RPM_BUILD_ROOT%{_mandir}/man1/jovetool.1
#rm $RPM_BUILD_ROOT%{_mandir}/man1/xjove.1
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_mandir}

%files
%{_libdir}/jove
%{_datadir}/jove
%{_bindir}/jove
%{_bindir}/teachjove
%{_mandir}/man1/jove.1*
%{_mandir}/man1/teachjove.1*
%doc README doc/jove.man.txt doc/jove.man.ps doc/jove.qref 

%changelog
* Sun May 22 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 4.17.3.7
- Rebuilt for Fedora
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.16.0.73-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.16.0.73-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.16.0.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.16.0.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.16.0.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Paul Wouters <pwouters@redhat.com> - 4.16.0.73-4
- Include more jove documentation (txt,ps) and quick ref card
* Mon Jul 16 2012 Paul Wouters <pwouters@redhat.com> - 4.16.0.73-3
- Fix license to "Copyright only" as per spot's advise
- Removed defattr (no el5 built)
- use global, not define
* Sun Jun 10 2012 Paul Wouters <pwouters@redhat.com> - 4.16.0.73-2
- new .spec file
* Sun Jul 11 2010 D. Hugh Redelmeier 4.16.0.73
- added NROFF="nroff -Tascii" to Makefile and jove.spec to force groff to use ASCII
- spelling corrections [Cord Beermann]
- remove -lolgx from xjove link [Cord Beermann]
- improve recover's email Subject [Cord Beermann]
* Mon May 24 2010 D. Hugh Redelmeier 4.16.0.72
- eliminate strcpy and byte_copy calls with overlapping source and destination
- fix setmaps.c misuse of fprintf
* Sun May 16 2010 D. Hugh Redelmeier 4.16.0.71
- add new variable display-default-filenames (Casey Leedom)
- eliminate most GCC warnings; improve handling of some errors
- allow for Linux/glibc elimination of I_PUSH (pseudo TTY STREAMS)
- improve jove.spec for Red Hat packaging
- delete obsolete command process-dbx-output
- delete obsolete variables allow-bad-filenames, display-bad-filenames, internal-tabstop
- add bindings for more xterm function key variants
