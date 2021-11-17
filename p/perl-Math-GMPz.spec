%define upstream_name    Math-GMPz

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.51
Release:    2
Summary:    Perl interface to the GMP library's integer (mpz) functions
License:    GPL+ or Artistic
Group:      Development/Perl
URL:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Math/%{upstream_name}-%{version}.tar.gz
BuildRequires: perl-Exporter
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildRequires: gmp-devel
BuildRequires: perl-devel

%description
A perl interface to the GMP library's integer (mpz) functions.

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
%doc CHANGES META.json META.yml MYMETA.yml README V demos
%{_mandir}/man3/*
%{perl_vendorarch}/*
%exclude %{_libdir}/perl5/perllocal.pod

%changelog
* Sun Oct 03 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.51
- Rebuilt for Fedora
* Mon May 24 2021 umeabot <umeabot> 0.510.0-2.mga9
+ Revision: 1726892
- Rebuild for perl 5.34
* Sun Apr 04 2021 tv <tv> 0.510.0-1.mga9
+ Revision: 1713149
- update to 0.51
* Mon Mar 29 2021 tv <tv> 0.500.0-1.mga9
+ Revision: 1711636
- update to 0.50
* Thu Feb 25 2021 tv <tv> 0.490.0-1.mga9
+ Revision: 1691402
- update to 0.49
* Wed Jun 17 2020 umeabot <umeabot> 0.480.0-6.mga8
+ Revision: 1594917
- Rebuild for perl 5.32
* Sun Feb 16 2020 umeabot <umeabot> 0.480.0-5.mga8
+ Revision: 1529836
- Mageia 8 Mass Rebuild
* Tue Aug 27 2019 tmb <tmb> 0.480.0-4.mga8
+ Revision: 1433830
- rebuild for perl 5.30
* Fri Sep 21 2018 umeabot <umeabot> 0.480.0-3.mga7
+ Revision: 1293431
- Mageia 7 Mass Rebuild
* Wed Aug 08 2018 pterjan <pterjan> 0.480.0-2.mga7
+ Revision: 1249529
- Rebuild for perl 5.28
* Tue Dec 26 2017 shlomif <shlomif> 0.480.0-1.mga7
+ Revision: 1185278
- update to 0.48
* Tue Oct 03 2017 tv <tv> 0.460.0-2.mga7
+ Revision: 1165347
- rebuild with fixed rpm for missing autodeps
* Tue Sep 19 2017 sander85 <sander85> 0.460.0-1.mga7
+ Revision: 1155560
- update to 0.46
* Thu Aug 31 2017 pterjan <pterjan> 0.430.0-4.mga7
+ Revision: 1149077
- Rebuild for perl ABI changes
* Sat Jul 22 2017 neoclust <neoclust> 0.430.0-3.mga7
+ Revision: 1127241
- Rebuild against new Perl 5.26
* Sun Jun 19 2016 pterjan <pterjan> 0.430.0-2.mga6
+ Revision: 1029645
- Rebuild for perl 5.22.2
* Wed Feb 10 2016 shlomif <shlomif> 0.430.0-1.mga6
+ Revision: 953221
- update to 0.43
* Mon Jan 04 2016 shlomif <shlomif> 0.420.0-1.mga6
+ Revision: 919594
- update to 0.42
* Mon Nov 09 2015 shlomif <shlomif> 0.410.0-1.mga6
+ Revision: 899912
- New version 0.41
* Thu Jun 25 2015 shlomif <shlomif> 0.400.0-2.mga6
+ Revision: 842867
- Rebuild for the new perl-5.22.0
* Sat Jun 20 2015 shlomif <shlomif> 0.400.0-1.mga6
+ Revision: 836859
- Importing perl-Math-GMPz
* Mon May 11 2015 cpan2dist 0.39-1mga
- initial mageia release, generated with cpan2dist
