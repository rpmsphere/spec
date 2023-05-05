%define dashedver %(echo %{version} |sed -e 's,\\.,-,g')

# Build system doesn't generate debugsources (but does generate debuginfo)
%define _empty_manifest_terminate_build 0

Name: schilytools
Version: 2021.09.18
Release: 3
Source0: https://nav.dl.sourceforge.net/project/schilytools/schily-%{dashedver}.tar.bz2
Summary: Replacements for common tools that resemble their Solaris counterparts
URL: http://schilytools.sourceforge.net/
License: Various Open Source Licenses (CDDL.Schily, GPL-2.0, LGPL-2.1, BSD)
Group: Archiving/Cd burning
BuildRequires: libcap-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
Obsoletes: cdrkit < 1.1.11-11
Obsoletes: cdrkit-genisoimage < 1.1.11-11
Provides: cdrtools smake btcflash
BuildRequires: recode

%description
Schily-Tools are a set of tools developed or maintained by Joerg Schilling.

Cdrtools is a set of command line programs that allows to record CD/DVD/BluRay media.
The suite includes the following programs:
  cdrecord  A CD/DVD/BD recording program 
  readcd    A program to read CD/DVD/BD media with CD-clone features 
  cdda2wav  The most evolved CD-audio extraction program with paranoia support 
  mkisofs   A program to create hybrid ISO-9660/Joliet/HFS filesystems
            with optional Rock Ridge attributes 
  isodebug  A program to print mkisofs debug information from media 
  isodump   A program to dump ISO-9660 media 
  isoinfo   A program to analyse/verify ISO-9660/Joliet/Rock-Ridge filesystems 
  isovfy    A program to verify the ISO-9660 structures 
  rscsi     A Remote SCSI enabling daemon
Star is an alternative implementation of the tar command.
Smake is powerful, but not compatible with GNU make (which is used by just about everything).
BTCflash is a Flash tool for BTC CD drives.

%prep
%autosetup -p1 -n schily-%{dashedver}
sed -i -e 's,^INS_BASE=.*,INS_BASE=%{_prefix},g' DEFAULTS/*
sed -i -e 's,-noclobber,,' cdrecord/Makefile.dfl

# Get rid of old ISO-8859-1 encoded umlaut characters
find . -name "*.c" -o -name "*.h" -o -name "*README*" -type f |xargs recode ISO-8859-1..UTF-8

# Remove lib*/*_p.mk to skip the compilation of profiled libs
rm -f lib*/*_p.mk
%ifarch %ix86
# doesnt work with clang on i586
sed -i -e 's,^DEFCCOM=.*,DEFCCOM=gcc,g' DEFAULTS/*
%endif

# We can specify LINKMODE="dynamic" here, but it just causes
# dynamic linking to libraries not used anywhere outside of
# schily world - so linking them statically is probably better
MAKEPROG=gmake make RUNPATH="" COPTOPT="%{optflags}" LDOPTX="" SCCS_BIN_PRE="" SCCS_HELP_PRE="" config

%build
# The Makefile system isn't 100% ready for an SMP build -- can't use -j
MAKEPROG=gmake make RUNPATH="" COPTOPT="%{optflags}" LDOPTX="" SCCS_BIN_PRE="" SCCS_HELP_PRE="" all

%install
MAKEPROG=gmake make RUNPATH="" COPTOPT="%{optflags}" LDOPTX="" SCCS_BIN_PRE="" SCCS_HELP_PRE="" DESTDIR="%{buildroot}" INS_BASE="%{_prefix}" install

# We don't need any Solaris-isms in our filesystem...
# Kill dupes
rm %{buildroot}%{_prefix}/xpg4/bin/{make,sh,od}
# And move the rest to a more reasonable place
mv %{buildroot}%{_prefix}/xpg4/bin/* %{buildroot}%{_prefix}/ccs/bin/* %{buildroot}%{_bindir}
rmdir %{buildroot}%{_prefix}/xpg4/bin %{buildroot}%{_prefix}/ccs/bin
rmdir %{buildroot}%{_prefix}/xpg4 %{buildroot}%{_prefix}/ccs

%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/*.so* %{buildroot}%{_libdir}
%endif

# Not much of a point in shipping static libs and headers for libs used
# only by cdrtools
rm -rf \
	%{buildroot}%{_prefix}/lib/*.a \
	%{buildroot}%{_includedir}

# The libraries/headers aren't installed, so we don't need their man
# pages either
rm -rf %{buildroot}%{_mandir}/man3

# Don't conflict with standard tools
# The tools are still available via their s* name
for i in make tar gnutar sh diff ctags isodebug isodump isoinfo isovfy cal od printf patch compare help translit spax lndir bsh count calc rmt mkhybrid mkisofs scpio star; do
  if [ -f %{buildroot}%{_bindir}/$i ] ; then
    mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i-schily
  elif [ -f %{buildroot}%{_sbindir}/$i ] ; then
    mv %{buildroot}%{_sbindir}/$i %{buildroot}%{_sbindir}/$i-schily
  fi
  if [ -f %{buildroot}%{_mandir}/man1/$i.1 ] ; then
    mv %{buildroot}%{_mandir}/man1/$i.1 %{buildroot}%{_mandir}/man1/$i-schily.1
  elif [ -f %{buildroot}%{_mandir}/man8/$i.8 ] ; then
    mv %{buildroot}%{_mandir}/man8/$i.8 %{buildroot}%{_mandir}/man8/$i-schily.8
  fi
done
mv %{buildroot}%{_prefix}/lib/cpp %{buildroot}%{_prefix}/lib/cpp-schily

%post
%{_sbindir}/setcap cap_sys_resource,cap_dac_override,cap_sys_admin,cap_sys_nice,cap_net_bind_service,cap_ipc_lock,cap_sys_rawio+ep %{_bindir}/cdrecord
%{_sbindir}/setcap cap_dac_override,cap_sys_admin,cap_sys_nice,cap_net_bind_service,cap_sys_rawio+ep %{_bindir}/cdda2mp3
%{_sbindir}/setcap cap_dac_override,cap_sys_admin,cap_sys_nice,cap_net_bind_service,cap_sys_rawio+ep %{_bindir}/cdda2ogg
%{_sbindir}/setcap cap_dac_override,cap_sys_admin,cap_sys_nice,cap_net_bind_service,cap_sys_rawio+ep %{_bindir}/cdda2wav
%{_sbindir}/setcap cap_dac_override,cap_sys_admin,cap_net_bind_service,cap_sys_rawio+ep %{_bindir}/readcd

%files
%{_bindir}/*-schily
%{_sbindir}/*-schily
%{_mandir}/man?/*-schily.*
%{_prefix}/lib/cpp-schily
#
%{_sysconfdir}/sformat.dat
%{_bindir}/cdrecord
%{_bindir}/cdda2mp3
%{_bindir}/cdda2ogg
%{_bindir}/cdda2wav
#{_bindir}/isodebug
#{_bindir}/isodump
#{_bindir}/isoinfo
#{_bindir}/isovfy
%{_bindir}/readcd
#{_bindir}/mkisofs
#{_bindir}/mkhybrid
%{_sbindir}/mountcd
%{_sbindir}/rscsi
%{_datadir}/lib/siconv
%{_sysconfdir}/default/cdrecord
%{_sysconfdir}/default/rscsi
%doc %{_docdir}/mkisofs
%doc %{_docdir}/libparanoia
%doc %{_docdir}/rscsi
%doc %{_docdir}/cdda2wav
%doc %{_docdir}/cdrecord
%{_mandir}/man1/cdda2mp3.1*
%{_mandir}/man1/cdda2ogg.1*
%{_mandir}/man1/cdda2wav.1*
%{_mandir}/man1/cdrecord.1*
#{_mandir}/man8/isodebug.8*
#{_mandir}/man8/isodump.8*
#{_mandir}/man8/isoinfo.8*
#{_mandir}/man8/isovfy.8*
#{_mandir}/man8/mkhybrid.8*
#{_mandir}/man8/mkisofs.8*
#
%doc %{_docdir}/rmt
%doc %{_docdir}/star
%config(noreplace) %{_sysconfdir}/default/rmt
%config(noreplace) %{_sysconfdir}/default/star
#{_sbindir}/rmt
#{_bindir}/scpio
#{_bindir}/star
%{_bindir}/suntar
%{_bindir}/star_sym
%{_bindir}/strar
#{_mandir}/man1/rmt.1*
#{_mandir}/man1/scpio.1*
#{_mandir}/man1/star.1*
%{_mandir}/man1/suntar.1*
%{_mandir}/man1/star_sym.1*
%{_mandir}/man1/strar.1*
#
%{_libdir}/libmakestate.so*
%{_bindir}/smake
%{_mandir}/man1/smake.1*
%{_mandir}/man5/makefiles.5*
%{_mandir}/man5/makerules.5*
%{_datadir}/lib/make
%{_datadir}/lib/smake
#
%{_bindir}/btcflash
%{_mandir}/man1/btcflash.1*
#
%{_bindir}/Cstyle
%{_bindir}/admin
%{_bindir}/bdiff
%{_bindir}/bosh
#{_bindir}/bsh
#{_bindir}/cal
#{_bindir}/calc
%{_bindir}/calltree
%{_bindir}/cdc
%{_bindir}/change
%{_bindir}/comb
#{_bindir}/compare
%{_bindir}/copy
#{_bindir}/count
%{_bindir}/cstyle.js
#{_bindir}/ctags
%{_bindir}/delta
%{_bindir}/devdump
#{_bindir}/diff
%{_bindir}/dmake
%{_bindir}/fdiff
%{_bindir}/fifo
%{_bindir}/fsdiff
%{_bindir}/get
%{_bindir}/hdump
#{_bindir}/help
%{_bindir}/jsh
%{_bindir}/krcpp
%{_bindir}/label
#{_bindir}/lndir
%{_bindir}/man2html
%{_bindir}/match
%{_bindir}/mdigest
%{_bindir}/mt
%{_bindir}/obosh
#{_bindir}/od
%{_bindir}/opatch
%{_bindir}/p
%{_bindir}/pbosh
%{_bindir}/pfbsh
%{_bindir}/pfsh
#{_bindir}/printf
%{_bindir}/prs
%{_bindir}/prt
%{_bindir}/pxupgrade
%{_bindir}/rcs2sccs
%{_bindir}/rmchg
%{_bindir}/rmdel
%{_bindir}/sact
%{_bindir}/sccs
%{_bindir}/sccscvt
%{_bindir}/sccsdiff
%{_bindir}/sccslog
%{_bindir}/sccspatch
%{_bindir}/scgcheck
%{_bindir}/scgskeleton
%{_bindir}/scut
%{_bindir}/sdd
%{_bindir}/sfind
%{_bindir}/sformat
%{_bindir}/sgrow
%{_bindir}/smt
%{_bindir}/spaste
%{_bindir}/spatch
#{_bindir}/spax
%{_bindir}/svr4.make
%{_bindir}/tartest
%{_bindir}/termcap
#{_bindir}/translit
%{_bindir}/udiff
%{_bindir}/unget
%{_bindir}/ustar
%{_bindir}/val
%{_bindir}/vc
%{_bindir}/vctags
%{_bindir}/ved
%{_bindir}/ved-e
%{_bindir}/ved-w
%{_bindir}/what
%{_prefix}/etc/termcap
#{_prefix}/lib/cpp
%{_prefix}/lib/diffh
%{_prefix}/lib/help/locale/C/ad
%{_prefix}/lib/help/locale/C/bd
%{_prefix}/lib/help/locale/C/cb
%{_prefix}/lib/help/locale/C/cm
%{_prefix}/lib/help/locale/C/cmds
%{_prefix}/lib/help/locale/C/co
%{_prefix}/lib/help/locale/C/de
%{_prefix}/lib/help/locale/C/default
%{_prefix}/lib/help/locale/C/ge
%{_prefix}/lib/help/locale/C/he
%{_prefix}/lib/help/locale/C/pr
%{_prefix}/lib/help/locale/C/prs
%{_prefix}/lib/help/locale/C/rc
%{_prefix}/lib/help/locale/C/sc
%{_prefix}/lib/help/locale/C/un
%{_prefix}/lib/help/locale/C/ut
%{_prefix}/lib/help/locale/C/va
%{_prefix}/lib/help/locale/C/vc
%{_prefix}/lib/svr4.make
%{_docdir}/bosh
%{_docdir}/bsh
%{_docdir}/ved
%{_mandir}/de/man1/sdd.1*
%{_mandir}/help/ved.help
%{_mandir}/man1/admin.1*
%{_mandir}/man1/bdiff.1*
%{_mandir}/man1/bosh.1*
#{_mandir}/man1/bsh.1*
#{_mandir}/man1/cal.1*
#{_mandir}/man1/calc.1*
%{_mandir}/man1/calltree.1*
%{_mandir}/man1/cdc.1*
%{_mandir}/man1/change.1*
%{_mandir}/man1/comb.1*
#{_mandir}/man1/compare.1*
%{_mandir}/man1/copy.1*
#{_mandir}/man1/count.1*
%{_mandir}/man1/cstyle.1*
%{_mandir}/man1/delta.1*
#{_mandir}/man1/diff.1*
%{_mandir}/man1/dmake.1*
%{_mandir}/man1/fdiff.1*
%{_mandir}/man1/fifo.1*
%{_mandir}/man1/fsdiff.1*
%{_mandir}/man1/get.1*
%{_mandir}/man1/hdump.1*
#{_mandir}/man1/help.1*
%{_mandir}/man1/jsh.1*
%{_mandir}/man1/krcpp.1*
%{_mandir}/man1/label.1*
#{_mandir}/man1/lndir.1*
%{_mandir}/man1/man2html.1*
%{_mandir}/man1/match.1*
%{_mandir}/man1/mdigest.1*
%{_mandir}/man1/mountcd.1*
%{_mandir}/man1/mt.1*
%{_mandir}/man1/obosh.1*
#{_mandir}/man1/od.1*
%{_mandir}/man1/opatch.1*
%{_mandir}/man1/p.1*
#{_mandir}/man1/patch.1*
%{_mandir}/man1/pbosh.1*
%{_mandir}/man1/pfbsh.1*
%{_mandir}/man1/pfsh.1*
#{_mandir}/man1/printf.1*
%{_mandir}/man1/prs.1*
%{_mandir}/man1/prt.1*
%{_mandir}/man1/pxupgrade.1*
%{_mandir}/man1/rcs2sccs.1*
%{_mandir}/man1/readcd.1*
%{_mandir}/man1/rmdel.1*
%{_mandir}/man1/rscsi.1*
%{_mandir}/man1/sact.1*
%{_mandir}/man1/sccs-add.1*
%{_mandir}/man1/sccs-admin.1*
%{_mandir}/man1/sccs-branch.1*
%{_mandir}/man1/sccs-cdc.1*
%{_mandir}/man1/sccs-check.1*
%{_mandir}/man1/sccs-clean.1*
%{_mandir}/man1/sccs-comb.1*
%{_mandir}/man1/sccs-commit.1*
%{_mandir}/man1/sccs-create.1*
%{_mandir}/man1/sccs-cvt.1*
%{_mandir}/man1/sccs-deledit.1*
%{_mandir}/man1/sccs-delget.1*
%{_mandir}/man1/sccs-delta.1*
%{_mandir}/man1/sccs-diffs.1*
%{_mandir}/man1/sccs-edit.1*
%{_mandir}/man1/sccs-editor.1*
%{_mandir}/man1/sccs-enter.1*
%{_mandir}/man1/sccs-fix.1*
%{_mandir}/man1/sccs-get.1*
%{_mandir}/man1/sccs-help.1*
%{_mandir}/man1/sccs-histfile.1*
%{_mandir}/man1/sccs-info.1*
%{_mandir}/man1/sccs-init.1*
%{_mandir}/man1/sccs-istext.1*
%{_mandir}/man1/sccs-ldiffs.1*
%{_mandir}/man1/sccs-log.1*
%{_mandir}/man1/sccs-print.1*
%{_mandir}/man1/sccs-prs.1*
%{_mandir}/man1/sccs-prt.1*
%{_mandir}/man1/sccs-rcs2sccs.1*
%{_mandir}/man1/sccs-remove.1*
%{_mandir}/man1/sccs-rename.1*
%{_mandir}/man1/sccs-rmdel.1*
%{_mandir}/man1/sccs-root.1*
%{_mandir}/man1/sccs-sact.1*
%{_mandir}/man1/sccs-sccsdiff.1*
%{_mandir}/man1/sccs-status.1*
%{_mandir}/man1/sccs-tell.1*
%{_mandir}/man1/sccs-unedit.1*
%{_mandir}/man1/sccs-unget.1*
%{_mandir}/man1/sccs-val.1*
%{_mandir}/man1/sccs.1*
%{_mandir}/man1/sccscvt.1*
%{_mandir}/man1/sccsdiff.1*
%{_mandir}/man1/sccslog.1*
%{_mandir}/man1/sccspatch.1*
%{_mandir}/man1/scgcheck.1*
%{_mandir}/man1/scgskeleton.1*
%{_mandir}/man1/scut.1*
%{_mandir}/man1/sdd.1*
%{_mandir}/man1/sfind.1*
%{_mandir}/man1/sgrow.1*
%{_mandir}/man1/smt.1*
%{_mandir}/man1/spaste.1*
%{_mandir}/man1/spatch.1*
#{_mandir}/man1/spax.1*
%{_mandir}/man1/sysV-make.1*
%{_mandir}/man1/tartest.1*
%{_mandir}/man1/termcap.1*
#{_mandir}/man1/translit.1*
%{_mandir}/man1/udiff.1*
%{_mandir}/man1/unget.1*
%{_mandir}/man1/ustar.1*
%{_mandir}/man1/val.1*
%{_mandir}/man1/vc.1*
%{_mandir}/man1/vctags.1*
%{_mandir}/man1/ved-e.1*
%{_mandir}/man1/ved-w.1*
%{_mandir}/man1/ved.1*
%{_mandir}/man1/what.1*
%{_mandir}/man5/changeset.5*
%{_mandir}/man5/sccschangeset.5*
%{_mandir}/man5/sccsfile.5*
%{_mandir}/man5/star.5*
%{_mandir}/man5/streamarchive.5*
%{_mandir}/man8/devdump.8*
%{_mandir}/man8/sformat.8*

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2021.09.18
- Rebuilt for Fedora
