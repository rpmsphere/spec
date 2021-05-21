Name: giac
Summary: Computer algebra system
Version: 1.2.2
Release: 5.4
License: see /usr/share/doc/giac/copyright
Group: Applications/Engineering
Source: http://www-fourier.ujf-grenoble.fr/~parisse/giac/%{name}-%{version}.tar.gz
URL: http://www-fourier.ujf-grenoble.fr/~parisse/giac.html
BuildRequires: gcc-c++, latex2html
BuildRequires: readline-devel, mpfr-devel, gmp-devel, gsl-devel, mesa-libGL-devel, ntl-devel, pari-devel
BuildRequires: fltk-devel
BuildRequires: sane-backends-libs, atlas-devel

%description
Giac Is A Cas (computer algebra system). It is under active development and
consists of:
   - a C++ library (libgiac)
   - a command line interpreter (icas)
   - a FLTK-based GUI (xcas)
Bernard Parisse is the main author of the CAS of HP40G and HP49G calculators.

%package devel
Summary: Development files for libgiac
Requires: %{name}

%description devel
Development files for libgiac.

%prep
%setup -q

%build
%configure --enable-gui
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm %{buildroot}%{_datadir}/info/dir

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_datadir}/doc/giac
%{_datadir}/giac
%{_datadir}/info/giac_*.info.gz
%{_datadir}/locale/*/LC_MESSAGES/giac.mo
%{_libdir}/libgiac.so.*
%{_datadir}/applications/xcas.desktop
%{_datadir}/application-registry/xcas.applications
%{_datadir}/pixmaps/xcas.xpm
%{_datadir}/icons/hicolor/*/*/*.png

%files devel
%{_includedir}/giac
%{_libdir}/libgiac.a
%{_libdir}/libgiac.la
%{_libdir}/libgiac.so

%changelog
* Tue Feb 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.2
- Rebuilt for Fedora
