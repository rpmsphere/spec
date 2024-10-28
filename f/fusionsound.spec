%define oname FusionSound
%define dfbmoduledir %(pkg-config --variable=moduledir direct)

Summary:        An audio sub system
Name:           fusionsound
Version:        1.6.3
Release:        1
License:        GPLv2+
Group:          System/Libraries
URL:            https://www.directfb.org
Source0:        https://www.directfb.org/downloads/Core/%{oname}-%{version}.tar.gz
Patch0:         FusionSound-1.6.2-ffmpeg1.0.patch
Patch1:         FusionSound-1.6.3-ffmpeg2.0.patch
Patch2:         FusionSound-1.6.3-ffmpeg2.4.patch
#BuildRequires: ffmpeg-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(directfb)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(vorbis)

%description
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion.

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.

%files
%doc AUTHORS ChangeLog TODO
%{_docdir}/%{name}
%{_bindir}/fs*
%{_mandir}/*/%{name}*
%dir %{dfbmoduledir}/interfaces/IFusionSound
%{dfbmoduledir}/interfaces/IFusionSound/libifusionsound.*
%dir %{dfbmoduledir}/interfaces/IFusionSoundMusicProvider
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_cdda.*
#{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_ffmpeg.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_mad.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_playlist.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_vorbis.*
%{dfbmoduledir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_wave.*
%dir %{dfbmoduledir}/snddrivers
%{dfbmoduledir}/snddrivers/libfusionsound_alsa.*
%{dfbmoduledir}/snddrivers/libfusionsound_oss.*
%{dfbmoduledir}/snddrivers/libfusionsound_wave.*
%{dfbmoduledir}/snddrivers/libfusionsound_dummy.*
%{_libdir}/lib%{name}-*.so.*

%package devel
Group:          Development/Other
Summary:        An audio sub system
Requires:       %{name} = %{version}-%{release}

%description devel
FusionSound is a very powerful audio sub system in the
manner of DirectFB and a technical demonstration of Fusion.

FusionSound supports multiple applications using Fusion IPC.
It provides streams, static sound buffers and control over any
number of concurrent playbacks. Sample data is always stored
in shared memory, starting a playback simply adds an entry to
the playlist of the mixer thread in the master application.

%files devel
%doc AUTHORS ChangeLog TODO
%{_libdir}/pkgconfig/fusionsound*.pc
%{_includedir}/fusionsound
%{_includedir}/fusionsound-internal
%{_libdir}/lib%{name}.so
%exclude %{_libdir}/lib%{name}.la

%prep
%setup -q -n %{oname}-%{version}
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

%build
autoreconf -fi
%configure \
        --without-ffmpeg
%make_build

%install
%make_install

%changelog
* Tue Jun 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.3
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.6.3-8
- (d9c3add) MassBuild#1257: Increase release tag
