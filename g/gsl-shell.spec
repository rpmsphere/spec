%undefine _debugsource_packages

Name: gsl-shell
Summary: A command-line interface to GSL collection of mathematical functions
Version: 2.3.2
Release: 1
Group: Sciences/Mathematics
License: GPLv3
URL: https://savannah.nongnu.org/projects/gsl-shell/
Source0: https://ftp.twaren.net/Unix/NonGNU//gsl-shell/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: agg-devel
BuildRequires: gsl-devel
BuildRequires: atlas-devel
BuildRequires: libX11-devel
BuildRequires: readline-devel
BuildRequires: libstdc++-static
BuildRequires: blas-devel
BuildRequires: fox-devel
Requires: lua
Source1:        https://luajit.org/download/LuaJIT-2.1.0-beta3.tar.gz

%description
GSL shell offers an interactive command-line interface that gives access
to GSL collection of mathematical functions.

%prep
%setup -q -a 1
sed -i 's|none|linux|' makeconfig
sed -i 's|/usr/local|/usr|' makeconfig
sed -i 's/\r//' README
sed -i 's|-lgsl|-lgsl -lgslcblas|' makepackages
sed -i 's|-Wall|-Wall -fPIE|' makedefs
rm -rf luajit2
mv LuaJIT-2.1.0-beta3 luajit2

%build
make -C luajit2
mkdir .libs
cp luajit2/src/libluajit.a .libs/
sed -i 's|-Wall|-Wall -fPIE|' Makefile */Makefile */*/Makefile
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/examples $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%doc README LICENSE doc/*
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/gsl-shell.desktop
%{_datadir}/icons/hicolor/128x128/apps/gsl-shell.png

%changelog
* Thu Oct 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuilt for Fedora
* Sat Feb 04 2012 Cristobal Lopez <lopeztobal@gmail.com> 2.1.0
- New version/release for MIB (Mandriva International Backports) users
* Tue Jan 18 2011 Alberto Altieri <alberto.altieri@gmail.com> 1.1
- New version/release for MIB (Mandriva International Backports) users
