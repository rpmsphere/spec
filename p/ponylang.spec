%undefine _debugsource_packages

Name: ponylang
Summary: Compiler for the Pony Language
Version: 0.33.0
#Version: 0.36.0
Release: 1
Group: Development/Language
License: BSD
URL: https://github.com/ponylang/ponyc
Source0: https://github.com/ponylang/ponyc/archive/%{version}.tar.gz#/ponyc-%{version}.tar.gz
BuildRequires: llvm7.0-devel
BuildRequires: llvm7.0-static
BuildRequires: libatomic

%description
Pony is an open-source, actor-model, capabilities-secure, high performance
programming language.

%prep
%setup -q -n ponyc-%{version}
sed -i 's|-Werror|-Wno-error -Wno-stringop-overflow|' Makefile
sed -i 's|llvm-config|llvm-config-7.0-64|' Makefile

%build
#cmake . -DLLVM_DIR=%{_libdir}/cmake/llvm -DGTest_DIR=%{_libdir}/cmake/GTest -Dbenchmark_DIR=%{_libdir}/cmake/benchmark -DPONY_BUILD_CONFIG=release
make %{?_smp_mflags}

%install
make install prefix=%{buildroot}/usr ponydir=%{buildroot}%{_libdir}/pony
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib/* %{buildroot}/usr/lib64/
%endif

%files
%{_bindir}/ponyc
%{_includedir}/pony/detail/atomics.h
%{_includedir}/pony.h
%{_libdir}/libpony*.a
%{_libdir}/pony

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.33.0
- Rebuilt for Fedora
