%define upstream_name    XML-Mini

Name:           perl-%{upstream_name}
Version:        1.38
Release:        11.1
Summary:        Perl implementation of the XML::Mini XML create/parse interface
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            https://search.cpan.org/dist/%{upstream_name}/
Source0:        https://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires: perl-ExtUtils-MakeMaker

%description
XML::Mini is a set of Perl classes that allow you to access XML data and create
valid XML output with a tree-based hierarchy of elements. The MiniXML API has
both Perl and PHP implementations.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
#rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/perllocal.pod
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3*/*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.38
- Rebuilt for Fedora
* Sat Jan 22 2011 jquelin <jquelin> 1.380.0-1.mga1
+ Revision: 31491
- mageia rebuild
- imported package perl-XML-Mini
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.380.0-1mdv2010.0
+ Revision: 401859
- rebuild using %%perl_convert_version
* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.38-5mdv2009.1
+ Revision: 350216
- 2009.1 rebuild
* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.38-4mdv2009.0
+ Revision: 258842
- rebuild
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.38-3mdv2009.0
+ Revision: 246732
- rebuild
* Wed Feb 06 2008 Funda Wang <fundawang@mandriva.org> 1.38-1mdv2008.1
+ Revision: 162943
- update to new version 1.38
* Mon Feb 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2008.1
+ Revision: 162064
- update to new version 1.36
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %$RPM_BUILD_ROOT on Pixel's request
* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.8-7mdv2008.0
+ Revision: 87108
- rebuild
* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.8-6mdv2007.0
- better summary and description
* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.2.8-5mdk
- Fix According to perl Policy
    - Source URL
    - URL
- use mkrel
* Mon Jul 04 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-4mdk
- rebuild
* Sat Jun 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.8-3mdk
- rebuilt, fix deps
- use macros
