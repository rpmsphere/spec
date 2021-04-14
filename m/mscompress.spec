Summary:	MS compress/expand-compatible (de)compressor
Name:		mscompress
Version:	0.3
Release:	1
License:	GPL
Group:		Archiving/Compression
URL:            ftp://ftp.penguin.cz/pub/users/mhi/mscompress
Source0:	ftp://ftp.penguin.cz/pub/users/mhi/mscompress/%{name}-%{version}.tar.bz2
Patch0:		mscompress-0.3-LDFLAGS.diff
BuildRequires:	autoconf

%description
Microsoft compress.exe/expand.exe-compatible file (de)compressor.

%prep
%setup -q
%patch0 -p0

%build
autoconf
%configure
%__make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install mscompress msexpand $RPM_BUILD_ROOT%{_bindir}
install mscompress.1 msexpand.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog README TODO format.txt
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-9mdv2009.1
+ Revision: 317114
- use %%optflags and %%ldflags (P0)
* Tue Jun 17 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-8mdv2009.0
+ Revision: 223323
- rebuild
* Tue Jan 15 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-6mdv2008.1
+ Revision: 153264
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 0.3-5mdv2008.0
+ Revision: 68538
- rebuild
* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 19:48:03 (55069)
- rebuild
* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 19:47:15 (55068)
Import mscompress
* Fri Dec 30 2005 Olivier Thauvin <nanardon@mandriva.org> 0.3-3mdk
- rebuild
- mkrel
* Fri Sep 03 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3-2mdk
- yearly rebuild
