Name: lucidor
Version: 0.9.1
Release: 1
Summary: E-book reader application
Group: Applications/Publishing
License: GPLv3+
URL: http://lucidor.org/lucidor/
Source0: http://lucidor.org/lucidor/%{name}_%{version}.tar.gz
BuildArch: noarch
Requires: xulrunner

%description
Lucidor is an e-book reader application. It supports e-books
in the EPUB file format, and catalogs in the OPDS format.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make install install-man install-mime DESTDIR=%{buildroot}
echo -e 'Name[zh_TW]=清澈者閱讀器\nComment[zh_TW]=Lucidor 電子書閱讀程式' >> %{buildroot}%{_datadir}/applications/lucidor.desktop

%clean
rm -rf %{buildroot}

%post
update-desktop-database %{_datadir}/applications &> /dev/null || :
#/usr/sbin/update-icon-caches %{_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :
/usr/sbin/update-mime &> /dev/null || :

%postun
update-desktop-database %{_datadir}/applications &> /dev/null || :
#/usr/sbin/update-icon-caches %{_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :
/usr/sbin/update-mime &> /dev/null || :

%files
%{_bindir}/lucidor
%{_datadir}/lucidor/
%doc credits.txt gpl-3.0.txt readme.html style.css
%doc %{_mandir}/man1/lucidor.1.gz
%{_datadir}/applications/lucidor.desktop
%{_datadir}/mime/packages/lucidor.xml
#%{_libdir}/mime/packages/lucidor
/usr/lib/mime/packages/lucidor
%{_datadir}/icons/hicolor/scalable/apps/lucidor.svg
%{_datadir}/pixmaps/lucidor.xpm

%changelog
* Mon Mar 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1
- Rebuild for Fedora
* Fri Oct 2 2009 Ordbrand <ordbrand@lucidor.org> 0.8.1-1
- Bugfix.
* Thu Sep 24 2009 Ordbrand <ordbrand@lucidor.org> 0.8-1
- Initial RPM release.
