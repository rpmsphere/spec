Name: afnix
Summary: Compiler and run-time for the AFNIX programming language
Version: 3.8.0
Release: 1
Group: interpreters
License: Free Software
URL: https://www.afnix.org/
Source0: https://www.afnix.org/ftp/%{name}-src-%{version}.tgz
BuildRequires: ncurses-devel

%description
AFNIX is a multi-threaded functional programming language with
dynamic symbol bindings that support the object oriented paradigm.
The language features a state of the art runtime engine. The
distribution is available with several clients and a rich set
of modules that are designed to be platform independent.

%prep
%setup -q -n %{name}-src-%{version}
sed -i 's|/opt/%{name}|%{buildroot}/usr|' cnf/bin/%{name}-setup
sed -i '120i *) ccvers=11 ;;' cnf/bin/%{name}-vcomp
sed -i 's|-Werror||' cnf/mak/*

%build
make

%install
make install
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}/etc/ld.so.conf.d
echo %{_libdir}/%{name} > %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}.conf

%files
%{_bindir}/*
%{_includedir}/%{name}
%{_libdir}/%{name}
/etc/ld.so.conf.d/%{name}-%{_arch}.conf

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 3.8.0
- Rebuilt for Fedora
