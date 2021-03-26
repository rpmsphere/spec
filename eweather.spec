Summary: Enlightenment weather/forecasts module
Name: 		eweather
Version: 	0.2.0
Release: 	1
License: LGPLv2+
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/
Source:	%{name}-%{version}.tar.gz
Patch0: eweather-0.2.0-linkage.patch
# Common
BuildRequires: gettext-devel
# Enlightenment BR
BuildRequires:	libeina-devel
BuildRequires: 	eet-devel
BuildRequires:  evas-devel
BuildRequires:	ecore-devel
BuildRequires:	efreet-devel
BuildRequires:	embryo-devel
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	e_dbus-devel

%description
Enlightenment weather/forecasts module.

%package devel
Summary: Headers and development libraries from %{name}
Group: Graphical desktop/Enlightenment
Requires: %name = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description devel
%{name} development headers and libraries

%prep
%setup -q
%patch0 -p0

%build
export LDFLAGS='-lm -leina'
./autogen.sh --disable-static --prefix=/usr --libdir=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%{_datadir}/default/* $RPM_BUILD_ROOT%{_datadir}/%{name}/default
mv $RPM_BUILD_ROOT%{_datadir}/simple/* $RPM_BUILD_ROOT%{_datadir}/%{name}/simple

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/eweather_test
%{_libdir}/eweather
%{_datadir}/eweather
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.la

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuild for Fedora
* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn
* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
