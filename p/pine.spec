%define _default_patch_fuzz 2
%define pgpver		0.18.0
%define with_gpgpine	1

Summary:	A commonly used, MIME compliant mail and news reader
Name:		pine
Version:	4.64
Release:	38.1
License:	Freeware
URL:		http://www.washington.edu/pine
Group:		Networking/Mail
Source0:	ftp://ftp.cac.washington.edu/pine/pine%{version}.tar.bz2
Source1:	pine.conf
Source2:	pine-spellcheck
Source3:	http://www.megaloman.com/~hany/_data/pinepgp/pinepgp-%{pgpver}.tar.bz2
Source4:	pine.desktop
Source5:	pico.desktop
# eduardo patch (http://www.math.washington.edu/~chappa/pine/info/all.html)
# contains many bugfixes and feature enhancements such as maildir support.
Patch1:	pine-%{version}-eduardo.patch.bz2
Patch3: pine-4.56-passwd.patch.bz2
Patch4: pine-4.21-fixhome.patch.bz2
Patch9: pine-4.30-ldap.patch.bz2
Patch14: pine-4.56-boguswarning.patch.bz2
Patch21: pine-4.31-segfix.patch.bz2
Patch22: pine-4.40-lockfile-perm.patch.bz2
Patch32: imap-2000-time.patch.bz2
# fixes bug #60818 (RH)
Patch37: pine-4.60-overflow.patch.bz2
# SSL Certificates of remote sites or CA must go
# into /etc/ssl/pine/cert.pem
Patch39: pine-4.60-sslpath.patch.bz2
Patch40: pine-wrongsed.patch
BuildRequires:	openldap-devel
BuildRequires:	ncurses-devel
BuildRequires:	compat-openssl10-devel
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	ghostscript-core ImageMagick
BuildRequires:	krb5-devel
BuildRequires:	cyrus-sasl-devel

%description
Pine is a very popular, easy to use, full-featured email user agent
which includes a simple text editor called pico. Pine supports MIME
extensions and can also be used to read news.  Pine also supports
IMAP, mail and MH style folders.

Pine should be installed because Pine is a very commonly used email
user agent and it is currently in development.

%prep
%setup -q -n %{name}%{version} -a 3

%patch1 -p1 -b .eduardo
%patch3 -p1 -b .passwd
%patch4 -p1 -b .fixhome
%patch9 -p1 -b .ldap-patch
%patch14 -p1 -b .boguswarning
%patch21 -p1 -b .segfix
%patch22 -p0 -b .lockfile-perm
%patch32 -p1 -b .time-h
%patch37 -p1 -b .overflow
%patch39 -p1 -b .sslpath
%patch40 -p0 -b .wrongsed

# this wants /usr/local/bin/perl
chmod 644 contrib/utils/pwd2pine
perl -pi -e "s|/usr/local/bin/perl|/usr/bin/perl|" contrib/utils/pwd2pine

#rm -fr ldap && mkdir ldap && ln -s %{_libdir} ldap/libraries && ln -s /usr/include ldap/include
./contrib/ldap-setup lnx linux-gcc || true

# gssapi support (kerberos 5)
mkdir krb5
ln -s %{_libdir} krb5/lib
ln -s /usr/include krb5/include

# build ssl support
# FIXME: for some reason ssl support is kinda whacked.  Included in patch0
# is some stuff for the Makefile.ssl that might be wrong as well.  There may
# also be a conflict between SSL support and the maildir patch.
# (vdanen) enabled for testing (4.33-1mdk)
perl -pi -e "s|/usr/local/ssl|/usr/lib/ssl|" build


%build
perl -pi -e "s|(-g )?-fno-omit-frame-pointer -O6|$RPM_OPT_FLAGS ${no_strength_reduce}|g" \
	./imap/src/imapd/Makefile \
	./imap/src/ipopd/Makefile \
	./imap/src/mtest/Makefile \
	./imap/src/osdep/unix/Makefile \
	./imap/Makefile \
	./imap/tools/Makefile

sed -e "s:\$(SSLDIR)/certs:%{_sysconfdir}/ssl/pine:" \
                        -e "s:\$(SSLCERTS):%{_sysconfdir}/ssl/pine:" \
                        -i "./imap/src/osdep/unix/Makefile"

sed -i 's|SIGUNUSED|31|' pico/osdep/os-*.h

./build \
%ifarch ia64
	OPTIMIZE="-O" \
%else 
	OPTIMIZE="$RPM_OPT_FLAGS" \
%endif
	EXTRACFLAGS="-DIGNORE_LOCK_EACCES_ERRORS -Wno-format-security" \
	EXTRALDFLAGS+=" -lsasl2 -llber" \
%{!?nossl:SPECIALAUTHENTICATORS=ssl} \
%{!?nossl:SSLTYPE=unix} \
%{!?nossl:SSLDIR=/usr} \
%{!?nossl:SSLCERTS=%{_sysconfdir}/ssl/pine} \
%{!?nossl:SSLINCLUDE=/usr/include/openssl} \
%{!?nossl:SSLLIB="-lssl -lcrypto"} \
    DEBUG="-O2" \
	lrh

%if %{with_gpgpine}
(
cd pinepgp-%{pgpver}
./configure --prefix=%_prefix \
            --bindir=%_bindir \
	    --libdir=%_libdir \
            --with-gpg=%_bindir/gpg
make
)
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir} $RPM_BUILD_ROOT%{_libdir}
install -m 644 doc/mime.types $RPM_BUILD_ROOT%{_libdir}/mime.types
for n in pine pico pilot rpdump rpload; do
    install -m 755 bin/$n $RPM_BUILD_ROOT%{_bindir}/$n
done

### PINEPGP DROPIN ###
%if %{with_gpgpine}
cd pinepgp-%{pgpver}
make install-pinegpg DESTDIR=$RPM_BUILD_ROOT
cd ..
%endif
######################

cd doc
for n in pine.1 pico.1 pilot.1 rpdump.1 rpload.1; do
    install -m 644 $n $RPM_BUILD_ROOT%{_mandir}/man1
done
cd -

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT/usr/bin

cat <<EOF > $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf.fixed
#
# Pine system-wide enforced configuration file - customize as needed
#
# This file holds the system-wide enforced values for pine configuration
# settings. Any values set in it will override values set in the
# system-wide default configuration file (/etc/pine.conf) and
# the user's own configuration file (~/.pinerc).
# For more information on the format of this file, read the
# comments at the top of /usr/lib/pine.conf

EOF

# Change braindead permissions in contrib directory!
chmod 644 contrib/*-setup
chmod 644 contrib/bitmaps/pine2.icon

# Icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert -transparent white -geometry 48x48 contrib/bitmaps/%name.icon $RPM_BUILD_ROOT%{_datadir}/pixmaps/%name.png

# Desktop files
mkdir -p $RPM_BUILD_ROOT%_datadir/applications
install %{SOURCE4} $RPM_BUILD_ROOT%_datadir/applications/pine.desktop
install %{SOURCE5} $RPM_BUILD_ROOT%_datadir/applications/pico.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%doc README CPYRIGHT doc/*.txt doc/pine-ports doc/tech-notes doc/mailcap.unx imap/docs/bugs.txt 
%doc contrib
%{_bindir}/pine
%{_bindir}/pico
%{_bindir}/pilot
%{_bindir}/rpdump
%{_bindir}/rpload
%{_bindir}/pine-spellcheck
%{_mandir}/man1/*
%attr(0644,root,root)	%{_libdir}/mime.types
%attr(0644,root,root)	%{_datadir}/applications/pico.desktop
%attr(0644,root,root)	%{_datadir}/applications/pine.desktop
%attr(0644,root,root)	%config(noreplace) %{_sysconfdir}/pine.conf
%attr(0644,root,root)	%config(noreplace) %{_sysconfdir}/pine.conf.fixed

%{_datadir}/pixmaps/%{name}.png

%if %{with_gpgpine}
%attr(0755, root, root) %{_bindir}/pinepgpgpg-install
%attr(0755, root, root) %{_bindir}/pinegpg-install
%attr(0755, root, root) %{_bindir}/pinegpg
%attr(0755, root, root) %{_bindir}/gpg-sign
%attr(0755, root, root) %{_bindir}/gpg-sign+encrypt
%attr(0755, root, root) %{_bindir}/gpg-encrypt
%attr(0755, root, root) %{_bindir}/gpg-check
%endif

%changelog
* Tue May 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4.64
- Rebuild for Fedora

* Tue Apr 24 2007 Olivier Thauvin <nanardon@zarb.org> 4.64-4plf
- update Edouardo's patch

* Thu May 11 2006 Olivier Thauvin <nanardon@zarb.org> 4.64-3plf
- rebuild

* Sat Oct 15 2005 Olivier Thauvin <nanardon@zarb.org>
- add changelog...

* Sat Oct 15 2005 Olivier Thauvin <nanardon@zarb.org> 4.64-1plf
- 4.64

* Fri Sep 09 2005 Olivier Thauvin <nanardon@zarb.org> 4.62-3plf
- From Andreas Hasenack <ahasenack@terra.com.br>
  - enabled with gssapi support
  - enabled with sasl2 support
  - rebuilt with openldap-2.3.x

* Tue Apr 19 2005 Olivier Thauvin <nanardon@zarb.org> 4.62-2plf
- From Giuseppe Ghib <ghibo@mandriva.com>
  - spec clean up
  - fix ssl dir

* Tue Feb 01 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.62-1plf
- 4.62

* Sat Nov 27 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.61-5plf 
- Matthias Debus <psic4t@netbands.de>
  - patch1: eduardo's patch (includes fixes and feature enhancements
  - backout patch8 (flock): included in patch1?
  - backout patch36 (maildir support): included in patch1
  - backout patch43 (wrtaccents): seems to be included in patch1

* Tue Aug 31 2004 Matthias Debus <psic4t@netbands.de> 4.61-4plf
- new menu
- fix permissions

* Sun Aug 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.61-3plf
- reinclude maildir patch (thx ghibo)
- flock patch (ghibo)

* Tue Aug 03 2004 Matthias Debus <psic4t@netbands.de> 4.61-2plf
- make icons transparent

* Fri Jul 23 2004 Matthias Debus <psic4t@netbands.de> 4.61-1plf
- new version
- use ImageMagick to convert icons
- add desktop files for pine and pico (from pld)
- fix license
- fix menu
- cleanup (at least a bit)

* Wed May 12 2004 Matthias Debus <psic4t@netbands.de> 4.60-1plf
- new version
- back out patch0: merged (finally)
- back out patch8 and source4: merged
- back out patch33: merged (finally!)
- back out patch36: needs to get regenerated -> no maildir support ATM 

* Fri Sep 12 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.58-1plf
- 4.58 (Major security fixes)
- cleanup

* Tue Aug 05 2003 Matthias Debus <psic4t@netbands.de> 4.56-1plf 
- new version
- put in new versions of patches 0,3 and 14 again (not merged, needed :)

* Mon Apr 21 2003 Matthias Debus <psic4t@netbands.de> 4.55-1plf 
- new version
- backed out patches 0,3 and 14 (merged?)

* Sun Jan 26 2003 Matthias Debus <psic4t@netbands.de> 4.53-1plf 
- new version

* Sun Dec 15 2002 Matthias Debus <psic4t@netbands.de> 4.51-1plf 
- new version

* Tue Dec 03 2002 Matthias Debus <psic4t@netbands.de> 4.50-1plf 
- new version
- back out patch35 (threading, not needed anymore)

* Sun Jul 28 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.44-4plf 
- From Oden Eriksson <oden.eriksson@kvikkjokk.net> 
	- added P36 (qmail Maildir support)

* Wed Jul 24 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.44-3plf 
- From Matthias Debus <psic4t@netbands.de>
	- first PLF release
	- build with gcc-3.1
	- (patch 35) add support for real threading
	- update pinepgp to 0.18
	- sanitize spec file (patches)
- png icons (out xpm!)

* Fri Feb 15 2002 Stefan van der Eijk <stefan@eijk.nu> 4.44-2mdk
- BuildRequires

* Thu Feb 14 2002 Jesse Kuang <kjx@mandrakesoft.com> 4.44-1mdk
- upgrade to 4.44

* Sun Dec 30 2001 Jesse Kuang <kjx@mandrakesoft.com> 4.43-1mdk
- upgrade to 4.43
- add support for pgp, gpg

* Sun Oct 07 2001 Jesse Kuang <kjx@mandrakesoft.com> 4.40-1mdk
- upgrade pine to 4.40

* Thu Jun 28 2001 Vincent Danen <vdanen@mandrakesoft.com> 4.33-2mdk
- add BuildRequires: pam-devel

* Wed Apr 25 2001 Vincent Danen <vdanen@mandrakesoft.com> 4.33-1mdk
- 4.33
- sync patches with rh
- new maildir patch
- re-enable ssl to see if works better now

* Fri Apr 13 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 4.30-4mdk
- sanitized specfile (s/Copyright/License, BuildRequires, etc.)
- added missing includes in imap/src/osdep/os_lnx.h (patch21)
- rebuilt for post LDMDK 8.0 with -fno-strength-reduce on ix86
- completely got rid of -O6 optimization flag

* Fri Nov 10 2000 Vincent Danen <vdanen@mandrakesoft.com> 4.30-3mdk
- merge with Red Hat
- use lnp (PAM auth) insteaf of slx (crypt)
- some spec fixes
- enable SSL
- make config files noreplace
- added large icon
- bzip patches and icons


* Thu Nov 09 2000 Vincent Danen <vdanen@mandrakesoft.com> 4.30-2mdk
- patch to correct pine crashing and check extra NULL pointers from RH

* Tue Nov 07 2000 Vincent Danen <vdanen@mandrakesoft.com> 4.30-1mdk
- 4.30
- security fix for incoming mailbox handling
- remove hardcoded icon directory in menus

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.21-6mdk
- automatically added BuildRequires

* Thu Aug 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.21-5mdk
- rebuild for BM
- rebuild with macros
- tmppath
* Sun Apr 09 2000 Denis HAvlik <denis@mandrakesoft.com> 4.21-4mdk
- Group: Networking/Mail
- pine-tree icon + menu entries (for pine + pico)
- spec-helper

* Sat Feb 19 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 4.21-3mdk
- make patch to change os-lnx.h from /bin/passwd to /usr/bin/passwd

* Tue Dec 14 1999 John Buswell <johnb@mandrakesoft.com>
- add new maildir patches
- add vfs patch
- fixed non-existant directory seek problem (bug:#506)

* Tue Nov 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 4.21.
- Merge with recent redhat changes.

* Tue Nov 02 1999 John Buswell <johnb@mandrakesoft.com>
- Rebuild and Repackage for oxygen (release 2)

* Thu Oct 14 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 4.20
- sync with RH

* Thu Aug 12 1999 Cristian Gafton <gafton@redhat.com>
- add maildir patch

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- fix buildroot and add cleanup section
- move config files to /etc/pine.conf

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- turned off .pine-debugX files

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Fri Nov 13 1998 Cristian Gafton <gafton@redhat.com>
- patch to enable SIGWINCH processing (why do the pine folks keep 
  disabling this stuff?!)

* Fri Oct 09 1998 Cristian Gafton <gafton@redhat.com>
- use termios instead of termio (patch used to be in here...)
- use terminfo instead of termcap and link against ncurses instead of termcap
- supply -lcrypt as a standard lib

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 4.04 (compatibility with some client imaps).

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- use only fcntl locking.

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.03

* Fri Aug 14 1998 Jeff Johnson <jbj@redhat.com>
- patch to 4.02A.
- disable stupid EACCESS warnings.

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.02.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jan 15 1998 Erik Troan <ewt@redhat.com>
- added patch to fix pine filters

* Tue Dec 30 1997 Erik Troan <ewt@redhat.com>
- fixed resizing in pine and pico

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- removed patch for SIGCHLD race -- it shouldn't be necessary
- added patch to avoid longjmp() from SIGCHLD handler -- SIGCHLD handling
  is sane now

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- added a patch for handling a SIGCHLD race condition

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- fix for locks w/ long st_dev field
- use termios rather then termio

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- removed exec bit from /usr/doc/pine-3.96-1/contrib/utils/pwd2pine
