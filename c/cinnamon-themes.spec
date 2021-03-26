Name:           cinnamon-themes
Version:        2016.05.03
Release:        2.1
Summary:        Default Cinnamon Themes
License:        GPL-3.0+
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon-themes
Source:         http://packages.linuxmint.com/pool/main/c/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch

%description
Default Cinnamon upstream themes.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_datadir}/
cp -aT .%{_datadir}/ %{buildroot}%{_datadir}/

%files
%doc debian/{changelog,copyright}
%{_datadir}/themes/*

%changelog
* Thu Aug 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2016.05.03
- Rebuild for Fedora
* Tue May  3 2016 sor.alexei@meowr.ru
- Update to version 2016.05.03:
  * Linux Mint: Switch snap OSD tint from blue to green.
* Fri Apr 22 2016 sor.alexei@meowr.ru
- Update to 2016.04.22:
  * Fix sound applet -> applications -> volume sliders.
* Fri Nov  6 2015 sor.alexei@meowr.ru
- Update to 2015.11.06:
  * Mint-X: Tweak theming for the new workspace and sound applets.
* Tue Oct 27 2015 sor.alexei@meowr.ru
- Update to 2015.10.21:
  * Reduced opacity of Alt-tab preview backdrop to 65%%.
  * Mint-X: Rework styling of check and radio buttons.
  * Linux Mint: Tweak the look of modal dialogs.
  * Linux Mint: Add some theming for the new workspace switcher.
  * Linux Mint: Clean up the styling of check and radio buttons.
* Sun Oct 18 2015 sor.alexei@meowr.ru
- Update to 2015.06.14:
  * Fix file permissions.
  * Add theming for the about dialog box to all themes.
  * Add a bit of padding around the workspace switcher.
  * Remove now unused selectors for Cinnamon looking glass.
  * Remove unused .hotplug-* selectors.
  * Fixed OSD look in Linux Mint theme (it looked more like the
    Cinnamon theme lately).
- Correct license.
* Tue Jun  2 2015 stefan@fam-elser.de
- update to version 0.0.0~git20150603
* Thu Apr 23 2015 stefan@fam-elser.de
- update to version 0.0.0~git20141118
* Wed Nov  5 2014 i@marguerite.su
- update version 0.0.0~git20141104
* Mon Jun  2 2014 stefan@fam-elser.de
- initial release
