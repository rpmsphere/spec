Name:           alock
Version:        2.4.0git
Release:        1
Summary:        A simple screen locker
License:        MIT
URL:            https://github.com/Arkq/alock
Source0:        %{name}-master.zip
BuildRequires:  pam-devel
BuildRequires:  imlib2-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXpm-devel
BuildRequires:  xmlto
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-xbitmaps

%description
alock locks the X server until the user enters a password via the keyboard.
If the authentification was successful the X server is unlocked and the user
can continue to work.

Fork from https://github.com/mgumz/alock (https://code.google.com/p/alock/)

%prep
%setup -q -n %{name}-master

%build
autoreconf -ifv
%configure --prefix %{_prefix}\
           --enable-xrender --enable-xcursor --enable-xpm --enable-pam\
           --enable-hash --enable-imlib2 --with-dunst --with-xbacklight
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
#{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Mar 25 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.0git
- Rebuilt for Fedora
* Wed Mar 07 2012 qmp <glang@lavabit.com> 0.94-1
- Initial packaging for fedora
