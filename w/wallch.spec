%global debug_package %{nil}

Name:		wallch
Version:	4.15.r213
Release:	10.1
Summary:	A wallpaper changer
License:	GPLv3
URL:		http://melloristudio.com/wallch/
Source0:	wallch-4.15.r213.tar.gz
Source1:	wallch.desktop
Source2:	wallch.appdata.xml
Source3:	generate-tarball.sh
Patch0:		%{name}-4.15-qt4-compat.patch
Patch1:		%{name}-4.15-remove-unity-dependency.patch
Patch2:		%{name}-4.15-math.patch
BuildRequires:	dbus-glib-devel libnotify-devel libappindicator-devel
BuildRequires:	libdbusmenu-devel libexif-devel keybinder-devel
BuildRequires:	qt5-qtbase-devel qt5-qtwebkit-devel
BuildRequires:	desktop-file-utils libappstream-glib
Requires:	xdg-utils unzip
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils

%description
Wallch doesn't simply change your desktop
background with the wallpapers that you have in your hard disk, though.
While it does that well by monitoring the folder that you have selected
for new or deleted pictures, it has lots of features, like
Picture of the day, Live Earth, Wallpaper Clocks and Live Website! 

%prep
%setup -q
%patch0 -p0 -b .compat
%patch1 -p0 -b .unity
%patch2 -p1 -b .math

%build
qmake-qt5 *.pro
make %{?_smp_mflags}

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT/usr/share/wallch/files/
install -d $RPM_BUILD_ROOT/etc/bash_completion.d/
install -d $RPM_BUILD_ROOT/%{_mandir}/man1/
install -d $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
install -d $RPM_BUILD_ROOT/%{_datadir}/appdata/

install wallch $RPM_BUILD_ROOT/%{_bindir}
install src/themes/indicator_* $RPM_BUILD_ROOT/usr/share/wallch/files/
install data/bash_autocompletion/wallch $RPM_BUILD_ROOT/etc/bash_completion.d/
install data/man/wallch.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/
install data/pixmap/wallch.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
desktop-file-install %{SOURCE1}
install %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/appdata/


# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Icon_Cache
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc README
%license COPYING
%{_bindir}/wallch
%{_mandir}/man1/wallch.1*
/etc/bash_completion.d/wallch
%{_datadir}/wallch/files/indicator_*
%{_datadir}/applications/wallch.desktop
%{_datadir}/pixmaps/wallch.png
%{_datadir}/appdata/wallch.appdata.xml

%changelog
* Wed Jan 04 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.15.r213
- Rebuild for Fedora
* Tue May 17 2016 Jakub Jelen <jjelen@redhat.com> - 4.15.r213-2
- Add missing cmath include to work on Fedora 24
* Tue May 17 2016 Jakub Jelen <jjelen@redhat.com> - 4.15.r213-1
- Build latest bzr "release" with several bug fixes
* Tue Dec 22 2015 Jakub Jelen <jjelen@redhat.com> 4.15-2
- Move to qt5, rebase patches, fix icons
* Mon Dec 21 2015 Jakub Jelen <jjelen@redhat.com> 4.15-1
- Initial release for Fedora
