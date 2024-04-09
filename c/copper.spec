%undefine _debugsource_packages

Name: copper
Summary: Another experimental programming language
Version: 7.0
Release: 1
Group: Development/Languages
License: Public Domain
URL: https://tibleiz.net/copper/
Source0: https://tibleiz.net/download/%{name}-%{version}-src.tar.gz
BuildRequires: libffi-devel
BuildRequires: llvm11-devel
BuildRequires: dos2unix

%description
Copper is based on Zinc with some improvements such as genericity, multiple
return values or variadic arguments. It does not generate intermediary C code
anymore, it has two backends: a x86 COFF generator and LLVM.

%prep
%setup -q
sed -i 's|/usr/local|/usr|' Makefile lib/std/Makefile scripts/copper
#sed -i 's|\$(INSTALL) -s|$(INSTALL)|' Makefile
dos2unix scripts/*
chmod +x scripts/*
##sed -i 's|stage2/copper-elf64|stage1/copper-elf64|' Makefile
sed -i 's|$(OUTDIR)/stage2/copper-elf64|"scripts/copper -c --no-sys --cc --compiler $(OUTDIR)/copper-c"|' Makefile
sed -i 's|/lib$|/lib64|' lib/std/Makefile
sed -i 's|llvm-config|llvm-config-11|' Makefile

%build
make

%install
%make_install
#install -Dm755 scripts/copper %{buildroot}%{_bindir}/copper
#install -m755 build/copper-* %{buildroot}%{_bindir}
#install -Dm644 build/libcopper-std.a %{buildroot}%{_libdir}/libcopper-std.a
#install -d %{buildroot}%{_datadir}/copper
#cp -a lib/std/include %{buildroot}%{_datadir}/copper

%files
%doc *.txt
%{_bindir}/*
%{_libdir}/libcopper-std.a
%{_datadir}/copper

%changelog
* Sun Sep 11 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 7.0
- Rebuilt for Fedora
