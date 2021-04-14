Name:		winff
Summary:	A cross platform batch GUI for FFmpeg
Version:	1.5.5
Release:	9.1
URL:		http://code.google.com/p/winff/
Source0:	winff-%{version}-source.tar.gz
Source1:	winff.desktop
License:	GPL-3.0
Group:		Video/Editors and Convertors
Requires:	ffmpeg
BuildRequires:	dos2unix fpc fpc-src lazarus xorg-x11-proto-devel desktop-file-utils

%description
WinFF is a GUI for the command line video converter FFMPEG.
It will convert most any video file that FFmpeg will convert.
WinFF does multiple files in multiple formats at one time.
You can for example convert mpeg's, flv's, and mov's
all into avi's all at once.

%prep
%setup -q -n winff
dos2unix *.txt
chmod 644 *.txt docs/*.pdf docs/*.odg docs/*.odt docs/*.txt winff-icons/*.txt
sed -i 's|PoTranslator, types, FileUtil, regexpr|PoTranslator, types, FileUtil, regexpr, LazUTF8, LazFileUtils|' unit1.pas

%build
lazbuild \
	--lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
	--cpu=x86_64 \
%endif
	--widgetset=gtk2 \
	-B winff.lpr

%install
install -D -m755 winff %buildroot%{_bindir}/winff
install -D -m644 %{S:1} %buildroot%{_datadir}/applications/winff.desktop
install -D -m644 presets.xml %buildroot%{_datadir}/winff/presets.xml
install -d -m755 %buildroot%{_datadir}/winff/languages/
install -m644 languages/*.po %buildroot%{_datadir}/winff/languages/
install -d -m755 %buildroot%{_mandir}/man1
install -m644 winff.1 %buildroot%{_mandir}/man1

install -d -m755 %buildroot%{_datadir}/icons/hicolor
for i in 16 24 32 48; do
  install -d -m755 %buildroot%{_datadir}/icons/hicolor/"$i"x"$i"/apps
  install -m644 winff-icons/"$i"x"$i"/*.png %buildroot%{_datadir}/icons/hicolor/"$i"x"$i"/apps
done

%clean
rm -rf %buildroot

%files
%{_bindir}/winff
%{_datadir}/applications/winff.desktop
%{_datadir}/icons/*
%{_datadir}/winff
%{_mandir}/man1/*
%doc AUTHORS *.txt docs/*.pdf docs/*.odg docs/*.odt docs/*.txt winff-icons/*.txt

%changelog
* Mon May 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.5
- Rebuilt for Fedora
* Thu Feb 14 2013 - joerg.lorenzen@ki.tng.de
- update to version 1.5.0
* Thu Oct 11 2012 - joerg.lorenzen@ki.tng.de
- update to version 1.4.3
* Tue Feb 28 2012 - joerg.lorenzen@ki.tng.de
- update to version 1.4.2
* Tue Jan 17 2012 - joerg.lorenzen@ki.tng.de
- update to version 1.4.1
* Mon Dec 19 2011 - joerg.lorenzen@ki.tng.de
- update to version 1.4.0
* Wed Mar 23 2011 - joerg.lorenzen@ki.tng.de
- update to version 1.3.1
* Mon Sep 06 2010 - joerg.lorenzen@ki.tng.de
- Initial package, version 1.3.1
