Summary: Image GD
Summary(zh_TW): 圖片批次縮圖
Name: image-gd
Version: 0.0.18
Release: 1
Source0: %{name}-%{version}.tar.bz2
License: General Public Licence
Group: Applications/Multimedia
URL: http://opendesktop.org.tw/
BuildArch: noarch
BuildRequires: gambas3-runtime gambas3-gb-gui gambas3-gb-form gambas3-gb-gtk gambas3-devel
Requires: gambas3-runtime gambas3-gb-gui gambas3-gb-form gambas3-gb-gtk
Requires: ImageMagick
AutoReqProv: no

%description
This program is written in Gambas, so you will need Gambas to be installed.

%prep
%setup -q -n image_gd

%build
gbc3 -a -v
gba3 -v

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_bindir}
install -p image_gd.gambas %{buildroot}/%{_bindir}/image_gd
install -d %{buildroot}/%{_datadir}/pixmaps
install -d %{buildroot}/%{_datadir}/applications
install -p .icon/48.png %{buildroot}/%{_datadir}/pixmaps/image_gd.png
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Image GD
Name[zh_TW]=圖片批次縮圖
Comment=Batch Zooming Images
Exec=image_gd
Icon=image_gd
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;
EOF

%clean
rm -rf %{buildroot}

%files
%{_bindir}/image_gd
%{_datadir}/pixmaps/image_gd.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu May 27 2010 羽山 <john@ossii.com.tw> 0.0.18
- 調整了Requries﹑BuildRequires

* Fri May 14 2010 羽山 <john@ossii.com.tw> 0.0.17
- 改了一些標籤的名字

* Fri May 14 2010 羽山 <john@ossii.com.tw> 0.0.15
- 修正輸出的檔名多了個分號的問題

* Thu May 13 2010 羽山 <shadow@3wa.tw> 0.0.10
- Shell WAIT WAIT WAIT WAIT WAIT WAIT WAIT

* Thu May 13 2010 羽山 <shadow@3wa.tw> 0.0.9
- Logo
- Shell wait

* Thu May 13 2010 羽山 <shadow@3wa.tw> 0.0.6
- Fix exec to shell

* Thu May 13 2010 羽山 <shadow@3wa.tw> 0.0.5
- Fix Default Paths

* Thu May 13 2010 羽山 <shadow@3wa.tw> 0.0.4
- Initial release
