%global uuid poweroptions@fpmurphy.com
%global shortname poweroptions

Name:           gnome-shell-extension-%{shortname}
Version:        2.0
Release:        2.1
Summary:        A gnome-shell extension to add Poweroff and Hibernate options

Group:          User Interface/Desktops
License:        GPLv2
URL:            http://www.fpmurphy.com/gnome-shell-extensions/
Source0:        http://www.fpmurphy.com/gnome-shell-extensions/%{shortname}-%{version}.tar.gz
BuildArch:      noarch

Requires:       gnome-shell >= 3.0.1

%description
This Gnome Shell extension adds Poweroff and Hibernate options to user menu.

%prep
%setup -q -n %{uuid}

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json} \
  $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 2.0-1
- Initial package for Fedora
