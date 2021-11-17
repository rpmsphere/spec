%define module_name XML-RPC
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(LWP::Protocol::https) perl(LWP::UserAgent) perl(MIME::Base64) perl(Test::More) perl(XML::TreePP)
%define _unpackaged_files_terminate_build 1
BuildRequires: perl-devel perl-podlators

Name: perl-%module_name
Version: 1.1
Release: 2.1
Summary: Pure Perl implementation for an XML-RPC client and server
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/%module_name
Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/C/CA/CAVAC/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor
make

%install
%make_install

%files
%doc README Changes
%exclude %{_libdir}/perl5/perllocal.pod
%{_libdir}/perl5/vendor_perl/auto/XML/RPC/.packlist
%{_mandir}/man3/XML::RPC.3pm.gz
%{_datadir}/perl5/vendor_perl/XML/RPC.pm

%changelog
* Mon Aug 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- regenerated from template by package builder
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1-alt1
- regenerated from template by package builder
* Mon Jan 20 2014 Cronbuild Service <cronbuild@altlinux.org> 0.9-alt2
- rebuild to get rid of unmets
* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1
- initial import by package builder
