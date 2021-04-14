Summary: User contributed themes for xpenguins
Name: xpenguins-themes-contrib
Version: 1.0
Release: 19.1
Source0: http://xpenguins.seul.org/contrib/Megaman.tar.gz
Source1: http://xpenguins.seul.org/contrib/Turkeys.tar.gz
Source2: http://xpenguins.seul.org/contrib/Walking_Man.tar.bz2
Source3: http://xpenguins.seul.org/contrib/Ninja-0_9b.tar.gz
Source4: http://xpenguins.seul.org/contrib/xpenguins_theme_mule-1.1.tar.gz
Source5: http://www.linuxforblondes.com/applications/esheep/_files/xsheep.tar.gz
#http://www.murga-linux.com/puppy/viewtopic.php?t=35002
Source6: XPark.tar.gz
#Source7: http://xpenguins.seul.org/contrib/xpenguins_theme_lemmings-1.1.tar.gz
#http://nepeta.mozai.com/shimeji/xpenguins-theme-Alterniabound.tgz
Source8: Alterniabound.tar.gz
#http://nepeta.mozai.com/shimeji/xpenguins-theme-Nepeta-by-ZethRina.tgz
Source9: shimeji_Nepeta.tar.gz
#http://regrunner.de/
Source10: TheRegRunner.tar.gz
Group: Amusements/Graphics
Requires: xpenguins >= 1.9
License: unknown
URL: http://xpenguins.seul.org/contrib/
BuildArch: noarch
Provides: xsheep

%description
Themes for xpenguins: "Megaman", "Turkeys", "Walking Man", "Ninja",
"M.U.L.E.", "XSheep", "XPark", "Alterniabound", "shimeji Nepeta" and
"TheRegRunner". These are contributed separately from users of
xpenguins so the licensing/copyright situation is unclear.
Type "xpenguins -l" to see a list of available themes.

%prep
%setup -q -c -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 8 -a 9 -a 10
rm -r Walking_Man/.xvpics XSheep/config~
sed -i -e '/explosion.xpm/d' -e '/zapped.xpm/d' -e '/angel.xpm/d' Ninja/config

%install
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xpenguins/themes
cp -a * $RPM_BUILD_ROOT/%{_datadir}/xpenguins/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/xpenguins/themes/Megaman
%{_datadir}/xpenguins/themes/Turkeys
%{_datadir}/xpenguins/themes/Walking_Man
%{_datadir}/xpenguins/themes/Ninja
%{_datadir}/xpenguins/themes/M.U.L.E.
%{_datadir}/xpenguins/themes/XSheep
%{_datadir}/xpenguins/themes/XPark
%{_datadir}/xpenguins/themes/Alterniabound
%{_datadir}/xpenguins/themes/shimeji_Nepeta
%{_datadir}/xpenguins/themes/TheRegRunner

%changelog
* Sun Aug 26 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
