Name:           ripit
Summary:        Perl Script to Create .ogg or .mp3 Files from an Audio CD
Version:        3.9.0
Release:        6.1
URL:            http://www.suwald.com/ripit/ripit.html
License:        GPL v2 or later
Group:          Productivity/Multimedia/CD/Grabbers
Requires:       cdparanoia vorbis-tools perl perl-CDDB_get perl-libwww-perl
Source:         http://www.suwald.com/ripit/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This Perl script makes it easy to create MP3 files from an audio CD. It
tries to find the artist and song titles with the help of CDDB.

Authors:
--------
Simon Quinn
Mads Martin Joergensen
Felix Suwald <felix@suwald.com>

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 ripit.pl $RPM_BUILD_ROOT/%{_bindir}/ripit
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
install -m 644 config $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 ripit.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README HISTORY LICENSE
%doc %{_mandir}/man1/*
%{_bindir}/ripit
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.9.0
- Rebuilt for Fedora
* Wed Nov  5 2008 lrupp@example.com
- recommend normalize
* Mon Nov  3 2008 lars@linux-schulserver.de
- update to 3.0.7 Beta 20081019:
  + No new options, but $dirtemplate accepts more
variables to automatically generate different
output-directories when different encoding
formats or the same format at different
qualities is used.
  + Option ghost now accepts values larger than zero
at a decimal precision. RipIT will try to trim
lead in/out if true silence is encounterd.
  + Fixed bug on corrupted wav headers when using
option ghost. Flac should not fail anymore.
  + Fixed bug on too long file names and paths for
rippers, encoder should not wait endlessly.
  + Fixed bug that option md5sum settings were not
read in config file.
  + Fixed bug on option loop, the CD tray should not
close again when done and endlessly rip the same
CD.
  + Option chars has slightly different default
settings and argument possebilites, but behaves the
same.
* Mon Sep  8 2008 kssingvo@suse.de
- fixed stderr output of lame (bnc#419873)
* Mon Jun 18 2007 kssingvo@suse.de
- new version 3.6.0 with new features:
  * Fixed bug on special characters for tags during submission of
CDDB entries.
  * Fixed unpleasent behaviour if Lame is not installed.
  * Fixed semi-bug on deletion of wavs using remote machines.
  * Added option --merge to merge tracks for gapless encoding.
  * Added option --resume to continue a previously started
session.
  * Added option --ghost to split tracks with gaps into chunks of
sound (at experimental stage).
  * Added options --prepend and --extend to enlarge chunks of
sound when splitted with option --ghost.
  * Added option --ejectcmd to specify command used to control
ejection/loading of CD.
  * Added option --ejectopt to specify options and arguments for
  - -ejectcmd.
  * Added optons --dpermission and --fpermission to set directory
and file permissions.
  * Added option --md5sum to create MD5-sum files for each type of
sound files.
  * Added option --nicerip to set niceness of ripping process.
  * Added option --core to allow several encoding processes on
each machine.
  * Enhanced output from encoding process not to interfer with
output of ripper.
  * Submission of CDDB entries uses sendmail, not mail or nail.
  * Some fine-tuning on detection of hidden-tracks and
ghost-songs.
  * Enhanced detection of perl modules needed, Ripit depends not
on CDDB_get 2.22 but 2.25 and newer, please update.
- changed specfile accordingly
* Tue Apr  3 2007 kssingvo@suse.de
- added perl-libwww-perl to Requires
* Wed Jun 28 2006 kssingvo@suse.de
- new version 3.5.1 with new features:
- new options: --normalize, --loop, --cdtoc
- global config file now included
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Jan 13 2006 mmj@suse.de
- update to version 3.4
* Wed May 11 2005 cthiel@suse.de
- update to version 3.3.7
- aligned ripit-ogg.diff
* Mon Mar 21 2005 mmj@suse.de
- Default to oggvorbis [#74015]
- Make the oggencoding quality better
* Wed Feb 23 2005 mmj@suse.de
- Update to version 3.3.3 which is a bugfix release since 3.3
* Wed Feb 16 2005 mmj@suse.de
- Update to version 3.3
* Wed Jan  5 2005 mmj@suse.de
- Update to version 3.1.1
* Mon Dec 20 2004 mmj@suse.de
- Update to version 3.0
* Mon Dec  6 2004 mmj@suse.de
- Update to version 2.8
* Thu Dec  2 2004 mmj@suse.de
- Update to version 2.7
* Tue Nov 23 2004 mmj@suse.de
- Update to version 2.6.2
* Tue Aug 31 2004 mmj@suse.de
- use proto version 6, we are in the age of UTF-8 now. When touching
  anyway also remove ^M's and greet properly. Thanks Bjoern Jacke.
* Tue Jan  6 2004 mmj@suse.de
- Update to version 2.4 which removes all problems with tmp file
  usage [#33812]
* Tue Oct 21 2003 mmj@suse.de
- Update to version 2.2 which has our patches included plus some
  small feature additions
* Thu Oct 16 2003 mmj@suse.de
- Don't build as root
- Use -q for oggenc instead of bitrate
- Allow outputdir without trailing slash
* Tue May 13 2003 mmj@suse.de
- Use %%defattr
* Mon Aug 26 2002 mmj@suse.de
- Make the ripit script config noreplace, since we don't want to
  replace a users ripit script if modified for hers needs.
* Mon Aug  5 2002 mmj@suse.de
- Added ""'s around mkdir to have it not fail when title contains
  '.
* Tue May 14 2002 mmj@suse.de
- Requires perl-CDDB_get not perl-CDDB.
* Mon May 13 2002 mmj@suse.de
- Update to version 2.0 which includes OggVorbis support and also
  removes dependancy on xmcd. Defaults to OggVorbis.
* Mon Oct 15 2001 sf@suse.de
- added patch to be able to parse disc ID, genre and interpret
  as xmcd has changed the output of 'cda -toc'
* Wed Apr  4 2001 poeml@suse.de
- add convenience link ripit -> ripit.pl
- use BuildRoot
- drop %%{suse_check}
* Wed Dec 13 2000 poeml@suse.de
- updated README.SuSE
- removed executable flag on doc files
* Wed Dec 13 2000 bjacke@suse.de
- update to 1.8 and fix some security vulnerabilities
* Thu Jun  8 2000 uli@suse.de
- moved docs to %%{_docdir}
* Fri Apr 14 2000 dbloms@suse.de
- change the link for bladeenc
* Thu Jan  6 2000 dbloms@suse.de
- change /usr/bin/cat to /bin/cat
- noarch
* Thu Sep 30 1999 dbloms@suse.de
- insert a patch from marc@suse.de to set new defaults
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Jun 10 1999 dbloms@suse.de
- fix bugs
* Mon May 17 1999 dbloms@suse.de
- create the package
