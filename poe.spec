%global debug_package %{nil}

Summary: Small and quick curses programmer's editor
Name: poe
Version: 0
Release: 8.1
License: BSD-like
Group: Applications/Editors
Source: https://codeload.github.com/FredFoonly/poe/zip/master#/%{name}-master.zip
URL: https://github.com/FredFoonly/poe
BuildRequires: ncurses

%description
Currently it's roughly functionally equivalent to PE2. The .dir file isn't yet
supported, though .keys and .unknown are. As I get more time to work on it I'll
push it farther along. Profile handling will be changing quite a bit. I want to
do undo in a different way than PE2 did it and different from the way other
programmers editors do it (with an undo/redo stack); both methods have their
advantages and I'd like to get the best of both worlds.

%prep
%setup -q -n %{name}-master
sed -i 's|/usr/local|%{buildroot}/usr|' linux/Makefile.inc
sed -i 's|/man/|/share/man/|' linux/Makefile

%build
make -C linux

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_bindir}
%make_install -C linux

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc License.txt design.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Aug 30 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0
- Rebuild for Fedora
