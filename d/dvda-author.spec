%undefine _debugsource_packages

Name: dvda-author
Summary: High-definition DVD-AUDIO disc creator
Version: 10.06
Release: 1
License: GPLv3
Group: Applications/Multimedia
Source: http://jaist.dl.sourceforge.net/project/dvd-audio/dvda-author/%{name}-%{version}/%{name}-%{version}-400.tar.gz
URL: http://dvd-audio.sourceforge.net

%description
dvda-author creates high-definition DVD-Audio discs with navigable DVD-Video zone
from DVD-Audio zone Supported input audio types: .wav, .flac, .oga, SoX-supported formats
EXAMPLES
-creates a 3-group DVD-Audio disc (legacy syntax):

dvda-author -g file1.wav file2.flac -g file3.flac -g file4.wav

-creates a hybrid DVD disc with both AUDIO_TS mirroring audio_input_directory
and VIDEO_TS imported from directory VID, outputs disc structure to directory
DVD_HYBRID and links video titleset #2 of VIDEO_TS to AUDIO_TS:

dvda-author -i ~/audio/audio_input_directory -o DVD_HYBRID -V ~/Video/VID -T 2

Both types of constructions can be combined.

%prep
%setup -q -n %{name}-10.06-400

%build
export LDFLAGS=-Wl,--allow-multiple-definition
cp -f /usr/share/automake-*/config.guess config/
./configure --prefix=/usr --without-debug --enable-core-build
make -j 2

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-strip
install -m644 %{name}.1 $RPM_BUILD_ROOT%{_datadir}/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%exclude %{_datadir}/applications
%{_datadir}/pixmaps/*
%{_bindir}/*
%{_datadir}/doc/*
%{_datadir}/man/man?/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 10.06
- Rebuilt for Fedora
* Tue Aug 24 2010 Fab Nicol
- Initial package
