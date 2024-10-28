Name:           burg-manager
Version:        1.1.0
Release:        1
Summary:        GUI to simplify the installation and configuration of Burg
License:        GPL
URL:            https://www.sourceslist.eu/burg-manager/
Group:          Applications/System
#Source:        git clone git://github.com/ingalex/burg-manager.git
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       buc, burg

%description
Burg-manager is a gui to simply install Burg, to set most of Burg bootloader
parameters, to restore Grub2 and to install new themes.

%prep
%setup -q
sed -i 's/bash global/bash killlang/' root/usr/share/burg-manager/burg-manager.mc

%build

%install
rm -rf $RPM_BUILD_ROOT
%__install -d -m755 %{buildroot}%{_bindir}
%__install -d -m755 %{buildroot}%{_datadir}
%__cp -a root/usr/share/* %{buildroot}%{_datadir}

cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
mkdir -p \$HOME/.burg-manager
if [ -f \$HOME/.burg-manager/language ] ; then
  buc /usr/share/burg-manager/burg-manager.mc
else
  buc /usr/share/burg-manager/langchooser.mc
fi
EOF

%post
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%files
%doc LICENSE README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
