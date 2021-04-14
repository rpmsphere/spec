Summary: 	GNOME meta themes for the Smooth GTK themes
Name: 		smooth-meta-themes
Version: 	0.5.8
Release: 	6.1
License:	Public Domain
Group: 		User Interface/Desktops
BuildArch: 	noarch
Requires:	smooth-gtk-themes
Requires:   metacity-themes
Requires:   somatic-icon-theme
Requires:   linuxcommunity-backgrounds

%description
GNOME meta themes for the Smooth GTK themes, metacity themes,
icon themes and backgrounds.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cat > index.theme <<EOF
[Desktop Entry]
Name=
Type=X-GNOME-Metatheme
Comment=GTK and Metacity theme
Encoding=UTF-8

[X-GNOME-Metatheme]
GtkTheme=
MetacityTheme=
IconTheme=Somatic
EOF
for i in Delightfully-Smooth G26 Smooth-Funky-Monkey Smooth-Line Smooth-Okayish Smooth-Sea-Ice Smooth-Tangerine-Dream Smooth-Winter
do
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/$i
cp index.theme $RPM_BUILD_ROOT%{_datadir}/themes/$i
done

cd $RPM_BUILD_ROOT%{_datadir}/themes
sed -i -e 's|Name=|Name=Delightfully Smooth|' -e 's|GTK|Delightfully-Smooth GTK|' -e 's|GtkTheme=|GtkTheme=Delightfully-Smooth|' -e 's|MetacityTheme=|MetacityTheme=quiet-purple|' -e '$a BackgroundImage=/usr/share/backgrounds/linuxcommunity/101344-1856x960_new_tb2.jpg' Delightfully-Smooth/index.theme
sed -i -e 's|Name=|Name=G26|' -e 's|GTK|G26 GTK|' -e 's|GtkTheme=|GtkTheme=G26|' -e 's|MetacityTheme=|MetacityTheme=mcblue|' -e '$a BackgroundImage=/usr/share/backgrounds/linuxcommunity/96663-MonteSecco.jpg' G26/index.theme
sed -i -e 's|Name=|Name=Smooth Funky Monkey|' -e 's|GTK|Smooth-Funky-Monkey GTK|' -e 's|GtkTheme=|GtkTheme=Smooth-Funky-Monkey|' -e 's|MetacityTheme=|MetacityTheme=keramik-Gyellow|' -e '$a BackgroundImage=/usr/share/backgrounds/linuxcommunity/116491-JohnsRose1920x1200.jpg' Smooth-Funky-Monkey/index.theme
sed -i -e 's|Name=|Name=Smooth Line|' -e 's|GTK|Smooth-Line GTK|' -e 's|GtkTheme=|GtkTheme=Smooth-Line|' -e 's|MetacityTheme=|MetacityTheme=Urbicande|' -e '$a BackgroundImage=/usr/share/backgrounds/linuxcommunity/69723-Priroda 3.jpg' Smooth-Line/index.theme
sed -i -e 's|Name=|Name=Smooth Okayish|' -e 's|GTK|Smooth-Okayish GTK|' -e 's|GtkTheme=|GtkTheme=Smooth-Okayish|' -e 's|MetacityTheme=|MetacityTheme=BrushedMetal|' -e '$a BackgroundImage=/usr/share/backgrounds/linuxcommunity/kilpisjarvitapeta.jpg' Smooth-Okayish/index.theme
sed -i -e 's|Name=|Name=Smooth Sea Ice|' -e 's|GTK|Smooth-Sea-Ice GTK|' -e 's|GtkTheme=|GtkTheme=Smooth-Sea-Ice|' -e 's|MetacityTheme=|MetacityTheme=Redmond|' -e '$a BackgroundImage=/usr/share/backgrounds/linuxcommunity/108691-1824x1152_wheat_field2.jpg' Smooth-Sea-Ice/index.theme
sed -i -e 's|Name=|Name=Smooth Tangerine Dream|' -e 's|GTK|Smooth-Tangerine-Dream GTK|' -e 's|GtkTheme=|GtkTheme=Smooth-Tangerine-Dream|' -e 's|MetacityTheme=|MetacityTheme=OutlineHot|' -e '$a BackgroundImage=/usr/share/backgrounds/linuxcommunity/111635-FeatheryOrange1920x1200.jpg' Smooth-Tangerine-Dream/index.theme
sed -i -e 's|Name=|Name=Smooth Winter|' -e 's|GTK|Smooth-Winter GTK|' -e 's|GtkTheme=|GtkTheme=Smooth-Winter|' -e 's|MetacityTheme=|MetacityTheme=Watercolor|' -e '$a BackgroundImage=/usr/share/backgrounds/linuxcommunity/116807-Immagine 010-rem1920.jpg' Smooth-Winter/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/*/index.theme

%changelog
* Wed Jul 20 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.8
- Rebuilt for Fedora
