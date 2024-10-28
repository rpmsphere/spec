%undefine _debugsource_packages

Name:           xmove
Version:        2.0
Release:        6.1
Summary:        X11 pseudoserver to dynamically move X11 applications
Source0:        ftp://ftp.cs.columbia.edu/pub/xmove/%{name}.%{version}beta2.tar.bz2
License:        MIT
Group:          System/X11
URL:            ftp://ftp.cs.columbia.edu/pub/xmove/
BuildRequires:  libX11-devel imake
Patch0:         xmove-2.0-unix-domain.patch

%description
xmove is a pseudoserver (aka proxy server) which allows you
to dynamically move an X application between servers, and screens
within a server.

%prep
%setup -q -n %{name}
%patch 0 -p1 -b .unix-domain
chmod 644 doc/*

%build
for i in xmove xmovectrl; do
        cd $i
        ln -sf ../man/man1/$i.1 $i.man
        xmkmf
        make CXXOPTIONS="%optflags" EXTRA_LDOPTIONS="%optflags"
        cd $OLDPWD
done

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{_mandir}/man1/
for i in xmove xmovectrl; do
        cd $i
        %make_install
        cd $OLDPWD
        install -m 644 man/man1/$i.1 $RPM_BUILD_ROOT%{_mandir}/man1/
done

%files
%doc README doc/*
%_bindir/xmove*
%{_mandir}/man1/xmove*

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Fri Oct 18 2013 umeabot <umeabot> 2.0-0.beta2.6.mga4
+ Revision: 520708
- Mageia 4 Mass Rebuild
* Mon Jan 14 2013 umeabot <umeabot> 2.0-0.beta2.5.mga3
+ Revision: 387223
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sun May 08 2011 grenoya <grenoya> 2.0-0.beta2.4.mga1
+ Revision: 96230
- imported package xmove
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 2.0-0.beta2.4mdv2011.0
+ Revision: 634908
- simplify BR
* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.0-0.beta2.3mdv2010.0
+ Revision: 435250
- rebuild
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0-0.beta2.2mdv2009.0
+ Revision: 136612
- restore BuildRoot
* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 2.0-0.beta2.2mdv2008.1
+ Revision: 135615
- adatp to new xorg layout
- BR imake
- kill bogus BR
- kill re-definition of %%buildroot on Pixel's request
- import xmove
* Sat Sep 03 2005 Marcel Pol <mpol@mandriva.org> 2.0-0.beta2.2mdk
- buildrequires x11
* Thu Aug  4 2005 Olivier Blin <oblin@mandriva.com> 2.0-0.beta2.1mdk
- initial Mandriva release
- Patch0: Unix domain sockets support (from Debian)
