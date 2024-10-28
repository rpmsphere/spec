%undefine _debugsource_packages
%define         shortname       cr3

Name:           coolreader3
Version:        3.0.56
Release:        19.1
Summary:        Free e-book reader
Group:          Books/Literature
License:        GPL
Source:         %{shortname}_%{version}.orig.tar.gz
URL:            https://coolreader.org/e-index.htm
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, qt4-devel, cmake, libjpeg-devel, fontconfig-devel, zlib-devel

%description
CoolReader is fast and small cross-platform XML/CSS based E-Book reader for desktops
and handheld devices. Supported formats: FB2, TXT, RTF, DOC, TCR, HTML, EPUB, CHM,
PDB. Platforms: Win32, Linux, Android. Ported on some eInk based devices.

%prep
%setup -q -n cr%{version}-7
#sed -i 's|<freetype/|<freetype2/|' crengine/src/lvfntman.cpp
sed -i '1182s|return false;|return NULL;|' crengine/src/lvfntman.cpp
sed -i '4935s|return false;|return NULL;|' crengine/src/lvdocview.cpp
sed -i '172s/$/ || __aarch64__/' thirdparty/chmlib/src/chm_lib.c

%build
mkdir qtbuild
cd qtbuild
cmake -D GUI=QT -D CMAKE_BUILD_TYPE=Release -D MAX_IMAGE_SCALE_MUL=2 -D DOC_DATA_COMPRESSION_LEVEL=3 -D DOC_BUFFER_SIZE=0x1400000 -D CMAKE_INSTALL_PREFIX=/usr ..
make

%install
rm -rf $RPM_BUILD_ROOT
cd qtbuild
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/%{shortname}
%{_datadir}/%{shortname}
%{_datadir}/pixmaps/%{shortname}.*
%{_datadir}/applications/%{shortname}.desktop
%{_datadir}/doc/%{shortname}/*
%{_mandir}/man1/%{shortname}.*

%changelog
* Thu Jun 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.56
- Rebuilt for Fedora
* Thu Sep 08 2011 Sergey Zhemoitel <serg@mandriva.org> 3.0.49-1mdv2012.0
+ Revision: 698983
- new version 3.0.49
- fix build, add russian comment in .desktop
- fix install in spec
* Sun Aug 28 2011 Sergey Zhemoitel <serg@mandriva.org> 3.0.45-1
+ Revision: 697261
- imported package coolreader3
