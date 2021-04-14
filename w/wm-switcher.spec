Name:		wm-switcher
Version:	0.3
Release:	2.1
Summary:	Window manager switcher
Group:		User Interface/Desktops
License:	GPLv2
URL:		https://launchpad.net/wm-switcher
Source0:	http://launchpad.net/wm-switcher/trunk/%{version}/+download/%{name}.tar.gz
Requires:	pygtk2
BuildArch:	noarch

%description
The functionality desired is to be able to switch window managers instantly
(to try out), but also to set a different window manager to boot into.
The program is wrote in PyGTK. At the moment, only window managers that support
the '--replace' protocol are supported, however we will try to overcome
this barrier, in our mission to support as many Window Managers as possible.

%prep
%setup -q -c

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{name}
python2 base.py
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}
install -Dm644 img/logo.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.svg
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Comment=Window manager switcher
Name=WM Switcher
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Settings;DesktopSettings;
EOF

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}

%changelog
* Tue May 10 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
