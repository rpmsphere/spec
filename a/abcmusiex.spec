%undefine _debugsource_packages

Name:           abcmusiex
Summary:        ABC Music Reading Exercises Generator 
Version:        1.0 
Release:        15.1
License:        GPLv3+
Group:          Applications/Multimedia
Source0:        %{name}-%{version}.tar.gz
URL:            https://abcmusiex.sourceforge.net
BuildRequires:  gtk2-devel help2man libconfig-devel
Requires:       abcMIDI timidity++

%description
ABC Music Reading Exercises generate music score sight reading exercises.

Based upon ABC Music Notation Standard, the executable generates an ABC file, 
which is converted to printable PS or PDF files. WAV and MP3 are also created
to allow student play the exercises on a audio player (CD, PC) while he plays
the printed exercises on his own instrument. 

Output is highly configurable: permits triplets, rests, dotted notes, note 
ranges, notes dispersion (on some instruments very distant notes are difficult
to follow), score key, clefs, different times and metrics (4/4, 6/8, you say).

Programmed in GNU C. Should be portable to other platforms: Unix, OsX, 
Windows, Solaris, BSD...

%prep
%setup -q
sed -i 's|-ggdb|-Wl,--allow-multiple-definition|' configure

%build
./configure
%make_build

%install
%make_install

%files 
%doc COPYING README INSTALL AUTHORS NEWS
%doc %{_mandir}/man1/%{name}.1*
%{_bindir}/abcmusiex
%{_bindir}/abcmusiex-gui
%{_datadir}/%{name}/abcmusiex-gui.gtk
%{_datadir}/%{name}/abcmusiex-gui.glade
%{_datadir}/%{name}/abcmusiex.png
%{_datadir}/applications/abcmusiex.desktop

%changelog
* Wed May 10 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Thu Jul 1 2010 Rodolfo Alcazar <rodolfoap@gmail.com> 1.0-8
- Fixes: minor syscommand fixes
* Wed Jun 23 2010 Rodolfo Alcazar <rodolfoap@gmail.com> 1.0-7
- Fifth release signed 1.0-7
- Fixes: minor bugs in system command
-        Spec file with some Willy Cat <siamwilly@yahoo.com.ar> suggestions
- Adds: Graphic user interface
* Tue Jun 17 2008 Rodolfo Alcazar <rodolfoap@gmail.com> 0.9-5
- Fifth release signed 0.9-5
- Fixes: using yaps instead of abcm2ps
* Sat Dec 29 2007 Rodolfo Alcazar <rodolfoap@gmail.com> 0.9-4
- Fourth release signed 0.9-4
- Fixes: A couple of bugs
-        Uses evince instead of acroread, timidity as player, not needed wav or mp3 files for exercises starting
-        Faster generation and action
-        Fedora 8 ready, avoid many dependences, rpm process generation improved
-        Stages generation improved
-        Pulseaudio not fixed in timidity, but abcmusiex now working fine with default device.
* Tue Apr 4 2006 Rodolfo Alcazar <rodolfoap@gmail.com> 0.8-2
- Third release signed 0.8-2
- Fixes: Generation algorithms improved;
-        Sharps and flats generator;
-        Ties generator.
* Thu Mar 23 2006 Rodolfo Alcazar <rodolfoap@gmail.com> 0.8
- Second release signed 0.8
- Fixes: Controlling generation stages;
-        Updated documentation and manpage;
-        Better generation tools;
-        Metronom optional;
-        Randomizer bug fixed;
-        Dispersion fixed;
-        Interface standardization.
