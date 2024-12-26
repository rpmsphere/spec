%define upstream_name    Sidef

Name:       perl-%{upstream_name}
Version:    24.11
Release:    1
Summary:    The Sidef programming language
License:    GPL+ or Artistic
Group:      Development/Perl
URL:        https://metacpan.org/pod/%{upstream_name}
Source0:    https://cpan.metacpan.org/authors/id/T/TR/TRIZEN/%{upstream_name}-%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Algorithm::Combinatorics)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
#BuildRequires: perl(Algorithm::Loops)
Requires: perl(Math::GMPq)
Requires: perl(Math::GMPz)
Requires: perl(Math::MPC)
Requires: perl(Math::MPFR)
Requires: perl(Math::Prime::Util::GMP)
#BuildRequires: perl(Memoize)
BuildArch: noarch
#BuildRequires: perl(Cwd)
#BuildRequires: perl(Data::Dump)
#BuildRequires: perl(Encode)
#BuildRequires: perl(Fcntl)
#BuildRequires: perl(File::Basename)
#BuildRequires: perl(File::Copy)
#BuildRequires: perl(File::Find)
#BuildRequires: perl(File::Path)
#BuildRequires: perl(File::Spec)
#BuildRequires: perl(Getopt::Std)
#BuildRequires: perl(List::Util)
#BuildRequires: perl(POSIX)
#BuildRequires: perl(Scalar::Util)
#BuildRequires: perl(Socket)
#BuildRequires: perl(Term::ReadLine)
#BuildRequires: perl(parent)
#BuildRequires: perl(utf8)
#BuildRequires: perl(Module::Build::Compat)
#BuildRequires: perl(Test::Pod)

%description
Sidef is a modern, high-level, general-purpose programming language,
inspired by Ruby, Perl 6 and Go.

This is perl module for %{upstream_name} with executable script.

%prep
%setup -qn %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README.md LICENSE Changes TODO
%exclude %{_libdir}/perl5/perllocal.pod
%{_libdir}/perl5/vendor_perl/auto/Sidef/.packlist
%{perl_vendorlib}/*
%{_mandir}/man?/*
%{_bindir}/sidef

%changelog
* Sun Dec 08 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 24.11
- Rebuilt for Fedora
* Thu Mar 02 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2.330.1-3
- (afff86f) MassBuild#1273: Increase release tag
