Name: musikcube
Summary: A cross-platform, terminal-based audio engine, library, player and server written in C++
Version: 0.70.0
Release: 1
Group: Applications/Multimedia
License: BSD-3-Clause
URL: https://github.com/clangen/musikcube
Source0: https://github.com/clangen/musikcube/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
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

%description
musikcube is a fully functional terminal-based music player, library,
and streaming audio server that runs natively on Windows, macOS, and Linux.

%prep
%setup -q

%build
%cmake -DCMAKE_C_FLAGS="%{optflags} -fpermissive -fPIC" -DCMAKE_CXX_FLAGS="%{optflags} -fpermissive -fPIC" .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README.md CHANGELOG.txt LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_includedir}/%{name}
%{_datadir}/%{name}

%changelog
* Fri Nov 01 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.70.0
- Rebuild for Fedora
