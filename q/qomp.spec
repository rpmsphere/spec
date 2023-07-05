%define _unpackaged_files_terminate_build 1

Name: qomp
Version: 1.4
Release: 1
Summary: Quick(Qt) Online Music Player 
License: GPLv2
Group: Sound
URL: https://qomp.sourceforge.net
Source: %name-%version.tar
Source1: %name-%version-ga.tar
Source2: %name-%version-themes.tar
Source3: %name-%version-translations.tar
Source4: %name-%version-singleapp.tar
BuildRequires: qt5-qtbase-devel 
BuildRequires: libcue-devel
BuildRequires: taglib-devel 
BuildRequires: cmake

%description
Qomp's main features:
- Search and play music from several online music hostings (Yandex.Music, myzuka.ru, pleer.com)
- Play music from local filesystem
- Last.fm scrobbling
- MPRIS support(Linux only)
- CUE SHEET support(*.cue files)
- System tray integration
- Proxy-server support
- Playlists support
- Themes support
- Crossplatform (Windows, OS X, Linux, Android)

%prep
%setup -q -a 1 -a 2 -a 3 -a 4

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_libdir/%name
%_libdir/*.so*
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*x*/apps/%name.png

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Mon Mar 25 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.4-alt2
- Fixed requires (ALT #36347)
* Fri Nov 16 2018 Alexander Makeenkov <amakeenk@altlinux.org> 1.4-alt1
- Initial build for ALT
