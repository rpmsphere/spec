Name: midisheetmusic
Summary: Midi Sheet Music Player
Version: 2.4
Release: 10.1
Group: sound
URL: http://midisheetmusic.sourceforge.net/
Source0: http://sourceforge.net/projects/midisheetmusic/files/midisheetmusic/%{version}/MidiSheetMusic-%{version}-linux-src.tar.gz
BuildArch: noarch
License: GPLv2
BuildRequires: mono-devel, alsa-lib-devel

%description
Midi Sheet Music is a free program that plays MIDI music files 
while highlighting the piano notes and sheet music notes.
It will be installed under the menu "Applications : Sound and Video".
Or, you can run it from the command line using /usr/bin/midisheetmusic.mono.exe.
This package depends on 
- The Mono.NET runtime (libmono-system2.0-cil, libmono-winforms2.0-cil)
- The Linux Sound Architecture (alsa-base, alsa-utils)
- The Timidity MIDI player (timidity)

%prep
%setup -q -n MidiSheetMusic-%{version}-linux-src
sed -i 's|gmcs|mcs|' build.sh

%build
./build.sh

%install
rm -rf %{buildroot}
install -Dm755 %{name}.mono.exe %{buildroot}%{_bindir}/%{name}.mono.exe
install -Dm644 deb/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 NotePair.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc *.txt *.rtf *.html
%{_bindir}/%{name}.mono.exe
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuild for Fedora
