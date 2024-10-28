Name:           awesome-gnome
Version:        0.0.1
Release:        4.1
Summary:        Setup awesome as window manager of GNOME 3
License:        CCPL
URL:            https://awesome.naquadah.org/wiki/Quickly_Setting_up_Awesome_with_Gnome
Source0:        https://aur.archlinux.org/packages/aw/awesome-gnome/%{name}.tar.gz
Requires:       awesome
Requires:       gdm
BuildArch:      noarch

%description
Simple set of config files to use awesome as a replacement for gnome-shell in 
GNOME 3.

%prep
%setup -q -n %{name}
rm %{name}.install
rm PKGBUILD

%build

%install
install -D -m 644 awesome.session $RPM_BUILD_ROOT/%{_datadir}/gnome-session/sessions/awesome.session
#install -D -m 644 awesome.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/awesome.desktop
install -D -m 644 %{name}.desktop $RPM_BUILD_ROOT/%{_datadir}/xsessions/%{name}.desktop

%files
%{_datadir}/gnome-session/sessions/awesome.session
#{_datadir}/applications/awesome.desktop
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Tue Jul 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuilt for Fedora

* Tue Jun 19 2012 qmp <glang@lavabit.com> - 0.0.1-2
- Rebuild

* Mon Dec 05 2011 qmp <glang@lavabit.com> - 0.0.1-1
- Initial packaging
