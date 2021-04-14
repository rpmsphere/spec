Name: obshutdown
Version: 0.1
Release: 5.1
Summary: Openbox shutdown manager
Summary(ru_RU.UTF-8): Управеление сеансом openbox
License: GPL
Group: Graphical desktop/Other
URL: https://github.com/panjandrum/obshutdown/
Source: %name-%version.tar.gz
BuildRequires: gtk2-devel cairo-devel automake

%description
GTK/Cairo based shutdown box styled for Openbox and others windows managers.

%prep
%setup -q
sed -i 's|inline ||' src/main.h

%build
export LDFLAGS=-Wl,--allow-multiple-definition
autoreconf -ifv
%configure 
%make_build CFLAGS+=-Wno-format-security

%install
%make_install

%files
%doc AUTHORS COPYING README
%_bindir/%name
%_datadir/%name/*

%changelog
* Tue May 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Sun Nov 08 2015 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt2
- initial build for ALT Linux Sisyphus
