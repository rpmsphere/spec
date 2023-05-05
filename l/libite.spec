Summary: That missing frog DNA you've been looking for
Name: libite
Version: 2.5.2
Release: 1
License: MIT
Group: Applications
Source0: https://github.com/troglobit/libite/releases/download/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/troglobit/libite
BuildRequires: automake

%description
Libite is a lightweight library of frog DNA that can be used to fill the gaps
in any dinosaur project. It holds useful functions and macros developed by
both Finit and the OpenBSD project. Most notably the string functions:
strlcpy(3), strlcat(3) and the highly useful *BSD sys/queue.h and sys/tree.h API's.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%{configure}
%{make_build}

%install
%{make_install}

%files
%{_docdir}/%{name}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_includedir}/lite

%changelog
* Sun Nov 13 2022 root <root@localhost.localdomain> - 2.5.2
- Rebuilt for Fedora
