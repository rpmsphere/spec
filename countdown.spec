%define upstream_name    App-Countdown

Name:       countdown
Version:    0.4.3
Release:    4.1
Summary:    Like sleep, only displays the amount of time remaining
License:    MIT
Group:      File tools
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/%{upstream_name}-v%{version}.tar.gz
BuildRequires: perl-JSON-PP
BuildRequires: perl(Test::More)
BuildRequires: perl-Module-Build
BuildRequires: perl-Time-HiRes
BuildArch:  noarch

%description
countdown is similar to sleep, only displays the amount of time remaining
to go.

%prep
%setup -q -n %{upstream_name}-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}
perl -i -lpe 's{^(#\!/usr/bin/perl).*}{$1} if $. == 1' %{buildroot}/%{_bindir}/*

%files
%doc Changes META.yml README
%{perl_vendorlib}/App/*
%{_libdir}/perl5/vendor_perl/auto/App/Countdown/.packlist
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Thu Mar 30 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.3
- Rebuild for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 0.2.0-2.mga3
+ Revision: 348190
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri Nov 16 2012 shlomif <shlomif> 0.2.0-1.mga3
+ Revision: 318917
- New version 0.2.0
* Wed Nov 14 2012 shlomif <shlomif> 0.0.4-1.mga3
+ Revision: 317864
- New version 0.0.4
* Tue Nov 13 2012 shlomif <shlomif> 0.0.2-1.mga3
+ Revision: 317538
- Fix summary and group.
- countdown package based on the Mageia ack package
