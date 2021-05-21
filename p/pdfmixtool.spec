Summary:	An application to split, merge, rotate and mix PDF files
Name:		pdfmixtool
Version:	0.6
Release:	1
Source0:	pdfmixtool-v%{version}.tar.gz
License:	GPL v2
Group:		Office
URL:		https://gitlab.com/scarpetta/pdfmixtool
BuildRequires:  openssl-devel 
BuildRequires:  podofo-devel 
BuildRequires:  qpdf-devel
BuildRequires:  qt5-qtbase-devel

%description
An application to split, merge, rotate and mix PDF files

%prep
%setup -qn pdfmixtool-v%{version}

%build
#cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr
%cmake
%cmake_build

%install
rm -rf %buildroot
%cmake_install

%files
%{_bindir}/pdfmixtool
%{_datadir}/applications/eu.scarpetta.PDFMixTool.desktop
%{_datadir}/metainfo/eu.scarpetta.PDFMixTool.appdata.xml
%{_datadir}/icons/hicolor/*/apps/eu.scarpetta.PDFMixTool.*
%{_datadir}/pdfmixtool

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
* Fri Jun 21 2019 tex - 0.3.4-1pclos2019
- new
