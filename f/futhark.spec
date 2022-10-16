#global __os_install_post %{nil}
#undefine _debugsource_packages

Summary: A data-parallel functional programming language
Name: futhark
Version: 0.22.2
Release: 1
License: ISC
Group: Development/Languages
Source0: https://github.com/diku-dk/futhark/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://futhark-lang.org/
BuildRequires: ghc-base-devel

%description
Futhark is a purely functional data-parallel programming language in the
ML family. It can be compiled to typically very efficient parallel code,
running on either a CPU or GPU.

%prep
%setup -q
sed -i 's|base >=4.15|base >=4.14|' %{name}.cabal

%build
make

%install
%make_install
#install -d %{buildroot}%{_bindir}
#install -m755 *-linux-build/%{name}* *-linux-build/stategraph %{buildroot}%{_bindir}
#install -d %{buildroot}%{_includedir}/%{name}
#install -m644 include/* %{buildroot}%{_includedir}/%{name}

%files 
%doc LICENSE.txt *.md
#{_bindir}/*
#{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.22.2
- Rebuilt for Fedora
