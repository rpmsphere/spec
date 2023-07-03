%define _name NeoTool

BuildArch:	noarch
Name:           neotool
Group:          Development/Tools/Other
Requires:       bash, zenity, util-linux, gawk, dfu-util, xterm
Version:        1.2.3
Release:        8.1
URL:            https://wiki.openmoko.org/wiki/NeoTool
Summary:        A bash script to provide a GUI frontend for flashing Openmoko for instance
License:        GPLv3
Source0:        %{_name}
Source1:        %{_name}.desktop
Source2:        %{_name}_16x16.png
Source3:        %{_name}_24x24.png
Source4:        %{_name}_32x32.png
Source5:        %{_name}_48x48.png
Source6:        %{_name}_root-mode.desktop

%description
NeoTool is a bash script for your desktop system to provide a friendly GUI
frontend to some common management tasks, like for example flashing Openmoko
smartphones. It is aimed at being very intuitive and easy to use, and flexible
enough to make it useful in a wide variety of circumstances.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{S:0}  $RPM_BUILD_ROOT/%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/24x24/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cp -avL %{S:2} $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps/NeoTool.png
cp -avL %{S:3} $RPM_BUILD_ROOT/usr/share/icons/hicolor/24x24/apps/NeoTool.png
cp -avL %{S:4} $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps/NeoTool.png
cp -avL %{S:5} $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps/NeoTool.png
cp -avL %{S:1} $RPM_BUILD_ROOT/usr/share/applications/NeoTool.desktop
cp -avL %{S:6} $RPM_BUILD_ROOT/usr/share/applications/NeoTool_root-mode.desktop

%files
%{_bindir}/neotool
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.3
- Rebuilt for Fedora
* Sun May 23 2010 joop.boonen@opensuse.org
- Buid version 1.2.3 with xterm for flash progress
* Sun Jan 10 2010 joop.boonen@opensuse.org
- Made it possibe to run NeoTool also as root
* Tue Jul 28 2009 joop.boonen@opensuse.org
- Correction in script
* Sat Feb 21 2009 joop.boonen@opensuse.org
- Adapted the script
- It can now be run as a user in group uucp
* Tue Jan 20 2009 joop.boonen@opensuse.org
- Building including icons etc
* Tue Jan 13 2009 joop.boonen@opensuse.org
- build NeoTool v1.2
