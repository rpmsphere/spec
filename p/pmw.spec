Summary:	A program to typeset music scores into Postscript
Name:		pmw
Version:	4.34
Release:	1
License:	GPLv2+
Group:		Publishing
URL:		https://www.quercite.com/pmw.html
Source0:	https://www.quercite.com/%{name}-%{version}.tar.gz

%description
Philip's Music Writer is a program for typesetting music. It reads text files
as input, and generates PostScript as output. It can also write simple MIDI
files for proofhearing purposes. PMW is written in C and is freestanding; that
is, it does not require additional processing software. It is a Linux/Unix
port of a program that has run for over a decade on Acorn systems, where it
was known as Philip's Music Scribe.

%prep
%setup -q

%build
%configure
make

%install
%makeinstall \
	BINDIR=%{buildroot}%{_bindir} \
	DATADIR=%{buildroot}%{_datadir}/pmw \
	MANDIR=%{buildroot}%{_mandir}

rm -rf examples
mkdir examples
cp testdist/infiles/* examples/

# link fonts to ghostscript dir
mkdir -p %{buildroot}%{_datadir}/ghostscript/Resource/Font
ln -s ../../../pmw/psfonts/PMW-Alpha %{buildroot}%{_datadir}/ghostscript/Resource/Font/PMW-Alpha
ln -s ../../../pmw/psfonts/PMW-Music.pfa %{buildroot}%{_datadir}/ghostscript/Resource/Font/PMW-Music

%files
%doc doc/ChangeLog doc/spec.pdf contrib doc/examples
%{_bindir}/*
%{_datadir}/pmw
%{_datadir}/ghostscript/Resource/Font/*
%{_mandir}/man1/*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 4.34
- Rebuilt for Fedora
* Fri Mar 30 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.240-1
+ Revision: 788306
- new version 4.24
* Mon Feb 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.231-1
+ Revision: 771360
- new version 4.231
* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 4.06-4mdv2009.0
+ Revision: 259120
- rebuild
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 4.06-3mdv2009.0
+ Revision: 247039
- rebuild
  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot
* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 4.06-1mdv2008.1
+ Revision: 125470
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import pmw
* Tue Dec 07 2004 Abel Cheung <deaddog@mandrake.org> 4.06-1mdk
- Adopt for Mandrakelinux
* Sun Nov 21 2004 Martin Tarenskeen <m.tarenskeen@zonnet.nl>
- initial RPM package release for pmw-4.06
