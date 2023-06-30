Name:          crystal-cursor-theme
Version:       1.0
Release:       10.1
Summary:       Crystal mouse icons themes for X11
Group:         User Interface/Desktops
URL:           https://digilander.libero.it/m4rt/html/crystalcursors.html
Source0:       https://digilander.libero.it/m4rt/files/crystalblue.tar.gz
Source1:       https://digilander.libero.it/m4rt/files/crystalgray.tar.gz
Source2:       https://digilander.libero.it/m4rt/files/crystalgreen.tar.gz
Source3:       https://digilander.libero.it/m4rt/files/crystalwhite.tar.gz
License:       LGPL
BuildArch:     noarch

%description
Some cursors themes inspired from crystal icons from Mart.
There are blue, gray, green and white versions.

%prep
%setup -q -c -a1 -a2 -a3

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/icons
for d in crystalblue crystalgray crystalgreen crystalwhite; do
   cp -R --no-dereference $d $RPM_BUILD_ROOT%{_datadir}/icons
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/crystalblue
%{_datadir}/icons/crystalgray
%{_datadir}/icons/crystalgreen
%{_datadir}/icons/crystalwhite

%changelog
* Mon Jun 20 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Mon Jul 07 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0-4mamba
- specfile updated
* Fri Mar 09 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0-3qilnx
- remove requirement for Xorg
* Thu Feb 02 2006 Davide Madrisan <davide.madrisan@qilinux.it> 1.0-2qilnx
- package arch set to noarch
* Wed Feb 01 2006 Davide Madrisan <davide.madrisan@qilinux.it> 1.0-1qilnx
- added crystalblue crystalgray crystalgreen mouse icons
- do not write files in the /etc/skel folder, use the system folder instead
* Mon Oct 10 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.4-4qilnx
- fixed permissions of index.theme
* Thu May 06 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4-3qilnx
- skel/.icons/default directory removed because it hurt the KDE 3.2.x
  mouse cursors manager
* Sat Mar 06 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4-2qilnx
- fix: preserve symbolic links
* Thu Mar 04 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4-1qilnx
- first build
