%undefine _debugsource_packages

Name:           zmqpp
Version:        4.2.0
Release:        1
License:        MIT
Summary:        0mq/Zeromq Highlevel C++ bindings
URL:            https://zeromq.github.io/zmqpp/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  zeromq-devel

%description
This C++ binding for 0mq/zmq is a 'high-level' library that 
hides most of the c-style interface core 0mq provides. 

%package devel
Summary:        Development headers for zmqpp
Group:  Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This C++ binding for 0mq/zmq is a 'high-level' library that
hides most of the c-style interface core 0mq provides.

This package provides development headers for zmqpp.

%prep
%setup -q

%build
%make_build all

%install
mkdir -p %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{buildroot}%{_libdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS CHANGES.md README.md LICENSE
%{_bindir}/zmqpp
%{_libdir}/libzmqpp.so.*

%files devel
%{_includedir}/zmqpp
%{_libdir}/libzmqpp.so
%exclude %{_libdir}/libzmqpp.a
%{_libdir}/pkgconfig/libzmqpp.pc

%changelog
* Fri Sep 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.2.0
- Rebuilt for Fedora
* Thu Feb 19 2015 i@marguerite.su
- initial version 4.1.1
