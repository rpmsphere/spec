%undefine _debugsource_packages
Name:           djvusmooth
Version:        0.2.19
Release:        3.1
License:        GPL-2.0
Summary:        Graphical Text Editor for DjVu
URL:            https://jwilk.net/software/djvusmooth
Group:          Productivity/Publishing/Other
Source0:        https://pypi.python.org/packages/source/d/%{name}/%{name}-%{version}.tar.gz
Source1:        djvusmooth.png
BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
#BuildRequires:  python2-djvulibre
BuildArch:      noarch

%description
DjVuSmooth is a graphical text editor for DjVu documents.

%prep
%setup -q

%build

%install
# Replace desktop file. Provided one isn't good enough.
cat > extra/%{name}.desktop << EOF
[Desktop Entry]
Name=DjVuSmooth
GenericName=Graphical Text Editor for DjVu
GenericName[pl]=Graficzny edytor plików DjVu
GenericName[ru]=Текстовый редактор DjVu-книг
Comment=Graphical Text Editor for DjVu
Comment[pl]=Graficzny edytor plików DjVu
Comment[ru]=Граффический текстовый редактор для DjVu-книг
Type=Application
Exec=djvusmooth %f
Icon=djvusmooth
Categories=Utility;TextEditor;
StartupNotify=true
Terminal=false
MimeType=image/x-djvu;image/x.djvu;image/vnd.djvu;
EOF

python2 setup.py install \
    --root=%{buildroot} \
    --prefix=%{_prefix}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
    
install -Dm 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%files -f %name.lang
%doc doc/COPYING doc/changelog doc/credits.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%doc %{_mandir}/man?/*
%{python2_sitelib}/djvusmooth*

%changelog
* Wed Apr 11 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.19
- Rebuilt for Fedora
* Sat Jun 16 2012 lazy.kent@opensuse.org
- Update to 0.2.12.
  * Rename menu item “Edit → Outline → Remove” to “… → Remove all”.
  * Use our own minimal XDG Base Directory implementation instead
    of PyXDG.
  * Add Spanish translation.
  * Update Russian translation.
- Doesn't require fdupes.
* Mon Feb 27 2012 lazy.kent@opensuse.org
- Split off lang package.
- Install icon to icons/hicolor.
- Remove check for unsupported openSUSE versions.
* Thu Jan 26 2012 lazy.kent@opensuse.org
- Update to 0.2.11.
  * Don't throw exceptions when using "Fit width", "Fit height" and
    "Stretch" zoom factors and no page is shown.
  * Fix a typo in the manual page.
  * Let the setup.py script build and install binary message
    catalogs.
* Sun Nov  6 2011 lazy.kent@opensuse.org
- Corrected dependencies (python-distribute for openSUSE >= 1210).
- Added desktop_database_post/un macros
- Corrected License tag.
- Use full URL as a source.
- spec clean up.
* Sat Feb 19 2011 lazy.kent@opensuse.org
- Update to 0.2.10.
  * Let the setup.py script build and install manual pages.
  * Fix the code that was supposed to disable the GUI while an
    external editor is running.
  * Fix the manual page: djvusmooth uses XDG_CONFIG_HOME rather
    than XDG_DATA_HOME.
- added COPYING
* Tue Jan 25 2011 lazy.kent@opensuse.org
- Update to 0.2.9.
  * Fix support for external editors that use the
    overwrite-by-rename technique.
- Requires python-wxWidgets for openSUSE 11.4
* Tue Aug 31 2010 lazy.kent.suse@gmail.com
- Update to 0.2.8.
  * Update the Russian translation.
  * Handle directories with non-ASCII characters (deb#595002).
  * Fix editing line/arrow annotations (deb#595012).
* Sat Jun 26 2010 lazy.kent.suse@gmail.com
- Update to 0.2.7.
  * Add Russian translation.
  * Handle non-ASCII metadata keys.
- Dropped translation patch (included upstream).
* Sun Jun 20 2010 lazy.kent.suse@gmail.com
- Added Russian translation.
* Tue Jun 15 2010 lazy.kent.suse@gmail.com
- Update to 0.2.6.
  * Add keyboard shortcut Ctrl+G for “Go to page…”.
  * Reopen document after save, so that it's possible to display
    non-cached pages.
- Dropped obsolete keyboard shortcut patch (fixed upstream).
* Wed Jun  9 2010 lazy.kent.suse@gmail.com
- Added keyboard shortcut for "Go to page…" action.
- Moved desktop menu entry to Utility/TextEditor.
* Fri Apr  9 2010 lazy.kent.suse@gmail.com
- Update to 0.2.5.
  * Fix setup.py to install all the required packages.
- Dropped setup patch (fixed upstream).
* Thu Apr  8 2010 lazy.kent.suse@gmail.com
- Fixed setup script.
- Added icon.
* Tue Apr  6 2010 lazy.kent.suse@gmail.com
- Initial package created - 0.2.4.
