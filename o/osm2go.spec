%global subrelease 2

Name:           osm2go
Version:        0.8.3
Release:        16.4
Summary:        A simple openstreetmap editor
Group:          Applications/Internet
License:        GPLv3+
URL:            http://www.harbaum.org/till/maemo/index.shtml#osm2go
Source0:        http://repository.maemo.org/extras/pool/fremantle/free/source/o/osm2go/osm2go_%{version}-maemo%{subrelease}.tar.gz
Patch0:         %{name}-linking.patch
BuildRequires:  libpng-devel
BuildRequires:  goocanvas-devel
BuildRequires:  libgnome-devel
BuildRequires:  libcurl-devel
BuildRequires:  libsoup-devel
BuildRequires:  libxml2-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  sane-backends-devel
BuildRequires:  desktop-file-utils
BuildRequires:  udisks2
Requires:       hicolor-icon-theme

%description
OSM2Go is an editor for openstreetmap.org map data. OSM2Go is designed
for simplicity and user friendliness and not for maximum feature count.
It is meant for simple mapping on the road.

%prep
%setup -q
%patch0 -p1 -b .linking
sed -i '/curl\/types.h/d' src/osm_api.c src/net_io.c

%build
%configure
sed -i 's|-Werror=format-security||' Makefile src/Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
install -Dp -m 0644 data/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
desktop-file-install                                        \
    --add-category="Education;Network;"                     \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications              \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc ChangeLog COPYING readme.txt
%{_mandir}/man*/%{name}*.1*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.3
- Rebuilt for Fedora
* Mon Aug 30 2010 Fabian Affolter <fabian@bernewireless.net> - 0.8.3-4.2
- Changed source URL
- Typos fixed in description
- Changed path for the man page
- Removed the second license file
* Sat Aug 14 2010 Fabian Affolter <fabian@bernewireless.net> - 0.8.3-3.2
- Added patch to fix DSO linking issue
* Mon Jun 07 2010 Fabian Affolter <fabian@bernewireless.net> - 0.8.3-2.2
- Changed to new upstream version
- According to upstream the license is GPLv3+
* Fri Feb 19 2010 Fabian Affolter <fabian@bernewireless.net> - 0.8.3-1
- Updated to new upstream version 0.8.3
* Tue Oct 13 2009 Fabian Affolter <fabian@bernewireless.net> - 0.7.22-1
- Added hicolor-icon-theme
- Updated to new upstream version 0.7.22
* Tue Oct 13 2009 Fabian Affolter <fabian@bernewireless.net> - 0.7.21-1
- Removed the preparation for l10n
- Updated to new upstream version 0.7.21
* Wed Sep 16 2009 Fabian Affolter <fabian@bernewireless.net> - 0.7.19-1
- Initial spec for Fedora
