%define upstream_name    Math-MPFR
%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    4.24
Release:    1
Summary:    Perl interface to the MPFR (floating point) library
License:    GPL+ or Artistic
Group:      Development/Perl
URL:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Math/%{upstream_name}-%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl-devel
BuildRequires: gmp-devel
BuildRequires: pkgconfig(mpfr)
BuildRequires: libquadmath-devel

%description
A bigfloat module utilizing the MPFR library. Basically
this module simply wraps the 'mpfr' floating point functions
provided by that library. Operator overloading is also available.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc CHANGES META.json META.yml MYMETA.yml README V demos
%{_mandir}/man3/*
%{perl_vendorarch}/*
%exclude %{_libdir}/perl5/perllocal.pod

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 4.24
- Rebuilt for Fedora
* Fri Sep 10 2021 tv <tv> 4.170.0-1.mga9
+ Revision: 1745024
- update to 4.17
* Mon May 24 2021 umeabot <umeabot> 4.160.0-2.mga9
+ Revision: 1726895
- Rebuild for perl 5.34
* Thu Feb 25 2021 tv <tv> 4.160.0-1.mga9
+ Revision: 1691403
- update to 4.16
* Fri Jul 17 2020 tv <tv> 4.140.0-1.mga8
+ Revision: 1606662
- update to 4.14
* Wed Jun 17 2020 umeabot <umeabot> 4.130.0-3.mga8
+ Revision: 1594921
- Rebuild for perl 5.32
* Wed Feb 19 2020 umeabot <umeabot> 4.130.0-2.mga8
+ Revision: 1543517
- Mageia 8 Mass Rebuild
* Tue Jan 21 2020 tv <tv> 4.130.0-1.mga8
+ Revision: 1481852
- update to 4.13
* Tue Aug 27 2019 tmb <tmb> 4.120.0-2.mga8
+ Revision: 1433832
- rebuild for perl 5.30
* Sat Jun 29 2019 shlomif <shlomif> 4.120.0-1.mga8
+ Revision: 1415603
- update to 4.12
* Mon Mar 25 2019 tv <tv> 4.110.0-1.mga7
+ Revision: 1380185
- update to 4.11
* Fri Feb 15 2019 tv <tv> 4.90.0-1.mga7
+ Revision: 1367367
- disable on ARM due to missing quadmath-devel
+ shlomif <shlomif>
- New version 4.09
* Wed Jan 30 2019 tv <tv> 4.80.0-1.mga7
+ Revision: 1361923
- update to 4.08
* Fri Jan 11 2019 tv <tv> 4.60.0-1.mga7
+ Revision: 1355125
- update to 4.06
* Tue Oct 30 2018 tv <tv> 4.50.0-1.mga7
+ Revision: 1326671
- update to 4.05
* Fri Sep 21 2018 umeabot <umeabot> 4.40.0-3.mga7
+ Revision: 1293434
- Mageia 7 Mass Rebuild
* Wed Aug 08 2018 pterjan <pterjan> 4.40.0-2.mga7
+ Revision: 1249531
- Rebuild for perl 5.28
* Thu May 10 2018 shlomif <shlomif> 4.40.0-1.mga7
+ Revision: 1228159
- update to 4.04
* Mon Apr 23 2018 shlomif <shlomif> 4.30.0-1.mga7
+ Revision: 1221589
- update to 4.03
- update to 4.02
- update to 4.01
* Mon Feb 19 2018 kekepower <kekepower> 4.0.0-2.mga7
+ Revision: 1203260
- Rebuild for new mpfr
* Mon Jan 08 2018 shlomif <shlomif> 4.0.0-1.mga7
+ Revision: 1191653
- update to 4.0
* Tue Oct 03 2017 tv <tv> 3.360.0-2.mga7
+ Revision: 1165372
- rebuild with fixed rpm for missing autodeps
* Wed Sep 27 2017 tv <tv> 3.360.0-1.mga7
+ Revision: 1160720
- update to 3.36
* Thu Aug 31 2017 pterjan <pterjan> 3.320.0-4.mga7
+ Revision: 1149079
- Rebuild for perl ABI changes
* Sat Jul 22 2017 neoclust <neoclust> 3.320.0-3.mga7
+ Revision: 1126696
- Rebuild against new Perl 5.26
* Sun Jun 19 2016 pterjan <pterjan> 3.320.0-2.mga6
+ Revision: 1029699
- Rebuild for perl 5.22.2
* Sat Mar 05 2016 shlomif <shlomif> 3.320.0-1.mga6
+ Revision: 986134
- update to 3.32
* Wed Feb 10 2016 shlomif <shlomif> 3.300.0-1.mga6
+ Revision: 953225
- update to 3.30
* Fri Jan 15 2016 shlomif <shlomif> 3.290.0-1.mga6
+ Revision: 923278
- update to 3.29
* Thu Nov 26 2015 shlomif <shlomif> 3.280.0-1.mga6
+ Revision: 906196
- New version 3.28
* Wed Jul 08 2015 sander85 <sander85> 3.250.0-1.mga6
+ Revision: 852854
- update to 3.25
* Thu Jun 25 2015 shlomif <shlomif> 3.240.0-2.mga6
+ Revision: 842869
- Fix BRs and description
- imported package perl-Math-MPFR
