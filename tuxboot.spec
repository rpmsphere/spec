%global debug_package %{nil}
Name:           tuxboot
Version:        23
Release:        1
URL:            http://tuxboot.org/
License:        GPL v2 or later
Group:          System/GUI/Other
Summary:        To create a bootable Live USB drive
Source0:        %{name}-%{version}.src.tar.gz
Source1:	%{name}.png
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
Requires:       mtools p7zip udev util-linux syslinux

%description
Tuxboot helps you to create a bootable Live USB drive for Clonezilla live,
DRBL live, GParted live and Tux2live. It is modified from UNetbootin
revision 485 and runs on both MS Windows and GNU/Linux.

You can choose to download the latest version of Clonezilla live, DRBL live,
or GParted live ISO/zip file then create the live USB.

%prep
%setup -q
rename unetbootin tuxboot *
sed -i 's/unetbootin/tuxboot/g' *.htm build-* *.txt *.cpp *.bat *.sh mk* qmake* *.desktop *.h *.pot *.pro *.qrc *.ts *.ui *.rc vcs-*
sed -i 's/"7z"/"7za"/' tuxboot.cpp

%build
lupdate-qt4 tuxboot.pro
lrelease-qt4 tuxboot.pro
qmake-qt4 "DEFINES+=NOSTATIC CLONEZILLA" "RESOURCES+=tuxboot-linux.qrc" tuxboot.pro
make

%install
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Tuxboot
Icon=tuxboot
Comment=Tool for creating Live USB drives
Categories=Application;System;
Exec=tuxboot
Terminal=false
Type=Application
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.TXT
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 23
- Rebuild for Fedora
