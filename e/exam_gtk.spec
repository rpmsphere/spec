%define _binaries_in_noarch_packages_terminate_build 0
Name:           exam_gtk
Version:        0.1
Release:        3
Summary:        Test system develop by PHP-GTK.
Group:          Amusements/Eduactions
License:        GPL
URL:            http://www.ossii.com.tw/
Source0:        exam_gtk.tar.gz
Requires:	php php-gtk2 php-gd php-cli php-pdo php-common
BuildArch:	noarch

%description
Test system developed using PHP-GTK.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages/

cd $RPM_BUILD_ROOT%{_datadir}/
tar zxf %{SOURCE0} 
mv %{name}/%{name}.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages/
cd -

#Desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=exam_gtk
Comment=Test system develop by PHP-GTK
Comment[zh_TW]=數位化評量系統
Exec=php /usr/share/exam_gtk/for_exam.php
Terminal=false
Type=Application
MimeType=application/x-quiz;
NoDisplay=true
Categories=ebook;
EOF

%post
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0777)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Thu Dec 03 2009 Kami <kami@ossii.com.tw> 0.1-3.ossii
- Fix the newest PHP compatibility

* Tue Dec 01 2009 Kami <kami@ossii.com.tw> 0.1-2.ossii
- Change file locations and test sample

* Thu Nov 19 2009 Feather Mountain <john@ossii.com.tw> 0.1-1.ossii
- Build for OSSII
