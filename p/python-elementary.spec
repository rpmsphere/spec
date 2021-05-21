Summary:	A collection python of tools for E17
Name:		python-elementary
Version:	0.7.3
Release:	20100930
Source0:	%{name}-%{version}.tar.bz2
Patch1:		python-elementary-configure.patch
License:	GPL
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
BuildRequires:	Cython
BuildRequires:	python-evas-devel

%description
Python support files for Elementary

%package devel
Summary: Headers and development libraries from %{name}
Group: Graphical desktop/Enlightenment
Requires: %name = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description devel
%{name} development headers and libraries

%prep
%setup -q
%patch1 -p1

%build
%configure --disable-static --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf %{buildroot}

%files
%doc README
%_libdir/python*/site-packages/
%{_datadir}/python-elementary

%files devel
%{_libdir}/pkgconfig/python-elementary.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Jan 05 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
