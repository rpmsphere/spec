Name:           hills-sddm-theme
Summary:        Hills Theme for SDDM
Version:        20151005
Release:        2.1
License:        CC-BY-SA
URL:            https://bitbucket.org/zettdaymond/sddm-hills-theme
Source0:        https://bitbucket.org/zettdaymond/sddm-hills-theme/downloads/hills-without-video-background.zip
Requires:       qt5-qtmultimedia
Requires:       sddm
BuildArch:      noarch

%description
SDDM Hills Theme is based on two themes: Maui, Numix and contains performance
fix for Intel i915 video card that removes freezes and reduces unjustified CPU
utilization (at least, on my ASUS Eee PC 1215P).

If QML works fine on your mashine, or SDDM works without freezes with any theme,
you will not feel the difference. SDDM Hills Theme also supports looped video
background.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_datadir}/sddm/themes
cp -a hills %{buildroot}%{_datadir}/sddm/themes

%files
%{_datadir}/sddm/themes/hills

%changelog
* Tue Mar 14 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 20151005
- Rebuild for Fedora
