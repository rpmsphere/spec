%define upstream_name    Math-GMPq

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.47
Release:    1
Summary:    Perl interface to the GMP library's rational (mpq) functions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Math/%{upstream_name}-%{version}.tar.gz
BuildRequires: perl-Exporter
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: gmp-devel
BuildRequires: perl-devel

%description
A perl interface to the GMP library's rational (mpq) functions.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%make_install

%files
%doc CHANGES META.json META.yml MYMETA.yml README V
%{_mandir}/man3/*
%{perl_vendorarch}/*
%exclude %{_libdir}/perl5/perllocal.pod

%changelog
* Sun Oct 03 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.47
- Rebuilt for Fedora
* Mon Sep 27 2021 tv <tv> 0.470.0-1.mga9
+ Revision: 1746678
- update to 0.47
* Mon May 24 2021 umeabot <umeabot> 0.460.0-2.mga9
+ Revision: 1726891
- Rebuild for perl 5.34
* Thu Feb 25 2021 tv <tv> 0.460.0-1.mga9
+ Revision: 1691356
- update to 0.46
* Wed Jun 17 2020 umeabot <umeabot> 0.450.0-7.mga8
+ Revision: 1594916
- Rebuild for perl 5.32
* Sun Feb 16 2020 umeabot <umeabot> 0.450.0-6.mga8
+ Revision: 1529832
- Mageia 8 Mass Rebuild
* Tue Aug 27 2019 tmb <tmb> 0.450.0-5.mga8
+ Revision: 1433829
- rebuild for perl 5.30
* Fri Sep 21 2018 umeabot <umeabot> 0.450.0-4.mga7
+ Revision: 1293430
- Mageia 7 Mass Rebuild
* Wed Aug 08 2018 pterjan <pterjan> 0.450.0-3.mga7
+ Revision: 1249528
- Rebuild for perl 5.28
* Tue Oct 03 2017 tv <tv> 0.450.0-2.mga7
+ Revision: 1165341
- rebuild with fixed rpm for missing autodeps
* Tue Sep 19 2017 sander85 <sander85> 0.450.0-1.mga7
+ Revision: 1155558
- update to 0.45
* Thu Aug 31 2017 pterjan <pterjan> 0.390.0-4.mga7
+ Revision: 1149076
- Rebuild for perl ABI changes
* Sat Jul 22 2017 neoclust <neoclust> 0.390.0-3.mga7
+ Revision: 1126650
- Rebuild against new Perl 5.26
* Sun Jun 19 2016 pterjan <pterjan> 0.390.0-2.mga6
+ Revision: 1029638
- Rebuild for perl 5.22.2
* Mon Jan 04 2016 shlomif <shlomif> 0.390.0-1.mga6
+ Revision: 919585
- update to 0.39
* Mon Nov 09 2015 shlomif <shlomif> 0.380.0-1.mga6
+ Revision: 899907
- New version 0.38
* Thu Jun 25 2015 shlomif <shlomif> 0.370.0-2.mga6
+ Revision: 842868
- Rebuild for the new perl-5.22.0
* Sat Jun 20 2015 shlomif <shlomif> 0.370.0-1.mga6
+ Revision: 836869
- Importing perl-Math-GMPq
