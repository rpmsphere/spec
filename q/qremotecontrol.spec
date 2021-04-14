Name:           qremotecontrol
Version:        2.4.1
Release:        3.1
Summary:        Remote control your desktop from your mobile
License:        GPLv3
Group:          Networking/Other
URL:            http://qremote.org
Source0:        http://downloads.sourceforge.net/project/qrc/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt3Support)
BuildRequires:  pkgconfig(xtst)

%description
With QRemoteControl installed on your desktop you can easily control
your computer via WiFi from your mobile. By using the touch pad of your
Phone you can for example open the internet browser and navigate to
the pages you want to visit, use the music player or your media center
without being next to your PC or laptop. Summarizing QRemoteControl
allows you to do almost everything you would be able to do with a
mouse and a keyboard, but from a greater distance. To make these
replacements possible QRemoteControl offers you a touch pad, a
keyboard, multimedia keys and buttons for starting applications. Even
powering on the computer via Wake On Lan is supported.

%prep
%setup -q

%build
%qmake_qt4
make

%install
make install INSTALL_ROOT=%{buildroot}

%files
%doc README
%{_bindir}/qremotecontrol-server
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Tue May 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.1
- Rebuilt for Fedora
* Tue Feb 16 2016 umeabot <umeabot> 2.4.1-2.mga6
+ Revision: 962514
- Mageia 6 Mass Rebuild
* Tue Jul 28 2015 eatdirt <eatdirt> 2.4.1-1.mga6
+ Revision: 858711
- imported package qremotecontrol
* Tue Jul 28 2015 Chris Ringeval <eatdirt@mageia.com> 2.4.1-1.mga6
- Importing package qremotecontrol
