%undefine _debugsource_packages
%global __os_install_post %{nil}

Summary: The Nelson Programming Language
Name: nelson
Version: 1.13.0
Release: 1
License: GPLv2
Group: Development/Language
URL: https://nelson-lang.github.io/nelson-website/
Source0: https://github.com/nelson-lang/nelson/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: cmake gcc-c++
BuildRequires: giflib-devel libjpeg-devel libpng-devel libtiff-devel libcurl-devel
BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtsvg-devel qt5-qttools-devel
BuildRequires: eigen3-devel matio-devel openmpi-devel libsndfile-devel libgit2-devel portaudio-devel zlib-devel
BuildRequires: libicu-devel libffi-devel boost-devel alsa-lib-devel libevent-devel flexiblas-devel hdf5-devel hwloc-devel
BuildRequires: lapack-devel libgit2-devel libstdc++-devel libxml2-devel pipewire-jack-audio-connection-kit-devel taglib-devel
AutoReq: off
Requires: openmpi
Requires: qt5-qtbase-gui qt5-qtdeclarative alsa-lib boost libcurl libevent libffi flexiblas-netlib libgcc libgit2 libgomp
Requires: hdf5 hwloc-libs libicu pipewire-jack-audio-connection-kit lapack matio portaudio libsndfile libstdc++ taglib libxml2 zlib

%description
The aim of Nelson is providing a powerful open computing environment for
engineering and scientific applications using modern C/C++ libraries
(Boost, Eigen, FFTW, ...) and others state of art numerical libraries.

It has sophisticated data structures (including cell, struct, linear
systems...), an interpreter and a high level programming language.

Nelson has been developed to be an open/modular system where an user can define
these own data types and operations on these data types by using overload.

%prep
%setup -q
sed -i 's|fscanf(filepointer, np)|fscanf(filepointer, "%s", np)|' modules/stream_manager/src/cpp/FscanFunction.cpp
sed -i '13i #include <cstdint>' modules/file_archiver/src/cpp/UnzipHelpers.hpp
sed -i '58i #include <stdint.h>' modules/file_archiver/src/c/minizip/mz_os.h

%build
#cmake -G "Unix Makefiles" .
cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=release -DMPI_C_COMPILER=/usr/lib64/openmpi/bin/mpicc -DMPI_CXX_COMPILER=/usr/lib64/openmpi/bin/mpicxx -DMPI_C_INCLUDE_PATH=/usr/include/openmpi-%{_arch}/
make

%install
%make_install
#mkdir -p %{buildroot}%{_bindir}
#cd %{buildroot}%{_libexecdir}/Nelson-%{version}/bin/linux
#sed -i 's|$0|$(realpath $0)|' %{name}-*i
#for i in %{name}-*i; do
#  ln -s %{_libexecdir}/Nelson-%{version}/bin/linux/$i %{buildroot}%{_bindir}/$i
#done
#mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
#echo %{_libexecdir}/Nelson-%{version}/bin/linux > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
#echo %{_libdir}/openmpi/lib >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%files
%doc LICENSE *.md
#{_libexecdir}/*
%{_bindir}/*
%{_datadir}/Nelson
%{_includedir}/Nelson
%{_libdir}/Nelson
%{_libdir}/cmake/Nelson
%{_datadir}/applications/org.nelson.Nelson.desktop
%{_datadir}/icons/hicolor/*/apps/nelson.png
#{_datadir}/locale/*/LC_MESSAGES/nelson.mo
%{_datadir}/metainfo/org.nelson.Nelson.appdata.xml

%changelog
* Sun Apr 06 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 1.13.0
- Rebuilt for Fedora
