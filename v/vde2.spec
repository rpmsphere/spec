%global __os_install_post %{nil}

Name:          vde2
Version:       2.3.2
Release:       8.1
Summary:       An ethernet compliant virtual network
Group:         Network/Routing
URL:           https://vde.sourceforge.net/
Source:        https://downloads.sourceforge.net/project/vde/vde2/%{version}/vde2-%{version}.tar.bz2
License:       GPL
BuildRequires: gcc-c++
BuildRequires: automake
BuildRequires: compat-openssl10-devel
BuildRequires: libpcap-devel
BuildRequires: python2

%description
VDE is an ethernet compliant virtual network that can be spawned over a set of
physical computer over the Internet. VDE is part of virtualsquare project.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
VDE is an ethernet compliant virtual network that can be spawned over a set of
physical computer over the Internet. VDE is part of virtualsquare  project.

This package contains static libraries and header files need for development.

%prep
%setup -q
sed -i 's|/usr/bin/python$|/usr/bin/python2|' src/lib/python/VdePlug.py

%build
export PYTHON=/usr/bin/python2
%configure
make CFLAGS+="-Wno-format-security"

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%config %{_sysconfdir}/vde2/libvdemgmt/*.rc
%{_sysconfdir}/vde2/vdecmd
%{_bindir}/*
%{_sbindir}/vde_tunctl
%{_libdir}/lib*.so.*
%{_libdir}/vde2
%{_libexecdir}/vdetap
%{_mandir}/man1/*.1*
%{_mandir}/man8/vde_tunctl.8*
%doc COPYING README
%{python2_sitelib}/VdePlug*
%{python2_sitelib}/vdeplug_python.*

%files devel
%{_includedir}/*.h
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jan 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuilt for Fedora
* Mon Jun 21 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 2.2.3-1mamba
- package created by autospec
