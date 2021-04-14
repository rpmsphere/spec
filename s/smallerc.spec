%global _name SmallerC
%global __os_install_post %{nil}
%undefine _debugsource_packages

Summary:	Simple C Compiler
Name:		smallerc
Version:	0100
Release:	6.1
License:	BSD-2
Group:		Development/C
URL:		https://github.com/alexfru/SmallerC
Source0:	%{_name}-master.zip
BuildRequires: nasm

%description
Smaller C is a simple and small single-pass C compiler,
currently supporting most of the C language common between C89/ANSI C
and C99 (minus some C89 and plus some C99 features).

%prep
%setup -q -n %{_name}-master
sed -i -e 's|bindir = .*|bindir = %{_bindir}|' -e 's|libdir = .*|libdir = %{_libdir}/smlrc|' -e 's|incdir = .*|incdir = %{_includedir}/smlrc|' common.mk

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%{_bindir}/*
%{_includedir}/smlrc
%{_libdir}/smlrc

%changelog
* Thu Jul 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0100
- Rebuilt for Fedora
