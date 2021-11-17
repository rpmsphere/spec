#undefine _missing_build_ids_terminate_build

Summary: The Pure Programming Language
Name: pure
Version: 0.68
Release: 1
License: LGPLv3
Group: Development/Language
URL: https://agraef.github.io/pure-lang/
Source0: https://github.com/agraef/pure-lang/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires: llvm34-devel

%description
Pure is a modern-style functional programming language based on term rewriting.
It offers equational definitions with pattern matching, full symbolic rewriting
capabilities, dynamic typing, eager and lazy evaluation, lexical closures,
built-in list and matrix support and an easy-to-use C interface. The interpreter
uses LLVM as a backend to JIT-compile Pure programs to fast native code.

Pure is the successor of the author's Q language. It offers many new and powerful
features and programs run much faster than their Q equivalents. It also
integrates nicely with a number of other computing environments, most notably
Faust, Pure Data, Octave, Reduce and TeXmacs. A fairly extensive collection of
addon modules is available, which makes Pure usable as a compiled scripting
language for a variety of purposes.

%prep
%setup -q

%build
export LLVMCONF=llvm-config-3.4
%configure
%make_build

%install
#install -Dm755 %{name} %{buildroot}%{_bindir}/%{_name}
%make_install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc COPYING* TODO ChangeLog NEWS
%{_bindir}/%{name}

%changelog
* Sun Sep 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.68
- Rebuilt for Fedora
