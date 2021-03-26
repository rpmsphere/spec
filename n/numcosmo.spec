#undefine _python_bytecompile_errors_terminate_build
%global __python __python3

Name:           numcosmo
Version:        0.15.2
Release:        1
Summary:        Numerical Cosmology
Group:          Productivity/Scientific/Physics
License:        GPL-3.0
URL:            https://github.com/NumCosmo/NumCosmo
Source0:        NumCosmo-master.zip
BuildRequires:  gtk-doc atlas-devel
BuildRequires:  gobject-introspection-devel glib2-devel gsl-devel gmp-devel mpfr-devel fftw3-devel sqlite-devel lapack-devel
BuildRequires:  nlopt-c-devel cfitsio-devel
BuildRequires:  sundials-devel
BuildRequires:  python3-devel
BuildRequires:  w3m
Patch0:         numcosmo-0.14.2-self.patch

%description
The NumCosmo is an free software C library whose main purposes 
are to test cosmological models using observational data and to 
provide a set of tools to perform cosmological calculations. 
Particularly, the current version has implemented three different 
probes: cosmic microwave background (CMB),supernovae type Ia 
(SNeIa) and large scale structure (LSS) information, such as 
baryonic acoustic oscillations (BAO) and galaxy cluster 
abundance. The code supports a joint analysis of these data and 
the parameter space can include cosmological and phenomenological 
parameters. It is worth emphasizing that NumCosmo matter power 
spectrum and CMB codes were written independently of other 
implementations such as CMBFAST, CAMB, etc.

The library is structured in such way to simplify the inclusion 
of non-standard cosmological models. Besides the functions 
related to cosmological quantities, this library also implements 
mathematical and statistical tools. The former was developed to 
enable the inclusion of other probes and/or theoretical models 
and to optimize the codes. The statistical framework comprises 
algorithms which define likelihood functions, minimization, Monte 
Carlo, Fisher Matrix and profile likelihood methods.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n NumCosmo-master
#patch0 -p1

%build
./autogen.sh --prefix=/usr --disable-static --enable-shared
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/doc/%{name}-%{version}
%{_datadir}/man/man1/*
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*
%attr(0755, root, root) %{_bindir}/*
%{_datadir}/%{name}-%{version}

%files devel
#{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/*

%changelog
* Wed Aug 26 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.15.2
- Rebuild for Fedora
* Mon Oct 29 2012 sandro@isoftware.com.br
- Added backward compat for older fftw.
* Mon Oct 29 2012 sandro@isoftware.com.br
- Removed installed INSTALL from upstream.
* Mon Oct 29 2012 sandro@isoftware.com.br
- Fixed GPL string (GPL-3.0).
