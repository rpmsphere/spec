Name: llvm-qbasic
Summary: LLVM based QBASIC compiler
Version: 0.09.git
Release: 19.1
Group: Development/Language
License: GPLv3
URL: https://github.com/microcai/llvm-qbasic
Source0: %{name}-master.zip
BuildRequires: cmake
BuildRequires: libffi-devel
BuildRequires: boost-devel boost-static
BuildRequires: llvm3.7-devel llvm3.7-static
#BuildRequires: llvm3.9-devel llvm3.9-static
#BuildRequires: llvm35-devel llvm35-static

%description
llvm-qbc is a QBASIC compiler as well as an runtime library.

%prep
%setup -q -n %{name}-master
sed -i 's|return arg_it;|return getptr(ctx);|' compiler/codegen.cpp

%build
%cmake
make

%install
make install DESTDIR=%{buildroot}

%files
%doc NEWS README.md LICENSES
%{_bindir}/llvm-qbc

%changelog
* Thu Dec 22 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.09.git
- Rebuilt for Fedora
