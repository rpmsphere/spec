%global rustflags -Clink-arg=-Wl,-z,relro,-z,now
%undefine _debugsource_packages
%define user_service /etc/systemd/user/

Name:     asusctl
Version:  5.0.7
Release:  1
Summary:  A control daemon, CLI tools, and a collection of crates for interacting with ASUS ROG laptops 
License:  MPL-2.0
Group:    System/Configuration/Hardware
URL:      https://asus-linux.org
# GiSource   https://gitlab.com/asus-linux/asusctl
Source:  https://gitlab.com/asus-linux/asusctl/-/archive/%version/%name-%version.tar.gz
Source1: README.ru
#Source2: vendors-%version.tar
#Patch1: asusctl-4.3.1-systemd.patch
BuildRequires: cmake
BuildRequires: fontconfig-devel gcc-c++ libudev-devel cargo
#BuildRequires: python3-mpl_toolkits python3-setuptools python3-zope
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gdk-3.0)

%description
asusd is a utility for Linux to control many aspects of various ASUS laptops
but can also be used with non-asus laptops with reduced features.

%description -l ru_RU.utf8
asusd - утилита для Linux, позволяющая управлять многими аспектами различных ноутбуков ASUS.
но также может использоваться с ноутбуками сторонних производителей с ограниченными возможностями.

%package rog-gui
Summary: An experimental GUI for %name
Group:    System/Configuration/Hardware
ExclusiveArch: x86_64

%description rog-gui
A one-stop-shop GUI tool for asusd/asusctl. It aims to provide most controls,
a notification service, and ability to run in the background.

%prep
%setup -q
#%%patch1 -p1

%build
export RUSTFLAGS="%rustflags"
#RUST_BACKTRACE=1 
cargo build --release

%install
export RUSTFLAGS="%rustflags"
install -m644 %SOURCE1 %_builddir/%name-%version
%make_install

mkdir -p %buildroot/%user_service
mv %buildroot/usr/lib/systemd/user/asusd-user.service %buildroot/%user_service/asusd-user.service
#mkdir -p %buildroot/%_unitdir
#mv %buildroot/usr/lib/systemd/system/asusd.service %buildroot/%_unitdir/asusd.service
#mkdir -p %buildroot/%_udevrulesdir
#mv %buildroot/usr/lib/udev/rules.d/99-asusd.rules %buildroot/%_udevrulesdir/99-asusd.rules
#rm -rf %buildroot/usr/lib/

%files
%_bindir/asusctl
%_bindir/asusd*
%doc README.ru *.md
#%%_sysconfdir/asusd
%_datadir/asusd
%_datadir/dbus-1/system.d/*.conf
#_datadir/fish/vendor_completions.d/*
#_datadir/zsh/site-functions/*
%_udevrulesdir/*.rules
%_unitdir/*.service
%user_service/*.service
%_iconsdir/hicolor/*/*/*

%files rog-gui
%_bindir/rog-control-center
%_datadir/applications/rog-control-center.desktop
%_iconsdir/hicolor/512x512/apps/rog-control-center.png
%_datadir/rog-gui/*

%changelog
* Sat Feb 10 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.7
- Rebuilt for Fedora
* Mon Sep 11 2023 Hihin Ruslan <ruslandh@altlinux.ru> 4.7.2-alt1.1
- Update sisyphus
* Sat Sep 09 2023 Evgeniy Kukhtinov <neurofreak@altlinux.org> 4.7.2-alt1
- Version 4.7.2 
* Mon Oct 31 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.5.0-alt0_1_rc4
- Update from git (Version 4.5.0-rc4)
- Git commit ba1d3f045d0fca79f125c165fd3cf34da249b506
* Sun Jul 24 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.3.0-alt1
- Version 4.3.0
* Tue Jun 21 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.1.1-alt1
- Initial build for Sisyphus
