%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

Summary: eXe eLearning XHTML editor
Name: exe
Version: 1.04.0.3600
Release: 1
Source0: https://eduforge.org/frs/download.php/839/%{name}-%{version}-source.tgz
Source1: %{name}-1.03.zh_TW.po
License: GPL
Group: Applications/Editors
URL: https://exelearning.org/
BuildRequires: python2-devel, python2-setuptools, gettext
Requires: python-imaging, python-zope-interface
Requires: firefox
Obsoletes: exe-twisted

%description
eXe, the eLearning XHTML editor, is an authoring environment which enables
teachers to publish web content in standard package formats (like IMS
Content Packages and SCORM) without the need to become proficient in HTML
or XML markup.  Content generated using eXe can be used by any Learning
Management System.

%prep
%setup -q -n exe
# remove the other platform binaries
#rm -f exe/webui/templates/mimetex.64.cgi
rm -f exe/webui/templates/mimetex.exe
rm -f exe/webui/templates/mimetex-darwin.cgi
rm -f exe/msvcr71.dll
rm -f twisted/spread/cBanana.so
rm -f twisted/protocols/_c_urlarg.so

#sed -i 's/2\.0\.0\.6/3.0.5/' exe/webui/linux-profile/prefs.js
#sed -i 's/2\.0\.0\.\*/3.0.5/' exe/webui/linux-profile/extensions/exeex@exelearning.org/install.rdf

%build
rm -rf %{buildroot}
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}
cp -a twisted nevow formless %{buildroot}%{_datadir}/exe
mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/exe.png %{buildroot}%{_datadir}/pixmaps/exe.png
mkdir -p %{buildroot}%{_datadir}/applications/
cp exe.desktop %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/mime/packages/
cp exe.xml %{buildroot}%{_datadir}/mime/packages/
chmod 755 %{buildroot}%{_datadir}/exe/templates/mimetex.cgi

cd %{buildroot}%{_datadir}/%{name}/locale
cp -f %{SOURCE1} zh_tw/exe_zh_tw.po
msgfmt zh_tw/exe_zh_tw.po -o zh_tw/LC_MESSAGES/exe.mo
mv zh_tw zh_TW
sed -i -e 's/Utility/Development/' -e 's/Exec=exe/Exec=run-exe.sh/' %{buildroot}%{_datadir}/applications/exe.desktop
echo -e 'Name[zh_TW]=eXe\nComment[zh_TW]=數位學習網頁編輯程式' >> %{buildroot}%{_datadir}/applications/exe.desktop

%{__cat} <<EOF > $RPM_BUILD_ROOT%{_bindir}/run-exe.sh
#!/bin/sh
python2/usr/bin/exe "\$@" &
sleep 10
LOGNAME=eXe7913 firefox -profile \$HOME/.exe/linux-profile:/ https://127.0.0.1:51235/
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%attr(755,root,root) %{_bindir}/*
%{python2_sitelib}/exe*
%{_datadir}/exe
%{_datadir}/pixmaps/exe.png
%config %{_datadir}/mime/packages/exe.xml
%config %{_datadir}/applications/exe.desktop
%doc COPYING NEWS README
#exclude /usr/lib/debug/usr/share/exe/templates/mimetex.cgi.debug
%exclude %{_datadir}/exe/templates/mimetex.cgi

%post
/usr/bin/update-mime-database /usr/share/mime &> /dev/null

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.04.0.3600
- Rebuilt for Fedora
* Mon Jul 09 2007 Jim Tittsler <jim@exelearning.org>
- update spec file to work with Fedora 7
- use files list instead of recording INSTALLED_FILES in setup.py to catch .pyo files
* Mon May 28 2007 Jim Tittsler <jim@exelearning.org>
- add desktop file and icon
- add MIME type and .elp glob to associate file types
* Thu May 24 2007 Jim Tittsler <jim@exelearning.org>
- remove temp_print_dirs workaround from datadir/exe
* Tue May 22 2007 Jim Tittsler <jim@exelearning.org>
- optional clversion and clrelease defines to improve automation
- remove more spurious binaries for other platforms
- require firefox
* Mon May 21 2007 Jim Tittsler <jim@exelearning.org>
- make 'Release:' distribution specific
* Wed May 09 2007 Jim Tittsler <jim@exelearning.org>
- bring up to date, including our custom twisted/nevow
