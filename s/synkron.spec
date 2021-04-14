Name:           synkron
Version:        1.6.2
Release:        6.1
Summary:        An Open Source Folder Synchroniser
License:        GPLv2+
URL:            http://synkron.sourceforge.net/
Group:          Productivity/Archiving/Backup
Source0:        Synkron-%{version}-src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ qt4-devel

%description
Synkron is an application for folder synchronisation that allows you to
configure your synchronisations in detail. Despite having many features, the
user interface of Synkron is very user-friendly and easy to use.

Synkron is able to synchronise multiple folders at once, analyse folders before
sync, restore overwritten or deleted files, plan synchronisations and much
more.

%prep
%setup -q -n Synkron-%{version}-src
# Fix rpmlint warning about "wrong-file-end-of-line-encoding"
sed -i 's/\r//' readme.txt

%build
lrelease-qt4 Synkron.pro
qmake-qt4 QMAKE_CXXFLAGS+="%{optflags}" -config release Synkron.pro
make %{?_smp_mflags}

%install
install -Dm 0755 synkron $RPM_BUILD_ROOT%{_bindir}/synkron
install -Dm 0644 images/Synkron16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/synkron.png
install -Dm 0644 images/Synkron48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/synkron.png
install -Dm 0644 images/Synkron128.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/synkron.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc gpl.txt readme.txt
%{_bindir}/synkron
%{_datadir}/icons/hicolor/*x*/apps/synkron.png

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.2
- Rebuilt for Fedora
* Tue Feb 15 2011 asterios.dramis@gmail.com
- Update to version 1.6.2:
  * added Romanian translation
  * fixed a bug that caused deleting of files when a device was disconnected
    during sync
  * added an option to ignore 1 hour time differences - solves daylight saving
    time issues
  * several bug fixes
- Spec file updates:
  * Minor fixes.
  * Changed License: to GPLv2+.
  * Updated Group: and BuildRequires: sections.
  * Fix Categories: entry of synkron.desktop file.
* Thu Jan 13 2011 bitshuffler@opensuse.org
- Fix build & cleanup spec.
* Mon Jan 10 2011 asterios.dramis@gmail.com
- Initial release (version 1.6.1)
