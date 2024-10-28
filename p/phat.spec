%undefine _debugsource_packages

Summary: Persistent Homology Algorithm Toolbox
Name:          phat
Version:       1.6
Release:       1
License:       GPLv2+, LGPL
URL:           https://phat.googlecode.com
Source0:       %{name}-%{version}.tar.gz
#BuildRequires: gtk2-devel
#BuildRequires: libgnomecanvas-devel
#BuildRequires: chrpath
#BuildRequires: /usr/bin/gtkdocize gcc-c++
BuildRequires: python3-pybind11
Group: System/Libraries

%description
This software library contains methods for computing the persistence pairs
of a filtered cell complex represented by an ordered boundary matrix with
Z2 coefficients.

%package devel
Group: Development/Other
Summary: Header files for PHAT 
BuildArch: noarch

%description devel
The Persistent Homology Algorithm Toolox is a header-only C++ library
for performing the filtered Z/2Z (co)boundary matrix operations
commonly needed when computing (persistent) (co)homology in
topological data analysis.

%package utils
Group: Development/Other
Summary: Utilities from the PHAT library

%description utils
This package contains some standalone utilities built using the PHAT
library, such as persistent homology of a given filtered boundary
matrix.

%package -n python3-%{name}
Group: Development/Other
Summary: Python 3 interface for the PHAT library

%description -n python3-%{name}
This package contains the PHAT library's Python 3 interface.

%prep
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr
%make_build 
%{py3_build}

%install
#make_install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 benchmark %{buildroot}%{_bindir}/%{name}-benchmark
install -Dm755 convert %{buildroot}%{_bindir}/%{name}-convert
install -Dm755 info %{buildroot}%{_bindir}/%{name}-info
install -d %{buildroot}%{_includedir}
cp -a include/%{name} %{buildroot}%{_includedir}
%{py3_install}

%files devel
%doc COPYING* README.md
%{_includedir}/%{name}

%files utils
%{_bindir}/phat*

%files -n python3-%{name}
%{python3_sitearch}/*

%changelog
* Sun Dec 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
