%define theme_name Sonar

Summary: %{theme_name} icon theme
Name: sonar-icon-theme
Version: 11.3.1
Release: 8.1
License: GPL2+
Group: User Interface/Desktops
Source: icon-theme-sonar-%{version}.tar.bz2
BuildRequires: icon-naming-utils
BuildArch: noarch

%description
OpenSUSE Sonar icon theme based on the upcoming GNOME icon theme.

%prep
%setup -q -n icon-theme-sonar-%{version}

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
sed -i 's|Example=user-home|Example=folder|' $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog AUTHORS NEWS README COPYING
%{_datadir}/icons/%{theme_name}

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 11.3.1
- Rebuild for Fedora
* Fri Mar  1 2013 dimstar@opensuse.org
- Spec-cleanup using format_spec_file service.
* Tue Jan 18 2011 vuntz@opensuse.org
- Remove the gtk3-metatheme-sonar subpackage (and all references to
  it in various Suggests): we can't build it this way anymore,
  since theming in GTK+ 3 changed and the format is different. We
  might create a gtk3-metatheme-sonar package again later, but with
  a working GTK+ 3 theme.
* Tue Jan 11 2011 vuntz@opensuse.org
- Add gtk2-metatheme-sonar-main-menu-theming.patch: correctly match
  the main menu button for theming. With the relevant change in
  gnome-main-menu, this fixes bnc#642956.
* Thu Oct 14 2010 vuntz@opensuse.org
- Create a theme for gtk3 too:
  + copy gtk-2.0 theme directory as gtk-3.0, it should just work.
  + create a gtk3-metatheme-sonar subpackage.
  + split the common files between gtk2-metatheme-sonar and
    gtk3-metatheme-sonar in metatheme-sonar-common. This subpackage
    is required by both gtk2-metatheme-sonar and
    gtk3-metatheme-sonar. It also has a sonar-icon-theme
    Recommends, and Suggests for both gtk2-metatheme-sonar and
    gtk3-metatheme-sonar.
  + change gtk2-metatheme-sonar Recommends in sonar-icon-theme to a
    Suggests, and add a gtk3-metatheme-sonar Suggests too.
  + remove gtk2 Requires for gtk2-metatheme-sonar:
    gtk2-engine-murrine will already bring gtk2.
* Thu Sep 23 2010 badshah400@gmail.com
- Add metatheme-Sonar_compatibilty-with-murrine-0.98.patch to
  remove options deprecated in murrine 0.98, that create warnings.
* Wed Aug 25 2010 vuntz@opensuse.org
- Add hicolor-icon-theme BuildRequires.
- Use the %%icon_theme_cache_* macros to make sure the icon theme
  cache is created/updated.
* Sat Aug  7 2010 vuntz@opensuse.org
- Drop icon-theme-gilouche.patch: the size of the icon theme is now
  reduced, so we don't need this anymore.
- Change sonar-icon-theme Suggests to Recommends: the sonar icon
  theme is the one that is recommended by the theme, and this will
  make it easier to have it installed by default.
* Wed Jun 30 2010 vuntz@opensuse.org
- Update sonar-icon-theme to 11.3.1: this version removes many
  icons that are now part of gnome-icon-theme (since 2.30.0).
* Thu Jun 24 2010 psankar@opensuse.org
- Change recommended icon theme to Gilouche in the metatheme file,
  as 11.3 does not ship sonar-icon-theme by default because of size
  constraints.
* Thu May 13 2010 jimmac@novell.com
- metatheme 11.3.0 - use Sonar icon theme again
- icon theme 11.3.0 - add 24x24px size for volume icons. bug #602871
* Tue Dec  1 2009 dimstar@opensuse.org
- Update to version 11.2.10:
  + Sonar icon theme too big and too late, reverting to Gilouche
* Wed Nov 18 2009 jimmac@novell.com
- update icon theme to 11.2.5:
  + improved the styling of the XDG folders. Changed user-desktop
    to be consistent.
* Mon Nov 16 2009 jimmac@novell.com
- update icon theme to 11.2.4:
  + restyled and expanded coverage of XDG folders.
* Thu Nov 12 2009 jimmac@novell.com
- update icon theme to 11.2.3:
  + network manager signal strengt icons ate 16x16, 22x22, 32x32
    and 48x48.
* Tue Oct 20 2009 vuntz@opensuse.org
- Update gtk theme to 11.2.9:
  + enlarge bottom border to allow easier sizing in compiz.
    bnc#544586
  + brasero notifications
  + insensitive menu entries
  + work around gtkcombobox issues with gdm. bnc#544079
- Drop gtk2-metatheme-sonar-greeter-panel.patch: fixed with the new
  tarball.
- Update icon-theme-sonar to 11.2.2: this is a different theme,
  which is not based on the GNOME colors icon theme anymore.
- Add icon-naming-utils and pkg-config BuildRequires, needed by the
  new theme.
- Version sonar-icon-theme according to the tarball version of the
  icon theme, not according to the version of the gtk+ theme.
* Mon Oct 19 2009 dimstar@opensuse.org
- Add gtk2-metatheme-sonar-greeter-panel.patch by Mingxi Wu to fix
  panel colors in gdm greeter. Fixes bnc#544079.
* Mon Sep 28 2009 dimstar@opensuse.org
- Update to version 11.2.5:
  + bnc#508196 - fix slab icon clipping
- Changes from version 11.2.4:
  + remove duplicate roundness
  + bnc#538835 - make gdm panel dark as well
- Drop bnc508196-fix-main-menu-icon-size.patch, included upstream.
* Mon Sep 14 2009 mxwu@novell.com
- Add bnc508196-fix-main-menu-icon-size.patch. Fix bnc#508196
* Wed Sep  9 2009 vuntz@opensuse.org
- Update to version 11.2.3:
  + better contrast for disable menu items (bnc#533320)
  + better contrast for unfocudes window title and icons
* Mon Aug 17 2009 vuntz@novell.com
- Update to version 11.2.2:
  + less whitespace in the titlebar (bnc#520020)
  + special case a broken panel applet (bnc#528786)
* Mon Aug  3 2009 vuntz@novell.com
- Update to new upstream tarball (which has the same version
  number, unfortunately).
* Wed May  6 2009 vuntz@novell.com
- Rename package to gtk2-metatheme-sonar, since it's a metatheme.
- Merge icon-theme-sonar package in this source package, but still
  create a sonar-icon-theme package.
- Make sure the files are not writable or executable: they're all
  data files.
* Tue May  5 2009 abockover@novell.com
- Initial import of Sonar for openSUSE 11.2 inclusion
