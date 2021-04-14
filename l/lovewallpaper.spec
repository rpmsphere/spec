%undefine _debugsource_packages
Name:           lovewallpaper
Version:        1.5.4
Release:        4.1
License:        opensource
Summary:        The most professional WallPaper Application
URL:            http://lovebizhi.com
Group:          System/GUI/GNOME
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  python-devel
Requires:       python-pyside
BuildArch:      noarch

%description
Lovewallpaper is a simple app letting you able to play around with your desktop
wallpapers. Get access to over 500,000 wallpapers in all kinds and start the fun!

%prep
%setup -q

%build

%install
#build dirs
mkdir -p %{buildroot}%{python2_sitelib}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_bindir}/
#copy files
cp -r ./* %{buildroot}%{python2_sitelib}/%{name}/
#deploy icon file
ln -s  %{python2_sitelib}/%{name}/source/notify.png %{buildroot}%{_datadir}/pixmaps/love-wallpaper.png
#deploy .desktop file
mv %{buildroot}%{python2_sitelib}/%{name}/love-wallpaper.desktop %{buildroot}%{_datadir}/applications/love-wallpaper.desktop
sed -i 's|Utility;.*||' %{buildroot}%{_datadir}/applications/love-wallpaper.desktop
#deploy launcher file
mv %{buildroot}%{python2_sitelib}/%{name}/source/love-wallpaper.at_usr_bin %{buildroot}%{_bindir}/love-wallpaper
echo /usr/bin/python2 %{python2_sitelib}/%{name}/love-wallpaper >> %{buildroot}%{_bindir}/love-wallpaper

%files
%{_bindir}/love-wallpaper
%{_datadir}/applications/love-wallpaper.desktop
%{_datadir}/pixmaps/love-wallpaper.png
%{python2_sitelib}/%{name}

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.4
- Rebuilt for Fedora
* Tue Nov 13 2012 avastms@ghostunix.org
- version 1.5.4
  * Added support for Mate.
  * Added support for LXDE.
  * Multiple bug fix.
* Mon Oct 22 2012 avastms@ghostunix.org
- version 1.5.3
  * Merge StartOS Team patch about StartOS and KDE Support
  * Add plugin select list
  * Add Mac Support
* Sat Oct 13 2012 avastms@jhxs.org
- fix on fedora dependency.
* Sun Sep 23 2012 avastms@ghostunix.org
- version 1.5.2
  * off-line mode
  * merged changes from avastms
* Sat Sep 22 2012 avastms@ghostunix.org
- necessary change in source code due to change of install dir
* Sat Sep 22 2012 i@marguerite.su
- fix install dir.
  * openSUSE use %%{python2_sitelib} instead of pyshared.
  * fix spec
- clean source
- no Chinese changelog.
* Fri Sep 21 2012 avastms@ghostunix.org
-1.5.1 Open Source
  * open source everything except the wallpaper server API, provides .py
  * imporve .desktop file
  * link repeated files
  * tweak some module to make propiretary module works with open source ones.
* Thu Sep 20 2012 info@lovebizhi.com
-1.5.1 Version
  * add support for XFCE DE
  * fix the multi-screen width/height bug
  * fix program flash error
  * fix KDE path bug
  * other improvements
-1.5 Version
  * rewrite based on PySide, redesign UI and effects
  * support plugins. increase KDE 4.5 support to 4.8 (need xdotool)
