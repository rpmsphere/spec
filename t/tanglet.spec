Name:           tanglet
Version:        1.5.6
Release:        1
Summary:        Word finding game
License:        GPLv3+
URL:            http://gottcode.org/%{name}/
Source:         http://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qttools-devel
BuildRequires:  zlib-devel
Requires:       %{name}-data = %{version}-%{release}

%description
A single player word finding game based on Boggle. The object of the game is
to list as many words as you can before the time runs out. There are several
timer modes that determine how much time you start with, and if you get extra
time when you find a word.

You can join letters horizontally, vertically, or diagonally in any direction
to make a word, so as long as the letters are next to each other on the board.
However, you can not reuse the same letter cells in a single word. Also, each
word must be at least three letters on a normal board, and four letters on a
large board.

%package data
Summary:        Shared files for %{name}
BuildArch:      noarch
Requires:       hicolor-icon-theme
 
%description data
This package contains arch-independent files for %{name}.

%prep
%setup -q
#sed -i '58,65d' tools/dice/main.cpp

%build
%{qmake_qt5} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man6/
install -p -m 644 doc/%{name}.6 %{buildroot}%{_mandir}/man6/

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop || :
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml || :

%post data
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun data
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans data
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc CREDITS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man6/%{name}.6.*

%files data
%license COPYING
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.6
- Rebuild for Fedora
* Tue Nov 07 2017 Mario Blättermann <mario.blaettermann@gmail.com> - 1.5.0-1
- New upstream version
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Sun Oct 09 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.4.0-1
- New upstream version
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.1-3
- Rebuilt for GCC 5 C++11 ABI change
* Sat Feb 07 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.3.1-2
- Fix issues according to review (bz1190060)
* Thu Feb 05 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.3.1-1
- New upstream release (switch to Qt5)
- Spec file cleanup
- Create -data subpackage
* Wed Sep 25 2013 Huaren Zhong <huaren.zhong@gmail.com> - 1.2.1
- Rebuild for Fedora
* Wed Feb 01 2012 graeme@gottcode.org 1.2.1-1
- New upstream release
* Mon Dec 05 2011 graeme@gottcode.org 1.2.0-4
- Update GNOME icon cache
* Fri Nov 11 2011 graeme@gottcode.org 1.2.0-3
- Improve spec file
* Sat Oct 29 2011 graeme@gottcode.org 1.2.0-2
- Remove patch
* Sat Oct 29 2011 graeme@gottcode.org 1.2.0-1
- New upstream release
* Sat Apr 02 2011 graeme@gottcode.org 1.1.1-3
- Add dependency on hicolor-icon-theme
* Wed Sep 22 2010 graeme@gottcode.org 1.1.1-2
- Fixed build issue on openSUSE 11.2
* Tue Sep 21 2010 graeme@gottcode.org 1.1.1-1
- Initial package
