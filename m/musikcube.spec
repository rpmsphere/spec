%global __os_install_post %{nil}

Name: musikcube
Summary: A cross-platform, terminal-based audio engine, library, player and server written in C++
Version: 0.93.1
Release: 1
Group: Applications/Multimedia
License: BSD-3-Clause
URL: https://github.com/clangen/musikcube
Source0: https://github.com/clangen/musikcube/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++ cmake
BuildRequires: alsa-lib-devel
BuildRequires: ffmpeg-devel
BuildRequires: boost-devel
BuildRequires: lame-devel
BuildRequires: libcurl-devel
BuildRequires: libev-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: taglib-devel
BuildRequires: zlib-devel
BuildRequires: libmicrohttpd-devel
Patch0:        musikcube-av_codec_next.patch

%description
musikcube is a fully functional terminal-based music player, library,
and streaming audio server that runs natively on Windows, macOS, and Linux.

%prep
%setup -q
%patch0 -p 1
sed -i '8i #include <memory>\n#include <string>' src/plugins/mpris/mpris.h
sed -i '41i #include <memory>' src/plugins/httpdatastream/LruDiskCache.h
sed -i '/av_register_all()/d' src/plugins/stockencoders/FfmpegEncoder.cpp src/plugins/ffmpegdecoder/plugin.cpp

%build
%cmake -DCMAKE_C_FLAGS="${CFLAGS/-Werror=format-security/} -fpermissive -fPIC" -DCMAKE_CXX_FLAGS="${CXXFLAGS/-Werror=format-security/} -fpermissive -fPIC" .
%cmake_build

%install
%cmake_install

%files
%doc README.md CHANGELOG.txt LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.93.1
- Rebuilt for Fedora
