Summary:	A collection python of tools for E17
Name:		python-emotion
Version:	0.7.3
Release:	20100930
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
BuildRequires:	Cython, emotion-devel, python-evas-devel
Requires:	python >= 2.6

%description
Python support files for emotion

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
%makeinstall

%clean
%__rm -rf %{buildroot}

%files
%doc README
%_libdir/python*/site-packages/
%{_datadir}/python-emotion/examples/emotion_test.py*

%files devel
%{_libdir}/pkgconfig/python-emotion.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Jan 05 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
