%undefine _debugsource_packages

Name:		pdftk-qgui
Summary:	A Qt4-based GUI for pdftk
Version:	0.1.9.2
Release:	11.1
URL:		http://suslic-2012.narod.ru/PDFTkGUI.html
Source0:	pdftk-qgui_0.1.9-2_src.tar.gz
Source1:	pdftk-qgui.desktop
Patch0:		pdftk-qgui-qt44.patch
Patch1:		pdftk-qgui.patch
License:	BSD
Group:		Productivity/Publishing/PDF
Requires:	pdftk
BuildRequires:	qt-devel qtwebkit-devel libstdc++-devel

%description
PdfTk-QGui is a simple GUI for pdftk - the pdf toolkit written on Qt for Linux.

Author: Koptsow Dmitriy <suslic-2012@rambler.ru>

%prep
%setup -q -n pdftk-qgui_0.1.9-2_src
%patch0
%patch1
chmod 644 readme

%build
qmake-qt4
make

%install
install -D -m 755 bin/pdftk-qgui $RPM_BUILD_ROOT%{_bindir}/pdftk-qgui
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/pdftk-qgui.desktop
install -D -m 644 images/addall.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/pdftk-qgui.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/pdftk-qgui
%{_datadir}/applications/pdftk-qgui.desktop
%{_datadir}/pixmaps/pdftk-qgui.png
%doc readme

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.9.2
- Rebuilt for Fedora
* Wed Jan 13 2010 - joerg.lorenzen@ki.tng.de
- Initial package, version 0.1.9-2
