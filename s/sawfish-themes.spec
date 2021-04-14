Summary:	A collection of themes for the sawfish window manager
Name:		sawfish-themes
Version: 	0.2
Release:	54.1
License:	GPL
Group:		Graphical desktop/Sawfish
URL:		http://themes.freshmeat.net/browse/927/
BuildArch:	noarch
Source:		%{name}-%{version}.tar.bz2
Source1:	BrushedMetalII.tar.bz2
Source2:	Chromium.tar.bz2
Source3:	CoolClean.tar.bz2
Source4:	SawBox.tar.bz2
Source5:	Smalldome.tar.bz2
Source6:	Step.tar.bz2
Source7:	TigDomeII.tar.bz2
Source8:	blue-steel.tar.bz2
Source9:	brushed-gtk.tar.bz2
Source10:	iron.tar.bz2
Source11:	SawBoxL.tar.bz2
Source12:	HeliX-gray.tar.bz2
Source13:	LockSmith.tar.bz2
Source14:	Alien8.tar.bz2
Source15:	MetalliqueS.tar.bz2 
Source16:	SawTech-Hydro.tar.bz2
Source17:	StyleS.tar.bz2
Source18:	cyrus.tar.bz2
Source19: 	s.t.o.2.tar.bz2
Source20: 	s12.tar.bz2
Source21:	s13.tar.bz2
Source22:	s6.5.tar.bz2
Source23:	sawSlate.tar.bz2
Source24:	shinyblue.tar.bz2
Source25:	Eazel-blue.tar.bz2
Source26:	LiquidMetal.tar.bz2
Source27:	Mozilla-modern.tar.bz2
Source28:	glass.tar.bz2
# from helix code ftp://ftp.whatnot.org/pub/helix-sweetpill/helix-sweetpill-0.1.tar.bz2
Source29:	HeliX-Sweetpill-Blackcurrant.tar.bz2
Source30:	HeliX-Sweetpill-Citrus.tar.bz2
Source31:	HeliX-Sweetpill-Crowberry.tar.bz2
Source32:	HeliX-Sweetpill-Eggplant.tar.bz2
Source33:	HeliX-Sweetpill-Jade.tar.bz2
Source34:	HeliX-Sweetpill-Lime.tar.bz2
Source35:	HeliX-Sweetpill-Popcorn.tar.bz2
Source36:	HeliX-Sweetpill-Pumpkin.tar.bz2
Source37:	BlueElegance-mdk.tar.bz2
Source38:	GEX.tar.bz2
Source39:	Operational.tar.bz2
Source40:	Silver.tar.bz2
Requires:	sawfish >= 0.27

%description
This is a collection of themes for the Sawfish window manager.
Authors include John Harper <jsh@users.sourceforge.net> and 
Tuomas Kuosmanen <tigert@helixcode.com>.

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/sawfish/themes/
for tarball in \
	%{SOURCE1} \
	%{SOURCE2} \
	%{SOURCE3} \
	%{SOURCE4} \
	%{SOURCE5} \
	%{SOURCE6} \
	%{SOURCE7} \
	%{SOURCE8} \
	%{SOURCE9} \
	%{SOURCE10} \
	%{SOURCE11} \
	%{SOURCE12} \
	%{SOURCE13} \
	%{SOURCE14} \
	%{SOURCE15} \
	%{SOURCE16} \
	%{SOURCE17} \
	%{SOURCE18} \
	%{SOURCE19} \
	%{SOURCE20} \
	%{SOURCE21} \
	%{SOURCE22} \
	%{SOURCE23} \
	%{SOURCE24} \
	%{SOURCE25} \
	%{SOURCE26} \
	%{SOURCE27} \
	%{SOURCE28} \
	%{SOURCE29} \
	%{SOURCE30} \
	%{SOURCE31} \
	%{SOURCE32} \
	%{SOURCE33} \
	%{SOURCE34} \
	%{SOURCE35} \
	%{SOURCE36} \
	%{SOURCE37} \
	%{SOURCE38} \
	%{SOURCE39} \
	%{SOURCE40}; do
	cp $tarball $RPM_BUILD_ROOT%{_datadir}/sawfish/themes/
done;

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README
%{_datadir}/sawfish/themes/*

%changelog
* Wed Aug 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Mon Sep 12 2005 Götz Waschk <waschk@mandriva.org> 0.2-13mdk
- new URL
* Fri Sep 10 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2-12mdk
- Rebuild
* Sat Aug 02 2003 Levi Ramsey <levi@cygnetnet.net> 0.2-11mdk
- Change URL (thx Adam)
- New themes: GEX, Operational, Silver
* Fri Aug 01 2003 Levi Ramsey <levi@cygnetnet.net> 0.2-10mdk
- Fix URL/description to reflect the death of the old themes.org
- Add theme: BlueElegance-mdk
* Fri Feb 14 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2-9mdk
- Rebuild
* Wed Aug 22 2001 dam's <damien@mandrakesoft.com> 0.2-8mdk
- added Provides
* Mon Aug 13 2001 dam's <damien@mandrakesoft.com> 0.2-7mdk
- rebuilt
* Thu Apr 05 2001 Vincent Danen <vdanen@mandrakesoft.com> 0.2-6mdk
- added four new themes to match some gtk themes
- fix url
- make buildarch: noarch
* Mon Nov 27 2000 dam's <damien@mandrakesoft.com> 0.2-5mdk
- added doumentation
* Sat Sep 23 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.2-4mdk
- corrected sweetpill themes
* Fri Sep 22 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.2-3mdk
- added helix sweetpill themes
- updated description
- used %{SOURCExx} instead of explicit filenames
* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 0.2-2mdk
- BM + macrozification.
* Thu Jun 22 2000 dam's <damien@mandrakesoft.com> 0.2-1mdk
- update to helix version.
* Tue Apr 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1-3mdk
- merge themes from Vincent Danen <vdanen@linux-mandrake.com>
* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.1-2mdk
- fix group.
* Tue Mar 28 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.1-1mdk
- Use the helixcode package for gnome.
- Mandrakized.
