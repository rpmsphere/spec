Name:           hxtools
Version:        20180301
Release:        1.1
Summary:        Collection of day-to-day tools (binaries)
License:        GPL-2.0+ and WTFPL
Group:          Productivity/Other
Url:            http://inai.de/projects/hxtools/
Source:         http://jftp.inai.de/hxtools/%name-%version.tar.xz
Source2:        http://jftp.inai.de/hxtools/%name-%version.tar.asc
Source3:        %name.keyring
BuildRequires:  bdftopcf
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel >= 2
BuildRequires:  xz
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  pkgconfig(libHX) >= 3.17
#BuildRequires:  pkgconfig(libpci) >= 3
BuildRequires:  pkgconfig(mount) >= 2.20
BuildRequires:  pkgconfig(xcb) >= 1

%define build_profile 1
%define hldir %_libexecdir/%name

%description
A collection of various tools. Some of the important ones:

* declone(1) — break hardlinks
* fd0ssh(1) — pipe for password-over-stdin support to ssh
* ofl(1) — open file lister (replaces fuser and lsof -m)
* tailhex(1) — hex dumper with tail-following support
* utmp_register(1) — make entries in the utmp/wtmp database
* vfontas(1) — VGA font file assembler

%package scripts
Summary:        Collection of day-to-day tools (scripts)
Group:          Productivity/Other
BuildArch:      noarch
Requires:       %name
Recommends:     %name-man
Requires:       perl(Data::Dumper)
Requires:       perl(File::Find)
Requires:       perl(File::Find::Rule)
Requires:       perl(Getopt::Long)
Requires:       perl(IPC::Open2)
Requires:       perl(Text::CSV_XS)

%description scripts
Architecture-independent programs from hxtools.

* checkbrack(1) — check parenthesis and bracket count
* cwdiff(1) — run wdiff with color
* diff2php(1) — transform patch to self-serving PHP file
* doxygen-kerneldoc-filter(1) — filter for Doxygen to support kerneldoc
* filenameconv(1) — convert file name encoding
* fnt2bdf(1) — convert VGA raw fonts to X11 BDF
* git-author-stat(1) — show commit author statistics of a git repository
* git-export-patch(1) — produce perfect patch from git comits for mail submission
* git-forest(1) — display the commit history forest
* git-revert-stats(1) — show reverting statistics of a git repository
* git-track(1) — set up branch for tracking a remote
* man2html(1) — convert nroff manpages to HTML
* pegrep(1) — perl-regexp-based multi-line grep
* pesubst(1) — perl-regexp-based stream substitution (replaces sed for substitutions)
* recursive_lower(1) — recursively lowercase all filenames
* spec-beautifier(1) — program to clean up RPM .spec files
* vcsaview(8) — display a screen dump in VCSA format
* wktimer(1) — work timer

%package man
Summary:        Manual pages for the hxtools suite
Group:          Documentation/Man
BuildArch:      noarch

%description man
This package contains the manual pages for the binaries and scripts
from hxtools.

%package data
Summary:        Collection of day-to-day tools (data)
Group:          Productivity/Other
BuildArch:      noarch

%description data
Architecture-independent data from hxtools.

* VAIO U3 keymap
* additional fonts for console and xterm
* additional syntax highlighting definitions for mcedit

%package profile
Summary:        The hxtools shell environment
Group:          Productivity/Other
Requires:       %name = %version
Requires:       %name-data = %version
Requires:       %name-scripts = %version
BuildArch:      noarch

%description profile
Bash environment settings from hxtools. Particularly, this provides
the SUSE 6.x ls color scheme, and a reduced PS1 that shows only the
rightmost parts of a path.

%package -n sysinfo
Summary:        System diagnosis tools from hxtools
Group:          System/Base

%description -n sysinfo
This subpackage contains programs from the hxtools suite that
give info about available system components.

* clock_info(1) – show available system clocks for clock_gettime(2)
* pmap_dirty(1) — display amount of RAM a process uses hard
* sysinfo(1) — print IRC-style system information banner

%package -n fd0ssh
Summary:        Helper program for using a pipe for SSH authentication
Group:          System/Base

%description -n fd0ssh
fd0ssh a helper program used by non-interactive programs, for example
pam_mount, that want to pipe a password to ssh.

%package -n ofl
Summary:        Open File Lister from hxtools
Group:          System/Base

%description -n ofl
ofl lists processes (and can send signals to them) that have
directories or files in specific locations in use. It differs from
lsof/fuser in that it can scan recursively and won't bluntly look at
an entire mount.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
b="%buildroot"
mv "$b/%_bindir/rot13" "$b/%_libexecdir/%name/"
install -dm0755 "$b/%_datadir/mc/syntax"
install -pm0644 cooledit/*.syntax "$b/%_datadir/mc/syntax/"
install -dm0755 "$b/%_sysconfdir/openldap/schema"
ln -s "%_datadir/hxtools/rfc2307bis-utf8.schema" \
	"$b/%_sysconfdir/openldap/schema/"

%if 0%{?build_profile}
mkdir -p "$b/%_sysconfdir/bashrc.d"
ln -s "%_datadir/%name/hxtools_bashrc.bash" "$b/%_sysconfdir/bashrc.d/"
mkdir -p "$b/%_sysconfdir/profile.d"
ln -s "%_datadir/%name/hxtools_profile.bash" "$b/%_sysconfdir/profile.d/z_hxtools_profile.sh"
%else
rm -Rf "$b/%_sysconfdir/profile.d" "$b/%_sysconfdir"/hx*
%endif

%files
%doc LICENSE*
%_bindir/bin2c
%_bindir/clt2bdf
%_bindir/declone
%_bindir/gxxdm
%_bindir/hcdplay
%_bindir/tailhex
%_bindir/xcp
%dir %hldir
%hldir/bsvplay
%hldir/cctypeinfo
%hldir/clt2pbm
%hldir/pcmdiff
%hldir/peicon
%hldir/proc_iomem_count
%hldir/proc_stat_parse
%hldir/psthreads
%hldir/qplay
%hldir/rot13
%hldir/utmp_register
%hldir/vfontas

%files scripts
%_bindir/aumeta
%_bindir/checkbrack
%_bindir/cwdiff
%_bindir/fxterm
%_bindir/git-*
%_bindir/gpsh
%_bindir/man2html
%_bindir/mkvappend
%_bindir/pegrep
%_bindir/pesubst
%_bindir/qpdecode
%_bindir/qtar
%_bindir/spec-beautifier
%_bindir/ssa2srt
%_bindir/su1
%_bindir/wktimer
%dir %hldir
%hldir/diff2php
%hldir/doxygen-kerneldoc-filter
%hldir/extract_*
%hldir/fnt2bdf
%hldir/git-*
%hldir/ldif-duplicate-attrs
%hldir/ldif-leading-spaces
%hldir/logontime
%hldir/mailsplit
%hldir/mod2opus
%hldir/recursive_lower
%hldir/rezip
%hldir/shared.pm
%hldir/sourcefuncsize
%hldir/stxdb
%hldir/vcsaview

%files man
%doc %_mandir/man*/*
%exclude %_mandir/man*/fd0ssh.1*
%exclude %_mandir/man*/ofl.1*

%files data
%dir %_sysconfdir/openldap
%dir %_sysconfdir/openldap/schema
%config %_sysconfdir/openldap/schema/*
%_datadir/%name
%_datadir/kbd
%_datadir/fonts/misc
%_datadir/mc

%if 0%{?build_profile}

%files profile
%config %_sysconfdir/hxloginpref.conf
%dir %_sysconfdir/bashrc.d
%config %_sysconfdir/bashrc.d/*
%config %_sysconfdir/profile.d/*
%endif

%files -n fd0ssh
%defattr(-,root,root)
%dir %hldir
%hldir/fd0ssh
%_mandir/man1/fd0ssh.1*

%files -n ofl
%_bindir/ofl
%_mandir/man1/ofl.1*

%files -n sysinfo
%_bindir/clock_info
%_bindir/pmap_dirty
%_bindir/sysinfo
%dir %hldir
%hldir/hxnetload
%hldir/paddrspacesize
%hldir/proc_stat_signal_decode

%changelog
* Thu Mar  1 2018 jengelh@inai.de
- Update to new upstream release 20180301
  * aumeta: handle containers other than mp4
  * spec-beautifier: escape { in regexes for Perl 5.26 fitness
* Sun Apr 30 2017 jengelh@inai.de
- Update to new upstream release 20170430
  * build: make build result time-invariant
  * sysinfo: avoid printing garbage display sizes
* Sat Jan 14 2017 jengelh@inai.de
- Update to new upstream release 20170114
  * Drop old utilities: orec, oplay, omixer, git-export-patch,
  googtts
  * Added manpages for: aumeta, pegrep, rezip
  * psthreads: display subthreads and subprocesses in different
  color
* Mon Jan  9 2017 jengelh@inai.de
- Update to new upstream release 20170109
  * A new utility "gxxdm" was added which explains libstdc++v3
  mangled names in detail. (Not feature-complete.)
  * New utility "ldif-duplicate-attrs": counts multiple occurrences
  of an attribute within one DN leaf and reports them.
  * New utility "ldif-leading-spaces": reports if LDAP attribute
  values start or end with whitespaces. (Spaces have implications
  for sorting addressbook entries, for example.)
  * New utilities: pegrep (a multiline pcregrep), qpdecode
  (quoted-printable filter), settime.pl (set filetime according
  to oldest archive member)
  * move_moov was renamed to aumeta
  * Removed utilities: git-new-root (git implements this itself
  easily now)
* Wed Mar  4 2015 jengelh@inai.de
- Update to new upstream release 20150304
  * bin2c: improve coding efficiency of Ultra mode
  * bin2c: improve runtime by 30%%
* Sat Feb 21 2015 jengelh@inai.de
- Update to new upstream release 20150221
  * diff2php: escape <? in plain text output
  * diff2php: fix wrong placement of HTML tags
* Fri Feb 20 2015 jengelh@inai.de
- Update to new upstream release 20150220
  * sysinfo: parse info from /etc/os-release
  * gpsh: do not sort the queue at all when -z is given
  * qtar: account for changed tar behavior due to
  Base:System/tar's new tar-recursive--files-from.patch
* Wed Nov 12 2014 jengelh@inai.de
- Update to new upstream release 20141112
  * Removed fduphl (replaced by hardlink(1))
  * New utility "rezip" to recompress ZIP archives recursively with
  maximum settings
  * New utility "move_moov" to call ffmpeg for moving MOOV section of
  MP4 to the front for enabling streaming
  * bin2c gained a -D option for directory prefix prepending
* Thu Jul  3 2014 jengelh@inai.de
- Update to new upstream release 20140703
  * New utilities: clt2pbm, clt2bdf/clt2sfd, cltscale
- Remove remove-conflicting-types.diff (merged upstream)
* Thu Apr  3 2014 dmueller@suse.com
- add remove-conflicting-types.diff, fixes build
  failure on aarch64
* Tue Mar 25 2014 jengelh@inai.de
- Update to new upstream release 20140325
  * bin2c now supports the -p option to strip paths
  * bin2c also defaults to stripping all leading paths
- Drop support for old distros in .spec file
* Wed Feb 12 2014 idonmez@suse.com
- Package license files.
* Tue Feb 11 2014 coolo@suse.com
- change WTFPL license to new spelling
* Sun Dec 22 2013 jengelh@inai.de
- Update to new upstream release 20131222
  * New utilities: bin2c (replaces png2wx), peicon
* Wed Jun  5 2013 jengelh@inai.de
- Update to new upstream release 20130605
  * ru-translit-de scim-table replaced by ru-phonde M17N mdbIM
  * hcdplay: new utility for control of analog CDROM playback
  * cp437AB font: Czech and Polish support/maps
* Tue Nov 27 2012 sbrabec@suse.cz
- Verify GPG signature
* Sun Nov 25 2012 jengelh@inai.de
- Update to new upstream release 20121125
  * Enhance cp437AB.uni to support the Unicode quotation marks
* Tue Nov 20 2012 jengelh@inai.de
- Update to new upstream release 20121121
  * profile: have hxpref_cd relay complaints if HOME is unset
  * new screenfonts A1.fnt, B1.fnt with unimap cp437AB.uni
  * vfontas: add -G option for 8x16->9x16 conversion
  * gpsh: support index exclusion
* Mon Oct 22 2012 cfarrell@suse.com
- license update: GPL-2.0+ and SUSE-WTFPL-2.0
  Use tags from the list linked at license.opensuse.org
* Wed Aug  1 2012 jengelh@inai.de
- Update to new upstream release 20120802
  * sysinfo: do count tmpfs files as memory used
- Split some tools into separate package so that they are
  installable independently (benefit to e.g. pam_mount)
* Mon May 14 2012 jengelh@inai.de
- Update to new upstream release 20120514
  * add statparse.pl (parse numbers from /proc/X/stat)
  * printcaps: support new capabilities as of Linux 3.2
  * sysinfo: avoid counting disks multiple times
  * googtts: automatically split long text into multiple HTTP reqs
* Mon Mar 12 2012 cfarrell@suse.com
- license update: GPL-2.0+
  spec file license should be in SPDX (compatible) format. GPL-2.0+ seems
  to be the most appropriate license choice for the resulting binary (no
  GPL-3.0 except for as choice in dual license situation)
* Sat Feb 25 2012 jengelh@medozas.de
- Avoid fdupes-induced hardlink across partitions
* Sat Jan  7 2012 jengelh@medozas.de
- Update to new upstream release 20120107
  * make `qtar -x` ignore CVS directories as well
  * gpsh: -OM option for passthrough of mplayer options
  * gpsh: make -l option functional again
  * gpsh: print extra status messages
  * printcaps: allow lookup by PID
  * clock_info: new tool
* Sun Dec  4 2011 jengelh@medozas.de
- Update to new upstream release 20111204
  * update code for libHX 3.12 API
  * git-forest: work together with git 1.7.7 rebases
  * gpsh: massively speed up reading index file
  * ssa2srt: new utility
* Mon Aug 29 2011 aj@suse.de
- clone needs _GNU_SOURCE defined to be visible (patch
  hxtools-fix-clone.patch)
* Thu Jul 21 2011 jengelh@medozas.de
- Update to hxtools-20110721
  * all: include libHX_CFLAGS to avoid build abort due to missing -I
  * ofl: define _GNU_SOURCE to avoid build abort
* Sat May 21 2011 jengelh@medozas.de
- Update to hxtools-20110509
  * phased out and/or removed obsolete scripts
- Update dependencies on Perl modules
* Mon Feb 14 2011 jengelh@medozas.de
- Update to hxtools-20110214
  * obsolete scripts removed
  * documentation updates
- Split package up further into binary, -scripts, -man, and avoid
  using Recommends: hxtools-data, because zypper defaults to
  pulling it in by default
* Tue Dec 21 2010 jengelh@medozas.de
- Initial package for build.opensuse.org
