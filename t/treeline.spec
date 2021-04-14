%undefine _debugsource_packages
Summary:	Versatile Tree-Style Outliner for Defining Custom Data Schemas
Name:		treeline
Version:	3.1.2
Release:	1
Group:		Productivity/Office/Other
License:	GPLv2+
URL:		http://treeline.bellz.org/
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-qt5, python-lxml
Requires:	python3-qt5

%description
TreeLine is a versatile tool for working with all kinds of information
that fit into a tree-like structure. TreeLine is written in Python and
uses the PyQt bindings to the Qt toolkit, which makes it very portable.

It can be used to edit bookmark files, create mini-databases (for
example, for addresses, tasks, records, or CDs), outline documents, or
just collect ideas. It can also be used as a generic editor for XML
files.

The data schemas for any node in the data tree can be customized and
new types of nodes can be defined. The way data is presented on the
screen, exported to HTML, or printed can be defined with HTML-like
templates. Plug-ins can be written to load and save data from and to
custom file formats or external data sources and extend the
functionality of TreeLine.

%prep
%setup -q -n TreeLine

%build

%install
rm -rf $RPM_BUILD_ROOT
for i in source/*.py; do
	sed -i "s|#!/usr/bin/env python|#!/usr/bin/python3|g" $i
	chmod 755 $i
done

python3 install.py -x \
	-p %{_prefix} \
	-d %{_defaultdocdir}/%{name} \
	-i %{_datadir}/%{name}/icons \
	-b $RPM_BUILD_ROOT

# Associate Files with MimeTypes (the KDE4/Gnome way)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages
cat > $RPM_BUILD_ROOT%{_datadir}/mime/packages/%{name}.xml << EOF
<?xml version="1.0"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-treeline">
    <comment>TreeLine File</comment>
    <glob pattern="*.trl"/>
    <glob pattern="*.TRL"/>
  </mime-type>
  <mime-type type="application/x-treeline-gz">
    <comment>Compressed TreeLine File</comment>
    <glob pattern="*.trl.gz"/>
    <glob pattern="*.TRL.GZ"/>
  </mime-type>
  <mime-type type="application/x-treepad">
    <comment>TreePad File</comment>
    <glob pattern="*.hjt"/>
    <glob pattern="*.HJT"/>
  </mime-type>
</mime-info>
EOF

# Menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=%{name}
Icon=%{name}
Name=TreeLine
GenericName=Outliner
Categories=Office;X-MandrivaLinux-Office-TasksManagement;
MimeType=application/x-treeline;application/x-treeline-gz;application/x-treepad;text/xml;
StartupNotify=true
Terminal=false
EOF

%files
%doc %{_defaultdocdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/treeline-icon.*

%changelog
* Tue May 12 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.2
- Rebuilt for Fedora
* Thu May 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.1-1
+ Revision: 800424
- imported package treeline
* Thu Jul 10 2008 TI_Eugene <ti.eugene@gmail.com>
- Init build at OBS
* Sun Apr 06 2008 joe@suse.de
- fix DOS EOL encoding in setup.py file
* Wed Feb 13 2008 joe@suse.de
- update to 1.1.10
- fix missing shebang and remove it from rpmlintrc exceptions
* Fri Nov 09 2007 lrupp@suse.de
- fix rpmlint errors
* Wed Aug 08 2007 joe@suse.de
- update to 1.1.9
- rewrite, moved to Qt 4.x and PyQt 4.x
- basic ODF support
* Fri Aug 25 2006 joe@suse.de
- update to 1.0.0
- fixed a problem with duplicate nodes showing up when pasting
  multiple nodes on Windows
- deriving types from other derived types is no longer allowed, since
  it did not function properly
- a problem with saving an encrypted file in the German version of
  TreeLine has been fixed
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Dec 20 2005 joe@suse.de
- update to 0.14.0
* Wed Sep 21 2005 joe@suse.de
- fixed non-matching string in German translation
* Mon Aug 29 2005 joe@suse.de
- update to 0.13.0
- German and French translations
* Mon Jul 11 2005 joe@suse.de
- update to 0.12.82a
- first version that is prepared for localization
* Wed May 04 2005 joe@suse.de
- update to 0.12.0
- SUSE-specific patches are not needed any more
- Desktop icon was missing; added one from the last release
* Sun Mar 13 2005 joe@suse.de
- removing plain text files from supported mime types in .desktop
  file
* Mon Feb 28 2005 joe@suse.de
- update to 0.11.1
- removing some SUSE-specific changes that are not necessary
  any more
* Tue Feb 08 2005 joe@suse.de
- update to 0.11.0
- SUSE improvements (KDE icons)
- .desktop files are included now
- fixed dependencies
* Fri Jan 28 2005 joe@suse.de
- update to 0.10.83
- patch for documentation directory not needed any more because of
  new option in install script
* Mon Jan 24 2005 joe@suse.de
- initial checkin of TreeLine
