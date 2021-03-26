Name: darkt-icewm-theme
Version: 0.1.0
Release: 2.1
License: GPL
Group: Graphical desktop/Icewm
URL: http://icewmdarkt.berlios.de
Summary: A theme for IceWM inspired by the Silver Vista, IceVista and VistaBlack themes
BuildArch: noarch
Requires: icewm
Source: http://download.berlios.de/icewmdarkt/darkt-0.1.0.tar.gz

%description
These themes were inspired by the Silver Vista, IceVista and VistaBlack themes.
They have a look based on gradients, rounded borders and shaped windows's decorations.
Currently there are two themes: DarkT and DarkT II.

%prep
%setup -q -c

%build

%install
mkdir -p %buildroot%_datadir/icewm/themes
cp -a * %buildroot%_datadir/icewm/themes

# don't use nonexistent background image
/bin/sed -i 's|DesktopBackgroundImage="bgimage.png"|# DesktopBackgroundImage=""|' %buildroot%_datadir/icewm/themes/*/default.theme
# show default network status
/bin/sed -i 's|NetworkStatusDevice|# NetworkStatusDevice|' %buildroot%_datadir/icewm/themes/*/default.theme
# fix font name
/bin/sed -i 's|-koi8-r|-*-*|g' %buildroot%_datadir/icewm/themes/*/default.theme

/bin/find %buildroot%_datadir/icewm/themes -type f -print0 | 
	xargs -r0 chmod 0444
/bin/find %buildroot%_datadir/icewm/themes -type d -print0 | 
	xargs -r0 chmod 0755

%files
%_datadir/icewm/themes/*

%changelog
* Thu Mar 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuild for Fedora
* Sun Jan 06 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.1.0-alt2
- updated some .xpm's for fix breaks themes with xorg 1.12.3.902 and later
  (bfo#54168)
* Sun Mar 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 0.1.0-alt1
- initial build for ALTLinux
