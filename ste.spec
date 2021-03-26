Name:           ste
Version:        0.4.0
Release:        7.1
License:        GPL-2.0+
Summary:        Powerful Plain Text Editor
URL:            http://ste.sintegrial.com
Group:          Productivity/Text/Editors
Source0:        http://ste-editor.googlecode.com/files/%{name}-%{version}-src.7z
# PATCH-FIX-UPSTREAM ste-0.4.0-ste-uncrustify_includes.patch lazy.kent@opensuse.org -- add missing includes
Patch0:         ste-0.4.0-ste-uncrustify_includes.patch
# PATCH-FIX-UPSTREAM ste-0.4.0-gcc47.patch lazy.kent@opensuse.org -- fix compilation with GCC 4.7
Patch1:         ste-0.4.0-gcc47.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  icoutils
BuildRequires:  cxxtools-devel
BuildRequires:  p7zip
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  pkgconfig(enca)
#BuildRequires:  qscintilla-devel #don't install
Requires:       enca
Requires:       tidy
Requires:       astyle
Requires:       csstidy

%description
S.T.E. is easy-to-use and feature-rich plain text editor. It is completely
free-of-charge for everybody (licensed under GPL). S.T.E. is a multiplatform
application (runs on Windows, Linux and other platforms). Therefore, it has
the same look-and-feel everywhere.

%prep
%setup -qn %{name}-%{version}-src
%patch0
%patch1
icotool -x -o . application/ste.ico
sed -i 's/\r$//' LICENSE.GPL2
dnf -y remove qscintilla-devel ||:

%build
qmake-qt4 \
    QMAKE_CFLAGS+="%{optflags}" \
    QMAKE_CXXFLAGS+="%{optflags}" \
    QMAKE_STRIP=""
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
# Create desktop-file
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=STE
GenericName=Powerful Plain Text Editor
GenericName[ru]=Мощный текстовый редактор
Type=Application
Exec=ste %U
Icon=ste
Categories=Utility;TextEditor;Qt;
Comment=Feature-rich Plain Text Editor
Comment[ru]=Многофункциональный текстовый редактор
MimeType=text/plain;text/html;text/css;
StartupNotify=true
Terminal=false
EOF

install -Dm 0644 *_16x16x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -Dm 0644 *_32x32x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm 0644 *_48x48x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
rm -rf %{buildroot}{%{_datadir}/qt4,%{_includedir},%{_libdir}}

%files
%doc LICENSE.GPL2 LICENSE.GPL3 README
%{_bindir}/%{name}
%{_datadir}/sintegrial
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuild for Fedora
* Fri Apr 27 2012 lazy.kent@opensuse.org
- Patch to fix compilation with GCC 4.7.
- Use pkgconfig(*) as build dependencies.
- Removed check for unsupported openSUSE versions.
* Thu Nov 10 2011 lazy.kent@opensuse.org
- Corrected License tag.
- spec clean up.
* Fri Jun  3 2011 lazy.kent@opensuse.org
- Patch to add missing includes to 3rdparty/uncrustify.
- Added qmake optflags.
- Use full URL as a source.
- Added desktop_database_post/un and icon_theme_cache_post/un
  scripts.
- Don't install any qscintilla files.
- Don't install icon to pixmaps.
* Sat Nov  6 2010 lazy.kent.suse@gmail.com
- Fix directories owner.
- Add icon to pixmaps.
* Wed Nov  3 2010 lazy.kent.suse@gmail.com
- Initial package created - 0.4.0.
