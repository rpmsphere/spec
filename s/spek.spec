Name:		spek
Version:	0.8.4
Release:	1
Group:		Sound/Utilities
License:	GPLv3
Summary:	Tool for audio spectrum analysis and visualization
URL:		https://spek-project.org
Source0:	https://spek.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		spek-0.8.4-ffmpeg-5.0.patch
BuildRequires:	wxGTK3-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	intltool

%description
Spek (IPA: /spɛk/, ‘bacon’ in Dutch) helps to analyse your audio files by showing
their spectrogram. Spek is free software available for Unix, Windows and Mac OS X.

Features:
* Supports all popular lossy and lossless audio file formats thanks to the FFmpeg libraries.
* Ultra-fast signal processing, uses multiple threads to further speed up the analysis.
* Shows the codec name and the audio signal parameters.
* Allows to save the spectrogram as an image file.
* Drag-and-drop support; associates with common audio file formats.
* Auto-fitting time, frequency and spectral density rulers.
* Adjustable spectral density range.
* Translated into 16 languages.

%prep
%setup -q
%patch0 -p 1
sed -i 's|-pthread|-pthread -fpermissive -I/usr/include/ffmpeg|' src/Makefile.am

%build
#configure
./autogen.sh
make

%install
%makeinstall
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/man/man1/%{name}.*

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.4
- Rebuilt for Fedora
* Fri Jul 12 2013 fwang <fwang> 0.8.1-4.mga4
+ Revision: 453382
- fix build with recent ffmpeg
* Mon Jan 14 2013 umeabot <umeabot> 0.8.1-4.mga3
+ Revision: 382517
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Jan 09 2013 malo <malo> 0.8.1-3.mga3
+ Revision: 343376
- updated RPM group (Visualization is no more)
* Tue Jan 08 2013 fwang <fwang> 0.8.1-2.mga3
+ Revision: 341743
- rebuild for new ffmpeg
* Thu Nov 22 2012 mitya <mitya> 0.8.1-1.mga3
+ Revision: 320424
- 0.8.1
- Created package structure for spek.
