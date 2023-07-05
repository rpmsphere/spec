Name:           nootka
Version:        2.0.2
Release:        1
Summary:        Application to help with learning classical score notation
License:        GPLv3
Group:          Sound/Utilities
URL:            https://nootka.sf.net
Source0:        https://sourceforge.net/projects/nootka/files/Nootka-%{version}/%{name}-%{version}-source.tar.bz2
BuildRequires:  qt5-qtbase-devel
BuildRequires:  fftw-devel
#BuildRequires:  ecasound-devel
BuildRequires:  cmake
BuildRequires:  soundtouch-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel

%description
Nootka is open-source application
to help with learning (also with teaching) classical score notation.
Mostly it is for guitarists,
but it can be used for ear training as well.

Features:
interactive interface to discover the rules of musical notation
exercises with possibility to create own sets
accurate method for detecting sung and played sounds
natural sound of guitars
clefs (treble, bass and others) and grand staff
analyse of results
different kinds of guitars and theirs tuning
Czech, French, German, Polish and Russian translations

%prep
%setup -q -n %{name}-%{version}-source
sed -i 's|-std=|-Wno-narrowing -std=|' src/CMakeLists.txt

%build
%cmake -DJACK_LIBRARY=/usr/lib64/pipewire-0.3/jack/libjack.so
%cmake_build

%install
%cmake_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
cp changes LICENSE *.md %{buildroot}%{_docdir}/%{name}

%files
%{_docdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/*
%{_datadir}/mime/packages/*
%{_datadir}/metainfo/*

%changelog
* Sun Apr 2 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.2
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 1.0.1-4.mga5
+ Revision: 743953
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.0.1-3.mga5
+ Revision: 682914
- Mageia 5 Mass Rebuild
  + tv <tv>
    - s/uggests:/Recommends:/
* Thu May 08 2014 barjac <barjac> 1.0.1-2.mga5
+ Revision: 621176
- rebuild for new ecasound
* Sat Mar 29 2014 dglent <dglent> 1.0.1-1.mga5
+ Revision: 609319
- New version 1.0.1
* Sun Mar 23 2014 dglent <dglent> 1.0.0-1.mga5
+ Revision: 606751
- New version 1.0.0
- Add br soundtouch
- Add lang tags
- imported package nootka
  + kamil <kamil>
    - fix group: Education -> Sound/Utilities
    - add cmake to BR
    - fix BR: fftw -> fftw-devel
