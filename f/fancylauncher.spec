%undefine _debugsource_packages

Summary: The fanciest program launcher whatsoever!
Name: fancylauncher
Version: 0.10
Release: 5.1
License: GPL
Group: X11/Utilities
Source: https://www.docs.uu.se/~adavid/utils/FancyLauncher-%{version}.tgz
URL: https://www.docs.uu.se/~adavid/utils/FancyLauncher/
BuildRequires: imlib-devel

%description
This is a very configurable program launcher with extra
features like: blending with the root window, highlight,
tooltips, several pages, clock, pop mail checker...

%prep
%setup -q -n FancyLauncher-%{version}
sed -i 's|/usr/local/FancyLauncher|/usr/share/fancylauncher|' Makefile data/config *.c help.html plugins/xscreensaver/*
sed -i 's|-mpentiumpro|-Wl,--allow-multiple-definition|' Makefile

%build
make

%install
rm -rf %{buildroot}
install -Dm755 FancyLauncher %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r FancyLauncher.gif help.html data plugins snapshots %{buildroot}%{_datadir}/%{name}

%files
%doc Changelog
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Fri Apr 10 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10
- Rebuilt for Fedora
* Mon Jul 17 2000 Alexandre David <adavid@docs.uu.se>
- Initial package
