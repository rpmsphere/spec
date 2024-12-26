Name: xbps
Summary: The X Binary Package System
Version: 0.59.2
Release: 1
Group: System/Libraries
License: BSD
URL: https://github.com/voidlinux/xbps
Source0: %{name}-%{version}.tar.gz
BuildRequires: openssl-devel
BuildRequires: libarchive-devel
BuildRequires: libconfuse-devel

%description
The X Binary Package System (in short XBPS) is a new binary package system
designed and implemented from scratch. Its goal is to be fast, easy to use,
bug-free, featureful and portable as much as possible.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
%configure
#make %{?_smp_mflags} CFLAGS="%{optflags} -std=gnu99 -Wno-error -fPIC"
make %{?_smp_mflags} CFLAGS="%{optflags} -Wno-error -fPIC"

%install
%make_install

%files
%doc TODO README.md NEWS LICENSE* 3RDPARTY
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_mandir}/man?/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/xbps.d
%{_datadir}/zsh/site-functions/*
#%{_sysconfdir}/xbps/xbps.conf
/var/db/xbps

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.a
%{_libdir}/lib*.so

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.59.2
- Rebuilt for Fedora
