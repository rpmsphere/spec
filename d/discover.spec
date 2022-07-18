%global __os_install_post %{nil}

Name: discover
Summary: Hardware Detection System
Version: 2.1.2
Release: 10.1
Group: Applications/System
License: GPLv2
URL: https://launchpad.net/discover
Source0: https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.orig.tar.gz
BuildRequires: expat-devel
BuildRequires: libcurl-devel

%description
Discover is a cross-platform hardware detection system that uses
system-dependent modules (selected at build time) for detecting
the hardware on a system.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
%configure --disable-static
make -i %{?_smp_mflags} CFLAGS+="-Wno-format-security -fPIC" LDFLAGS+="-shared -L%{_libdir}"

%install
sed -i 's|555|755|' lib/Makefile
%make_install -i
cp AUTHORS LICENSE RELEASE README %{buildroot}%{_datadir}/doc/%{name}

%files
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*
%{_libdir}/lib*.so.*
%{_datadir}/%{name}
%{_sysconfdir}/%{name}*

%files devel
%{_datadir}/doc/%{name}
%{_includedir}/*
#{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%changelog
* Fri Nov 01 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.2
- Rebuilt for Fedora
