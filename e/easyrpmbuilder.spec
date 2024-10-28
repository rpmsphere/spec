%undefine _debugsource_packages

Name:          easyrpmbuilder
Summary:       A rpm package builder helper
Version:       0.5.6
Release:       4.1
License:       GPL v2
Group:         Development/Tools/Building 
BuildRequires: gcc-c++, qt4-devel
Source0:       easyrpmbuilder-0.5.6.tar.bz2
URL:           https://kde-apps.org/content/show.php/Easy+RPM+Builder?content=114271
Requires:      rpm-build

%description
A tool for developers who want to make there application available as RPM
packages. The templates will give you some help how to build your own rpm
package for your application.

%prep
%setup -q

%build
qmake-qt4
make %{?_smp_mflags}
lrelease-qt4 %{name}.pro

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/qt4/translations
mkdir -p %{buildroot}%{_datadir}/doc/packages/%{name}/RPM-HOWTO
mkdir -p %{buildroot}%{_datadir}/applications
cp bin/* %{buildroot}%{_bindir}
cp src/templates/*.tpl %{buildroot}%{_datadir}/%{name}
cp src/groups/*.grp %{buildroot}%{_datadir}/%{name}
cp -r doc/RPM-HOWTO/* %{buildroot}%{_datadir}/doc/packages/%{name}/RPM-HOWTO
cp src/translations/english.qm %{buildroot}%{_datadir}/qt4/translations/%{name}_en_GB.qm
cp src/translations/german.qm %{buildroot}%{_datadir}/qt4/translations/%{name}_de_DE.qm
cp src/translations/spanish.qm %{buildroot}%{_datadir}/qt4/translations/%{name}_es_ES.qm
cp src/translations/brazilian.qm %{buildroot}%{_datadir}/qt4/translations/%{name}_br_BR.qm
cp src/icons/rpm.png %{buildroot}%{_datadir}/%{name}/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
Comment=A tool for developers who want to make there application available as RPM packages
Exec=%{_bindir}/%{name}
Icon=%{_datadir}/%{name}/rpm.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Development;Qt;IDE;
EOF

%files
%{_bindir}/easyrpmbuilder
%dir %{_datadir}/easyrpmbuilder
%{_datadir}/easyrpmbuilder/rpm.png
%{_datadir}/easyrpmbuilder/*.tpl
%{_datadir}/easyrpmbuilder/*.grp
%{_datadir}/applications/easyrpmbuilder.desktop
%dir %{_datadir}/doc/packages/easyrpmbuilder
%dir %{_datadir}/doc/packages/easyrpmbuilder/RPM-HOWTO
%{_datadir}/doc/packages/easyrpmbuilder/RPM-HOWTO/*.html
%{_datadir}/doc/packages/easyrpmbuilder/RPM-HOWTO/*.css
%dir %{_datadir}/doc/packages/easyrpmbuilder/RPM-HOWTO/stylesheet-images
%{_datadir}/doc/packages/easyrpmbuilder/RPM-HOWTO/stylesheet-images/*.gif
%{_datadir}/qt4/translations/*.qm

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.6
- Rebuilt for Fedora
* Fri Jan 07 2011 zawertun@gmail.com
- Initial release, version 0.5.6
