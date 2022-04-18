%undefine _debugsource_packages

Name: copper
Summary: Another experimental programming language
Version: 4.6
Release: 1
Group: Development/Languages
License: Public Domain
URL: http://tibleiz.net/copper/
Source0: http://tibleiz.net/download/%{name}-%{version}-src.tar.gz
BuildRequires: libffi-devel
BuildRequires: dos2unix

%description
Copper is based on Zinc with some improvements such as genericity, multiple
return values or variadic arguments. It does not generate intermediary C code
anymore, it has two backends: a x86 COFF generator and LLVM.

%prep
%setup -q
sed -i 's|/usr/local|/usr|' Makefile
sed -i 's|\$(INSTALL) -s|$(INSTALL)|' Makefile
dos2unix scripts/*
chmod +x scripts/*

%build
make COPPER=boot/copper-elf64 BACKEND=c
#make boot-c
#make BACKEND=c

%install
%make_install BACKEND=c

%files
%doc *.txt
%{_bindir}/*

%changelog
* Sun Mar 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 4.6
- Rebuilt for Fedora
