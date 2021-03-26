%define cpan_name XML-LibXML-Simple

Name:           perl-XML-LibXML-Simple
Version:        0.93
Release:        7.1
Summary:        XML::LibXML clone of XML::Simple::XMLin()
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/XML-LibXML-Simple/
Source:         http://www.cpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(XML::LibXML) >= 1.64
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(File::Slurp)
Requires:       perl(XML::LibXML) >= 1.64

%description
This module is a blunt rewrite of XML::Simple (by Grant McLean) to use the
XML::LibXML parser for XML structures, where the original uses plain Perl
or SAX parsers.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%install
%__make DESTDIR=$RPM_BUILD_ROOT pure_install
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

%files
%defattr(-,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3*/*

%changelog
* Tue Dec 10 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.93
- Rebuild for Fedora
* Tue Jun  4 2013 coolo@suse.com
- updated to 0.93
  - move pod-test to xt/
  - fix warning produced by Pod::Checker
  - include license in the manuals.
* Fri May 25 2012 werner@suse.de
- Do version update to 0.91
* Wed May 23 2012 cfarrell@suse.com
- license update: Artistic-1.0 or GPL-1.0+
  Perl license in SPDX format
* Tue May 22 2012 werner@suse.de
- run osc service localrun format_spec_file
* Fri Apr 29 2011 pascal.bleser@opensuse.org
- initial version (0.15)
