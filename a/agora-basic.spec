%undefine _debugsource_packages

Summary: BASIC compiler for POSIX systems
Name: agora-basic
Version: 0.1
Release: 11.1
License: GPL
Group: Development/Languages
Source: https://antti-juhani.kaijanaho.fi/agora-basic/dist/%{name}-%{version}.tar.gz
URL: https://antti-juhani.kaijanaho.fi/agora-basic/
Requires: gcc

%description
Agora BASIC aims to implement all of Standard Full BASIC(ANSI INCITS 113-1987),
with useful but compatible extensions. It does not do that quite yet. What it
does is implement a small subset of the language, enough that simple programs
can be written in it. A lot of work expanding the support of the language is
still required.

%prep
%setup -q

%build
%ifarch aarch64
cp -f /usr/lib/rpm/redhat/config.* .
%endif
./configure --prefix=/usr --libdir=%{_libdir}
sed -i 's|-std=c99|-std=c99 -fPIE|' GNUmakefile
%make_build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
 
%files 
%{_bindir}/agora-basic-compiler
%{_libdir}/agora-basic/libbas.a
%{_libexecdir}/agora-basic/basictoc
%{_datadir}/%{name}/baslib.h
%{_datadir}/doc/%{name}
%{_datadir}/man/man1/agora-basic-compiler.1.*

%changelog
* Wed Aug 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
