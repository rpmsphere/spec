%global debug_package %{nil}

Name:       sigram
Summary:    Sigram Telegram Client
Version:    0.7.1
Release:    19.1
Group:      System/GUI/Other
License:    GPL
URL:        https://github.com/sialan-labs/sigram.git
Source0:    %{name}-master.zip
BuildRequires: compat-openssl10-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: unzip
#BuildRequires: qt5-qtgraphicaleffects-devel
#BuildRequires: qt5-qtquickcontrols-devel

%description
Telegram Client for Linux written in QT5.

%prep
%setup -q -n %{name}-master
sed -i '1i #include <QDataStream>' Sigram/qtsingleapplication/qtlocalpeer.cpp
sed -i '1i #include <QObject>\n#include <QMetaType>' Sigram/telegram/strcuts.h

%build
qmake-qt5 . QMAKE_CXXFLAGS+="-Wno-narrowing" LIBS+="-Wl,--allow-multiple-definition"
make %{?_snmp_mflags} 

%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install

%files
%{_bindir}/*
%doc GPL.txt license.txt LICENSE README.md
%{_datadir}/sigram
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%clean
rm -rf %{buildroot}

%changelog
* Thu Jun 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.1
- Rebuild for Fedora
* Thu Jun 19 2014 Markus Dorfer
- use of %doc variable
- optimized build with sed
* Mon Jun 16 2014 Markus Dorfer
- update to version 0.5.5.2
- rpm file path cleanup no /opt anymore
* Sat Jun 14 2014 Markus Dorfer
- update version 0.5.5.1
- optimizations in the spec file
