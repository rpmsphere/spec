%global git cd7c03b
%global uuid system-monitor@paradoxxx.zero.gmail.com
%global github paradoxxxzero-gnome-shell-system-monitor-applet

Name:           gnome-shell-extension-system-monitor-applet
Version:        1.92
Release:        2.1
Summary:        A Gnome shell system monitor extension

Group:          User Interface/Desktops
License:        GPLv3+
URL:            https://github.com/paradoxxxzero/gnome-shell-system-monitor-applet
Source0:        https://github.com/paradoxxxzero/gnome-shell-system-monitor-applet/tarball/master/%{github}-%{version}-0-gc03ab92.zip
BuildArch:      noarch

Requires:       gnome-shell

%description
Display system information in gnome shell status bar, such as memory usage,
CPU usage, and network rate.

%prep
%setup -q -n %{github}-%{git}

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/%{uuid}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/
install -Dp -m 0644 %{uuid}/{extension.js,metadata.json,stylesheet.css} \
  $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/%{uuid}/
install -Dp -m 0644 org.gnome.shell.extensions.system-monitor.gschema.xml \
  $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/
# The translations are coming soon.

%postun
if [ $1 -eq 0 ] ; then
     glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%defattr(-,root,root,-)
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.system-monitor.gschema.xml

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.92
- Rebuild for Fedora

* Sun Jun 26 2011 Fabian Affolter <fabian@bernewireless.net> - 1.92-1
- Updated to new upstream release 1.92

* Sat Jun 18 2011 Fabian Affolter <fabian@bernewireless.net> - 1.90-1
- Updated to new upstream release 1.90

* Wed Jun 08 2011 Fabian Affolter <fabian@bernewireless.net> - 0.99-1
- Updated to new upstream release 0.99

* Sat Jun 04 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9-2
- Scriplet updated
- Version condition removed

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9-1
- Initial package for Fedora
