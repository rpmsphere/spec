Name:          libxkbui
Version:       1.0.2
Release:       4.1
Summary:       X.Org xkbui library
Group:         System/Libraries
URL:           https://x.org
Source:        https://ftp.x.org/pub/individual/lib/libxkbui-%{version}.tar.bz2
License:       MIT
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXt-devel

%description
X.Org xkbui library.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
Obsoletes:     libXorg-devel

%description devel
X.Org xkbui library.
This package contains static libraries and header files need for development.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%{_libdir}/libxkbui.so.*
%doc COPYING ChangeLog

%files devel
%{_libdir}/libxkbui.a
#{_libdir}/libxkbui.la
%{_libdir}/libxkbui.so
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
* Sat Jun 21 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.2-2mamba
- specfile updated
* Mon Dec 18 2006 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.2-1qilnx
- package created by autospec
