Name:		feff
Summary:	Front-end for FFmpeg
Version:	1.10.1
Release:	1
URL:		https://dansoft.krasnokamensk.ru/soft.html
Source0:	feff_source.tar.gz
Source1:	feff.desktop
Source2:	feff.png
Patch0:		feff-installdir.patch
License:	GPL
Group:		Productivity/Multimedia/Video/Editors and Convertors
Requires:	ffmpeg
BuildRequires:  gcc-c++ qt4-devel desktop-file-utils

%description
FeFF is a simple graphical frontend (GUI) for FFmpeg.
It supports all formats supported by FFmpeg.

%prep
%setup -q -n feff_source
%patch0

%build
lrelease-qt4 feff.pro
qmake-qt4 QMAKE_CFLAGS="%optflags" QMAKE_CXXFLAGS="%optflags" feff.pro
%__make %{?jobs:-j %jobs}

%install
install -D -m755 Bin/feff $RPM_BUILD_ROOT%{_bindir}/feff
install -D -m644 %{S:1} $RPM_BUILD_ROOT%{_datadir}/applications/feff.desktop
install -D -m644 %{S:2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/feff.png
for i in *.qm; do
  install -D -m644 "$i" $RPM_BUILD_ROOT%{_datadir}/feff/languages/"$i";
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/feff
%{_datadir}/applications/feff.desktop
%{_datadir}/pixmaps/feff.png
%dir %{_datadir}/feff
%dir %{_datadir}/feff/languages
%{_datadir}/feff/languages/feff_*.qm
%doc Bin/COPYING Bin/HISTORY

%changelog
* Sun Nov 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10.1
- Rebuilt for Fedora
* Sun Jun 24 2012 - joerg.lorenzen@ki.tng.de
- update to version 1.9.1
* Sat Jun 23 2012 - joerg.lorenzen@ki.tng.de
- update to version 1.9
* Fri Jun 15 2012 - joerg.lorenzen@ki.tng.de
- Initial package, version 1.8.1
