%global debug_package %{nil}

Name: ponylang
Summary: Compiler for the Pony Language
Version: 0.37.0
Release: 1
Group: Development/Language
License: BSD
URL: https://github.com/ponylang/ponyc
Source0: https://github.com/ponylang/ponyc/archive/%{version}.tar.gz#/ponyc-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gmock
BuildRequires: llvm-devel
BuildRequires: libatomic
BuildRequires: google-benchmark-devel
BuildRequires: gtest-devel

%description
Pony is an open-source, actor-model, capabilities-secure, high performance
programming language.

%prep
%setup -q -n ponyc-%{version}
sed -i 's|-Werror|-Wno-error -Wno-stringop-overflow|' Makefile
#sed -i 's|llvm-config|llvm-config-7.0-64|' Makefile

%build
cmake . -DLLVM_DIR=%{_libdir}/cmake/llvm -DGTest_DIR=%{_libdir}/cmake/GTest -Dbenchmark_DIR=%{_libdir}/cmake/benchmark -DPONY_BUILD_CONFIG=release
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
* Tue Sep 1 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.37.0
- Rebuild for Fedora
