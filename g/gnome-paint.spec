Name:           gnome-paint
Version:        0.4.0
Release:        18.1
Summary:        Easy to use paint program
Group:          Graphics/Editors and Converters
License:        GPLv3+
URL:            https://launchpad.net/gnome-paint
Source0:        http://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        %{name}.1
Patch0:         %{name}-deb-crash-in-toolbar.patch
Patch1:         %{name}-deb-ftbfs-format-security.patch
Patch2:         %{name}-deb-ftbfs-libs-lm.patch
Patch3:         %{name}-deb-handle-urls.patch
Patch4:         %{name}-deb-update_translations.patch
Patch5:         %{name}-alt-packaging.patch
Patch6:         %{name}-mga-desktop.patch
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-2.0)

%description
Simple, easy to use paint program for GNOME.
gnome-paint is a program inspired by MS Paint and designed for 
GNOME (and maybe other) desktop environment. It could be used to 
manipulate images in a very simple way. With a very friendly 
user interface, gnome-paint is easy to get started for new users.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
autoreconf -fisv
%configure
make CFLAGS+="-Wno-format-security -lm"

%install
%make_install
#remove docs, use rpmbuild instead
rm -rf %{buildroot}%{_prefix}/doc
#remove unnecessary includedir files
rm -rf %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
mv -f %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gp.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_mandir}/man1/%{name}*

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuild for Fedora
* Tue Jan 06 2015 alexl <alexl> 0.4.0-4.mga5
+ Revision: 808864
- new desktop file with GenericName
* Wed Oct 15 2014 umeabot <umeabot> 0.4.0-3.mga5
+ Revision: 741057
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.4.0-2.mga5
+ Revision: 679745
- Mageia 5 Mass Rebuild
* Fri Apr 18 2014 alexl <alexl> 0.4.0-1.mga5
+ Revision: 616524
- imported package gnome-paint
