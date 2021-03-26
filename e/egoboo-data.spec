%global __os_install_post %{nil}

Name:           egoboo-data
Version:        2.7.7
Release:        1
Summary:        Data files for the Egoboo RPG
Group:          Amusements/Games
License:        GPL+
URL:            http://home.no.net/egoboo/
# This is http://downloads.sourceforge.net/egoboo/egob275.exe
# installed under wine, with the exe's and dll's removed from
# ~/.wine/drive_c/Program\ Files/Egoboo\ Development\ Team/Egoboo
# and then put in a tarbal. I'll try to educate upstream to make this
# available in a better suited format.
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildArch:      noarch
Requires:       hicolor-icon-theme
# so that we get uninstalled together with egoboo
Requires:       egoboo >= %{version}

%description
Data files for the Egoboo RPG. 

%prep
%setup -q
sed -i 's/\r//' Changelog.txt Readme.txt

%build
convert basicdat/icon.bmp -transparent '#c8c8c8' egoboo.png

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/egoboo
cp -a controls.txt setup.txt basicdat modules players \
  $RPM_BUILD_ROOT%{_datadir}/egoboo

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -m 644 egoboo.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%doc *.pdf Changelog.txt Readme.txt
%{_datadir}/egoboo
%{_datadir}/icons/hicolor/64x64/apps/egoboo.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.7
- Rebuild for Fedora
* Fri Oct 31 2008 Wind <yc.yan@ossii.com.tw> 2.7.7-1
- Rebuild for OSSII.
* Mon Dec 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.7.5-1
- New upstream release 2.7.5
* Mon Oct 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.4b-1
- New upstream release 2.4.4b
* Sun Oct  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.3-1
- Initial Fedora package
