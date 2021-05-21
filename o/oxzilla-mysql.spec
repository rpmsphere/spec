Summary:	OXZilla plugin for mysql.
Name:		oxzilla-mysql
Version:	0.1.1
Release:	18
License:	GPLv2 with exceptions
Group:		System Environment/Libraries
URL:		http://www.opdesktop.org.tw/
Source0:	%{name}-%{version}.tar.gz
Requires:	oxzilla, mysql-libs
BuildRequires:	oxzilla-devel >= 0.1.1-18, mysql-devel

%description
Files provided for build OXZilla plugin for Mysql.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT %{__make} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} \;

%post

%postun

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/oxzilla/jsplugins/*.so
#%exclude %{_libdir}/oxzilla/jsplugins/*.la

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Thu Apr 1 2010 Wind Yan <yc.yan@ossii.com.tw> 0.0.1-1
- Build for first time.
