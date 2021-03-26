Name: minuit
Summary: Minimizing general N-dimensional functions in high-energy physics
Version: 1.7.9p1
Release: 3.1
Group: Applications/Engineering
License: BSD
URL: http://seal.web.cern.ch/seal/snapshot/work-packages/mathlibs/minuit/
Source0: Minuit-1_7_9-patch1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
MINUIT is a physics analysis tool for function minimization. The functions
(so-called objective functions, can be chisquare, likelihood or user defined)
are provided by the user. MINUIT contains several tools for minimizing a
function and for special error analysis. MINUIT was initially written in
Fortran about 25 years ago at CERN by Fred James. Its main field of usage is
statistical data analysis of experimental data recorded at CERN, but it is
also used by people outside high energy physics (HEP). This project aims to
re-implement MINUIT in an object-oriented way using C++.

%package devel
Summary: Development files for Minuit
Requires: %{name}

%description devel
Header files and Libraries for the package Minuit.

%prep
%setup -q -n Minuit-1_7_9

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/Minuit
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.9
- Rebuild for Fedora
