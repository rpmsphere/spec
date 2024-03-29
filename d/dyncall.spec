%undefine _debugsource_packages

Name:         dyncall
Summary:      Dynamic Foreign Function Call Library
URL:          https://dyncall.org/
Group:        Compiler
License:      MIT
Version:      1.0
Release:      8.1
Source0:      https://dyncall.org/r%{version}/dyncall-%{version}.tar.gz

%description
The dyncall library encapsulates architecture-, OS- and
compiler-specific function call semantics in a virtual "bind
argument parameters from left to right and then call" interface
allowing programmers to call C functions in a completely dynamic
manner. In other words, instead of calling a function directly,
the dyncall library provides a mechanism to push the function
parameters manually and to issue the call afterwards. This means,
that a program can determine at runtime what function to call, and
what parameters to pass to it. The library is written in C and
assembly and provides a very simple C interface to program against.
The library comes in very handy to power flexible message systems,
dynamic function call dispatch mechanisms, closure implementations
or even to bridge different programming languages. When it comes
to language bindings, the dyncall library provides a clean and
portable C interface to dynamically issue calls to foreign code
using small call kernels written in assembly. Instead of providing
code for every bridged function call, which unnecessarily results in
code bloat, only a couple of instructions are used to invoke every
possible call.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make} %{_smp_mflags -O}

%install
make install %{_smp_mflags} PREFIX=$RPM_BUILD_ROOT%{_prefix}
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%{_includedir}/*
%{_libdir}/lib*
#{_mandir}/man3/*

%changelog
* Tue Aug 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
