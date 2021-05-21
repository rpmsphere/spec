Summary:	A collection python of tools for E17
Name:		python-ethumb
Version:	0.7.3
Release:	20101225
Source0:	%{name}-%{version}.tar.gz
License:	GPL
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
BuildRequires:	Cython
Requires:	python >= 2.6

%description
Python support files for ethumb

%package devel
Summary: Headers and development libraries from %{name}
Group: Graphical desktop/Enlightenment
Requires: %name = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description devel
%{name} development headers and libraries

%prep
%setup -q

%build
%configure --disable-static --prefix=/usr
%__make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf %{buildroot}

%files
%doc README
%_libdir/python*/site-packages/
%{_datadir}/python-ethumb/examples/ethumb-client/01-simple.py*

%files devel
%{_libdir}/pkgconfig/python-ethumb.pc
%{_libdir}/pkgconfig/python-ethumb_client.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Jan 05 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
