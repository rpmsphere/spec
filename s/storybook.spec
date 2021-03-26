%undefine _missing_build_ids_terminate_build
%define __os_install_post %{nil}

Name:           storybook
License:        GPLv3
Group:          Productivity/Publishing
Summary:        Story Writing Software for Novelists, Authors and Creative Writers
Version:        4.0.9
Release:        1.bin
URL:            http://storybook.intertec.ch
Source0:        %{name}-%{version}-linux.bin
Requires:       jre
ExclusiveArch:  %ix86
AutoReqProv:    off

%description
StorYBook is a free, open source story writing software for creative
writers, novelists and authors that helps to keep the overview over
the strands when writing a book, a novel or a story.

StorYBook assists you in structuring your book. Have all your data
in one place. With StorYBook you can manage chapters, scenes,
characters and locations and assign them to the related scenes.

Authors
--------
  Martin Mustun
  Daniel Wall
  Werner Keil

%prep
%setup -T -c

%build
chmod +x %{SOURCE0}

%install
%{SOURCE0} --noexec --keep --target $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/jdic/lib/{sunos,windows}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# %{name} script

JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-Dfile.encoding=UTF-8 -splash:splash.png -XX:MaxPermSize=256m -Xmx400m -jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS lib/%{name}.jar
EOF

install -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Storybook 4
GenericName=Novel Writing Software
Comment=Open Source Novel Writing Software for Novelists, Authors and Creative Writers
Exec=storybook %f
Terminal=false
Type=Application
Icon=/usr/share/storybook/storybook-icon.png
Categories=Office;
MimeType=application/vnd.storybook
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Jan 20 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.9
- Rebuild binary package

* Mon Jun  1 2009 toms@suse.de
- Added missing log4j package in requires section. Thanks to Zonker!

* Sun May 31 2009 toms@suse.de
- Improved storybook script and included JPackage conventions
- Added diff files to reduce warnings
- Added .desktop and .png file to see it in main menu
- Added more dependencies to jakarta-commons-* packages

* Sat May 30 2009 toms@suse.de
- Added .desktop file
- Improved SPEC file
- Updated to version 2.1.12:
  * integrated the new logo
  * some translations has been updated
- Previous versions:
  2.1.11:
  * implemented "quick navigation" for chapters and scenes
  * most dialogs are non-modal now (don't prevent the workflow
    on the application anymore)
  * most windows are re-sizable now
  * after editing a scene, the refreshing is more accurate now
  * the dictionaries has been updates
  * added predefined color for strands and characters
  * added support for dark colors (strands and characters)
  * some labels and panels are pastel-colored now
  2.1.10:
  * added a so called "translator mode"
  * implemented feature request #2455821: Use JFreeChart for
    Statistics
  * implemented feature request #2363392: Improve adding
    character / locations links
  * improved refreshing mechanism
  * improved object tree
  * translated into Traditional Chinese
  * translated into Japanese
  2.1.9:
  * undo / redo is now supported for text areas and text fields
  * translated into Greek
  * improved object tree
  * fixed bug #2354336: Export of Character List fails
  * the French translation has been completed
  2.1.8:
  * a tree is used instead of the lists (characters, locations etc.)
  * the layout has been improved
  * characters can be grouped now (central characters and minor
    characters)
  * added Nimbus Look and Feel
  * implemented feature request #2174275: Notes for scenes,
    characters etc.
  * translated into Swedish
  2.1.7
  * implemented feature request #1881265: column order of strands
  * exported files can be opened directly now
  * implemented feature request #2174280: Task List
  * the manage lists for characters, locations etc. has been improved
  * French translation has been completed

* Sun Oct 19 2008 toms@suse.de
  Updated to version 2.1.5:
  * 2.1.5
  - bug fix: application didn't start under certain circumstances
  * 2.1.4
  - improved focus handling for dialogs
  - the information window can be resized now
  - implemented feature request #2043691: Save As
  - translated to Hebrew
  - implemented draft of feature request #2113136 to showing
    status based colors.
  - implemented feature request #2071595: Add character / location
    on scene dialog.
  - the location list shows the country now
  - implemented feature request #1936260: Location sorting
  - implemented plugin mechanism for jasper reports
  - updated H2 Database Engine to version 1.0.78 (2008-08-28)
  * 2.1.3
  - a time stamp has been added to export file names
  - added ODT export (OpenDocument Text, Open Office)
  - fixed bug #2049282: Text is cut off on export
  - updated H2 Database Engine to version 1.0.77 (2008-08-16)
  - added Dutch translation

* Tue Jan  1 2008 toms@suse.de
- First release of version 2.1.2
