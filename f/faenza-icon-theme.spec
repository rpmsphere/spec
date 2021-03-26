%global themes Faenza Faenza-Ambiance Faenza-Dark Faenza-Darker Faenza-Darkest Faenza-Radiance

Name:           faenza-icon-theme
Version:        1.3.1
Release:        3
Summary:        Icon theme designed for Equinox GTK theme
Group:          User Interface/Desktops 
License:        GPLv3
URL:            http://tiheum.deviantart.com/art/Faenza-Icons-173323228
Source0:        http://ppa.launchpad.net/tiheum/equinox/ubuntu/pool/main/f/faenza-icon-theme/%{name}_%{version}.tar.gz
BuildArch:      noarch

%description
This icon theme for Gnome provides monochromatic icons for panels, toolbars and
buttons and colorful squared icons for devices, applications, folder, files and
Gnome menu items. Six themes are included to fit with light or dark
themes/panels.

%prep
%setup -q -n %{name}-1.3
# Remove executable bits on all files
find . -type f -exec chmod 0644 {} \;

%install
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/icons

# link the distributor-logo icon to the Fedora icon
for icon in ./*/places/*/distributor-logo-fedora.*
do
    pushd ${icon%/*}
        ln -sf ${icon##*/} distributor-logo.${icon##*.}
    popd
done

# link the start-here-symbolic icon to the Fedora icon
for icon in ./*/places/*/start-here-fedora-symbolic.*
do
    pushd ${icon%/*}
        ln -sf ${icon##*/} start-here-symbolic.${icon##*.}
    popd
done

# link the start-here icon to the Fedora icon
for icon in ./*/places/*/start-here-fedora.*
do
    pushd ${icon%/*}
        ln -sf ${icon##*/} start-here.${icon##*.}
    popd
done

cp -a Faenza* $RPM_BUILD_ROOT%{_datadir}/icons

%post
for theme in %{themes}
do
    touch --no-create %{_datadir}/icons/${theme} &>/dev/null ||:
done

%postun
if [ $1 -eq 0 ] ; then
    for theme in %{themes}
    do
        touch --no-create %{_datadir}/icons/${theme} &>/dev/null
        gtk-update-icon-cache %{_datadir}/icons/${theme} &>/dev/null || :
    done
fi

%posttrans
for theme in %{themes}
do
    gtk-update-icon-cache %{_datadir}/icons/${theme} &>/dev/null || :
done

%files
%doc debian/changelog debian/copyright
%{_datadir}/icons/Faenza*

%changelog
* Tue Nov 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.1
- Rebuild for Fedora
* Sun Sep 01 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.1-3
- fix start-here icon (BZ#1003265)
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Wed Feb 13 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.1-1
- update to 1.3.1
- point S:1 to Ubuntu PPA source URL
- added the following fixes from Mohamed El Morabity:
  - Add missing %%build section (mandatory even if empty)
  - Link start-here-symbolic icons to the Fedora icon
  - Update description, taken from the DeviantArt theme page
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Fri Oct 14 2011 Felix Kaechele <heffer@fedoraproject.org> - 1.1-1
- update to 1.1
- clean up specfile
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Aug 11 2010 Tajidin Abd <tajidinabd@archlinux.us> - 0.6-1
- New Version from upstream
* Tue Aug 10 2010 Tajidin Abd <tajidinabd@archlinux.us> - 0.5-5
- Cleaned up files macro
- Modified install macro  with -a option to keep timestamps on files
* Mon Aug 09 2010 Tajidin Abd <tajidinabd@archlinux.us> - 0.5-4
- Version number comes from URL
- made corrections to prep macro 
* Sun Aug 08 2010 Tajidin Abd <tajidinabd@arhclinux.us> - 0.5-3
- Corrected version number
- Added scriplet
- Corrected unused of macro
* Sun Aug 08 2010 Tajidin Abd <tajidinabd@archlinux.us> - 0.5.2-2
- added global tarname macro
- Corrected the License 
- made corrections to scriplets
- deleted redundant characters
- changed permission issues to satisfy rpmlint errors
* Thu Aug 05 2010 Tajidin Abd <tajidinabd@archlinux.us> - 0.5.2-1
- Intial RPM release
