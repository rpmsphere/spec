%undefine _debugsource_packages

Name:               eggwm
Version:            0.2
Release:            19.1
Summary:            Lightweight Qt Window Manager
#Source0:            https://eggwm.googlecode.com/files/eggwm-%{version}.tar.gz
Source0:            eggwm-master.zip
Source1:            eggwm.desktop
#URL:                https://code.google.com/p/eggwm/
URL:                https://github.com/xiangzhai/eggwm
Group:              System/GUI/Other
License:            GNU General Public License version 3 (GPL v3)
#BuildRequires:      qt4-devel
BuildRequires:      qt5-qtbase-devel
BuildRequires:      qt5-qtx11extras-devel
BuildRequires:      gcc-c++ make glibc-devel pkgconfig

%description
EggWM is a lightweight window manager written in Qt.

%prep
#setup -q
%setup -q -n eggwm-master
find . -type f -exec %__chmod 0644 {} \;

%build
#qmake-qt4
qmake-qt5
%__make %{?_smp_flags}

%install
make INSTALL_ROOT=%{buildroot} install
#install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/%{name}.desktop

%files
%{_bindir}/eggwm
%{_datadir}/eggwm
#{_datadir}/xsessions/%{name}.desktop

%changelog
* Mon Mar 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Sat Jun  4 2011 pascal.bleser@opensuse.org
- initial version (0.2)
