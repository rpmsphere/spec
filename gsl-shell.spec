%global debug_package %{nil}

Name: gsl-shell
Summary: A command-line interface to GSL collection of mathematical functions
Version: 2.3.2
Release: 1
Group: Sciences/Mathematics
License: GPLv3
URL: http://savannah.nongnu.org/projects/gsl-shell/
Source0: http://ftp.twaren.net/Unix/NonGNU//gsl-shell/%{name}-%{version}.tar.gz
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
Source1:	http://luajit.org/download/LuaJIT-2.1.0-beta3.tar.gz

%description
GSL shell offers an interactive command-line interface that gives access
to GSL collection of mathematical functions.

%prep
%setup -q -a 1
sed -i 's|none|linux|' makeconfig
sed -i 's|/usr/local|/usr|' makeconfig
sed -i 's/\r//' README
sed -i 's|-lgsl|-lgsl -lgslcblas|' makepackages
rm -rf luajit2
mv LuaJIT-2.1.0-beta3 luajit2

%build
make -C luajit2
mkdir .libs
cp luajit2/src/libluajit.a .libs/
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

%clean
%__rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Oct 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuild for Fedora
* Sat Feb 04 2012 Cristobal Lopez <lopeztobal@gmail.com> 2.1.0
- New version/release for MIB (Mandriva International Backports) users
* Tue Jan 18 2011 Alberto Altieri <alberto.altieri@gmail.com> 1.1
- New version/release for MIB (Mandriva International Backports) users
