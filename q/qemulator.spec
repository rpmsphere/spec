%define oname   Qemulator

Summary:	Interface to configure and launch Qemu
Name:		qemulator
Version:	0.5
Release:	1
License:	GPL
Group:		Emulators
URL:		http://qemulator.createweb.de/
Source0:	http://qemulator.createweb.de/%{oname}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         fix_python_dir.patch
BuildArch:	noarch
Requires:       python2
Requires:       pygtk2
Requires:       libglade2
Requires:       gnome-python2
Requires:       qemu
Requires:	pygtk2-libglade

%description
A launcher for Qemu that manages Qemu configs and creates disk images
Qemu-launcher provides a point and click interface to Qemu. It also
allows you to create, save, load, and run multiple Qemu VM
configurations. It has a basic interface for creating or convertering
disk images.

Only supports the x86 PC emulator part of Qemu.

%prep
%setup -q -n %{oname}-%{version}

%patch0 -p1

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir} \
         %{buildroot}%{_datadir}/%{name} \
         %{buildroot}%{_datadir}/pixmaps \
         %{buildroot}%{_libdir}
%__cp -a usr/local/lib/qemulator/* %{buildroot}%{_datadir}/qemulator
%__cp -a usr/local/share/* %{buildroot}%{_datadir}/
%__chmod +x %{buildroot}%{_datadir}/qemulator/qml_imagecreation.py \
         %{buildroot}%{_datadir}/qemulator/qml_machinesetup.py \
         %{buildroot}%{_datadir}/qemulator/qml_filehandlers.py \
         %{buildroot}%{_datadir}/qemulator/qml_configuration.py \
         %{buildroot}%{_datadir}/qemulator/qml_tools.py \
         %{buildroot}%{_datadir}/qemulator/qml_installwizzard.py \
         %{buildroot}%{_datadir}/qemulator/qml_style.py
%__chmod -x %{buildroot}%{_datadir}/qemulator/icons/mac.png
convert -resize 32x32 usr/local/share/pixmaps/qemulator.svg qemulator.xpm
%__cp qemulator.xpm %{buildroot}%{_datadir}/pixmaps/
%__ln_s /usr/share/qemulator/qemulator.py %{buildroot}%{_bindir}/qemulator
%__cp -a %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%clean
%__rm -rf %buildroot

%files
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/pixmaps/%{name}/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/locale/*/LC_MESSAGES/%{oname}.mo
%{_datadir}/pixmaps/qemulator/*.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Fri Oct 17 2008 Wind <Wind@ossii.com.tw> 0.5-3
- Rebuild for OSSII.
* Mon Mar 31 2008 Anne Nicolas <anne.nicolas@mandriva.com> 0.5-2mdv2008.1
+ Revision: 191235
- Add pygtk2.0-libglade require (#39627)
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Tue Oct 09 2007 Jérôme Soyer <saispo@mandriva.org> 0.5-1mdv2008.1
+ Revision: 95839
- Add imagemagick to BuildRequires
- Add desktop file
- Add desktop file
- import qemulator
