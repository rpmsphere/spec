Name:		oxstore-menus
Version:	2.0
Release:	3
Summary:	OxStore Menus for the Desktop
Group:		User Interface/Desktops
License:	MIT
URL:		http://oxstore.linux.org.tw/
Source0:	%{name}-%{version}-ox.tgz
BuildArch:	noarch
Requires:	redhat-menus hicolor-icon-theme

%description
This Package adds OxStore menus to the xdg menu structure.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
install -pm 0644 *.menu $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
install -d $RPM_BUILD_ROOT%{_datadir}/desktop-directories
install -pm 0644 *.directory $RPM_BUILD_ROOT%{_datadir}/desktop-directories
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/categories
install -pm 0644 *.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/categories

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
        %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
ln -sf applications-merged %{_sysconfdir}/xdg/menus/applications-gnome-merged

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
        %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/menus/applications-merged/*.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/hicolor/128x128/categories/*.png

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Wed Jun 20 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0-3
- Add link to applications-gnome-merged

* Fri Jun 24 2011 David Hung <david.hung@ossii.com.tw> - 2.0-2
- Modify the filename eApps->eBookapps

* Tue Jan 18 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0-1
- Add eApps, simplified eBook and eCourse

* Mon Nov 15 2010 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2-1
- Minor fix

* Wed Mar 24 2010 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0-1
- Initial package for OSSII
