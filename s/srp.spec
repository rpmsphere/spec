%undefine _debugsource_packages

Name:         srp
Summary:      Secure Remote Password Library
URL:          http://srp.standford.edu/
Group:        Cryptography
License:      MIT-style
Version:      2.1.2
Release:      8.1
Source0:      http://srp.stanford.edu/source/srp-%{version}.tar.gz
BuildRequires: compat-openssl10-devel

%description
The Secure Remote Password protocol is the core technology behind the Stanford
SRP Authentication Project. The Project is an Open Source initiative that
integrates secure password authentication into new and existing networked
applications.

%prep
%setup -q

%build
cd libsrp
./configure \
      --prefix=%{_prefix} \
      --libdir=%{_libdir} \
      --includedir=%{_includedir}/srp
  %{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
cd libsrp
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
mv $RPM_BUILD_ROOT%{_prefix}/bin/tconf \
   $RPM_BUILD_ROOT%{_prefix}/bin/srp-tconf

%files
%{_bindir}/*
%{_includedir}/srp
%{_libdir}/libsrp.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.2
- Rebuilt for Fedora
