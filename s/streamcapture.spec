Name:           streamcapture
Summary:        A program to save streaming video to your computer
Version:        0.3.3
Release:        1
URL:            https://ceicer.org/streamcapture/index_eng.php
Source0:        streamcapture-%{version}-source.zip
Source1:        streamcapture.desktop
Source2:        streamcapture.png
Patch0:         streamcapture-installdirs.patch
License:        GPL
Group:          Productivity/Networking/Other
Requires:       rtmpdump
BuildRequires:  gcc-c++ qt4-devel desktop-file-utils

%description
Want to save video on your computer to view whenever you want?

The program works with Linux, Windows and MacOS X.
The program is written in C++ and uses Qt4 graphic library.
There is a setup program for Windows, Slackware and an experimental version for Ubuntu.

Tested on Windows XP and Windows 7 and Slackware 13.37
and an experimental version runs on Ubuntu 11.04.

streamCapture is designed to work primarily on https://svtplay.se/ and https://urplay.se/

streamCapture using RTMPDump to download.
rtmpdump is a toolkit for RTMP streams.
All forms of RTMP are supported, including RTMP://, RTMPT://, RTMPE://, RTMPTE://, and RTMPS://.

It works on many sites that use RTMP streams.

streamCapture does not work on youtube.

%prep
%setup -q -n streamcapture-%{version}-source
%patch 0

%build
lrelease-qt4 streamcapture.pro
qmake-qt4 QMAKE_CFLAGS="%optflags" QMAKE_CXXFLAGS="%optflags" streamcapture.pro
%__make %{?jobs:-j %jobs}

%install
install -D -m755 streamcapture-%{version} $RPM_BUILD_ROOT%{_bindir}/streamcapture
install -D -m644 images/arrow.png $RPM_BUILD_ROOT%{_datadir}/streamcapture/arrow.png
install -D -m644 %{S:1} $RPM_BUILD_ROOT%{_datadir}/applications/streamcapture.desktop
install -D -m644 %{S:2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/streamcapture.png
for i in *.html; do
  install -D -m644 "$i" $RPM_BUILD_ROOT%{_datadir}/streamcapture/"$i";
done
for i in *.qm; do
  install -D -m644 "$i" $RPM_BUILD_ROOT%{_datadir}/streamcapture/languages/"$i";
done

%files
%{_bindir}/streamcapture
%{_datadir}/applications/streamcapture.desktop
%{_datadir}/pixmaps/streamcapture.png
%dir %{_datadir}/streamcapture
%dir %{_datadir}/streamcapture/languages
%{_datadir}/streamcapture/arrow.png
%{_datadir}/streamcapture/help_*.html
%{_datadir}/streamcapture/languages/streamcapture_*.qm

%changelog
* Sun Dec 08 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuilt for Fedora
* Fri Jun 15 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.2.8
* Fri May 18 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.2.7
* Mon Feb 06 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.2.6
* Sun Jan 29 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.2.5
* Mon Jan 23 2012 - joerg.lorenzen@ki.tng.de
- Initial package, version 0.2.4
