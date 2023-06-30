Name:           keepnote
Version:        0.7.8
Release:        10.1
License:        GPL-2.0
Summary:        Note Taking and Organization
URL:            https://keepnote.org/
Group:          Productivity/Office/Organizers
Source0:        https://keepnote.org/download/%{name}-%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  python2-setuptools
#BuildRequires:  python2-libxml2
BuildRequires:  desktop-file-utils
BuildRequires:  python2
Requires:       pygtk2-libglade
Requires:       python2-libxml2
BuildArch:      noarch

%description
KeepNote is a note taking application that works on Windows, Linux, and
MacOS X. With KeepNote, you can store your class notes, TODO lists,
research notes, journal entries, paper outlines, etc in a simple
notebook hierarchy with rich-text formatting, images, and more. Using
full-text search, you can retrieve any note for later reference.

%prep
%setup -q
# Remove '/usr/bin/env' from scripts (rpmlint warnings).
sed -i '/\/usr\/bin\/env/d' %{name}/tarfile.py

%build

%install
# Don't use "record-rpm" — it records system directories.
python2 setup.py install \
    --root=$RPM_BUILD_ROOT \
    --prefix=%{_prefix}
# Remove useless suffix UTF8.
cd $RPM_BUILD_ROOT%{python2_sitelib}/%{name}/rc/locale
for dir in *.UTF8 ; do
    mv -f "${dir}" "${dir%.UTF8}"
done

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc CHANGES COPYING LICENSE README
%{_bindir}/%{name}
%{python2_sitelib}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.8
- Rebuilt for Fedora
* Fri Apr 13 2012 lazy.kent@opensuse.org
- Update to 0.7.8.
  * Faster startup and save performance.
* Sat Mar  3 2012 lazy.kent@opensuse.org
- Added build and runtime dependencies: python-pysqlite.
- Removed check for unsupported openSUSE versions.
- Removed '/usr/bin/env' from scripts (rpmlint warnings).
* Tue Jan 17 2012 lazy.kent@opensuse.org
- Update to 0.7.7.
  * Added "Paste As Quote".
  * Added creation/modification time editing.
  * Added --continue option to command-line.
  * Improved support for concurrent reading.
  * Fixed bugs.
- Removed runtime dependency on sqlite3.
- Split off languages.
- Recommends ImageMagick.
* Sun Nov 13 2011 lazy.kent@opensuse.org
- Initial package created - 0.7.6.
