Name: kite-llvm
Summary: A rewrite of Kite to use LLVM
Version: 0.3.0
Release: 1
Group: Development/Languages
License: GPL
URL: https://github.com/tmiw/kite-llvm
#Source0: https://www.kite-language.org/files/%{name}-%{version}.tar.gz
Source0: https://github.com/tmiw/kite-llvm/archive/refs/heads/master.zip#/%{name}-master.zip
BuildRequires: llvm-devel, libgc-devel, boost-devel, openssl-devel, libffi-devel
Obsoletes: kite <= 1.0.4

%description
Kite is a programming language designed to minimize the required experience
level of the programmer -- quick development and running time and low CPU and
memory usage (the binary is around 250KB stripped on OSX, for instance).

%prep
%setup -q -n %{name}-master

%build
autoreconf -ifv
%configure
%make_build

%install
%make_install

%files
%doc README
%{_bindir}/*
%{_libdir}/libkite.*
%{_datadir}/%{name}

%changelog
* Sun Apr 17 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuild for Fedora
