%undefine _debugsource_packages

Name:           furiusisomount
Version:        0.11.3.1
Release:        6.1
Summary:        An ISO, IMG, BIN, MDF and NRG Image management utility
License:        GPLv3
Group:          Archiving/Cd burning
URL:            https://www.marcus-furius.com/?page_id=170
Source:         furiusisomount_%{version}.tar.gz
BuildRequires:  desktop-file-utils python-devel
BuildArch:      noarch

%description
Simple Gtk+ Interface to Mount ISO, IMG, BIN, MDF and NRG Image files without 
burning to disk.

%prep
%setup -q -n %{name}_%{version}
sed -i 's|gtk-cdrom|%{name}|' app.desktop

%build

%install
%__install -dm 755 %{buildroot}%{python2_sitelib}/%{name}
%__install -dm 755 %{buildroot}%{_bindir}
%__install -dm 755 %{buildroot}%{_datadir}/applications
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps

#Remove unneeded files
rm -fr .bzr .project .pydevproject .settings %{name}

mv app.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
cp -r * $RPM_BUILD_ROOT%{python2_sitelib}/%{name}
cp pix/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
desktop-file-install --remove-key='Comment' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --set-comment='Simple Gtk+ Interface to Mount ISO, IMG, BIN, MDF and NRG Image files without burning to disk.' %{buildroot}%{_datadir}/applications/%{name}.desktop

#Create a working launch script (the included one doesn't work when you move the files around)
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
python2 "%{python2_sitelib}/%{name}/src/main.py" \$1
EOF

chmod 755 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.3.1
- Rebuilt for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 0.11.3.1-3.mga3
+ Revision: 350979
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Oct 20 2012 malo <malo> 0.11.3.1-2.mga3
+ Revision: 308525
- update RPM group
* Wed Apr 04 2012 juancho <juancho> 0.11.3.1-1.mga2
+ Revision: 228294
- Install the python in correct location %%{python2_sitelib}
- Fix launch script
- Replace the use of the application name for %%{name} macro
- Remove included VCS files.
- Fixed comments in desktop file
- Fixed installation of binary
- Fixed Url and description
  + gregorybravas <gregorybravas>
    - initial package
    - imported package furiusisomount
