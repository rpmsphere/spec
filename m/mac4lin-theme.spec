%define oname Mac4Lin
%define themesdir %{_datadir}/themes
%define pixmapsdir %{_datadir}/pixmaps
%define splashdir %{_datadir}/pixmaps/splash
%define iconsdir %{_datadir}/icons
%define wallpapersdir %{_datadir}/backgrounds
%define wallpaperspropdir %{_datadir}/gnome-background-properties
%define fontsdir %{_datadir}/fonts/Mac4Lin
%define soundsdir %{_datadir}/sounds/Mac4Lin/stereo
%define soundsdir1 %{_datadir}/sounds/Mac4Lin
%define emeralddir %{_datadir}/emerald/themes

Summary: 	Look and feel of MacOS X on *nix systems
Name:     	mac4lin-theme
Version: 	1.0
Release: 	10.1
Source0: 	%{oname}-%{version}.tar.bz2
Source1:	mcosx-wallpaper.xml
License: 	LGPL
Group: 		User Interface/Desktops
URL:   	   	http://sourceforge.net/projects/mac4lin/
BuildArch: 	noarch

%description
Mac4Lin theme contains a full theme based in MC-OSX.
It includes the following components:
   * GTK+ theme
   * Metacity theme
   * Icons set
   * Sounds set
   * Wallpapers
   * Cursor icons theme
   * Splash image
   * Fonts ttp set
   * Emerald theme
By Anirudh Acharya (a.k.a infra_red_dude)

%prep
%setup -q -n %{oname}-%{version}

%install
%__rm -rf %{buildroot}
%__rm -rf __MCOSX
%__rm -f *.sh
%__rm -rf GDM
%__rm -rf GRUB
%__rm -rf Usplash
%__rm -rf AWN
%__rm -rf Mozilla
%__rm -rf MP
%__rm -rf Pidgin
%__rm -rf Songbird
%__install -d %{buildroot}%{themesdir}
%__install -d %{buildroot}%{iconsdir}
%__install -d %{buildroot}%{wallpapersdir}
%__install -d %{buildroot}%{wallpaperspropdir}
%__install -d %{buildroot}%{fontsdir}
%__install -d %{buildroot}%{splashdir}
%__install -d %{buildroot}%{soundsdir}
%__install -d %{buildroot}%{emeralddir}

pushd Fonts
%__rm -rf readme *.png
%__tar -xzf *.tar.gz
%__rm -f *.tar.gz  
%__install -m 644 *.ttf $RPM_BUILD_ROOT/%{fontsdir}
##ttmkfdir $RPM_BUILD_ROOT/%{fontsdir} > $RPM_BUILD_ROOT/%{fontsdir}/fonts.dir
##ln -s fonts.dir $RPM_BUILD_ROOT/%{fontsdir}/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../../%{fontsdir} \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-mac:pri=50
popd

pushd "GTK Splash"
%__cp -f *.png %{buildroot}%{splashdir}
popd

%__cp -f Wallpapers/*.jpg %{buildroot}%{wallpapersdir}
%__cp -f %{SOURCE1} %{buildroot}%{wallpaperspropdir}

pushd Cursor
%__tar -xzf *.tar.gz 
%__rm -f *.tar.gz 
%__cp -a * %{buildroot}%{iconsdir}
popd

pushd GTK
%__tar -xzf Mac4Lin_GTK_Aqua_v1.0.tar.gz
%__tar -xzf Mac4Lin_GTK_Graphite_v1.0.tar.gz  
%__tar -xzf Mac4Lin_Meta_v1.0.tar.gz 
%__cp Mac4Lin_Meta_v1.0/Mac4Lin_Aqua/index.theme Mac4Lin_GTK_Aqua_v1.0/index.theme
%__cp Mac4Lin_Meta_v1.0/Mac4Lin_Graphite/index.theme Mac4Lin_GTK_Graphite_v1.0/index.theme
rm `find . -name *~`
sed -i '$a BackgroundImage=/usr/share/backgrounds/Mac4Lin_Wallpaper1.jpg' Mac4Lin_GTK_Aqua_v1.0/index.theme
sed -i '$a BackgroundImage=/usr/share/backgrounds/Mac4Lin_Wallpaper2.jpg' Mac4Lin_GTK_Graphite_v1.0/index.theme
%__cp -a Mac4Lin_GTK_Aqua_v1.0 Mac4Lin_GTK_Graphite_v1.0 %{buildroot}%{themesdir}
popd

pushd Icons
rm `find . -name *~`
%__cp -a * %{buildroot}%{iconsdir}
popd

pushd Sounds
%__rm -f Mac4Lin_Pidgin-Sounds_v1.0.tar.gz
%__tar -xzf Mac4Lin_Sounds_v1.0.tar.gz 
%__rm -f Mac4Lin_Sounds_v1.0.tar.gz 
%__cp -a * %{buildroot}%{soundsdir}
popd

pushd Emerald
%__rm -f *.emerald
%__tar -xzf Mac4Lin_Emerald_Aqua_v1.0.tar.gz
%__tar -xzf Mac4Lin_Emerald_Graphite_v1.0.tar.gz  
%__rm -f Mac4Lin_Emerald_Aqua_v1.0.tar.gz
%__rm -f Mac4Lin_Emerald_Graphite_v1.0.tar.gz  
%__cp -a * %{buildroot}%{emeralddir}
popd

# Index file for the sound theme.
cat > %{buildroot}%{_datadir}/sounds/Mac4Lin/index.theme <<EOF
[Sound Theme]
Name=Mac4Lin
Directories=stereo

[stereo]
OutputProfile=stereo
EOF

%clean
%__rm -rf %{buildroot}

%post
[ -x /usr/bin/gtk-update-icon-cache ] && gtk-update-icon-cache --quiet %{_datadir}/icons/Mac4Lin
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache -f 2> /dev/null

%postun
[ -x /usr/bin/gtk-update-icon-cache ] && gtk-update-icon-cache --quiet %{_datadir}/icons/Mac4Lin
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache -f 2> /dev/null

%files
%{themesdir}/*
%{pixmapsdir}/*
%{iconsdir}/*
%{wallpapersdir}/*
%{wallpaperspropdir}/*
%{soundsdir}/*
%{soundsdir1}/index.theme
%{emeralddir}/*
%{fontsdir}/*
##%verify(not mtime) %{fontsdir}/fonts.dir
%{_sysconfdir}/X11/fontpath.d/ttf-mac:pri=50

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Mon Oct 04 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.0-1mib2010.1
- First time ported to Mandriva by MIB.
- I have solved a lot of bugs with the index.theme files in the GTK+ and Icons.
- I have added a xml file about the two wallpapers of the theme.
- Fixed permissions with the wallpapers.
