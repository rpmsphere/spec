%global uuid iconplacesbookmarks@fpmurphy.com
%global shortname iconplacesbookmarks

Name:           gnome-shell-extension-%{shortname}
Version:        1.1
Release:        2.1
Summary:        A gnome-shell extension to add a Places and Bookmarks menu

Group:          User Interface/Desktops
License:        GPLv2
URL:            http://www.fpmurphy.com/gnome-shell-extensions/
Source0:        http://www.fpmurphy.com/gnome-shell-extensions/%{shortname}-%{version}.tar.gz
BuildArch:      noarch

Requires:       gnome-shell >= 3.0.1

%description
This Gnome Shell extension adds a Places and Bookmarks menu to panel.

%prep
%setup -q -n %{uuid}

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json,stylesheet.css} \
  $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora

* Wed Sep 07 2011 Fabian Affolter <fabian@bernewireless.net> - 1.0-1
- Updated to new upstream version 1.1

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 1.0-1
- Initial package for Fedora
