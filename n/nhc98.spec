%define nname    nhc98
%define nversion 1.22
%define hname    hmake
%define hversion 3.13

Name:            %{nname}
Version:         %{nversion}
Release:         1
License:         Freely available
Group:           Development/Languages/Haskell
URL:             http://haskell.org/nhc98/
Source:          ftp://ftp.cs.york.ac.uk/pub/haskell/nhc98/nhc98src-%{nversion}.tar.gz
Requires:        %{hname}
BuildRequires:   ghc happy java
Provides:        haskell hoodui
Summary:         York compiler for Haskell 98

%description
nhc98 is a small, easy to install, standards-compliant compiler for
Haskell 98, the lazy functional programming language. It is very
portable, and aims to produce small executables that run in small
amounts of memory. It produces medium-fast code, and compilation is
itself quite fast. It also comes with extensive tool support for
automatic compilation, foreign language interfacing, heap and time
profiling, tracing, and debugging. (Some of its advanced kinds of heap
profiles are not found in any other Haskell compiler.)

%package -n %{hname}
Version:         %{hversion}
Group:           Development/Languages/Haskell
Requires:        readline
Summary:         A make tool for Haskell programs

%description -n %{hname}
hmake is a compilation manager for Haskell programs. hmake interactive,
or hi for short, is an interactive program development environment for
Haskell, rather like Hugs. hmake-config is an auxiliary tool for
managing the set of compilers known by hmake, useful when you install
a new compiler, or a new version of a compiler.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}/man1 --docdir=html --buildwith=ghc --buildopts=-O
make all hoodui

%install
make DESTDIR=${RPM_BUILD_ROOT} install
( cd ${RPM_BUILD_ROOT}%{_mandir}/man1 && gzip -9 harch.1 hi.1 hmake.1 hp2graph.1 nhc98.1 )
./configure --install -bin -lib -inc -man +docs
mv html/hmake html-hmake

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc ANNOUNCE COPYRIGHT INSTALL README html/*
%{_bindir}/cpphs
%{_bindir}/greencard-nhc98
%{_bindir}/hood
%{_bindir}/hp2graph
%{_bindir}/nhc98
%{_bindir}/runhs
%{_bindir}/tprofprel
%{_includedir}/nhc98
%{_libdir}/nhc98
%{_mandir}/man1/hi.1.*
%{_mandir}/man1/hp2graph.1.*
%{_mandir}/man1/nhc98.1.*

%files -n %{hname}
%doc html-hmake
%{_bindir}/harch
%{_bindir}/hi
%{_bindir}/hmake
%{_bindir}/hmake-config
%{_libdir}/hmake
%{_mandir}/man1/harch.1.*
%{_mandir}/man1/hmake.1.*

%changelog
* Sat Sep 29 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.22
- Rebuilt for Fedora
