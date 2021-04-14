Name:             bluej
Summary:          An integrated Java environment specifically designed for introductory teaching
Version:          3.1.6
Release:          4.1
License:          Freely available to anyone as is for use and non-commercial distribution
URL:              http://www.bluej.org/
Group:            Development/Tools/IDE
BuildRequires:    ant
BuildRequires:    unzip
BuildRequires:    desktop-file-utils
BuildRequires:    java-devel-openjdk lua
Requires(post):   shared-mime-info
Requires(postun): shared-mime-info
BuildArch:        noarch
Source0:          http://bluej.org/download/files/source/BlueJ-source-%(echo %{version}|tr -d .).zip
Source1:          %{name}.desktop
Source2:          bluej-hicolor-icons.tar.gz
Source3:          build.properties
Source4:          %{name}.xml
Source5:          bluej_oxygen_icons.tar.gz
Source6:          bluej_open_project.desktop
Source7:          bluej_open_folder.desktop

%description
The BlueJ environment was developed as part of a university research project
about teaching object-orientation to beginners. The aim of BlueJ is to provide
an easy-to-use teaching environment for the Java language that facilitates the
teaching of Java to first year students. Special emphasis has been placed on
visualisation and interaction techniques to create a highly interactive
environment that encourages experimentation and exploration.

BlueJ is based on the Blue system. Blue is an integrated teaching environment
and language, developed at the University of Sydney and Monash University,
Australia. BlueJ provides a Blue-like environment for the Java language.


Authors:
-------
    M. Kölling and J. Rosenberg

%package oxygen-icons
License:          LGPLv3
Summary:          BlueJ Icons for Oxygen Icon Theme
Group:            Development/Tools/IDE
Requires:         oxygen-icon-theme
Requires:         %{name} = %{version}

%description oxygen-icons
This package provides MIME type icons that integrate well into the KDE
Oxygen icon theme (http://www.oxygen-icons.org).

%package kde
License:          LGPLv3
Summary:          KDE integration for BlueJ
Group:            Development/Tools/IDE
Requires:         kdebase4-runtime
Requires:         %{name} = %{version}

%description kde
This package installs a KDE service menu that lets the user open BlueJ projects
by right clicking on BlueJ package files or folders.

%prep
unzip -u %{SOURCE0} -d %{name}-%{version}
%{__install} -m644 %{SOURCE3} %{name}-%{version}/build.properties
tar -xzf %{SOURCE2}
tar -xzf %{SOURCE5}

cd %{name}-%{version}/src/bluej
sed -i 's|ö|oe|' editor/moe/ReplacePanel.java debugger/jdi/NetworkTest.java editor/moe/FindPanel.java

%build
cd %{name}-%{version}
ant

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}
cp -pr %{name}-%{version}/lib $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/lib $RPM_BUILD_ROOT%{_datadir}/%{name}
for SIZE in 16x16 22x22 32x32 48x48 64x64 128x128 256x256; do
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$SIZE/apps
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$SIZE/mimetypes
%{__install} -m644 hicolor/$SIZE/apps/bluej.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$SIZE/apps/%{name}.png
cp -d hicolor/$SIZE/mimetypes/text-x-bluej.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$SIZE/mimetypes
done
for SIZE in 16x16 22x22 32x32 48x48 64x64 128x128 256x256; do
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/icons/oxygen/$SIZE/mimetypes
%{__install} -m644 bluej_oxygen_icons/oxygen/$SIZE/mimetypes/text-x-bluej.png $RPM_BUILD_ROOT%{_datadir}/icons/oxygen/$SIZE/mimetypes
done
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/applications
%{__install} -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/mime/packages
%{__install} -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/mime/packages/%{name}.xml
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus
%{__install} -m644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus
%{__install} -m644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus
%{__install} -d -m755 $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__install} -m644 bluej-%{version}/doc/LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}/LICENSE.txt
%{__install} -m644 bluej-%{version}/doc/THIRDPARTYLICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}/THIRDPARTYLICENSE.txt
cp -pr bluej-%{version}/examples $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__install} -d -m755 $RPM_BUILD_ROOT%{_docdir}/%{name}-oxygen-icons
%{__install} -m644 bluej_oxygen_icons/COPYING $RPM_BUILD_ROOT%{_docdir}/%{name}-oxygen-icons/
%{__install} -m644 bluej_oxygen_icons/README $RPM_BUILD_ROOT%{_docdir}/%{name}-oxygen-icons/
%{__install} -d -m755 $RPM_BUILD_ROOT%{_bindir}

# startscript
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/bash
# simple script to start BlueJ
java -cp "%{_datadir}/%{name}/bluej.jar:/etc/alternatives/java_sdk/lib/tools.jar" bluej.Boot "\$@"
EOF
%{__chmod} 755 $RPM_BUILD_ROOT%{_bindir}/%{name}

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/update-mime-database %{_datadir}/mime >/dev/null

%postun
%{_bindir}/update-mime-database %{_datadir}/mime >/dev/null

%files
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/22x22
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/22x22/apps
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/64x64/apps
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/256x256/apps
%dir %{_datadir}/icons/hicolor/16x16/mimetypes
%dir %{_datadir}/icons/hicolor/22x22/mimetypes
%dir %{_datadir}/icons/hicolor/32x32/mimetypes
%dir %{_datadir}/icons/hicolor/48x48/mimetypes
%dir %{_datadir}/icons/hicolor/64x64/mimetypes
%dir %{_datadir}/icons/hicolor/128x128/mimetypes
%dir %{_datadir}/icons/hicolor/256x256/mimetypes
%{_docdir}/%{name}
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/*.png

%files oxygen-icons
%dir %{_datadir}/icons/oxygen
%dir %{_datadir}/icons/oxygen/16x16
%dir %{_datadir}/icons/oxygen/22x22
%dir %{_datadir}/icons/oxygen/32x32
%dir %{_datadir}/icons/oxygen/48x48
%dir %{_datadir}/icons/oxygen/64x64
%dir %{_datadir}/icons/oxygen/128x128
%dir %{_datadir}/icons/oxygen/256x256
%dir %{_datadir}/icons/oxygen/16x16/mimetypes
%dir %{_datadir}/icons/oxygen/22x22/mimetypes
%dir %{_datadir}/icons/oxygen/32x32/mimetypes
%dir %{_datadir}/icons/oxygen/48x48/mimetypes
%dir %{_datadir}/icons/oxygen/64x64/mimetypes
%dir %{_datadir}/icons/oxygen/128x128/mimetypes
%dir %{_datadir}/icons/oxygen/256x256/mimetypes
%{_docdir}/%{name}-oxygen-icons
%{_datadir}/icons/oxygen/*/*/*.png

%files kde
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/ServiceMenus
%{_datadir}/kde4/services/ServiceMenus/bluej_open_project.desktop
%{_datadir}/kde4/services/ServiceMenus/bluej_open_folder.desktop

%changelog
* Wed Jan 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.6
- Rebuilt for Fedora
* Mon Apr  2 2012 schoett@gmx.de
- Added mime type text/x-bluej for BlueJ package files
- Added subpackage oxygen-icons
- Added subpackage kde
- Require java-sdk >= 1.6.0, because otherwise package
  java-1_5_0-gcj-compat-devel could get installed
* Tue May 10 2011 schoett@gmx.de
- Require java-sdk >= 1.5.0
- Removed unneeded dependencies
- build from deb archive
- Changed installation path
* Thu Apr 28 2011 schoett@gmx.de
- update to 304:
  + Changelog: http://www.bluej.org/help/changes.html
* Thu Jul 30 2009 lars@linux-schulserver.de
- Recommend new package bluej-extensions
* Mon Jul 27 2009 lars@linux-schulserver.de
- update to 251:
  + This release also collects some (anonymous) data about BlueJ
    use, such as BlueJ and Java versions, operating system and
    interface language
  + Added some control over the date formatting by the
    Submitter extension
  + Includes newer version of Svnkit library, should resolve
    some subversion issues
  + Fixed: "New Project", then selecting an existing project gave
    a bad error message
  + Improved cursor behaviour in editor slightly
  + Fixed: BlueJ launcher (Windows) sometimes gave a "MSVCR71.dll
    not found" error
  + Fixed: BlueJ launcher (Windows) fails when
    bluej.windows.vm.args changed
  + Fixed: Java ME projects fail to open on non-Windows OSes
  + Fixed: Couldn't open jar file via "Open non-BlueJ"
- remove specfile code for older distries
- added bluej-rpmlintrc
* Tue Apr 22 2008 lars@linux-schulserver.de
- initial version for openSUSE-Education
