%undefine _debugsource_packages

Summary: An open source programming language in Ada
Name: sparforte
Version: 2.6.2
Release: 1
License: GPL2 (GNAT Modified)
Group: Development/Languages
Source: https://www.sparforte.com/downloads/%{name}-%{version}-src.tar.gz
URL: https://www.sparforte.com/
BuildRequires: gcc-gnat
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: gstreamer1-devel
BuildRequires: readline-devel
BuildRequires: locate
#BuildRequires: libdb-devel
#BuildRequires: libpq-devel

%description
Based a ISO standard proven effective for large, mission-critical projects,
SparForte is designed for fast development of large projects while, at the
same time, providing easier maintenance and bug removal.

%prep
%setup -q -n %{name}-%{version}-src
sed -i 's|i486|aarch64|' configure
sed -i -e 's|$(CPU_FLAG)=$(CPU)||' -e 's|-gnatfaoN|-gnatfaoN -gnatd.E -gnatwv|' src/GNUmakefile*

%build
./configure --prefix=/usr --without-mysql --without-bdb --without-postgres
sed -i '/param_ptr :=/d' src/parser_pen.adb
%make_build -j1

%install
rm -rf $RPM_BUILD_ROOT
%make_install
install -d %{buildroot}%{_mandir}
mv %{buildroot}%{_datadir}/man1 %{buildroot}%{_mandir}

%files 
%doc *.md AUTHORS ChangeLog* COPYING README TODO
%{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.2
- Rebuilt for Fedora
