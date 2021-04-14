Name: gmtp
Version: 1.3.3
Release: 5.1
Summary: A basic media player client
License: BSD-like
Group: File tools
Source: gMTP-%version.tar
BuildRequires: libmtp-devel
BuildRequires: flac-devel
BuildRequires: libid3tag-devel
BuildRequires: libusb-devel
BuildRequires: libvorbis-devel
BuildRequires: gtk3-devel
#BuildRequires: gio-devel
BuildRequires: glib2-devel

%description
Supports MTP devices including those with multiple storage devices
(typically mobile phones). Supports Drag'n'Drop interface for
upload/download of files.

%prep
%setup -q -n gMTP-%version

%build
export LDFLAGS=-Wl,--allow-multiple-definition
make gtk3

%install
%make_install \
		DESTDIR=%buildroot \
                PREFIX=%_usr \
        install-gtk3

%make_install \
		DESTDIR=%buildroot \
                PREFIX=%_usr \
	register-gsettings-schemas

%find_lang gmtp

%files -f gmtp.lang
%_bindir/*
%_datadir/applications/*.desktop
%_datadir/gmtp
%_datadir/pixmaps/*
%_datadir/glib-2.0/schemas/*
%_datadir/gconf/schemas/gmtp.schemas

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.3
- Rebuilt for Fedora
* Thu Jul 12 2012 Paul Wolneykien <manowar@altlinux.ru> 1.3.3-alt1
- Initial release for ALT Linux.
