Name:           koceansaver
Version:        0.8
Release:        3
Summary:        An under water screen saver for KDE4
License:        GPLv2
Group:          Graphics/Utilities
URL:            http://sourceforge.net/projects/koceansaver/
Source0:        http://freefr.dl.sourceforge.net/project/%{name}/%{name}/KOceanSaver-%{version}.tar.gz
BuildRequires:  kde-workspace-devel qca2 udisks2

%description
A KDE 4 screensaver that shows an underwater ocean seen   
with sea creatures. In particular, swimming Baracudas and 
sharks. A treasure chest lies on the sea floor with a ship
wrecked in the background.

%prep
%setup -q -n KOceanSaver
sed -i '/KSCREENSAVER/d' CMakeLists.txt
sed -i '/kscreensaver/d' src/kocean.h

%build
%cmake
make

%install
%make_install

%files
%doc AUTHORS ChangeLog
%{_bindir}/%{name}.kss
%{_datadir}/kde4/services/ScreenSavers/koceansaver.desktop
%{_datadir}/kde4/apps/%{name}
%{_mandir}/man1/%{name}.kss.1.*

%changelog
* Thu Feb 26 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 0.8-3.mga5
+ Revision: 745169
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.8-2.mga5
+ Revision: 681148
- Mageia 5 Mass Rebuild
* Tue Nov 12 2013 dglent <dglent> 0.8-1.mga4
+ Revision: 550663
- Cosmetic changes (tabs and whitespaces)
- imported package koceansaver
