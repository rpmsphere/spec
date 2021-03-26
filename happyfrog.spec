%global debug_package %{nil}
%global _name HappyFrog

Name:           happyfrog
Version:        0.0.4
Release:        14.4
Summary:        Qt4 Funny Game
License:        LGPLv3
URL:            https://www.linux-apps.com/p/1132414/
# https://gitorious.org/happyfrog/happyfrog
Source0:        Happyfrog-Src-%{version}.tar.bz2
Source1:        HappyFrog.pro
BuildRequires:  qt-mobility-devel
BuildRequires:  Box2D-devel

%description
HappyFrog is a funny game which is based on Qt and Box2D (mainly,Declarative
UI integrated with Box2D).Maybe It reminds you of \"Angry bird\". The most
interesting thing you can find in the game is that you can customize the level
and edit your own fixture world.And of course,you can save the fixture world
and play it next time.

%prep
%setup -q -n HappyFrog
cp %{SOURCE1} .
sed -i 's|/usr/local|/usr|' deployment.pri
sed -i '161s|,true||' slingshot.cpp
sed -i '93s|p);|p, true);|' frog.cpp
sed -i '516s|vec2);|vec2, true);|' fixture.cpp

%build
qmake-qt4
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=%{buildroot}

%files
%doc changelog LICENSE ReadMe.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{_name}.png

%changelog
* Wed Aug 17 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.4
- Rebuild for Fedora
