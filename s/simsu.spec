Name:           simsu
Version:        1.4.0
Release:        1
Summary:        Basic Sudoku game
Summary(de):    Einfaches Sudoku-Spiel
License:        GPLv3+
URL:            https://gottcode.org/%{name}/
Source0:        https://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2
Source1:        %{name}.6.po
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  po4a
BuildRequires:  qt5-qttools-devel
Requires:       hicolor-icon-theme

%description
Simsu is a basic Sudoku game. You can switch between filling in notes
(pencil mode), or filling in answers (pen mode). To make it easier to see
where to place numbers, you can highlight all instances of a number.
You can also check your answers for correctness while playing. The game
stores your current notes and answers, so that you can pick up where you
left off the next time you play.

%description -l de
Simsu ist ein einfaches Sudoku-Spiel. Sie können wechseln zwischen dem 
Eintragen von Notizen (Bleistift-Modus) und dem festen Eintragen der Ziffern
(Füller-Modus). Um besser beurteilen zu können, wo welche Ziffern
eingetragen werden müssen, können Sie alle Vorkommen einer Ziffer
hervorheben. Sie können auch während des Spiels prüfen, ob Ihre bisherigen
Eintragungen korrekt sind. Das Spiel speichert Ihre Notizen und festen
Eintragungen, so dass diese beim Beenden erhalten bleiben und beim nächsten
Start des Spiels wieder verfügbar sind.

%prep
%setup -q

%build
%{qmake_qt5} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man6/
install -p -m 644 doc/%{name}.6 %{buildroot}%{_mandir}/man6/

# Generate and install localized man pages
mkdir -p man/de
po4a-translate -M utf-8 -f man \
               --option groff_code=verbatim \
               -m doc/%{name}.6 -p %SOURCE1 \
               -l man/de/%{name}.6

#mkdir -p %{buildroot}/%{_mandir}/de/man6
#install -p -m 0644 man/de/%{name}.6 %{buildroot}/%{_mandir}/de/man6

%find_lang %{name} --with-qt --without-mo --with-man

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop || :
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml || :

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
%doc CREDITS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations
%{_datadir}/icons/hicolor/*/apps/%{name}.*
#%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man6/%{name}.6.*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.0
- Rebuilt for Fedora
* Wed Nov 08 2017 Mario Blättermann <mario.blaettermann@gmail.com> - 1.3.4-1
- New upstream version
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Sun Oct 09 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.3.3-1
- New upstream version
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Sun Jan 31 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.3.2-1
- New upstream version
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.1-3
- Rebuilt for GCC 5 C++11 ABI change
* Mon Mar 09 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.3.1-2
- Add German man page, summary and description
* Sat Mar 07 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.3.1-1
- Initial package
