%global debug_package %{nil}

Name:      mupen64plus
Summary:   Nintendo 64 emulator and plugins
Version:   2.5
Release:   6.1
Group:     Applications/Emulators
License:   GPLv2
URL:       https://github.com/mupen64plus/mupen64plus-core
Source:    mupen64plus-bundle-src-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: SDL-devel, libpng-devel, gtk2-devel, SDL_ttf-devel, lirc-devel, boost-devel

%description
Mupen64Plus is a cross-platform plugin-based N64 emulator which is capable of
accurately playing many games. Included are four MIPS R4300 CPU emulators, with
dynamic recompilers for 32-bit x86 and 64-bit amd64 systems, and necessary
plugins for audio, graphical rendering (RDP), signal co-processor (RSP), and
input. There is 1 included OpenGL video plugin, called RiceVideo. There are 3
other excellent video plugins being maintained by wahrhaft, called Arachnoid,
Glide64, and Z64.

%package devel
Summary:  Mupen64plus Headers
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains headers for mupen64plus plugins.

%prep
%setup -qn mupen64plus-bundle-src-%{version}
##sed -i 's|x86_64 amd64|x86_64 aarch64 amd64|' source/mupen64plus-*/projects/unix/Makefile

%build
export LDFLAGS=-Wl,--allow-multiple-definition
CC="gcc $RPM_OPT_FLAGS" CXX="g++ $RPM_OPT_FLAGS" \
COREDIR=%_libdir/%name/ PLUGINDIR=%_libdir/%name LIRC=1 bash -x m64p_build.sh

%install
PREFIX=$RPM_BUILD_ROOT/usr \
LIBDIR=$RPM_BUILD_ROOT%_libdir/%name \
MANDIR=$RPM_BUILD_ROOT%_mandir bash -x m64p_install.sh

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%_bindir/mupen64*
%_libdir/mupen64plus
%_datadir/mupen64plus
%doc %_mandir/*
%_datadir/applications/mupen64plus.desktop
%_datadir/icons/hicolor/*/apps/mupen64plus.*

%files devel
%_includedir/%name

%changelog
* Thu Aug 17 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
* Sun Oct 14 2012 TingPing <tingping@tingping.se> - 1.99.5-1
- first version for fedora based off opensuse's package
