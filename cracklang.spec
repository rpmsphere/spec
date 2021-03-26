Name: cracklang
Summary: Crack scripting language
Version: 1.6
Release: 1
Group: Development/Language
License: MPL-2.0
URL: https://github.com/crack-lang/crack
Source0: http://crack-lang.org/downloads/crack-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gtk2-devel pcre-devel SDL-devel cairo-devel libcurl-devel
#BuildRequires: llvm-devel
#BuildRequires: llvm-static
BuildRequires: llvm34-devel
BuildRequires: llvm34-static
#BuildRequires: lmdb-devel
#BuildRequires: netcdf-devel

%description
Crack aims to provide the ease of development of a scripting language with the
performance of a compiled language. The "crack" program is a "script executor"
that compiles source to machine code on the fly (it will eventually cache the
code to intermediate formats as appropriate). It can also compile a script to
a native binary.

The crack language itself derives concepts from C++, Java and Python, incorpo-
rating object-oriented programming, operator overloading and strong typing.

%package devel
Summary: Development files for Crack
Requires: %{name}

%description devel
Header files and Libraries for the package Crack.

%prep
%setup -q -n crack-%{version}
sed -i 's| jit||' configure m4/llvm.m4 cmake/modules/FindLLVM.cmake
#sed -i '2452s|errors, 0|errors|' builder/llvm/LLVMBuilder.cc
sed -i '/JITExceptionHandling/d' builder/llvm/LLVMJitBuilder.cc
sed -i 's|PathV1.h|Path.h|' builder/llvm/Native.cc
##sed -i '39s|src.read(\&ch, 1)|bool(src.read(\&ch, 1))|' parser/Toker.cc
#sed -i '/OwningPtr.h/d' builder/llvm/LLVMBuilder.h
#sed -i 's|<llvm/|<llvm/IR/|' builder/llvm/DebugInfo.h builder/llvm/BTypeDef.h

%build
autoheader
%cmake -DCMAKE_CXX_FLAGS="-fpermissive -I/usr/include/llvm34"
make

%install
make install DESTDIR=%{buildroot}
#ifarch x86_64
#mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
#endif

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/crack*
%{_libdir}/crack*
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/crack*
%{_libdir}/lib*.so

%changelog
* Mon Jan 20 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuild for Fedora
