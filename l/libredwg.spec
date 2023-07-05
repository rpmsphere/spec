Summary:	A free replacement for the OpenDWG libraries
Name:		libredwg
Version:	0.12.5
Release:	1
License:	GPL
Group:		System/Libraries
URL:		https://www.gnu.org/software/libredwg/
Source:		https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
#BuildRequires:	swig
BuildRequires:	texinfo
#BuildRequires:	python2-devel
#BuildRequires:	python2-libs
#BuildRequires:	python2-setuptools

%description
GNU LibreDWG is a free C library to handle DWG files. DWG is the native file
format of AutoCAD. GNU LibreDWG is based on LibDWG, originally written by
Felipe Castro.

%package python
Summary:	LibreDWG bindings for Python
Group:		Development/Python
Requires:	%{name} = %{version}

%description python
This package provides the files needed for python software that uses
LibreDWG.

%package devel
Summary:	LibreDWG development files
Group:		Development/C
Requires:	%{name} = %{version}

%description devel
This package provides the files needed to compile software that uses
LibreDWG.

%prep
%setup -q

%build
%configure --disable-static --enable-python
sed -i 's|CFLAGS = |CFLAGS = -fPIC |' */Makefile
make

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_datadir}/dwgadd.example %{buildroot}%{_datadir}/load_dwg.py %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc README COPYING AUTHORS ChangeLog NEWS TODO
%{_bindir}/*
%{_libdir}/%{name}.so.*
%{_mandir}/man?/*
%{_datadir}/info/LibreDWG.*
%exclude %{_datadir}/info/dir
%{_datadir}/%{name}
   
%files python
%{python3_sitelib}/*
%{python3_sitearch}/*
   
%files devel
%{_includedir}/*.h
%{_libdir}/%{name}.so
%exclude %{_libdir}/%{name}.la
%{_libdir}/pkgconfig/libredwg.pc
%exclude %{_libdir}/perl5/perllocal.pod
%exclude /usr/local/lib64/perl5/5.34/LibreDWG.pm
%exclude /usr/local/lib64/perl5/5.34/auto/LibreDWG/.packlist
%exclude /usr/local/lib64/perl5/5.34/auto/LibreDWG/LibreDWG.so

%changelog
* Sun Mar 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12.5
- Rebuilt for Fedora
