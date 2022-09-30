Name:       opensonic
Version:    0.1.4
Release:    1
License:    GPLv2+
Source0:    http://switch.dl.sourceforge.net/project/opensnc/Open%20Sonic/0.1.4/opensnc-src-0.1.4.tar.gz
Source1:    opensonic.desktop
Group:      Amusements/Games
Summary:    Game Based on the Sonic the Hedgehog Universe 
URL:        http://opensnc.sourceforge.net  
BuildRequires:  allegro-logg-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  jpgalleg-devel
BuildRequires:  libpng-devel
BuildRequires:  allegro-loadpng-devel
BuildRequires:  allegro-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ cmake

%description
Open Sonic is an open-source game based on the "Sonic the Hedgehog"
universe. It introduces a different style of gameplay called cooperative
play, in which it's possible to control 3 characters simultaneously.
Unlike most similar games, Open Sonic provides a greater level of
interaction between the player and the levels. It's more than just
a jump'n'run; the user must come up with some strategy in order to
get through the levels.

%prep
%setup -qn opensnc-src-%{version}

%build
./configure
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mv ${RPM_BUILD_ROOT}%{_datadir}/%{name}/%{name} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
desktop-file-install                                    \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  %{SOURCE1}
install -m644 icon.png ${RPM_BUILD_ROOT}%{_datadir}/%{name}/icon.png

%files 
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.4
- Rebuilt for Fedora
* Fri Oct 26 2012 Robert Wei <robert.wei@ossii.com.tw> 0.1.4-1
- install the icon file
* Sun Mar 25 2012 Minh Ngo <nlminhtl@gmail.com> 0.1.4-1
- initial build 
