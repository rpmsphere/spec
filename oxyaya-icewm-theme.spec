Name:		oxyaya-icewm-theme
Summary:	Oxygen and Aya theme for IceWM
Version:	0.1
Release:	9.1
License:	GPL
Group:		Graphical desktop/Icewm
URL:		http://box-look.org/content/show.php/OxyAya?content=136242
Source0:	http://box-look.org/CONTENT/content-files/136242-oxygen-aya-azul.tar.gz
BuildArch: noarch
BuildRequires:  ghostscript-core ImageMagick

%description
The icewm theme which simulates kde4 "Oxygen" and "Aya" look and feel.

%prep
%setup -q -n oxygen-aya-azul
# Resize image to workaround bug 8705
mogrify -resize 2x19! title*.xpm
mogrify -resize 2x2! *frame??.xpm

%install
install -d %{buildroot}%{_datadir}/icewm/themes
cp -r %{_builddir}/oxygen-aya-azul %{buildroot}/%{_datadir}/icewm/themes/OxyAya

# fix permissions
find %{buildroot}%{_datadir} -type f -exec chmod 644 {} \;
find %{buildroot}%{_datadir} -type d -exec chmod 755 {} \;

%files
%{_datadir}/icewm/themes/*

%changelog
* Thu Mar 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 0.1-8.mga5
+ Revision: 743441
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.1-7.mga5
+ Revision: 680447
- Mageia 5 Mass Rebuild
* Sat Oct 19 2013 umeabot <umeabot> 0.1-6.mga4
+ Revision: 522498
- Mageia 4 Mass Rebuild
* Tue Mar 12 2013 yochenhsieh <yochenhsieh> 0.1-5.mga3
+ Revision: 402120
- Resize images to workaround bug #8705
* Sat Jan 12 2013 umeabot <umeabot> 0.1-4.mga3
+ Revision: 354190
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Feb 29 2012 yochenhsieh <yochenhsieh> 0.1-3.mga2
+ Revision: 216002
- Use existing icon directly which works as expected
* Thu Feb 23 2012 fwang <fwang> 0.1-2.mga2
+ Revision: 212497
- bump rel
  + yochenhsieh <yochenhsieh>
    - Use large icon for conversion source.
      Set default Mageia background as wallpaper.
* Thu Feb 23 2012 fwang <fwang> 0.1-1.mga2
+ Revision: 212486
- use image in desktop-common-data instead of own icon
  + yochenhsieh <yochenhsieh>
    - imported package icewm-theme-oxygen-aya
