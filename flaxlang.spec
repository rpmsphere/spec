Summary: Compiled, low-level programming language with LLVM
Name: flaxlang
Version: 0.42.0
Release: 1
License: Apache 2.0
Group: Development/Languages
Source: https://github.com/flax-lang/flax/archive/%{version}.tar.gz#/flax-%{version}.tar.gz
URL: https://github.com/flax-lang/flax
BuildRequires: llvm-devel
BuildRequires: mpfr-devel
BuildRequires: gmp-devel

%description
A low level language with high level syntax and expressibility, aimed at OSDev work.

%prep
%setup -q -n flax-%{version}
#sed -i 's|usr/local|usr|' makefile source/frontend/arguments.cpp

%build
#make LLVM_CONFIG=llvm-config-64
make

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}/usr/local
cp -a build/sysroot/usr/local/bin %{buildroot}/usr/bin
cp -a build/sysroot/usr/local/lib %{buildroot}/usr/local/lib

%files 
%doc LICENSE *.md
%{_bindir}/*
/usr/local/lib/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jan 27 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.42.0
- Rebuild for Fedora
