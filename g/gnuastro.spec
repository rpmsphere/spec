Name:           gnuastro
Version:        0.23
Release:        1
Summary:        GNU Astronomy Utilities
License:        GPL-3.0+
URL:            https://www.gnu.org/software/gnuastro/
Source0:        https://ftp.gnu.org/pub/gnu/gnuastro/%{name}-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(wcslib)

%description
The GNU Astronomy Utilities (Gnuastro) contains various programs and
library functions for the manipulation and analysis of astronomical
data.

%package devel
Summary:        Development files for gnuastro
Requires:       %{name} = %{version}

%description devel
Development files required for development with GNU Astronomy
Utilities (Gnuastro).

%package doc
Summary:        Documentation for the GNU Astromomy Utilities
BuildArch:      noarch

%description doc
Additional documentation for the GNU Astromomy Utilities.

%prep
%setup -q

%build
%configure \
        --docdir=%{_docdir}/%{name} \
        --disable-static \
        --disable-rpath \
        CPPFLAGS="$(pkg-config cfitsio --cflags)"
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING*
%doc ChangeLog README NEWS THANKS AUTHORS
%config %{_sysconfdir}/%{name}/*.conf
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_libdir}/libgnuastro.so.*
%{_libdir}/libgnuastro_make.so.*
%{_datadir}/gnuastro

%files devel
%license COPYING*
%{_includedir}/gnuastro
%{_libdir}/libgnuastro.so
%{_libdir}/libgnuastro_make.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_infodir}/gnuastro.info*.gz
%{_infodir}/gnuastro-figures
%exclude %{_infodir}/dir

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.23
- Rebuilt for Fedora
* Tue Nov 26 2019 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.11 (library 9.0.0):
  * documentation updates
  * Updates and extensions to multiple operations
- drop upstreamed patch
  0001-Reference-wcslib-by-correct-name-in-gnuastro.pc-pkgc.patch
* Sun Nov 10 2019 Stefan Brüns <stefan.bruens@rwth-aachen.de>
- Fix wrong automatic pkgconfig(wcs) requires, add
  0001-Reference-wcslib-by-correct-name-in-gnuastro.pc-pkgc.patch
- Drop ghostscript BuildRequires, only needed for running tests
  (not done), the PDF exporter is built unconditionally. At runtime,
  the exporter uses a "gs" executable in PATH, so add a Recommends.
- Add bcond for running tests, keep it disabled by default.
* Sun Nov  3 2019 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.10 (library 8.0.0):
  * Report/warn when using arrays memory-mapped to non-volatile
    storage. Users should use --minmapsize to allow use of available
    RAM, --quietmmap' option to disable the messages
  * Various additions and extensions to operators and tools
  * crop now supports 3D datasets (data cubes)
  * documentation updates and bug fixes
- includes changes from 0.9:
  * --checkconfig: print the names and values given to options as
    they are parsed on the command-line or in various configuration
    files
  * Multithreaded operation for many operators
  * Add bash scripts for common higher-level usage
* Fri Dec 28 2018 astieger@suse.com
- update to 0.8:
  * various improvements to input/output handling of all programs
  * Various functional updates and fixes to multiple commands
  * NoiseChisel: New outlier identification algorithm for quantile
    thresholds
* Sun Aug 12 2018 jengelh@inai.de
- Use pkg-config instead of hardcoding the cfitsio path.
- Wrap descriptions consistently.
- Fix RPM group of shared library subpackage.
* Sat Aug 11 2018 astieger@suse.com
- initial package (0.7)
