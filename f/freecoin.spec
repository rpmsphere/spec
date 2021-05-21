Name: freecoin
Summary: Bitcoin integration/staging tree
Version: 0.4.0
Release: 1
Group: System Environment/Daemons
License: GPL
URL: https://github.com/dyne/freecoin
Source0: https://files.dyne.org/freecoin/%{name}-%{version}.tar.gz
BuildRequires: glib2-devel
BuildRequires: openssl-devel
BuildRequires: libcurl-devel
BuildRequires: boost-devel
BuildRequires: libdb-cxx-devel

%description
Freecoin is a versatile implementation of a bitcoin daemon.

%prep
%setup -q
sed -i 's|array<int, 10>|boost::array<int, 10>|' src/net.h src/net.cpp
#sed -i 's|a\.Serialize|a.serialize|' src/serialize.h

%build
%configure
make %{?_smp_mflags} LDFLAGS+="-ldb_cxx-5.3 -lboost_system -lboost_filesystem -lboost_thread -lcrypto" CXXFLAGS+="-fPIC -Wno-narrowing"

%install
%make_install

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/*
%{_libdir}/libfreecoin.*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
