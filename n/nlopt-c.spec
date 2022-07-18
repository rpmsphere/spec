%global __os_install_post %{nil}
%define __python /usr/bin/python2
%global _name nlopt

Name:           nlopt-c
Version:        2.4.2
Release:        12.1
Summary:        A library for nonlinear optimization
License:        LGPL-2.0
Group:          Development/Libraries/C and C++
URL:            http://ab-initio.mit.edu/wiki/index.php/NLopt
Source0:        http://ab-initio.mit.edu/%{_name}/%{_name}-%{version}.tar.gz
#BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  fltk, octave-devel, java-1.8.0-openjdk-headless, lua
BuildRequires:  python2-devel
BuildRequires:  gnuplot
BuildRequires:  numpy
BuildRequires:  atlas urw-fonts
Patch0:         NLopt-octave4.patch
BuildRequires:  llvm-devel

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python-%{name}
Summary:        A library for nonlinear optimization
Group:          Development/Libraries/Python
Requires:       numpy

%description -n python-%{name}
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package -n octave-%{name}
Summary:        A library for nonlinear optimization
Group:          Productivity/Scientific/Math
Requires:       octave

%description -n octave-%{name}
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ifarch x86_64 aarch64
test -d %{buildroot}%{_prefix}/lib && \
     mv %{buildroot}%{_prefix}/lib/python*/* %{buildroot}%{python_sitearch} && \
     rm -rf %{buildroot}%{_prefix}/lib
%endif

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{_name}.pc
%{_mandir}/man3/%{_name}.*

%files -n python-%{name}
%{python3_sitearch}/*

#files -n octave-%{name}
#dir %{_libdir}/octave/*/site
#dir %{_libdir}/octave/*/site/oct
#dir %{_libdir}/octave/*/site/oct/*
#{_libdir}/octave/*/site/oct/*/*.oct
#{_datadir}/octave/*/site/m/*

%changelog
* Tue Dec 23 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.2
- Rebuilt for Fedora
* Sun Aug 19 2012 scorot@free.fr
- again fix build on x86_64
* Sun Aug 19 2012 scorot@free.fr
- fix build on x86_64
- fix package group names
* Sun Aug 19 2012 scorot@free.fr
- first package
