%global debug_package %{nil}

Name: waave
Summary: Why Another Audio Video Engine
Version: 3.01
Release: 12.1
Group: Development/Libraries
License: GPLv3
URL: http://waave.sourceforge.net/
Source0: http://sourceforge.net/projects/waave/files/%{name}/%{name}-%{version}.tar.gz
BuildRequires: SDL-devel
BuildRequires: compat-ffmpeg-devel

%description
Waave intent to be a simple, modular and multi-contextual audio/video library
based on FFmpeg and SDL.

%package devel
Summary: Development files for WAAVE
Requires: %{name}

%description devel
Header files and Libraries for the package WAAVE.

%prep
%setup -q
sed -i 's|AV_CH_LAYOUT_STEREO|CH_LAYOUT_STEREO|' src/waave_ffmpeg.c
sed -i 's|extended_data|data|' src/waave_ffmpeg.c

%build
export CFLAGS="-fPIC -I/usr/include/compat-ffmpeg"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/WAAVE.h
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.01
- Rebuild for Fedora
