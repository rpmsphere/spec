%define upstream_name    Math-MPC
%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    1.32
Release:    1
Summary:    Perl interface to the MPC (multi precision complex) library
License:    GPL+ or Artistic
Group:      Development/Perl
URL:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Math/%{upstream_name}-%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl-Exporter
#BuildRequires: perl(Math::BigInt)
#BuildRequires: perl(Math::Complex_C)
#BuildRequires: perl(Math::GMP)
#BuildRequires: perl(Math::GMPf)
#BuildRequires: perl(Math::GMPq)
#BuildRequires: perl(Math::GMPz)
#BuildRequires: perl(Math::MPFR)
BuildRequires: perl-devel
BuildRequires: gmp-devel
BuildRequires: pkgconfig(mpfr)
BuildRequires: libmpc-devel

%description
A multiple precision complex number module utilising the MPC library.
Basically, this module simply wraps the 'mpc' complex number functions
provided by that library. Operator overloading is also available.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc CHANGES META.json META.yml MYMETA.yml README
%{_mandir}/man3/*
%{perl_vendorarch}/*
%exclude %{_libdir}/perl5/perllocal.pod

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.32
- Rebuilt for Fedora
