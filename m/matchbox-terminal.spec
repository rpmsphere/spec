Summary:        Terminal for the Matchbox Desktop
Name:           matchbox-terminal
Version:        0.2
Release:        4.1
URL:            https://git.yoctoproject.org/cgit/cgit.cgi/matchbox-terminal/
License:        GPLv2+
Group:          Graphical desktop/Other
Source0:        https://git.yoctoproject.org/cgit/cgit.cgi/matchbox-terminal/snapshot/%name-%version.tar.gz
BuildRequires:  gtk3-devel
BuildRequires:  vte291-devel

%description
TODO:
* Tabs
* Check it builds with GTK+ 2.6
* Menu with optional libowl
* Single instance binary which creates new windows

%prep
%setup -q

%build
autoreconf -vfi
%configure
make

%install
%make_install

%files
%doc AUTHORS COPYING
%_bindir/*
%_datadir/applications/*

%changelog
* Sun Aug 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
