%global debug_package %{nil}

Summary:        X Settings Libraries for GPE
Name:           libxsettings-client
Version:        0.17
Release:        11.1
License:        LGPL
Group:          System Environment/Libraries
URL:            http://gpe.linuxtogo.org/
Source:         http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:  glib2-devel, gtk2-devel, pkgconfig, gtk-doc
BuildRequires:  w3m

%description
GPE X Settings client library.
Library providing utility functions for the Xsettings protocol.
This library is used for applications making use of the Xsettings
configuration setting propagation protocol.

%package devel
Group:          Development/Libraries
Summary:        Static libraries and header files from %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for %{name}
This package contains headers and other files required to compile
software using the Xsettings library.

%prep
%setup -q

%build
./autogen.sh
./configure --prefix=/usr --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%{_libdir}/*.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/xsettings*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
* Thu Apr 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.17
- Rebuild for Fedora
* Thu Jan 24 2008 d.marlin <dmarlin@redhat.com> - 0.17-1
- First cut at packaging RPM.
