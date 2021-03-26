Summary:	SSL library developed for embedded environments
Name:		cyassl
Version:	2.8.0
Release:	12.1
License:	GPL
Group:		System/Libraries
URL:		http://www.yassl.com/
Source0:	http://www.yassl.com/%{name}-%{version}.zip

%description
CyaSSL is a C language based SSL library developed for embedded environments
and real time operating systems where resources are constrained. CyaSSL is
about 10 times smaller than yaSSL and up to 20 times smaller than OpenSSL. User
benchmarking and feedback also reports dramatically better performance from
CyaSSL vs. OpenSSL in the vast majority of standard SSL operations.

%package devel
Summary:	Development package with static libs and headers
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
CyaSSL is a C language based SSL library developed for embedded environments
and real time operating systems where resources are constrained. CyaSSL is
about 10 times smaller than yaSSL and up to 20 times smaller than OpenSSL. User
benchmarking and feedback also reports dramatically better performance from
CyaSSL vs. OpenSSL in the vast majority of standard SSL operations.

%prep
%setup -q

%build
%configure
make CFLAGS+="-fPIC"

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%{_datadir}/doc/%{name}
%{_bindir}/*
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/cyassl
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so
%{_libdir}/lib*.*a

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.8.0
- Rebuild for Fedora
* Mon Mar 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-1mdv2011.0
+ Revision: 642435
- 1.9.0
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-2mdv2011.0
+ Revision: 610187
- rebuild
* Wed Feb 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2010.1
+ Revision: 510612
- import cyassl
* Wed Feb 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2010.0
- initial Mandriva package
