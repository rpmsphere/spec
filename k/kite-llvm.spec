Name: kite-llvm
Summary: A rewrite of Kite to use LLVM
Version: 0.2.0
Release: 49.1
Group: Development/Languages
License: GPL
URL: https://github.com/tmiw/kite-llvm
Source0: http://www.kite-language.org/files/%{name}-%{version}.tar.gz
BuildRequires: llvm34-devel, libgc-devel, boost-devel, openssl-devel, libffi-devel
BuildRequires: llvm34-static

%description
Kite is a programming language designed to minimize the required experience
level of the programmer -- quick development and running time and low CPU and
memory usage (the binary is around 250KB stripped on OSX, for instance).

%prep
%setup -q
cp %{_includedir}/ffi*.h src/stdlib
cp %{_includedir}/ffi*.h src/stdlib/System
sed -i 's|FFI_HEADER|"ffi.h"|' src/stdlib/api.cpp src/stdlib/System/method.cpp

%build
autoreconf -i
sed -i '17121s|succeeded=no|succeeded=yes|' configure
sed -i 's|llvm/Analysis/DebugInfo.h|llvm/DebugInfo.h|' src/codegen/llvm_node_codegen.cpp
sed -i -e 's|llvm/DerivedTypes.h|llvm/IR/DerivedTypes.h|' -e 's|llvm/Support/IRBuilder.h|llvm/IR/IRBuilder.h|' -e 's|llvm/LLVMContext.h|llvm/IR/LLVMContext.h|' -e 's|llvm/Module.h|llvm/IR/Module.h|' src/codegen/llvm_compile_state.h
sed -i -e 's|llvm/Analysis/DebugInfo.h|llvm/DebugInfo.h|' -e 's|llvm/Analysis/DIBuilder.h|llvm/DIBuilder.h|' src/codegen/llvm_compile_state.h
sed -i -e 's|llvm/LLVMContext.h|llvm/IR/LLVMContext.h|' -e 's|llvm/Target/TargetData.h|llvm/Target/TargetOptions.h|' src/stdlib/language/kite.cpp
%ifarch x86_64
sed -i 's|llvm-config|llvm-config-64-3.4|' configure
%else
sed -i 's|llvm-config|llvm-config-32-3.4|' configure
%endif
%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%doc README
%{_bindir}/*
%{_libdir}/libkite.*
%{_datadir}/%{name}

%changelog
* Sun Jun 02 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
