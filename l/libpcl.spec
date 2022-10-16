Name:           libpcl
Version:        1.12
Release:        1
Summary:        Portable Coroutine Library (PCL)
License:        GPLv2+
URL:            http://xmailserver.org/libpcl.html
Source0:        http://xmailserver.org/pcl-%{version}.tar.gz

%description
The Portable Co-routine Library (PCL) implements the low level 
functionality for co-routines in C. Co-routines are a very simple 
cooperative multitasking environment where the switch from one task
to another is done explicitly by a function call. Co-routines are a 
lot faster and require much less OS resources than processes or 
threads.

%package devel
Summary:        Development headers and libraries for pcllib
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and libraries for Portable Co-routine Library (PCL).

%prep
%setup -q -n pcl-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.a

%clean
rm -rf %{buildroot}

%files
%{_libdir}/libpcl.so.*
%doc AUTHORS COPYING

%files devel
%{_includedir}/*
%{_libdir}/libpcl.so
%{_mandir}/man3/*

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.12
- Rebuilt for Fedora
* Sun Nov 10 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.12-1
- Initial version of the package
