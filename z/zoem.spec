%global version 11.166
%global version2 %(tr '.' '-' <<<%{version})

Summary: Zoem is an interpretive macro/programming language
Name:    zoem
Version: %{version}
Release: 10
License: GPLv2
Group:   Publishing
URL:     https://micans.org/%{name}/
Source0: https://micans.org/%{name}/src/%{name}-%{version2}.tar.gz
Patch0:  zoem-11-166-mga-multiple-def.patch

%description
Zoem is an interpretive macro/programming language that is evaluated by the
macro processor called zoem. It is used by Portable Unix Documentation
(PUD) and Aephea. The latter is a general authoring tool for writing HTML
documents and provides both useful abstractions and a framework for
creating new abstractions. It uses and promotes the use of CSS. A small
core of Aephea has been ported to the typesetting language troff. This core
is used in PUD, which provides mini-languages for FAQ documents and UNIX
manual pages. Documents written in PUD can be output to troff and html, and
further to plain text, PostScript, and PDF.

%prep
%setup -q -n %{name}-%{version2}
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc %{_defaultdocdir}/%{name}/doc/*
%doc %{_defaultdocdir}/%{name}/examples/*
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun Jan 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 11.166
- Rebuilt for Fedora
* Fri May 15 2020 danf <danf> 11_166-10.mga8
+ Revision: 1583994
- Fix multiple definition error with gcc 10.1
* Fri Feb 14 2020 umeabot <umeabot> 11_166-9.mga8
+ Revision: 1519150
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x
* Sun Sep 23 2018 umeabot <umeabot> 8.mga7-current
+ Revision: 1302061
- Mageia 7 Mass Rebuild
* Sun Jan 17 2016 daviddavid <daviddavid> 11_166-7.mga6
+ Revision: 925176
- switch to %%configure2_5x to fix build
* Wed Oct 15 2014 umeabot <umeabot> 11_166-6.mga5
+ Revision: 749235
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 11_166-5.mga5
+ Revision: 690885
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 11_166-4.mga4
+ Revision: 521329
- Mageia 4 Mass Rebuild
* Mon Jan 21 2013 malo <malo> 11_166-3.mga3
+ Revision: 390351
- spec clean-up
- updated RPM group
* Mon Jan 14 2013 umeabot <umeabot> 11_166-2.mga3
+ Revision: 387772
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Apr 10 2012 bcornec <bcornec> 11_166-1.mga2
+ Revision: 230036
- Upload the zoem package
- Created package structure for zoem.
