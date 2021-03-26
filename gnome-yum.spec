Summary:         GNOME interface for YUM
Name:            gnome-yum
Version:         0.1.5
Release:         1
Group:           Applications/System
License:         GPL
Source0:         http://prdownloads.sourceforge.net/g/gn/gnome-yum/%{name}-%{version}.tar.bz2
Source1:         %{name}-0.1.5.zh_TW.po
Url:             http://gnome-yum.sourceforge.net
Requires:        usermode
BuildRequires:   GConf2-devel vte-devel gnome-vfs2-devel desktop-file-utils libgnomeui-devel

%description 
GNOME Interface for YUM

%prep
%setup -q
sed -i '160i extern char **environ;' src/gyum_utils.c
sed -i 's/ALL_LINGUAS="/ALL_LINGUAS="zh_TW /' configure
cp %{SOURCE1} po/zh_TW.po

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang gnome-yum
rm -f $RPM_BUILD_ROOT%{_bindir}/gnome-yum
cd $RPM_BUILD_ROOT%{_bindir}
ln -s consolehelper gnome-yum
for doc in ABOUT-NLS AUTHORS README COPYING INSTALL NEWS TODO ChangeLog; do
	rm -f $RPM_BUILD_ROOT%{_prefix}/doc/gnome-yum/$doc
done
echo -e 'Name[zh_TW]=套件管理介面\nComment[zh_TW]=YUM 的 GNOME 介面' >> $RPM_BUILD_ROOT%{_datadir}/applications/gnome-yum.desktop
desktop-file-install --vendor fedora --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  $RPM_BUILD_ROOT%{_datadir}/applications/gnome-yum.desktop
rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%post
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update; fi

%postun
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update; fi

%files -f gnome-yum.lang
%doc ABOUT-NLS AUTHORS README COPYING INSTALL TODO ChangeLog 
%dir %{_datadir}/pixmaps/gnome-yum
%{_datadir}/pixmaps/gnome-yum
%dir %{_datadir}/gnome/help/gnome-yum
%{_datadir}/gnome/help/gnome-yum/*
%dir %{_datadir}/omf/gnome-yum
%{_datadir}/omf/gnome-yum/*.omf
%{_datadir}/applications/*.desktop
%{_bindir}/gnome-yum
%{_sbindir}/gnome-yum
%config(noreplace) %{_sysconfdir}/pam.d/gnome-yum
%config(noreplace) %{_sysconfdir}/security/console.apps/gnome-yum
%attr(0755,root,root) %{_datadir}/gnome-yum/gyum-query.sh

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Mon May 12 2008 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.5-1.ossii
- Added traditional Chinese translation
- Rebuild for M6(CentOS5)

* Fri Nov 17 2006 András Tóth  <toth_bandi@users.sourceforge.net> - 0.1.5-1
- Added Swedish translation (thanks for Daniel Nylander)

* Sun Sep 24 2006 András Tóth  <toth_bandi@users.sourceforge.net> - 0.1.4-1
- Added User Manual (thanks for Sam S. Ganzha)
- Added Czech translation (thanks for Lukas Novotny)

* Mon Jun 5 2006 András Tóth  <toth_bandi@users.sourceforge.net> - 0.1.3-1.1
- Rebuild for fedora-extras-development: resolve broken dependencies

* Sat Jan 14 2006 András Tóth  <toth_bandi@users.sourceforge.net> - 0.1.3-1
- Fixed specfile format bugs
