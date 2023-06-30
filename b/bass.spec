Name:           bass
Version:	0
Release:        8.20030801
Summary:	Beneath a Steel Sky (Adventure Game)
Group:		Amusements/Games
License:	Freeware
URL:		https://www.scummvm.org/downloads.php
Source0:	https://www.mixnmojo.com/bss/BASS-Floppy.zip
Source1:	%name.sh
Source2:	%name.desktop
Source3:	%name.info
Source4:	%name.png
Source5:	https://svn.sourceforge.net/viewcvs.cgi/*checkout*/scummvm/engine-data/trunk/sky.cpt
BuildArch:      noarch
BuildRequires:  unzip
Requires:	scummvm timidity++

%description
Beneath a Steel Sky is a 2D, point-and-click science fiction thriller
set in a bleak future. It was originally published for DOS and the
Amiga. You are Robert Foster, an innocent outsider stranded in a vast
city where oppressed civilians live and work in soaring tower blocks
while the corrupt, covetous, and rich live underground, safe from all
pollution. Alone, save for a robot circuit board, Foster must fight
for survival - and discover the sinister truth behind both his own
past and the city he has found himself trapped in.

%prep
%setup -q -n sky-floppy

%build

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT%{_prefix}/games
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/games/BASS
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/doc/packages/BASS
install -m 644 sky.dnr $RPM_BUILD_ROOT%{_datadir}/games/BASS
install -m 644 sky.dsk $RPM_BUILD_ROOT%{_datadir}/games/BASS
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/games/BASS/info
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/games/BASS
#install -m 644 readme.txt $RPM_BUILD_ROOT%{_datadir}/doc/BASS-%{version}
%__mkdir_p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/BASS
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf $RPM_BUILD_ROOT sky-floppy

%files
%doc readme.txt
%{_bindir}/BASS
%{_datadir}/games/BASS/
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/%name.png

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 8.20030801
- Rebuilt for Fedora
* Mon Oct 20 2009 Wind <yc.yan@ossii.com.tw> - 0-8.20030801
- Rebuild for OSSII.
* Thu Mar 09 2006 Richard June <rjune@bravegnuworld.com> 0-7.20030801
- Added sky.cpt file to spec
- Added noarch
* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch
* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist
* Sun Feb 13 2005 Dams <anvil[AT]livna.org> - 0:0-0.fdr.5.20030801
- Removed some useless comments
- Added -q option in setup line
- Doubled all %% in changelog to avoid rpm confusion
* Fri Feb 11 2005 Richard June <rjune@bravegnuworld.com> - 0:0-0.fdr.4.20030801
- Changed BASS in name and some sources to bass
* Mon Jan 31 2005 Richard June <rjune@bravegnuworld.com> - 0:0-0.fdr.3.20030801
- Changed %%prep to use %%setup
  Removed useless part of %%description
  changed version to 0, changed release to 0.fdr.3.release_date
  changed %%doc to point to docs in $RPM_BUILD_DIR
* Thu Jan 27 2005 Richard June <rjune@bravegnuworld.com> - 0:20030801-0.fdr.2
- Changed %%prep to use %%setup
* Sun Jan 16 2005 Richard June <rjune@bravegnuworld.com> - 0:20030801-0.fdr.1
- Used fedora-newrpmspec to generate this specfile
* Wed Dec 28 2004 Richard June <rjune@bravegnuworld.com> - 0:20030801-0.bgw.1
- Checked against rpmlint, checked against Fedora QA Guidelines
* Fri Jul 02 2004 Richard June <rjune@bravegnuworld.com> - 0:20030801
- fixed .desktop file, requirements.
* Fri Jul 02 2004 Richard June <rjune@bravegnuworld.com> - 0:20030801
- Initial build for rh9
* Fri Sep 12 2003 - sndirsch@suse.de
- use "Try MIDI" instead of "MIDI" for second button name when
  choosing music support as in most cases it falls back to Adlib
  anyway ...
* Sat Aug 30 2003 - sndirsch@suse.de
- added icon entry in desktop file (was missing)
* Fri Aug 29 2003 - sndirsch@suse.de
- added desktop icon
* Wed Aug 27 2003 - tiwai@suse.de
- improved the detection of timidity port.
* Tue Aug 26 2003 - tiwai@suse.de
- improved detection of wavetable synth devices.
  don't try to start timidity if no enough PCM streams are left.
  fallback in adlib mode.
* Sat Aug 16 2003 - sndirsch@suse.de
- fixed BASS start script:
  * only use SBLive builtin MIDI support, if soundfonts are
  installed
* Sat Aug 16 2003 - sndirsch@suse.de
- improved BASS start script:
  * let the user choose to use MIDI instead of Adlib emulation for
  music; SBLive users will get very happy - for others timidity
  is used
* Wed Aug 13 2003 - sndirsch@suse.de
- improved BASS start script:
  * start BASS directly (skipping scummvm menu)
  * information window how to enable Game Menu (F5) before game
  is started
* Mon Aug 11 2003 - sndirsch@suse.de
- fixed category of desktop file
* Sun Aug 10 2003 - sndirsch@suse.de
- added desktop file
* Wed Aug 06 2003 - sndirsch@suse.de
- start script:
  * better locale handling
  * use gb instead of us english as default language (builtin game
  default as well)
* Sun Aug 03 2003 - sndirsch@suse.de
- enabled fullscreen and 'advmame2x' graphics filtering
* Sun Aug 03 2003 - sndirsch@suse.de
- created package
