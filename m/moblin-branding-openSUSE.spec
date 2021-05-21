Name:           moblin-branding-openSUSE
Summary:        The openSUSE background for Moblin
Group:          System/GUI/Other
Version:        0.3
Release:        4.2
License:        BSD3c
URL:            http://www.moblin.org
BuildRequires:  ImageMagick
BuildRequires:  plymouth
Source0:        bubbles.png
Source1:        thumb-selected-template.png
Source2:        thumb-unselected-template.png
Source3:        LICENSE
Source4:	SmeegolStripesWhite.png
Source5:	SmeegolStripesBlack.png
BuildArch:      noarch
Summary:        The openSUSE background for Moblin
Group:          System/GUI/Other
Provides:       moblin-branding
Conflicts:      otherproviders(moblin-branding)

%description
The openSUSE specific branding package for Moblin

Image created by Jackub Steiner, "Bubbles with Logo" Found on
Flickr http://www.flickr.com/photos/forcev/3842096407/in/set-72157618908491290/

%prep

%build
convert -resize 1024x600! -format "png" %{SOURCE0} splash-vendor.png
convert -resize 198x115! -format "png" %{SOURCE0} - | composite -gravity Center -geometry -0-1 - %{SOURCE1} thumb-selected-vendor.png
convert -resize 198x115! -format "png" %{SOURCE0} - | composite -gravity Center -geometry -0-1 - %{SOURCE2} thumb-unselected-vendor.png

%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}
%{__mkdir_p} %{buildroot}/%{_datadir}/plymouth
%{__mkdir_p} %{buildroot}/%{_datadir}/mutter-moblin/theme/chooser
%{__mkdir_p} %{buildroot}/%{_datadir}/mutter-moblin/theme/panel
mkdir -p %{buildroot}%{_datadir}/backgrounds/images/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/backgrounds/images/SmeegolStripesWhite.png
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/backgrounds/images/SmeegolStripesBlack.png
install -m 0644 splash-vendor.png %{buildroot}/%{_datadir}/plymouth
install -m 0644 thumb-selected-vendor.png %{buildroot}/%{_datadir}/mutter-moblin/theme/chooser
install -m 0644 thumb-unselected-vendor.png %{buildroot}/%{_datadir}/mutter-moblin/theme/chooser
ln -sf %{_datadir}/plymouth/splash-vendor.png %{buildroot}/%{_datadir}/mutter-moblin/theme/panel/background-tile-vendor.png

%files
%defattr(-,root,root,-)
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/*
%dir %{_datadir}/mutter-moblin
%{_datadir}/mutter-moblin/*
%{_datadir}/backgrounds/images/SmeegolStripesWhite.png
%{_datadir}/backgrounds/images/SmeegolStripesBlack.png

%clean
rm -rf %{buildroot}


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Mon Oct 18 2010 awafaa@opensuse.org
- Add Smeegol wallpaper - in both white & black
* Mon Jul 26 2010 awafaa@opensuse.org
- Update wallpaper to slicker looking bubbles
* Fri Apr 23 2010 aj@suse.de
- Conflict with other providers of branding.
- Package is noarch.
* Fri Apr 23 2010 awafaa@opensuse.org
- Rename .spec & .changes to moblin-branding-openSUSE to comply
  with naming policy
- Change license to BSD3c and added LICENSE file
* Mon Mar 29 2010 awafaa@opensuse.org
- Rename package to moblin-branding-openSUSE to comply with
  naming policy.
* Thu Oct 29 2009 jimmac@novell.com
- updated wallpapers specifically for SUSE edition of Moblin
* Thu Jun  4 2009 awafaa@opensuse.org
- change image to Goblin
* Thu May 14 2009 gregkh@suse.de
- created package
