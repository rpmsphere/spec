%define upstream_name    Sidef

Name:       perl-%{upstream_name}
Version:    3.97.1
Release:    1
Summary:    The Sidef programming language
License:    GPL+ or Artistic
Group:      Development/Perl
URL:        https://metacpan.org/pod/%{upstream_name}
Source0:    https://cpan.metacpan.org/authors/id/T/TR/TRIZEN/%{upstream_name}-v%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Algorithm::Combinatorics)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
#BuildRequires: perl(Algorithm::Loops)
#BuildRequires: perl(Math::GMPq)
#BuildRequires: perl(Math::GMPz)
#BuildRequires: perl(Math::MPC)
#BuildRequires: perl(Math::MPFR)
#BuildRequires: perl(Math::Prime::Util::GMP)
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

This is perl module for %{upstream_name}.

%package -n %{upstream_name}
Summary: Sidef executable script
Requires: %{name}

%description -n %{upstream_name}
Sidef is a modern, high-level, general-purpose programming language,
inspired by Ruby, Perl 6 and Go.

%prep
%setup -qn %{upstream_name}-v%{version}

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
%{_mandir}/man3/*

%files -n %{upstream_name}
%{_bindir}/sidef

%changelog
* Tue Mar 09 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.97.1
- Rebuild for Fedora
* Thu Mar 02 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2.330.1-3
- (afff86f) MassBuild#1273: Increase release tag
