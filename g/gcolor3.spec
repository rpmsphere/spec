Name:           gcolor3
Version:        2.2
Release:        6.1
Summary:        A simple color chooser written in GTK3 (like gcolor2)
License:        GPLv2+
URL:            https://github.com/Unia/gcolor3
Source0:        https://github.com/Hjdskes/gcolor3/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         gcolor3-2.2-appdata_url.patch
BuildRequires:  gnome-common,gtk3-devel >= 3.12.0,intltool,desktop-file-utils,gettext,libappstream-glib

%description
Gcolor3 is a color selection dialog written in GTK+ 3. It is much alike Gcolor2,
but uses the newer GTK+ version to better integrate into your modern desktop.
It has the same feature set as Gcolor2, except that recent versions of Gcolor3
use an .ini style file to save colors (older versions use the same file as
Gcolor2).

%prep
%setup -q
%patch0
NOCONFIGURE=1 ./autogen.sh

%build
%configure
sed -i 's|-Wall|-Wall -Wno-error|' Makefile */Makefile
%make_build

%install
%make_install
%find_lang Gcolor3
desktop-file-validate %{buildroot}/%{_datadir}/applications/gcolor3.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/gcolor3.appdata.xml

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f Gcolor3.lang
%doc README.md AUTHORS
%license LICENSE
%{_bindir}/gcolor3
%{_datadir}/appdata/gcolor3.appdata.xml
%{_datadir}/applications/gcolor3.desktop
%{_datadir}/icons/hicolor/scalable/apps/gcolor3.svg

%changelog
* Thu Mar 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Sun Sep 03 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-4
  - Update license field from GPLv2 to GPLv2+
  - Use the --nonet flag in gcolor3.appdata.xml's validation
  - Add an empty line between each changelog entry
* Wed Aug 09 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-3
  - Patch and validate gcolor3.appdata.xml
  - Use the license macro instead of the doc macro for the LICENSE file
  - Remove the deprecated RPM Group
  - use the make_build macro instead of make %%{?_smp_mflags}
  - Add minimal version for gtk3-devel (in BuildRequires)
  - Use a more explicit name for the source file
* Sun Apr 23 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-2
  - Improve specfile in order to comply with the "Fedora Packaging Guidelines"
