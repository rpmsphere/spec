Name:          libXprintUtil
Version:       1.0.1
Release:       4.1
Summary:       X.Org XprintUtil library
Group:         System/Libraries
URL:           https://x.org
Source:        ftp://ftp.freedesktop.org/pub/individual/lib/libXprintUtil-%{version}.tar.bz2
License:       MIT
BuildRequires: gcc-c++
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libXp-devel
BuildRequires: libXt-devel

%description
X.Org XprintUtil library.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
X.Org XprintUtil library.

This package contains static libraries and header files need for development.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/libXprintUtil.so.*
%doc COPYING ChangeLog

%files devel
%{_libdir}/libXprintUtil.a
#{_libdir}/libXprintUtil.la
%{_libdir}/libXprintUtil.so
%{_includedir}/X11/XprintUtil/xprintutil.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuilt for Fedora
* Thu Mar 13 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.1-2mamba
- ... add a changelog entry
* Thu Dec 21 2006 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.1-1qilnx
- package created by autospec
