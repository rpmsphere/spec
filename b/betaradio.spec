Name:           betaradio
Version:        1.2
Release:        1
License:        GPLv2
URL: 		https://code.google.com/p/betaradio/
BuildRequires:  gtk2-devel, libcurl-devel, gstreamer-devel, json-glib-devel, libsoup-devel, vala
Source0:        https://betaradio.googlecode.com/files/%{name}-%{version}.tar.bz2
Group:          Multimedia/Sound/Players
Summary:        Listen to hiChannel radio online

%description
With this client you can listen to hiChannel radio , PTT Radio, Pinewave Radio,
and THBS without opening a browser. It displays a icon on system tray that you
can click and select the channel you want to listen to. 

%prep
%setup -q

%build
cp /usr/share/automake-*/config.guess build-aux/
./configure --prefix=/usr
make

%install
rm -rf %buildroot
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/betaradio
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/*
%{_mandir}/man1/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Sat Apr 25 2009 swyear@yahoo.com.tw
- packaged betaradio version 0.1.2
