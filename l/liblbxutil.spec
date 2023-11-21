Name:          liblbxutil
Version:       1.1.0
Release:       4.1
Summary:       X.Org lbxutil library
Group:         System/Libraries
URL:           https://x.org
Source:        ftp://x.org/pub/individual/lib/liblbxutil-%{version}.tar.bz2
License:       MIT
BuildRequires: xorg-x11-proto-devel

%description
X.Org lbxutil library.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
X.Org lbxutil library.

This package contains static libraries and header files need for development.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/liblbxutil.so.*
%doc AUTHORS COPYING ChangeLog README

%files devel
%{_includedir}/X11/extensions/lbx*.h
%{_libdir}/liblbxutil.a
#{_libdir}/liblbxutil.la
%{_libdir}/liblbxutil.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
* Wed Jan 13 2010 Automatic Build System <autodist@mambasoft.it> 1.1.0-1mamba
- automatic update by autodist
* Sun Feb 08 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.1-2mamba
- specfile updated
* Tue Dec 26 2006 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.1-1qilnx
- package created by autospec
