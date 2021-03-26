%global _name CPU-X

Name: cpu-x
Version: 3.2.4
Release: 1
Summary: A Free software that gathers information on CPU, motherboard and more
License: GPLv3+
Group: System/Kernel and hardware
URL: https://github.com/X0rg/CPU-X
Source: https://github.com/X0rg/CPU-X/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Buildrequires: cmake
Buildrequires: vim-common
%ifarch x86_64
Buildrequires: libcpuid-devel
%endif
Buildrequires: gcc-c++ pkgconfig(gtk+-3.0) pkgconfig(libarchive) pkgconfig(libcurl) pkgconfig(libpci) pkgconfig(libprocps) pkgconfig(libstatgrab) pkgconfig(ncurses)

%description
CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and Open Source
software designed for GNU/Linux; also, it works on *BSD.
This software is written in C and built with CMake tool.
It can be used in graphical mode by using GTK or in text-based mode by using
NCurses. A dump mode is present from command line.

%prep
%setup -q -n %{_name}-%{version}

%build
%cmake
%make_build

%install
%make_install
install -d %{buildroot}%{_libdir}
install -m755 src/lib*.so %{buildroot}%{_libdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%_bindir/*
%_datadir/%name
%_datadir/icons/hicolor/*/*/*
%_datadir/applications/*
%_datadir/polkit-1/actions/org.pkexec.cpu-x.policy
%_datadir/locale/*/LC_MESSAGES/cpu-x.mo
%_datadir/metainfo/cpu-x.appdata.xml
%_libdir/lib*.so

%changelog
* Fri Oct 18 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.4
- Rebuild for Fedora
* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 3.2.2-alt1
- new version 3.2.2
* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1
- new version 3.2.1
* Wed Jan 10 2018 Anton Midyukov <antohami@altlinux.org> 3.1.3.1-alt1
- new version 3.1.3.1
* Mon Sep 18 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt2
- fix run as root for sysvinit
* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1
- new version 3.1.3
* Mon Oct 24 2016 Anton Midyukov <antohami@altlinux.org> 3.1.2-alt1
- Initial build for Alt Linux Sisyphus.
