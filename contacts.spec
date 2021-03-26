Name:           contacts        
Version:        0.9
Release:        1
Summary:        Contacts addressbook
Group:          Applications/Productivity
License:        GPLv2+
URL:            http://projects.o-hand.com/contacts
Source0:        http://projects.o-hand.com/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-0.9.zh_TW.po
Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2
BuildRequires:  gtk2-devel
BuildRequires:  evolution-data-server-devel >= 1.2.0
BuildRequires:  desktop-file-utils intltool gettext
BuildRequires:  libtool

%description
Contacts is a small, lightweight addressbook that uses libebook. 
This is the same library that GNOME Evolution uses, so all contact data that 
exists in your Evolution database is accessible via Contacts. Contacts features 
advanced vCard field type handling and is designed for use on hand-held 
devices, such as the Nokia 770 or the Sharp Zaurus series of PDAs.

%prep
%setup -q
echo zh_TW >> po/LINGUAS
cp %{SOURCE1} po/zh_TW.po

%build
%configure --disable-schemas-install --enable-gconf
sed -i '681,682d' Makefile
make %{?_smp_mflags} 
sed -i 's/SingleInstance/X-SingleInstance/' data/%{name}.desktop

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --vendor "" --delete-original  \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
  --add-category X-Fedora                               \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang Contacts

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
    # If the schema file has ever been renamed::
    #gconftool-2 --makefile-uninstall-rule \
    #  %{_sysconfdir}/gconf/schemas/[OLDNAME].schemas > /dev/null || :
fi

%post
umask 022
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &> /dev/null ||:

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
    killall -HUP gconfd-2 || :
fi

%postun
umask 022
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &> /dev/null ||:

%files -f Contacts.lang
%doc COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_bindir}/contacts
%{_mandir}/man1/%{name}*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuild for Fedora
* Sun Aug 03 2008 Jesse Keating <jkeating@redhat.com> - 0.9-1
- New upstream release
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8-3
- Autorebuild for GCC 4.3
* Thu Feb 14 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8-2
- Autorebuild for GCC 4.3
* Sat Dec 22 2007 Denis Leroy <denis@poolshark.org> - 0.8-1
- Update to upstream 0.8
* Fri Aug 17 2007 Denis Leroy <denis@poolshark.org> - 0.7-1
- Update to upstream 0.7
- Updated License tag
* Mon Jul 16 2007 Denis Leroy <denis@poolshark.org> - 0.6-1
- Update to 0.6, extra icons
- Fixed desktop file
* Sat Jun  2 2007 Denis Leroy <denis@poolshark.org> - 0.5-1
- Update to 0.5
- Updated dependencies
- Added icon cache and desktop database scripts
* Fri Dec 15 2006 Jesse Keating <jkeating@redhat.com> - 0.2-1
- build for 0.2
* Mon Oct 30 2006 Jesse Keating <jkeating@redhat.com> - 0.1-6.20060813svn
- rebuild for new eds
* Sun Aug 27 2006 Jesse Keating <jkeating@redhat.com> - 0.1-5.20060813svn
- rebuild
* Sun Aug 11 2006 Jesse Keating <jkeating@redhat.com> - 0.1-4.20060813svn
- Pull an SVN snapshot for e-d-s fixes (among other things)
* Fri Jun 09 2006 Jesse Keating <jkeating@redhat.com> - 0.1-2
- Bump for newer mock
- Add dist
* Thu Apr 13 2006 David Nielsen <david@lovesunix.net> - 0.1-1
- Initial import
