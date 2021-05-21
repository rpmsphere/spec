Name: intclock
Summary: An international clock
Version: 2.13
Release: 25.1
Group: Applications/System
License: GPLv2
URL: http://users.skynet.be/Peter.Verthez/projects/intclock/
Source0: http://www.peterverthez.net/projects/intclock/%{name}-%{version}.tar.gz
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: perl-Gtk2
BuildRequires: perl-Data-Dumper
BuildRequires: perl-Locale-Maketext
BuildRequires: perl-Time-HiRes
BuildArch: noarch
Requires: perl-Gtk2
Requires: perl-Data-Dumper

%description
This program provides an international, i.e. multi-timezone, clock for Linux.
It is based on hsclock by Jens-Ulrik Petersen, but is written in Perl instead
of Haskell. It also adds some extra features.

%prep
%setup -q
sed -i -e 's|/usr/share|%{buildroot}%{_datadir}|' -e 's|$prefix/share|%{buildroot}%{_datadir}|' Makefile.PL
sed -i 's|qw(Data::Dumper Time::HiRes Locale::Maketext)|(qw(Data::Dumper Time::HiRes Locale::Maketext))|' Makefile.PL

sed -i '/UI_gtk.pm/d' MANIFEST
sed -i '222,225d' bin/intclock
rm lib/Intclock/UI_gtk.pm

%build
perl Makefile.PL PREFIX=/usr
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/applications
%make_install
sed -i 's|%{buildroot}||' %{buildroot}%{_datadir}/perl5/5.*/Intclock.pl

%files
%doc README NEWS COPYING ChangeLog AUTHORS TRANSLATING
%{_bindir}/*
%{_datadir}/perl5/*
%{_datadir}/applications/*.desktop
%exclude %{_libdir}/perl5/*
%{_datadir}/%{name}

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.13
- Rebuilt for Fedora
