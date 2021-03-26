Summary: Gungirl Sequencer
Name: ggseq
Version: 0.3.1
Release: 1
License: GPL
Group: Applications/Multimedia
Source: http:/dl.sf.net/%{name}/%{name}-%{version}.tar.gz
URL: http://sourceforge.net/projects/ggseq/
BuildRequires: libsndfile-devel wxGTK-devel >= 2.4.0 libsamplerate-devel >= 0.0.15

%description
Gungirl Sequencer is NOT a midi seqencer. 
But it is helpful to sample different
PCM audio files (at the moment just WAV files)

%description -l de
Gungirl Sequencer ist KEIN midi Sequencer.
Aber er ist sehr hilfreich um verschiedene
PCM Audio Dateien zu Sampeln (im Augenblick nur WAV Dateien)

%prep
%setup -q
sed -i 's/SoundTouch:://' src/SoundTouch/SoundTouch.h
sed -i 's|/.*/||' ggseq.desktop
sed -i 's|doc/ggseq|doc/ggseq-%{version}|' src/ggseq_ui.cpp

%build
%configure
%__make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -rf %{buildroot}%{_datadir}/doc/%{name}
install -Dm 644 icons/ggseq_32.xpm %{buildroot}%{_datadir}/pixmaps/ggseq_32.xpm
install -Dm 644 ggseq.desktop %{buildroot}%{_datadir}/applications/ggseq.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING NEWS AUTHORS THANKS ChangeLog doc/ggseq.htb
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_32.xpm

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuild for Fedora
* Sat May 07 2005 Richard Spindler <richard.spindler AT gmail.com>
- removed dependencies
- changed version number
* Sat Feb 19 2005 Georg E Schneider <georg@georgs.org>
- build from cvs
- Added "include <math.h>" src/WaveEditor.cpp
- Added request for SoundTouch in configure.ac
* Wed Feb 16 2005 Georg E Schneider <georg@georgs.org>
- corrected horrible bugs in the spec-file
* Mon Feb 14 2005 Georg E Schneider <georg@georgs.org>
- rebuild for FC3
- Added "#include <math.h>" in src/TLView.cpp
- reonfigured *.desktop-file
* Mon Feb 16 2004 Richard Spindler <oracle2025@gmx.de>
- strip ggseq executable
* Sat Dec 27 2003 Georg E Schneider <georg@georgs.org> 
- removed not needed icons
- corrected some little mistakes
* Sun Dec 21 2003 Georg E Schneider <georg@georgs.org>
- initial build
