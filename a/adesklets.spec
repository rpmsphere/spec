%undefine _debugsource_packages
Summary:        Simple desklets for Unix
Name:           adesklets
Version:        0.6.1
Release:        1
License:        GPL
URL:            https://adesklets.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Group:          Development/Tools
Requires:       tkinter
BuildRequires:  imlib2-devel python2-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
Patch1:         adesklets-fontconfig24-crashfix.patch
Source1:        imlib2-config

%description
adesklets is an interactive Imlib2 console for the X Window system. It provides
to scripted languages a clean and simple way to write great looking, mildly
interactive desktop integrated graphic applets (aka "desklets").

%prep
%setup -q
%patch 1 -p1
sed -i 's|PKGDATADIR|"%{_datadir}/%{name}"|' src/main.c
cp %{SOURCE1} .

%build
export PATH=$PATH:.
%configure
pushd scripting/perl/
%{__perl} Makefile.PL INSTALLDIRS=vendor
popd
%__make LIBS="-lm -lX11 -lImlib2 -lncurses -lreadline -lhistory -lfontconfig -lfreetype" CFLAGS+="-Wno-format-security -Wno-incompatible-pointer-types"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
%__make DESTDIR=%buildroot install

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}_*

%files
%doc README ChangeLog NEWS INSTALL COPYING AUTHORS 
%{_bindir}/*
%{_infodir}/*.info.gz
%exclude %{_infodir}/dir
%{python2_sitearch}/*
%exclude %{perl_archlib}/*
%{perl_vendorlib}/*
%{_datadir}/adesklets
%{_mandir}/*/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuilt for Fedora
* Mon Jan 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.1-4mdv2008.1
+ Revision: 151759
- rebuild
* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.6.1-3mdv2008.1
+ Revision: 135817
- restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.1-3mdv2007.0
+ Revision: 96503
- Rebuild against new python
- Import adesklets
* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 0.6.1-2mdv2007.0
- rebuild
* Sat May 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.1-1mdk
- New release 0.6.1
* Wed Mar 29 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.0-2mdk
- requires tkinter (Fabrice Facorat, #20404)
* Tue Mar 28 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.0-1mdk
- 0.6.0
* Wed Dec 14 2005 Pascal Terjan <pterjan@mandriva.org> 0.5.0-1mdk
- 0.5.0
* Fri Oct 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.11-2mdk
- Fix BuildRequires
* Sat Sep 03 2005 Pascal Terjan <pterjan@mandriva.org> 0.4.11-1mdk
- 0.4.11
* Mon Aug 15 2005 Pascal Terjan <pterjan@mandriva.org> 0.4.10-1mdk
- First Mandriva package
