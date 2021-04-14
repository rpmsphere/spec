Name:         libghttp
Summary:      GNOME HTTP Client Library
URL:          http://www.gnome.org/
Group:        Web
License:      GPL/LGPL
Version:      1.0.9
Release:      20.1
Source0:      ftp://ftp.gnome.org/pub/GNOME/sources/libghttp/%{V_major}/libghttp-%{version}.tar.gz

%description
The gHTTP library is designed to be simple and easy to use while
still allowing you to get your feet wet at the protocol layer if
you have to. It is also designed with graphical, non-threaded
applications in mind. You should be able to use the library in
your application and never block waiting to send or recieve data
to a remote server. The main thread of execution should always be
available to refresh its display.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
./configure \
    --host=i386-pc-linux-gnu \
    --prefix=%{_prefix} \
    --libdir=%{_libdir}
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT

%files
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/ghttpConf.sh

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.9
- Rebuilt for Fedora
