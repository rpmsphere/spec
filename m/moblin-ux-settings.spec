Name:           moblin-ux-settings
Version:        0.39
Release:        3.1
Summary:        Package to setup the environment and schemas

Group:          Desktop/Interface
License:        LGPLv2.1
URL:            http://www.moblin.org
BuildArch:      noarch
Source0:        README
Source1:        %gconf-tree.xml
Source2:        air-environment.sh
BuildRequires: GConf2
BuildRequires: libxml2


%description
Package to install Netbook schemas and stuff.

%prep

%build
%install
cp %{SOURCE0} .
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.moblin
sed -i 's/meego-background/SmeegolStripesWhite/g' %{SOURCE1} 
xmllint  %{SOURCE1} && install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.moblin 
install -d $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

%files
%defattr(-, root, root)
%{_sysconfdir}/gconf/gconf.xml.moblin/%gconf-tree.xml
%{_sysconfdir}/profile.d/air-environment.sh
%doc README

%clean
rm -rf %{buildroot}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Mon Oct 18 2010 awafaa@opensuse.org
- Use SmeegolStripesWhite.png as the background instead of MeeGo
  artwork
* Thu Oct 14 2010 vincent.lejeune@scilab.org
- Changed meego-background.png to goblin-background.png
* Wed Jun 16 2010 dimstar@opensuse.org
- Fix filelist by adding %%defattr(-, root, root)
* Thu Jun 10 2010 awafaa@opensuse.org
- Update to version 0.34
* Thu Nov 19 2009 abockover@novell.com
- No longer require xulrunner
* Thu Sep  3 2009 sragavan@novell.com
- Make Anjal the mailto url handler.
* Wed Sep  2 2009 michael.meeks@novell.com
- make packagekit auto-update everything by default.
* Sat Aug 15 2009 abockover@novell.com
- Disabled Mojito test accounts
