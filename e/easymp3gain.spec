Name:		easymp3gain
Version:	0.5.0
Release:	16.1
License:	GPLv2
Summary:	Graphical user interface for MP3Gain, AACGain and VorbisGain (GTK2)
Group:		Sound/Utilities
URL:		http://easymp3gain.sourceforge.net
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
Patch1:		easymp3gain-0.5.0-desktop.patch
Patch3:		fix_missing_LazarusDir.diff
Patch4:		fix_missing_overload_on_AddTask.diff
BuildRequires:	fpc
BuildRequires:	lazarus
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
Requires:	mp3gain
Requires:	vorbisgain

%description
easyMP3Gain is a graphical user interface for MP3Gain, AACGain and VorbisGain.
(enables you to modify the loudness level of mp3,ogg,mp4 files)

%prep
%setup -q

%ifarch aarch64
sed -i s/x86_64/aarch64/ easymp3gain.lpi
%endif

%patch1 -p0
%patch3 -p1
%patch4 -p1

%build
%__make all

%install
./install.sh DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Tue Aug 23 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
* Mon Jul 04 2016 pterjan <pterjan> 0.5.0-10.mga6
+ Revision: 1038639
- Support building on arm
* Mon Feb 08 2016 umeabot <umeabot> 0.5.0-9.mga6
+ Revision: 944224
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.5.0-8.mga5
+ Revision: 746016
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.5.0-7.mga5
+ Revision: 678909
- Mageia 5 Mass Rebuild
* Fri Mar 21 2014 wally <wally> 0.5.0-6.mga5
+ Revision: 606402
- rebuild for mga5
  + umeabot <umeabot>
    - Mageia 4 Mass Rebuild
* Wed Sep 18 2013 fwang <fwang> 0.5.0-5.mga4
+ Revision: 481148
- patch 2 is not needed
- add archlinux patch to make it build with latest gfortran
* Fri Jan 11 2013 umeabot <umeabot> 0.5.0-4.mga3
+ Revision: 349279
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Nov 27 2012 dams <dams> 0.5.0-3.mga3
+ Revision: 322394
- update %%group for new policy
* Wed Jul 18 2012 dams <dams> 0.5.0-2.mga3
+ Revision: 272302
- fix .desktop file (missing semicolon)
- clean specfile
- import as requested in mga#2483
- imported package easymp3gain
* Wed Feb 22 2012 Andrey Bondrov <abondrov@mandriva.org> 0.5.0-2
+ Revision: 779252
- Disable debug package
- Update file list
- imported package easymp3gain
* Fri Dec 31 2010 Andrey Bondrov <bondrov@math.dvgu.ru> 0.5.0-69.1mib2010.2
- New version
* Sun May 31 2009 Andrey Bondrov <bondrov@math.dvgu.ru> 0.4.2-69.1mib2009.1
- First build for MIB users
