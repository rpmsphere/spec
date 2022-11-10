%undefine _debugsource_packages

Name:           dvd-vr
Version:        0.9.7
Release:        1
Summary:        Utility to identify and optionally copy recordings from DVD-VR
License:        GPLv2
URL:            https://www.pixelbeat.org/programs/dvd-vr/
Source0:        %{name}-%{version}.tar.gz
#BuildRequires:  
#Requires:       

%description
dvd-vr is a utility to identify and optionally copy recordings
from a DVD-VR format disc, which can be created by devices like
DVD recorders and camcorders.

%prep
%autosetup
sed -i 's|/usr/local|/usr|' Makefile

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license COPYING
%doc NEWS README THANKS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.7
- Rebuilt for Fedora
