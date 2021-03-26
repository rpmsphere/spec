%define upstream_name    Term-Screen

Name:       perl-%{upstream_name}
Version:    1.06
Release:    4.1
Summary:    A simple all-Perl Term::Cap based screen positioning module
License:    Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{version}.tar.gz
BuildRequires:  perl-devel
BuildArch:      noarch

%description
Term::Screen is a very simple screen positioning module that should
work wherever C<Term::Cap> does. It is set up for Unix using stty's but
these dependences are isolated by evals in the C<new> constructor. Thus
you may create a child module implementing Screen with MS-DOS, ioctl,
or other means to get raw and unblocked input. This is not a replacement
for Curses -- it has no memory.  This was written so that it could be
easily changed to fit nasty systems, and to be available first thing.

The input functions getch, key_pressed, echo, and noecho are implemented
so as to work under a fairly standard Unix system. They use 'stty'
to set raw and no echo modes and turn on auto flush. All of these are
'eval'ed so that this class can be inherited for new definitions easily.

Term::Screen was designed to be "required", then used with object syntax
as shown above. One quirk (which the author was used to so he didn't
care) is that for function key translation, no delay is set. So for many
terminals to get an esc character, you have to hit another char after it,
generally another esc.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%install
rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT pure_install
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Aug 15 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.06
- Rebuild for Fedora
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 664910
- mass rebuild
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 405542
- rebuild using %%perl_convert_version
* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.03-7mdv2009.0
+ Revision: 258509
- rebuild
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.03-6mdv2009.0
+ Revision: 246525
- rebuild
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.03-4mdv2008.1
+ Revision: 136360
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-4mdv2008.0
+ Revision: 86966
- rebuild
* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-3mdv2007.0
- rewrite spec file
* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-2mdk
- Fix SPEC according to Perl Policy
    - Source URL
    - URL
- use mkrel
* Sun May 29 2005 Lev Givon <lev@columbia.edu> 1.03-1mdk
- Adapted cpan2rpm-generated spec for Mandrake.
