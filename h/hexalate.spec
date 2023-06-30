Name:           hexalate
Version:        1.2.0
Release:        1
Summary:        Color matching game
License:        GPLv3+
URL:            https://gottcode.org/%{name}/
Source:         https://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qttools-devel
Requires:       hicolor-icon-theme

%description
Hexalate is a color matching game. The goal of the game is to rotate and
position the circles so that each touching line matches in color. You
rotate circles by right clicking, and you move circles by dragging them.
The game stores the positions and rotations of the circles across runs.

%prep
%setup -q

%build
%{qmake_qt5} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt --without-mo

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc ChangeLog CREDITS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
#%{_datadir}/pixmaps/%{name}.xpm
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/
%{_mandir}/man6/%{name}.6.*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Tue Nov 07 2017 Mario Blättermann <mario.blaettermann@gmail.com> - 1.1.1-1
- New upstream version
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Wed Nov 02 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.1.0-1
- New upstream version
- Remove custom appdata file
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.3-3
- Rebuilt for GCC 5 C++11 ABI change
* Tue Feb 17 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.0.3-2
- Add appdata file
* Sun Feb 15 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.0.3-1
- Initial package
