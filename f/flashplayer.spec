%global debug_package %{nil}

Name:           flashplayer
Version:        26.0.0.131
Release:        1.bin
Summary:        Adobe Flash Plugin and Standalone Player
License:        see license.pdf
Group:          Productivity/Networking/Web/Browsers
URL:            https://get.adobe.com/flashplayer
Source0:        flash_player_sa_%{version}_linux.x86_64.tar.gz
Source1:        flashplayer.desktop
Source2:        flashplayer.png
Requires:       alsa-lib
Requires:       libcurl

%description
This package contains Adobe's standalone flash player application.

%prep
%setup -q -c

%build

%install
install -Dpm 0755 flashplayer %{buildroot}%{_bindir}/flashplayer
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/flashplayer.desktop
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/flashplayer.png

%files
%doc LGPL/* license.pdf
%{_bindir}/flashplayer
%{_datadir}/applications/flashplayer.desktop
%{_datadir}/pixmaps/flashplayer.png

%changelog
* Mon Jul 10 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 26.0.0.131
- Initial binary package
