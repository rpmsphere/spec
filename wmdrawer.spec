%global debug_package %{nil}
Name: 		wmdrawer
Version: 	0.10.5
Release: 	1
Summary:	Retractable button bar launcher dockapp
Source:		http://people.easter-eggs.org/~valos/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-lib64.patch
License:	GPL
Group:		User Interface/Desktops
URL:		http://people.easter-eggs.org/~valos/%{name}/
Requires:	gtk2
BuildRequires: 	gtk2-devel

%description
wmDrawer is a dock application (dockapp) which provides a drawer
(retractable button bar) to launch applications.

%description -l de
wmDrawer ist ein Dockapp, welches eine ausklappbare
Knopfleiste mit Anwendungsstartern darstellt.

%prep
%__rm -rf %{buildroot}

%setup -q
%if "%{_lib}" == "lib64"
%patch0 -p1
%endif

%build
%__make

%install
%__mkdir -p %{buildroot}%{_bindir}
%__mkdir -p %{buildroot}%{_mandir}/man1
%__install -m 755 %{name} %{buildroot}%{_bindir}/%{name}-bin
%__install -m 644 doc/%{name}.1x.gz %{buildroot}%{_mandir}/man1

#startup script
%__mkdir -p %{buildroot}%{_bindir}
%{__cat} > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
if [ -e \$HOME/.wmdrawerrc ] ; then
  exec wmdrawer-bin
else
  cp /usr/share/doc/%{name}-%{version}/wmdrawerrc.example \$HOME/.wmdrawerrc
  exec wmdrawer-bin
fi
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc wmdrawerrc.example AUTHORS ChangeLog COPYING INSTALL README TODO ./doc/wmdrawer-it.sgml ./doc/wmdrawer.sgml
%attr(755,root,root) %{_bindir}/%{name}*
%{_mandir}/man1/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10.5
- Rebuild for Fedora
* Thu Jan 03 2008 Oliver Burger <rpm@mandrivauser.de> 0.10.5-3mud2008.0
- rebuild for MUde
- changed from csh to bash-script
* Thu Jan 03 2008 Mario Blaettermann <mario.blaettermann@t-online.de>
- add startup script and xdg menu entry
* Mon Dec 03 2007 Mario Blaettermann <mbl103@arcor.de>
- initial version
