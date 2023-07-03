Name:           weather-wallpaper
Version:        0.2.0
Release:        12.1
Summary:        Utility to create a wallpaper based on the current weather
License:        GPL-2.0
Group:          Amusements/Toys/Background
URL:            https://mundogeek.net/weather-wallpaper/
Source0:        https://launchpadlibrarian.net/17362202/weather-wallpaper_0.2.0-1.tar.gz
# PATCH-FIX-UPSTREAM weather-wallpaper-update-for-gnome3.patch lp#921375 malcolmlewis@opensuse.org -- Update python code to use gsettings as well as gconf.
Patch0:         weather-wallpaper-update-for-gnome3.patch
# PATCH-FIX-UPSTREAM weather-wallpaper-fix-desktop-file.patch lp#929642 malcolmlewis@opensuse.org -- Add trailing ; to desktop categories.
Patch1:         weather-wallpaper-fix-desktop-file.patch
BuildRequires:  python2-devel
Requires:       ImageMagick
Requires:       inkscape
Requires:       pygtk2
Requires:       pymetar
BuildArch:      noarch

%description
Weather wallpaper is a program which connects to NOAA each hour to get the
current weather at the specified location and creates and sets a wallpaper
with the data retrieved.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make

%install
%make_install
# Remove installed files as we'll package them as rpm docs
rm %{buildroot}%{_datadir}/%{name}/AUTHORS \
   %{buildroot}%{_datadir}/%{name}/COPYING \
   %{buildroot}%{_datadir}/%{name}/TRANSLATORS
%find_lang %{name} %{?no_lang_C}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files -f %{name}.lang
%doc AUTHORS changelog COPYING TRANSLATORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Sun Sep 23 2012 dimstar@opensuse.org
- Do not call suse_update_desktop_file with '-n' parameter: there
  is no reason why we would not want translations in the .desktop
  file.
* Thu Feb  9 2012 malcolmlewis@opensuse.org
- Initial build.
- Add weather-wallpaper-update-for-gnome3.patch: Update python
  code to use gsettings as well as gconf (lp#921375).
- Add weather-wallpaper-fix-desktop-file.patch: Add trailing ; to
  desktop categories (lp#929642).
