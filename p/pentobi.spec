Name:           pentobi
Version:        21.0
Release:        1
Summary:        Program to play the board game Blokus
License:        GPLv3
URL:            http://pentobi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake gcc-c++ qt5-qtsvg-devel qt5-qttools-devel
BuildRequires:  extra-cmake-modules kf5-kio-devel
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  qt5-qtquickcontrols2-devel qt5-qtwebview-devel docbook-style-xsl
BuildRequires:  librsvg2-tools

%description
Pentobi is a computer opponent for the board game Blokus with
support for Classic, Duo, Junior, Trigon, and Nexos game variants.
Different levels of playing strength are available. Pentobi can
save and load games along with comments and move variations.

%package kde-thumbnailer
Summary: KDE thumbnailer for Pentobi game files
Enhances: dolphin

%description kde-thumbnailer
This package contains a KDE plugin to display thumbnails of
Pentobi game files.

%prep
%autosetup
#sed -i '15i /usr/share/sgml/docbook/xsl-stylesheets-1.79.2' pentobi/docbook/CMakeLists.txt

%build
export CXXFLAGS="%{optflags} -O3"
%cmake -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
       -DPENTOBI_BUILD_KDE_THUMBNAILER=ON \
       -DPENTOBI_BUILD_TESTS=ON .
#make %{?_smp_mflags} VERBOSE=1 -C %{_host}
%cmake_build

%install
#make_install -C %{_host}
%cmake_install

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc *.md
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/thumbnailers/*
#{_docdir}/%{name}
#{_datadir}/help/*/%{name}
%{_mandir}/man6/*
%{_datadir}/metainfo/io.sourceforge.pentobi.appdata.xml
%{_mandir}/*/man6/*

%files kde-thumbnailer
%{_libdir}/qt5/plugins/*.so
%{_datadir}/kservices5/*.desktop
#{_datadir}/metainfo/io.sourceforge.pentobi.kde-thumbnailer.metainfo.xml

%changelog
* Sun May 22 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 21.0
- Rebuilt for Fedora
* Mon Jan 04 2016 Juhani Numminen <juhaninumminen0@gmail.com> - 11.0-1
- Created by borrowing from existing pentobi.spec files
- Add subpackage kde-thumbnailer
- Build with -O3 to make higher levels faster
