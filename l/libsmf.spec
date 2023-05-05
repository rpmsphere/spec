%global __spec_install_post %{nil}
%undefine _debugsource_packages

Name:		libsmf
Version:	1.3
Release:	1
Summary:	Library for handling SMF ("*.mid") files.
Group:		System/Libraries
License:	BSD
Source:		libsmf-1.3.tar.xz
URL:		http://sourceforge.net/projects/libsmf/files/libsmf/
BuildRequires:  readline-devel

%description
LibSMF is a BSD-licensed C library for handling SMF ("*.mid") files.
It transparently handles conversions between time and pulses, tempo
map handling etc. The only dependencies are C compiler and glib. Full
API documentation and examples are included.

%package devel
Summary:	Development headers for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
LibSMF is a BSD-licensed C library for handling SMF ("*.mid") files.
It transparently handles conversions between time and pulses, tempo
map handling etc. The only dependencies are C compiler and glib. Full
API documentation and examples are included.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/%{_libdir}/*.la

%files
%{_bindir}/smfsh
%{_mandir}/man1/smfsh.1*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/smf.pc

%clean
rm -rf %{buildroot}

%changelog
* Sun Dec 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
* Sun Feb 24 2013 gseaman <galen.seaman at comcast.net> 1.3-1gseaman2013
- first build for PCLinuxOS
