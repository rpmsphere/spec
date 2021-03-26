Name: linda
Summary: Simple C-Linda with Posix Threads
Version: 0.1.1
Release: 7.1
Group: Development/Languages
License: GPLv2
URL: http://sourceforge.net/projects/linda/
Source0: http://sourceforge.net/projects/linda/files/%{version}/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel

%description
This a simple implementation of Linda using Posix threads. The prime motivation
is to use it to teach my parallel programming course. The program was written
for Posix threads and should run on any platform supporting Posix threads,
although I've only tried it on Sun Solaris 2. The only other thing that may
give problem if you attempt to port it is the variable argument library calls.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README* HACKING COPYING ChangeLog AUTHORS
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuild for Fedora
