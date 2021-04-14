Name:           gutenbrowser
Version:        0.9.0cvs.20090725
Release:        14.1
Summary:        Ebook Reader for Gutenberg Etexts
License:        GPL-2.0
Group:          Productivity/Publishing/Other
URL:            http://sourceforge.net/projects/gutenbrowser/
# cvs -z3 -d:pserver:anonymous@gutenbrowser.cvs.sourceforge.net:/cvsroot/gutenbrowser co -P gutenbrowser; cd gutenbrowser/; find . -name CVS -type d | xargs rm -rf; tar jcf gutenbrowser-0.9.0cvs.20090725.tar.bz2 gutenbrowser/
Source0:        %{name}-%{version}.tar.bz2
Source1:        gutenbrowser.desktop
Source2:        http://osdab.googlecode.com/files/OSDaB-Zip-20120404.tar.bz2
# PATCH-FIX-OPENSUSE no-copy-dt-needed-entries.patch asterios.dramis@gmail.com -- Fix linking with --no-copy-dt-needed-entries
Patch0:         no-copy-dt-needed-entries.patch
# PATCH-FIX-OPENSUSE compile_with_new_OSDaB-Zip.patch asterios.dramis@gmail.com -- Fix compilation with newer version of zip class from OSDaB Project
Patch1:         compile_with_new_OSDaB-Zip.patch
# PATCH-FIX-OPENSUSE use_system_zlib.patch asterios.dramis@gmail.com -- Use system zlib
Patch2:         use_system_zlib.patch
BuildRequires:  desktop-file-utils
BuildRequires:  qtwebkit-devel
BuildRequires:  qt-devel

%description
Gutenbrowser is an application to easily search, download and read free classic
literature, in the form of electronic etexts republished electronically by the
Project Gutenberg (http://www.gutenberg.org/).

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

# Replace the zip class from OSDaB Project with a newer one (the existing one doesn't work)
rm -rf zip/
tar jxf %{SOURCE2}
mv OSDaB-Zip zip

%patch2 -p1

# Make sure the system zlib is used
rm -rf zlib/

sed -i 's|return false;|return NULL;|' gutendb.cpp

%build
qmake-qt4 QMAKE_CXXFLAGS+="%{optflags} -Wno-format-security" -config release gutenbrowser.pro

make %{?_smp_mflags}

%install
install -Dpm 0755 gutenbrowser %{buildroot}%{_bindir}/gutenbrowser
install -Dpm 0644 images/gutenbrowser.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gutenbrowser.png

# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc README
%{_bindir}/gutenbrowser
%{_datadir}/applications/gutenbrowser.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/64x64/apps
%{_datadir}/icons/hicolor/64x64/apps/gutenbrowser.png

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
* Wed Aug 29 2012 asterios.dramis@gmail.com
- Initial release (version 0.9.0cvs.20090725).
- Added a desktop file for the application.
- Replaced the zip class from OSDaB Project with a newer one
  (OSDaB-Zip-20120404) since the older one didn't work.
- Added the following patches:
  * no-copy-dt-needed-entries.patch:
    Fix linking with --no-copy-dt-needed-entries.
  * compile_with_new_OSDaB-Zip.patch:
    Fix compilation with newer version of zip class from OSDaB Project.
  * use_system_zlib.patch:
    Use system zlib.
