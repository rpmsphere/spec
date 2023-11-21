Summary:	Simula to C translator: Mother of all OO-languages
Name:		cim
Version:	5.1
Release:	6.1
License:	GPLv2+
Group:		Development/Languages
URL:		https://www.gnu.org/software/cim/
Source0:	https://ftp.gnu.org/gnu/cim/%{name}-%{version}.tar.gz

%description
Cim compiles Simula code to C and uses a C compiler like gcc to
compile it further to machine-code. Simula was the first language
with object-oriented features. The Simula language has features for
quasi-parallel execution and a framework for doing simulations.

%files
%doc NEWS README doc/SIMULA-HISTORY AUTHORS COPYING TODO
%{_bindir}/*
%{_mandir}/man1/cim.1*
%{_libdir}/libcim.so.*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/cim.h
%{_infodir}/cim.info.*
%exclude %{_infodir}/dir

%prep
%setup -q
sed -i 's|../../lib/cim.h|cim.h|' lib/simset.c lib/simulation.c

%build
%configure --enable-dump=yes --disable-static
%make_build

%install
%make_install

%changelog
* Fri Oct 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 5.1
- Rebuilt for Fedora
* Sat Feb 04 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3.37-14
- (4342e8b) MassBuild#1230: Increase release tag
