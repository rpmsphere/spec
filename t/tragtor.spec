Name:           tragtor
Summary:        A GUI for FFmpeg for audio and video-conversion
Version:        0.8.82
Release:        11.1
URL:            https://mein-neues-blog.de/tragtor-gui-for-ffmpeg/
Source0:        https://repository.mein-neues-blog.de:9000/archive/%{name}-%{version}_all.tar.gz
License:        LGPL v2.1
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       pygtk2 ffmpeg id3v2
BuildArch:      noarch

%description
traGtor is a graphical user interface (GUI) for the awesome conversion tool ffmpeg for the use with Linux-OS.
It is written in Python and uses the GTK-Engine (standard in GNOME desktops) for displaying its interface.
The goal of traGtor is not to bring you all of the features ffmpeg offers, but to be a fast
and user friendly choice for converting a single media file into any other format.
For a full ffmpeg featuring GUI please refer to the other great projects listed below.
This GUI is written for not dealing too much with command lines, options and parameters and so on,
and refers mostly to the real keyboard haters.

One may edit the command line sent to ffmpeg to fit all of his needs,
but for those cases the more command line oriented tools (with nice GUIs too) could be the better choice.
But if you need a tool for click oriented and flawless conversion like stripping an mp3 from a youtube movie,
resizing and recoding a clip to fit your mobiles screen or just changing the format of a movie-file
to be able to play it in a flash-media-player traGor may be Mr. Right for you.

%prep
%setup -q -c
sed -i 's/traGtor 0.8/traGtor %{version}/' usr/share/tragtor/tragtor.py
sed -i 's/traGtor - a/A/' usr/share/applications/tragtor.desktop
sed -i 's|/usr/share/pixmaps/%{name}.svg|%{name}|' usr/share/applications/%{name}.desktop

%build

%install
install -D -m755 usr/bin/tragtor %buildroot/%{_bindir}/tragtor
install -D -m644 usr/share/applications/tragtor.desktop %buildroot%{_datadir}/applications/tragtor.desktop
install -D -m644 usr/share/pixmaps/tragtor.svg %buildroot%{_datadir}/pixmaps/tragtor.svg
pushd usr/share/tragtor
for i in *.py; do
  install -D -m755 "$i" %buildroot%{_datadir}/tragtor/"$i"
done
for i in *.svg; do
  install -D -m644 "$i" %buildroot%{_datadir}/tragtor/"$i"
done
install -D -m644 ee.jpg %buildroot%{_datadir}/tragtor/ee.jpg
install -D -m644 tragtor.glade %buildroot%{_datadir}/tragtor/tragtor.glade
install -D -m644 tragtor.gladep %buildroot%{_datadir}/tragtor/tragtor.gladep
install -D -m644 version %buildroot%{_datadir}/tragtor/version

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files 
%{_bindir}/tragtor
%{_datadir}/applications/tragtor.desktop
%{_datadir}/pixmaps/tragtor.svg
%{_datadir}/tragtor
%doc usr/share/doc/tragtor/*

%changelog
* Tue Feb 10 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.82
- Rebuilt for Fedora
* Sat Jul 14 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.8.55
* Tue Jul 03 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.8.54
* Mon May 07 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.8.53
* Sun Apr 22 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.8.52
* Tue Apr 17 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.8.50
* Tue Mar 06 2012 - joerg.lorenzen@ki.tng.de
- update to version 0.8.48
* Sun Nov 27 2011 - joerg.lorenzen@ki.tng.de
- update to version 0.8.45
* Sun Nov 27 2011 - joerg.lorenzen@ki.tng.de
- update to version 0.8.43
* Fri Oct 14 2011 - joerg.lorenzen@ki.tng.de
- update to version 0.8.41
* Fri Jul 22 2011 - joerg.lorenzen@ki.tng.de
- Initial package, version 0.8.37
