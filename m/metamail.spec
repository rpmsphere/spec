Name:           metamail
BuildRequires: ncurses-devel libX11-devel
License:        MIT License (or similar)
Group:          Productivity/Networking/Email/Utilities
Requires:       sharutils
Version:        2.7.19
Release:        1259.1
Summary:        MIME Mail Handler
Source0:        metamail-2.7-19.tar.gz
Source1:        mimecheck
Source2:        mimecheck.1
Patch0:         metamail-2.7-19.dif
Patch1:         metamail-2.7-19-security.dif
Patch2:         metamail-2.7-19-getline.dif
Patch3:         metamail-2.7-19-binderman.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Metamail is required for reading multimedia mail messages (such as
those using the Andrew toolkit) with elm.

%prep
%setup -n metamail-2.7-19
%patch -P 1 -b .security
%patch -P 0
%patch2
%patch3

%build
make
make -C fonts

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT%_mandir/man{1,4}
make INSTROOT=$RPM_BUILD_ROOT/usr INSTALL=install install-all
#    mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc
#    install -m 444 fonts/heb8x13B.pcf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc/
#    gzip -9f $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc/heb8x13B.pcf
install -m 755 %{S:1} $RPM_BUILD_ROOT/usr/bin/
install -m 644 %{S:2} $RPM_BUILD_ROOT%{_mandir}/man1/
ln -sf mimecheck $RPM_BUILD_ROOT/usr/bin/mimezip
ln -sf mimecheck $RPM_BUILD_ROOT/usr/bin/mimebzip
ln -sf mimecheck $RPM_BUILD_ROOT/usr/bin/mimegzip

%files
%defattr(-,root,root)
%doc README mailers.txt
#/usr/X11R6/lib/X11/fonts/misc/heb8x13B.pcf.gz
/usr/bin/audiocompose
/usr/bin/audiosend
/usr/bin/extcompose
/usr/bin/getfilename
/usr/bin/mailserver
/usr/bin/mailto
/usr/bin/mailto-hebrew
/usr/bin/metamail
/usr/bin/metasend
/usr/bin/mimeit
/usr/bin/mimencode
/usr/bin/mimecheck
/usr/bin/mimezip
/usr/bin/mimebzip
/usr/bin/mimegzip
/usr/bin/mmencode
/usr/bin/mgrep
/usr/bin/patch-metamail
/usr/bin/rcvAppleSingle
/usr/bin/richtext
/usr/bin/richtoatk
/usr/bin/showaudio
/usr/bin/showexternal
/usr/bin/shownonascii
/usr/bin/showpartial
/usr/bin/showpicture
/usr/bin/sndAppleSingle
/usr/bin/splitmail
/usr/bin/sun-audio-file
/usr/bin/sun-message
/usr/bin/sun-message.csh
/usr/bin/sun-to-mime
/usr/bin/sun2mime
/usr/bin/uudepipe
/usr/bin/uuenpipe
%doc %{_mandir}/man1/audiocompose.1.gz
%doc %{_mandir}/man1/audiosend.1.gz
%doc %{_mandir}/man1/extcompose.1.gz
%doc %{_mandir}/man1/getfilename.1.gz
%doc %{_mandir}/man1/mailto-hebrew.1.gz
%doc %{_mandir}/man1/mailto.1.gz
%doc %{_mandir}/man1/metamail.1.gz
%doc %{_mandir}/man1/metasend.1.gz
%doc %{_mandir}/man1/mgrep.1.gz
%doc %{_mandir}/man1/mime.1.gz
%doc %{_mandir}/man1/mimencode.1.gz
%doc %{_mandir}/man1/mimecheck.1.gz
%doc %{_mandir}/man1/mmencode.1.gz
%doc %{_mandir}/man1/patch-metamail.1.gz
%doc %{_mandir}/man1/richtext.1.gz
%doc %{_mandir}/man1/showaudio.1.gz
%doc %{_mandir}/man1/showexternal.1.gz
%doc %{_mandir}/man1/shownonascii.1.gz
%doc %{_mandir}/man1/showpartial.1.gz
%doc %{_mandir}/man1/showpicture.1.gz
%doc %{_mandir}/man1/splitmail.1.gz
%exclude %doc %{_mandir}/man4/mailcap.4.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.19
- Rebuilt for Fedora
* Tue Oct 20 2009 werner@suse.de
- Yet an other David Binderman fix (bnc#547909)
* Sun Aug 30 2009 coolo@novell.com
- provide Patch0
* Sun Jun  7 2009 ro@suse.de
- rename getline to my_getline to avoid conflict with function
  from glibc
* Mon Sep 15 2008 werner@suse.de
- Fix typo in mailto manual page (bnc#422090)
* Mon Sep 15 2008 werner@suse.de
- Avoid autobuild error
* Thu Jun 28 2007 werner@suse.de
- Add MIME check script usable e.g. in procmailrc filter rules
* Thu Mar 29 2007 rguenther@suse.de
- Add ncurses-devel BuildRequires
* Thu Feb 23 2006 werner@suse.de
- Fix for buffer overflow (bug #153145)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Jan 17 2006 schwab@suse.de
- Don't strip binaries.
* Fri Jul  1 2005 werner@suse.de
- Remove -fsigned-char (bug #93881)
* Fri Jun 10 2005 werner@suse.de
- Use declaration from stdio.h for gets(3)
* Thu May  6 2004 hmacht@suse.de
- added # norootforbuild in specfile
* Fri Mar 19 2004 werner@suse.de
- Fix date issue with locale: be always RFC 822 conform (#35828)
* Tue Mar  2 2004 werner@suse.de
- Fix security fix: sizeof(char*) is not equal to sizeof(char[250])
* Mon Feb  9 2004 werner@suse.de
- Security fix format-string bug and buffer overflow (bug #34369)
* Fri Jan 23 2004 werner@suse.de
- Fix declarations of the stuff to make gcc happy
* Fri Jun 13 2003 coolo@suse.de
- use BuildRoot
- really package mgrep (not just the man page :)
- use %%_mandir
* Tue Dec 17 2002 werner@suse.de
- New: mgrep which does similar to zgrep on mimencoded data
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Sat Jul 13 2002 schwab@suse.de
- mmencode: don't change mode of stdout.
* Mon Oct  1 2001 schwab@suse.de
- Fix quoting in shell scripts.
* Tue May 22 2001 werner@suse.de
- Remove space after ?= closing phrase
* Wed Mar  7 2001 uli@suse.de
- added xf86 to neededforbuild
* Wed Mar  7 2001 werner@suse.de
- Be sure that font directory exists
* Fri Dec 22 2000 werner@suse.de
- If terminal attributes will be restored then do this immediately
* Fri Dec 22 2000 werner@suse.de
- Declare standard functions
- Use putenv of glibc
- Print commando is lpr
- Use limits.h
- Use termios interface of glibc
* Mon Nov 27 2000 sndirsch@suse.de
- removed /usr/X11R6/lib/X11/fonts/misc/heb8x13B.pcf.gz
  from filelist (font already included in xf86 package)
* Fri Nov 17 2000 kukuk@suse.de
- fix Requires: sharutil -> sharutils
* Mon Nov 13 2000 ro@suse.de
- don't redeclare killpg
* Wed Oct 11 2000 werner@suse.de
- Fix bug within metasend (bug# 4099)
* Wed Jun  7 2000 ro@suse.de
- doc relocation
* Thu Mar  2 2000 werner@suse.de
- /usr/man -> /usr/share/man
* Tue Oct 19 1999 werner@suse.de
- If -o is used for mmencoding the file permissions should
  be the same as the input file
- Use Fopen within mmencode.c
- sendmail is stored in /usr/sbin/
- MAILCAPDIR is /etc
- showexternal: check for broken arguments
- mailto.c: don't be fooled by newlines
- Use RPM_OPT_FLAGS
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Tue Aug 24 1999 uli@suse.de
- added -fsigned-char to CFLAGS (PPC)
* Fri Jul 17 1998 werner@suse.de
- Add C source fixes of RedHat against temp exploits
- Make sh and shell scripts using mktemp for temp files
- Use PAGER if set
- Use -o of uudecode to avoid attacks over net
* Tue May 27 1997 florian@suse.de
- fix shell script "audiosend"
* Sat Apr 26 1997 florian@suse.de
- update to new version 2.7-19 from debian
* Thu Jan  2 1997 florian@suse.de
- Bisherige Anpassungen mit der neusten debian-Version vergleichen
  und zusammenbringen.
- Die extra Fonts sind momentan nicht mehr dabei,
  sollten aber auch nicht fehlen...
