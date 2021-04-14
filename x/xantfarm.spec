%undefine _debugsource_packages

Summary: Animates X11 root window with a simulated ant hill
Name: xantfarm
Version: 2014.08.14
Release: 5.1
Source: http://www.acme.com/software/xantfarm/xantfarm_14Aug2014.tar.gz
URL: https://acme.com/software/xantfarm/
License: distributable
Group: X11/Amusements
BuildRequires: imake
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libXext-devel

%description
There are three Elements in the ant world: Air, Dirt, and Sand. Ants move
through Air, dig up Dirt, and drop it as Sand. Ants have three Behaviors:
Wandering, Carrying, and Panic. There are a few simple probabilities built
in to the program that control the transitions between Wandering and Carrying.
To see them Panic, try poking the ants with the cursor.

%prep
%setup -q -n %{name}

%build
xmkmf
make

%install
make DESTDIR=%{buildroot} install install.man

%files
%doc README
%{_bindir}/xantfarm
%{_mandir}/man1/xantfarm.1x.*

%changelog
* Tue Dec 26 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2014.08.14
- Rebuilt for Fedora
* Mon Mar 02 1998 chorn@warwick.net
- Initial package
