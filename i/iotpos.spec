Name:     iotpos
Version:  0.9.4git
Release:  11.1
Summary:  An open source Point of Sale software
Group:    Productivity/Office
License:  GPLv2
URL:      https://github.com/hiramvillarreal/iotpos
Source0:  %{name}-master.zip
BuildRequires: kdelibs-devel
Requires: mariadb-server
Requires: qt-mysql

%description
Welcome to IotPOS  an open source Point of Sale software, is targeted for micro,
small and medium businesses. This Point of Sale was modified to work with single-
board computers (SBC) as the Raspberry pi, banana pi and BeagleBone Black by
making use of the GPIO interface, giving options and Internet of Things functions
not possible with common laptops and PCs.

IotPos and IotStock are derived from LemonPOS, to his author: Miguel Chavez Gamboa,
and collaborators; all my respects.

%prep
%setup -q -n %{name}-master

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make

%install
cd build
%make_install

%post
cat %{_datadir}/kde4/apps/%{name}/iotpos_mysql.sql | mysql -u root -p ||:

%files
%doc CHANGELOG COPYING LICENSE NOTES README USING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/config.kcfg/*
%{_datadir}/config/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/kde4/apps/*
%{_datadir}/locale/*/LC_MESSAGES/*

%changelog
* Wed Sep 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4git
- Rebuild for Fedora
