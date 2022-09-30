%undefine _debugsource_packages

Name:           polo
Version:        18.8.3beta
Release:        1
Summary:        Advanced file manager for Linux written in Vala.
License:        LGPLv3+
URL:            https://github.com/teejee2008/%{name}
#Source0:        https://github.com/teejee2008/%{name}/archive/v%{vermaj}.%{vermin}.tar.gz
Source0:        %{name}-master.zip
BuildRequires:  vala, vte291-devel, libgee-devel, json-glib-devel, libxml2-devel, chrpath, gettext
Requires:       rsync, p7zip, p7zip-plugins, tar, gzip, bzip2, xz, gvfs, libsoup
#Requires:       pv, fish, qemu-kvm, qemu-img, rclone

%description
Advanced file manager for Linux written in Vala. Supports multiple panes (single, dual, quad)
with multiple tabs in each pane. Supports archive creation, extraction and browsing. Support 
for cloud storage; running and managing KVM images, modifying PDF documents and image files, 
booting ISO files in KVM, and writing ISO files to USB drives.

%prep
%setup -q -n polo-master
sed -i 's|public ProgressPanel|protected ProgressPanel|' src/Gtk/ProgressPanel.vala
sed -i 's|public AsyncTask|protected AsyncTask|' src/Utility/AsyncTask.vala
sed -i 's|public MediaStream|protected MediaStream|' src/Utility/MediaFile.vala
sed -i 's|de nl fr tr|nl sv|' src/makefile
sed -i 's|cmd.to_utf8()|cmd.data|' src/Gtk/TermBox.vala
sed -i '147,176d' src/Utility/ArchiveTask.vala
sed -i 's|ArchiveTask.7zip_version|16.02|' src/Utility/ArchiveTask.vala src/Gtk/MainMenubar.vala

%build
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/%{name}-disk
%{_bindir}/%{name}-gtk
%{_bindir}/%{name}-gtk3-helper
%exclude %{_bindir}/%{name}-uninstall
%{_datadir}/polo
%{_datadir}/appdata/polo-gtk.appdata.xml
%{_datadir}/applications/polo-gtk.desktop
%{_datadir}/locale/*/LC_MESSAGES/polo.mo
%{_datadir}/pixmaps/polo.png

%changelog
* Fri Dec 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 18.8.3beta
- Rebuilt for Fedora
* Tue Jan 30 2018 <grturner@5x5code.com> 18-1beta
- Initial packaging
