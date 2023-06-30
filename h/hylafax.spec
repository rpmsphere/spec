Name:           hylafax
Requires:       ghostscript metamail mm postfix mgetty xz
BuildRequires:  gcc-c++ automake zlib-devel libjpeg-devel libpng-devel libtiff-devel
License:        MIT License (or similar)
Group:          Hardware/Fax
Provides:       fax_daemon
Requires:       libtiff a2ps hylafax-client mgetty
Conflicts:      sendfax
Version:        6.0.7
Release:        2.1
Source0:        %{name}-%{version}.tar.gz
Source1:        latex-cover-1.04.tar.lzma
Source2:        %{name}-SuSE.tar.lzma
Source3:        hylafax-6.0.4.de.po
Patch:          hylafax-6.0.4.patch
Patch1:         hylafax-6.0.4-isdn.patch
Patch2:         hylafax-6.0.4-valist.patch
Patch3:         hylafax-6.0.4-pic.patch
Patch4:         hylafax-6.0.4-fax_user.patch
Patch5:         hylafax-6.0.4-asciifix.patch
Patch6:         hylafax-6.0.4-warning.patch
Patch7:         hylafax-6.0.4-dispatch-isdn.patch
Patch8:         hylafax-6.0.4-conv.patch
Patch9:         hylafax-6.0.4-no-timestamp.patch
Patch10:        hylafax-6.0.4-DESTDIR.patch
Patch11:        hylafax-6.0.4-configure.patch
Patch12:        hylafax-changed_options.patch
URL:            https://www.hylafax.org
Summary:        Very Powerful Fax Server
%define lib_dir %{_prefix}/lib/fax
%define spooldir /var/spool/fax

%description
HylaFAX is an enterprise-class system for sending and receiving facsimiles as well as for sending alpha-numeric pages.

Authors:
--------
    Sam Leffler <sam@engr.sgi.com>

%package client
License:        MIT License (or similar)
Group:          Hardware/Fax
Conflicts:      sendfax
Summary:        Linux client package for the Hylafax server

%description client
This is linux client part of the very powerful Hylafax fax server. If
you already run the Hylafax fax server on an other machine at your
network, you can use this package to access the server.

Authors:
--------
    Sam Leffler <sam@engr.sgi.com>

%prep
%setup -q -a 1 -a 2
%patch
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
##%patch8
%patch9
%patch10
##%patch11
%patch12
# needs to be executable 
chmod 755 SuSE/usr/lib/fax/a2pswrap
find ../ -name .cvsignore -exec rm {} \;  
cp %{SOURCE3} po/de.po
sed -i 's/4\.\[0\]/4.[4]/' configure

%build
./configure --with-OPTIMIZER="%{optflags} -Wno-format-security" --with-STRIP=: \
            --with-MKDIR="/bin/mkdir -p" ${RPM_ARCH}-suse-linux < /dev/null
%{__make} BIN=%{_bindir} \
     LIBDATA=%{lib_dir} \
     LIBEXEC=%{lib_dir} \
     SBIN=%{_sbindir} \
     SPOOL=%{spooldir} \
     MAN=%{_mandir} \
     DESTDIR=%{buildroot} \
     LIBDIR=%{_libdir} \
     LOCALEDIR=%{_datadir}/locale

%install
rm -rf ${RPM_BUILD_ROOT}
install -d %{buildroot}%{spooldir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_mandir}
install -d %{buildroot}%{_sysconfdir}/init.d
%{__make} BIN=%{_bindir} \
     LIBDATA=%{lib_dir} \
     LIBEXEC=%{lib_dir} \
     SBIN=%{_sbindir} \
     SPOOL=%{spooldir} \
     MAN=%{_mandir} \
     DESTDIR=%{buildroot} \
     LIBDIR=%{_libdir} \
     LOCALEDIR=%{_datadir}/locale install
install -m755 etc/hylafax %{buildroot}%{_sysconfdir}/init.d
install -d %{buildroot}%{_sbindir}
ln -sf ../../etc/init.d/hylafax %{buildroot}%{_sbindir}/rchylafax
cp -af SuSE/* %{buildroot}
rm -f %{buildroot}/README.SuSE
install -d %{buildroot}%{spooldir}/bin/
install -m755 faxsend %{buildroot}%{spooldir}/bin/
##install -d %{buildroot}%{_defaultdocdir}/%{name}
##mv %{buildroot}%{lib_dir}/faxcover_example_sgi.ps %{buildroot}%{_defaultdocdir}/%{name}
#rm -f %{buildroot}%{_libdir}/*.so
rm -f /usr/lib/debug/.build-id/11/877b19d1d92aae65fa3cdadbace22c918d8a7c
rm -f /usr/lib/debug/.build-id/11/877b19d1d92aae65fa3cdadbace22c918d8a7c.debug
rm -f /usr/lib/debug/usr/lib/fax/typetest.debug
rm -f /usr/lib/debug/usr/lib64/libhylafax-6.0.so.3.debug
%{find_lang} %{name}-client
%{find_lang} %{name}-server
%{find_lang} lib%{name}

%pre
/usr/sbin/useradd -r -o -g uucp -u 33 -s /bin/bash -c "Facsimile agent" -d /var/spool/fax fax 2> /dev/null || :
/usr/sbin/usermod -g uucp -G dialout fax 2> /dev/null || :

%post
/bin/chown -f -R fax var/spool/fax/*

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{name}-server.lang
%doc COPYRIGHT README SuSE/README.SuSE TODO VERSION latex-cover-1.04 doc/RELEASENOTES-6.0.txt
%config /etc/init.d/hylafax
%dir /usr/lib/fax
%attr(700,root,root) /etc/cron.daily/suse.de-faxcron
#/usr/%_lib/libfaxserver*
/usr/lib/fax/faxgetty
/usr/lib/fax/faxsend
/usr/lib/fax/hfaxd
/usr/lib/fax/faxcover_example_sgi.ps
%config(noreplace) /usr/lib/fax/hfaxd.conf
/usr/lib/fax/lockname
/usr/lib/fax/ondelay
/usr/lib/fax/pagesend
%doc %{_mandir}/man5/hylafax-config.5f.gz
%doc %{_mandir}/man5/doneq.5f.gz
%doc %{_mandir}/man5/dialrules.5f.gz
%doc %{_mandir}/man5/hosts.hfaxd.5f.gz
%doc %{_mandir}/man5/hylafax-server.5f.gz
%doc %{_mandir}/man5/hylafax-info.5f.gz
%doc %{_mandir}/man5/hylafax-log.5f.gz
%doc %{_mandir}/man5/pagermap.5f.gz
%doc %{_mandir}/man5/pagesizes.5f.gz
%doc %{_mandir}/man5/recvq.5f.gz
%doc %{_mandir}/man5/sendq.5f.gz
%doc %{_mandir}/man5/hylafax-shutdown.5f.gz
%doc %{_mandir}/man5/status.5f.gz
%doc %{_mandir}/man5/tsi.5f.gz
%doc %{_mandir}/man5/typerules.5f.gz
%doc %{_mandir}/man5/xferfaxlog.5f.gz
%doc %{_mandir}/man8/choptest.8c.gz
%doc %{_mandir}/man8/cqtest.8c.gz
%doc %{_mandir}/man8/dialtest.8c.gz
%doc %{_mandir}/man8/faxabort.8c.gz
%doc %{_mandir}/man8/faxaddmodem.8c.gz
%doc %{_mandir}/man8/faxadduser.8c.gz
%doc %{_mandir}/man8/faxanswer.8c.gz
%doc %{_mandir}/man8/faxconfig.8c.gz
%doc %{_mandir}/man8/faxcron.8c.gz
%doc %{_mandir}/man8/faxdeluser.8c.gz
%doc %{_mandir}/man8/faxgetty.8c.gz
%doc %{_mandir}/man8/faxinfo.8c.gz
%doc %{_mandir}/man8/faxlock.8c.gz
%doc %{_mandir}/man8/faxmodem.8c.gz
%doc %{_mandir}/man8/faxq.8c.gz
%doc %{_mandir}/man8/faxqclean.8c.gz
%doc %{_mandir}/man8/faxquit.8c.gz
%doc %{_mandir}/man8/faxrcvd.8c.gz
%doc %{_mandir}/man8/faxsend.8c.gz
%doc %{_mandir}/man8/faxsetup.8c.gz
%doc %{_mandir}/man8/faxstate.8c.gz
%doc %{_mandir}/man8/faxwatch.8c.gz
%doc %{_mandir}/man8/hfaxd.8c.gz
%doc %{_mandir}/man8/jobcontrol.8c.gz
%doc %{_mandir}/man8/mkcover.8c.gz
%doc %{_mandir}/man8/notify.8c.gz
%doc %{_mandir}/man8/pagesend.8c.gz
%doc %{_mandir}/man8/pollrcvd.8c.gz
%doc %{_mandir}/man8/pdf2fax.8c.gz
%doc %{_mandir}/man8/ps2fax.8c.gz
%doc %{_mandir}/man8/recvstats.8c.gz
%doc %{_mandir}/man8/tagtest.8c.gz
%doc %{_mandir}/man8/tiff2fax.8c.gz
%doc %{_mandir}/man8/tiffcheck.8c.gz
%doc %{_mandir}/man8/tsitest.8c.gz
%doc %{_mandir}/man8/wedged.8c.gz
%doc %{_mandir}/man8/xferfaxstats.8c.gz
/usr/sbin/choptest
/usr/sbin/cqtest
/usr/sbin/dialtest
/usr/sbin/faxabort
/usr/sbin/faxaddmodem
/usr/sbin/faxadduser
/usr/sbin/faxanswer
/usr/sbin/faxconfig
%config(noreplace) %attr(700,root,root) /usr/sbin/faxcron
/usr/sbin/faxdeluser
/usr/sbin/faxinfo
/usr/sbin/faxlock
/usr/sbin/faxmodem
/usr/sbin/faxmsg
/usr/sbin/faxq
/usr/sbin/faxqclean
/usr/sbin/faxquit
/usr/sbin/faxsetup
/usr/sbin/faxsetup.bsdi
/usr/sbin/faxsetup.irix
/usr/sbin/faxsetup.linux
/usr/sbin/faxstate
/usr/sbin/faxwatch
/usr/sbin/probemodem
/usr/sbin/rchylafax
/usr/sbin/recvstats
/usr/sbin/tagtest
/usr/sbin/tiffcheck
/usr/sbin/tsitest
/usr/sbin/typetest
/usr/sbin/xferfaxstats
#dir /var/spool/fax
%dir %attr(0700,fax,uucp) /var/spool/fax/archive
%dir %attr(0755,fax,uucp) /var/spool/fax/bin
/var/spool/fax/bin/*
%dir %attr(0755,fax,uucp) /var/spool/fax/client
%dir %attr(0755,fax,uucp) /var/spool/fax/config
/var/spool/fax/config/*
%dir %attr(0755,fax,uucp) /var/spool/fax/dev
%dir %attr(0700,fax,uucp) /var/spool/fax/docq
%dir %attr(0700,fax,uucp) /var/spool/fax/doneq
%dir %attr(0755,fax,uucp) /var/spool/fax/etc
%config(noreplace) /var/spool/fax/etc/cover.templ
%config(noreplace) /var/spool/fax/etc/dialrules
%config(noreplace) /var/spool/fax/etc/dialrules.europe
%config(noreplace) /var/spool/fax/etc/dialrules.sf-ba
%config(noreplace) /var/spool/fax/etc/dpsprinter.ps
%config(noreplace) /var/spool/fax/etc/hosts.hfaxd
%config(noreplace) /var/spool/fax/etc/lutRS18.pcf
%config(noreplace) /var/spool/fax/etc/xferfaxlog
%config(noreplace) /var/spool/fax/etc/users
/var/spool/fax/etc/templates/
%dir %attr(0755,fax,uucp) /var/spool/fax/info
%dir %attr(0755,fax,uucp) /var/spool/fax/log
%dir %attr(0700,fax,uucp) /var/spool/fax/pollq
%dir %attr(0755,fax,uucp) /var/spool/fax/recvq
%dir %attr(0700,fax,uucp) /var/spool/fax/sendq
%dir %attr(0755,fax,uucp) /var/spool/fax/status
%dir %attr(0700,fax,uucp) /var/spool/fax/tmp
/var/spool/fax/COPYRIGHT
/var/spool/fax/FIFO

%files client -f hylafax-client.lang -f libhylafax.lang
%ifnarch aarch64
%{_libdir}/libhylafax*.so*
%endif
/usr/bin/faxalter
/usr/bin/faxcover
/usr/bin/faxmail
/usr/bin/faxrm
/usr/bin/faxstat
/usr/bin/sendfax
/usr/bin/sendpage
%dir /usr/lib/fax
/usr/lib/fax/a2pswrap
%config /usr/lib/fax/faxcover.ps
/usr/lib/fax/faxmail.ps
%config /usr/lib/fax/pagesizes
%config(noreplace) /usr/lib/fax/sendfax.conf
/usr/lib/fax/textfmt
%config /usr/lib/fax/typerules
/usr/lib/fax/typetest
/usr/sbin/edit-faxcover
%doc %{_mandir}/man1/edit-faxcover.1.gz
%doc %{_mandir}/man1/faxalter.1.gz
%doc %{_mandir}/man1/faxcover.1.gz
%doc %{_mandir}/man1/faxmail.1.gz
%doc %{_mandir}/man1/faxrm.1.gz
%doc %{_mandir}/man1/faxstat.1.gz
%doc %{_mandir}/man1/hylafax-client.1.gz
%doc %{_mandir}/man1/sendfax.1.gz
%doc %{_mandir}/man1/sendpage.1.gz
%doc %{_mandir}/man1/sgi2fax.1.gz
%doc %{_mandir}/man1/textfmt.1.gz

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 6.0.7
- Rebuilt for Fedora
* Mon Mar 28 2011 pth@suse.de
- Remove the -o option from call of hylafax in init script (bnc#632586).
- Remove the useless version dependency of the patches.
* Mon Mar 15 2010 ro@suse.de
- update to 6.0.4:
  * Page sent protocol trace fixes (2009-07-24)
  * Don't duplicate any file in a release tarball (2009-08-07)
  * IPv6: Rework initial bind (2009-08-07)
  * Some CVS-GIT cleanups/release notes (2009-08-14)
  * pagesend: Fix broken switch statement (2009-08-14)
  * hfaxd:  Cleanup uid initizliaztion and theoretical overflow (2009-08-14)
  * nls: Add German translation (2009-09-14)
  * PageHandling:  Fix handling of large blank areas (2009-09-18)
  * Add support for libtiff 3.9 (2007-11-21)
  * faxq: Don't assert on bad FIFO messages (2009-09-21)
  * Updated RPM dependencies (2009-09-25)
  * Str::vformat()  Don't reuse va_args (2009-10-07)
  * faxmail: Fix broken to address/name parsing (2009-10-29)
  * Update releasenotes and documentation re IPv6 support (2009-11-13)
  * hfaxd: log what address(es) we're listing on when starting (2009-11-13)
  * faxsend: Class1 1 ECM when skipping pages needs to be more careful (2009-11-13)
  * Class1: ECM page and block count should be sent as modulus. (2009-11-13)
* Fri Sep 18 2009 pth@suse.de
- Update to 6.0.3:
  HylaFAX 6.0 introduces several new features for HylaFAX:
  There are many additional features available:
  * PCL Support
  * hfaxd Can sort list output arbitrarily for clients
  * I18n: HylaFAX client strings are now translated and available in
    different languages
  * IPv6 support
  * New permissions in hfaxd to allow for more admin control on who can
    see/modify jobs/faxes (see PublicJobQ/JobProtection/PublicRecvQ)
  * Powerful page range handling capabilities
  * Better faxq/notify integration
  * Numerous fax modem/protocol fixes and enhancements
  In addition, the aging support for the unused "old protocol" has been
  removed.
  For detailed changes see /usr/src/packages/hylafax/RELEASENOTES-6.0.txt
- Add proper support for DESTDIR.
- Add german translation (will be part of the next release).
- Fix most compiler warnings.
- Add a rpmlintrc file.
- Repackage all tarballs with lzma.
- Various fixes for configure:
  * Ansify test code.
  * Make C++ test code use C compatibility headers (like cstdio)
  * Don't use rpath when installing in /usr/lib64
* Tue Jul 28 2009 lnussel@suse.de
- set permissions via %%attr
- remove timestamp from init script to make buildcompare work
* Sun Aug 17 2008 kkeil@suse.de
- update to 4.4.4
- fix init scpript
  CHANGES for 4.4.1
  * faxmail: don't submit an empty postscript file if not formatting was
  done (17 Aug 2007)
  * faxaddmodem doesn't fuser -k by default, allowing iaxmodem to be
  detected by faxaddmodem (17 Aug 2007)
  * fix status/statuscode parsing of the job qfile which showed artifacts
  in the notify emails (20 Aug 2007)
  * Fix faxmail handling of RFC 822 comments in headers  (21 Aug 2007)
  * Fix faxq handling of large formatter output (21 Aug 2007)
  * Fix configure GCC version detection for Gentoo (22 Aug 2007)
  * Fix faxq trigger handling (14 Sep 2007)
  CHANGES for 4.4.2
  * Fix configure GCC for broken Gentoo fix (23 Aug)
  * faxq: Suppress blocked notifies if job is already blocked (7 Sep 2007)
  * faxq: reduce copius scheduler logging (7 Sep 2007)
  * faxmail: fix suppression of empty postcript formatting file (10 Sep 2007)
  * faxmail: Fixed RFC 822 comment segfaults (14 Sep 2007)
  * faxq: Fixed multiple trigger issues (14 Sep 2007)
  * hfaxd: fix double 550 error code on access permisions (14 Sep 2007)
  * man pages: fix mulitple typos (17 Sep 2007)
  * Fix large SESSION_LOG variable causing bash problems (24 Sep 2007)
  CHANGES for 4.4.3
  * setSleep must be called before sending the notification if we want the
  right time to be passed to notify. (24 Oct 2007)
  * faxmail: Update man page/options to match again (6 Nov 2007)
  * prototype configs: typo in MT5600ZDX (9 Nov 2007)
  * Bug 875: faxsetup and faxaddmodem may forget locks and temporary files
  when exiting (13 Nov 2007)
  * hfaxd: Remove PAM debug logging (15 Nov 2007)
  * TypeRules: fix istring addition (15 Nov 2007)
  * faxmail: Don't pass non-plain text through the internal plain text
  formatter (11 Nov 2007)
  * xferfaxlog: Update man pages (20 Nov 2007)
  * Add support for libtiff 3.9 (21 Nov 2007)
  CHANGES for 4.4.4
  * faxq: Don't allow pending jobs with future TTS to block current jobs
  (11 Dec 2007, 19 Dec 2007)
* Sun Jun  8 2008 kkeil@suse.de
- fix conversion function to use correct parameter (bnc#392794)
* Tue Jul 31 2007 kkeil@suse.de
- move capi4hylafax in a extra source package
* Tue Jul 31 2007 kkeil@suse.de
- update to version 4.4.0
  * Stop caching of DATE and VERSION by configure (Bug 854) (9 Mar 2007)
  * Adds T.32 Addendum 1 Extended DF formats (12 Mar 2007)
  * Unify and simply FCF tracing routines (12 Mar 2007)
  * Pad TCS/CSI string to avoid Class2 modem bugs (12 Mar 2007)
  * Increase the wait time for AT+FCLASS=? response (12 Mar 2007)
  * Fix error of forgotton fxgetty child under flawed ECM
  * Stop using CRP in Phase D in Class 1 sending (12 Mar 2007)
  * Add BadPageHandlingMethod feature defauting to RTN-SAVE (12 Mar 2007)
  * Don't wait Class1TrainingRecovery when CRP was received (12 Mar 2007)
  * Don't trigger hasV17Trouble for pages other than the first (12 Mar 2007)
  * Fix error of sending a block twice, empty the 2nd time (12 Mar 2007)
  * Replace Class1TrainingRecovery with Class1SwitchingCmd
  * Simplify Class1SwitchingCmd code and prevent duplication of the
  command in session (12 Mar 2007)
  * Add Class1PageLengthSupport config option (12 Mar 2007)
  * Add Class1PageWidthSupport modem config option (12 Mar 2007)
  * Extend "awaiting ECM synchronization" timeout (12 Mar 2007)
  * Improve ECM HDLC frame decoder to recover more quickly from data corruption
  and possibly find frames where it couldn't before (12 Mar 2007)
  * Improve response handling of AT+FRH=3 (12 Mar 2007)
  * Calculate PPM/PPS waiter instead of using T1
  * We can't rely on the timeout value to know if CONNECT has been seen
  (12 Mar 2007)
  * Handle +FCERROR after most +FRH=3 commands (12 Mar 2007)
  * Restart Class 1 TCF reception timer after zeros start
  * Add more intelligence to the Class 1 receiver in sending RTN (12 Mar 2007)
  * Log correctly when a receiver DIS indicates no V.8 bit but
  V.8 was already known to have succeeded (12 Mar 2007)
  * Handle MPS/EOP/EOM/CRP when expecting DCS, i.e. after RTN
  * Handle instances where ECM is negotiated but the sender
  transmits non-ECM data and signalling (12 Mar 2007)
  * Bug 811: children should exit with _exit() (12 Mar 2007)
  * when dealing with JBIG/JPEG send PPR if we detect no frames
  received but we're still missing the last frame (12 Mar 2007)
  * Logging instances where a sender transmits PPS again after our fourth PPR
  signal (12 Mar 2007)
  * Add DTMF handling during call (12 Mar 2007)
  * Use DLE+DTX to help reseting when stuck in transmit (13 Mar 2007)
  * Recognize DTMF as caller id when waiting for rings (13 Mar 2007)
  * Force ECM when using V.8 (13 Mar 2007)
  * Prevent picking up again on the receiver's MCF signal when
  re-entering Phase B in a batch (13 Mar 2007)
  * Don't fallback to V.17 speeds on TCF retransmisions (13 Mar 2007)
  * Improve sender-side RNR/RR flow control interaction (13 Mar 2007)
  * Flush modem input after NO CARRIER result in Class 1 Phase C send
  (13 Mar 2007)
  * Fix send buffer when transmitting non-ECM data with a non-zero
  scanline-time value (13 Mar 2007)
  * Restrict the usage of sending EOR, even when using MH and MR (13 Mar 2007)
  * Improve and extend JPEG parsing (13 Mar 2007)
  * Improve Class 1 handling when prologue frames fail after EOM (13 Mar 2007)
  * Compensate for 1728 pixel data when they DCS signalled differently
  (13 Mar 2007)
  * Added the complete debian/ directory in order to create official
  Debian packages (17 Mar 2007)
  * Email raw TIFF files with the correct MIME type of image/tiff (23 Mar 2007)
  * Accepts 'original' as equivalent to 'raw' for RETURNFILETYPE (23 Mar 2007)
  * faxq scheduler overhaul for efficiency and batching (May 4 2007)
  * Faxmail overhaul - make handle documents independantly, just like
  sendfax (9 May 2007)
  * Change socklen_t configure/detection for HP-UX 11 (11 May 2007)
  * Add preliminary Class2 JBIG Support (11 May 2007)
  * Add JPEC (colour fax) to Class2 (12 May 2007)
  * Remove broken JobControlWait (23 July 2007)
* Thu May 24 2007 kkeil@suse.de
- cleanup spec file
* Thu May 24 2007 ro@suse.de
- added capi4linux-devel to buildreq
* Fri Mar 30 2007 ro@suse.de
- added pwdutils to buildreq
* Thu Dec  7 2006 kkeil@suse.de
- fix FaxDispatch to take the correct parameter (#212516)
* Tue Dec  5 2006 kkeil@suse.de
- capi4hylafax: security fix against executing arbitrary commands
  on the fax receiving system. CVE-2006-3126 (#203515)
* Thu Aug  3 2006 kkeil@suse.de
- update to version 4.3.0
  * Fix DCS tag handling in Class2 (BUG 771) (5 May 2006)
  * Fix hfaxd corruption on killed jobs (BUG 401) (5 May 2006)
  * More fixes to batching and jobcontrol interaction (3 May 2006)
  * Re-work fix for hfaxd's time handling (BUG 723) (28 Apr 2006)
  * Don't let users kill each other's jobs (BUG 752) (28 Apr 2006)
  * Use areBatchable() to make sure batching doesn't ignore job
  modems (28 Apr 2006)
  * Enhance Italian translation (BUG 758) (26 Apr 2006)
  * Fix faxq sleepq concurrency problem (BUG 745) (26 Apr 2006)
  * Fix runSchedule() concurrency problem (BUG 745) (26 Apr 2006)
  * Fix some of the error paths in the setReadyToRun jobcontrol
  pipe, fork, and exec calls (BUG 745) (25 Apr 2006)
  * Fix unblocking job problem (BUG 733) (24 Apr 2006)
  * back out flush modem I/O (BUG 756) (24 Apr 2006)
  * Make sure hfaxd returns JBIG faxes in recvq list (BUG 731) (23 Apr 2006)
  * Resolve Solaris bus error under native compiler (BUG 769) (23 Apr 2006)
  * Fix quoted-printable MIME encoding in faxrcvd (BUG 760) (21 Apr 2006)
  * Fix sendfax to accept both destination and user subaddresses
  (BUG 762) (21 Apr 2006)
  * Repair broken MMR from some Multitech modems (BUG 763) (21 Apr 2006)
  * Add JobControlWait to allow faxq to wait for JobControlCmd
  to finish synchronously (4 Apr 2006)
  * flush modem I/O on receptions before sending any data (03 Apr 2006)
  * fix incorrect "Fax protocol error" in ECM mode (03 Apr 2006)
  * add German NSFs and correct HylaFAX NSF bit order (03 Apr 2006)
  * set Class1RMPersistence to 0 in digi config prototype (03 Apr 2006)
  * extend V.21 HDLC frame reception timeout to 10 sec (03 Apr 2006)
  * ignore MESSAGE-WAITING response after dialing (02 Apr 2006)
  * Correctly remove EOFB at the end of MMR images (02,10 Apr 2006)
  * set minimum of 4800 for V.34 primary rate renegotiations (02 Apr 2006)
  * improve handling of V.34 control channel retrain (02 Apr 2006)
  * Add isdn4linux modem config prototype (02 Apr 2006)
  * Add IAXmodem config prototype (02 Apr 2006)
  * Update config.guess & config.sub (27 Mar 2006)
  * Add JobControl (obsoletes DestControl) (27 Mar 2006)
  * Fix hfaxd SNPP login code to 250 (Bug 732) (27 Mar 2006)
  * Fix hfaxd timezone handling on new GLIBC (BUG 723) (24 Mar 2006)
  * Fix locking of recvq tiff files (BUG 739) (23 Mar 2006)
  * fix batching of page jobs (23 Mar 2006)
  * expand Class1JBIGSupport to allow for differentiation
  between full, none, send, and receive support (17 Mar 2006)
  * remove QualifyCID in lieu of DynamicConfig RejectCall (15 Mar 2006)
  * fix buffer overrun in NSF parsing (21 Feb 2006)
  * add dictionary for notify, faxrcvd, and pollrcvd
  internationalization support (21 Feb 2006)
  * add CHARSET config option for mailing scripts (21 Feb 2006)
  * use To-Company and To-Name coverpage entries in the notification
  message if they are available to use (21 Feb 2006)
  * add support for libtiff-3.8 (31 Jan 2006)
  * use PDF in q-files when appropriate (30 Jan 2006)
  * fix configure in vsnprintf detection (30 Jan 2006)
  * fix segfault on some compilers where the rare occassion
  of receiving CTC instead of PPS occurs (30 Jan 2006)
  * fix rare occassion where TCF fails following an unexpected
  receipt of prologue frames (30 Jan 2006)
* Fri May 26 2006 schwab@suse.de
- Don't build as root.
- Use RPM_OPT_FLAGS.
- Don't strip binaries.
* Mon Mar 13 2006 kkeil@suse.de
- move log/debug files to none world writeable directory (#156975)
- fix faxaddmodem.capi script to produce a valid configfile
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 16 2006 kkeil@suse.de
- update to hylafax-4.2.5
  * security fixes (#119666, 140908)
* Mon Dec 19 2005 kkeil@suse.de
- update to hylafax-4.2.3
* Fri Aug 19 2005 kkeil@suse.de
- update capi4hylafax from beta to final version 01.03.00
* Thu Aug  4 2005 kkeil@suse.de
- capi4hylafax update to 01-02-91beta
* Thu Jun  2 2005 ro@suse.de
- rename faxcron to suse-faxcron for now
* Wed May 18 2005 kkeil@suse.de
- fix handling of return codes in hylafax mode (#80592)
* Mon Apr 25 2005 kkeil@suse.de
- more GCC4 fixes
* Sat Apr  9 2005 kkeil@suse.de
- fix GCC4 issues
* Wed Jan 26 2005 kkeil@suse.de
- a2pswrap should be only in hylafax-client
* Mon Jan 24 2005 kkeil@suse.de
- update to hylafax-4.2.1
- split haylafax into hylafax and hylafax-client
* Thu Oct 28 2004 kkeil@suse.de
- add tiff lib version 3.7 and 3.8 to configure test
* Tue Sep 21 2004 kkeil@suse.de
- need shareutils and metamail for correct build
* Mon Sep  6 2004 kkeil@suse.de
- better ASCII -> PS conversion (#44609)
* Tue Aug 31 2004 kkeil@suse.de
- readd in spec file fillup_and_insserv; deleted one line too much
* Tue Aug 31 2004 kkeil@suse.de
- update to hylafax-4.2.0
* Tue Aug 31 2004 kkeil@suse.de
- remove notify mail (#44371)
- remove wrong test in faxcron (#43038)
* Thu May  6 2004 kkeil@suse.de
- fix problem with connection abort on c2faxsend
  new NPTL sem_wait() is interruptible by signals (#40051)
- update README.SuSE, remove old stuff (#39789)
* Mon Apr 19 2004 ro@suse.de
- remove apache from neededforbuild
  (serverroot is hardcoded in specfile anyway ...)
* Fri Mar 26 2004 mmj@suse.de
- Add postfix to # neededforbuild
* Tue Mar  2 2004 kkeil@suse.de
- update to hylafax-4.1.8
* Wed Oct  8 2003 kkeil@suse.de
- fix hfaxd remote vulnerability due to format string bugs (#32036)
- fix ownership of preexistent hylafax FIFO files (#32136)
* Sat Sep 20 2003 kkeil@suse.de
- add useradd,usermod to PreReq (#31479)
* Mon Sep  8 2003 kkeil@suse.de
- fix owner of files under /var/spool/fax (#29610)
- use now the system user fax for hylafax
* Fri Aug 29 2003 kkeil@suse.de
- capi4hylafax update to the cvs version; many bugfixes
* Mon Aug 18 2003 kkeil@suse.de
- update to hylafax-4.1.7
* Tue Jul 29 2003 aj@suse.de
- Fix chown invocation.
* Fri May 30 2003 kkeil@suse.de
- fix wrong config files for FCLASS 2 setup (# 27129)
* Mon May 26 2003 kkeil@suse.de
- cleanup build tree and add missed files
* Fri May  9 2003 kkeil@suse.de
- Add URL to package capi4hylafax
* Tue Jan 21 2003 kkeil@suse.de
- update to hylafax-4.1.5
- update to capi4hylafax-01.02.02
* Mon Nov 25 2002 kkeil@suse.de
- fixes for 64 bit architectures
- finaly solve all va_list problems in capi4hylafax
* Thu Nov 14 2002 kkeil@suse.de
- fix problem in c2recvfax with receiving 2 fax at the same time
* Wed Nov 13 2002 kkeil@suse.de
- more fixes to setup scripts (#21116)
- add SuSE docu and setup scripts for capi4hylafax (#20767)
* Wed Nov  6 2002 kkeil@suse.de
- update capi4hylafax to 01.02.01, which includes all previous
  fixes and a solution for the va_list problem (#21741)
* Tue Oct 22 2002 kkeil@suse.de
- fix missing leading zeros in config files (#21116)
* Fri Oct 11 2002 kkeil@suse.de
- add AcceptGlobalCall option
* Tue Oct  8 2002 kkeil@suse.de
- fix problem with FaxDispatch wrong parameter was used
- remove not working va_list patch for capi4hylafax
* Mon Sep 23 2002 tcrhak@suse.cz
- be more strict in init script when
  killing faxq and hfaxd [bug #19235]
* Mon Sep  2 2002 meissner@suse.de
- Dropped va_list in va_list junk (this just does not work).
- Do not pass va_list*, but va_list directly to integer formatting.
- lib64 fixes
- fixed stdint.h inclusion for wordsize 64
* Tue Aug 20 2002 mmj@suse.de
- Correct PreReq
* Fri Aug  2 2002 tcrhak@suse.cz
- update to 4.1.3
- fixed bugs #12645 and #14771
* Fri Aug  2 2002 ro@suse.de
- adapted server root
* Sun Jul 28 2002 kukuk@suse.de
- Add capi4linux, remove libz
* Tue Jul 23 2002 kukuk@suse.de
- Fix neededforbuild (i4l is splittet)
* Mon Jul 15 2002 kkeil@suse.de
-  add capi4hylafax subpackage
* Thu Jul 11 2002 kkeil@suse.de
- if compiled with shared libs, it should also install them
* Fri Jun 28 2002 schwab@suse.de
- Fix building shared libraries.
- Fix conflicting types.
* Thu Jun 27 2002 tcrhak@suse.cz
- update to 4.1.2
- fixed for gcc 3.1
* Thu May 16 2002 meissner@suse.de
- va_list generates a pseudo block which we cannot goto over.
* Mon Feb 18 2002 ro@suse.de
- fixed init-script (status) (#13303)
* Fri Feb  1 2002 ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Mon Jan 14 2002 ro@suse.de
- removed START_HYLAFAX
* Wed Aug 29 2001 schwab@suse.de
- Don't use obsolete <osfcn.h>
- Fix conflicting types.
* Fri Aug 10 2001 dan@suse.cz
- man page fix (#9707)
* Wed Aug  8 2001 dan@suse.cz
- update to version 4.01
- installing documentation fixed
- font path fixed (#9662)
- spec file clean-up
* Fri Jul 20 2001 kukuk@suse.de
- changed neededforbuild <gs_x11> to <ghostscript-x11>
* Fri May  4 2001 pblaha@suse.cz
- place faxcron to /etc/cron.daily
* Mon Apr 23 2001 pblaha@suse.cz
- fix problem with permison of /usr/lib/fax/a2pswrap
- fix problem with /usr/lib/fax/faxsend
* Tue Apr 17 2001 kkeil@suse.de
- add some ISDN features (dispatch fax according MSN)
- example configs for I4L CLASS1 and CLASS2 modems
* Tue Apr 17 2001 stark@suse.de
- added insserv in %%post and %%postun (Bug #6487)
* Fri Feb 23 2001 ro@suse.de
- changed neededforbuild <apache> to <apache apache-devel>
* Thu Jan  4 2001 smid@suse.cz
- fixed startcript
- bzip sources
* Thu Nov 30 2000 ro@suse.de
- fixed startscript
* Fri Jul 28 2000 smid@suse.cz
- fix syntax error in faxcron script (bugzilla #3520)
* Thu Jul 13 2000 kasal@suse.de
- fixed possible bug if LC_ALL != C
* Mon Jul 10 2000 choeger@suse.de
- Bugfix for a2pswrap: tr command changed.
  seems to be more POSIX like
* Wed Jun 28 2000 kasal@suse.cz
- added tiff-3.5-interfaces.patch to build with new libtiff
- added twice "-type f" to faxcron script (fixes bug #2955)
* Mon Jun 26 2000 schwab@suse.de
- Fix test for compiler version.
- Add %%suse_update_config.
* Thu Apr 13 2000 ro@suse.de
- added mm to neededforbuild
* Wed Mar 15 2000 choeger@suse.de
- bugfix for typerules
  textfmt does not work anymore on SuSE Linux 6.4
  Don't know how to fix this, so I wrote a new
  ascii2ps called a2pswrap
* Tue Mar  7 2000 choeger@suse.de
- bugfixes for probemodem and faxaddmodem
- stty 0 does not work anymore, tried stty -clocal, works
- trap'ed sig 15 und tries to kill with TERM, what is not possible
  then, fixed
* Mon Mar  6 2000 choeger@suse.de
- removed optimization flag -O2, because with this
  option, hylafax won't work anymore with gpp-2.95.2
* Wed Mar  1 2000 choeger@suse.de
- added FIFO to rpm-package and removed it from postinstall
- changed manpath in config.site
* Wed Mar  1 2000 choeger@suse.de
- added %%{_mandir}
* Mon Jan 10 2000 ro@suse.de
- patched to accept libtiff v3.5
* Tue Jan  4 2000 choeger@suse.de
- y2k bugfix for xferfaxstats
* Fri Dec 17 1999 werner@suse.de
- Seems that SCRIPT_SH="/bin/bash -f" isn't a good idea because it
  will be used during package build: back to SCRIPT_SH="/bin/bash"
* Thu Dec 16 1999 werner@suse.de
- Make "any:.*" ModemGroup work for faxsetup (change
  awk FS from `:' to `\000')
- Use `bash -f' (noglob option) instead of plain bash
- Make xferfaxstats secure as done for the other scripts
- Within scripts use for EXIT a own trap for not changing
  exit status in a false matter.
- Remove temporary directory in faxcron script
  even if terminated within option handling.
- Force usage not only linkage of system libz
- Set GCOPTS and GCXXOPTS in specs to be able to use $RPM_OPT_FLAGS
- Say YES to configure :-)
- Host type is ${RPM_ARCH}-suse-linux
* Tue Oct  5 1999 choeger@suse.de
- new version (beta but necessary) 4.1beta2
* Mon Sep 20 1999 ro@suse.de
- added Provides: fax_daemon, Requires: smtp_daemon
* Mon Mar  1 1999 ro@suse.de
- added -D_GNU_SOURCE to GC++FLAGS for fds_bits and glibc-2.1
* Fri Dec 18 1998 choeger@suse.de
- just another faxcron-patch...
* Sun Dec 13 1998 choeger@suse.de
- applied a patch to make regex work under glibc,
  changed path to tiff-libs and -bins
* Fri Dec 11 1998 choeger@suse.de
- added some patches from hylafax.org
* Wed Dec  9 1998 choeger@suse.de
- made init-scripts complete
* Fri Nov 20 1998 choeger@suse.de
- added new init-script functionality
* Tue Nov 10 1998 ro@suse.de
- fixes to compile with egcs (ANSI-C++):
  if a function expects a function pointer,
    don't try to pass a function as argument
* Wed Sep 23 1998 choeger@suse.de
- fixes for /tmp racecondition
* Thu Sep 10 1998 choeger@suse.de
- fixed faxcron
* Wed Jul 29 1998 choeger@suse.de
- removed faxsurvey from the list of files, because
  of a security-hole
* Mon Jul 27 1998 choeger@suse.de
- fixed error in postinstall (leading slash)
* Tue Jul 21 1998 choeger@suse.de
- added -e to echo in init-script
* Mon Feb 23 1998 choeger@suse.de
- new version, v4.0pl2
* Tue Nov 18 1997 choeger@suse.de
- changed spec-file, because html-docu was not correctly installed
* Mon Nov 17 1997 choeger@suse.de
- now ready for autobuild and ready to run... :-)
* Mon Oct 20 1997 ro@suse.de
- ready for autobuild
* Tue Oct  7 1997 choeger@suse.de
- created .spec file
* Wed Jul  9 1997 choeger@suse.de
- fixed uucp-locking misconfiguration (config.site)
* Mon Jul  7 1997 choeger@suse.de
- new package with directory-fix
* Tue Jul  1 1997 choeger@suse.de
- new package with fixed faxaddmodem and faxsetup
  scripts ( uid <-> gid problem )
* Wed Jun  4 1997 choeger@suse.de
- new package with new README.SuSE that points to the behaviour
  of the fax and uucp uid problem
* Sun Jun  1 1997 bs@suse.de
- moved fillup stuff to var/adm/fillup-templates
- fixed doinst.sh for installion not in running system
* Fri May 30 1997 choeger@suse.de
- built new package because of new location of httpd/cgi-bin
  - > /usr/local/httpd/cgi-bin
* Mon May  5 1997 choeger@suse.de
- added latex-cover v1.03 to the binary distribution
* Tue Apr 22 1997 choeger@suse.de
- by the fact that the newer version of mgetty now seems to work
  with faxgetty, I recompiled it with Adaptive Answer Support in
  combination with mgetty
* Tue Feb 25 1997 choeger@suse.de
- new package, v4.0pl1
