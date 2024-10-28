Name:           FOTAQ
BuildRequires:  unzip desktop-file-utils
URL:            https://www.scummvm.org/downloads.php
License:        Other uncritical OpenSource License
Group:          Amusements/Games/Other
Requires:       scummvm timidity++
Version:        20040315
Release:        1.bin
Summary:        Flight of the Amazon Queen (Adventure Game)
Source0:        FOTAQ_Floppy.zip
Source1:        FOTAQ
Source2:        %name.desktop
Source3:        %name.info
Source4:        %name.png
Source5:        queen.tbl
BuildArch:      noarch

%description
Flight of the Amazon Queen is a 2D point-and-click adventure game set
in the 1940s, and originally published for DOS and the Amiga.

You assume the role of Joe King, a pilot for hire who is given the job
of flying Faye Russell (a famous movie star) into the Amazon jungle for
a photo shoot. Of course, things never go according to plan. After an
unfortunate turn of events, they find themselves stranded in the heart
of the Amazon jungle where Joe embarks on a quest to rescue a kidnapped
princess and, in the process, discovers the sinister intentions of a
suspiciously-located Lederhosen company. Joe crosses paths with a
variety of unlikely jungle inhabitants, including a tribe of Amazon
women and 6-foot-tall pygmies.

Authors:
--------
    John Passfield (Krome Studios, Australia)
    Steve Stamatiadis (Krome Studios, Australia)

%prep
%setup -q -n FOTAQ_Floppy
#unzip -u $RPM_SOURCE_DIR/FOTAQ_Floppy.zip

%build

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT/%{_bindir}
%__mkdir_p $RPM_BUILD_ROOT/%{_datadir}/games/FOTAQ
%__mkdir_p $RPM_BUILD_ROOT/%{_datadir}/doc/packages/FOTAQ
install -m 644 queen.1 $RPM_BUILD_ROOT/%{_datadir}/games/FOTAQ
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_datadir}/games/FOTAQ
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_datadir}/games/FOTAQ/info
install -m 644 readme.txt $RPM_BUILD_ROOT/%{_datadir}/doc/packages/FOTAQ
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}
%__mkdir_p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/%{_datadir}/pixmaps
#%suse_update_desktop_file -i %name Game X-SuSE-AdventureGame
%__rm -f $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%name
%__mkdir_p %{buildroot}%{_datadir}/applications/
%__cp %{SOURCE2} %{buildroot}%{_datadir}/applications/

%files
%doc %{_datadir}/doc/packages/FOTAQ/
%{_bindir}/FOTAQ
%{_datadir}/games/FOTAQ/
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/%name.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20040315
- Rebuilt for Fedora
* Wed Oct 22 2008 Wind <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
* Thu Mar 29 2007 sndirsch@suse.de
- added unzip to Buildrequires
* Mon Feb  6 2006 sndirsch@suse.de
- fixed Wavetable MIDI support (Bug #148395)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Aug 11 2005 sndirsch@suse.de
- added queen.tbl required for rebuilding FOTAQ; somewhat related
  to the scummvm-tools recently added to the scummvm package
  (Bug #103725)
* Thu May 12 2005 sndirsch@suse.de
- use norootforbuild
* Wed Mar 23 2005 sndirsch@suse.de
- build as noarch
* Wed Feb 16 2005 sndirsch@suse.de
- fixed build
* Tue Mar 16 2004 sndirsch@suse.de
- created package
